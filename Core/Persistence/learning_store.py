"""Persistent storage bridge for qualified A.R.I.A. learning."""

from Core.Persistence.memory_store import remember


def retain_learning(
    content,
    source,
    confidence,
    context=None,
):
    """
    Persist learning that has already been qualified for retention.

    This layer does not decide whether something is true or deserves
    to be learned. That responsibility belongs to A.R.I.A.'s Learning
    and Memory reasoning architecture.
    """
    return remember(
        content=content,
        memory_type="learned_experience",
        source=source,
        confidence=confidence,
        context=context,
    )