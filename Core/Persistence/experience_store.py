"""Canonical Experience Ledger persistence for A.R.I.A."""

import json
import uuid
from datetime import datetime, timezone
from pathlib import Path

from jsonschema import Draft202012Validator
from psycopg.types.json import Jsonb

from Core.Persistence.memory_store import _connect


SCHEMA_PATH = (
    Path(__file__).resolve().parents[1]
    / "Schemas"
    / "experience.schema.json"
)

with SCHEMA_PATH.open("r", encoding="utf-8") as schema_file:
    EXPERIENCE_SCHEMA = json.load(schema_file)

_VALIDATOR = Draft202012Validator(EXPERIENCE_SCHEMA)


def _new_experience_id():
    """Create a canonical A.R.I.A. Experience Ledger identifier."""
    return f"exp_{uuid.uuid4()}"


def retain_experience(learning_result):
    """
    Persist an accepted learning result as a canonical Experience Ledger record.

    This function does not decide whether the learning should be retained.
    It persists learning only after the applicable reasoning and governance
    layers have authorized retention.
    """
    now = datetime.now(timezone.utc).isoformat()

    experience = {
        "experience_id": _new_experience_id(),
        "content": learning_result["content"],
        "learning_class": learning_result["learning_class"],
        "source": learning_result["source"],
        "source_ids": learning_result.get("source_ids", []),
        "confidence": {
            "value": learning_result["confidence"],
            "basis": learning_result["reasoning_summary"],
        } if learning_result["confidence"] is not None else None,
        "context": learning_result["context"],
        "generalization_scope": learning_result["generalization_scope"],
        "causal_state": learning_result["causal_state"],
        "supporting_evidence_ids": learning_result.get(
            "supporting_evidence_ids", []
        ),
        "supporting_case_ids": learning_result.get(
            "supporting_case_ids", []
        ),
        "contradicting_case_ids": learning_result.get(
            "contradicting_case_ids", []
        ),
        "restrictions": learning_result["restrictions"],
        "residual_uncertainty": learning_result.get(
            "residual_uncertainty", []
        ),
        "candidate_knowledge_claim": learning_result.get(
            "candidate_knowledge_claim"
        ),
        "reasoning_summary": learning_result["reasoning_summary"],
        "provenance": None,
        "created_at": now,
        "updated_at": now,
    }

    _VALIDATOR.validate(experience)

    with _connect() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO cognition.experience (
                    experience_id,
                    content,
                    learning_class,
                    source,
                    source_ids,
                    confidence,
                    context,
                    generalization_scope,
                    causal_state,
                    supporting_evidence_ids,
                    supporting_case_ids,
                    contradicting_case_ids,
                    restrictions,
                    residual_uncertainty,
                    candidate_knowledge_claim,
                    reasoning_summary,
                    provenance,
                    created_at,
                    updated_at
                )
                VALUES (
                    %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                )
                """,
                (
                    experience["experience_id"],
                    experience["content"],
                    experience["learning_class"],
                    experience["source"],
                    Jsonb(experience["source_ids"]),
                    Jsonb(experience["confidence"]),
                    Jsonb(experience["context"]),
                    experience["generalization_scope"],
                    experience["causal_state"],
                    Jsonb(experience["supporting_evidence_ids"]),
                    Jsonb(experience["supporting_case_ids"]),
                    Jsonb(experience["contradicting_case_ids"]),
                    Jsonb(experience["restrictions"]),
                    Jsonb(experience["residual_uncertainty"]),
                    experience["candidate_knowledge_claim"],
                    experience["reasoning_summary"],
                    Jsonb(experience["provenance"]),
                    experience["created_at"],
                    experience["updated_at"],
                ),
            )

    return experience["experience_id"]