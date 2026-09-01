"""Validation boundary for A.R.I.A. learning results."""

import json
from pathlib import Path

from jsonschema import Draft202012Validator


SCHEMA_PATH = (
    Path(__file__).resolve().parents[1]
    / "Schemas"
    / "learning.schema.json"
)


with SCHEMA_PATH.open("r", encoding="utf-8") as schema_file:
    LEARNING_SCHEMA = json.load(schema_file)


_VALIDATOR = Draft202012Validator(LEARNING_SCHEMA)


def validate_learning_result(learning_result):
    """
    Validate a proposed learning result against A.R.I.A.'s
    authoritative learning schema.

    Returns the unchanged learning result when valid.
    Raises jsonschema.ValidationError when invalid.
    """
    _VALIDATOR.validate(learning_result)
    return learning_result