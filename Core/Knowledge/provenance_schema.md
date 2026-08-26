# A.R.I.A. Knowledge Provenance Schema

**Document Type:** Cognitive Knowledge Data Specification  
**Authority:** Subordinate to `Core/Knowledge/knowledge_graph.md` and `Core/Persona/ARIA_CONSTITUTION.md`  
**Version:** 0.1

---

## 1. Purpose

This document defines how A.R.I.A. records and preserves the origin of technical knowledge.

A.R.I.A. shall maintain sufficient provenance to distinguish between:

- what a source explicitly states;
- what A.R.I.A. extracted from that source;
- what a human approved;
- what A.R.I.A. inferred;
- what historical experience suggests;
- what has been superseded;
- and what remains uncertain.

A.R.I.A. shall not treat knowledge as authoritative merely because it exists within her systems.

Knowledge must retain its lineage.

---

## 2. Fundamental Provenance Principle

For material technical knowledge, A.R.I.A. should be capable of answering:

**What do I believe?**

**Why do I believe it?**

**Where did the information originate?**

**How authoritative is the source?**

**What revision or version did it come from?**

**Under what context does it apply?**

**Has it been reviewed or validated?**

**Has anything newer superseded it?**

The language model shall not reconstruct provenance from memory.

Provenance shall be stored as structured data.

---

## 3. Sources Are First-Class Objects

A source shall have its own stable identity.

Example:

SOURCE ID:
SRC-00000427

SOURCE TYPE:
MANUFACTURER_MANUAL

TITLE:
Nokia Wavence UBT-T Installation Manual

MANUFACTURER:
Nokia

DOCUMENT REVISION:
...

PUBLICATION DATE:
...

INGESTED DATE:
...

STATUS:
ACTIVE
