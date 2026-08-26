# A.R.I.A. Canonical Knowledge Graph

**Document Type:** Cognitive Knowledge System Specification  
**Authority:** Subordinate to `Core/Persona/ARIA_CONSTITUTION.md`  
**Version:** 0.1

---

## 1. Purpose

This document defines the architecture of A.R.I.A.'s Canonical Knowledge Graph.

The Knowledge Graph represents A.R.I.A.'s structured technical understanding of telecommunications and, primarily, Microwave Backhaul.

Its purpose is to allow technical knowledge to exist as an interconnected network of concepts and relationships rather than as a collection of isolated files or rigid directory paths.

A.R.I.A. shall not require a piece of knowledge to exist in only one location.

A technical concept may participate simultaneously in many manufacturers, products, procedures, symptoms, failure modes, measurements, configurations, and diagnostic routes.

The Knowledge Graph shall represent these relationships without duplicating the underlying canonical concept unnecessarily.

---

## 2. The Graph Is Shared

A.R.I.A. shall maintain one shared Canonical Knowledge Graph.

The Knowledge Graph shall not be replicated for every user.

User-specific experience, competency, history, and interaction context shall exist as overlays and relationships referencing the shared graph.

Conceptually:

CANONICAL KNOWLEDGE
        |
        +---- Steve Experience Overlay
        |
        +---- Clayton Experience Overlay
        |
        +---- Michael Experience Overlay
        |
        +---- Future User Overlay

Technical truth remains shared.

Individual experience modifies how that truth is applied.

---

## 3. Knowledge Is Not a Directory

Filesystem organization may be used for source management and human navigation.

Filesystem location shall not define the meaning of knowledge.

A.R.I.A. shall not require structures such as:

Manufacturers
/Nokia
/Wavence
/UBT
/UBT-T
/18GHz
/RSL
/Troubleshooting
/Alignment

as the only route to knowledge.

Instead:

RSL

may connect directly to:

- alignment;
- antenna gain;
- frequency;
- path loss;
- weather;
- obstruction;
- polarization;
- radio output;
- receiver performance;
- waveguide;
- flex;
- connectors;
- OCM;
- AIM;
- configuration;
- Nokia;
- Aviat;
- Ceragon;
- UBT-T;
- commissioning;
- troubleshooting; and
- historical cases.

The graph shall permit all applicable relationships simultaneously.

---

## 4. Canonical Entities

A canonical entity represents one identifiable concept within A.R.I.A.'s technical knowledge.

Initial entity classes may include:

- DOMAIN;
- TECHNOLOGY;
- MANUFACTURER;
- PRODUCT_FAMILY;
- PRODUCT;
- PRODUCT_VARIANT;
- COMPONENT;
- INTERFACE;
- PORT;
- CABLE;
- ANTENNA;
- FREQUENCY_BAND;
- CONFIGURATION;
- TOPOLOGY;
- FEATURE;
- PARAMETER;
- MEASUREMENT;
- UNIT;
- SYMPTOM;
- CONDITION;
- FAILURE_MODE;
- CAUSE;
- PROCEDURE;
- TEST;
- TOOL;
- CORRECTIVE_ACTION;
- ALARM;
- STANDARD;
- REQUIREMENT;
- CONSTRAINT;
- CONCEPT; and
- SCOPE_OF_WORK.

This list may expand.

Adding a new entity class should not require redesigning the entire Knowledge Graph.

---

## 5. Stable Entity Identity

Every canonical entity shall have a stable unique identity independent of:

- display name;
- file name;
- manufacturer naming convention;
- database location;
- language-model terminology;
- abbreviation; or
- future repository reorganization.

Conceptually:

ENTITY ID:
CONCEPT-00001482

TYPE:
MEASUREMENT

CANONICAL NAME:
Received Signal Level

ALIASES:
RSL
Receive Signal Level
Rx Level
RX Signal Level

The canonical identity remains stable even when terminology varies.

---

## 6. Aliases and Terminology

A.R.I.A. shall support multiple names referring to the same canonical concept.

Example:

CANONICAL ENTITY:
Received Signal Level

ALIASES:
RSL
Rx Level
RX Level
Receive Level

Manufacturer-specific terminology may also reference the same underlying concept when technically appropriate.

Aliases shall not require duplicate canonical entities unless the terms represent materially different technical concepts.

---

## 7. Relationships

Entities shall be connected through typed relationships.

Initial relationship types may include:

- IS_A;
- PART_OF;
- BELONGS_TO;
- MANUFACTURED_BY;
- VARIANT_OF;
- CONNECTED_TO;
- MATES_WITH;
- INTERFACES_WITH;
- INSTALLED_ON;
- CONFIGURED_AS;
- OPERATES_AT;
- MEASURED_BY;
- MEASURES;
- AFFECTS;
- CAN_CAUSE;
- CAN_INDICATE;
- SUPPORTS;
- CONTRADICTS;
- REQUIRES;
- PRECEDES;
- TESTED_BY;
- VERIFIED_BY;
- CORRECTED_BY;
- RESOLVED_BY;
- APPLIES_TO;
- INCOMPATIBLE_WITH;
- DEPENDS_ON; and
- RELATED_TO.

Generic relationships such as `RELATED_TO` should be used sparingly when a more precise relationship is available.

Relationship meaning shall be explicit enough to support machine reasoning.

---

## 8. Relationships Are First-Class Knowledge

A.R.I.A.'s intelligence depends not only on entities but on the relationships between them.

For example:

UBT-T
MANUFACTURED_BY
Nokia

UBT-T
PART_OF
Wavence

UBT-T
INTERFACES_WITH
AIM

Incorrect Flex Routing
CAN_CAUSE
RSL Discrepancy

Cross Polarization
CAN_CAUSE
RSL Degradation

RSL
MEASURED_IN
dBm

These relationships shall be queryable independently of the original document from which they were learned.

Their provenance shall remain preserved.

---

## 9. Relationship Context

A relationship may be true only under specific conditions.

Therefore relationships may carry context such as:

- manufacturer;
- product family;
- product;
- product variant;
- hardware revision;
- firmware;
- frequency;
- configuration;
- topology;
- scope;
- environment;
- date range; and
- customer-specific implementation.

Example:

RELATIONSHIP:
Component A MATES_WITH Component B

APPLIES TO:
Specific Nokia product family

HARDWARE REVISION:
Rev C and later

A.R.I.A. shall not generalize contextual relationships beyond their supported applicability.

---

## 10. Relationship Strength

Some relationships represent deterministic technical facts.

Others represent probabilistic or experiential associations.

These shall remain distinguishable.

Example:

UBT-T
MANUFACTURED_BY
Nokia

may be treated as a deterministic relationship.

Whereas:

Incorrect Flex Routing
CAN_CAUSE
RSL Discrepancy

represents a causal relationship whose diagnostic relevance depends upon context.

The Knowledge Graph shall permit different relationship semantics without reducing every edge to the same numerical meaning.

---

## 11. Canonical Knowledge and Probability

The Knowledge Graph defines what relationships are technically possible or established.

The Probability Model determines how likely a hypothesis is in the current context.

These functions shall remain separate.

For example:

KNOWLEDGE GRAPH:

Incorrect Flex Routing
CAN_CAUSE
RSL Discrepancy

EXPERIENCE LEDGER:

Incorrect Flex Routing occurred in 18 of 126 comparable validated cases.

CURRENT CASE:

Evidence increases the probability of Incorrect Flex Routing to 47 percent.

The canonical relationship did not change.

The current diagnostic probability did.

---

## 12. Canonical Knowledge and Experience

Canonical Knowledge represents:

**What A.R.I.A. knows about the domain.**

The Experience Ledger represents:

**What A.R.I.A. has observed happening.**

These systems shall reference each other without becoming the same system.

A repeated field outcome may increase the diagnostic relevance of an existing relationship.

It shall not automatically redefine the technical relationship itself.

---

## 13. Manufacturer Knowledge

Manufacturer-specific information shall be represented through relationships and context rather than isolated knowledge silos.

Example:

Nokia
MANUFACTURES
UBT-T

UBT-T
BELONGS_TO
Wavence

UBT-T
USES
AIM

This permits shared concepts such as:

RSL
XPIC
ACM
BER
MSE
Cross Polarization
Antenna Alignment

to remain canonical while participating in Nokia-specific relationships.

A.R.I.A. shall avoid unnecessary duplicate concepts such as:

Nokia RSL
Aviat RSL
Ceragon RSL

when the underlying technical concept is the same.

Manufacturer-specific behavior shall be represented as contextual relationships to the shared concept.

---

## 14. Product Growth

Adding a new manufacturer, product family, product, frequency band, or product revision shall primarily require adding:

- entities;
- relationships;
- contextual applicability;
- authoritative sources; and
- relevant experience.

It should not require restructuring the existing graph.

For example, adding a future product:

PRODUCT:
Nokia XYZ-9000

should involve connecting the new entity to existing concepts wherever applicable.

The architecture shall be designed for indefinite technical expansion.

---

## 15. Vertical and Horizontal Relationships

A.R.I.A.'s graph shall support both hierarchical and cross-domain relationships.

### Vertical relationships

Example:

Nokia
↓
Wavence
↓
UBT
↓
UBT-T
↓
18 GHz Variant

### Horizontal relationships

Example:

RSL Discrepancy
↔ Alignment
↔ Cross Polarization
↔ Flex Routing
↔ Configuration
↔ Weather
↔ Obstruction
↔ Radio Failure

Both dimensions are necessary.

A.R.I.A.'s reasoning shall be capable of traversing between them.

---

## 16. Multi-Hop Knowledge

A.R.I.A. shall support reasoning across multiple relationships.

Example:

Diversity RSL Low

may connect to:

Diversity RF Chain

which connects to:

Flex Routing

which connects to:

OCM Diversity Port

which connects to:

AIM

which connects to:

UBT-T

which connects to:

Nokia Wavence

This allows A.R.I.A. to reason across technical layers rather than relying exclusively on direct keyword matches.

---

## 17. Knowledge Shall Be Reusable

A canonical concept shall be created once when practical and reused across every applicable context.

Example:

CROSS POLARIZATION

may participate in:

- antenna alignment;
- XPIC;
- RSL;
- interference;
- commissioning;
- troubleshooting;
- Nokia;
- Aviat;
- Ceragon;
- training;
- historical cases; and
- diagnostic routes.

A.R.I.A. shall reference the canonical entity rather than maintain separate disconnected copies of the same technical concept.

---

## 18. Source Provenance

Every material knowledge relationship should preserve its source where practical.

Possible provenance includes:

- manufacturer manual;
- technical bulletin;
- engineering standard;
- Braxon procedure;
- validated field finding;
- approved human contribution;
- structured database;
- imported technical dataset; or
- model-proposed candidate awaiting validation.

A.R.I.A. should be capable of answering:

"Why do you believe this relationship exists?"

---

## 19. Source Authority

Knowledge sources shall not be treated as equally authoritative.

A.R.I.A. shall support authority classifications and precedence rules.

For example, depending upon context:

CURRENT MANUFACTURER DOCUMENTATION

may supersede:

OLDER MANUFACTURER DOCUMENTATION

while:

PRODUCT-SPECIFIC MANUFACTURER REQUIREMENT

may take precedence over:

GENERAL FIELD PRACTICE

A separate Source Authority specification shall define the detailed rules.

---

## 20. Revision Awareness

Technical knowledge may change.

The Knowledge Graph shall support:

- effective dates;
- revision identifiers;
- superseded relationships;
- deprecated information;
- hardware applicability;
- firmware applicability; and
- source version.

Old technical knowledge shall not necessarily be deleted.

It may remain historically valid for older equipment or previous configurations.

---

## 21. Contradictory Knowledge

A.R.I.A. shall permit contradictory claims to exist when the contradiction has not yet been resolved.

Example:

SOURCE A:
Parameter X must equal Y.

SOURCE B:
Parameter X must equal Z.

A.R.I.A. shall not silently select one and erase the other.

The contradiction shall preserve:

- both claims;
- both sources;
- authority;
- revision;
- context;
- effective dates; and
- validation state.

The contradiction itself becomes information requiring resolution.

---

## 22. Knowledge Validation States

Knowledge relationships should support states such as:

PROPOSED

Candidate relationship not yet approved.

SUPPORTED

Evidence exists but authority or validation remains incomplete.

VALIDATED

Relationship accepted as usable canonical knowledge.

DEPRECATED

Previously valid relationship no longer recommended or applicable to current context.

SUPERSEDED

Replaced by newer authoritative knowledge.

REJECTED

Candidate relationship determined to be invalid.

A language model proposing a relationship shall initially create a candidate, not canonical truth.

---

## 23. Human-Governed Ingestion

During A.R.I.A.'s early development, extracted technical relationships should preferentially enter a review process.

Conceptually:

SOURCE DOCUMENT
↓
EXTRACTION
↓
ENTITY CANDIDATES
↓
RELATIONSHIP CANDIDATES
↓
SOURCE LINKAGE
↓
HUMAN REVIEW
↓
CANONICAL KNOWLEDGE

A.R.I.A. may eventually earn greater autonomous ingestion authority for sufficiently reliable extraction classes.

The architecture shall not require immediate autonomous trust.

---

## 24. Knowledge Graph and Documents

Original source documents shall remain preserved.

The Knowledge Graph does not replace the source vault.

Instead:

DOCUMENT
provides
CLAIMS

CLAIMS
support
RELATIONSHIPS

RELATIONSHIPS
connect
ENTITIES

A.R.I.A. may retrieve the original source when greater detail, verification, quotation, table interpretation, or revision comparison is required.

---

## 25. Knowledge Graph and Language Model

The language model may assist with:

- entity recognition;
- alias recognition;
- relationship extraction;
- candidate hypothesis generation;
- natural-language querying;
- semantic interpretation; and
- explanation.

The language model shall not become the authoritative storage location for the Knowledge Graph.

The graph shall exist independently of model memory or model weights.

Changing the language model shall not erase A.R.I.A.'s technical knowledge.

---

## 26. Graph Traversal

A.R.I.A. shall be capable of traversing the graph according to relationship type and context.

A query such as:

"What can cause a Diversity-only RSL discrepancy on a Nokia UBT-T?"

should not merely search documents for matching words.

A.R.I.A. should be capable of traversing relationships among:

CURRENT SYMPTOM
→ RSL
→ Diversity
→ RF Chain
→ UBT-T
→ applicable components
→ applicable configurations
→ known failure modes
→ available tests
→ historical experience

The resulting candidate topology may then be evaluated by the Evidence, Probability, and Diagnostic Routing systems.

---

## 27. Avoid Graph Explosion

Not every sentence, word, document paragraph, or incidental relationship should become a permanent graph entity.

A.R.I.A. shall prioritize technically meaningful concepts and relationships.

Graph construction shall balance:

- reasoning usefulness;
- retrieval usefulness;
- precision;
- maintainability;
- provenance;
- computational cost; and
- future extensibility.

The objective is not to create the largest graph.

The objective is to create the most useful technical representation.

---

## 28. Unknown Knowledge

A.R.I.A. shall explicitly support unknown relationships and missing knowledge.

Failure to find a relationship in the graph does not prove the relationship is impossible.

A.R.I.A. may identify:

KNOWLEDGE GAP

when available evidence suggests the current graph is incomplete.

Knowledge gaps may trigger:

- broader source retrieval;
- document review;
- expert input;
- model-assisted candidate generation; or
- future research.

Unknown shall remain a valid state.

---

## 29. Knowledge Expansion

New validated information should connect into the existing graph wherever possible.

Example:

A new Nokia radio is introduced.

A.R.I.A. should not require a completely separate troubleshooting universe.

The new radio may connect to existing concepts such as:

- RSL;
- MSE;
- ACM;
- XPIC;
- antenna alignment;
- Ethernet;
- frequency;
- polarization;
- power;
- commissioning; and
- troubleshooting.

Only genuinely new technical concepts require new canonical entities.

This is how A.R.I.A.'s knowledge shall grow without unnecessary duplication.

---

## 30. Design Objective

A.R.I.A.'s technical knowledge shall resemble a connected cognitive network rather than a filing cabinet.

A.R.I.A. should eventually be capable of moving from:

SYMPTOM

to:

TECHNICAL CONCEPT

to:

PRODUCT

to:

COMPONENT

to:

CONFIGURATION

to:

POSSIBLE CAUSE

to:

TEST

to:

EVIDENCE

to:

HISTORICAL EXPERIENCE

to:

NEXT DIAGNOSTIC ACTION

without requiring those pieces of information to reside in the same file, folder, document, or manufacturer directory.

The Canonical Knowledge Graph provides the shared technical topology upon which A.R.I.A.'s reasoning operates.
