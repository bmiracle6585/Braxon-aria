# A.R.I.A. Entity Schema

**Document Type:** Cognitive Knowledge Data Specification  
**Authority:** Subordinate to `Core/Knowledge/knowledge_graph.md` and `Core/Persona/ARIA_CONSTITUTION.md`  
**Version:** 0.1

---

## 1. Purpose

This document defines the required structure of canonical entities within A.R.I.A.'s Knowledge Graph.

An entity represents one identifiable technical, operational, organizational, or contextual concept.

Entities shall have stable identities independent of:

- file location;
- display name;
- manufacturer naming convention;
- language-model terminology;
- repository structure;
- database migration;
- aliases; or
- future system implementations.

A.R.I.A. shall reference entities by stable identity.

Human-readable names may change.

The canonical identity shall not.

---

## 2. Entity Design Principle

An entity should exist when representing the concept independently is useful for:

- reasoning;
- retrieval;
- relationship modeling;
- contextual filtering;
- source attribution;
- experience analysis;
- diagnostic routing; or
- future expansion.

Not every word or phrase should become an entity.

The objective is meaningful structure, not maximum entity count.

---

## 3. Required Entity Fields

Every canonical entity shall contain at minimum:

### 3.1 Entity ID

A stable unique identifier.

Example:

`ENT-000001482`

The identifier shall not encode mutable business meaning.

Avoid identifiers such as:

`NOKIA-UBTT-18GHZ-001`

because product names, classifications, or hierarchies may change.

The stable ID remains permanent.

---

### 3.2 Entity Type

Defines the entity's primary class.

Examples:

`MANUFACTURER`

`PRODUCT_FAMILY`

`PRODUCT`

`COMPONENT`

`MEASUREMENT`

`SYMPTOM`

`FAILURE_MODE`

`PROCEDURE`

`TEST`

`CONCEPT`

Entity types shall come from an approved entity-type registry.

---

### 3.3 Canonical Name

The preferred human-readable name.

Example:

`Received Signal Level`

or:

`UBT-T`

The canonical name may be updated if terminology changes.

The Entity ID remains unchanged.

---

### 3.4 Status

Defines whether the entity is currently authoritative and usable.

Initial states should include:

`PROPOSED`

`ACTIVE`

`DEPRECATED`

`SUPERSEDED`

`REJECTED`

An entity created by automated extraction shall not become authoritative merely because it was detected.

---

## 4. Optional Core Fields

Entities may also contain:

- description;
- short description;
- aliases;
- manufacturer part number;
- model number;
- revision;
- unit;
- category;
- parent classifications;
- effective date;
- retirement date;
- source authority;
- validation state;
- created timestamp;
- modified timestamp;
- created by;
- modified by; and
- notes.

Optional fields shall not be abused to store relationships that belong in the relationship system.

For example:

Do not store:

`manufacturer = Nokia`

as arbitrary text if:

`UBT-T MANUFACTURED_BY Nokia`

should exist as a graph relationship.

---

## 5. Entity Types

The initial entity-type registry should support at least the following:

### Technical Domain

- DOMAIN
- TECHNOLOGY
- CONCEPT
- STANDARD
- REQUIREMENT
- CONSTRAINT

### Manufacturer and Product

- MANUFACTURER
- PRODUCT_FAMILY
- PRODUCT
- PRODUCT_VARIANT
- HARDWARE_REVISION
- FIRMWARE
- SOFTWARE_VERSION

### Physical System

- COMPONENT
- INTERFACE
- PORT
- CABLE
- CONNECTOR
- ANTENNA
- MOUNT
- POWER_COMPONENT
- NETWORK_COMPONENT

### RF and Engineering

- FREQUENCY_BAND
- CHANNEL
- POLARIZATION
- MODULATION
- CONFIGURATION
- TOPOLOGY
- PARAMETER
- MEASUREMENT
- UNIT

### Diagnostics

- SYMPTOM
- CONDITION
- FAILURE_MODE
- CAUSE
- TEST
- PROCEDURE
- CORRECTIVE_ACTION
- OUTCOME
- ALARM

### Operational Context

- SCOPE_OF_WORK
- PROJECT_PHASE
- ENVIRONMENTAL_CONDITION
- CUSTOMER_REQUIREMENT

This registry may expand.

Expansion shall normally involve adding new entity types rather than redesigning existing ones.

---

## 6. Aliases

An entity may have multiple aliases.

Example:

ENTITY:
Received Signal Level

ALIASES:

- RSL
- RX Level
- Receive Level
- Received Level

Aliases may contain metadata such as:

- manufacturer;
- source;
- terminology type;
- abbreviation status;
- effective date;
- deprecated status; and
- confidence.

Aliases shall not automatically create separate entities.

---

## 7. Alias Collision

The same alias may refer to different concepts in different contexts.

A.R.I.A. shall support contextual alias resolution.

For example:

`AIM`

may require product or manufacturer context to determine the intended entity.

Alias resolution may consider:

- active manufacturer;
- active product;
- conversation context;
- current diagnostic case;
- scope of work; and
- neighboring concepts.

A.R.I.A. shall not permanently merge entities solely because they share an abbreviation.

---

## 8. Canonical Description

An entity may contain a concise canonical description.

Example:

ENTITY:
Received Signal Level

DESCRIPTION:

Measured received RF power at the applicable receiver point, generally represented in dBm within A.R.I.A.'s Microwave Backhaul domain.

The description shall define the entity.

It shall not attempt to contain every known relationship involving the entity.

Relationships belong in the graph.

---

## 9. Manufacturer Independence

Shared technical concepts should remain manufacturer-independent when technically appropriate.

Example:

ENTITY:
Received Signal Level

shall normally be shared across:

- Nokia;
- Aviat;
- Ceragon;
- Ericsson;
- DragonWave; and
- future manufacturers.

Manufacturer-specific behavior shall be represented through relationships, applicability, or manufacturer-specific entities when required.

Do not create:

- Nokia RSL;
- Aviat RSL;
- Ceragon RSL;

unless those names represent technically distinct concepts rather than different implementations of the same measurement.

---

## 10. Product Variants

A.R.I.A. shall distinguish between a product and a product variant only when the distinction provides meaningful technical value.

Example:

PRODUCT:
UBT-T

Possible variant dimensions may include:

- frequency band;
- hardware revision;
- power capability;
- interface configuration; or
- regional variant.

A variant should be created when the variant has sufficiently different:

- specifications;
- compatibility;
- behavior;
- procedures;
- relationships; or
- failure characteristics.

Do not create a new entity merely because a product is being discussed in a different context.

---

## 11. Frequency Representation

Frequency shall not be encoded only into product names.

Example:

Do not rely upon:

`UBT-T 18GHz`

as the sole representation.

Prefer:

ENTITY:
UBT-T

RELATIONSHIP:
UBT-T OPERATES_AT 18 GHz Band

If the 18 GHz version represents a materially different hardware variant, a `PRODUCT_VARIANT` may also be created and linked to the frequency band.

---

## 12. Measurement Entities

Measurements shall be represented canonically.

Example:

ENTITY TYPE:
MEASUREMENT

NAME:
Received Signal Level

UNIT:
dBm

Related information may include:

- measurement point;
- expected range;
- applicability;
- instrument source;
- engineered target; and
- interpretation.

The numeric value measured during a specific case is not the canonical entity.

It is evidence referencing the measurement entity.

Example:

CANONICAL ENTITY:
Received Signal Level

CASE EVIDENCE:
-54 dBm

---

## 13. Symptoms and Causes

Symptoms and causes shall remain distinct.

Example:

SYMPTOM:
RSL Discrepancy

CAUSE:
Incorrect Flex Routing

Relationship:

Incorrect Flex Routing
CAN_CAUSE
RSL Discrepancy

A.R.I.A. shall not collapse the symptom and the cause into the same entity simply because they frequently occur together.

---

## 14. Tests and Procedures

Tests and procedures may be represented as entities when they are reusable across cases.

Example:

TEST:
Compare Main and Diversity RSL

PROCEDURE:
Verify Radio A/B Configuration

These entities may connect to:

- hypotheses;
- measurements;
- required tools;
- prerequisites;
- risks;
- costs;
- expected information gain; and
- corrective actions.

A completed execution of the test in a real case shall be represented as a case event referencing the canonical test entity.

---

## 15. Entity Scope

Some entities are globally applicable.

Others are inherently contextual.

An entity may carry scope metadata when the concept itself is limited.

Examples:

GLOBAL CONCEPT:
Cross Polarization

PRODUCT-SPECIFIC ENTITY:
UBT-T AIM Interface

CUSTOMER-SPECIFIC REQUIREMENT:
Customer X Microwave Closeout Requirement

Scope shall not be used to duplicate generic concepts unnecessarily.

---

## 16. Provenance

Every canonical entity should preserve provenance for how it entered A.R.I.A.'s knowledge system.

Possible origins include:

- manually created;
- manufacturer source;
- Braxon-controlled source;
- approved extraction;
- imported structured data;
- validated field discovery; or
- migration from legacy A.R.I.A. knowledge.

Entity existence and individual relationships may have different provenance.

For example:

ENTITY:
AIM

may be established from one source.

RELATIONSHIP:
AIM MATES_WITH UBT-T

may be established from another.

Both shall remain traceable.

---

## 17. Validation

Entities may be created before they are fully validated.

Initial validation states may include:

`PROPOSED`

`REVIEWED`

`VALIDATED`

`REJECTED`

Entity validation does not automatically validate every relationship associated with that entity.

Entity truth and relationship truth shall remain separable.

---

## 18. Supersession

An entity may be superseded without being deleted.

Example:

Old product entity remains historically relevant.

New product supersedes it.

Relationship:

NEW_PRODUCT
SUPERSEDES
OLD_PRODUCT

Historical cases referencing the old product shall continue to resolve correctly.

---

## 19. Deprecation

Deprecated entities shall remain queryable for historical reasoning.

Deprecation may indicate:

- product no longer supported;
- terminology no longer preferred;
- old revision;
- obsolete procedure;
- retired standard; or
- replaced technology.

Deprecated does not mean historically false.

---

## 20. Entity Merge

Duplicate entities may occasionally be discovered.

A.R.I.A. shall support controlled entity merge.

A merge shall:

- preserve source provenance;
- preserve legacy identifiers;
- redirect relationships;
- preserve audit history; and
- avoid silently losing case references.

Entity merging shall require explicit validation.

Automated similarity alone shall not permanently merge canonical entities.

---

## 21. Entity Split

An entity may later be discovered to represent multiple distinct concepts.

A.R.I.A. shall support controlled entity splitting.

Example:

A term originally treated as one component is later discovered to represent:

- hardware component A;
- hardware component B.

A split shall preserve historical auditability.

Historical relationships may require reclassification rather than deletion.

---

## 22. Human-Readable Slugs

A.R.I.A. may optionally maintain human-readable slugs for debugging, URLs, exports, or administrative interfaces.

Example:

`received-signal-level`

or:

`nokia-ubt-t`

Slugs shall not be authoritative identifiers.

Changing a slug shall not break stored relationships.

---

## 23. Entity Metadata Extensibility

The entity system shall permit future metadata expansion.

The initial implementation should avoid placing every possible field directly into a single rigid table if doing so would make future entity types difficult to support.

However, flexibility shall not come at the expense of data integrity.

Core identity fields shall remain strongly structured.

Optional domain-specific metadata may use controlled extensibility.

---

## 24. Entity Example: RSL

Conceptually:

ENTITY ID:
ENT-000001

ENTITY TYPE:
MEASUREMENT

CANONICAL NAME:
Received Signal Level

ALIASES:
RSL
RX Level
Receive Level

UNIT:
dBm

STATUS:
ACTIVE

DESCRIPTION:
Received RF power measured at the applicable receiver point.

Possible relationships:

RSL
AFFECTED_BY
Antenna Alignment

RSL
AFFECTED_BY
Path Loss

RSL
AFFECTED_BY
Weather

RSL
AFFECTED_BY
Radio TX Power

RSL
USED_BY
Alignment Procedure

RSL
APPLIES_TO
Multiple Manufacturers

The entity exists once.

Its relationships create its technical meaning within the graph.

---

## 25. Entity Example: UBT-T

Conceptually:

ENTITY ID:
ENT-000427

ENTITY TYPE:
PRODUCT

CANONICAL NAME:
UBT-T

STATUS:
ACTIVE

Possible relationships:

UBT-T
MANUFACTURED_BY
Nokia

UBT-T
BELONGS_TO
Wavence

UBT-T
INTERFACES_WITH
AIM

UBT-T
OPERATES_AT
Applicable Frequency Bands

UBT-T
SUPPORTS
Applicable Configurations

The product entity shall not require separate duplicate knowledge trees for every band or procedure.

---

## 26. Entity Example: User

People shall exist as entities within A.R.I.A.'s broader graph architecture, but technical user experience shall not be embedded directly into a monolithic entity record.

Example:

ENTITY ID:
PERSON-0017

ENTITY TYPE:
PERSON

NAME:
Clayton

Relationships may connect Clayton to:

- cases;
- observations;
- procedures;
- products;
- scopes;
- competencies;
- roles; and
- outcomes.

The user's technical history remains derived from authoritative relationships and cases.

---

## 27. Entity Creation Rules

Before creating a new canonical entity, A.R.I.A. or the reviewing system should ask:

1. Does this concept already exist?
2. Is this merely an alias?
3. Is this only a contextual instance of an existing entity?
4. Is this a case-specific value rather than a canonical concept?
5. Does representing it independently improve reasoning or retrieval?
6. Can its meaning be clearly defined?
7. Is there sufficient provenance to justify creation?

If the answer indicates duplication, the existing entity should be reused.

---

## 28. Database Readiness

The entity schema shall be designed so it can later map cleanly into a structured database.

Conceptually, an entity record may eventually include fields such as:

- id;
- entity_type_id;
- canonical_name;
- description;
- status;
- validation_state;
- effective_at;
- deprecated_at;
- created_at;
- updated_at;
- created_by;
- updated_by.

Aliases, relationships, sources, and context-specific metadata should normally exist in related structures rather than being serialized into unqueryable text.

---

## 29. Model Independence

Canonical entity identity shall exist independently of the language model.

The model may:

- recognize entities;
- propose new entities;
- map aliases;
- interpret ambiguous terminology; and
- explain entities.

The language model shall not be the authoritative registry of what entities exist.

Changing the model shall not change entity identity.

---

## 30. Design Objective

The Entity Schema exists so that A.R.I.A. can continuously expand without turning her knowledge into an unmanageable directory tree or collection of duplicate terms.

A new product should be added as an entity.

A new manufacturer should be added as an entity.

A new failure mode should be added as an entity.

A new technical concept should be added as an entity.

Existing concepts should be reused through relationships wherever possible.

A.R.I.A.'s intelligence shall grow primarily by increasing the richness of the connections among stable canonical concepts.
