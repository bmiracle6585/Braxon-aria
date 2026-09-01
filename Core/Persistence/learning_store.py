"""Persistence bridge for qualified A.R.I.A. learning."""

from Core.Persistence.experience_store import retain_experience
from Core.Persistence.learning_validator import validate_learning_result


def retain_learning(learning_result):
    """
    Validate and persist an authorized A.R.I.A. learning result.

    Learning determines what the experience means.
    Retention authorization occurs before this persistence boundary.
    Accepted learning is stored in the canonical Experience Ledger.
    """
    validated = validate_learning_result(learning_result)
    return retain_experience(validated)