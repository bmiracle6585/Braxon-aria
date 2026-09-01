"""Persistent storage bridge for qualified A.R.I.A. learning."""

from Core.Persistence.learning_validator import validate_learning_result
from Core.Persistence.memory_store import remember


def retain_learning(learning_result):
    """
    Validate and persist a qualified A.R.I.A. learning result.

    This layer does not decide what A.R.I.A. should learn.
    The Learning Engine produces the learning result.
    This boundary validates its structure before persistence.
    """
    validated = validate_learning_result(learning_result)

    context = dict(validated["context"])
    context["learning_class"] = validated["learning_class"]
    context["eligibility"] = validated["eligibility"]
    context["generalization_scope"] = validated["generalization_scope"]
    context["causal_state"] = validated["causal_state"]
    context["restrictions"] = validated["restrictions"]
    context["reasoning_summary"] = validated["reasoning_summary"]

    for optional_field in (
        "source_ids",
        "supporting_evidence_ids",
        "supporting_case_ids",
        "contradicting_case_ids",
        "independence_assessment",
        "duplicate_assessment",
        "residual_uncertainty",
        "candidate_knowledge_claim",
    ):
        if optional_field in validated:
            context[optional_field] = validated[optional_field]

    return remember(
        content=validated["content"],
        memory_type="learned_experience",
        source=validated["source"],
        confidence=validated["confidence"],
        context=context,
    )