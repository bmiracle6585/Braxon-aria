# A.R.I.A. Canonical Knowledge Graph Doctrine

**Document Type:** Cognitive Knowledge System Specification  
**Authority:** Subordinate to `Core/Persona/ARIA_CONSTITUTION.md`  
**Version:** 2.0.0

---

## 1. Purpose

This document defines the architectural role and governing principles of A.R.I.A.'s Canonical Knowledge Graph.

The Knowledge Graph represents durable structured understanding as interconnected:

- Entities;
- Relationships;
- contextual applicability;
- provenance;
- source lineage;
- revision history;
- governance state;
- and other canonical Knowledge metadata defined by the authoritative architecture.

Its purpose is to allow A.R.I.A. to reason across interconnected Knowledge rather than relying exclusively upon:

- isolated documents;
- filesystem organization;
- keyword retrieval;
- language-model memory;
- conversational context;
- or duplicated domain-specific knowledge silos.

The Knowledge Graph shall remain durable independently of the language model used to reason over it.

---

## 2. Authority Boundaries

The Knowledge Graph operates with, but does not replace, the authoritative architecture defined by:

- `Core/Knowledge/entity_schema.md`;
- `Core/Knowledge/relationship_schema.md`;
- `Core/Knowledge/provenance_schema.md`;
- `Core/Knowledge/source_authority.md`;
- `Core/Reasoning/context_engine.json`;
- `Core/Reasoning/evidence_engine.json`;
- `Core/Reasoning/hypothesis_engine.json`;
- `Core/Reasoning/probability_engine.json`;
- `Core/Reasoning/uncertainty_engine.json`;
- `Core/Reasoning/decision_engine.json`;
- `Core/Reasoning/routing_engine.json`;
- `Core/Reasoning/learning_engine.json`;
- `Core/Reasoning/memory_engine.json`;
- `Core/Reasoning/validating_engine.json`;
- `Core/Reasoning/orchestration_engine.json`;
- applicable canonical schemas and registries;
- and `Core/Persona/ARIA_CONSTITUTION.md`.

This document shall not create competing:

- Entity classes;
- Entity schemas;
- Relationship types;
- Relationship schemas;
- Context vocabularies;
- Evidence structures;
- hypothesis states;
- probability systems;
- uncertainty systems;
- confidence scales;
- Validation states;
- Learning structures;
- Memory structures;
- source-authority classifications;
- provenance structures;
- or reasoning-engine contracts.

Where a more specific authoritative contract governs a structure or behavior, that contract controls.

---

## 3. Fundamental Principle

A.R.I.A.'s Knowledge is not merely a collection of facts.

Knowledge is a structured network of concepts and relationships that preserves:

> **what is known, what it relates to, where it came from, when and where it applies, and what authority legitimately supports it.**

The Knowledge Graph provides durable structure.

Reasoning engines determine how that structure should influence the current Case.

---

## 4. One Shared Canonical Knowledge Graph

A.R.I.A. shall maintain one logically shared Canonical Knowledge Graph.

Canonical technical Knowledge shall not be independently duplicated for every user, participant, Case, customer, manufacturer, or application.

Conceptually:

**SHARED CANONICAL KNOWLEDGE**

may be referenced by:

- Cases;
- participants;
- historical observations;
- learned experience;
- applications;
- projects;
- customers;
- organizations;
- and future reasoning systems.

Technical Knowledge remains shared unless its actual applicability is Context-specific.

---

## 5. Shared Knowledge Does Not Mean Universal Applicability

A shared graph does not mean every Knowledge object applies everywhere.

Knowledge may be constrained by:

- product;
- manufacturer;
- hardware revision;
- software version;
- firmware version;
- configuration;
- topology;
- jurisdiction;
- environment;
- organization;
- customer;
- date;
- or another canonical Context dimension.

The graph is shared.

Applicability remains contextual.

Context Engine owns canonical Context semantics.

---

## 6. Knowledge Is Not a Directory

Filesystem organization may support:

- source storage;
- repository maintenance;
- human navigation;
- development;
- and document management.

Filesystem location shall not define Knowledge meaning.

A concept should not need to exist in only one directory merely because humans traditionally organize information hierarchically.

A single canonical concept may participate in many technical contexts simultaneously.

---

## 7. Canonical Concepts Should Be Reusable

Where two references describe the same underlying concept, A.R.I.A. should prefer one canonical Entity with appropriate:

- aliases;
- Relationships;
- Context;
- provenance;
- and source-specific terminology

rather than unnecessary duplicate Entities.

Manufacturer-specific naming does not automatically require manufacturer-specific duplication of a universal technical concept.

Entity Schema owns canonical Entity identity and alias behavior.

---

## 8. Entity Schema Owns Entities

`Core/Knowledge/entity_schema.md` is the authoritative specification governing canonical Entities.

This Knowledge Graph doctrine shall not independently define:

- Entity classes;
- Entity IDs;
- Entity lifecycle;
- alias structures;
- Entity properties;
- Entity identity rules;
- or Entity validation rules.

The Knowledge Graph stores and connects canonical Entities according to that authority.

Any Entity examples in this doctrine are illustrative only.

---

## 9. Stable Entity Identity Is Required

Canonical Knowledge must not depend upon display names alone.

Entity identity should survive changes to:

- terminology;
- aliases;
- filenames;
- repository paths;
- manufacturer naming;
- UI labels;
- model terminology;
- abbreviations;
- or application presentation.

Stable identity allows Relationships, provenance, history, and downstream reasoning to remain attached to the same concept over time.

Entity Schema owns the implementation contract.

---

## 10. Aliases Do Not Automatically Create New Knowledge

Different terms may refer to the same Entity.

For example, a technical concept may have:

- full terminology;
- abbreviations;
- manufacturer terminology;
- historical terminology;
- informal terminology;
- or user shorthand.

A.R.I.A. should resolve these to the canonical Entity where technically appropriate.

She shall not create duplicate Knowledge merely because vocabulary differs.

---

## 11. Distinct Concepts Must Remain Distinct

Canonical reuse shall not collapse materially different concepts into one Entity merely because their names are similar.

Entity resolution must preserve genuine technical distinctions.

Examples may include differences in:

- product revision;
- measurement meaning;
- logical versus physical interface;
- procedure versus Action;
- symptom versus cause;
- or another technically meaningful distinction.

Canonicalization shall reduce duplication without destroying meaning.

---

## 12. Relationship Schema Owns Relationships

`Core/Knowledge/relationship_schema.md` is the authoritative specification governing Relationships.

This doctrine shall not independently define:

- canonical Relationship types;
- directionality;
- inverse behavior;
- Relationship identity;
- Relationship lifecycle;
- Relationship properties;
- causal semantics;
- deterministic semantics;
- or Relationship validation.

The Knowledge Graph stores and traverses Relationships according to that authority.

Any Relationship examples in this doctrine are illustrative only.

---

## 13. Relationships Are First-Class Knowledge

A.R.I.A.'s intelligence depends not merely upon Entities but upon how Entities relate.

A Relationship may represent, according to the authoritative Relationship Schema:

- structural association;
- hierarchy;
- dependency;
- compatibility;
- incompatibility;
- causality;
- applicability;
- measurement;
- configuration;
- requirement;
- sequence;
- correction;
- support;
- contradiction;
- or another canonical semantic.

Relationships must remain machine-interpretable enough to support reasoning.

---

## 14. Relationship Meaning Must Be Explicit

A.R.I.A. should prefer precise canonical Relationships over vague association when the authoritative Relationship Schema supports the distinction.

A generic association should not replace a known:

- dependency;
- requirement;
- causal relationship;
- structural relationship;
- compatibility relationship;
- or other meaningful semantic.

Precise Relationships improve:

- retrieval;
- graph traversal;
- reasoning;
- explanation;
- and downstream validation.

---

## 15. Relationships May Be Contextual

A Relationship may be valid only under particular Context.

For example, a technical relationship may depend upon:

- hardware revision;
- software;
- firmware;
- configuration;
- topology;
- operating mode;
- environment;
- date;
- jurisdiction;
- or another canonical Context dimension.

A.R.I.A. shall not generalize a contextual Relationship beyond its supported applicability.

Context Engine owns canonical Context representation.

---

## 16. Relationships May Change Over Time

Technical Relationships are not necessarily timeless.

A Relationship may become:

- newly applicable;
- restricted;
- superseded;
- deprecated;
- corrected;
- disputed;
- or no longer applicable

because the underlying technical world changed.

The graph shall support historical continuity rather than assuming every Relationship is eternally static.

---

## 17. Knowledge Is More Than Entities and Relationships

The Knowledge Graph may need to preserve or reference additional information such as:

- provenance;
- source authority;
- Context;
- revision;
- effective dates;
- lifecycle information;
- governance information;
- contradiction state;
- dependencies;
- and other metadata defined by authoritative schemas.

This doctrine does not define competing field structures for those concepts.

---

## 18. Provenance Is Required for Material Knowledge

Material Knowledge should preserve sufficient provenance to determine how it became known.

Provenance may establish whether Knowledge originated from:

- authoritative documentation;
- structured systems;
- human authorship;
- extraction;
- normalization;
- inference;
- qualified Learning;
- historical material;
- or another authorized source.

`provenance_schema.md` owns provenance semantics.

The Knowledge Graph preserves or references provenance.

---

## 19. Source Authority Remains Separate

The Knowledge Graph may contain Knowledge from sources possessing different authority.

The graph shall not assume:

> stored = authoritative.

`source_authority.md` determines the principles by which source authority is evaluated.

The graph preserves the Knowledge and source relationships necessary for that evaluation.

---

## 20. Knowledge Graph Is Not Truth by Storage

Persistence inside the Knowledge Graph does not automatically establish universal truth.

Stored Knowledge may be:

- canonical;
- provisional;
- disputed;
- historical;
- superseded;
- deprecated;
- inferred;
- learned;
- imported;
- incomplete;
- or otherwise governed according to authoritative architecture.

A.R.I.A. shall not reason:

> "It is in the graph, therefore it must be true now."

---

## 21. Knowledge Governance Must Be Explicit

If canonical Knowledge lifecycle or governance states are required, they shall be defined by an explicit authoritative schema or registry.

This doctrine shall not independently establish universal enums such as:

- `PROPOSED`;
- `SUPPORTED`;
- `VALIDATED`;
- `DEPRECATED`;
- `SUPERSEDED`;
- `REJECTED`;

unless those values are explicitly canonical elsewhere.

Conceptual lifecycle language may be used descriptively without becoming an implicit registry.

---

## 22. Candidate Knowledge Must Remain Distinguishable

A.R.I.A. may generate or ingest potential Knowledge that has not yet earned canonical authority.

Candidate Knowledge may arise from:

- language-model extraction;
- inferred Relationships;
- human suggestion;
- imported legacy data;
- historical Learning;
- source conflict;
- or another authorized process.

Candidate Knowledge shall not silently become canonical merely because it is persisted.

Knowledge governance owns promotion.

---

## 23. Canonical Knowledge Must Remain Distinguishable

Canonical Knowledge represents Knowledge accepted for use according to the authoritative governance architecture.

Canonical status does not mean:

- universally applicable;
- permanently correct;
- impossible to supersede;
- immune to contradiction;
- or guaranteed by storage.

Canonical Knowledge remains subject to:

- Context;
- provenance;
- source authority;
- revision;
- correction;
- and current Evidence.

---

## 24. Knowledge and Evidence Are Distinct

The Knowledge Graph describes durable understanding.

Evidence describes information relevant to the current Case or proposition.

For example:

Canonical Knowledge may establish:

> A particular condition can cause a particular symptom.

Current Evidence may establish:

> The condition is or is not present in this Case.

The graph defines technical possibility or established relationships.

Evidence Engine owns current Evidence.

---

## 25. Knowledge and Hypotheses Are Distinct

The existence of a causal Relationship in the Knowledge Graph does not automatically create a current hypothesis.

Hypothesis Engine owns current hypothesis state.

The graph may help identify technically plausible candidates.

The current Case determines whether those candidates should become active hypotheses.

---

## 26. Knowledge and Probability Are Distinct

The Knowledge Graph shall not own current diagnostic Probability.

For example:

Canonical Knowledge may establish:

> Condition A can cause Symptom B.

Historical qualified Learning may establish:

> Condition A occurred frequently in comparable cases.

Current Evidence may establish:

> Several observations support Condition A now.

Probability Engine determines current belief.

The canonical Relationship itself need not change merely because current Probability changes.

---

## 27. Knowledge and Uncertainty Are Distinct

The Knowledge Graph may contain incomplete, disputed, or context-limited Knowledge.

Uncertainty Engine owns formal current uncertainty.

A.R.I.A. shall not create a competing graph-level uncertainty scale merely because Knowledge can be incomplete.

The graph should preserve the facts necessary for Uncertainty to reason correctly.

---

## 28. Knowledge and Validation Are Distinct

Knowledge may define:

> what should happen;

> what is supported;

> what is required;

or

> what technical relationship exists.

Validation determines what current results demonstrate.

Validation Engine owns current Validation semantics.

The Knowledge Graph shall not independently validate a Case merely because the expected behavior is known.

---

## 29. Knowledge and Decision Are Distinct

The Knowledge Graph may establish:

- dependencies;
- constraints;
- compatibility;
- procedures;
- expected outcomes;
- or other information relevant to choosing an Action.

Decision Engine owns current Action selection.

Knowledge informs Decision.

Knowledge does not independently decide.

---

## 30. Knowledge and Routing Are Distinct

The Knowledge Graph may inform route construction by identifying:

- dependencies;
- plausible causes;
- available tests;
- prerequisites;
- incompatibilities;
- and other technical structure.

Routing Engine owns diagnostic or operational route progression.

The graph shall not independently maintain a competing route state machine.

---

## 31. Knowledge and Learning Are Distinct

Learning Engine determines what qualified historical experience can be generalized.

The Knowledge Graph may receive or reference qualified learned Knowledge according to the authoritative governance architecture.

The graph shall preserve that the origin was empirical.

Repeated experience shall not automatically rewrite canonical technical truth.

---

## 32. There Is No Independent Experience Ledger Authority

Earlier A.R.I.A. architecture referred to a separate **Experience Ledger** as though it were an independent cognitive authority.

That model is obsolete.

Qualified Experience now emerges through the coordinated canonical architecture involving, as applicable:

- Case State;
- Evidence;
- Context;
- Actions;
- Observations;
- Validation;
- Learning;
- and persistent historical records.

The Knowledge Graph may reference qualified empirical Knowledge or historical Case material.

It shall not depend upon a competing Experience Ledger authority.

---

## 33. Knowledge and Memory Are Distinct

The Knowledge Graph stores durable structured Knowledge.

Memory determines what prior information should be retrieved into current reasoning.

Memory may retrieve:

- Entities;
- Relationships;
- source information;
- Context;
- historical Cases;
- learned experience;
- or other relevant material.

Retrieval does not alter canonical Knowledge merely because an item was remembered.

---

## 34. Knowledge and Context Are Distinct

The Knowledge Graph may preserve Contextual applicability.

Context Engine owns current Context interpretation and canonical Context semantics.

The graph shall not invent parallel Context dimensions.

Knowledge says:

> This relationship applies under Context X.

Context Engine helps determine:

> Is Context X present now?

---

## 35. Knowledge and Orchestration Are Distinct

Knowledge operations may require coordinated processes such as:

- ingestion;
- extraction;
- normalization;
- Entity resolution;
- Relationship resolution;
- provenance linkage;
- review;
- promotion;
- supersession;
- reprocessing;
- dependency review;
- or correction propagation.

Orchestration Engine coordinates operations according to authoritative contracts.

The Knowledge Graph shall not independently become a workflow engine.

---

## 36. Canonical Knowledge and Experience Must Cooperate

A.R.I.A. should be able to combine:

**Canonical Knowledge**

with

**Qualified Experience**

without confusing them.

For example:

Canonical Knowledge may establish that several causes are technically possible.

Qualified historical experience may indicate that one cause has been common under comparable Context.

Current Evidence may support or contradict that cause.

Probability Engine may then adjust current belief.

Each system retains its role.

---

## 37. Historical Experience Must Not Rewrite Deterministic Knowledge Automatically

Repeated historical outcomes can be extremely useful.

They do not automatically redefine deterministic technical facts.

If qualified experience repeatedly contradicts canonical Knowledge, A.R.I.A. may have discovered:

- an undocumented condition;
- incomplete canonical Knowledge;
- an implementation defect;
- a revision difference;
- an incorrect source;
- or a genuine Knowledge gap.

The appropriate response is investigation and Knowledge governance.

Not silent rewriting.

---

## 38. Manufacturer Knowledge Should Connect to Shared Concepts

Manufacturer-specific Knowledge should normally be represented through canonical Entities, Relationships, provenance, and Context rather than isolated duplicate universes.

A shared technical concept may participate in:

- multiple manufacturers;
- multiple product families;
- multiple products;
- multiple procedures;
- and multiple Cases.

Manufacturer-specific behavior should be represented as contextual Knowledge where technically appropriate.

---

## 39. Product Expansion Should Not Require Architectural Redesign

Adding a new:

- manufacturer;
- product;
- product family;
- hardware revision;
- software version;
- technology;
- procedure;
- measurement;
- or technical domain

should primarily require new canonical Knowledge objects and Relationships.

It should not require redesigning the fundamental Knowledge architecture.

The graph shall be extensible.

---

## 40. Domain Expansion Should Reuse Existing Knowledge

When A.R.I.A. expands into a new domain, existing universal concepts should be reused where technically appropriate.

The system should avoid creating unnecessary duplicate concepts merely because the domain changed.

At the same time, genuinely different domain concepts shall remain distinct.

Extensibility requires both reuse and precision.

---

## 41. Vertical Relationships Matter

The graph should support hierarchical traversal where canonical Relationships define hierarchy.

Conceptually:

**organization → family → product → variant → component**

or another applicable structure.

The exact Relationship semantics belong to `relationship_schema.md`.

Hierarchical traversal may help establish technical scope.

---

## 42. Horizontal Relationships Matter

A.R.I.A. must also traverse across technical dimensions.

A symptom may connect to:

- conditions;
- measurements;
- configurations;
- components;
- failure mechanisms;
- procedures;
- tests;
- and other relevant concepts.

Knowledge intelligence depends upon cross-domain connectivity rather than hierarchy alone.

---

## 43. Multi-Hop Traversal Is Required

A.R.I.A. should be capable of traversing multiple Relationships to discover technically meaningful paths.

Conceptually:

**SYMPTOM → CONDITION → COMPONENT → INTERFACE → CONFIGURATION → TEST**

or:

**PRODUCT → COMPONENT → REQUIREMENT → MEASUREMENT → PROCEDURE**

The exact path depends upon canonical Relationship semantics and current Context.

Multi-hop traversal enables reasoning beyond keyword matching.

---

## 44. Multi-Hop Traversal Is Not Proof

A path through the Knowledge Graph does not automatically prove a current conclusion.

A path may establish:

- possibility;
- dependency;
- technical association;
- or a candidate reasoning route.

Current Evidence, Probability, Context, Validation, and other reasoning systems determine what the path means in the current Case.

Graph connectivity shall not be mistaken for diagnosis.

---

## 45. Traversal Must Respect Relationship Semantics

A.R.I.A. shall not treat every graph edge as interchangeable.

For example, a:

- causal Relationship;
- structural Relationship;
- compatibility Relationship;
- requirement Relationship;
- and contextual Relationship

may have very different implications.

Graph traversal must preserve the meaning defined by the Relationship Schema.

---

## 46. Traversal Must Respect Directionality

Where canonical Relationships are directional, graph reasoning must respect that directionality.

A.R.I.A. shall not assume that:

> A causes B

means:

> B causes A.

Likewise:

> A requires B

does not imply:

> B requires A.

Relationship Schema owns directionality and inverse semantics.

---

## 47. Traversal Must Respect Context

A technically valid path under one Context may be invalid under another.

Graph traversal should filter or qualify Relationships according to applicable Context.

A.R.I.A. shall not traverse through revision-specific or configuration-specific Knowledge as though it were universally applicable.

---

## 48. Traversal Must Respect Historical State

Historical Knowledge may remain in the graph.

Current traversal should not silently treat superseded historical Relationships as current unless the current Context calls for them.

Historical Cases may intentionally require historical Knowledge.

Current Cases normally require currently applicable Knowledge.

---

## 49. Contradictory Knowledge Must Be Preserved

A.R.I.A. shall permit contradictory Knowledge to exist when the contradiction has not been legitimately resolved.

She shall not silently erase one claim merely to simplify the graph.

Contradiction may reveal:

- source conflict;
- revision differences;
- Context differences;
- implementation differences;
- source error;
- incomplete Knowledge;
- or another unresolved distinction.

The contradiction itself is meaningful Knowledge state.

---

## 50. Contradiction Is Not Automatically Error

Two apparently contradictory claims may both be valid under different Context.

Before treating Knowledge as erroneous, A.R.I.A. should investigate:

- revision;
- product;
- configuration;
- topology;
- jurisdiction;
- date;
- operating mode;
- source scope;
- or another contextual distinction.

Context may resolve apparent contradiction.

---

## 51. Unresolved Contradiction Must Remain Visible

If contradictory Knowledge cannot yet be reconciled, A.R.I.A. shall preserve the unresolved state.

She shall not invent consensus.

Reasoning may proceed with explicit uncertainty where permitted.

The system should retain enough provenance and Context to revisit the conflict later.

---

## 52. Revision Awareness Is Required

Technical Knowledge may change across revisions.

The graph should preserve enough structure to distinguish Knowledge applicable to:

- different hardware;
- different firmware;
- different software;
- different document revisions;
- different standards;
- different dates;
- or another relevant version dimension.

Revision awareness prevents inappropriate generalization.

---

## 53. Superseded Knowledge May Remain Valuable

Superseded Knowledge should not necessarily be deleted.

It may remain necessary to understand:

- legacy systems;
- historical Cases;
- old configurations;
- previous procedures;
- prior decisions;
- or why an earlier conclusion was reasonable.

Current reasoning must distinguish superseded Knowledge from governing current Knowledge.

---

## 54. Correction Must Preserve History

When canonical Knowledge is corrected, A.R.I.A. should preserve sufficient lineage to understand:

- what the prior Knowledge was;
- why it changed;
- what source caused the correction;
- what replaced it;
- and what downstream Knowledge may depend upon it.

Provenance and Knowledge governance own the detailed lineage.

---

## 55. Dependency Tracing Is Important

Knowledge objects may depend upon other Knowledge.

When upstream Knowledge changes, A.R.I.A. should be capable of identifying downstream Knowledge potentially affected.

Conceptually:

**SOURCE → CLAIM → RELATIONSHIP → DERIVED KNOWLEDGE → ROUTING CONSEQUENCE**

If the source or claim is invalidated, dependent structures may require review.

The graph should support such dependency analysis where authoritative schemas permit it.

---

## 56. Knowledge Corrections May Require Reprocessing

When:

- provenance changes;
- source authority changes;
- a source is corrected;
- Entity resolution changes;
- Relationship semantics change;
- Context modeling improves;
- or a source is superseded,

affected Knowledge may require reprocessing.

The graph should preserve enough lineage to make reprocessing possible.

---

## 57. Source Documents Remain Important

The Knowledge Graph does not eliminate the need for original source material.

Documents may contain:

- tables;
- diagrams;
- warnings;
- exceptions;
- Context;
- formatting;
- revision history;
- and detailed explanation

that cannot be fully represented by isolated graph objects.

The graph should preserve or reference provenance sufficient to return to source material when authorized and necessary.

---

## 58. Documents Are Not the Knowledge Graph

Original documents and structured Knowledge serve different purposes.

Conceptually:

**SOURCE MATERIAL**

may support

**CLAIMS / KNOWLEDGE**

which may produce or support

**ENTITIES + RELATIONSHIPS + CONTEXT + PROVENANCE**

The document remains a source.

The graph becomes structured understanding.

Neither replaces the other.

---

## 59. Source Extraction Must Preserve Transformation

When A.R.I.A. extracts Knowledge from documents, she shall preserve the distinction between:

- what the source explicitly stated;
- what was extracted;
- what was normalized;
- what was inferred;
- and what became canonical.

`provenance_schema.md` governs that lineage.

The graph shall not make derived Knowledge appear verbatim from the source.

---

## 60. Human Review May Govern Knowledge Ingestion

A.R.I.A.'s architecture shall support human governance where required.

A conceptual ingestion path may include:

**SOURCE → EXTRACTION → CANDIDATE KNOWLEDGE → REVIEW → GOVERNED KNOWLEDGE**

This is conceptual only.

It does not define a mandatory workflow or lifecycle enum.

Orchestration and Knowledge governance own implementation.

---

## 61. Autonomous Ingestion Must Be Earned, Not Assumed

The architecture may eventually permit greater autonomous ingestion where reliability and governance justify it.

A language model shall not automatically possess authority to convert every extracted or inferred statement into canonical Knowledge.

Autonomy shall remain bounded by authoritative policy.

---

## 62. Model-Proposed Knowledge Is Not Automatically Canonical

The language model may propose:

- Entities;
- aliases;
- Relationships;
- candidate facts;
- interpretations;
- inferred applicability;
- or Knowledge corrections.

These proposals may be useful.

They remain proposals until qualified through the authoritative Knowledge architecture.

Fluent generation does not create canonical truth.

---

## 63. The Language Model Is Not the Knowledge Graph

The installed language model may assist with:

- natural-language interpretation;
- Entity recognition;
- alias resolution;
- Relationship extraction;
- candidate generation;
- source interpretation;
- semantic retrieval;
- synthesis;
- reasoning;
- and explanation.

The language model shall not be the authoritative storage location for canonical Knowledge.

Model weights are not A.R.I.A.'s canonical Knowledge Graph.

---

## 64. Model Familiarity Is Not Canonical Knowledge

A language model may know or recognize technical concepts from pretraining.

That familiarity may assist reasoning according to system policy.

It shall not automatically become canonical A.R.I.A. Knowledge with fabricated:

- provenance;
- source authority;
- revision;
- Context;
- or governance.

Canonical Knowledge requires canonical lineage.

---

## 65. Model Replacement Must Not Destroy Knowledge

A.R.I.A.'s Knowledge shall survive replacement of the underlying language model.

Changing:

- model provider;
- model version;
- inference architecture;
- prompt architecture;
- or reasoning implementation

shall not erase the canonical Knowledge Graph.

This separation is fundamental to A.R.I.A.'s identity as a persistent system.

---

## 66. Conversation Length Must Not Destroy Knowledge

Canonical Knowledge shall not depend upon remaining inside the current model context window.

A.R.I.A. shall not forget technical Knowledge merely because:

- the conversation becomes long;
- a session ends;
- context is summarized;
- or another model instance handles the next request.

Persistent architecture owns Knowledge.

---

## 67. Repository Reorganization Must Not Redefine Knowledge

Moving:

- files;
- directories;
- source documents;
- modules;
- or repositories

shall not inherently redefine canonical Entity or Relationship identity.

Knowledge identity must remain sufficiently independent of storage location.

---

## 68. Knowledge Retrieval Is Not Knowledge Creation

Finding a document or graph object does not create new canonical Knowledge.

Retrieval makes existing information available to reasoning.

A.R.I.A. shall not confuse:

> retrieved

with:

> validated

or:

> canonical.

Memory and retrieval systems shall preserve that distinction.

---

## 69. Missing Knowledge Is a Valid State

Failure to find a Relationship in the graph does not prove that the Relationship is impossible.

The graph may be incomplete.

A.R.I.A. should support explicit Knowledge gaps.

A Knowledge gap may trigger, according to authoritative architecture:

- broader retrieval;
- source review;
- expert consultation;
- candidate generation;
- investigation;
- or future Learning.

Unknown shall remain valid.

---

## 70. Absence Is Not Negation

A.R.I.A. shall not reason:

> "The graph does not contain A → B, therefore A cannot relate to B."

unless the authoritative Knowledge explicitly establishes that impossibility.

Missing Knowledge and negative Knowledge are different.

This distinction is critical for an evolving system.

---

## 71. Negative Knowledge May Be Valuable

Where authoritative sources establish that something:

- is unsupported;
- is incompatible;
- cannot occur;
- is prohibited;
- does not apply;
- or is impossible under defined conditions,

that negative Knowledge may be represented according to canonical Entity and Relationship semantics.

Negative Knowledge requires the same attention to:

- provenance;
- Context;
- revision;
- and source authority

as positive Knowledge.

---

## 72. Knowledge Gaps Should Be Learnable

A.R.I.A. should be capable of recognizing recurring areas where canonical Knowledge is insufficient.

A repeated Knowledge gap may justify:

- source acquisition;
- structured research;
- human review;
- new Entity creation;
- new Relationship creation;
- or qualified Learning.

The gap itself should not be filled with hallucination.

---

## 73. Avoid Graph Explosion

Not every:

- word;
- sentence;
- paragraph;
- conversational statement;
- incidental association;
- or transient observation

should become permanent canonical graph structure.

Knowledge ingestion should balance:

- reasoning usefulness;
- retrieval value;
- semantic precision;
- maintainability;
- provenance;
- scalability;
- computational cost;
- and future extensibility.

The goal is not the largest possible graph.

The goal is the most useful durable representation of Knowledge.

---

## 74. Avoid Over-Normalization

Graph normalization should not destroy information merely to reduce object count.

If two concepts differ materially, they should remain distinct even when they are closely related.

A.R.I.A. shall not collapse:

- variants;
- revisions;
- states;
- measurements;
- procedures;
- or Relationships

when doing so would damage reasoning precision.

---

## 75. Avoid Under-Normalization

The opposite problem is also harmful.

A.R.I.A. shall avoid creating separate disconnected Entities for every:

- manufacturer synonym;
- spelling variation;
- capitalization difference;
- abbreviation;
- source wording;
- or conversational phrase

when they refer to the same canonical concept.

Entity Schema governs canonical resolution.

---

## 76. Graph Traversal Should Be Purposeful

A.R.I.A. shall not traverse the graph without regard to the reasoning objective.

Traversal may be constrained by:

- current Case;
- active hypotheses;
- Context;
- desired information;
- routing objective;
- current Evidence;
- uncertainty;
- or another authoritative reasoning state.

The graph provides possibilities.

Reasoning determines which possibilities matter now.

---

## 77. Graph Size Must Not Become Reasoning Noise

As the graph expands, indiscriminate traversal could produce enormous irrelevant candidate sets.

A.R.I.A. should use:

- Context;
- Relationship semantics;
- source applicability;
- active reasoning state;
- and other authoritative constraints

to focus traversal.

More Knowledge is useful only if relevant Knowledge can be selected.

---

## 78. Retrieval Ranking Does Not Determine Truth

Search or graph retrieval systems may rank certain Knowledge highly.

High retrieval rank means:

> likely relevant to the query.

It does not automatically mean:

> most authoritative;

> most current;

> most applicable;

or

> true.

Source Authority, Context, provenance, and reasoning remain necessary.

---

## 79. Knowledge Graph Must Support Explanation

Where materially relevant, A.R.I.A. should be capable of explaining:

- what Entities are involved;
- what Relationships connect them;
- what source supports those Relationships;
- what Context applies;
- whether the Knowledge is current;
- whether it is inferred or documented;
- whether contradictory Knowledge exists;
- and how the Knowledge influenced current reasoning.

Explanation shall reflect actual graph state.

---

## 80. Explanation Should Not Expose Internal Complexity Unnecessarily

A.R.I.A. does not need to narrate every graph traversal to the user.

The graph may perform complex internal retrieval while A.R.I.A. communicates simply:

> "That port supports gigabit, but your current link is negotiating at 10 Mbps. That points us toward the physical connection or negotiation path rather than a basic capability limitation."

Detailed graph explanation should be available when useful, not forced into every interaction.

---

## 81. Knowledge Graph Must Support Auditability

Authorized review should be capable of determining, where applicable:

- what Knowledge existed;
- when it existed;
- where it came from;
- what it related to;
- what Context governed it;
- whether it changed;
- what superseded it;
- and what downstream Knowledge depended upon it.

Auditability supports both technical reliability and future system evolution.

---

## 82. Knowledge Graph Must Support Reproducibility

Where practical, A.R.I.A. should preserve enough structure to reproduce why a material Knowledge Relationship exists.

This may require access to:

- source lineage;
- transformation history;
- Entity resolution;
- Relationship derivation;
- Context;
- and governance history.

Provenance owns the detailed lineage.

The graph must preserve its connections.

---

## 83. Knowledge Graph Must Support Evolution

A.R.I.A.'s technical understanding will change.

The architecture must allow:

- new Knowledge;
- corrected Knowledge;
- superseded Knowledge;
- new Relationships;
- new Entities;
- new domains;
- improved Context;
- improved provenance;
- improved source authority;
- and improved reasoning systems

without requiring wholesale replacement of the Knowledge Graph architecture.

The architecture should evolve through extension and reconciliation rather than repeated reinvention.

---

## 84. Knowledge Graph Must Not Freeze Early Assumptions

Early A.R.I.A. development may contain incomplete assumptions.

The graph architecture shall not hardcode those assumptions so deeply that later correction becomes impossible.

Examples include premature:

- Entity taxonomies;
- Relationship taxonomies;
- source classes;
- lifecycle states;
- confidence scales;
- domain structures;
- or workflow assumptions.

Canonical registries and schemas may evolve deliberately.

Doctrine shall remain structurally durable.

---

## 85. Universal Knowledge Architecture Must Remain Domain-Independent

The universal Knowledge Graph doctrine shall not hardcode:

- microwave-specific Entity classes;
- RF-specific Relationship types;
- networking-specific graph rules;
- specific manufacturers;
- specific products;
- specific customers;
- specific organizations;
- or named individuals

into the universal cognitive architecture.

Microwave Backhaul may be A.R.I.A.'s first deep technical domain.

It shall not define the limits of the architecture.

---

## 86. Domain Knowledge Belongs in the Graph, Not the Doctrine

Domain-specific information belongs in canonical Knowledge objects.

For example, telecommunications Knowledge may define:

- products;
- components;
- measurements;
- procedures;
- configurations;
- failure mechanisms;
- technical Relationships;
- and applicable Context.

The universal doctrine defines how Knowledge behaves.

It does not itself become the telecommunications database.

---

## 87. Application Knowledge Must Remain Distinguishable

A.R.I.A. may know information specific to:

- an organization;
- customer;
- project;
- application;
- workflow;
- or operational system.

Such Knowledge may exist within the broader graph where appropriate.

Its Context must prevent organizational or customer-specific Knowledge from being mistaken for universal technical truth.

---

## 88. Participant Knowledge Must Remain Distinguishable

A.R.I.A. may maintain Knowledge concerning:

- participant roles;
- competency;
- prior interactions;
- responsibilities;
- preferences;
- or history

according to applicable privacy and Memory architecture.

Participant-specific information shall not redefine shared technical Knowledge.

The graph may reference participants without creating separate technical universes for each participant.

---

## 89. Privacy Applies to Knowledge

The Knowledge Graph may contain sensitive information.

A.R.I.A. shall respect applicable:

- privacy;
- authorization;
- organizational;
- customer;
- security;
- and retention

boundaries.

Shared graph architecture does not mean unrestricted visibility.

Logical sharing and user authorization are separate concerns.

---

## 90. Security Applies to Knowledge

Knowledge may include:

- credentials-related information;
- network architecture;
- customer infrastructure;
- proprietary technical material;
- security-sensitive configuration;
- or restricted operational data.

The Knowledge Graph shall cooperate with applicable access-control architecture.

A.R.I.A.'s ability to know something does not automatically grant every participant permission to retrieve it.

---

## 91. Knowledge Should Remain Explainably Governed

A.R.I.A. should be capable of distinguishing:

- canonical Knowledge;
- candidate Knowledge;
- historical Knowledge;
- learned empirical Knowledge;
- source assertions;
- inferred Knowledge;
- current Evidence;
- and current conclusions.

These distinctions are essential to trustworthy reasoning.

The graph shall not collapse them into one undifferentiated pool of statements.

---

## 92. Core Knowledge Graph Invariants

The following principles shall remain true throughout A.R.I.A.'s architecture:

1. A.R.I.A. maintains one logically shared Canonical Knowledge Graph.
2. Shared Knowledge does not imply universal applicability.
3. Knowledge meaning is not defined by filesystem location.
4. Canonical concepts should be reused where technically appropriate.
5. Distinct concepts shall remain distinct.
6. Entity Schema owns canonical Entity semantics.
7. Relationship Schema owns canonical Relationship semantics.
8. Stable Entity identity is required.
9. Aliases do not automatically create duplicate Knowledge.
10. Relationships are first-class Knowledge.
11. Relationship meaning shall remain explicit.
12. Relationships may be contextual.
13. Relationships may change over time.
14. Knowledge may include metadata beyond Entities and Relationships.
15. Material Knowledge should preserve provenance.
16. Source Authority remains distinct from graph persistence.
17. Storage in the graph does not automatically establish truth.
18. Knowledge governance must be explicit.
19. Candidate Knowledge shall remain distinguishable from canonical Knowledge.
20. Canonical Knowledge remains subject to Context and revision.
21. Knowledge is distinct from Evidence.
22. Knowledge is distinct from hypotheses.
23. Knowledge is distinct from Probability.
24. Knowledge is distinct from formal Uncertainty.
25. Knowledge is distinct from Validation.
26. Knowledge informs Decision but does not own Action selection.
27. Knowledge informs Routing but does not own route state.
28. Knowledge is distinct from Learning.
29. There is no independent Experience Ledger authority.
30. Knowledge is distinct from Memory.
31. Context Engine owns canonical Context semantics.
32. Orchestration owns coordinated Knowledge operations.
33. Canonical Knowledge and qualified Experience may cooperate without becoming the same system.
34. Historical experience shall not silently rewrite deterministic technical Knowledge.
35. Manufacturer-specific Knowledge should connect to shared concepts where technically appropriate.
36. Product expansion should not require architectural redesign.
37. Domain expansion should reuse canonical concepts where appropriate.
38. The graph supports hierarchical and cross-domain traversal.
39. Multi-hop traversal is required.
40. Multi-hop traversal does not itself prove a current conclusion.
41. Traversal shall respect Relationship semantics.
42. Traversal shall respect directionality.
43. Traversal shall respect Context.
44. Traversal shall respect historical applicability.
45. Contradictory Knowledge may coexist.
46. Contradiction is not automatically error.
47. Unresolved contradiction shall remain visible.
48. Revision awareness is required.
49. Superseded Knowledge may remain historically valuable.
50. Correction should preserve history.
51. Dependency tracing should be possible where applicable.
52. Knowledge correction may require reprocessing.
53. Original source material remains important.
54. Documents and structured Knowledge are distinct.
55. Extraction transformations shall preserve provenance.
56. Human governance may apply to ingestion.
57. Autonomous ingestion shall not be assumed.
58. Model-proposed Knowledge is not automatically canonical.
59. The language model is not the Knowledge Graph.
60. Model familiarity is not canonical Knowledge.
61. Model replacement shall not destroy canonical Knowledge.
62. Conversation length shall not destroy canonical Knowledge.
63. Repository reorganization shall not redefine canonical Knowledge identity.
64. Retrieval is not Knowledge creation.
65. Missing Knowledge is a valid state.
66. Absence from the graph is not automatic negation.
67. Negative Knowledge may be represented when authoritative.
68. Knowledge gaps should be learnable.
69. Graph construction shall avoid unnecessary explosion.
70. Graph normalization shall avoid both over-normalization and under-normalization.
71. Graph traversal should be purposeful.
72. Graph scale shall not be allowed to create uncontrolled reasoning noise.
73. Retrieval ranking does not determine truth.
74. Knowledge influence shall remain explainable.
75. User-facing explanation should remain proportional.
76. The graph should support authorized auditability.
77. The graph should support reproducibility where practical.
78. The graph must support architectural evolution.
79. Early assumptions shall not be frozen into universal doctrine unnecessarily.
80. Universal Knowledge architecture shall remain technically domain-independent.
81. Domain Knowledge belongs in canonical graph content rather than universal doctrine.
82. Application-specific Knowledge must retain applicable Context.
83. Participant-specific Knowledge shall not redefine shared technical truth.
84. Privacy restrictions apply to Knowledge.
85. Security restrictions apply to Knowledge.
86. Canonical, candidate, historical, learned, inferred, evidentiary, and concluded information shall remain distinguishable.

---

## 93. Prohibited Cognitive Behaviors

A.R.I.A. shall not:

- create separate canonical technical graphs for every participant without architectural justification;
- assume shared Knowledge applies universally;
- define Knowledge meaning solely through filesystem paths;
- duplicate canonical concepts merely because terminology differs;
- collapse materially different concepts into one Entity;
- create competing Entity classes inside this doctrine;
- create competing Relationship types inside this doctrine;
- redefine Entity Schema authority;
- redefine Relationship Schema authority;
- treat vague association as equivalent to precise canonical Relationship semantics;
- generalize contextual Relationships beyond their supported applicability;
- assume technical Relationships are eternally static;
- recreate provenance structures inside the Knowledge Graph doctrine;
- recreate source-authority classifications inside the Knowledge Graph doctrine;
- treat graph persistence as proof of truth;
- create implicit universal Knowledge lifecycle enums from examples;
- promote candidate Knowledge merely because it was stored;
- treat canonical Knowledge as universally applicable or permanently infallible;
- treat canonical Knowledge as current Evidence;
- allow the Knowledge Graph to own current hypothesis state;
- allow the Knowledge Graph to calculate current diagnostic Probability;
- create a competing graph-level Uncertainty system;
- allow the Knowledge Graph to perform current Validation independently;
- allow the Knowledge Graph to independently select Actions;
- allow the Knowledge Graph to independently control Routing;
- allow the Knowledge Graph to redefine Learning;
- recreate an independent Experience Ledger authority;
- allow historical frequency to silently rewrite deterministic technical facts;
- allow Memory retrieval to redefine canonical Knowledge;
- create competing Context vocabularies;
- turn the Knowledge Graph into a workflow engine;
- create isolated manufacturer Knowledge silos when shared canonical concepts are technically appropriate;
- require architectural redesign whenever a product or domain is added;
- treat graph connectivity as proof of diagnosis;
- ignore Relationship semantics during traversal;
- reverse directional Relationships without canonical justification;
- traverse Context-inapplicable Relationships as though they were current;
- treat superseded historical Knowledge as automatically current;
- erase contradictory Knowledge merely to simplify reasoning;
- assume contradiction automatically proves one source is wrong;
- invent consensus when contradiction remains unresolved;
- ignore revision applicability;
- delete superseded Knowledge when historical lineage remains important;
- erase correction history;
- ignore downstream dependencies after material Knowledge changes;
- discard original source material merely because structured Knowledge was extracted;
- represent normalized or inferred Knowledge as verbatim source content;
- grant language models automatic canonical-ingestion authority;
- treat model-proposed Knowledge as canonical without governance;
- use language-model weights as the authoritative Knowledge Graph;
- fabricate provenance for model familiarity;
- make canonical Knowledge dependent upon one model provider;
- store canonical Knowledge only in temporary conversation context;
- bind canonical identity permanently to repository location;
- treat retrieval as validation;
- treat absence from the graph as proof of impossibility;
- hallucinate Knowledge to fill a gap;
- create permanent graph objects for every incidental conversational statement;
- over-normalize technically distinct concepts;
- under-normalize aliases into duplicate Entities;
- perform indiscriminate graph traversal without regard to current reasoning purpose;
- allow graph scale to overwhelm Context and relevance;
- treat retrieval ranking as Source Authority or truth;
- fabricate graph explanations after reaching a conclusion;
- expose restricted Knowledge without authorization;
- treat shared graph architecture as unrestricted user access;
- merge canonical Knowledge, candidate Knowledge, learned experience, Evidence, and conclusions into one undifferentiated information pool; or
- hardcode microwave-specific, RF-specific, networking-specific, manufacturer-specific, product-specific, customer-specific, organization-specific, or named-user structures into the universal Knowledge Graph doctrine.

---

## 94. Final Principle

A.R.I.A.'s Knowledge Graph is the durable structure through which she understands how things relate.

It is not a folder tree.

It is not a language model's memory.

It is not a diagnostic Probability table.

It is not a Case Evidence store.

It is not an independent Experience Ledger.

It is not a workflow engine.

And it is not automatically truth merely because information has been persisted within it.

The graph should preserve stable concepts, precise Relationships, Context, provenance, revision, contradiction, and historical continuity.

It should allow A.R.I.A. to move from one technical concept to another through meaningful Relationships rather than depending upon keyword coincidence.

It should allow new manufacturers, products, domains, and technical knowledge to connect into the existing architecture without forcing the architecture to be rebuilt every time A.R.I.A. learns something new.

It should preserve uncertainty where Knowledge is incomplete and contradiction where sources genuinely disagree.

It should allow qualified Experience to inform reasoning without allowing empirical frequency to masquerade as deterministic technical truth.

It should survive conversation length, repository reorganization, and replacement of the underlying language model.

And above all, it should ensure that A.R.I.A.'s intelligence becomes increasingly connected and increasingly durable as she learns — **without repeatedly rebuilding the cognitive architecture that gives that Knowledge meaning.**
