# A.R.I.A. Relationship Architecture

**Document Type:** Canonical Knowledge and Reasoning Specification  
**Authority:** Subordinate to `Core/Schemas/entity_contracts.json`, `Core/Registries/relationship_types.json`, and `Core/Persona/ARIA_CONSTITUTION.md`  
**Version:** 1.0

---

## 1. Purpose

This document defines how A.R.I.A. represents, interprets, validates, traverses, and learns relationships between canonical entities.

Entities establish what concepts exist.

Relationships establish how those concepts interact.

A.R.I.A.'s technical reasoning depends heavily upon the precision, context, provenance, validation, and temporal applicability of those relationships.

Relationships are therefore first-class semantic objects.

A.R.I.A. distinguishes two related but separate structures:

1. **Semantic Relationships** — identified by `rel_<UUID>`.
2. **Knowledge Graph Edges** — identified by `ke_<UUID>`.

These objects may correspond to one another, but they are not interchangeable.

---

## 2. Canonical Authority

Relationship architecture is governed by the following hierarchy:

1. `Core/Schemas/entity_contracts.json`
2. `Core/Registries/relationship_types.json`
3. `Core/Schemas/relationships.schema.json`
4. this document

The relationship-type Registry is the authoritative vocabulary for relationship semantics.

This document shall not independently establish competing relationship-type names.

---

## 3. Semantic Relationships

A semantic relationship is a first-class assertion connecting two canonical A.R.I.A. entities.

Conceptually:

```text
SOURCE ENTITY
    |
    | RELATIONSHIP TYPE
    v
TARGET ENTITY
