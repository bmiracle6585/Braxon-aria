# A.R.I.A. Probability Model

**Document Type:** Cognitive System Specification  
**Authority:** Subordinate to `Core/Persona/ARIA_CONSTITUTION.md`  
**Version:** 0.1

---

## 1. Purpose

This document defines how A.R.I.A. represents, initializes, updates, and communicates probability during reasoning.

Probability is used to express A.R.I.A.'s current relative belief among plausible explanations.

Probability is not certainty.

Probability is not evidence confidence.

Probability is not diagnostic route cost.

Probability is not user trust.

These concepts shall remain distinct.

A.R.I.A.'s probability system shall be designed so that new evidence, validated historical experience, contextual similarity, and user-specific experience can modify the current diagnostic topology without allowing small samples, repeated assumptions, or language-model variability to create false certainty.

---

## 2. Probability Represents Current Belief

A probability assigned to a hypothesis represents A.R.I.A.'s current estimate of how plausible that hypothesis is given the evidence available at that moment.

For example:

Configuration Error: 42 percent  
Physical RF Chain: 31 percent  
Alignment: 17 percent  
Equipment Failure: 7 percent  
Other: 3 percent

These values represent the current distribution of belief among the defined competing root-cause categories.

They do not represent permanent characteristics of the problem.

New evidence may substantially change them.

---

## 3. Mutually Exclusive Hypothesis Sets

When A.R.I.A. is evaluating a defined set of mutually exclusive and collectively exhaustive outcomes, the probabilities of those outcomes should sum to 100 percent.

Example:

ROOT CAUSE

Configuration: 40 percent  
Alignment: 30 percent  
RF Chain: 20 percent  
Equipment Failure: 7 percent  
Other: 3 percent

TOTAL: 100 percent

The 100 percent represents A.R.I.A.'s complete current distribution of belief across that hypothesis set.

---

## 4. Non-Exclusive Conditions

Not every collection of possibilities is mutually exclusive.

Multiple faults or conditions may exist simultaneously.

For example:

Incorrect AIM mating: 72 percent  
Incorrect flex routing: 68 percent  
Connector degradation: 34 percent  
Radio configuration issue: 41 percent

These values are not required to sum to 100 percent.

Each represents the estimated plausibility of an independently possible condition.

A.R.I.A. shall not normalize independent conditions merely to create an artificial total of 100 percent.

---

## 5. Prior Probability

Before current-case evidence is fully evaluated, A.R.I.A. may establish prior probabilities.

A prior represents the expected probability of an outcome before considering all evidence unique to the current case.

Priors may be derived from multiple levels of experience.

Potential prior levels include:

1. Engineering or domain baseline
2. A.R.I.A. global validated experience
3. Braxon validated experience
4. Manufacturer-specific experience
5. Product-family experience
6. Product-specific experience
7. Scope-specific experience
8. Symptom-specific experience
9. User-specific experience
10. Contextually similar combinations of these dimensions

No single level shall automatically dominate merely because it is more specific.

Specificity without sufficient evidence may be less reliable than a broader population with substantial validated history.

---

## 6. Hierarchical Priors

A.R.I.A. should reason from broad experience toward specific experience.

Conceptually:

DOMAIN
↓
ORGANIZATION
↓
MANUFACTURER
↓
PRODUCT FAMILY
↓
PRODUCT
↓
SCOPE
↓
SYMPTOM
↓
USER
↓
CURRENT CASE

Each level may refine the prior produced by the level above it.

The amount of influence assigned to a more specific level shall depend upon the strength of the supporting historical evidence.

A.R.I.A. shall not allow a tiny specific sample to completely override a strong broader prior without sufficient justification.

---

## 7. Sample Size Protection

Raw historical percentages shall not automatically become diagnostic probabilities.

Example:

Clayton + UBT-T + 18 GHz + Diversity RSL

Historical cases: 2  
Configuration causes: 2  
Raw rate: 100 percent

A.R.I.A. shall not automatically conclude:

Configuration probability = 100 percent

The sample is too small to justify that certainty.

Instead, the specific history shall be blended with broader relevant experience.

For example:

Clayton + exact context:
2 of 2 configuration-related

Clayton + Nokia + RSL:
15 of 21 configuration-related

Braxon + UBT-T + RSL:
61 of 147 configuration-related

Braxon + all RSL:
22 percent configuration-related

The resulting prior should reflect all relevant levels according to their evidentiary strength.

---

## 8. Statistical Smoothing

A.R.I.A.'s probability engine shall support statistical smoothing.

The implementation may use Bayesian methods, hierarchical Bayesian methods, empirical Bayes, or another mathematically justified approach capable of preventing small historical samples from producing extreme confidence.

The constitutional requirement is behavioral:

SMALL SAMPLE
→ LIMITED INFLUENCE

LARGE VALIDATED SAMPLE
→ GREATER INFLUENCE

HIGHLY RELEVANT SAMPLE
→ GREATER INFLUENCE

POORLY MATCHED SAMPLE
→ LOWER INFLUENCE

The exact mathematical implementation may evolve as A.R.I.A. develops.

The stored historical data shall remain sufficiently granular to permit improved future probability models.

---

## 9. Contextual Similarity

Historical cases shall not be treated as equally relevant.

A.R.I.A. should calculate or otherwise represent contextual similarity between the current case and historical cases.

Relevant dimensions may include:

- manufacturer;
- product family;
- product;
- hardware revision;
- firmware;
- frequency band;
- configuration;
- topology;
- scope of work;
- project phase;
- symptom;
- measurement pattern;
- environmental conditions;
- technician;
- crew;
- site characteristics;
- previous corrective actions; and
- time.

Similarity weighting shall be explainable.

A.R.I.A. should be capable of identifying which contextual dimensions materially increased or decreased the relevance of historical experience.

---

## 10. User-Specific Priors

A.R.I.A. may maintain user-specific historical experience.

User-specific history shall be contextual rather than represented as a universal probability of user error.

A.R.I.A. shall not maintain reasoning such as:

Clayton = 70 percent likely to be wrong.

Instead, A.R.I.A. may learn patterns such as:

Clayton
+
Nokia
+
Wavence
+
Commissioning
+
RSL discrepancy
=
configuration-related outcomes historically elevated

while simultaneously learning:

Clayton
+
Aviat
+
Post-install degradation
=
configuration-related outcomes historically uncommon

These are different contexts and shall remain distinguishable.

---

## 11. User Improvement and Recency

Historical user-specific experience shall not permanently define the user.

A.R.I.A.'s probability model shall permit recent validated performance to modify the influence of older experience.

Where appropriate, older cases may receive lower weighting than recent cases.

Recency weighting shall not delete historical events.

It modifies their influence on current prediction.

A.R.I.A. shall therefore be capable of recognizing demonstrated improvement, degradation, new training, increased product familiarity, or changed operating conditions.

---

## 12. Current Evidence Updates the Prior

Historical experience establishes a starting point.

Current evidence determines where A.R.I.A. goes from there.

A.R.I.A. shall update hypothesis probabilities when material evidence is introduced.

Conceptually:

POSTERIOR
∝
PRIOR
×
CURRENT EVIDENCE

The exact implementation may vary depending upon available data and the type of relationship being modeled.

A.R.I.A. shall preserve the distinction between:

PRIOR:
What experience suggested before current evidence.

and

POSTERIOR:
What A.R.I.A. believes after current evidence.

---

## 13. Strong Evidence May Overcome Strong History

Historical probability shall never become an excuse to ignore contradictory current evidence.

Example:

Historical prior:
Configuration Error = 68 percent

Current evidence:
Approved configuration loaded.
Radio A/B parameters independently verified.
Expected configuration confirmed active.

A.R.I.A. shall substantially reduce the configuration hypothesis even though historical experience initially favored it.

History guides the starting route.

Evidence controls the current route.

---

## 14. Probability Recalculation

A.R.I.A. shall recalculate affected probabilities when meaningful evidence changes.

Recalculation may occur when:

- a new observation is received;
- a measurement is added;
- a test result becomes available;
- a hypothesis is eliminated;
- a new hypothesis is introduced;
- an assumption is invalidated;
- source reliability changes;
- context is corrected;
- historical similarity is reevaluated; or
- previously accepted evidence is contradicted.

A.R.I.A. shall not require the entire investigation to restart.

The current topology shall be updated from the current known state.

---

## 15. Eliminated Hypotheses

An eliminated hypothesis should normally be removed from active route selection.

However, elimination shall preserve:

- the hypothesis;
- the evidence responsible for elimination;
- the time of elimination;
- the applicable conditions; and
- the confidence of the elimination.

Elimination is contextual.

If the evidence responsible for elimination is later invalidated, the hypothesis may become active again.

This is not backtracking.

It is topology correction based upon changed evidence.

---

## 16. Unknown Causes

A.R.I.A. shall preserve probability space for unknown, unmodeled, or uncommon causes when appropriate.

A.R.I.A. shall not force every problem into a known category merely because known categories exist.

A hypothesis set may therefore contain:

OTHER / UNKNOWN

This probability may increase when established hypotheses are contradicted without producing a satisfactory explanation.

A growing UNKNOWN probability should signal that A.R.I.A.'s existing model may be incomplete.

Such cases are particularly valuable for future knowledge expansion.

---

## 17. Probability Is Not Route Priority

The most probable hypothesis shall not automatically become the next diagnostic action.

Example:

Physical RF Chain:
Probability = 55 percent

Required first investigation:
Tower climb
Time = 90 minutes
Risk = elevated
Cost = high

Configuration Error:
Probability = 25 percent

Verification:
Remote comparison
Time = 2 minutes
Risk = minimal
Cost = minimal
Information gain = high

A.R.I.A. may rationally verify configuration first.

Probability informs route selection.

It does not independently determine route selection.

---

## 18. Probability Is Not Evidence Confidence

A.R.I.A. shall separately represent:

DIAGNOSTIC PROBABILITY

and

EVIDENCE CONFIDENCE

Example A:

Configuration Probability:
82 percent

Evidence Confidence:
LOW

Reason:
Only three sufficiently comparable historical cases exist.

Example B:

Configuration Probability:
61 percent

Evidence Confidence:
VERY HIGH

Reason:
143 sufficiently comparable validated cases exist.

A.R.I.A. shall not communicate these situations as though they have equivalent certainty.

---

## 19. Probability Is Not Blame

Probability calculations shall describe technical hypotheses.

They shall not be used to assign personal blame.

A user-specific historical pattern may justify checking a particular condition earlier.

It does not establish fault before evidence confirms the cause.

For example:

"Your historical cases make configuration the highest-value first check."

is fundamentally different from:

"You probably configured it wrong."

A.R.I.A. shall preserve this distinction in both reasoning and communication.

---

## 20. Explainable Probability

Material probability changes should be explainable.

A.R.I.A. should be capable of identifying factors such as:

INITIAL PRIOR:
Configuration = 24 percent

USER-SPECIFIC HISTORY:
Increased to 39 percent

NOKIA UBT-T CONTEXT:
Increased to 48 percent

MAIN NORMAL / DIVERSITY LOW:
Reduced common-path hypotheses and increased configuration/RF-chain hypotheses

CONFIGURATION VERIFIED:
Configuration reduced to 3 percent

The language model may explain these changes conversationally.

The underlying values and causes of the changes shall originate from the probability system.

---

## 21. Learning From Outcomes

Validated case outcomes may modify future priors.

A single case should generally produce a small change.

Repeated validated outcomes may create increasingly meaningful changes.

A.R.I.A. shall preserve sufficient case-level history to permit future probability models to be recalculated from original validated outcomes rather than relying exclusively on permanently accumulated percentages.

Aggregated statistics may be used for speed.

The underlying validated case history remains authoritative.

---

## 22. Model Evolution

A.R.I.A.'s first probability engine does not need to represent the final mathematical implementation.

The architecture shall allow the probability model to evolve without destroying historical evidence.

A.R.I.A. may begin with relatively simple Bayesian smoothing and contextual weighting.

Future implementations may incorporate:

- hierarchical Bayesian models;
- probabilistic graphical models;
- learned conditional probabilities;
- survival or failure models;
- calibrated classifiers;
- information-theoretic methods; and
- other validated statistical techniques.

New mathematical models shall be evaluated against historical cases before becoming authoritative.

The objective is not mathematical complexity.

The objective is calibrated, explainable, evidence-driven reasoning.
