"""Persistent memory access for A.R.I.A."""

import psycopg
from psycopg.rows import dict_row
from psycopg.types.json import Jsonb


DATABASE_NAME = "aria"


def _connect():
    """Open a local connection to A.R.I.A.'s PostgreSQL database."""
    return psycopg.connect(
        host="localhost",
        dbname=DATABASE_NAME,
        user="aria",
        row_factory=dict_row,
    )


def remember(content, memory_type, source=None, confidence=None, context=None):
    """Persist a memory and return its database ID."""
    with _connect() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO cognition.memory
                    (content, memory_type, source, confidence, context)
                VALUES
                    (%s, %s, %s, %s, %s)
                RETURNING id
                """,
                (
                    content,
                    memory_type,
                    source,
                    confidence,
                    Jsonb(context or {}),
                ),
            )
            return cursor.fetchone()["id"]


def recall_active():
    """Return all active memories, newest first."""
    with _connect() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT
                    id,
                    content,
                    memory_type,
                    source,
                    context,
                    confidence,
                    created_at,
                    updated_at
                FROM cognition.memory
                WHERE is_active = TRUE
                ORDER BY created_at DESC
                """
            )
            return cursor.fetchall()