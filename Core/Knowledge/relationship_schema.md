# A.R.I.A. Relationship Architecture

**Document Type:** Canonical Knowledge and Reasoning Specification  
**Authority:** Subordinate to `Core/Schemas/entity_contracts.json`, `Core/Registries/relationship_types.json`, `Core/Schemas/relationships.schema.json`, and `Core/Persona/ARIA_CONSTITUTION.md`  
**Version:** 1.0

---

## 1. Purpose

This document defines how A.R.I.A. represents, interprets, validates, traverses, and learns relationships between canonical entities.

Entities establish what concepts exist.

Relationships establish how those concepts interact.

A.R.I.A.'s technical reasoning depends upon the precision, context, provenance, validation, and temporal applicability of those relationships.

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
4. This document

`Core/Registries/relationship_types.json` is the authoritative vocabulary for relationship semantics.

This document shall not independently establish competing relationship-type names.

If A.R.I.A. requires a relationship type that does not exist in the Registry, the Registry must be deliberately extended rather than allowing another file to invent a parallel vocabulary.

---

## 3. Semantic Relationships

A semantic relationship is a first-class assertion connecting two canonical A.R.I.A. entities.

Conceptually:

    SOURCE ENTITY
        |
        | RELATIONSHIP TYPE
        v
    TARGET ENTITY

Example:

    Incorrect Flex Routing
        |
        | CAN_CAUSE
        v
    RSL Discrepancy

A persisted semantic relationship uses:

    rel_<UUID>

A semantic relationship may participate in:

- canonical technical knowledge;
- diagnostic reasoning;
- evidence reasoning;
- experience;
- learning;
- source interpretation;
- configuration reasoning;
- procedural reasoning; or
- other technical contexts.

Not every semantic relationship belongs in the permanent Knowledge Graph.

---

## 4. Knowledge Graph Edges

A Knowledge Graph edge is a persisted graph structure representing reusable technical knowledge.

A Knowledge Graph edge uses:

    ke_<UUID>

Conceptually:

    KNOWLEDGE NODE
          |
          | KNOWLEDGE EDGE
          v
    KNOWLEDGE NODE

Knowledge Graph edges support efficient traversal and reusable technical graph structure.

They are distinct from semantic relationship records.

A semantic relationship may reference a corresponding Knowledge Graph edge.

A Knowledge Graph edge may embody a canonical semantic relationship.

Neither identity replaces the other.

---

## 5. Why `rel_` and `ke_` Are Separate

Not every meaningful relationship belongs permanently in the reusable Knowledge Graph.

For example:

    evd_<UUID>
        |
        | SUPPORTS
        v
    hyp_<UUID>

may be a legitimate first-class semantic relationship within a diagnostic case.

It does not necessarily belong in the permanent reusable technical Knowledge Graph.

By contrast:

    Incorrect Flex Routing
        |
        | CAN_CAUSE
        v
    RSL Discrepancy

may represent reusable technical knowledge suitable for persistence in the Knowledge Graph.

Therefore:

    rel_<UUID>

represents a semantic relationship assertion.

And:

    ke_<UUID>

represents persisted reusable graph structure.

This separation prevents case-specific reasoning state from polluting canonical technical knowledge.

---

## 6. Stable Relationship Identity

Every persisted semantic relationship shall have a stable unique identifier:

    rel_<UUID>

UUIDv7 is preferred according to the canonical entity contract.

Example:

    rel_018f3f3c-7f63-77f1-a9cc-61216e6f4179

Relationship identifiers shall not encode mutable technical meaning.

Do not create identifiers such as:

    NOKIA-UBTT-FLEX-CAUSES-RSL

The source entity, relationship type, target entity, context, and provenance contain the meaning.

The relationship identifier provides permanent identity.

Knowledge Graph edges independently use:

    ke_<UUID>

A `rel_<UUID>` identifier shall never be converted into or treated as a `ke_<UUID>` identifier.

---

## 7. Canonical Relationship Structure

A semantic relationship contains, at minimum:

- relationship identifier;
- relationship type;
- source entity;
- target entity; and
- creation time.

Additional properties may include:

- directionality;
- lifecycle status;
- validation state;
- confidence;
- provenance;
- context;
- relationship strength;
- deterministic status;
- conditions;
- supporting evidence;
- contradicting evidence;
- corresponding Knowledge Graph edge;
- temporal applicability;
- supersession;
- creator;
- updater; and
- metadata.

The machine-readable authority for this structure is:

    Core/Schemas/relationships.schema.json

This document explains the semantics. The schema validates the persisted structure.

---

## 8. Relationship Types

All relationship types shall come from:

    Core/Registries/relationship_types.json

The Registry owns:

- canonical relationship names;
- semantic definitions;
- categories;
- directionality;
- symmetry;
- inverse relationships; and
- related relationship metadata.

No schema or knowledge document shall create a second independent relationship vocabulary.

If A.R.I.A. requires a relationship type that does not exist, the Registry shall be deliberately extended.

---

## 9. Semantic Precision

A.R.I.A. shall use the most precise valid Registry relationship available.

A broad association should not be represented as causality unless causality is technically supported.

For example, when supported:

    Incorrect Flex Routing
    CAN_CAUSE
    RSL Discrepancy

provides materially more diagnostic meaning than an unspecified association.

Semantic precision allows relationships to support technical reasoning rather than merely connecting records.

A.R.I.A. shall not select a more specific relationship merely because it produces a stronger diagnostic conclusion.

The relationship must be supported by the underlying technical knowledge.

---

## 10. Directionality

Relationship directionality is defined by the relationship-type Registry.

Relationships may be:

- directed;
- symmetric; or
- otherwise explicitly defined by the Registry.

For a directed relationship:

    Entity A
    CAN_CAUSE
    Entity B

does not establish:

    Entity B
    CAN_CAUSE
    Entity A

The reverse semantic traversal may use a Registry-defined inverse such as:

    Entity B
    CAN_BE_CAUSED_BY
    Entity A

A.R.I.A. shall never assume reverse semantics merely because a forward relationship exists.

---

## 11. Inverse Relationships

A relationship type may define an inverse relationship type.

For example:

    CAN_CAUSE

may have the inverse:

    CAN_BE_CAUSED_BY

Likewise:

    TESTED_BY

may have the inverse:

    TESTS_FOR

And:

    RESOLVED_BY

may have the inverse:

    RESOLVES

A.R.I.A. may support inverse traversal without storing duplicate authoritative assertions when the Registry explicitly defines the inverse.

Inverse traversal is a semantic operation.

It does not automatically create a second persisted relationship.

---

## 12. Symmetric Relationships

Some Registry relationships may be symmetric.

For a symmetric relationship, traversal from either entity may preserve the same semantic meaning.

Symmetry shall exist only when explicitly defined by the relationship-type Registry.

A.R.I.A. shall never infer symmetry from:

- wording;
- common usage;
- graph shape;
- historical co-occurrence; or
- model inference alone.

---

## 13. Relationship Context

Technical relationships may apply only within specific contexts.

Context may include:

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
- environment;
- customer technical requirements;
- geographic domain;
- regulatory domain; and
- time.

For example, a technical relationship between two components may only be valid for a particular product variant or hardware revision.

A.R.I.A. shall not automatically apply a relationship outside its supported context.

---

## 14. Context Is Not Canonical Duplication

A.R.I.A. shall avoid duplicating canonical technical concepts merely because they appear in different contexts.

The same failure mode does not become a new failure mode merely because it occurs:

- on another manufacturer;
- in another product;
- under another scope;
- for another technician;
- for another customer; or
- in another case.

Applicability should normally be expressed through:

- relationships;
- context;
- provenance;
- experience overlays; and
- temporal applicability.

Separate relationship assertions may nevertheless be appropriate when:

- provenance differs materially;
- technical behavior differs;
- confidence differs;
- applicable conditions differ;
- relationship strength differs;
- revisions differ; or
- effective periods differ.

The objective is technical accuracy, not artificial deduplication.

---

## 15. Deterministic Relationships

Some relationships represent established technical facts.

Such relationships do not require hypothesis probability.

They may still require:

- provenance;
- context;
- validation;
- temporal applicability; and
- revision awareness.

A.R.I.A. shall not force probabilistic semantics onto deterministic technical facts.

The relationship record may identify such assertions as deterministic.

Deterministic does not mean context-free or eternally valid.

A deterministic relationship can still be limited by revision, product, configuration, or time.

---

## 16. Probabilistic and Conditional Relationships

Other relationships represent technical possibilities or conditional associations.

Example:

    Incorrect Flex Routing
    CAN_CAUSE
    RSL Discrepancy

This means the source condition is technically capable of producing the target condition.

It does not mean:

    P(Incorrect Flex Routing | current case) = 1.0

Current-case probability is calculated separately.

The relevance of the relationship to an active case may depend on:

- current evidence;
- product;
- configuration;
- topology;
- scope;
- historical experience;
- technician-specific validated experience;
- environmental conditions; and
- contextual similarity.

Canonical possibility and current-case probability must remain separate.

---

## 17. Relationship Strength

A relationship may contain a normalized strength value when meaningful.

Relationship strength represents the strength of the technical or statistical association under applicable conditions.

It shall not automatically represent:

- hypothesis probability;
- evidence confidence;
- relationship confidence;
- source authority;
- route priority; or
- diagnostic certainty.

For example:

    Relationship strength: 0.82
    Current hypothesis probability: 0.46
    Relationship confidence: 0.93

These values answer different questions and shall remain distinct.

Relationship strength shall only be used when the underlying methodology gives the value meaningful technical interpretation.

---

## 18. Confidence

Relationship confidence represents how strongly A.R.I.A. trusts the validity or support of the relationship assertion.

Confidence follows the canonical confidence contract.

Example structure:

    {
      "value": 0.93,
      "basis": "Supported by manufacturer documentation and validated field observations."
    }

Confidence may depend upon:

- source authority;
- provenance quality;
- independent corroboration;
- validation;
- contextual consistency;
- revision applicability;
- historical support;
- expert review; and
- contradictory information.

Confidence is not probability.

A high-confidence relationship can still represent an uncommon cause.

A common cause can also have poor evidentiary support in a particular case.

---

## 19. Provenance

Material technical relationships should retain provenance.

Possible sources include:

- manufacturer documentation;
- manufacturer technical support;
- engineering documentation;
- standards;
- approved design documents;
- configuration exports;
- direct measurements;
- validated field observations;
- validated Experience Ledger records;
- approved human technical contributions;
- structured imports; and
- A.R.I.A.-derived candidate knowledge.

Provenance shall follow the canonical provenance contract.

A.R.I.A. should be capable of explaining:

- where the relationship came from;
- whether it was directly sourced or derived;
- what information supported it;
- whether transformation occurred;
- when it was acquired; and
- whether its integrity has been verified.

---

## 20. Multiple Supporting Sources

A technically identical relationship should not be duplicated merely because several sources support it.

For example, one assertion may be supported by:

- a manufacturer manual;
- an engineering document;
- a validated field discovery; and
- historical experience.

The relationship should exist once when the semantic assertion, context, temporal applicability, and technical meaning are the same.

Its provenance and supporting information should preserve the supporting lineage.

---

## 21. Independent Corroboration

Multiple sources do not necessarily represent independent confirmation.

For example:

    Manufacturer Bulletin
            |
            +--> Internal Procedure
            |
            +--> Training Document

If both downstream documents derive from the same manufacturer bulletin, they are not three independent confirmations.

A.R.I.A. shall preserve common lineage where known.

Source count alone shall not determine relationship confidence.

This principle is especially important when learned technical knowledge is derived from evidence or Experience Ledger records.

---

## 22. Contradictory Technical Assertions

A.R.I.A. shall permit contradictory technical assertions to coexist while unresolved.

Conceptually:

    Source A:
    Product X
    REQUIRES
    Configuration Y

    Source B:
    Product X
    REQUIRES
    Configuration Z

Where `REQUIRES` is an approved Registry relationship, both assertions may temporarily coexist when their technical applicability has not yet been resolved.

A.R.I.A. shall preserve relevant:

- provenance;
- authority;
- revision;
- context;
- effective date;
- validation state; and
- contradiction information.

The system shall not silently discard inconvenient technical information.

Contradiction resolution is a reasoning and validation process.

---

## 23. Relationship Conditions

Some relationships apply only when specific conditions exist.

Conceptually:

    Condition:
    2+0 diversity configuration active

    Relationship:
    Incorrect Diversity Flex Routing
    CAN_CAUSE
    Diversity RSL Discrepancy

Conditional requirements should reference canonical entities whenever practical.

A.R.I.A. shall evaluate applicable conditions before using a conditional relationship in diagnostic reasoning.

---

## 24. Negative Knowledge

A.R.I.A. may represent explicit negative technical knowledge when an appropriate relationship type exists in the canonical Registry.

Absence of a positive relationship does not imply a negative relationship.

Likewise, inability to establish a relationship does not prove that the opposite relationship exists.

Negative technical knowledge must be explicitly supported.

If A.R.I.A. requires a negative relationship semantic not currently represented by the Registry, the Registry must be deliberately extended.

---

## 25. Temporal Relationships

Technical truth may change over time.

Relationships may therefore have:

- `valid_from`;
- `valid_to`;
- supersession information; and
- revision-specific context.

A relationship valid for one firmware or hardware revision may not apply to another.

Historical reasoning shall use technical relationships applicable to the relevant historical context rather than blindly applying current knowledge.

---

## 26. Relationship Lifecycle

Relationship lifecycle status and validation state are distinct.

Lifecycle status may include:

- `PROPOSED`;
- `ACTIVE`;
- `DEPRECATED`;
- `SUPERSEDED`; and
- `REJECTED`.

Validation state may include:

- `UNREVIEWED`;
- `REVIEWED`;
- `VALIDATED`;
- `DISPUTED`; and
- `REJECTED`.

A relationship may therefore be active while still awaiting validation.

Likewise, a historically valid relationship may be superseded without being considered false for its original period of applicability.

---

## 27. Candidate Knowledge

Relationships extracted or inferred by an automated system shall not automatically become authoritative technical knowledge.

A candidate relationship may originate from:

- document extraction;
- model inference;
- repeated Experience Ledger observations;
- pattern detection;
- technical comparison; or
- human contribution.

Such relationships should enter an appropriate validation process.

A.R.I.A. may discover candidate knowledge.

A.R.I.A. shall not silently promote candidate knowledge into validated technical truth.

---

## 28. Human Review

During development and where technical authority requires it, candidate relationships may enter human review.

Review should support:

- approval;
- rejection;
- editing;
- merging;
- contextualization;
- relationship-type correction;
- provenance attachment;
- contradiction identification; and
- requests for additional validation.

Review actions should remain auditable.

Human review does not remove the requirement for provenance or technical support.

---

## 29. Supersession

A relationship may be superseded without deletion.

Conceptually:

    Earlier technical state:
    Procedure A
    REQUIRES
    Step X

    Later technical state:
    Procedure A
    REQUIRES
    Step Y

If the original relationship was valid for an earlier revision or period, it should remain available for historical reasoning.

Supersession preserves knowledge evolution.

---

## 30. Deprecation

Deprecated relationships may remain useful for:

- historical cases;
- older products;
- older hardware;
- older firmware;
- previous engineering standards;
- audits; and
- revision comparisons.

Deprecated does not automatically mean false.

It means the relationship should not normally govern current reasoning outside its valid context.

---

## 31. Relationships in Diagnostic Reasoning

The Diagnostic Routing Engine may traverse reusable technical relationships to construct candidate hypotheses.

Example current symptom:

    Diversity RSL Discrepancy

Reusable technical relationships may identify possibilities such as:

    Incorrect Flex Routing
    CAN_CAUSE
    Diversity RSL Discrepancy

    Incorrect Radio Configuration
    CAN_CAUSE
    Diversity RSL Discrepancy

    Cross Polarization
    CAN_CAUSE
    RSL Discrepancy

    Radio Failure
    CAN_CAUSE
    RSL Discrepancy

These relationships establish technical possibilities.

They do not establish current-case probability.

The Probability Engine evaluates current likelihood.

The Diagnostic Routing Engine determines what information or action is most useful next.

---

## 32. Relationships in Evidence Reasoning

Case evidence may create case-specific semantic relationships.

Conceptually:

    evd_<UUID>
    SUPPORTS
    hyp_<UUID>

or:

    evd_<UUID>
    CONTRADICTS
    hyp_<UUID>

where those semantics are defined by the canonical relationship Registry.

These are `rel_<UUID>` relationships.

They generally do not belong in the reusable Knowledge Graph because they describe the reasoning state of a particular case.

Evidence may also alter the relevance of reusable technical relationships without changing the underlying canonical knowledge.

For example:

    Main RSL normal
    Diversity RSL low

may:

- strengthen diversity-specific diagnostic routes;
- weaken common-path hypotheses;
- reduce environmental-route priority; and
- increase relevance of Diversity RF Chain relationships.

The canonical technical relationship does not necessarily change.

Its current-case relevance changes.

---

## 33. Relationships and Hypotheses

A hypothesis is a case-specific evaluation of a possible technical explanation.

Reusable relationships may generate or inform hypotheses.

Case-specific relationships may then connect:

- evidence to hypotheses;
- hypotheses to evidence;
- actions to hypotheses;
- outcomes to hypotheses; and
- hypotheses to relevant canonical entities.

A.R.I.A. shall not convert every hypothesis into permanent technical knowledge.

Hypotheses remain case-specific reasoning objects unless validated learning produces a separate reusable technical assertion.

---

## 34. Relationships and Actions

Actions may participate in semantic relationships.

For example:

    Failure Mode
    TESTED_BY
    Diagnostic Action

The Registry-defined inverse may permit traversal as:

    Diagnostic Action
    TESTS_FOR
    Failure Mode

Likewise:

    Failure Mode
    RESOLVED_BY
    Corrective Action

may permit inverse traversal as:

    Corrective Action
    RESOLVES
    Failure Mode

A case-specific action result may also produce evidence.

The relationship architecture therefore connects technical knowledge to executable diagnostic reasoning without conflating actions with evidence or outcomes.

---

## 35. Relationships and Measurements

Measurement relationships may connect technical quantities, observations, tools, or procedures where the Registry defines those semantics.

For example:

    Technical Quantity
    MEASURED_BY
    Measurement Method

may permit inverse traversal as:

    Measurement Method
    MEASURES
    Technical Quantity

Measurement semantics must remain distinct from the actual evidence record generated by a measurement.

A method describing how something is measured is reusable knowledge.

A measurement taken during a particular case is case evidence.

---

## 36. Relationships and Experience

Validated Experience Ledger records use:

    exp_<UUID>

An Experience Ledger record is not a diagnostic case.

Diagnostic cases use:

    case_<UUID>

Validated experience may support or challenge reusable technical relationships.

For example, repeated validated experience may support the technical assertion:

    Incorrect Radio Configuration
    CAN_CAUSE
    RSL Discrepancy

under a particular technical context.

Experience may influence:

- relationship confidence;
- relationship strength;
- diagnostic priors;
- route selection; and
- candidate knowledge generation.

The Experience Ledger does not require creation of duplicate technical relationships.

---

## 37. Learned Relationships

Repeated validated experience may reveal an association not currently represented in canonical technical knowledge.

A.R.I.A. may identify such an association as candidate knowledge.

The proposed relationship shall retain, where applicable:

- experience lineage;
- sample size;
- context;
- confidence;
- validation state; and
- supporting provenance.

If the correct semantic relationship type does not exist in the Registry, A.R.I.A. shall not invent one inside the learned relationship record.

The relationship vocabulary must be extended deliberately.

Candidate learned relationships remain candidate knowledge until appropriately validated.

---

## 38. Correlation Is Not Causation

A.R.I.A. shall distinguish association from causality.

Historical co-occurrence alone does not establish:

    CAN_CAUSE

A non-causal association must use an appropriate relationship type from the Registry.

If the required semantic relationship does not exist in the Registry, the correct action is to evaluate and extend the Registry deliberately—not misuse a causal relationship.

Causal assertions require sufficient technical or evidentiary support.

A.R.I.A. shall not infer causality merely because:

- two conditions frequently occur together;
- an action preceded a resolution;
- a technician believes a cause was present;
- several cases contain similar language; or
- a model predicts the relationship.

---

## 39. Relationship Traversal Constraints

A.R.I.A. shall not blindly traverse every relationship connected to an entity.

Traversal may be constrained by:

- relationship type;
- active context;
- product applicability;
- manufacturer;
- product family;
- product variant;
- firmware;
- configuration;
- topology;
- scope;
- current evidence;
- hypothesis state;
- validation state;
- source authority;
- temporal applicability;
- graph depth; and
- computational budget.

This prevents irrelevant graph expansion during reasoning.

---

## 40. Multi-Hop Reasoning

Some diagnostic reasoning requires multiple semantic hops.

Conceptually:

    Current Symptom
          ^
          |
    Possible Failure Mode
          |
          v
    Relevant Component
          |
          v
    Connected Technical Element

Multi-hop traversal may expose useful diagnostic routes that are not represented by one direct relationship.

Every hop must use an approved Registry relationship type.

A.R.I.A. shall not treat every reachable node as equally relevant.

Context and reasoning constraints remain applicable at each hop.

---

## 41. Graph Explosion Control

Uncontrolled relationship traversal can produce large amounts of irrelevant technical information.

A.R.I.A. should therefore prioritize traversal based on:

1. current symptoms;
2. current evidence;
3. active hypotheses;
4. technical context;
5. manufacturer/product applicability;
6. relationship semantics;
7. validation;
8. probability;
9. expected information gain; and
10. diagnostic cost.

The objective is not maximum traversal.

The objective is useful technical reasoning.

---

## 42. Manufacturer-Specific Knowledge

Manufacturer-specific technical relationships shall reuse canonical entities wherever appropriate.

Manufacturer, product, product-family, and technical-concept entities may be connected using relationship types defined by the Registry.

A.R.I.A. shall not create a second copy of a generic technical concept merely because another manufacturer uses it.

Manufacturer specificity should be represented through:

- canonical manufacturer entities;
- product relationships;
- context;
- provenance; and
- applicable technical relationships.

The manufacturer technical corpus remains a source of technical knowledge, not an alternative entity architecture.

---

## 43. Product and Variant Relationships

Product hierarchy should be expressed explicitly using Registry-approved relationships.

Relationships may connect, where supported:

- manufacturer;
- product family;
- product;
- product variant;
- hardware revision;
- firmware;
- component; and
- configuration.

For example, the Registry may express hierarchy using relationships such as:

    MEMBER_OF

and its defined inverse:

    HAS_MEMBER

A.R.I.A. shall use the precise Registry semantics appropriate to the entities being connected.

This allows A.R.I.A. to determine whether technical knowledge applies broadly or only to a particular implementation.

---

## 44. Scope Relationships

Scope is a contextual filter.

Scope shall not create duplicate technical truth.

A failure mode remains the same canonical failure mode even when its relevance differs between:

- installation;
- commissioning;
- troubleshooting;
- maintenance;
- migration; or
- acceptance.

Where scope must be explicitly connected to another canonical entity, A.R.I.A. shall use an appropriate relationship type defined by the Registry.

---

## 45. User-Specific Experience

User-specific experience shall not duplicate canonical technical relationships.

Instead, validated Experience Ledger records may associate:

- a user;
- technical context;
- canonical technical entities;
- outcomes; and
- observed relationships.

The Probability Engine may use this experience to alter priors or diagnostic strategy.

For example, the canonical technical relationship may remain:

    Incorrect Flex Routing
    CAN_CAUSE
    RSL Discrepancy

while validated historical experience shows that a particular technician encounters that condition more or less frequently than the broader population.

The technical relationship remains canonical.

The user's validated history affects the prior—not the technical truth.

---

## 46. Evidence Does Not Rewrite Knowledge Automatically

A single case observation shall not automatically modify canonical technical knowledge.

Case evidence affects:

- case hypotheses;
- current probability;
- diagnostic routing;
- action selection; and
- case-specific relationships.

Only appropriately validated learning may propose changes to reusable technical knowledge.

This prevents transient, incomplete, or erroneous field observations from corrupting the Knowledge Graph.

---

## 47. Relationship Promotion to the Knowledge Graph

A semantic relationship may be eligible for persistence as reusable Knowledge Graph knowledge when it represents a sufficiently validated, reusable technical assertion.

Promotion should consider:

- technical generalizability;
- validation;
- provenance;
- contextual scope;
- contradiction status;
- temporal applicability;
- source authority; and
- whether the assertion is genuinely reusable beyond one case.

When represented as persisted graph structure, the Knowledge Graph edge receives:

    ke_<UUID>

The semantic relationship retains:

    rel_<UUID>

where the semantic relationship record itself is persisted.

Promotion does not mutate one identifier type into the other.

A.R.I.A. shall preserve lineage between the semantic assertion and corresponding Knowledge Graph structure where appropriate.

---

## 48. Knowledge Graph Edge Semantics

Knowledge Graph edges shall use the approved relationship vocabulary where applicable.

The edge stores graph structure.

The Registry defines semantic meaning.

The underlying canonical entities define the technical concepts.

This keeps:

- identity;
- semantics;
- graph storage; and
- technical meaning

separate and composable.

Knowledge Graph storage shall not become a second source of relationship vocabulary.

---

## 49. No Silent Reverse Inference

A.R.I.A. shall never infer a reverse technical claim unless:

- the relationship is explicitly symmetric; or
- the Registry defines an inverse relationship.

For example:

    Failure Mode
    RESOLVED_BY
    Action

may permit inverse traversal as:

    Action
    RESOLVES
    Failure Mode

only because the Registry defines the applicable inverse semantics.

This rule prevents accidental semantic corruption.

---

## 50. No Silent Causal Promotion

A.R.I.A. shall never automatically promote an association into causality because:

- two entities frequently co-occur;
- an action preceded a resolution;
- a technician believes a cause was present;
- several cases contain similar language; or
- a model predicts the relationship.

Causal knowledge requires appropriate validation.

Historical frequency may affect investigation priority without establishing technical causation.

---

## 51. No Relationship Duplication for Source Count

If three sources support the same assertion, A.R.I.A. should normally have:

    1 canonical semantic relationship
    multiple supporting provenance paths

rather than:

    multiple duplicate semantic relationships

Separate relationships remain appropriate when the assertions materially differ in:

- context;
- conditions;
- temporal validity;
- technical meaning;
- confidence;
- relationship strength; or
- provenance-dependent applicability.

---

## 52. Relationship Auditability

A.R.I.A. should be able to answer, where the underlying records support it:

- What relationship is being used?
- What does that relationship type mean?
- What entities does it connect?
- Is it directed or symmetric?
- What is its inverse?
- What context applies?
- Where did it come from?
- How confident are we in it?
- Is it validated?
- What evidence supports it?
- What evidence contradicts it?
- When was it valid?
- Has it been superseded?
- Is it reusable knowledge or case-specific reasoning?
- Does a corresponding Knowledge Graph edge exist?

This auditability is necessary for trustworthy technical reasoning.

---

## 53. Example: Reusable Technical Relationship

The following illustrates the structure of a reusable semantic relationship:

    {
      "relationship_id": "rel_018f3f3c-7f63-77f1-a9cc-61216e6f4179",
      "relationship_type": "CAN_CAUSE",
      "source_entity_id": "fm_018f3f50-87c1-74d0-901f-58bbbf938921",
      "target_entity_id": "sym_018f3f54-9235-7461-8bd5-50fc3bd2e58e",
      "directed": true,
      "status": "ACTIVE",
      "validation_state": "VALIDATED",
      "confidence": {
        "value": 0.94,
        "basis": "Supported by authoritative technical documentation and validated field experience."
      },
      "relationship_strength": 0.82,
      "deterministic": false,
      "knowledge_edge_id": "ke_018f3f58-1828-7c93-aef2-12eb311429c0",
      "created_at": "2026-08-25T20:00:00Z"
    }

The `rel_<UUID>` represents the semantic assertion.

The corresponding `ke_<UUID>` represents reusable persisted graph structure.

---

## 54. Example: Case-Specific Evidence Relationship

The following illustrates a case-specific semantic relationship:

    {
      "relationship_id": "rel_018f3f60-2771-7241-82a2-35d5b6eb3813",
      "relationship_type": "SUPPORTS",
      "source_entity_id": "evd_018f3f63-7a33-7741-80fb-21396fcd9422",
      "target_entity_id": "hyp_018f3f66-a112-7461-86ef-85b88961a7c4",
      "directed": true,
      "status": "ACTIVE",
      "validation_state": "REVIEWED",
      "confidence": {
        "value": 0.91,
        "basis": "Direct instrument measurement with verified context."
      },
      "knowledge_edge_id": null,
      "created_at": "2026-08-25T20:05:00Z"
    }

This relationship belongs to diagnostic reasoning.

It does not need to become permanent reusable graph knowledge.

---

## 55. Example: Deterministic Technical Relationship

A deterministic relationship may use the same semantic relationship structure while explicitly identifying that its technical assertion is deterministic.

Conceptually:

    {
      "relationship_id": "rel_018f3f70-c8e4-7772-81b2-b3f428f38a42",
      "relationship_type": "<REGISTRY_DEFINED_RELATIONSHIP_TYPE>",
      "source_entity_id": "prod_018f3f73-83d0-7160-bdb0-40e2b610be2a",
      "target_entity_id": "mfr_018f3f76-3231-7612-9870-49ab16fdff61",
      "directed": true,
      "status": "ACTIVE",
      "validation_state": "VALIDATED",
      "confidence": {
        "value": 1.0,
        "basis": "Authoritative technical source."
      },
      "deterministic": true,
      "created_at": "2026-08-25T20:10:00Z"
    }

The placeholder relationship type is intentional in this example.

The actual persisted relationship must use a relationship type that exists in `Core/Registries/relationship_types.json`.

This prevents documentation examples from silently creating new vocabulary.

---

## 56. Relationship Integrity Rules

A.R.I.A. shall preserve the following invariants:

1. Every persisted semantic relationship has stable `rel_<UUID>` identity.
2. Every persisted Knowledge Graph edge has stable `ke_<UUID>` identity.
3. Relationship semantics come from the canonical Registry.
4. Schemas do not independently redefine relationship vocabulary.
5. Knowledge documents do not independently redefine relationship vocabulary.
6. Reverse relationships are not assumed.
7. Symmetry exists only when explicitly defined.
8. Confidence is not probability.
9. Relationship strength is not current-case probability.
10. Historical frequency is not causality.
11. Context does not justify unnecessary entity duplication.
12. Multiple sources do not automatically mean independent corroboration.
13. Case-specific reasoning does not automatically become canonical knowledge.
14. Experience must be validated before materially influencing learned technical knowledge.
15. Superseded knowledge remains available where historically applicable.
16. Provenance remains attached to material technical assertions.
17. Contradictory information is preserved until resolved.
18. Knowledge Graph promotion requires reusable technical applicability.
19. `rel_` and `ke_` identities are never treated as interchangeable.
20. A relationship type not present in the Registry shall not be invented by another layer.

---

## 57. Relationship Architecture Summary

The relationship system preserves the following separation:

    CANONICAL ENTITIES
          |
          | semantic meaning
          v
    rel_<UUID>
    SEMANTIC RELATIONSHIP
          |
          | when reusable and appropriate for graph persistence
          v
    ke_<UUID>
    KNOWLEDGE GRAPH EDGE

Meanwhile, active diagnostic reasoning may use:

    evd_<UUID>
          |
          | SUPPORTS / CONTRADICTS
          v
    hyp_<UUID>

through case-specific:

    rel_<UUID>

without polluting the reusable Knowledge Graph.

Historical validated outcomes may enter:

    exp_<UUID>

and influence future:

- priors;
- relationship confidence;
- relationship strength;
- routing strategy; and
- candidate knowledge generation.

They do not silently rewrite technical truth.

---

## 58. Final Principle

A.R.I.A.'s relationship architecture exists to make technical knowledge usable for reasoning.

A relationship is not merely a line between two nodes.

It is a traceable technical assertion with:

- precise semantics;
- stable identity;
- direction;
- context;
- provenance;
- validation;
- confidence;
- temporal applicability; and
- appropriate separation between current-case reasoning and reusable knowledge.

A.R.I.A. shall preserve those distinctions so that technical reasoning remains explainable, reusable, auditable, and capable of improving without corrupting canonical knowledge.
