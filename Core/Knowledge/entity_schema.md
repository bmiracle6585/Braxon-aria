# A.R.I.A. Entity Architecture

**Document Type:** Canonical Knowledge and Reasoning Specification  
**Authority:** Subordinate to `Core/Schemas/entity_contracts.json`, `Core/Registries/entity_types.json`, `Core/Schemas/entity.schema.json`, applicable canonical registries and schemas, and `Core/Persona/ARIA_CONSTITUTION.md`  
**Version:** 2.0.0

---

## 1. Purpose

This document defines the architectural principles governing how A.R.I.A. represents, identifies, distinguishes, reuses, relates, and evolves canonical Entities.

Entities answer:

> **What thing, concept, state, condition, object, or other independently meaningful subject exists within A.R.I.A.'s canonical Knowledge architecture?**

Entities provide stable identity.

Relationships describe how Entities interact.

Context determines applicability.

Provenance describes lineage.

Source Authority evaluates the authority of information supporting Knowledge.

Evidence describes information relevant to the current Case.

Hypotheses represent propositions being evaluated.

Probability represents current belief.

Validation determines what current results demonstrate.

Learning qualifies generalizable historical experience.

Memory retrieves relevant persistent information.

These structures shall remain distinct.

The Entity Architecture exists so A.R.I.A. can continuously expand her Knowledge without becoming a collection of:

- duplicate names;
- manufacturer-specific copies of universal concepts;
- transient observations represented as permanent concepts;
- source-document fragments mistaken for Entities;
- Case-specific state embedded into canonical identity;
- or unstructured model-generated terminology.

---

## 2. Canonical Authority

Entity architecture is governed by the applicable machine-readable contracts and registries.

Current primary authorities include:

1. `Core/Schemas/entity_contracts.json`
2. `Core/Registries/entity_types.json`
3. `Core/Schemas/entity.schema.json`
4. applicable canonical registries and schemas
5. `Core/Knowledge/relationship_schema.md`
6. `Core/Knowledge/knowledge_graph.md`
7. this document
8. `Core/Persona/ARIA_CONSTITUTION.md` as constitutional authority over the system

`Core/Schemas/entity_contracts.json` owns canonical Entity identity and shared interoperability contracts.

`Core/Registries/entity_types.json` owns canonical Entity-type vocabulary.

`Core/Schemas/entity.schema.json` owns machine-readable validation of canonical Entity records.

Applicable Relationship contracts own canonical Relationship vocabulary and semantics.

This document explains how those authorities should be interpreted together.

It shall not independently establish competing:

- Entity types;
- Entity identifiers;
- identifier prefixes;
- Relationship types;
- Context vocabularies;
- lifecycle enums;
- Validation states;
- confidence scales;
- provenance structures;
- source-authority classifications;
- Learning structures;
- Memory structures;
- or persistence contracts.

Where this doctrine conflicts with a more specific authoritative machine-readable contract, the more specific contract governs.

---

## 3. Fundamental Principle

An Entity should exist when stable independent identity materially improves A.R.I.A.'s ability to:

- understand Knowledge;
- connect Knowledge;
- reason;
- retrieve;
- preserve provenance;
- apply Context;
- distinguish technical concepts;
- learn across Cases;
- explain conclusions;
- or evolve the Knowledge architecture.

Not every noun deserves an Entity.

Not every observation deserves an Entity.

Not every value deserves an Entity.

Not every sentence deserves an Entity.

The objective is:

> **stable semantic identity where stable semantic identity provides durable cognitive value.**

---

## 4. Entity Design Principle

A canonical Entity should exist when representing a concept independently materially improves one or more of:

- technical reasoning;
- retrieval;
- Relationship modeling;
- contextual filtering;
- source attribution;
- historical analysis;
- qualified Learning;
- diagnostic Routing;
- Decision;
- explanation;
- reuse;
- interoperability;
- or future extensibility.

The goal is meaningful technical structure.

The goal is not maximum Entity count.

---

## 5. Canonical Entity Identity

Every persisted canonical Entity shall use identity according to the applicable authoritative machine-readable contracts.

Canonical identity shall not be invented from examples in this doctrine.

Where `Core/Schemas/entity_contracts.json` establishes:

- identifier form;
- typed prefixes;
- UUID requirements;
- namespace rules;
- or other identity requirements,

those definitions govern.

This document shall not duplicate those definitions as a competing registry.

---

## 6. Stable Identity Is Required

A canonical Entity's identity should remain stable despite changes to:

- display name;
- preferred terminology;
- alias;
- abbreviation;
- capitalization;
- manufacturer terminology;
- UI wording;
- repository location;
- source-document location;
- model terminology;
- or ordinary descriptive text.

Stable identity allows the Entity's:

- Relationships;
- provenance;
- Knowledge;
- historical references;
- Context;
- learned information;
- and downstream dependencies

to remain attached to the same concept over time.

---

## 7. Identity Is Not Display Name

The display name of an Entity is human-readable presentation.

It is not canonical identity.

Two Entities may have similar names while representing different concepts.

One Entity may have many names while representing one concept.

A.R.I.A. shall not use display text alone as the authoritative identity mechanism.

---

## 8. Identity Is Not Source Wording

A source may use terminology different from A.R.I.A.'s canonical terminology.

For example, multiple sources may use:

- abbreviations;
- legacy terminology;
- vendor-specific terminology;
- colloquial terminology;
- translated terminology;
- or descriptive phrases

for the same underlying concept.

Where technically justified, those terms should resolve to the same canonical Entity rather than creating duplicate Knowledge.

---

## 9. Most-Specific Established Identity Should Be Used

Where authoritative contracts define dedicated identity classes for particular canonical Entity categories, A.R.I.A. should use the most specific applicable established identity.

She shall not use a generic identity merely because doing so is easier if a more precise canonical identity class already exists.

The exact identity classes and prefixes are owned by the applicable machine-readable contracts.

This doctrine shall not freeze them through duplicated examples.

---

## 10. Generic Identity Remains Valid Where Appropriate

A generic canonical Entity identity may be appropriate where:

- no dedicated canonical identity class exists;
- the concept is still independently meaningful;
- and the applicable authoritative contract permits the generic identity.

Generic does not mean weak.

It means the architecture has not established a more specialized identity namespace for that concept.

---

## 11. Entity Type and Entity Identity Are Distinct

An Entity's identifier and its semantic type are related but distinct concepts.

The canonical type vocabulary is governed by:

`Core/Registries/entity_types.json`

The canonical identity contract is governed by:

`Core/Schemas/entity_contracts.json`

A.R.I.A. shall not infer unsupported Entity types solely from identifier appearance.

Nor shall she invent identifier namespaces solely because a new Entity type exists.

---

## 12. Entity Types Must Be Explicitly Registered

Canonical Entity types shall come from the authoritative Entity-type registry.

This doctrine shall not establish additional Entity types through prose examples.

If a new technical concept requires a new canonical Entity type, the appropriate registry should be deliberately extended according to governance.

This prevents accidental taxonomy drift.

---

## 13. Examples Are Not Registries

Any Entity examples appearing in documentation, prompts, Cases, source material, or model responses shall not become canonical Entity types merely because they were written in uppercase or presented as categories.

Only the authoritative registry defines canonical Entity-type vocabulary.

This principle applies equally to legacy documentation.

---

## 14. Aliases Belong to Identity Resolution

An alias is another expression referring to an existing canonical Entity.

Aliases may include:

- abbreviations;
- acronyms;
- spelling variants;
- punctuation variants;
- vendor terminology;
- historical names;
- shorthand;
- colloquial terms;
- and other equivalent expressions.

Alias handling shall follow the applicable authoritative Entity contracts.

Aliases shall not automatically create separate Entities.

---

## 15. Alias Resolution Must Preserve Meaning

A.R.I.A. shall resolve two terms to one Entity only when they genuinely represent the same underlying concept.

Similarity of wording is insufficient.

Entity resolution should consider, where applicable:

- technical meaning;
- product scope;
- revision;
- manufacturer;
- Context;
- units;
- function;
- Relationship structure;
- provenance;
- and other distinguishing information.

False merging is as damaging as duplication.

---

## 16. Ambiguous Aliases Must Remain Ambiguous

One term may legitimately refer to multiple different concepts.

A.R.I.A. shall not force ambiguous terminology into one canonical Entity merely because the same text appears in several places.

Where necessary, Context or additional information should resolve the intended Entity.

If ambiguity remains unresolved, it should remain unresolved rather than being guessed.

---

## 17. Distinct Concepts Must Remain Distinct

Canonical reuse shall not collapse materially different concepts.

Entities should remain distinct where differences materially affect:

- reasoning;
- Relationships;
- Context;
- technical behavior;
- source applicability;
- historical analysis;
- or explanation.

Examples of potentially meaningful distinctions include:

- product versus product variant;
- physical interface versus logical interface;
- symptom versus root cause;
- measurement type versus measurement observation;
- unit versus measured value;
- procedure versus Action execution;
- generic component versus specific installed component;
- technical concept versus Case-specific instance.

The authoritative Entity registry determines actual canonical types.

---

## 18. Universal Concepts Should Be Reused

A.R.I.A. should avoid unnecessary duplication of universal concepts across:

- manufacturers;
- customers;
- Cases;
- projects;
- participants;
- applications;
- and domains.

Where the underlying concept is genuinely the same, one canonical Entity should normally be reused with appropriate Relationships and Context.

This allows Knowledge learned in one area to become available elsewhere when applicable.

---

## 19. Manufacturer Terminology Does Not Automatically Create New Concepts

Manufacturers often use proprietary terminology for concepts that may be:

- universal;
- standardized;
- implementation-specific;
- or partly equivalent to broader concepts.

A.R.I.A. should determine whether the manufacturer term represents:

1. an alias of an existing canonical Entity;
2. a more specific Entity;
3. a product-specific Entity;
4. or a genuinely distinct technical concept.

She shall not automatically create manufacturer-specific duplicates.

She shall also not incorrectly collapse genuinely proprietary behavior into an overly generic concept.

---

## 20. Product-Specific Concepts May Require Distinct Entities

A concept should remain product-specific when product identity materially changes its technical meaning.

Examples may include:

- proprietary components;
- product-specific interfaces;
- unique operating modes;
- vendor-defined configuration objects;
- model-specific procedures;
- or implementation-specific behavior.

The purpose of canonical reuse is not to erase legitimate product distinctions.

---

## 21. Revision Does Not Automatically Create a New Entity

A revision change does not necessarily require a new canonical Entity.

The appropriate representation depends upon whether the revision represents:

- the same concept with changed properties;
- a new variant;
- a new product;
- a new behavior;
- a historical state;
- or another semantically distinct object.

The authoritative Entity and Context contracts should govern the representation.

A.R.I.A. shall not automatically create a new Entity for every revision number.

---

## 22. Revision May Require a Distinct Entity

Where a revision materially changes identity rather than merely Context or properties, a distinct Entity may be appropriate.

The distinction should be based upon technical meaning and authoritative schema—not arbitrary version counting.

This preserves precision without creating unnecessary graph explosion.

---

## 23. Entity and Context Must Remain Distinct

Context answers:

> **Under what circumstances does this Knowledge or Relationship apply?**

Entity answers:

> **What canonical thing or concept is being represented?**

A.R.I.A. shall not create separate Entities merely to encode every possible Context combination.

For example, Context such as:

- firmware;
- date;
- jurisdiction;
- configuration;
- topology;
- environment;
- or operating mode

should remain Context when the underlying Entity identity has not changed.

Context Engine owns canonical Context semantics.

---

## 24. Entity and Property Must Remain Distinct

Not every characteristic of an Entity should become another Entity.

A property may be more appropriate when the information:

- describes the Entity;
- does not require independent identity;
- does not require independent Relationships;
- does not require separate provenance;
- and does not materially benefit reasoning as a reusable concept.

The applicable Entity schema determines canonical record structure.

---

## 25. Entity and Value Must Remain Distinct

A value observed or assigned to an Entity is not automatically another Entity.

For example, conceptually:

**MEASUREMENT TYPE**

may be a canonical Entity.

A specific Case observation such as:

> -67 dBm

is typically current Evidence or observation data rather than a new permanent canonical technical Entity.

The authoritative schemas determine the exact representation.

---

## 26. Entity and Observation Must Remain Distinct

Case-specific observations shall not automatically become canonical Entities.

An observation may describe:

- current state;
- measured value;
- visible condition;
- test result;
- user report;
- system output;
- or another Case-specific fact.

Evidence Engine owns current Evidence.

Canonical Entities provide the stable concepts to which Evidence may refer.

---

## 27. Entity and Evidence Must Remain Distinct

An Entity may be the subject of Evidence.

The Evidence itself is not automatically an Entity.

For example:

**Canonical Entity**

Received Signal Level

**Current Evidence**

Observed RSL = -71 dBm

The Entity represents the reusable measurement concept.

The Evidence represents what was observed now.

This distinction prevents Case data from polluting canonical Knowledge.

---

## 28. Entity and Hypothesis Must Remain Distinct

A canonical Entity may represent a:

- condition;
- failure mechanism;
- component;
- symptom;
- configuration concept;
- or another reusable technical concept.

A current hypothesis is a Case-specific proposition involving one or more concepts.

Hypothesis Engine owns hypothesis state.

The existence of an Entity does not mean that Entity is currently suspected.

---

## 29. Entity and Probability Must Remain Distinct

Canonical Entities do not own current diagnostic Probability.

Probability attaches to current reasoning propositions according to the authoritative Probability architecture.

An Entity may appear in many Cases with different probabilities.

Its canonical identity remains unchanged.

---

## 30. Entity and Validation Must Remain Distinct

Canonical Entities may represent concepts involved in Validation.

They do not themselves become validated or invalidated merely because a current Case test passes or fails.

Validation Engine owns what current results demonstrate.

Entity architecture owns stable semantic identity.

---

## 31. Entity and Learning Must Remain Distinct

Learning may discover useful recurring patterns involving canonical Entities.

For example, qualified historical Learning may discover that a particular condition frequently appears with a particular symptom under comparable Context.

Learning Engine owns qualification of that historical pattern.

Entity architecture owns the identity of the concepts participating in it.

There is no independent Experience Entity authority merely because historical experience exists.

---

## 32. There Is No Independent Experience Entity System

Earlier architecture sometimes treated Experience as a separate canonical cognitive structure.

That model is obsolete.

Historical experience is governed through the coordinated architecture involving, as applicable:

- Case State;
- Context;
- Evidence;
- Actions;
- Observations;
- Validation;
- Learning;
- Memory;
- and persistent historical records.

Canonical Entities may participate in those structures.

Entity architecture shall not create an independent Experience ontology unless a future explicit authoritative schema deliberately establishes one.

---

## 33. Entity and Memory Must Remain Distinct

Memory may retrieve information about canonical Entities.

Retrieval does not create or redefine Entity identity.

An Entity is not more canonical because it was retrieved frequently.

Memory Engine owns retrieval.

Entity architecture owns canonical identity.

---

## 34. Entity and Source Must Remain Distinct

A source may discuss or define an Entity.

The source itself is not automatically the same Entity as the technical concept it describes.

Where source objects require canonical representation, they shall follow the applicable authoritative schemas.

Entity architecture shall preserve the distinction between:

> the thing being described

and

> the material describing it.

---

## 35. Entity and Provenance Must Remain Distinct

Provenance answers where Knowledge came from.

Entity identity answers what concept is being represented.

A.R.I.A. shall not create separate canonical technical Entities merely because the same concept came from different sources.

Multiple sources may support Knowledge concerning one Entity.

`provenance_schema.md` owns provenance.

---

## 36. Entity and Source Authority Must Remain Distinct

An Entity does not become more or less real because one source has stronger authority.

Source Authority evaluates information supporting claims involving Entities.

It does not determine Entity identity by itself.

`source_authority.md` owns Source Authority principles.

---

## 37. Entity and Relationship Must Remain Distinct

Entities represent concepts.

Relationships represent semantic connections between concepts.

A.R.I.A. shall not encode a Relationship solely by creating compound Entity names when the authoritative Relationship architecture provides the appropriate structure.

For example, conceptually:

**A CAUSES B**

should normally be represented through canonical Entities and a canonical Relationship rather than inventing an Entity named:

> "A-causes-B"

unless such a compound concept independently deserves Entity identity.

---

## 38. Relationship Schema Owns Relationship Semantics

`Core/Knowledge/relationship_schema.md` and applicable machine-readable Relationship contracts own:

- Relationship vocabulary;
- Relationship directionality;
- inverse semantics;
- Relationship identity;
- Relationship properties;
- causal meaning;
- dependency meaning;
- compatibility meaning;
- and other canonical Relationship semantics.

Entity Architecture shall not redefine those concepts.

---

## 39. Entity Creation Requires Semantic Justification

Before creating a new canonical Entity, A.R.I.A. should determine whether the proposed concept is:

- already represented;
- an alias;
- a property;
- a value;
- a Context condition;
- a Relationship;
- current Evidence;
- a current hypothesis;
- a Case-specific instance;
- or genuinely a new canonical Entity.

This decision protects Knowledge quality.

---

## 40. Entity Creation Should Prefer Reuse

When a technically equivalent canonical Entity already exists, A.R.I.A. should reuse it.

Creating duplicates damages:

- graph traversal;
- Learning;
- retrieval;
- provenance;
- Relationship analysis;
- historical reasoning;
- and explanation.

Reuse is the default when identity equivalence is established.

---

## 41. Entity Creation Must Not Force False Reuse

Reuse shall not be pursued at the expense of correctness.

When two concepts are materially different, A.R.I.A. shall preserve separate Entities.

False merging can cause more severe reasoning errors than duplication.

Canonicalization requires semantic judgment.

---

## 42. Entity Resolution May Require Investigation

A.R.I.A. may encounter two candidate Entities whose equivalence cannot immediately be determined.

She should be able to investigate:

- source definitions;
- product scope;
- revision;
- Relationships;
- properties;
- Context;
- aliases;
- and provenance.

If equivalence remains uncertain, A.R.I.A. shall not invent a merge.

---

## 43. Unknown Identity Is Valid

A.R.I.A. may encounter a concept that appears meaningful but cannot yet be confidently resolved to an existing Entity or established as a new canonical Entity.

Unknown identity is a valid state.

The system may preserve candidate information according to the authoritative ingestion architecture.

A.R.I.A. shall not fabricate canonical identity merely to avoid uncertainty.

---

## 44. Candidate Entities Must Remain Distinguishable

A model, source-ingestion process, user, or Learning process may propose a candidate Entity.

Candidate status does not automatically create canonical status.

Canonical promotion shall follow applicable Knowledge governance.

This doctrine shall not create a competing Entity lifecycle enum.

---

## 45. Canonical Entity Governance Must Be Explicit

If canonical lifecycle states for Entities are required, they shall be defined by an explicit authoritative registry or schema.

This doctrine shall not silently establish universal states such as:

- proposed;
- validated;
- approved;
- deprecated;
- rejected;
- superseded;

merely through descriptive language.

Descriptions are not registries.

---

## 46. Entity Evolution Must Preserve Identity Where Appropriate

When understanding of an existing Entity improves, A.R.I.A. should normally evolve its:

- properties;
- aliases;
- Relationships;
- provenance;
- Context;
- or documentation

without changing canonical identity unless the original identity itself was incorrect.

This allows Knowledge to mature without breaking historical references.

---

## 47. Identity Correction Must Preserve History

If an Entity was incorrectly identified, duplicated, or merged, correction should preserve enough history to understand:

- the prior identity;
- the corrected identity;
- affected aliases;
- affected Relationships;
- affected Knowledge;
- affected provenance;
- and downstream dependencies.

The applicable governance and orchestration architecture owns the correction process.

---

## 48. Entity Merge Must Be Governed

Merging Entities can materially change the Knowledge Graph.

A merge should occur only when the Entities are determined to represent the same canonical concept.

A merge may require reconciliation of:

- aliases;
- properties;
- Relationships;
- provenance;
- source references;
- historical Cases;
- learned information;
- and dependent Knowledge.

A.R.I.A. shall not perform semantic merges casually.

---

## 49. Entity Split Must Be Governed

A previously unified Entity may later be discovered to contain multiple materially distinct concepts.

A split may require:

- new canonical identities;
- Relationship reassignment;
- provenance review;
- source review;
- Context review;
- historical reprocessing;
- and downstream dependency analysis.

The architecture must support correction rather than freezing early modeling mistakes.

---

## 50. Deletion Should Be Exceptional

Canonical Entities with historical dependencies should not normally disappear merely because they are no longer current.

Historical identity may remain necessary for:

- legacy systems;
- old Cases;
- superseded products;
- prior documentation;
- historical decisions;
- or auditability.

Where governance requires retirement, the architecture should preserve appropriate historical lineage.

---

## 51. Supersession Does Not Necessarily Replace Identity

A newer Entity may supersede an older Entity without becoming the same Entity.

For example, a new product may replace an old product commercially while remaining technically distinct.

Supersession is a Relationship or governance concept.

It shall not automatically collapse identities.

---

## 52. Historical Entities Remain Valuable

Entities representing:

- legacy products;
- obsolete standards;
- retired components;
- superseded procedures;
- or historical technical concepts

may remain necessary for historical reasoning.

Current applicability and historical existence are different questions.

---

## 53. Entity Properties Must Not Become Hidden Relationships

Where information represents a meaningful connection between independently identifiable concepts, it may belong as a Relationship rather than an opaque property.

The applicable schemas govern the implementation.

A.R.I.A. should avoid burying reasoning-relevant semantics inside unstructured text properties when canonical Relationships exist.

---

## 54. Relationships Must Not Become Hidden Properties

If the authoritative Relationship architecture defines a semantic connection, Entity records should not independently invent competing ad hoc fields expressing the same relationship.

This prevents parallel representations such as:

- one source using a Relationship;
- another using a property;
- another using free text

for the same canonical meaning.

Canonical structure should converge.

---

## 55. Free Text Is Not Canonical Semantics

Descriptive text may be valuable for:

- explanation;
- source excerpts;
- notes;
- human readability;
- and context.

Free text shall not substitute for canonical Entity identity or canonical Relationships when structured semantics are required.

A.R.I.A. should preserve both where useful.

---

## 56. Entity Granularity Must Serve Reasoning

Entity granularity should be neither excessively broad nor excessively narrow.

An Entity is too broad when materially different concepts become indistinguishable.

An Entity is too narrow when every trivial variation creates a new identity without reasoning benefit.

Granularity should support:

- meaningful Relationships;
- Context;
- retrieval;
- Learning;
- provenance;
- and explanation.

---

## 57. Avoid Entity Explosion

A.R.I.A. shall not create permanent canonical Entities for every:

- observed value;
- conversation phrase;
- source sentence;
- temporary state;
- one-time Action;
- incidental object;
- typo;
- UI string;
- or unqualified model suggestion.

Entity growth should be deliberate.

---

## 58. Avoid Entity Scarcity

The opposite error is also harmful.

A.R.I.A. shall not force materially independent concepts into:

- free text;
- generic blobs;
- oversized records;
- or vague labels

merely to minimize Entity count.

If independent identity materially improves reasoning, an Entity may be appropriate.

---

## 59. Case-Specific Instances May Differ From Canonical Concepts

A canonical Entity may represent a reusable technical concept.

A specific Case may involve an instance of that concept.

Conceptually:

**Canonical Entity**

Ethernet cable

**Case-specific instance**

The physical cable currently connecting Device A to Device B.

These are not necessarily the same object.

The applicable Case and Entity schemas determine whether and how instance identity is persisted.

---

## 60. Installed Equipment May Require Instance Identity

A physical installed object may require persistent identity when doing so materially supports:

- asset tracking;
- configuration history;
- topology;
- maintenance;
- failure history;
- customer infrastructure;
- or Case continuity.

Such identity shall follow applicable authoritative schemas.

The universal Entity doctrine shall not invent a parallel asset-management system.

---

## 61. Concept Identity and Instance Identity Must Remain Distinguishable

A.R.I.A. shall distinguish where applicable between:

> the canonical concept of a product

and

> one specific physical instance of that product.

Knowledge about the product may apply to many instances.

Evidence concerning one physical instance shall not automatically become universal product Knowledge.

---

## 62. Manufacturer, Product Family, Product, and Variant Must Remain Semantically Distinct

Where the canonical registry defines these or comparable Entity types, A.R.I.A. shall preserve their distinct semantic roles.

A manufacturer is not a product.

A product family is not necessarily a product.

A product is not necessarily a product variant.

A.R.I.A. shall use the authoritative taxonomy rather than flattening hierarchy into names.

---

## 63. Hierarchy Is Not Identity

An Entity may participate in hierarchical Relationships without its identity being derived solely from its parent.

Moving or reclassifying an Entity within a hierarchy shall not automatically require changing canonical identity.

Relationship Schema owns hierarchy semantics.

---

## 64. Entity Identity Must Survive Taxonomy Evolution

A.R.I.A.'s taxonomy may improve.

An Entity may later be classified more precisely.

Where the underlying concept has not changed, canonical identity should normally survive the classification improvement.

This prevents taxonomy evolution from breaking Knowledge history.

---

## 65. Domain Expansion Should Reuse the Entity Architecture

Adding new technical domains should primarily require:

- new canonical Entities;
- new registered Entity types where genuinely necessary;
- new Relationships;
- new Context;
- and new Knowledge.

It should not require rebuilding the Entity architecture.

The architecture shall remain domain-independent.

---

## 66. New Entity Types Should Be Added Deliberately

A new domain does not automatically require dozens of new Entity types.

Before adding a type, A.R.I.A.'s governance process should determine whether:

- an existing type already fits;
- a generic canonical Entity is sufficient;
- the distinction materially improves reasoning;
- the distinction is stable;
- and the distinction is broadly useful.

Taxonomy should grow deliberately.

---

## 67. Entity Types Should Not Encode One Product's Ontology Universally

A product may contain proprietary concepts.

Those concepts may deserve Entities.

They do not automatically deserve new universal Entity types.

A.R.I.A. shall distinguish:

> new Entity

from

> new Entity type.

This is essential for long-term extensibility.

---

## 68. Entity Architecture Must Remain Domain-Independent

The universal Entity architecture shall not hardcode its cognitive structure around:

- microwave backhaul;
- RF;
- Ethernet;
- telecommunications;
- a specific manufacturer;
- a specific customer;
- a specific organization;
- or a named participant.

Those domains populate the architecture.

They do not define its universal limits.

---

## 69. Telecommunications Is Knowledge, Not the Architecture

A.R.I.A. may become deeply knowledgeable about telecommunications.

Telecommunications-specific:

- manufacturers;
- products;
- components;
- measurements;
- tools;
- failure mechanisms;
- procedures;
- and technical concepts

belong in canonical Knowledge and applicable registries.

They shall not turn the universal Entity doctrine into a telecommunications-only ontology.

---

## 70. Entity Architecture Must Support Future Domains

The same architecture should be capable of representing future domains such as:

- software;
- electrical systems;
- mechanical systems;
- construction;
- finance;
- business operations;
- logistics;
- regulatory processes;
- or other authorized areas

without fundamental redesign.

New domain Knowledge should extend the system rather than replace its foundations.

---

## 71. Provenance Must Attach to Knowledge About Entities

A canonical Entity may be referenced by many Knowledge claims originating from many sources.

A.R.I.A. should preserve provenance for material Knowledge concerning the Entity.

She shall not assume that the Entity itself requires one single source explaining everything known about it.

Different claims may have different provenance.

---

## 72. Entity Existence and Claim Provenance Are Different

An Entity may be well established while one particular claim about it has weak provenance.

Likewise, a newly introduced Entity may be supported by highly authoritative documentation.

A.R.I.A. shall evaluate claims independently rather than treating all information concerning an Entity as equally sourced.

---

## 73. Source Authority Is Claim-Specific

Source Authority concerning an Entity must remain claim-specific and contextual.

One source may be highly authoritative regarding:

- product specifications

while another is authoritative regarding:

- customer implementation

and another regarding:

- current Case observation.

The Entity provides shared identity across those claims.

It does not flatten their authority.

---

## 74. Contradictory Claims May Reference the Same Entity

A.R.I.A. shall allow conflicting Knowledge about the same Entity to remain represented when unresolved.

She shall not create duplicate Entities merely to separate contradictory claims if the claims concern the same underlying concept.

Contradiction belongs to Knowledge governance and provenance.

Identity should remain stable.

---

## 75. Contradiction May Reveal Identity Error

Sometimes contradictory information indicates that two references thought to concern one Entity actually concern different concepts.

A.R.I.A. should investigate whether the conflict arises from:

- revision;
- variant;
- product;
- manufacturer;
- Context;
- terminology;
- or mistaken Entity resolution.

Contradiction may therefore trigger identity review.

---

## 76. Entity Resolution Should Use Relationships

Relationships may provide important evidence for identity resolution.

Two similarly named concepts connected to different:

- manufacturers;
- products;
- functions;
- units;
- components;
- or technical behaviors

may be distinct.

Likewise, two differently named concepts with equivalent Relationship structure may be aliases.

Entity resolution should not rely on string similarity alone.

---

## 77. Entity Resolution Should Use Context

Context may determine whether two references identify the same concept.

For example, the same shorthand may mean different things:

- across manufacturers;
- across technical domains;
- across software systems;
- across jurisdictions;
- or across organizations.

Context Engine owns canonical Context semantics.

Entity resolution may consume Context.

---

## 78. Entity Resolution Should Use Provenance

Source provenance may clarify:

- intended terminology;
- product scope;
- revision;
- author meaning;
- manufacturer terminology;
- or historical naming.

Provenance may therefore assist Entity resolution.

Provenance does not independently own identity.

---

## 79. Entity Resolution Should Be Explainable

Where materially important, A.R.I.A. should be able to explain why two terms were:

- merged;
- kept separate;
- treated as aliases;
- or left unresolved.

For example:

> "These are the same canonical measurement concept; one is the vendor abbreviation and the other is the full technical name."

Or:

> "These names look similar, but they refer to different product variants and must remain separate."

The explanation should reflect actual canonical state.

---

## 80. Entity Resolution Must Not Be Post-Hoc

A.R.I.A. shall not manipulate Entity identity merely to make a preferred reasoning conclusion appear consistent.

Entity resolution should follow semantic evidence and authoritative architecture.

Identity shall not be rewritten to fit a desired diagnosis.

---

## 81. Entity Changes May Affect Downstream Knowledge

Changing canonical Entity identity or resolution may affect:

- Relationships;
- source mappings;
- historical Cases;
- learned patterns;
- routing Knowledge;
- current reasoning;
- application data;
- and downstream derived Knowledge.

Material Entity changes should therefore support dependency review.

---

## 82. Entity Corrections May Require Reprocessing

If A.R.I.A. discovers that Entities were:

- duplicated;
- incorrectly merged;
- incorrectly typed;
- incorrectly mapped;
- or incorrectly resolved,

dependent Knowledge may require reprocessing.

Orchestration and Knowledge governance own that process.

Entity architecture must make correction possible.

---

## 83. Entity Architecture Must Support Auditability

Authorized review should be able to determine, where applicable:

- what Entity exists;
- its canonical identity;
- its canonical type;
- its aliases;
- its Relationships;
- how it changed;
- what prior identities were reconciled;
- and what Knowledge depends upon it.

Auditability supports trustworthy evolution.

---

## 84. Entity Architecture Must Support Reproducibility

Where practical, A.R.I.A. should preserve enough information to reproduce material Entity-resolution decisions.

This may involve:

- aliases;
- source references;
- provenance;
- Context;
- Relationship structure;
- prior candidate identities;
- and governance history.

The exact persistence structure belongs to the authoritative schemas.

---

## 85. Entity Architecture Must Survive Conversation Length

Canonical Entity identity shall not depend upon temporary conversational context.

A.R.I.A. shall not forget that two terms refer to the same canonical Entity merely because an earlier conversation left the model context window.

Persistent architecture owns identity.

---

## 86. Entity Architecture Must Survive Model Replacement

Canonical Entity identity shall not belong to one language model.

Replacing:

- model provider;
- model version;
- inference implementation;
- prompt architecture;
- or reasoning model

shall not destroy:

- Entity IDs;
- aliases;
- types;
- Relationships;
- provenance;
- or identity history.

The language model may assist with resolution.

It does not own canonical identity.

---

## 87. Entity Architecture Must Survive Repository Reorganization

Moving source files or Knowledge files shall not inherently create new canonical Entities.

Repository paths are storage locations.

They are not Entity identity.

This prevents ordinary development work from breaking the Knowledge Graph.

---

## 88. Entity Architecture Must Support Schema Evolution

Canonical machine-readable schemas and registries may evolve.

The architecture should permit:

- new Entity types;
- improved validation;
- new properties;
- new identity namespaces;
- better interoperability;
- and improved governance

without requiring wholesale replacement of existing Knowledge.

Schema evolution should be deliberate and migration-aware.

---

## 89. Entity Architecture Must Not Freeze Early Assumptions

Early A.R.I.A. development may contain incomplete Entity classifications.

The architecture shall not preserve those assumptions forever merely because they were first.

A.R.I.A. should be capable of improving:

- taxonomy;
- alias resolution;
- granularity;
- identity mappings;
- and domain coverage

while preserving historical integrity.

---

## 90. Machine-Readable Contracts Are Authoritative

Where prose and machine-readable contracts differ concerning:

- valid Entity types;
- identifier formats;
- required fields;
- field types;
- validation;
- canonical enums;
- or persistence structure,

the applicable machine-readable authoritative contract governs unless constitutional authority requires otherwise.

This doctrine explains architecture.

It does not replace validation contracts.

---

## 91. Prose Shall Not Become a Shadow Schema

This document shall not be maintained as a second manual copy of every field and enum contained in machine-readable schemas.

Duplicating machine contracts into prose creates drift.

The prose should define:

- principles;
- boundaries;
- responsibilities;
- invariants;
- and interpretation.

The schemas define exact machine contracts.

---

## 92. Canonical Registries Must Remain Canonical

When a canonical registry defines vocabulary, A.R.I.A. shall use that registry rather than silently introducing new values in:

- model output;
- documentation;
- ingestion code;
- source normalization;
- or application logic.

If a new value is necessary, the registry should be deliberately extended.

---

## 93. Entity Architecture and Knowledge Graph

The Knowledge Graph uses canonical Entities as stable nodes or equivalent semantic objects according to implementation.

Entity Architecture owns:

> **what the canonical thing is.**

Relationship Architecture owns:

> **how canonical things relate.**

Knowledge Graph doctrine owns:

> **how durable structured Knowledge forms a connected system.**

These responsibilities shall remain separate.

---

## 94. Entity Architecture and Reasoning

Reasoning systems may consume canonical Entities to understand:

- symptoms;
- components;
- conditions;
- measurements;
- products;
- procedures;
- tools;
- configurations;
- and other concepts.

Reasoning state shall not redefine canonical identity merely because one Entity becomes more diagnostically important than another.

Entity identity is durable.

Reasoning relevance is contextual.

---

## 95. Entity Architecture and Routing

Routing may use canonical Entities when constructing or evaluating diagnostic paths.

Entity Architecture does not independently select the route.

Routing Engine owns route progression.

Canonical Entities provide stable semantic references used by the route.

---

## 96. Entity Architecture and Decision

Decision Engine may select Actions involving canonical Entities.

Entity Architecture does not independently decide what should be done.

For example, a Tool Entity may identify a reusable technical tool concept.

Decision determines whether using that tool is appropriate now.

---

## 97. Entity Architecture and Learning

Learning may generalize patterns involving canonical Entities across historical Cases.

Stable identity is essential for this.

If the same concept is represented by many duplicate Entities, Learning becomes fragmented.

If different concepts are incorrectly merged, Learning becomes corrupted.

Entity quality therefore directly affects Learning quality.

---

## 98. Entity Architecture and Memory

Memory may use canonical Entity identity to retrieve:

- prior Cases;
- relevant Knowledge;
- source material;
- learned patterns;
- and Relationships.

Stable Entity identity improves retrieval continuity.

Memory shall not create new canonical identity solely because a term appears frequently.

---

## 99. Entity Architecture and Explanation

Canonical Entities help A.R.I.A. explain technical reasoning consistently.

She may translate canonical terminology into user-friendly language without changing underlying identity.

The user does not need to see internal IDs during ordinary interaction.

Stable internal identity and natural external language should coexist.

---

## 100. User Terminology Should Be Respected Without Corrupting Canonical Identity

A user may use:

- shorthand;
- field terminology;
- informal names;
- customer terminology;
- or technically imperfect wording.

A.R.I.A. may understand and respond naturally using the user's language while internally resolving the intended canonical Entity where possible.

She shall not force the user to speak the ontology.

Nor shall she allow conversational wording to create unnecessary duplicate canonical Entities.

---

## 101. Unknown User Terminology Should Not Be Guessed Into Canonical Identity

If a user's term could refer to multiple Entities and Context does not resolve it, A.R.I.A. should preserve ambiguity or ask for clarification when materially necessary.

She shall not silently map ambiguous terminology to whichever Entity best fits a preferred conclusion.

---

## 102. Core Entity Invariants

The following principles shall remain true throughout A.R.I.A.'s architecture:

1. Entities provide stable canonical identity.
2. Entity Architecture is subordinate to authoritative machine-readable contracts and registries.
3. Entity types come from the canonical Entity-type registry.
4. Identifier rules come from the canonical Entity identity contracts.
5. Prose examples do not create canonical registry values.
6. Stable identity shall survive ordinary naming changes.
7. Identity is distinct from display name.
8. Identity is distinct from source wording.
9. The most-specific established canonical identity should be used where applicable.
10. Generic canonical identity remains valid where permitted.
11. Entity type and Entity identifier are distinct concepts.
12. Canonical Entity types must be explicitly registered.
13. Aliases do not automatically create new Entities.
14. Alias resolution must preserve technical meaning.
15. Ambiguous aliases may remain ambiguous.
16. Materially distinct concepts shall remain distinct.
17. Universal concepts should be reused where technically appropriate.
18. Manufacturer terminology does not automatically create duplicate universal concepts.
19. Product-specific concepts may remain distinct where technically necessary.
20. Revision does not automatically create a new Entity.
21. Revision may justify distinct identity when technical identity materially changes.
22. Entity and Context are distinct.
23. Entity and property are distinct.
24. Entity and value are distinct.
25. Entity and observation are distinct.
26. Entity and Evidence are distinct.
27. Entity and hypothesis are distinct.
28. Entity and Probability are distinct.
29. Entity and Validation are distinct.
30. Entity and Learning are distinct.
31. There is no independent Experience Entity authority.
32. Entity and Memory are distinct.
33. Entity and source are distinct.
34. Entity and provenance are distinct.
35. Entity and Source Authority are distinct.
36. Entity and Relationship are distinct.
37. Relationship Schema owns Relationship semantics.
38. Entity creation requires semantic justification.
39. Entity creation should prefer legitimate reuse.
40. Reuse shall not force false merging.
41. Entity resolution may require investigation.
42. Unknown identity is valid.
43. Candidate Entities shall remain distinguishable from canonical Entities.
44. Canonical Entity lifecycle states require explicit authoritative definition.
45. Entity evolution should preserve identity where appropriate.
46. Identity correction should preserve history.
47. Entity merge must be governed.
48. Entity split must be governed.
49. Deletion of historically referenced Entities should be exceptional.
50. Supersession does not automatically collapse identity.
51. Historical Entities may remain valuable.
52. Properties shall not hide canonical Relationships.
53. Relationships shall not be duplicated through competing ad hoc properties.
54. Free text shall not replace canonical semantics where structure is required.
55. Entity granularity shall serve reasoning.
56. Entity explosion shall be avoided.
57. Entity scarcity shall also be avoided.
58. Canonical concepts and Case-specific instances may be distinct.
59. Physical installed objects may require instance identity when authoritative schemas support it.
60. Concept identity and instance identity shall remain distinguishable.
61. Canonical hierarchy types shall remain semantically distinct where registered.
62. Hierarchy does not define identity by itself.
63. Identity should survive taxonomy refinement where the underlying concept remains the same.
64. Domain expansion should reuse the Entity architecture.
65. New Entity types should be added deliberately.
66. A new Entity does not automatically require a new Entity type.
67. Universal Entity architecture shall remain domain-independent.
68. Domain Knowledge populates the architecture rather than redefining it.
69. Provenance concerning Entity claims shall remain traceable.
70. Entity existence and claim provenance are distinct.
71. Source Authority concerning Entity claims is contextual and claim-specific.
72. Contradictory claims may reference the same canonical Entity.
73. Contradiction may trigger Entity-resolution review.
74. Entity resolution may use Relationships.
75. Entity resolution may use Context.
76. Entity resolution may use provenance.
77. Entity-resolution decisions should remain explainable.
78. Entity identity shall not be manipulated post-hoc to fit a desired conclusion.
79. Entity changes may affect downstream Knowledge.
80. Entity corrections may require reprocessing.
81. Entity architecture should support auditability.
82. Entity architecture should support reproducibility.
83. Entity identity shall survive conversation length.
84. Entity identity shall survive model replacement.
85. Entity identity shall survive repository reorganization.
86. Entity architecture shall support schema evolution.
87. Early taxonomy assumptions shall remain correctable.
88. Machine-readable contracts govern exact machine structure.
89. Prose shall not become a shadow schema.
90. Canonical registries shall remain authoritative.
91. Entity Architecture and Knowledge Graph responsibilities shall remain distinct.
92. Reasoning relevance shall not redefine canonical identity.
93. Routing owns route progression.
94. Decision owns Action selection.
95. Stable Entity identity supports reliable Learning.
96. Stable Entity identity supports reliable Memory.
97. Internal canonical identity and user-friendly language may coexist.
98. User terminology may be respected without corrupting canonical identity.
99. Ambiguous user terminology shall not be silently forced into unsupported identity.

---

## 103. Prohibited Cognitive Behaviors

A.R.I.A. shall not:

- create canonical Entity types outside the authoritative registry;
- invent identifier formats outside authoritative contracts;
- treat prose examples as canonical enums;
- use display names as canonical identity;
- use source wording as canonical identity;
- create duplicate Entities for simple aliases;
- merge terms solely because their strings are similar;
- force ambiguous aliases into one Entity;
- collapse materially distinct concepts;
- create manufacturer-specific copies of universal concepts without technical justification;
- erase legitimate product-specific distinctions in the name of reuse;
- create a new Entity automatically for every revision;
- encode Context solely by multiplying Entity identities;
- turn every Entity property into another Entity;
- turn every observed value into a canonical Entity;
- turn Case observations into permanent canonical technical Entities without justification;
- treat Evidence as Entity identity;
- treat current hypotheses as canonical Entities merely because they reference canonical concepts;
- attach diagnostic Probability to permanent Entity identity as though it were intrinsic;
- treat a current Validation result as permanent Entity validity;
- recreate an independent Experience ontology;
- treat Memory retrieval as Entity creation;
- confuse a source with the technical Entity described by that source;
- create duplicate Entities merely because provenance differs;
- use Source Authority as a substitute for identity resolution;
- encode canonical Relationships through arbitrary compound Entity names when proper Relationship semantics exist;
- redefine Relationship semantics inside Entity Architecture;
- create Entities without checking whether the concept is already represented;
- force reuse when concepts are materially different;
- invent identity when resolution is uncertain;
- silently promote candidate Entities to canonical status;
- create implicit Entity lifecycle enums through prose;
- unnecessarily change canonical IDs when aliases or properties change;
- merge Entities without dependency reconciliation;
- split Entities without preserving historical lineage;
- delete historically important Entities merely because they are obsolete;
- collapse superseding and superseded Entities automatically;
- hide meaningful Relationships in free-text properties;
- create competing ad hoc fields for canonical Relationship semantics;
- use free text as a substitute for structured identity where canonical structure is required;
- create an Entity for every incidental phrase, value, observation, or model suggestion;
- refuse to create Entities where independent identity materially improves reasoning;
- confuse canonical concepts with specific physical instances;
- convert every physical instance into a universal technical concept;
- flatten canonical taxonomy distinctions into display names;
- derive permanent identity solely from hierarchy position;
- replace Entity IDs merely because taxonomy improves;
- rebuild Entity architecture for every new domain;
- create universal Entity types for every product-specific concept;
- hardcode telecommunications as the limit of the universal Entity architecture;
- treat all claims concerning one Entity as having identical provenance;
- treat all claims concerning one Entity as having identical Source Authority;
- create duplicate Entities merely to separate contradictory claims;
- ignore the possibility that contradiction reveals mistaken Entity resolution;
- resolve identity using string similarity alone;
- ignore Context during ambiguous identity resolution;
- ignore provenance where it materially clarifies identity;
- fabricate Entity-resolution explanations after the fact;
- manipulate identity to support a preferred diagnosis;
- modify material Entity identity without considering downstream dependencies;
- store canonical Entity identity only in temporary conversational context;
- make canonical identity dependent upon one language model;
- bind canonical identity permanently to repository paths;
- freeze early Entity taxonomy assumptions permanently;
- allow prose documentation to become a competing machine-readable Entity schema;
- silently introduce unregistered Entity types through application code or model output;
- allow current reasoning importance to redefine permanent Entity identity;
- allow Routing to redefine Entity identity;
- allow Decision to redefine Entity identity;
- allow Learning frequency to redefine identity;
- force users to speak canonical ontology terminology;
- or silently map ambiguous user terminology to whichever Entity best supports the desired answer.

---

## 104. Final Principle

A.R.I.A.'s Entity Architecture gives durable identity to the things she understands.

An Entity is not merely a word.

It is not merely a database row.

It is not a sentence from a manual.

It is not a current observation.

It is not a hypothesis.

It is not a probability.

It is not an Action.

And it is not a fragment of temporary language-model memory.

A canonical Entity should exist because preserving independent identity improves A.R.I.A.'s ability to connect Knowledge across sources, Cases, products, domains, time, and reasoning processes.

The architecture should aggressively avoid meaningless duplication while equally refusing to collapse concepts that are technically different.

Aliases should change without breaking identity.

Taxonomies should improve without destroying history.

New manufacturers and domains should extend the system without requiring its foundations to be rebuilt.

Historical experience should connect to canonical Entities through Learning and persistent Case history rather than through a competing Experience ontology.

Exact machine structure should remain governed by explicit schemas and registries so prose does not become a second drifting implementation contract.

The language model may help A.R.I.A. recognize and resolve Entities, but it shall not own them.

And as A.R.I.A.'s Knowledge expands, the same stable canonical identities should allow what she learns today to remain connected, interpretable, correctable, and useful years later — without requiring the cognitive architecture to be rebuilt every time her understanding evolves.
