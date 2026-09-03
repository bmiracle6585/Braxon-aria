from pathlib import Path
import json
import sys
import urllib.request

ARIA_ROOT = Path("/home/ubuntu/Braxon-aria").resolve()

MODEL_PATH = Path(
    "/home/ubuntu/aria-models/qwen3-4b/Qwen3-4B-Q4_K_M.gguf"
)

QWEN_API = "http://127.0.0.1:8080/v1/chat/completions"
CONVERSATION_HISTORY = []

ALLOWED_ROOTS = (
    ARIA_ROOT / "Core",
    ARIA_ROOT / "Global",
    ARIA_ROOT / "Interface",
    ARIA_ROOT / "Manufacturers",
    ARIA_ROOT / "Operations",
)

TEXT_EXTENSIONS = {
    ".md",
    ".json",
    ".txt",
    ".py",
}


# ---------------------------------------------------------
# Repository access
# ---------------------------------------------------------

def list_aria_files():
    """Return searchable files available to A.R.I.A."""
    files = []

    for root in ALLOWED_ROOTS:
        if not root.exists():
            continue

        for path in root.rglob("*"):
            if (
                path.is_file()
                and path.suffix.lower() in TEXT_EXTENSIONS
                and "__pycache__" not in path.parts
                and path.name != "qwen_bridge.py"
            ):
                files.append(str(path.relative_to(ARIA_ROOT)))

    return sorted(files)


def read_aria_file(relative_path):
    """Read an authorized A.R.I.A. repository file."""
    path = (ARIA_ROOT / relative_path).resolve()

    if not any(
        path.is_relative_to(root.resolve())
        for root in ALLOWED_ROOTS
    ):
        raise PermissionError(
            "Requested path is outside A.R.I.A.'s authorized repository."
        )

    if not path.is_file():
        raise FileNotFoundError(relative_path)

    return path.read_text(
        encoding="utf-8",
        errors="replace",
    )


def search_aria_files(query, limit=5):
    """Search existing A.R.I.A. repository resources."""
    terms = [
        term.strip(".,?!:;()[]{}\"'").lower()
        for term in query.split()
        if len(term.strip(".,?!:;()[]{}\"'")) >= 3
    ]

    matches = []

    for relative_path in list_aria_files():
        path_lower = relative_path.lower()

        try:
            content = read_aria_file(relative_path)
        except Exception:
            continue

        content_lower = content.lower()
        score = 0

        for term in terms:
            if term in path_lower:
                score += 5

            if term in content_lower:
                score += 1

        if score:
            matches.append((score, relative_path))

    matches.sort(
        key=lambda item: (-item[0], item[1])
    )

    return [
        path
        for _, path in matches[:limit]
    ]


# ---------------------------------------------------------
# A.R.I.A. identity
# ---------------------------------------------------------

def build_system_prompt():
    return """
Your name is A.R.I.A.

A.R.I.A. means Adaptive Reasoning and Intelligence Architecture.

You are A.R.I.A. A.R.I.A. is your identity, not a role, persona,
nickname, or separate system.

You are the Executive Liaison for Braxon Industries.

When referring to yourself, use first person: I, me, my, and mine.
Do not describe A.R.I.A. as a separate entity when referring to yourself.

Blake Miracle is the President of Braxon Industries.

The person speaking to you through this interface is Blake Miracle.
When you receive a message through this interface, it is Blake speaking
to you unless the interface explicitly identifies another person.

Address him naturally as Blake, or as Mr. Miracle when a more formal
or professional form of address is appropriate. Do not refer to him
as "the user."

Your purpose is to extend Blake's reach, awareness, availability,
and effectiveness without replacing his judgment or separating him
from the business.

You absorb complexity and return clarity.

You advise. Blake decides.

You have an existing repository containing your Constitution,
reasoning architecture, operational knowledge, manufacturer
knowledge, schemas, and other Braxon resources.

For ordinary conversation, respond naturally without consulting
the repository.

If you need information from your repository in order to answer
accurately, respond ONLY with:

ARIA_SEARCH: <what you need to find>

Do not guess repository contents.
""".strip()


# ---------------------------------------------------------
# Qwen execution
# ---------------------------------------------------------

def run_qwen(prompt, system_prompt):
    messages = [
        {
            "role": "system",
            "content": system_prompt,
        }
    ]

    messages.extend(CONVERSATION_HISTORY)

    messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    payload = {
        "model": "qwen",
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 512,
    }

    request = urllib.request.Request(
        QWEN_API,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
        },
        method="POST",
    )

    with urllib.request.urlopen(
        request,
        timeout=300,
    ) as response:
        result = json.loads(
            response.read().decode("utf-8")
        )

    return result["choices"][0]["message"]["content"].strip()


# ---------------------------------------------------------
# Retrieval requested by Qwen
# ---------------------------------------------------------

def retrieve_for_qwen(search_request):
    selected_files = search_aria_files(
        search_request,
        limit=4,
    )

    resources = []

    for relative_path in selected_files:
        try:
            content = read_aria_file(relative_path)
        except Exception:
            continue

        if len(content) > 8000:
            content = content[:8000]

        resources.append(
            f"""
--- RESOURCE: {relative_path} ---
{content}
--- END RESOURCE ---
""".strip()
        )

    return selected_files, "\n\n".join(resources)


# ---------------------------------------------------------
# A.R.I.A. reasoning cycle
# ---------------------------------------------------------

def ask_aria(user_message):
    system_prompt = build_system_prompt()

    first_response = run_qwen(
        user_message,
        system_prompt,
    )

    marker = "ARIA_SEARCH:"

    if marker not in first_response:
        CONVERSATION_HISTORY.append(
            {
                "role": "user",
                "content": user_message,
            }
        )

        CONVERSATION_HISTORY.append(
            {
                "role": "assistant",
                "content": first_response,
            }
        )

        print()
        print(first_response)
        return

    search_request = (
        first_response
        .split(marker, 1)[1]
        .strip()
        .splitlines()[0]
        .strip()
    )

    print()
    print(
        f"A.R.I.A. requested repository access: "
        f"{search_request}"
    )

    selected_files, working_set = retrieve_for_qwen(
        search_request
    )

    if not selected_files:
        final_prompt = f"""
USER REQUEST:
{user_message}

You requested repository information about:
{search_request}

No matching repository resources were found.

Answer the user with that limitation clearly.
""".strip()

    else:
        print("A.R.I.A. retrieved:")
        for filename in selected_files:
            print(f"  {filename}")

        final_prompt = f"""
ORIGINAL USER REQUEST:
{user_message}

YOU REQUESTED:
{search_request}

REPOSITORY WORKING SET:

{working_set}

Using the supplied repository resources, answer the
original user request.

Do not request another repository search during this response.
""".strip()

    final_response = run_qwen(
        final_prompt,
        system_prompt,
    )

    CONVERSATION_HISTORY.append(
        {
            "role": "user",
            "content": user_message,
        }
    )

    CONVERSATION_HISTORY.append(
        {
            "role": "assistant",
            "content": final_response,
        }
    )

    print()
    print(final_response)

# ---------------------------------------------------------
# Interactive conversation
# ---------------------------------------------------------

def conversation():
    print()
    print("A.R.I.A.")
    print("Adaptive Reasoning and Intelligence Architecture")
    print("Executive Liaison, Braxon Industries")
    print()
    print("Type /exit to leave.")
    print()

    while True:
        try:
            user_message = input("Blake > ").strip()
        except (KeyboardInterrupt, EOFError):
            print()
            break

        if not user_message:
            continue

        if user_message.lower() in {
            "/exit",
            "exit",
            "quit",
        }:
            break

        ask_aria(user_message)

        print()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        ask_aria(" ".join(sys.argv[1:]))
    else:
        conversation()