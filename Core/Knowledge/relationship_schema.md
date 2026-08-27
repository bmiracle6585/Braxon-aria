# A.R.I.A. Relationship Architecture

**Document Type:** Canonical Knowledge and Reasoning Specification  
**Authority:** Subordinate to `Core/Schemas/entity_contracts.json`, `Core/Registries/relationship_types.json`, `Core/Schemas/relationships.schema.json`, applicable canonical schemas and registries, and `Core/Persona/ARIA_CONSTITUTION.md`  
**Version:** 2.0.0

---

## 1. Purpose

This document defines the architectural principles governing how A.R.I.A. represents, identifies, interprets, traverses, preserves, and evolves Relationships between canonical semantic objects.

Entities establish:

> **What concepts exist?**

Relationships establish:

> **How do those concepts relate?**

Relationships allow A.R.I.A. to move beyond isolated facts and understand technical structure such as:

- causality;
- dependency;
- hierarchy;
- compatibility;
- incompatibility;
- requirements;
- applicability;
- procedural relationships;
- support;
- contradiction;
- measurement relationships;
- configuration relationships;
- and other canonical semantics defined by the authoritative Relationship registry.

Relationships are first-class semantic objects.

They shall remain distinct from:

- Entities;
- Evidence;
- hypotheses;
- Probability;
- Uncertainty;
- Validation;
- Decisions;
- Actions;
- Routing state;
- Learning;
- Memory;
- provenance;
- Source Authority;
- and Context.

---

## 2. Canonical Authority

Relationship architecture is governed by the applicable machine-readable contracts and registries.

Current primary authorities include:

1. `Core/Schemas/entity_contracts.json`
2. `Core/Registries/relationship_types.json`
3. `Core/Schemas/relationships.schema.json`
4. applicable canonical schemas and registries
5. `Core/Knowledge/entity_schema.md`
6. `Core/Knowledge/knowledge_graph.md`
7. this document
8. `Core/Persona/ARIA_CONSTITUTION.md` as constitutional authority

`Core/Registries/relationship_types.json` owns canonical Relationship vocabulary and semantic definitions.

`Core/Schemas/relationships.schema.json` owns machine-readable validation of persisted Relationship records.

`Core/Schemas/entity_contracts.json` owns applicable identity and interoperability contracts.

This document explains architectural principles.

It shall not independently create competing:

- Relationship types;
- Relationship identifiers;
- directionality rules;
- inverse mappings;
- symmetry definitions;
- lifecycle enums;
- Validation states;
- confidence scales;
- probability structures;
- uncertainty structures;
- provenance structures;
- Source Authority classifications;
- Context vocabularies;
- Learning structures;
- Memory structures;
- or persistence contracts.

Where this doctrine conflicts with a more specific authoritative machine-readable contract, the more specific contract governs.

---

## 3. Fundamental Principle

A Relationship is a semantic assertion connecting canonical subjects according to a defined meaning.

Conceptually:

**SOURCE**

→ **RELATIONSHIP**

→ **TARGET**

For example:

**Condition A**

→ **CAN_CAUSE**

→ **Symptom B**

The Relationship's meaning comes from the authoritative Relationship registry.

The Relationship does not become more or less semantically causal merely because the current Case makes Condition A likely or unlikely.

Canonical semantic meaning and current reasoning state shall remain separate.

---

## 4. Semantic Relationships and Knowledge Graph Edges

A.R.I.A.'s architecture may distinguish between:

1. **Semantic Relationship records**
2. **Persisted Knowledge Graph edge records**

Where the authoritative machine-readable contracts establish distinct identity classes such as:

- `rel_<UUID>`
- `ke_<UUID>`

those distinctions shall remain authoritative.

This doctrine does not independently redefine their exact machine structure.

Conceptually:

A **Semantic Relationship** represents a semantic assertion.

A **Knowledge Graph Edge** represents persisted reusable graph structure.

These concepts may correspond.

They are not automatically interchangeable.

---

## 5. Why the Distinction Matters

Not every meaningful semantic Relationship belongs permanently in reusable canonical technical Knowledge.

For example, a current Case may contain a Relationship conceptually equivalent to:

**Current Evidence**

→ **SUPPORTS**

→ **Current Hypothesis**

That Relationship may be meaningful within current reasoning without becoming permanent universal technical Knowledge.

By contrast:

**Incorrect Configuration**

→ **CAN_CAUSE**

→ **Observed Technical Condition**

may represent reusable technical Knowledge suitable for the Canonical Knowledge Graph.

This separation helps prevent transient Case reasoning from contaminating durable canonical Knowledge.

---

## 6. Machine Contracts Own Relationship Identity

Where authoritative contracts define Relationship identifiers, prefixes, UUID requirements, or graph-edge identifiers, those contracts govern.

This doctrine shall not maintain a duplicate manual identity registry.

Relationship identity should remain stable despite changes to:

- display wording;
- source wording;
- explanatory text;
- repository location;
- model terminology;
- or ordinary metadata.

Identifiers shall not encode mutable technical meaning unless explicitly required by an authoritative contract.

---

## 7. Relationship Identity Is Not Relationship Type

A Relationship record's identity and its semantic Relationship type are different concepts.

The identity distinguishes one persisted Relationship assertion from another.

The Relationship type defines what the connection means.

For example, multiple distinct assertions may all use the same canonical type:

**CAN_CAUSE**

while connecting different Entities or applying under different Context.

A.R.I.A. shall not confuse type identity with assertion identity.

---

## 8. Relationship Types Come From the Registry

All canonical Relationship types shall come from:

`Core/Registries/relationship_types.json`

The registry owns, where defined:

- canonical names;
- semantic definitions;
- categories;
- directionality;
- symmetry;
- inverse semantics;
- and related metadata.

No documentation, model response, ingestion process, or application component shall silently create a competing Relationship vocabulary.

If a genuinely necessary semantic is missing, the canonical registry should be deliberately extended.

---

## 9. Examples Are Not Registry Values

Relationship names appearing in:

- documentation;
- Cases;
- prompts;
- model outputs;
- source material;
- historical files;
- or examples

shall not automatically become canonical Relationship types.

Only the authoritative registry establishes canonical vocabulary.

This prevents prose from becoming a shadow Relationship schema.

---

## 10. Semantic Precision

A.R.I.A. should use the most precise valid canonical Relationship supported by the underlying Knowledge.

A vague association shall not be represented as causality merely because causality would make reasoning easier.

Likewise, A.R.I.A. shall not represent:

- possibility as requirement;
- correlation as causation;
- sequence as dependency;
- compatibility as equivalence;
- support as proof;
- contradiction as negation;
- or historical frequency as deterministic technical truth.

Semantic precision is fundamental.

---

## 11. Stronger Semantics Require Stronger Support

A.R.I.A. shall not choose a stronger Relationship merely because it produces a stronger conclusion.

If the available information supports only:

> **is associated with**

she shall not silently upgrade it to:

> **causes**

unless the authoritative Knowledge supports causality.

Relationship semantics must describe the Knowledge.

They shall not be selected to manufacture certainty.

---

## 12. Directionality

Relationship directionality is governed by the authoritative Relationship registry.

For a directional Relationship:

**A → R → B**

does not automatically establish:

**B → R → A**

For example:

**A CAN_CAUSE B**

does not establish:

**B CAN_CAUSE A**

A.R.I.A. shall respect canonical directionality during:

- graph traversal;
- reasoning;
- retrieval;
- explanation;
- and Learning.

---

## 13. Inverse Semantics

A Relationship type may have a canonical inverse defined by the registry.

Where an inverse is defined, A.R.I.A. may reason or traverse using that inverse according to the authoritative semantics.

Inverse traversal does not necessarily require storing a duplicate authoritative Relationship assertion.

The machine-readable contracts determine persistence behavior.

A.R.I.A. shall not invent inverse semantics that the registry does not establish.

---

## 14. Symmetry

Some canonical Relationships may be symmetric.

Symmetry exists only when established by the authoritative Relationship registry.

A.R.I.A. shall not infer symmetry from:

- natural-language wording;
- graph shape;
- co-occurrence;
- model intuition;
- historical frequency;
- or convenience.

A directional Relationship remains directional unless canonical authority states otherwise.

---

## 15. Relationship and Entity Are Distinct

Entities represent canonical concepts or subjects.

Relationships represent semantic connections between them.

A.R.I.A. should not replace a Relationship with an artificial compound Entity merely to avoid structured semantics.

Conceptually:

**Condition A CAN_CAUSE Symptom B**

should normally remain:

- Entity A;
- canonical Relationship;
- Entity B

rather than creating an Entity named:

> "Condition-A-causes-Symptom-B"

unless that compound concept independently deserves canonical Entity identity.

---

## 16. Relationship and Property Are Distinct

Not every Entity property should become a Relationship.

Not every Relationship should be hidden inside an Entity property.

Where information describes a meaningful connection between independently identifiable concepts, a canonical Relationship may be appropriate.

Where information merely describes one Entity and does not benefit from independent semantic connection, a property may be appropriate.

Applicable schemas govern exact implementation.

---

## 17. Relationship and Free Text Are Distinct

Free text may explain a Relationship.

Free text shall not substitute for canonical Relationship semantics when machine-interpretable structure is required.

For example, a note saying:

> "This sometimes causes that."

should not become the only persisted representation when the canonical registry provides an appropriate causal Relationship.

Structured semantics and explanatory text may coexist.

---

## 18. Relationship Context

A Relationship may apply only under particular Context.

Applicability may depend upon dimensions such as:

- manufacturer;
- product;
- product family;
- product variant;
- hardware;
- firmware;
- software;
- configuration;
- topology;
- environment;
- jurisdiction;
- customer implementation;
- operating mode;
- date;
- or another canonical Context dimension.

Context Engine owns canonical Context semantics.

Relationship Architecture may reference applicable Context.

---

## 19. Context Does Not Automatically Create New Relationship Types

A Relationship does not become a new semantic type merely because it applies:

- to another manufacturer;
- under another configuration;
- on another revision;
- for another customer;
- or during another time period.

The same canonical semantic may exist under different Context.

A.R.I.A. shall use Context and appropriately distinct Relationship assertions where necessary rather than multiplying Relationship-type vocabulary.

---

## 20. Separate Assertions May Still Be Appropriate

Two Relationship assertions using the same canonical type may legitimately remain distinct when their:

- source and target differ;
- Context differs materially;
- provenance differs materially;
- effective period differs;
- conditions differ;
- technical meaning differs;
- revision applicability differs;
- or governance history differs.

Canonical reuse does not require collapsing semantically distinct assertions.

---

## 21. Relationship Conditions

Some Relationships apply only when defined conditions exist.

Conceptually:

**Condition X**

must be present before:

**Entity A CAN_CAUSE Entity B**

is technically applicable.

Conditions should reference canonical structure where authoritative schemas support doing so.

A.R.I.A. shall not use a conditional Relationship as universally applicable.

---

## 22. Conditional Possibility Is Not Current Probability

A canonical Relationship may establish:

> Under Context X, A can cause B.

This does not establish:

> A is probably causing B in this Case.

The first is canonical technical possibility.

The second is current reasoning.

Probability Engine owns current belief.

Relationship Architecture shall not collapse the two.

---

## 23. Deterministic Technical Relationships

Some canonical Relationships may represent deterministic or rule-like technical Knowledge where supported by authoritative sources.

Such Knowledge may still be limited by:

- Context;
- revision;
- configuration;
- time;
- implementation;
- or source scope.

Deterministic does not mean universal.

Deterministic does not mean eternally valid.

And deterministic does not mean current Case conditions have established that the Relationship is presently operative.

---

## 24. Deterministic Knowledge Does Not Need Diagnostic Probability

If canonical technical Knowledge establishes a deterministic Relationship under defined Context, A.R.I.A. shall not invent diagnostic Probability merely to express the Relationship itself.

Probability may still apply to whether:

- the relevant Context is present;
- the source condition exists;
- the current observation is accurate;
- or the Relationship explains the current Case.

Canonical technical semantics and current belief remain separate.

---

## 25. Statistical Association Must Remain Distinguishable

Some Relationships may represent statistical or empirical association rather than deterministic technical behavior.

Where the canonical registry and applicable schemas support such semantics, the Relationship should preserve that distinction.

A.R.I.A. shall not treat empirical frequency as though it were deterministic causality.

Learning Engine owns qualification of historical patterns.

---

## 26. Relationship Strength Is Not Universal

A numerical Relationship-strength field shall not be assumed to have universal meaning merely because a schema permits a number.

Any such value must have an explicit methodology and semantic definition.

A numerical association value shall not silently become:

- diagnostic Probability;
- Evidence confidence;
- Source Authority;
- Validation status;
- uncertainty;
- route priority;
- or certainty.

If no authoritative methodology defines a strength value, A.R.I.A. shall not invent one.

---

## 27. Relationship Confidence Is Not an Independent Cognitive Authority

Earlier architecture allowed Relationship records to accumulate independent confidence values.

That concept shall not become a competing universal confidence system.

Trust in a Relationship may depend upon:

- provenance;
- Source Authority;
- corroboration;
- Context;
- Validation;
- contradiction;
- Learning;
- revision applicability;
- and other authoritative reasoning structures.

If machine-readable contracts retain a relationship-level confidence field for interoperability or legacy purposes, its interpretation must defer to the canonical confidence architecture and shall not independently govern reasoning.

Relationship Architecture does not own a separate confidence scale.

---

## 28. Relationship and Evidence Are Distinct

A canonical Relationship may describe reusable Knowledge.

Evidence describes information relevant to the current Case.

For example:

Canonical Knowledge:

**Damaged Cable CAN_CAUSE Link Degradation**

Current Evidence:

> The cable currently shows physical damage.

The Relationship establishes technical possibility.

The Evidence establishes current observation.

Evidence Engine owns current Evidence.

---

## 29. Evidence Relationships May Be Case-Specific

A current Case may contain semantic Relationships involving Evidence, hypotheses, Actions, Observations, or other reasoning objects where authoritative contracts permit them.

Those Relationships do not automatically become reusable canonical technical Knowledge.

Case-specific semantic structure and canonical Knowledge Graph structure must remain distinguishable.

---

## 30. Relationship and Hypothesis Are Distinct

A canonical Relationship may make a hypothesis technically plausible.

It does not automatically create the hypothesis.

Hypothesis Engine owns:

- hypothesis creation;
- hypothesis state;
- hypothesis competition;
- and hypothesis retirement

according to its authoritative contract.

Relationship Architecture provides semantic Knowledge that Hypothesis Engine may use.

---

## 31. Relationship and Probability Are Distinct

A canonical Relationship does not own current diagnostic Probability.

For example:

**Condition A CAN_CAUSE Symptom B**

does not establish:

**P(Condition A | current Case) = any fixed value**

Probability Engine determines current belief using current reasoning state.

The canonical Relationship may inform Probability without becoming Probability.

---

## 32. Relationship and Uncertainty Are Distinct

A Relationship may be:

- incompletely sourced;
- context-limited;
- contradicted;
- historical;
- or unresolved.

Formal current uncertainty remains owned by Uncertainty Engine.

Relationship Architecture shall not create a competing uncertainty scale.

The Relationship should preserve the information needed for Uncertainty to reason correctly.

---

## 33. Relationship and Validation Are Distinct

Validation Engine determines what current results demonstrate.

Relationship Architecture determines canonical semantic connections.

A current Validation result may:

- support;
- challenge;
- fail to establish;
- or reveal a problem with

a Relationship or its applicability.

Validation shall not be redefined as a fixed Relationship lifecycle state inside this doctrine.

---

## 34. Relationship and Decision Are Distinct

Canonical Relationships may establish information relevant to selecting an Action.

For example:

- a Tool tests a Measurement;
- a Procedure requires a prerequisite;
- an Action affects a component;
- a configuration is incompatible with another configuration.

Decision Engine owns current Action selection.

Relationship Architecture does not independently decide what should happen next.

---

## 35. Relationship and Routing Are Distinct

Routing Engine may traverse canonical Relationships to identify:

- plausible causes;
- tests;
- dependencies;
- prerequisites;
- exclusions;
- or next diagnostic branches.

Relationship Architecture supplies semantic connectivity.

Routing Engine owns current route progression.

The graph shall not become a competing Routing state machine.

---

## 36. Relationship and Learning Are Distinct

Learning Engine may discover recurring patterns involving canonical Entities and Relationships.

Learning may propose:

- new candidate Relationships;
- revised applicability;
- empirical associations;
- Context restrictions;
- or Knowledge gaps.

Those proposals do not automatically become canonical technical Relationships.

Learning owns qualification.

Knowledge governance owns canonical promotion.

---

## 37. There Is No Independent Experience Ledger Authority

Earlier architecture referenced a separate **Experience Ledger** and Experience overlays as though they were independent sources of Relationship authority.

That model is obsolete.

Historical experience now emerges through the coordinated canonical architecture involving, as applicable:

- Case State;
- Context;
- Evidence;
- Actions;
- Observations;
- Validation;
- Learning;
- Memory;
- and persistent historical records.

Relationship Architecture may consume qualified learned Knowledge.

It shall not depend upon a competing Experience Ledger authority.

---

## 38. Historical Frequency Does Not Rewrite Relationship Semantics

Suppose repeated historical Cases show that Condition A frequently accompanies Symptom B.

That pattern may be useful Learning.

It does not automatically establish:

**Condition A CAUSES Symptom B**

A.R.I.A. must preserve the distinction between:

- co-occurrence;
- statistical association;
- technical possibility;
- causality;
- requirement;
- and deterministic behavior.

Learning shall not silently strengthen Relationship semantics.

---

## 39. Relationship and Memory Are Distinct

Memory may retrieve relevant Relationships from:

- canonical Knowledge;
- prior Cases;
- historical sources;
- learned patterns;
- or other authorized persistent structures.

Retrieval does not alter the Relationship's canonical meaning.

Frequently remembered Relationships do not become more authoritative merely because they are frequently retrieved.

Memory Engine owns retrieval.

---

## 40. Provenance

Material Relationships should preserve or reference sufficient provenance to establish their lineage.

`Core/Knowledge/provenance_schema.md` owns provenance semantics.

Relationship Architecture shall not create a competing provenance structure.

Provenance may establish:

- where the assertion originated;
- whether it was directly stated or derived;
- what transformation occurred;
- what source supported it;
- when it was acquired;
- and what lineage connects it to upstream information.

---

## 41. Source Authority

Source Authority remains distinct from Relationship persistence.

`Core/Knowledge/source_authority.md` governs authority principles.

A Relationship existing in the Knowledge Graph does not automatically mean every supporting source is equally authoritative.

Authority may vary by:

- source;
- claim;
- Context;
- revision;
- subject matter;
- and other applicable factors.

The Relationship preserves connectivity.

Source Authority evaluates legitimate support.

---

## 42. Multiple Supporting Sources

A technically identical Relationship should not automatically be duplicated merely because several sources support it.

Where the semantic assertion, Context, effective period, and technical meaning are the same, provenance may preserve multiple supporting sources.

However, separate assertions may remain appropriate where meaningful differences exist.

The goal is neither forced duplication nor forced collapse.

The goal is accurate semantic representation.

---

## 43. Independent Corroboration

Multiple sources do not automatically equal multiple independent confirmations.

Several downstream documents may originate from the same upstream source.

A.R.I.A. should preserve common lineage where known.

Source count alone shall not determine:

- truth;
- authority;
- confidence;
- Probability;
- or Validation.

Provenance and Source Authority provide the appropriate structure.

---

## 44. Contradictory Relationships

A.R.I.A. shall permit contradictory Relationship assertions to coexist when the contradiction has not been legitimately resolved.

For example, two sources may assert incompatible requirements concerning the same product.

The system shall preserve enough information to investigate whether the difference arises from:

- revision;
- configuration;
- product variant;
- jurisdiction;
- effective date;
- source scope;
- implementation;
- source error;
- or genuine unresolved disagreement.

Contradiction is meaningful state.

---

## 45. Contradiction Does Not Automatically Mean One Relationship Is False

Apparently contradictory Relationships may both be valid under different Context.

A.R.I.A. should investigate Context before collapsing the conflict into a simple true/false decision.

This is especially important for:

- revision-specific Knowledge;
- manufacturer-specific behavior;
- customer-specific implementation;
- regulatory differences;
- and historical Knowledge.

---

## 46. Unresolved Contradiction Must Remain Visible

When contradiction cannot yet be resolved, A.R.I.A. shall preserve it.

She shall not:

- silently delete one assertion;
- invent consensus;
- average incompatible semantics;
- or choose whichever assertion supports the preferred diagnosis.

Current reasoning may proceed with explicit uncertainty where permitted.

---

## 47. Negative Knowledge

A.R.I.A. may represent explicit negative technical Knowledge when the canonical Relationship registry supports the required semantic.

Absence of a positive Relationship does not establish its negation.

Likewise:

> no known Relationship

does not mean:

> impossible Relationship.

Negative Knowledge must be explicitly supported.

---

## 48. Absence Is Not Negation

If the Knowledge Graph does not contain:

**A → R → B**

A.R.I.A. shall not automatically conclude:

**A NOT-R B**

unless authoritative Knowledge explicitly establishes that negative semantic.

The graph may simply be incomplete.

Knowledge gaps must remain possible.

---

## 49. Temporal Applicability

Relationships may change over time.

The authoritative schemas may represent temporal applicability through structures such as:

- effective dates;
- valid-from;
- valid-to;
- revision Context;
- supersession;
- or other canonical mechanisms.

This doctrine shall not duplicate the exact fields.

A.R.I.A. shall distinguish current applicability from historical validity.

---

## 50. Historical Relationships May Remain Valid Historically

A Relationship may no longer govern current systems while remaining correct for an earlier:

- firmware;
- product;
- revision;
- configuration;
- standard;
- or time period.

Historical reasoning should use Knowledge applicable to the historical Context.

Superseded does not automatically mean historically false.

---

## 51. Relationship Lifecycle Must Be Canonically Defined

Earlier versions of this doctrine established lifecycle enums such as:

- `PROPOSED`;
- `ACTIVE`;
- `DEPRECATED`;
- `SUPERSEDED`;
- `REJECTED`.

This doctrine no longer establishes those values as universal architecture.

If Relationship lifecycle states are required, they shall be defined by an explicit authoritative machine-readable schema or registry.

Descriptive lifecycle terminology may be used without becoming an implicit enum.

---

## 52. Validation State Must Be Canonically Defined

Earlier versions of this doctrine separately established Validation states such as:

- `UNREVIEWED`;
- `REVIEWED`;
- `VALIDATED`;
- `DISPUTED`;
- `REJECTED`.

Those values shall not be treated as canonical merely because they appeared in prose.

Validation Engine and applicable machine-readable schemas own Validation semantics.

Relationship Architecture shall not create a competing Validation state machine.

---

## 53. Candidate Relationships

A Relationship may be proposed through:

- document extraction;
- language-model inference;
- human contribution;
- structured import;
- qualified Learning;
- source comparison;
- pattern detection;
- or another authorized process.

Candidate status does not automatically establish canonical Knowledge.

Candidate Relationships must remain distinguishable from governed canonical Relationships.

---

## 54. Model-Proposed Relationships Are Not Automatically Canonical

A language model may infer:

> A appears related to B.

That inference may be useful.

It is not automatically canonical technical Knowledge.

The model shall not manufacture:

- provenance;
- Source Authority;
- Validation;
- deterministic semantics;
- causality;
- or canonical status

merely because the generated Relationship sounds plausible.

---

## 55. Candidate Causality Requires Special Care

Causal Relationships have strong reasoning consequences.

A.R.I.A. shall not promote repeated co-occurrence into causality without legitimate technical support.

For example:

> A often appeared when B occurred

does not alone establish:

> A causes B.

The architecture must preserve the difference.

---

## 56. Canonical Promotion Must Be Governed

Promotion of candidate Relationships into canonical Knowledge shall follow the applicable Knowledge governance architecture.

This doctrine does not define a competing promotion workflow.

Orchestration may coordinate:

- extraction;
- review;
- source comparison;
- provenance capture;
- Entity resolution;
- Context resolution;
- Validation;
- dependency analysis;
- and persistence

according to authoritative contracts.

---

## 57. Relationship Correction

A canonical Relationship may later require correction because:

- its semantic type was wrong;
- its source Entity was wrong;
- its target Entity was wrong;
- its Context was incomplete;
- its provenance was incorrect;
- its applicability changed;
- its source was corrected;
- or new Knowledge revealed a modeling error.

Correction should preserve sufficient history and lineage.

---

## 58. Relationship Correction May Require Reprocessing

Material Relationship changes may affect:

- Knowledge Graph traversal;
- hypotheses;
- Routing Knowledge;
- learned patterns;
- historical interpretations;
- source mappings;
- application behavior;
- and derived Knowledge.

The architecture should support dependency review and reprocessing where necessary.

Orchestration owns coordinated execution.

---

## 59. Relationship Supersession

A Relationship may be superseded without being erased.

Supersession may be appropriate where newer Knowledge replaces an earlier assertion for current applicability.

Historical lineage should remain available when useful.

Exact supersession structure belongs to authoritative schemas.

---

## 60. Relationship Deletion Should Be Exceptional

Relationships with historical dependencies should not ordinarily disappear merely because they are no longer current.

Historical preservation may be necessary for:

- legacy systems;
- old Cases;
- previous decisions;
- historical configurations;
- prior procedures;
- or auditability.

Where removal is required, applicable governance should preserve appropriate lineage.

---

## 61. Relationship Merge

Two Relationship assertions may be candidates for merge when they represent the same:

- source;
- semantic;
- target;
- Context;
- effective applicability;
- and technical meaning.

Merge should preserve:

- provenance;
- source lineage;
- historical references;
- and downstream dependencies.

A.R.I.A. shall not merge merely because Relationship text looks similar.

---

## 62. Relationship Split

A previously unified Relationship may need to be split when new Knowledge reveals materially different:

- Context;
- revision applicability;
- technical behavior;
- provenance;
- conditions;
- or semantics.

Relationship architecture must support correction rather than freezing early modeling assumptions.

---

## 63. Multi-Hop Traversal

A.R.I.A. should support multi-hop traversal through canonical Relationships.

Conceptually:

**Symptom**

→ **CAN_BE_CAUSED_BY**

→ **Condition**

→ **INVOLVES**

→ **Component**

→ **TESTED_BY**

→ **Procedure**

The actual Relationship types must come from the canonical registry.

Multi-hop traversal allows structured reasoning beyond keyword retrieval.

---

## 64. Multi-Hop Traversal Is Not Proof

A path through the graph establishes connectivity according to canonical semantics.

It does not automatically establish that the entire path explains the current Case.

Current reasoning must still consider:

- Evidence;
- Context;
- Probability;
- Uncertainty;
- Validation;
- contradictions;
- and other applicable state.

A technically possible path may still be irrelevant now.

---

## 65. Traversal Must Preserve Semantics

A.R.I.A. shall not treat every Relationship as an interchangeable graph edge.

Traversal must preserve distinctions between semantics such as:

- causality;
- hierarchy;
- requirement;
- compatibility;
- support;
- contradiction;
- procedure;
- configuration;
- and other registered meanings.

Graph reachability alone is not semantic reasoning.

---

## 66. Traversal Must Preserve Directionality

A.R.I.A. shall respect canonical directionality during traversal.

She shall not reverse a directional Relationship unless:

- an authoritative inverse exists;
- or another canonical semantic explicitly supports the reverse traversal.

Convenient traversal shall not rewrite technical meaning.

---

## 67. Traversal Must Preserve Context

A Relationship applicable to one:

- product;
- revision;
- firmware;
- configuration;
- topology;
- jurisdiction;
- or environment

shall not automatically participate in reasoning for another.

Context should constrain graph traversal where materially relevant.

---

## 68. Traversal Must Preserve Temporal Applicability

Current reasoning should not silently traverse superseded historical Relationships as though they were current.

Historical Cases may intentionally require historical Relationships.

Temporal Context determines applicability.

---

## 69. Traversal Must Preserve Negative Semantics

Where canonical negative Relationships exist, A.R.I.A. shall preserve their actual meaning.

She shall not treat:

> incompatible with

as equivalent to:

> unrelated to.

Nor shall she treat:

> does not require

as equivalent to:

> prohibits.

Semantic precision remains necessary even for negative Knowledge.

---

## 70. Cycles Are Not Automatically Errors

A graph may contain legitimate cycles.

For example, hierarchical or dependency structures may produce traversable loops depending upon canonical semantics and inverse representation.

A.R.I.A. shall not assume every cycle indicates corrupt Knowledge.

Traversal systems should prevent uncontrolled recursion while preserving valid graph structure.

---

## 71. Relationship Architecture Must Avoid Graph Noise

As Knowledge grows, indiscriminate Relationship creation can reduce reasoning quality.

A.R.I.A. should avoid creating permanent Relationships for every:

- word co-occurrence;
- conversational association;
- incidental sequence;
- weak model inference;
- temporary observation;
- or one-time correlation.

Relationships should provide durable semantic value.

---

## 72. Avoid Overly Generic Relationships

A graph dominated by generic Relationships such as:

> RELATED_TO

may become connected but cognitively weak.

Where authoritative Knowledge supports a more precise canonical semantic, A.R.I.A. should use it.

Generic association remains appropriate only when the underlying Knowledge does not justify greater specificity.

---

## 73. Avoid Unsupported Precision

The opposite error is equally dangerous.

A.R.I.A. shall not choose:

- causal;
- deterministic;
- required;
- incompatible;
- resolves;
- or similarly strong semantics

when the source only establishes a weaker association.

The graph should be as precise as the Knowledge supports—not more.

---

## 74. Relationship Granularity Must Serve Reasoning

Relationship assertions should be neither unnecessarily fragmented nor overly broad.

Granularity should support:

- technical reasoning;
- Context;
- provenance;
- revision awareness;
- Learning;
- retrieval;
- auditability;
- and explanation.

The goal is useful semantic structure.

Not maximum edge count.

---

## 75. Domain Expansion Should Reuse Relationship Semantics

New technical domains should reuse existing canonical Relationship types where those semantics genuinely apply.

A new domain does not automatically require an entirely new Relationship vocabulary.

For example, concepts such as:

- dependency;
- hierarchy;
- requirement;
- causality;
- compatibility;
- support;
- contradiction

may apply across many domains.

The registry should expand only when genuinely new semantics are necessary.

---

## 76. New Relationship Types Must Be Deliberate

Before adding a new canonical Relationship type, governance should determine whether:

- an existing semantic already fits;
- the proposed distinction materially improves reasoning;
- the distinction is stable;
- directionality is understood;
- inverse semantics are understood;
- symmetry is understood;
- and the type has broad enough utility to justify canonical vocabulary.

Registry growth should be deliberate.

---

## 77. Product-Specific Semantics Do Not Automatically Require Universal Relationship Types

A product may use proprietary terminology describing a relationship between its components.

That does not automatically require adding the vendor's wording as a universal Relationship type.

A.R.I.A. should determine whether the concept maps to:

- an existing canonical semantic;
- product-specific Knowledge;
- an alias;
- or a genuinely new universal Relationship semantic.

---

## 78. Relationship Architecture Must Remain Domain-Independent

The universal Relationship architecture shall not hardcode itself around:

- microwave backhaul;
- RF;
- Ethernet;
- telecommunications;
- one manufacturer;
- one product;
- one customer;
- one organization;
- or one participant.

Those domains populate the graph.

They do not define the limits of Relationship Architecture.

---

## 79. Telecommunications Is Graph Content, Not Universal Relationship Doctrine

Telecommunications-specific causal and structural Knowledge belongs in canonical Knowledge.

The universal Relationship doctrine defines how such connections behave.

This distinction allows A.R.I.A. to expand into additional technical and operational domains without rebuilding her Relationship architecture.

---

## 80. Relationship Architecture Must Support Explanation

Where useful, A.R.I.A. should be capable of explaining:

- what concepts are connected;
- what the Relationship means;
- what Context applies;
- what source supports it;
- whether contradictory Relationships exist;
- whether the Relationship is historical;
- and how it influenced current reasoning.

Explanation should reflect actual canonical state.

---

## 81. Explanation Must Not Overstate Semantics

A.R.I.A.'s user-facing language should preserve the strength of the underlying Relationship.

If the graph establishes:

> can cause

she should not explain:

> definitely causes.

If the graph establishes:

> is associated with

she should not explain:

> causes.

Natural language may be simplified.

Semantic strength shall not be inflated.

---

## 82. Internal IDs Need Not Be Exposed

Stable internal Relationship identifiers are important for architecture.

Users ordinarily do not need to see:

- `rel_<UUID>`;
- `ke_<UUID>`;
- internal registry keys;
- or graph implementation details.

A.R.I.A. may explain the technical Relationship naturally while preserving canonical identity internally.

---

## 83. Relationship Architecture Must Support Auditability

Authorized review should be capable of determining, where applicable:

- what Relationship existed;
- what canonical semantic it used;
- what Entities it connected;
- what Context applied;
- what provenance supported it;
- when it applied;
- whether it changed;
- whether it was superseded;
- and what downstream Knowledge depended upon it.

Auditability supports trustworthy evolution.

---

## 84. Relationship Architecture Must Support Reproducibility

Where practical, A.R.I.A. should preserve enough information to reproduce why a material Relationship exists.

This may require:

- source lineage;
- Entity resolution;
- Relationship-type selection;
- Context;
- transformation history;
- governance history;
- and supporting Knowledge.

The exact persistence structure belongs to authoritative schemas.

---

## 85. Relationship Architecture Must Survive Conversation Length

Canonical Relationships shall not depend upon remaining in temporary model context.

A.R.I.A. shall not forget technical Relationships merely because:

- a conversation becomes long;
- a session ends;
- context is summarized;
- or another model handles the next interaction.

Persistent Knowledge architecture owns canonical Relationships.

---

## 86. Relationship Architecture Must Survive Model Replacement

Canonical Relationships shall not belong to one language model.

Changing:

- model provider;
- model version;
- inference implementation;
- prompt architecture;
- or reasoning model

shall not destroy canonical Relationship identity or semantics.

The model may help interpret Relationships.

It does not own them.

---

## 87. Relationship Architecture Must Survive Repository Reorganization

Moving files or documents shall not inherently change canonical Relationship identity.

Repository location is storage organization.

It is not Relationship semantics.

Source provenance may reference storage locations without allowing those locations to define canonical meaning.

---

## 88. Relationship Architecture Must Support Schema Evolution

Machine-readable schemas and registries may evolve.

The architecture should permit:

- new Relationship types;
- improved validation;
- improved inverse semantics;
- improved Context support;
- improved temporal representation;
- and improved interoperability

without requiring wholesale replacement of canonical Knowledge.

Schema evolution should be deliberate and migration-aware.

---

## 89. Early Relationship Assumptions Must Remain Correctable

Early A.R.I.A. development may contain:

- overly broad semantics;
- duplicate Relationship types;
- incorrect directionality;
- unnecessary lifecycle states;
- weak Context modeling;
- or assumptions tied too closely to the first technical domain.

The architecture shall permit deliberate correction.

Early implementation shall not become permanent doctrine merely because it existed first.

---

## 90. Machine-Readable Contracts Are Authoritative

Where prose and machine-readable contracts differ concerning:

- valid Relationship types;
- identifiers;
- required fields;
- field types;
- directionality;
- symmetry;
- inverse mappings;
- canonical enums;
- or persisted structure,

the applicable authoritative machine-readable contract governs unless constitutional authority requires otherwise.

This doctrine explains architecture.

It does not replace validation contracts.

---

## 91. Prose Shall Not Become a Shadow Schema

This document shall not manually duplicate every:

- Relationship enum;
- field;
- prefix;
- validation rule;
- lifecycle state;
- inverse mapping;
- or schema requirement.

Doing so creates drift.

The prose defines:

- principles;
- boundaries;
- responsibilities;
- invariants;
- and interpretation.

Machine-readable contracts define exact implementation.

---

## 92. Canonical Registries Must Remain Canonical

A.R.I.A. shall not silently introduce new Relationship types through:

- application code;
- language-model output;
- source ingestion;
- documentation;
- Learning;
- or domain-specific modules.

If a new canonical semantic is required, the authoritative registry should be deliberately extended.

---

## 93. Relationship Architecture and Knowledge Graph

Relationship Architecture owns:

> **the semantic connections between canonical subjects.**

Entity Architecture owns:

> **the canonical identity of those subjects.**

Knowledge Graph doctrine owns:

> **the durable connected Knowledge system formed from those structures.**

These responsibilities shall remain distinct.

---

## 94. Relationship Architecture and Current Reasoning

Current reasoning may traverse, rank, select, or ignore canonical Relationships depending upon:

- current Context;
- Evidence;
- hypotheses;
- Probability;
- Uncertainty;
- Routing;
- Decision;
- and Validation.

Current reasoning relevance shall not rewrite permanent Relationship semantics.

A Relationship does not become more causal because it is currently diagnostically useful.

---

## 95. Relationship Architecture and Learning

Stable Relationship semantics allow Learning to compare historical Cases meaningfully.

If the same technical semantic is represented inconsistently across Cases, Learning becomes fragmented.

If weak associations are mislabeled as causality, Learning becomes corrupted.

Relationship quality therefore directly affects Learning quality.

---

## 96. Relationship Architecture and Memory

Memory may use canonical Relationships to retrieve connected Knowledge.

For example, retrieval may begin from a symptom Entity and traverse toward:

- causes;
- components;
- tests;
- procedures;
- or historical Cases.

Memory shall respect canonical semantics and Context.

Retrieval frequency shall not redefine Relationship authority.

---

## 97. Relationship Architecture and Source Evolution

When an upstream source changes, Relationships derived from that source may require review.

The architecture should support tracing:

**SOURCE**

→ **CLAIM**

→ **RELATIONSHIP**

→ **DEPENDENT KNOWLEDGE**

where authoritative schemas support those structures.

Source correction should not leave downstream Knowledge silently stale.

---

## 98. Relationship Architecture and Knowledge Gaps

Failure to find an applicable Relationship is a valid outcome.

A.R.I.A. may determine:

> "I do not currently have canonical Knowledge connecting these concepts."

That is preferable to inventing a Relationship.

Knowledge gaps may later trigger:

- source research;
- human review;
- candidate generation;
- qualified Learning;
- or registry extension.

Unknown is valid.

---

## 99. Relationship Architecture and Human Language

Users may describe Relationships informally.

For example:

> "That cable is killing the link."

A.R.I.A. may interpret the intended technical meaning while preserving canonical semantics internally.

She should not require users to know Relationship registry vocabulary.

Natural language is the interface.

Canonical semantics are the internal structure.

---

## 100. Ambiguous Relationship Language Must Not Be Overinterpreted

Informal language may be ambiguous.

For example:

> "A affects B."

may mean:

- causes;
- changes;
- correlates with;
- interferes with;
- depends upon;
- or merely relates to.

Where the distinction materially affects reasoning and Context does not resolve it, A.R.I.A. shall not silently choose the strongest semantic.

---

## 101. Core Relationship Invariants

The following principles shall remain true throughout A.R.I.A.'s architecture:

1. Relationships are first-class semantic objects.
2. Relationship Architecture is subordinate to authoritative machine-readable contracts and registries.
3. Canonical Relationship types come from the authoritative registry.
4. Prose examples do not create canonical Relationship types.
5. Semantic Relationship identity and Relationship type are distinct.
6. Semantic Relationships and Knowledge Graph edges may remain distinct where authoritative contracts establish that distinction.
7. Stable Relationship identity shall not depend upon mutable wording.
8. Relationship semantics shall be as precise as the underlying Knowledge supports.
9. Stronger semantic meaning requires legitimate support.
10. Directionality shall be respected.
11. Inverse semantics shall be canonical rather than invented.
12. Symmetry shall exist only when canonically defined.
13. Entities and Relationships are distinct.
14. Properties and Relationships are distinct.
15. Free text shall not replace canonical Relationship semantics where structure is required.
16. Relationships may be Context-specific.
17. Context does not automatically create new Relationship types.
18. Separate Relationship assertions may remain appropriate where applicability materially differs.
19. Conditional Relationships shall not be generalized beyond their conditions.
20. Canonical possibility is distinct from current Probability.
21. Deterministic technical Knowledge may remain Context-limited.
22. Deterministic Relationships do not require invented diagnostic Probability.
23. Statistical association shall remain distinguishable from deterministic causality.
24. Numerical Relationship strength shall not have invented universal meaning.
25. Relationship Architecture does not own an independent confidence scale.
26. Relationships are distinct from current Evidence.
27. Case-specific Evidence Relationships do not automatically become canonical Knowledge.
28. Relationships are distinct from hypotheses.
29. Relationships are distinct from Probability.
30. Relationships are distinct from formal Uncertainty.
31. Relationships are distinct from Validation.
32. Relationships inform Decision but do not own Action selection.
33. Relationships inform Routing but do not own route progression.
34. Relationships are distinct from Learning.
35. There is no independent Experience Ledger authority.
36. Historical frequency shall not silently strengthen Relationship semantics.
37. Relationships are distinct from Memory.
38. Material Relationships should preserve provenance.
39. Source Authority remains distinct from Relationship persistence.
40. Multiple supporting sources do not automatically require duplicate Relationships.
41. Source count does not equal independent corroboration.
42. Contradictory Relationships may coexist.
43. Contradiction does not automatically mean one Relationship is false.
44. Unresolved contradiction shall remain visible.
45. Negative Knowledge requires explicit support.
46. Absence of a Relationship is not automatic negation.
47. Relationships may have temporal applicability.
48. Historical Relationships may remain historically valid after supersession.
49. Relationship lifecycle enums require explicit canonical authority.
50. Validation states require explicit canonical authority.
51. Candidate Relationships shall remain distinguishable from canonical Relationships.
52. Model-proposed Relationships are not automatically canonical.
53. Co-occurrence shall not automatically become causality.
54. Canonical promotion must be governed.
55. Relationship correction should preserve lineage.
56. Material Relationship correction may require downstream reprocessing.
57. Superseded Relationships may remain historically important.
58. Deletion of historically referenced Relationships should be exceptional.
59. Relationship merge must preserve semantic equivalence and lineage.
60. Relationship split must remain possible when prior modeling was too broad.
61. Multi-hop traversal is required.
62. Multi-hop traversal does not itself prove a current conclusion.
63. Traversal shall preserve semantic meaning.
64. Traversal shall preserve directionality.
65. Traversal shall preserve Context.
66. Traversal shall preserve temporal applicability.
67. Traversal shall preserve negative semantics.
68. Graph cycles are not automatically errors.
69. Relationship creation shall avoid graph noise.
70. Overly generic semantics should be avoided where precise semantics are supported.
71. Unsupported precision shall also be avoided.
72. Relationship granularity shall serve reasoning.
73. New domains should reuse canonical Relationship semantics where appropriate.
74. New Relationship types shall be added deliberately.
75. Product-specific terminology does not automatically require universal Relationship types.
76. Universal Relationship architecture shall remain domain-independent.
77. Domain-specific Relationships belong in Knowledge rather than universal doctrine.
78. Relationship influence should remain explainable.
79. Explanation shall not inflate semantic strength.
80. Internal Relationship IDs need not be exposed during ordinary interaction.
81. Relationship Architecture should support auditability.
82. Relationship Architecture should support reproducibility.
83. Canonical Relationships shall survive conversation length.
84. Canonical Relationships shall survive model replacement.
85. Canonical Relationships shall survive repository reorganization.
86. Relationship Architecture shall support schema evolution.
87. Early semantic assumptions shall remain correctable.
88. Machine-readable contracts govern exact persisted structure.
89. Prose shall not become a shadow schema.
90. Canonical registries shall remain authoritative.
91. Entity, Relationship, and Knowledge Graph responsibilities shall remain distinct.
92. Current reasoning relevance shall not rewrite canonical Relationship semantics.
93. Stable Relationship semantics support reliable Learning.
94. Memory retrieval shall respect Relationship semantics and Context.
95. Upstream source changes may require downstream Relationship review.
96. Missing Relationships are valid Knowledge gaps.
97. Natural user language may map to canonical Relationship semantics.
98. Ambiguous user language shall not be silently upgraded to stronger semantics.

---

## 102. Prohibited Cognitive Behaviors

A.R.I.A. shall not:

- create canonical Relationship types outside the authoritative registry;
- treat prose examples as canonical Relationship vocabulary;
- invent Relationship identifier formats outside authoritative contracts;
- confuse Relationship identity with Relationship type;
- collapse Semantic Relationship records and Knowledge Graph edges when authoritative contracts distinguish them;
- encode mutable technical meaning unnecessarily into stable identifiers;
- represent vague association as causality without support;
- strengthen Relationship semantics to support a preferred conclusion;
- reverse directional Relationships without canonical inverse semantics;
- invent inverse Relationships;
- infer symmetry without canonical authority;
- replace canonical Relationships with artificial compound Entities;
- hide meaningful canonical Relationships inside arbitrary properties;
- use free text as the sole semantic representation where canonical structure is required;
- create new Relationship types merely because Context changes;
- generalize conditional Relationships beyond supported conditions;
- convert technical possibility into current diagnostic Probability;
- force probabilistic semantics onto deterministic technical facts;
- treat historical frequency as deterministic causality;
- invent numerical Relationship-strength meaning without methodology;
- create an independent Relationship confidence authority;
- treat canonical Relationships as current Evidence;
- persist every Case-specific Evidence Relationship as reusable canonical technical Knowledge;
- allow Relationship Architecture to own hypothesis state;
- allow Relationship Architecture to own diagnostic Probability;
- create a competing Relationship-level Uncertainty system;
- create a competing Relationship Validation state machine;
- allow Relationship Architecture to independently select Actions;
- allow Relationship Architecture to independently control Routing;
- allow Relationship Architecture to redefine Learning;
- recreate an independent Experience Ledger;
- allow historical co-occurrence to silently strengthen canonical semantics;
- allow Memory retrieval frequency to determine Relationship truth;
- create competing provenance structures;
- treat graph persistence as Source Authority;
- count dependent sources as independent corroboration;
- erase contradictory Relationships merely to simplify reasoning;
- invent consensus when contradiction remains unresolved;
- treat absence from the graph as explicit negation;
- invent negative Knowledge without support;
- ignore temporal applicability;
- treat superseded historical Relationships as automatically false;
- create lifecycle enums through prose;
- create Validation enums through prose;
- promote model-inferred Relationships directly into canonical Knowledge without governance;
- infer causality from repeated co-occurrence alone;
- modify material Relationships without preserving lineage;
- ignore downstream dependencies after Relationship correction;
- delete historically important Relationships merely because they are obsolete;
- merge Relationships based solely on similar wording;
- prevent Relationship splits when prior modeling is discovered to be overly broad;
- treat multi-hop graph connectivity as proof of diagnosis;
- ignore semantic differences during traversal;
- ignore directionality during traversal;
- ignore Context during traversal;
- ignore temporal applicability during traversal;
- collapse distinct negative semantics;
- treat every graph cycle as corrupt Knowledge;
- create permanent Relationships for every incidental association;
- use generic Relationships when more precise supported semantics exist;
- use stronger semantics than the Knowledge supports;
- create universal Relationship types for every product-specific phrase;
- rebuild Relationship architecture for every new technical domain;
- hardcode telecommunications as the limit of universal Relationship architecture;
- inflate user-facing explanations beyond canonical semantic strength;
- make canonical Relationships dependent upon one language model;
- store canonical Relationships only in temporary conversation context;
- bind Relationship semantics permanently to repository location;
- freeze early Relationship assumptions merely because they were implemented first;
- allow prose documentation to become a competing machine-readable schema;
- silently introduce unregistered Relationship types through application code, Learning, ingestion, or model output;
- allow current diagnostic importance to rewrite canonical Relationship meaning;
- fabricate a Relationship to fill a Knowledge gap;
- force users to speak canonical Relationship vocabulary;
- or interpret ambiguous user wording as the strongest possible Relationship merely because doing so produces a cleaner answer.

---

## 103. Final Principle

A.R.I.A.'s Relationship Architecture gives structure to how the things she understands connect.

A Relationship is not merely a line between two database records.

It carries semantic meaning.

That meaning may express causality, dependency, hierarchy, compatibility, requirement, support, contradiction, procedure, configuration, or another canonical relationship defined by the authoritative registry.

Those semantics must remain stable enough to support durable Knowledge while flexible enough to evolve as A.R.I.A.'s understanding improves.

Canonical Relationships must remain distinct from current Evidence, hypotheses, Probability, Uncertainty, Validation, Decision, Routing, Learning, and Memory.

Historical experience may inform Relationship discovery through Learning, but it shall not operate through a competing Experience Ledger or silently transform frequency into deterministic truth.

Context must determine applicability without multiplying unnecessary Relationship vocabularies.

Provenance must preserve lineage without becoming Relationship meaning.

Source Authority must evaluate legitimate support without being confused with graph persistence.

Contradictions must remain visible until legitimately resolved.

Historical Relationships must remain available when necessary without being mistaken for current Knowledge.

Language models may help extract, interpret, and propose Relationships, but they shall not own canonical semantics or grant themselves authority to create technical truth.

And as A.R.I.A. expands across manufacturers, products, technologies, and eventually entirely different domains, the same canonical Relationship architecture should allow new Knowledge to connect naturally to what already exists — **without requiring the cognitive architecture to be rebuilt every time her understanding evolves.**
