# A.R.I.A. Relationship Schema

**Document Type:** Cognitive Knowledge Data Specification  
**Authority:** Subordinate to `Core/Knowledge/knowledge_graph.md`, `Core/Knowledge/entity_schema.md`, and `Core/Persona/ARIA_CONSTITUTION.md`  
**Version:** 0.1

---

## 1. Purpose

This document defines how relationships between entities are represented within A.R.I.A.'s Canonical Knowledge Graph.

Entities establish what concepts exist.

Relationships establish how those concepts interact.

A.R.I.A.'s reasoning capability depends heavily upon the quality, precision, context, and provenance of these relationships.

A relationship shall therefore be treated as a first-class knowledge object rather than as an incidental property of an entity.

---

## 2. Relationship Structure

A relationship connects a source entity to a target entity through a defined relationship type.

Conceptually:

SOURCE ENTITY
→ RELATIONSHIP TYPE
→ TARGET ENTITY

Example:

Incorrect Flex Routing
→ CAN_CAUSE
→ RSL Discrepancy

A relationship may additionally contain:

- context;
- applicability;
- directionality;
- strength;
- confidence;
- source provenance;
- validation state;
- effective dates;
- revision applicability;
- conditional requirements; and
- supporting or contradicting evidence.

---

## 3. Stable Relationship Identity

Every canonical relationship shall have a stable unique identifier.

Example:

`REL-00001482`

Relationship IDs shall not encode mutable technical meaning.

Avoid identifiers such as:

`NOKIA-UBTT-FLEX-CAUSES-RSL`

The entities and relationship type contain the meaning.

The relationship ID provides permanent identity.

---

## 4. Required Relationship Fields

Every canonical relationship shall contain at minimum:

### 4.1 Relationship ID

Stable unique identifier.

Example:

`REL-00001482`

### 4.2 Source Entity

The canonical entity from which the relationship originates.

Example:

`Incorrect Flex Routing`

### 4.3 Relationship Type

The semantic meaning of the connection.

Example:

`CAN_CAUSE`

### 4.4 Target Entity

The canonical entity to which the relationship points.

Example:

`RSL Discrepancy`

### 4.5 Status

Initial states should include:

- PROPOSED
- ACTIVE
- DEPRECATED
- SUPERSEDED
- REJECTED

### 4.6 Validation State

Initial states should include:

- UNREVIEWED
- REVIEWED
- VALIDATED
- DISPUTED
- REJECTED

Status and validation state shall remain distinct.

---

## 5. Relationship Types

Relationship types shall come from an approved registry.

Initial types may include:

### Classification

- IS_A
- INSTANCE_OF
- VARIANT_OF
- PART_OF
- BELONGS_TO

### Manufacturer and Product

- MANUFACTURED_BY
- MANUFACTURES
- SUPERSEDES
- COMPATIBLE_WITH
- INCOMPATIBLE_WITH

### Physical Relationships

- CONNECTED_TO
- MATES_WITH
- INTERFACES_WITH
- INSTALLED_ON
- CONTAINS
- FEEDS
- RECEIVES_FROM

### Configuration

- CONFIGURED_AS
- REQUIRES_CONFIGURATION
- SUPPORTS_CONFIGURATION
- DEPENDS_ON
- REQUIRES

### RF and Engineering

- OPERATES_AT
- MEASURED_BY
- MEASURED_IN
- AFFECTS
- CAN_AFFECT
- INCREASES
- DECREASES

### Diagnostic

- CAN_CAUSE
- CAN_INDICATE
- SUPPORTS
- CONTRADICTS
- ELIMINATED_BY
- CONFIRMED_BY
- TESTED_BY
- VERIFIED_BY

### Procedure and Resolution

- PRECEDES
- REQUIRES_TEST
- CORRECTED_BY
- RESOLVED_BY
- PRODUCES
- EXPECTED_TO_PRODUCE

### Applicability

- APPLIES_TO
- LIMITED_TO
- EXCLUDED_FROM

The registry may expand as A.R.I.A.'s knowledge develops.

---

## 6. Relationship Semantics Must Be Precise

Relationship types shall have defined meanings.

A.R.I.A. shall avoid using a generic relationship when a precise relationship exists.

For example:

Incorrect Flex Routing
`RELATED_TO`
RSL Discrepancy

contains little reasoning value.

Prefer:

Incorrect Flex Routing
`CAN_CAUSE`
RSL Discrepancy

Precision allows the graph to support reasoning rather than merely association.

---

## 7. Directionality

Relationships may be:

- DIRECTED;
- BIDIRECTIONAL; or
- SYMMETRIC.

Example of directed relationship:

UBT-T
`MANUFACTURED_BY`
Nokia

does not mean:

Nokia
`MANUFACTURED_BY`
UBT-T

Example of symmetric relationship:

Component A
`COMPATIBLE_WITH`
Component B

may imply:

Component B
`COMPATIBLE_WITH`
Component A

when the relationship definition explicitly establishes symmetry.

Directionality shall be defined by the relationship-type registry.

---

## 8. Inverse Relationships

A relationship type may define an inverse.

Example:

UBT-T
`MANUFACTURED_BY`
Nokia

Inverse:

Nokia
`MANUFACTURES`
UBT-T

The system may derive inverse traversal without requiring duplicate authoritative relationship records.

Where possible, one canonical relationship should support traversal in both semantic directions through its defined inverse.

This reduces unnecessary duplication.

---

## 9. Relationship Context

Relationships may apply only within specific contexts.

Possible context dimensions include:

- manufacturer;
- product family;
- product;
- product variant;
- hardware revision;
- firmware;
- software version;
- frequency band;
- configuration;
- topology;
- scope of work;
- project phase;
- environment;
- customer;
- effective date; and
- geographic or regulatory domain.

Example:

RELATIONSHIP:

Component X
`MATES_WITH`
Component Y

CONTEXT:

Product:
UBT-T

Hardware Revision:
Rev C and later

A.R.I.A. shall not assume the relationship applies outside that context.

---

## 10. Context Is Not Duplication

A.R.I.A. should not create multiple identical relationships merely because the same relationship applies in several contexts.

Where practical, one relationship may reference multiple applicable contexts.

However, separate relationships may be appropriate when:

- provenance differs;
- technical behavior differs;
- confidence differs;
- effective dates differ;
- relationship strength differs; or
- the relationship has materially different conditions.

The objective is accurate representation rather than artificial deduplication.

---

## 11. Deterministic Relationships

Some relationships represent established technical facts.

Example:

UBT-T
`MANUFACTURED_BY`
Nokia

These relationships may not require a probability value.

They still require:

- provenance;
- applicability;
- validation; and
- revision awareness.

A.R.I.A. shall not force probabilistic semantics onto deterministic technical facts.

---

## 12. Probabilistic Relationships

Other relationships represent possibilities rather than certainty.

Example:

Incorrect Flex Routing
`CAN_CAUSE`
RSL Discrepancy

This relationship indicates technical possibility.

Its relevance in a current diagnostic case may depend upon:

- historical frequency;
- current evidence;
- configuration;
- topology;
- product;
- scope;
- user-specific history; and
- contextual similarity.

The canonical relationship shall not be confused with the current diagnostic probability.

---

## 13. Relationship Strength

A relationship may carry a strength value when meaningful.

Relationship strength represents the strength of the technical or statistical association under the applicable context.

It shall not automatically represent:

- current-case probability;
- evidence confidence;
- route priority; or
- source authority.

These concepts remain separate.

For example:

RELATIONSHIP STRENGTH:
0.82

may describe a strong conditional association.

CURRENT CASE PROBABILITY:
0.46

may still differ substantially after current evidence is evaluated.

---

## 14. Confidence

Relationship confidence describes how strongly A.R.I.A. trusts that the relationship itself is valid.

Confidence may depend upon:

- source authority;
- number of supporting sources;
- validation;
- contextual consistency;
- historical support;
- expert review;
- contradictory evidence; and
- revision applicability.

A technically strong relationship with poor source support may have lower confidence.

---

## 15. Provenance

Every material relationship should preserve provenance.

Possible provenance sources include:

- manufacturer documentation;
- engineering specification;
- industry standard;
- Braxon procedure;
- approved human contribution;
- validated field discovery;
- imported structured data;
- legacy A.R.I.A. knowledge; and
- model-generated candidate.

Conceptually:

RELATIONSHIP:
Incorrect Flex Routing
CAN_CAUSE
RSL Discrepancy

SOURCE:
Nokia document XYZ

SOURCE LOCATION:
Section 7.4

REVISION:
3.2

VALIDATED BY:
...

A.R.I.A. should be capable of retrieving the evidence supporting the relationship.

---

## 16. Multiple Sources

A relationship may be supported by multiple sources.

The relationship should exist once when the technical assertion is the same.

Supporting sources should reference that relationship.

Example:

REL-000142

supported by:

SOURCE-001
Manufacturer manual

SOURCE-047
Braxon procedure

SOURCE-218
Validated engineering review

A.R.I.A. shall not create three duplicate relationships merely because three sources support the same technical assertion.

---

## 17. Independent Corroboration

Multiple sources do not necessarily represent independent evidence.

If several documents repeat information originating from the same technical bulletin, A.R.I.A. should preserve their common origin where known.

Source count alone shall not determine relationship confidence.

---

## 18. Contradictory Relationships

A.R.I.A. shall permit contradictory technical claims to coexist while they are unresolved.

Example:

SOURCE A:

Product X
`REQUIRES`
Configuration Y

SOURCE B:

Product X
`REQUIRES`
Configuration Z

A.R.I.A. shall preserve both claims with their:

- source;
- authority;
- revision;
- context;
- effective date;
- validation state; and
- contradiction status.

The system shall not silently discard one claim.

---

## 19. Relationship Conditions

Some relationships are true only when specific conditions exist.

Example:

CONDITION:

2+0 Diversity configuration active

RELATIONSHIP:

Incorrect Diversity Flex Routing
`CAN_CAUSE`
Diversity RSL Discrepancy

Conditional relationships shall preserve their required conditions.

This prevents technically valid knowledge from being applied to irrelevant configurations.

---

## 20. Negative Relationships

A.R.I.A. shall support meaningful negative relationships.

Examples:

Product X
`INCOMPATIBLE_WITH`
Component Y

Configuration A
`EXCLUDED_FROM`
Firmware B

Condition X
`CONTRADICTS`
Hypothesis Y

Absence of a positive relationship shall not automatically imply a negative relationship.

Negative knowledge must be explicitly supported.

---

## 21. Temporal Relationships

Relationships may change over time.

A relationship may contain:

- effective date;
- expiration date;
- superseded date;
- applicable revision range; and
- historical validity.

Example:

Firmware 4.2
`SUPPORTS_CONFIGURATION`
Feature X

Firmware 5.0
`SUPERSEDES`
Firmware 4.2

A historical case involving Firmware 4.2 must continue using relationships applicable at that time.

---

## 22. Relationship Validation

Relationships may progress through validation states.

Example lifecycle:

PROPOSED
↓
REVIEWED
↓
VALIDATED

or:

PROPOSED
↓
REJECTED

A relationship proposed by a language model or extraction engine shall not automatically become validated canonical knowledge.

---

## 23. Human Review

During early A.R.I.A. development, newly extracted relationships should normally enter a human-review queue.

Review should allow:

- approve;
- reject;
- edit;
- merge;
- add context;
- change relationship type;
- attach source;
- identify contradiction; and
- request additional evidence.

Human review decisions should themselves be preserved for auditability and future extraction improvement.

---

## 24. Relationship Supersession

A relationship may be superseded without deletion.

Example:

OLD RELATIONSHIP:
Procedure A
REQUIRES
Step X

NEW RELATIONSHIP:
Procedure A
REQUIRES
Step Y

The old relationship may remain historically valid for an earlier revision.

Supersession shall preserve historical reasoning capability.

---

## 25. Relationship Deprecation

A deprecated relationship remains available for:

- historical cases;
- older equipment;
- prior firmware;
- audit;
- revision comparison; and
- knowledge evolution.

Deprecated shall not automatically mean false.

---

## 26. Relationship Usage in Diagnostic Reasoning

The diagnostic engine may traverse relationships to construct candidate hypotheses.

Example:

CURRENT SYMPTOM:
Diversity RSL Discrepancy

Traversal may identify:

Incorrect Flex Routing
`CAN_CAUSE`
Diversity RSL Discrepancy

Incorrect Radio Configuration
`CAN_CAUSE`
Diversity RSL Discrepancy

Cross Polarization
`CAN_CAUSE`
RSL Discrepancy

Radio Failure
`CAN_CAUSE`
RSL Discrepancy

These relationships establish candidate possibilities.

The Probability Model then evaluates their current likelihood.

The Diagnostic Routing Engine determines what to investigate next.

---

## 27. Relationship Usage in Evidence Reasoning

Evidence may activate or affect graph relationships.

Example:

EVIDENCE:
Main RSL normal

EVIDENCE:
Diversity RSL low

These observations may:

- strengthen diversity-specific relationships;
- weaken common-path relationships;
- suppress environmental routes; and
- increase the diagnostic relevance of Diversity RF Chain relationships.

The canonical relationships themselves need not change.

Their relevance to the active case changes.

---

## 28. Relationship Usage in Experience

Experience Ledger cases shall reference canonical relationships when appropriate.

Example:

CASE EXP-0001847

CONFIRMED RELATIONSHIP OBSERVED:

Incorrect Radio B Configuration
`CAN_CAUSE`
RSL Discrepancy

The case becomes historical evidence supporting the relationship.

The case does not require creation of a duplicate relationship.

---

## 29. Learned Relationships

Repeated validated experience may reveal a relationship not currently represented in canonical knowledge.

Example:

A.R.I.A. observes across many validated cases that:

Condition X
appears associated with
Failure Y

The system may create:

PROPOSED RELATIONSHIP

Condition X
`CAN_INDICATE`
Failure Y

SOURCE:
Experience-derived

The relationship shall enter the applicable validation process before becoming authoritative canonical knowledge.

A.R.I.A. may discover knowledge.

She shall not silently promote correlation into technical truth.

---

## 30. Correlation Is Not Causation

A.R.I.A. shall distinguish:

`ASSOCIATED_WITH`

from:

`CAN_CAUSE`

Historical co-occurrence alone does not establish causality.

For example:

Weather Event
`ASSOCIATED_WITH`
RSL Degradation

does not automatically establish:

Weather Event
`CAUSED`
RSL Degradation

A causal relationship requires sufficient technical or validated evidentiary support.

---

## 31. Relationship Traversal Constraints

A.R.I.A. shall not blindly traverse every relationship connected to an entity.

Traversal may be constrained by:

- relationship type;
- current context;
- product applicability;
- manufacturer;
- active scope;
- evidence;
- route relevance;
- validation state;
- authority;
- graph depth; and
- computational budget.

This prevents irrelevant graph expansion during reasoning.

---

## 32. Relationship Depth

Some diagnostic conclusions may require multiple graph hops.

Example:

Diversity RSL Low
← CAN_BE_CAUSED_BY
Incorrect Flex Routing
→ INVOLVES
Diversity Flex
→ CONNECTED_TO
OCM Diversity Port
→ INTERFACES_WITH
AIM
→ INTERFACES_WITH
UBT-T
→ MANUFACTURED_BY
Nokia

A.R.I.A. shall support multi-hop reasoning without assuming every connected node is equally relevant.

---

## 33. Relationship Weighting Is Contextual

The same canonical relationship may have different diagnostic significance in different cases.

Example:

Incorrect Flex Routing
`CAN_CAUSE`
RSL Discrepancy

may be highly relevant when:

- Diversity path alone is degraded;
- applicable flex architecture exists; and
- the system was recently installed.

The same relationship may have very low current relevance when:

- the equipment has no applicable flex architecture; or
- both Main and Diversity degraded simultaneously.

The relationship remains technically valid.

Its current reasoning weight changes.

---

## 34. Relationship Auditability

A.R.I.A. shall preserve significant changes to canonical relationships.

Audit history should support:

- created;
- modified;
- validated;
- rejected;
- deprecated;
- superseded;
- merged;
- context changed;
- source added;
- source removed; and
- confidence changed.

A.R.I.A.'s technical knowledge shall not change invisibly.

---

## 35. Database Readiness

The relationship architecture should map cleanly to structured storage.

Conceptually, a relationship record may eventually contain:

- id;
- source_entity_id;
- relationship_type_id;
- target_entity_id;
- status;
- validation_state;
- strength;
- confidence;
- effective_at;
- expires_at;
- superseded_by;
- created_at;
- updated_at;
- created_by;
- updated_by.

Additional structures should represent:

- relationship context;
- provenance;
- supporting sources;
- contradictory sources;
- conditions;
- historical evidence; and
- audit history.

These should not be collapsed into a single unqueryable text field.

---

## 36. Model Independence

The language model may:

- identify candidate relationships;
- resolve natural-language descriptions;
- suggest relationship types;
- explain graph connections;
- propose contextual applicability; and
- discover possible missing relationships.

The language model shall not be the authoritative storage location for relationships.

The relationship graph shall remain intact when the language model is replaced.

---

## 37. Design Objective

A.R.I.A.'s intelligence shall emerge substantially from her ability to understand relationships.

Knowing that:

`UBT-T`

exists is useful.

Knowing that:

`UBT-T`
`MANUFACTURED_BY`
`Nokia`

is better.

Knowing how:

`UBT-T`
connects through its applicable interfaces, configurations, measurements, failure modes, procedures, symptoms, tests, historical outcomes, and user experience

creates the topology required for reasoning.

A.R.I.A. shall therefore treat relationships as foundational cognitive infrastructure.

The objective is not merely to know things.

The objective is to understand how those things connect.
