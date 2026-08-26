# A.R.I.A. Entity Architecture

**Document Type:** Canonical Knowledge and Reasoning Specification  
**Authority:** Subordinate to `Core/Schemas/entity_contracts.json`, `Core/Registries/entity_types.json`, `Core/Schemas/entity.schema.json`, `Core/Registries/relationship_types.json`, and `Core/Persona/ARIA_CONSTITUTION.md`  
**Version:** 1.0

---

## 1. Purpose

This document defines how A.R.I.A. represents, identifies, distinguishes, validates, reuses, and evolves canonical technical entities.

Entities establish what technical concepts exist.

Relationships establish how those concepts interact.

Evidence establishes what was observed in a specific diagnostic context.

Hypotheses establish what A.R.I.A. is evaluating in a specific case.

Experience preserves validated historical outcomes.

These structures must remain distinct.

The Entity Architecture exists so A.R.I.A. can continuously expand its technical knowledge without becoming a collection of duplicate names, manufacturer-specific copies, case observations, or unstructured documents.

---

## 2. Canonical Authority

Entity architecture is governed by the following hierarchy:

1. `Core/Schemas/entity_contracts.json`
2. `Core/Registries/entity_types.json`
3. `Core/Schemas/entity.schema.json`
4. `Core/Registries/relationship_types.json`
5. This document

`Core/Schemas/entity_contracts.json` owns canonical identity and shared interoperability contracts.

`Core/Registries/entity_types.json` owns canonical entity-type vocabulary.

`Core/Schemas/entity.schema.json` owns machine-readable validation of canonical entity records.

`Core/Registries/relationship_types.json` owns relationship vocabulary.

This document explains how those contracts work together.

It shall not independently establish competing entity types, relationship types, identifier systems, or persistence contracts.

---

## 3. Entity Design Principle

A canonical entity should exist when representing a concept independently materially improves:

- technical reasoning;
- retrieval;
- relationship modeling;
- contextual filtering;
- source attribution;
- experience analysis;
- diagnostic routing;
- historical reasoning; or
- future extensibility.

Not every word, phrase, observation, value, or document term should become an entity.

The objective is meaningful technical structure, not maximum entity count.

---

## 4. Canonical Entity Identity

Every persisted canonical technical entity shall have a stable typed identifier governed by:

    Core/Schemas/entity_contracts.json

Canonical identities use typed UUID identifiers.

Examples of established technical-entity identity classes include:

    ent_<UUID>
    mfr_<UUID>
    pfam_<UUID>
    prod_<UUID>
    pvar_<UUID>
    scope_<UUID>
    sym_<UUID>
    fm_<UUID>
    meas_<UUID>
    unit_<UUID>
    tool_<UUID>

The exact authoritative prefix contract is defined by `entity_contracts.json`.

UUIDv7 is preferred where specified by that contract.

The old sequential form:

    ENT-000001

is not the canonical identity architecture.

---

## 5. Most-Specific Identity Rule

A.R.I.A. shall use the most specific established canonical identity class available.

Examples:

    Nokia
    MANUFACTURER
    mfr_<UUID>

    Wavence
    PRODUCT_FAMILY
    pfam_<UUID>

    UBT-T
    PRODUCT
    prod_<UUID>

    UBT-T 18 GHz
    PRODUCT_VARIANT
    pvar_<UUID>

    RSL Discrepancy
    SYMPTOM
    sym_<UUID>

    Incorrect Flex Routing
    ROOT_CAUSE or FAILURE_MODE as technically classified
    fm_<UUID>

    Received Signal Level
    MEASUREMENT
    meas_<UUID>

    dBm
    UNIT
    unit_<UUID>

    Anritsu Site Master
    TOOL
    tool_<UUID>

    Troubleshooting
    SCOPE
    scope_<UUID>

The generic:

    ent_<UUID>

is used for canonical technical entities that do not have a dedicated identity prefix.

For example, entity types such as:

- `COMPONENT`;
- `INTERFACE`;
- `PORT`;
- `ANTENNA`;
- `RADIO`;
- `FREQUENCY_BAND`;
- `CONFIGURATION`;
- `FIRMWARE`;
- `SOFTWARE`;
- `STANDARD`;
- `REQUIREMENT`;
- `CONSTRAINT`; or
- `CONCEPT`

may use `ent_<UUID>` unless and until `entity_contracts.json` establishes a more specific identity class.

The generic `ent_` prefix shall not compete with an already-established specialized prefix.

---

## 6. Identity Does Not Encode Mutable Meaning

Canonical identifiers shall not encode mutable technical or business meaning.

Avoid identifiers such as:

    NOKIA-UBTT-18GHZ-001

A product name, manufacturer classification, frequency, hierarchy, or terminology may change.

The canonical identifier remains stable.

Meaning belongs in:

- entity type;
- canonical name;
- aliases;
- relationships;
- metadata;
- provenance;
- applicability; and
- temporal context.

Identity provides durable reference.

---

## 7. Canonical Entity Record

The machine-readable authority for canonical entity structure is:

    Core/Schemas/entity.schema.json

A canonical entity record requires:

- `id`;
- `entity_type`;
- `canonical_name`;
- `status`;
- `validation_state`;
- `created_at`; and
- `updated_at`.

The schema also supports controlled optional information such as:

- description;
- short description;
- aliases;
- provenance;
- confidence;
- temporal applicability;
- deprecation;
- supersession;
- legacy identifiers;
- creator;
- updater; and
- metadata.

This document shall not redefine a competing machine structure.

---

## 8. Entity Types

All canonical entity types shall come from:

    Core/Registries/entity_types.json

The Registry is the authoritative vocabulary.

It currently contains technical and contextual classes across areas including:

- organizations and actors;
- equipment;
- RF;
- architecture;
- configuration;
- software;
- diagnostics;
- actions;
- measurements;
- resources;
- environment;
- operational context; and
- knowledge.

The Registry may expand.

When a genuinely new canonical entity class is required, the Registry shall be deliberately extended.

No knowledge document, schema, manufacturer file, extraction process, or model response shall independently invent a permanent entity type.

---

## 9. Entity Type and Identity Prefix Are Different Concepts

`entity_type` and identity prefix are related but are not the same thing.

For example:

    entity_type = COMPONENT
    id = ent_<UUID>

is valid because `COMPONENT` is a Registry classification even though there is no dedicated `component_` identity prefix.

Likewise:

    entity_type = MANUFACTURER
    id = mfr_<UUID>

uses a specialized identity class because one exists.

A.R.I.A. shall not create a new prefix merely because an entity type exists.

Identity classes are governed separately by `entity_contracts.json`.

---

## 10. Canonical Name

`canonical_name` is the preferred human-readable name of the entity.

Examples:

    Received Signal Level

    UBT-T

    Incorrect Flex Routing

    2+0 Diversity

The canonical name may change if preferred terminology changes.

The canonical identifier does not.

A name is therefore not identity.

---

## 11. Canonical Description

An entity description defines the entity itself.

For example:

    ENTITY:
    Received Signal Level

    DESCRIPTION:
    Received RF power measured at the applicable receiver point.

The description should not attempt to contain every technical relationship involving the entity.

Do not turn descriptions into unstructured knowledge graphs.

Relationships belong in the relationship system.

Case observations belong in evidence.

Historical outcomes belong in experience.

---

## 12. Aliases

An entity may have multiple aliases.

Example:

    CANONICAL ENTITY:
    Received Signal Level

    ALIASES:
    RSL
    RX Level
    Receive Level
    Received Level

Aliases may preserve information such as:

- abbreviation;
- manufacturer terminology;
- historical terminology;
- alternate spelling;
- source;
- manufacturer context;
- temporal applicability;
- deprecation; and
- other controlled alias metadata.

Aliases do not automatically create separate canonical entities.

---

## 13. Alias Collision

The same alias may refer to different concepts in different contexts.

A.R.I.A. shall therefore support contextual alias resolution.

For example:

    AIM

may require manufacturer, product, component, or surrounding technical context to resolve correctly.

Alias resolution may consider:

- active manufacturer;
- active product;
- product family;
- product variant;
- conversation context;
- current diagnostic case;
- scope;
- neighboring entities; and
- source context.

A.R.I.A. shall not permanently merge entities merely because they share an abbreviation or label.

---

## 14. Alias Confidence

The current machine schema permits an optional normalized confidence value on an alias.

This value concerns confidence in the alias mapping.

It shall not be confused with:

- entity confidence;
- relationship confidence;
- hypothesis probability; or
- evidence confidence.

If the canonical confidence contract is later extended to aliases, the machine schema shall be deliberately reconciled at that time.

This document shall not silently redefine the alias-confidence structure independently of the schema.

---

## 15. Manufacturer Independence

Shared technical concepts should remain manufacturer-independent when technically appropriate.

For example:

    Received Signal Level

should normally exist once as a canonical measurement concept rather than being duplicated as:

    Nokia RSL
    Aviat RSL
    Ceragon RSL
    Ericsson RSL

Manufacturer-specific behavior should be represented through:

- relationships;
- applicability;
- product context;
- manufacturer context;
- aliases;
- provenance; or
- genuinely manufacturer-specific entities.

A separate entity is justified only when the technical concept itself is materially distinct.

---

## 16. Manufacturer Entities

Manufacturers are canonical entities.

Example:

    entity_type: MANUFACTURER
    id: mfr_<UUID>
    canonical_name: Nokia

Products, components, tools, software, and other relevant entities may connect to manufacturers using Registry-approved relationships.

For example:

    UBT-T
    MANUFACTURED_BY
    Nokia

The manufacturer relationship belongs in the relationship architecture.

It should not be hidden as arbitrary text inside the UBT-T entity record.

---

## 17. Product Families

Product families are canonical entities when they provide meaningful technical hierarchy.

Example:

    Wavence
    PRODUCT_FAMILY
    pfam_<UUID>

A product may connect to its family using Registry-approved hierarchy semantics.

For example:

    UBT-T
    MEMBER_OF
    Wavence

where `MEMBER_OF` is defined by the canonical relationship Registry.

The hierarchy should not be encoded solely into product names.

---

## 18. Products

A product represents a canonical telecommunications product or equipment platform.

Example:

    UBT-T
    PRODUCT
    prod_<UUID>

A product entity should represent the reusable product concept.

It should not be duplicated merely because the product appears:

- at another site;
- in another project;
- in another case;
- under another customer;
- in another scope; or
- in another technician's history.

Those are contextual relationships or instances, not new canonical product concepts.

---

## 19. Product Variants

A.R.I.A. shall distinguish between a product and a product variant when the distinction has meaningful technical consequences.

Possible variant dimensions include:

- frequency band;
- hardware implementation;
- power capability;
- interface configuration;
- regional implementation; or
- other technically significant differences.

A variant should be created when the distinction materially changes:

- specifications;
- compatibility;
- behavior;
- procedures;
- relationships;
- configuration;
- applicability; or
- failure characteristics.

Example:

    UBT-T 18 GHz
    PRODUCT_VARIANT
    pvar_<UUID>

The variant may connect to its parent product using:

    VARIANT_OF

where defined by the relationship Registry.

Do not create a variant merely because a product is discussed in a different context.

---

## 20. Hardware Revisions

Hardware revisions are canonical entities when revision differences materially affect technical applicability.

The current Registry contains:

    HARDWARE_REVISION

There is not currently a dedicated hardware-revision identity prefix in the canonical contract.

Therefore a hardware revision may use:

    ent_<UUID>

unless the identity contract is deliberately extended.

Revision applicability should be represented through Registry-approved relationships and temporal/contextual information rather than encoded only into free text.

---

## 21. Firmware and Software

The Registry distinguishes:

- `FIRMWARE`;
- `SOFTWARE`; and
- `SOFTWARE_VERSION`.

These are canonical technical concepts when independently useful for reasoning.

They currently use the generic:

    ent_<UUID>

unless `entity_contracts.json` later establishes specialized identity classes.

A.R.I.A. shall not treat firmware or software version strings as arbitrary metadata when those versions materially govern:

- compatibility;
- configuration;
- procedures;
- symptoms;
- requirements;
- failure modes; or
- technical applicability.

---

## 22. Components, Interfaces, and Ports

The Registry distinguishes structural equipment concepts including:

- `COMPONENT`;
- `INTERFACE`;
- `PORT`;
- `ANTENNA`;
- `RADIO`; and
- `RF_CHAIN_COMPONENT`.

These may use:

    ent_<UUID>

when no specialized prefix exists.

Their technical structure should be represented through Registry-approved relationships such as:

    COMPONENT_OF
    HAS_COMPONENT
    HAS_INTERFACE
    INTERFACE_OF
    HAS_PORT
    PORT_OF
    CONNECTS_TO
    MATES_WITH
    FEEDS
    FED_BY
    PRECEDES_IN_PATH
    FOLLOWS_IN_PATH

The relationship Registry remains authoritative for exact semantics.

---

## 23. RF Concepts

Canonical RF entities may include Registry types such as:

- `FREQUENCY_BAND`;
- `POLARIZATION`;
- `CHANNEL`;
- `MODULATION`;
- `ANTENNA`;
- `RADIO`; and
- `RF_CHAIN_COMPONENT`.

Frequency, polarization, channel, or modulation should not be encoded only into a product's display name when the concept needs independent reasoning.

For example, rather than relying exclusively on:

    UBT-T 18 GHz

A.R.I.A. may represent:

    UBT-T 18 GHz
    PRODUCT_VARIANT

and separately represent:

    18 GHz
    FREQUENCY_BAND

with an appropriate Registry-approved relationship establishing applicability.

This preserves queryable technical structure.

---

## 24. Configuration Entities

The Registry distinguishes:

- `CONFIGURATION`;
- `CONFIGURATION_PARAMETER`; and
- `CONFIGURATION_VALUE`.

These concepts should remain separate when doing so improves reasoning.

Conceptually:

    CONFIGURATION:
    2+0 Diversity

    PARAMETER:
    Radio Role

    VALUE:
    Radio B

A.R.I.A. shall avoid embedding complex configuration knowledge into unstructured strings when canonical configuration entities and relationships provide better technical structure.

---

## 25. Topology

The Registry contains:

    TOPOLOGY

Examples may include:

    1+0
    2+0
    2+0 Diversity
    1+1 HSB

Topology is not merely a display label.

It may materially affect:

- valid configurations;
- component paths;
- applicable procedures;
- failure modes;
- diagnostic routes;
- thresholds; and
- technical relationships.

Topology should therefore remain independently addressable when useful for reasoning.

---

## 26. Measurements

A measurement entity represents a canonical measurable technical quantity.

Example:

    id: meas_<UUID>
    entity_type: MEASUREMENT
    canonical_name: Received Signal Level

A unit is a separate canonical entity.

Example:

    id: unit_<UUID>
    entity_type: UNIT
    canonical_name: dBm

The relationship Registry provides measurement semantics including:

    MEASURED_IN
    UNIT_FOR
    MEASURED_BY
    MEASURES
    HAS_THRESHOLD
    THRESHOLD_FOR

The numeric value observed during a particular diagnostic case is not the canonical measurement entity.

For example:

    CANONICAL ENTITY:
    Received Signal Level

    CASE OBSERVATION:
    -54 dBm

The `-54 dBm` observation belongs in evidence or another appropriate case-specific structure.

---

## 27. Thresholds

The Registry contains:

    THRESHOLD

A threshold is a canonical technical boundary, tolerance, or limit when independently reusable.

A threshold may be associated with measurements, tests, alarms, or technical states through Registry-approved relationships.

Threshold values shall not be confused with individual case observations.

---

## 28. Symptoms

Symptoms represent observable problems or abnormal conditions contributing to diagnosis.

Canonical symptoms use:

    sym_<UUID>

Example:

    RSL Discrepancy
    SYMPTOM
    sym_<UUID>

A symptom is not automatically a root cause.

A symptom may be:

- observed directly;
- reported by a user;
- derived from evidence;
- exhibited by equipment; or
- associated with multiple possible causes.

The relationship system establishes those technical connections.

---

## 29. Failure Modes, Root Causes, and Contributing Causes

The Registry distinguishes:

- `FAILURE_MODE`;
- `ROOT_CAUSE`; and
- `CONTRIBUTING_CAUSE`.

These distinctions matter.

A failure mode describes a technical manner of failure.

A root cause describes an underlying cause capable of producing symptoms or failure modes.

A contributing cause may influence a failure without being the primary root cause.

The canonical identity contract currently provides:

    fm_<UUID>

for failure-mode/cause-class technical entities governed by that contract.

The precise semantic classification remains in `entity_type`.

A.R.I.A. shall not collapse symptoms, failure modes, root causes, and contributing causes merely because they frequently occur together.

---

## 30. Causal Relationships

Causality belongs in relationships, not in entity identity.

Example:

    Incorrect Flex Routing
    CAN_CAUSE
    RSL Discrepancy

This does not make the two concepts one entity.

It also does not establish that Incorrect Flex Routing is the cause in a particular case.

The relationship represents reusable technical possibility.

Current-case probability belongs to diagnostic reasoning.

---

## 31. Alarms

The Registry contains:

    ALARM

An alarm is a reusable canonical equipment or system alarm when independently useful for technical reasoning.

An alarm observed during a specific case is evidence referencing the canonical alarm entity.

The alarm definition and the alarm occurrence are not the same object.

---

## 32. Tests

The Registry contains:

    TEST

A test is a reusable diagnostic method capable of producing evidence.

Example:

    Compare Main and Diversity RSL

A canonical test entity describes the reusable technical test.

A completed execution of that test in a particular case is not a new canonical test entity.

It is a case-specific action/event that may produce evidence.

Registry-approved relationships may connect tests to technical conditions using semantics such as:

    TESTS_FOR
    TESTED_BY

---

## 33. Procedures

The Registry contains:

    PROCEDURE

A procedure represents a reusable defined technical or operational process.

Procedures may be connected to:

- products;
- configurations;
- scopes;
- requirements;
- tools;
- tests;
- corrective actions; and
- other canonical entities

using Registry-approved relationships.

A procedure performed during a specific case is an execution of the canonical procedure, not a new canonical procedure entity.

---

## 34. Corrective Actions

The Registry contains:

    CORRECTIVE_ACTION

A corrective action represents a reusable technical action intended to correct a confirmed or suspected problem.

Registry-approved remediation relationships include:

    RESOLVED_BY
    RESOLVES
    MITIGATED_BY
    MITIGATES

A corrective action performed during one case does not automatically prove that the action universally resolves the associated condition.

Case outcome and reusable technical knowledge remain separate.

---

## 35. Tools

Canonical tools use:

    tool_<UUID>

Example:

    Anritsu Site Master
    TOOL
    tool_<UUID>

Tools may participate in reusable technical relationships such as:

    MEASURES
    MEASURED_BY
    PERFORMED_WITH

where defined by the relationship Registry.

A specific field reading produced by a tool belongs to evidence.

The tool itself remains a reusable canonical entity.

---

## 36. Environmental Conditions and Obstructions

The Registry distinguishes:

- `ENVIRONMENTAL_CONDITION`; and
- `OBSTRUCTION`.

Examples may include:

    Heavy Rain
    High Wind
    Ice

Environmental conditions may affect technical behavior without becoming manufacturer-specific concepts.

An environmental observation during a case may reference a canonical environmental entity while preserving the actual observed details in evidence.

---

## 37. Scope

Canonical scopes use:

    scope_<UUID>

Examples include:

    Installation
    Commissioning
    Troubleshooting
    Maintenance

Scope is a technical or operational context.

Scope should affect applicability and reasoning without causing unnecessary duplication of canonical technical entities.

For example, `RSL Discrepancy` remains the same canonical symptom whether encountered during commissioning or troubleshooting.

---

## 38. Project Phase

The Registry contains:

    PROJECT_PHASE

Project phase may be represented independently when it materially affects:

- applicability;
- procedures;
- requirements;
- allowable actions;
- expected evidence; or
- diagnostic context.

Project phase is not interchangeable with scope unless the Registry and technical meaning explicitly establish that equivalence.

---

## 39. Standards, Requirements, and Constraints

The Registry distinguishes:

- `STANDARD`;
- `REQUIREMENT`; and
- `CONSTRAINT`.

These are canonical knowledge entities when independently useful.

Registry-approved relationships may express semantics such as:

    REQUIRES
    REQUIRED_BY
    PROHIBITS
    PROHIBITED_BY
    CONSTRAINS
    CONSTRAINED_BY
    APPLIES_TO
    GOVERNED_BY
    VALID_FOR

A.R.I.A. shall preserve the difference between:

- a document that contains a requirement;
- the canonical requirement itself; and
- the relationship establishing where that requirement applies.

---

## 40. Concepts

The Registry contains:

    CONCEPT

`CONCEPT` is intended for technical concepts that do not belong to a more specific canonical entity type.

A.R.I.A. should prefer a more precise Registry type when one exists.

`CONCEPT` shall not become a dumping ground for entities that were simply not classified carefully.

---

## 41. Customer Entities

The Registry currently contains:

    CUSTOMER

Customer entities may exist when customer identity is materially relevant to technical or operational context.

Customer-specific requirements should not cause generic technical concepts to be duplicated.

For example, a customer-specific closeout requirement may be a canonical `REQUIREMENT` associated with the relevant customer through approved relationship semantics.

The technical knowledge system shall remain technical in purpose.

Customer entities provide context where required; they do not transform A.R.I.A. into a general CRM.

---

## 42. Person and Role Entities

The Registry currently contains:

    PERSON
    ROLE

People and roles may participate in A.R.I.A.'s broader technical graph where required for:

- technical experience;
- observations;
- validated field history;
- procedures;
- competencies;
- diagnostic context; or
- auditability.

They are canonical entities but do not currently have dedicated person or role identity prefixes in the canonical contract.

Therefore they may use:

    ent_<UUID>

unless `entity_contracts.json` is deliberately extended.

User-specific technical history shall not be embedded as a monolithic entity description.

Historical experience belongs in the Experience Ledger and related relationships.

---

## 43. Canonical Entities vs. Case Objects

Not every object A.R.I.A. uses is a canonical technical entity.

The broader architecture includes first-class objects with their own identity classes.

Examples include:

    case_<UUID>
    evd_<UUID>
    hyp_<UUID>
    act_<UUID>
    exp_<UUID>
    rel_<UUID>
    ke_<UUID>

These objects shall not be serialized as ordinary records under `entity.schema.json` merely because they participate in the graph.

They have distinct architectural roles.

---

## 44. Canonical Entity vs. Case Evidence

A canonical entity represents reusable technical meaning.

Evidence represents an observation or information item relevant to a specific case.

Example:

    CANONICAL MEASUREMENT:
    Received Signal Level
    meas_<UUID>

    CASE EVIDENCE:
    Main RSL = -42 dBm
    evd_<UUID>

The evidence may reference the measurement entity.

The observation does not create another `MEASUREMENT` entity.

---

## 45. Canonical Entity vs. Hypothesis

A hypothesis is a case-specific evaluation of a possible explanation.

Example:

    CANONICAL ROOT CAUSE:
    Incorrect Flex Routing
    fm_<UUID>

    CURRENT CASE HYPOTHESIS:
    Incorrect Flex Routing is causing the observed diversity RSL discrepancy.
    hyp_<UUID>

The hypothesis references canonical technical knowledge.

It does not replace it.

Likewise, the existence of a canonical root cause does not mean that cause is active in the current case.

---

## 46. Canonical Entity vs. Experience

Experience Ledger records use:

    exp_<UUID>

A validated historical experience may reference:

- manufacturer entities;
- product entities;
- scopes;
- symptoms;
- failure modes;
- root causes;
- tests;
- procedures;
- corrective actions;
- measurements;
- tools; and
- other canonical entities.

The Experience Ledger records what happened historically.

Canonical entities represent the reusable technical concepts involved.

Repeated experience shall not create duplicate entities for the same technical concept.

---

## 47. Canonical Entity vs. Relationship

An entity represents a technical concept.

A relationship represents a semantic assertion between concepts or other eligible first-class objects.

For example:

    UBT-T
    MEMBER_OF
    Wavence

should not be encoded as arbitrary text such as:

    family = "Wavence"

when the relationship is important to reasoning.

Likewise:

    Received Signal Level
    MEASURED_IN
    dBm

is reusable graph knowledge.

Relationships belong in the relationship architecture.

---

## 48. Canonical Entity vs. Knowledge Graph Edge

Canonical entities are graph nodes.

Reusable persisted graph structure uses:

    ke_<UUID>

Semantic assertions use:

    rel_<UUID>

The entity record itself does not need to contain every edge connected to it.

A.R.I.A. should be able to retrieve relationships independently.

This prevents entity records from becoming monolithic knowledge containers.

---

## 49. Provenance

Every material canonical entity should preserve provenance describing how the concept entered A.R.I.A.'s knowledge system.

Possible origins may include:

- manufacturer documentation;
- manufacturer technical support;
- engineering documentation;
- standards;
- approved internal technical sources;
- structured imports;
- validated field discovery;
- approved extraction;
- human technical contribution; or
- migration from legacy A.R.I.A. knowledge.

Provenance semantics are governed by:

    Core/Schemas/entity_contracts.json

Entity provenance and relationship provenance are independent.

For example, A.R.I.A. may know that an `AIM` component exists from one source and know that it `MATES_WITH` another component from a different source.

Both assertions must remain independently traceable.

---

## 50. Confidence

Entity confidence represents confidence in the quality or support of the entity assertion.

The canonical confidence contract is governed by:

    Core/Schemas/entity_contracts.json

The entity machine schema represents confidence using:

    value
    basis

Confidence is not probability.

Entity confidence shall not be interpreted as:

- probability that a hypothesis is true;
- probability that a failure will occur;
- relationship strength;
- evidence confidence; or
- diagnostic priority.

---

## 51. Lifecycle Status

Canonical entity lifecycle status is validated by `entity.schema.json`.

Current lifecycle states are:

    PROPOSED
    ACTIVE
    DEPRECATED
    SUPERSEDED
    REJECTED

Lifecycle answers whether and how the entity should participate in the current knowledge system.

Lifecycle is separate from validation state.

---

## 52. Validation State

Current entity validation states are:

    PROPOSED
    REVIEWED
    VALIDATED
    DISPUTED
    REJECTED

Entity validation does not automatically validate every relationship involving the entity.

For example:

    AIM

may be a validated canonical component while a newly inferred relationship involving AIM remains unreviewed.

Entity truth and relationship truth remain separable.

---

## 53. Candidate Entities

Automated extraction, model inference, imported terminology, or field discovery may identify a candidate entity.

Detection does not make the candidate authoritative.

Before promotion, A.R.I.A. should determine whether the candidate is:

- genuinely new;
- an alias;
- a duplicate;
- a contextual instance;
- a case-specific value;
- a typo;
- a product variant;
- a revision;
- an existing concept under different terminology; or
- a valid new canonical entity.

Candidate entities should enter an appropriate validation process.

---

## 54. Human Review

Where required, entity review should support:

- approval;
- rejection;
- canonical-name correction;
- entity-type correction;
- alias assignment;
- duplicate detection;
- merge;
- split;
- provenance attachment;
- contextual clarification; and
- requests for additional validation.

Review actions should remain auditable.

A model suggestion alone shall not permanently alter canonical identity.

---

## 55. Supersession

An entity may be superseded without deletion.

The machine schema supports:

- `superseded_at`; and
- `superseded_by`.

The relationship Registry also provides versioning semantics including:

    SUPERSEDES
    SUPERSEDED_BY

Supersession preserves historical reasoning.

A historical case referencing an older product, revision, requirement, or procedure must continue to resolve correctly after newer knowledge is introduced.

---

## 56. Deprecation

Deprecated entities remain queryable where historically relevant.

Deprecation may indicate:

- obsolete terminology;
- retired product;
- old hardware revision;
- obsolete procedure;
- replaced standard;
- retired software; or
- other non-current technical concepts.

Deprecated does not mean historically false.

Temporal and contextual applicability must be preserved.

---

## 57. Legacy Identifiers

The machine schema provides:

    legacy_identifiers

Legacy identifiers exist for:

- migration;
- reconciliation;
- historical imports;
- auditability; and
- backward traceability.

They are not authoritative canonical identities.

For example, a historical identifier such as:

    ENT-000427

may be retained as a legacy identifier after migration to:

    prod_<UUID>

The new typed UUID remains authoritative.

---

## 58. Entity Merge

Duplicate canonical entities may occasionally be discovered.

A controlled merge shall preserve:

- canonical identity decisions;
- provenance;
- aliases;
- legacy identifiers;
- relationships;
- case references;
- experience references;
- audit history; and
- historical traceability.

Automated similarity alone shall not permanently merge canonical entities.

A merge is a knowledge-governance action.

---

## 59. Entity Split

An entity may later be discovered to represent multiple technically distinct concepts.

A.R.I.A. shall support controlled entity splitting.

A split may require:

- creation of new canonical identities;
- reassignment of aliases;
- relationship reclassification;
- provenance preservation;
- historical case reconciliation;
- experience reconciliation; and
- audit records.

Historical information should be reclassified where justified rather than silently deleted.

---

## 60. Metadata Extensibility

The machine schema provides controlled:

    metadata

for entity-type-specific technical information.

Metadata may support future domain-specific requirements.

Metadata shall not be used to:

- create hidden relationship systems;
- duplicate canonical entities;
- store case-specific evidence;
- replace Registry vocabulary;
- bypass provenance;
- bypass validation; or
- serialize entire technical documents into entity records.

Core semantic structure remains strongly modeled.

---

## 61. Product-Specific Metadata

Some technical attributes may reasonably remain metadata when they describe the entity rather than another independently useful concept.

However, if an attribute becomes independently useful for:

- reasoning;
- relationships;
- filtering;
- applicability;
- historical analysis; or
- reuse,

A.R.I.A. should consider representing it as a canonical entity instead.

The choice should be driven by technical reasoning value, not convenience alone.

---

## 62. Relationship Integrity

Entity records shall not become hidden relationship stores.

For example, avoid using arbitrary metadata to encode:

    manufacturer = Nokia
    family = Wavence
    unit = dBm
    tool = Anritsu

when those concepts are canonical entities and the relationship matters to reasoning.

Prefer Registry-approved semantic relationships such as:

    MANUFACTURED_BY
    MEMBER_OF
    MEASURED_IN
    MEASURED_BY

where appropriate.

This preserves graph consistency and queryability.

---

## 63. No Duplicate Entity Vocabulary

`Core/Registries/entity_types.json` is the sole canonical entity-type vocabulary.

This document shall not maintain a second exhaustive entity-type registry.

`Core/Schemas/entity.schema.json` shall not maintain a competing enum of Registry values unless architecture is deliberately changed to generate or synchronize that validation automatically.

Manufacturer knowledge files shall not independently create entity classes.

Extraction systems shall not invent permanent entity types.

The Registry owns vocabulary.

---

## 64. No Duplicate Relationship Vocabulary

`Core/Registries/relationship_types.json` is the sole canonical relationship vocabulary.

Entity documentation may use relationship examples only when those semantics exist in the Registry.

This document shall not invent relationship names such as:

    OPERATES_AT
    AFFECTED_BY
    BELONGS_TO
    INTERFACES_WITH
    USED_BY

unless those relationship types are deliberately added to the Registry.

Technical meaning shall conform to the canonical relationship architecture.

---

## 65. Model Independence

Canonical entity identity exists independently of the language model.

A model may:

- recognize entities;
- propose candidate entities;
- resolve aliases;
- identify possible duplicates;
- interpret ambiguous terminology;
- propose relationships;
- explain entities; and
- assist validation.

The model is not the authoritative Registry.

Changing the model shall not change canonical entity identity.

---

## 66. Repository Independence

Canonical identity shall not depend upon repository location.

Moving manufacturer documents, reorganizing folders, changing databases, or replacing application components shall not alter canonical identity.

Repository files are sources and implementation artifacts.

Canonical identity belongs to A.R.I.A.'s knowledge architecture.

---

## 67. Database Readiness

The entity architecture shall map cleanly into structured persistence.

Conceptually, a canonical entity record includes strongly structured fields such as:

    id
    entity_type
    canonical_name
    description
    status
    validation_state
    valid_from
    valid_to
    deprecated_at
    superseded_at
    superseded_by
    created_at
    updated_at
    created_by
    updated_by

Aliases, relationships, provenance, and other structures may be normalized or separately persisted as implementation evolves.

Database design shall preserve the canonical contracts rather than redefining them.

---

## 68. Entity Creation Rules

Before creating a new canonical entity, A.R.I.A. or the reviewing system should ask:

1. Does this technical concept already exist?
2. Is the proposed term merely an alias?
3. Is it only a contextual instance of an existing entity?
4. Is it a case-specific observation rather than reusable knowledge?
5. Is it a hypothesis rather than a canonical technical concept?
6. Is it an Experience Ledger record rather than a canonical concept?
7. Is it a relationship rather than an entity?
8. Is it a product variant rather than a new product?
9. Is it a hardware/software revision?
10. Does representing it independently materially improve reasoning or retrieval?
11. Can its meaning be clearly defined?
12. Is there sufficient provenance to justify creation?
13. Does an approved entity type exist in the Registry?
14. What is the correct canonical identity prefix?

If the answers indicate duplication, A.R.I.A. should reuse the existing entity.

---

## 69. Example: Received Signal Level

Conceptually:

    ID:
    meas_<UUID>

    ENTITY TYPE:
    MEASUREMENT

    CANONICAL NAME:
    Received Signal Level

    ALIASES:
    RSL
    RX Level
    Receive Level

    STATUS:
    ACTIVE

    VALIDATION STATE:
    VALIDATED

    DESCRIPTION:
    Received RF power measured at the applicable receiver point.

Related reusable knowledge may include:

    Received Signal Level
    MEASURED_IN
    dBm

    Received Signal Level
    MEASURED_BY
    Applicable Measurement Tool

The measurement entity exists once.

A specific case observation such as:

    -54 dBm

is evidence referencing the canonical measurement and unit.

---

## 70. Example: UBT-T

Conceptually:

    ID:
    prod_<UUID>

    ENTITY TYPE:
    PRODUCT

    CANONICAL NAME:
    UBT-T

    STATUS:
    ACTIVE

Related reusable knowledge may include:

    UBT-T
    MANUFACTURED_BY
    Nokia

    UBT-T
    MEMBER_OF
    Wavence

    UBT-T
    HAS_VARIANT
    UBT-T 18 GHz

    UBT-T
    HAS_COMPONENT
    Applicable Component

    UBT-T
    SUPPORTS
    Applicable Configuration

Every relationship type in this example is governed by the canonical relationship Registry.

The product entity should not require separate duplicate knowledge trees for every project, case, frequency, technician, or procedure.

---

## 71. Example: Symptom and Root Cause

Conceptually:

    SYMPTOM:
    RSL Discrepancy
    sym_<UUID>

    ROOT CAUSE:
    Incorrect Flex Routing
    fm_<UUID>

Reusable technical relationship:

    Incorrect Flex Routing
    CAN_CAUSE
    RSL Discrepancy

Current-case hypothesis:

    hyp_<UUID>

Current-case evidence:

    evd_<UUID>

These are four different architectural concepts.

A.R.I.A. shall preserve those distinctions.

---

## 72. Example: Person and Experience

Conceptually:

    PERSON:
    Technician
    ent_<UUID>

A validated historical technical event may be represented in:

    exp_<UUID>

The Experience Ledger may reference:

- the person;
- manufacturer;
- product;
- scope;
- symptom;
- root cause;
- action;
- evidence; and
- outcome.

The person's canonical entity should not become a giant serialized history of everything that technician has ever encountered.

Experience remains independently queryable.

---

## 73. Technical Resource Boundary

A.R.I.A. is intended to be a technical resource.

The Entity Architecture therefore exists primarily to support:

- telecommunications equipment knowledge;
- RF engineering;
- configuration;
- diagnostics;
- procedures;
- technical requirements;
- technical experience;
- field troubleshooting;
- technical reasoning; and
- related operational context necessary to perform that technical mission.

The existence of `PERSON`, `CUSTOMER`, `ROLE`, or similar contextual entity types does not authorize expansion into unrelated CRM, HR, sales, financial, or general business knowledge.

Contextual entities should be represented only when they materially support A.R.I.A.'s technical function.

---

## 74. Entity Integrity Rules

A.R.I.A. shall preserve the following invariants:

1. Every persisted canonical technical entity has stable typed identity.
2. Identity follows `Core/Schemas/entity_contracts.json`.
3. Entity type follows `Core/Registries/entity_types.json`.
4. Machine structure follows `Core/Schemas/entity.schema.json`.
5. Relationship semantics follow `Core/Registries/relationship_types.json`.
6. The most specific established identity prefix is used.
7. `ent_<UUID>` is the generic fallback, not a competing universal prefix.
8. Names are not identity.
9. Aliases are not automatically entities.
10. Shared technical concepts are not duplicated by manufacturer without technical justification.
11. Products are not duplicated by project, site, customer, technician, or case.
12. Product variants exist only when technically meaningful.
13. Measurements are concepts; measured case values are evidence.
14. Symptoms are not causes.
15. Canonical root causes are not current-case hypotheses.
16. Tests and procedures are reusable concepts; executions are case-specific.
17. Tools are canonical resources; readings are evidence.
18. Entity confidence is not probability.
19. Lifecycle state and validation state remain distinct.
20. Deprecated and superseded entities remain available for historical reasoning.
21. Legacy identifiers are not canonical identity.
22. Metadata does not become a hidden relationship system.
23. Case objects are not serialized as ordinary canonical entities.
24. Experience records are not canonical entities.
25. Semantic relationships are not canonical entities.
26. Knowledge Graph edges are not canonical entities.
27. Automated extraction may propose entities but does not silently establish canonical truth.
28. Duplicate entities are merged only through controlled reconciliation.
29. Entity splits preserve historical traceability.
30. A.R.I.A.'s entity system remains focused on its technical mission.

---

## 75. Architecture Summary

The canonical entity layer can be summarized as:

    TECHNICAL CONCEPT
          |
          v
    CANONICAL ENTITY
    typed UUID identity
          |
          +------------------------------+
          |                              |
          v                              v
    rel_<UUID>                      reusable references
    semantic relationships          from cases/experience
          |
          v
    ke_<UUID>
    reusable graph structure

Case-specific reasoning remains separate:

    case_<UUID>
        |
        +--> evd_<UUID>
        |
        +--> hyp_<UUID>
        |
        +--> act_<UUID>

Validated historical experience remains separate:

    exp_<UUID>

These structures may reference canonical entities without becoming duplicate canonical entities themselves.

---

## 76. Final Principle

A.R.I.A.'s Entity Architecture exists to give technical knowledge durable identity.

A canonical entity is not merely a word in a document.

It is a stable, reusable technical concept with:

- canonical identity;
- controlled classification;
- human-readable terminology;
- aliases;
- provenance;
- validation;
- lifecycle;
- temporal applicability;
- relationships; and
- historical continuity.

A.R.I.A. shall create a new entity when a genuinely distinct technical concept needs independent identity.

A.R.I.A. shall reuse an existing entity when the concept already exists.

A.R.I.A. shall use relationships to express how entities interact.

A.R.I.A. shall use evidence to represent what was observed.

A.R.I.A. shall use hypotheses to represent what is being evaluated.

A.R.I.A. shall use experience to preserve what happened historically.

Maintaining these boundaries allows A.R.I.A.'s technical intelligence to grow without sacrificing consistency, explainability, or trust.
