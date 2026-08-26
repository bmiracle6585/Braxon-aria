# A.R.I.A. Adaptive Diagnostic Routing

**Document Type:** Cognitive System Specification  
**Authority:** Subordinate to `Core/Persona/ARIA_CONSTITUTION.md`  
**Version:** 0.1

---

## 1. Purpose

This document defines how A.R.I.A. selects, evaluates, traverses, suppresses, and recalculates diagnostic routes.

A.R.I.A.'s diagnostic routing architecture is conceptually inspired by dynamic network routing.

A technical problem establishes a changing topology of possible causes, observations, tests, conditions, and outcomes.

A.R.I.A. shall not follow a fixed troubleshooting checklist when sufficient structured knowledge exists to reason dynamically.

Instead, A.R.I.A. shall continuously determine the most valuable next diagnostic hop toward a validated resolution.

The routing system shall operate independently from the language model.

The language model may interpret user input and communicate routing decisions.

It shall not independently invent route metrics, historical statistics, completed tests, eliminated hypotheses, or diagnostic state.

---

## 2. Diagnostic Topology

An active diagnostic case shall be represented as a graph.

The graph may contain nodes representing:

- problem states;
- symptoms;
- observations;
- measurements;
- hypotheses;
- components;
- configurations;
- conditions;
- tests;
- findings;
- corrective actions; and
- outcomes.

Relationships between nodes shall be represented by typed edges.

The topology may change throughout the case as evidence is introduced.

---

## 3. Diagnostic Nodes

Every meaningful node should have a stable identity and defined type.

Conceptually:

NODE ID:
NODE-000184

TYPE:
HYPOTHESIS

CONCEPT:
Incorrect Diversity Flex Routing

STATUS:
ACTIVE

CONTEXT:
Nokia / Wavence / UBT-T / Diversity

Nodes shall not depend upon their visual or filesystem location for meaning.

The same canonical concept may participate in many different diagnostic routes.

---

## 4. Diagnostic Edges

Edges define meaningful relationships between nodes.

Initial relationship types may include:

- CAN_CAUSE;
- SUPPORTS;
- CONTRADICTS;
- ELIMINATED_BY;
- CONFIRMED_BY;
- TESTED_BY;
- INDICATES;
- REQUIRES;
- PRECEDES;
- AFFECTS;
- CONNECTED_TO;
- MATES_WITH;
- CONFIGURED_AS;
- RESOLVED_BY; and
- LEADS_TO.

Edges may contain contextual attributes such as:

- conditional probability;
- relationship strength;
- evidence confidence;
- manufacturer applicability;
- product applicability;
- configuration applicability;
- scope applicability;
- source provenance; and
- historical support.

An edge shall not be interpreted as universally valid unless its scope establishes universal applicability.

---

## 5. Point A and Point Z

Point A represents the current understood problem state.

Point Z represents a sufficiently validated resolution or objective.

Point Z does not need to be known when the case begins.

A.R.I.A. may discover additional candidate destinations as the investigation develops.

Multiple routes may exist between A and Z.

The preferred route may change whenever the topology changes.

---

## 6. Route Selection Is Not Cause Selection

A.R.I.A. shall distinguish:

MOST LIKELY CAUSE

from

BEST NEXT ACTION

These may be different.

Example:

Physical RF Chain

Probability:
55 percent

Next verification:
Tower climb

Estimated time:
90 minutes

Risk:
Elevated

Cost:
High

versus:

Configuration

Probability:
25 percent

Next verification:
Remote configuration comparison

Estimated time:
2 minutes

Risk:
Minimal

Cost:
Minimal

Information gain:
High

A.R.I.A. may select configuration verification as the next diagnostic hop even though the physical RF chain remains the most probable cause.

---

## 7. Route Metric

A.R.I.A. shall calculate a diagnostic route metric representing the relative value of available next actions.

The metric may incorporate:

- hypothesis probability;
- relationship strength;
- evidence confidence;
- contextual similarity;
- historical success;
- expected information gain;
- time cost;
- labor cost;
- financial cost;
- operational impact;
- accessibility;
- safety risk;
- reversibility;
- dependency requirements; and
- expected ability to eliminate competing hypotheses.

The exact formula may evolve.

The architecture shall preserve the individual contributing factors rather than storing only a final opaque score.

This allows future recalculation, calibration, and explanation.

---

## 8. Additive Route Cost

Where useful, A.R.I.A. may transform probability-like relationship values into additive costs.

For a probability `p`, one possible transformation is:

`cost = -ln(p)`

This allows the cumulative strength of a route to be represented through additive edge costs.

For example:

A -> B

Probability:
0.85

Cost:
-ln(0.85)

B -> C

Probability:
0.78

Cost:
-ln(0.78)

Cumulative route probability:

0.85 x 0.78 = 0.663

Cumulative transformed cost:

-ln(0.85) + -ln(0.78)

Lower transformed probability cost represents a stronger probabilistic route.

This mechanism may contribute to routing.

It shall not be treated as the complete diagnostic route metric because diagnostic value also includes cost, risk, information gain, and other factors.

---

## 9. Shortest Diagnostic Path First

A.R.I.A.'s routing engine may implement a process conceptually described as:

**Shortest Diagnostic Path First**

SDPF does not mean the route containing the fewest steps.

It means the route currently estimated to provide the most efficient progression toward validated resolution according to A.R.I.A.'s diagnostic route metric.

A longer sequence of inexpensive, highly discriminating tests may be preferable to one immediate expensive intervention.

The objective is diagnostic efficiency, not minimum hop count.

---

## 10. Next-Hop Selection

A.R.I.A. shall normally select one preferred next diagnostic action.

The routing engine should also preserve alternate candidate actions.

Conceptually:

NEXT HOP:

Verify Radio A/B Configuration

ROUTE VALUE:
0.91

REASON:
High information gain
Low time cost
Low operational risk
Historically relevant
Can eliminate configuration branch

ALTERNATE 1:
Inspect Diversity Flex Routing

ROUTE VALUE:
0.84

ALTERNATE 2:
Perform Alignment Verification

ROUTE VALUE:
0.61

The user-facing response does not need to expose raw route metrics unless useful.

The underlying routing state shall preserve them.

---

## 11. Information Gain

A.R.I.A. shall estimate the diagnostic value of the information expected from a test.

A test capable of materially affecting several hypotheses may receive higher routing priority.

For example:

TEST:
Compare Main and Diversity RSL

Possible Result A:
Both low

Potentially increases:
Common-path issue
Alignment
Path obstruction
Weather

Possible Result B:
Main normal / Diversity low

Potentially decreases:
Common-path issue
Weather
General LOS obstruction

Potentially increases:
Diversity RF chain
Diversity configuration
Cross-polarization
Component-specific fault

Because either result substantially changes the topology, the test has high information value.

---

## 12. Route Suppression

A.R.I.A. may suppress a route when available evidence makes immediate investigation inefficient or unjustified.

A suppressed route is not necessarily eliminated.

Possible suppression reasons include:

- very low current probability;
- extremely high diagnostic cost;
- prerequisite test not completed;
- insufficient evidence;
- higher-value test available;
- safety restriction;
- lack of access;
- equipment unavailable; or
- current conditions prevent meaningful testing.

Suppressed routes shall remain available for reconsideration when conditions change.

---

## 13. Route Elimination

A route may be eliminated when sufficient evidence contradicts a required condition.

Example:

HYPOTHESIS:
General path obstruction

Evidence:

Main RSL:
Within 1 dB of engineered target

Diversity RSL:
11 dB below target

If both RF paths share the relevant propagation path, this evidence may strongly contradict a general path obstruction.

The route may be eliminated or substantially reduced according to the applicable technical relationships and evidence confidence.

Elimination shall preserve the reason.

---

## 14. Topology Change

The diagnostic topology shall be recalculated when meaningful evidence changes the case.

A topology change may:

- activate a route;
- suppress a route;
- eliminate a route;
- restore a previously eliminated route;
- introduce a new hypothesis;
- alter probability;
- alter evidence confidence;
- alter route cost;
- alter information value; or
- change the preferred next hop.

A.R.I.A. shall preserve the state transition responsible for the change.

---

## 15. Rerouting

When the preferred route becomes less desirable, A.R.I.A. shall recalculate from the current diagnostic state.

A.R.I.A. shall not unnecessarily return to Point A.

Example:

A -> B -> C

At C:

New evidence eliminates C.

A.R.I.A. preserves everything learned between A and C.

The routing engine recalculates.

New preferred route:

Current State -> D -> F

This is rerouting.

It is not restarting.

---

## 16. No Blind Loops

A.R.I.A. shall prevent diagnostic loops.

A previously completed test should not become the preferred next hop again unless:

- the underlying condition changed;
- the original test was unreliable;
- the test procedure was incorrect;
- contradictory evidence emerged;
- a dependent configuration changed;
- the original context was misunderstood; or
- repetition itself has legitimate diagnostic value.

The reason for repeating a test shall be recorded.

A.R.I.A. shall not repeat troubleshooting merely because the language model forgot that the test occurred.

---

## 17. Route History

An active case should preserve significant routing decisions.

Conceptually:

STEP 1

Selected:
Verify configuration

Reason:
Highest route value

Result:
Configuration correct

Effect:
Configuration hypothesis reduced

---

STEP 2

Selected:
Compare Main/Diversity RSL

Result:
Main normal / Diversity -11 dB

Effect:
Common-path hypotheses reduced
Diversity-specific hypotheses increased

---

STEP 3

Selected:
Inspect Diversity RF chain

Result:
Incorrect flex routing discovered

Effect:
Flex-routing hypothesis strongly confirmed

This history provides explainability and future learning data.

---

## 18. User-Specific Routing Influence

User-specific experience may modify route selection when relevant.

Example:

Current user:
Clayton

Comparable historical RSL cases:
13

Configuration-related outcomes:
9

This historical pattern may increase the initial value of configuration verification.

However, user history shall remain one routing input among many.

It shall not override strong contradictory current evidence.

It shall not become personal blame.

---

## 19. Historical Route Performance

A.R.I.A. may learn not only which causes occurred historically, but which diagnostic actions were useful.

For example:

TEST:
Compare Radio A/B configuration

Historical comparable cases:
82

Cases where test materially narrowed diagnosis:
61

Average execution time:
2.4 minutes

Risk:
Minimal

Such history may increase the test's future route value even when configuration is not the highest-probability cause.

This allows A.R.I.A. to learn **how to troubleshoot better**, not merely what historically failed.

---

## 20. Failed Routes Are Valuable

A diagnostic route that does not identify the cause may still produce valuable information.

Example:

Configuration verified correct.

The configuration route did not produce the resolution.

However, it eliminated a major hypothesis at low cost.

The route was therefore diagnostically valuable.

A.R.I.A.'s learning system shall not classify every non-resolution route as a failure.

Diagnostic value includes uncertainty reduction.

---

## 21. Route Cost Is Contextual

The cost of an action may differ by situation.

Example:

Inspect AIM mating

GROUND LAB:
Low cost

ACTIVE TOWER SITE:
Requires climb
Higher labor
Higher risk
Higher time cost

REMOTE SITE DURING WEATHER EVENT:
Potentially unavailable

Therefore, route cost shall be calculated from current context rather than treated as a permanent property of the test.

---

## 22. Safety and Authority

Diagnostic efficiency shall never override applicable safety or authority restrictions.

A technically efficient route that requires an unauthorized, unsafe, or prohibited action shall not be selected.

Such a route may remain technically relevant while being operationally unavailable.

A.R.I.A. should identify the restriction and select the next permissible route when possible.

---

## 23. Unknown Route Discovery

A.R.I.A.'s routing engine shall permit discovery of causes not currently represented in the known topology.

When established routes are repeatedly contradicted, the probability or relevance of:

OTHER / UNKNOWN

may increase.

A.R.I.A. may then:

- retrieve broader knowledge;
- identify weakly connected concepts;
- request additional observations;
- use model-assisted hypothesis generation;
- compare unusual historical cases; or
- escalate for human expertise.

A newly discovered route shall remain provisional until sufficient evidence supports it.

---

## 24. Route Completion

A route reaches Point Z when the applicable resolution requirements are satisfied.

A high probability alone does not establish completion.

Where practical, completion should include:

CONFIRMED CAUSE
+
CORRECTIVE ACTION
+
EXPECTED RESULT OBSERVED

Example:

Finding:
Diversity flex incorrectly routed

Action:
Corrected flex routing

Result:
Diversity RSL improved from -54 dBm to -42 dBm

Engineered target:
-41 dBm

Status:
RESOLVED / VALIDATED

The completed route may then become eligible for the Experience Ledger.

---

## 25. Explainability

A.R.I.A. shall be capable of explaining why a diagnostic action was selected.

The explanation should be derivable from actual routing state.

For example:

"Configuration is not currently the most probable root cause. I am asking you to verify it first because it takes approximately two minutes, has no operational risk, and a correct result eliminates an entire diagnostic branch before we consider a tower climb."

This explanation shall not be fabricated after the decision.

It shall reflect the factors that actually influenced route selection.

---

## 26. Routing Engine Independence

The Adaptive Diagnostic Routing Engine shall exist independently of the installed language model.

A language model may assist with:

- interpreting natural language;
- identifying candidate concepts;
- proposing provisional hypotheses;
- explaining route decisions;
- asking contextually appropriate questions; and
- communicating technical reasoning.

The authoritative routing engine shall determine:

- active diagnostic state;
- stored evidence;
- historical statistics;
- probability values;
- route metrics;
- eliminated hypotheses;
- completed tests; and
- preferred next hops.

Changing the language model shall not erase A.R.I.A.'s diagnostic state or learned routing experience.

---

## 27. Design Objective

The objective of A.R.I.A.'s routing architecture is not to imitate OSPF as a networking protocol.

OSPF provides the conceptual inspiration:

- maintain a topology;
- assign meaningful route costs;
- calculate preferred paths;
- respond to topology changes;
- preserve alternate routes; and
- recalculate when conditions change.

A.R.I.A. applies these principles to diagnostic reasoning.

Her destination is not an IP network.

Her destination is **Point Z: the most efficiently reached validated resolution supported by the available evidence.**
