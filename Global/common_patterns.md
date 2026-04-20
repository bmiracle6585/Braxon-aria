# Common Patterns

## Signal & RSL Patterns

### Pattern: Severity Changes Direction
The size of the deficiency matters. A subtle difference and a substantial difference should not be treated as the same class of problem.

_Applies to:_ Low RSL

---

### Pattern: Compare Expected vs Actual
Always compare engineered or expected values to live measured values before deciding the next path.

_Applies to:_ Low RSL, Power Issues, Throughput Issues

---

## Alarm-Driven Patterns

### Pattern: Alarm Before Alignment
If alarms suggest the link is not currently capable of passing valid signal, troubleshoot the alarm condition before continuing alignment.

_Applies to:_ Low RSL, Link Down

---

## Comparative Analysis Patterns

### Pattern: Compare Both Sides
When possible, compare Site A and Site B values. Symmetry and asymmetry help narrow whether the issue is shared or localized.

_Applies to:_ Low RSL, Link Instability

---

### Pattern: Outlier Isolation
If multiple comparable paths or elements exist, and most are within spec while one is not, isolate the outlier as the likely issue.

_Applies to:_ Low RSL, Diversity Systems

---

### Pattern: Process of Elimination
Use known-good components or paths to eliminate unlikely fault domains and narrow the most probable cause.

_Applies to:_ All troubleshooting scenarios

---

## Alignment Patterns

### Pattern: Path Confidence Must Be Earned
Do not assume alignment is complete just because pathing was performed. Confirm side lobes were counted and the center beam was truly identified.

_Applies to:_ Low RSL, Alignment Issues

---

## General Troubleshooting Patterns

### Pattern: Do Not Assume Hardware First
Do not jump to hardware failure before verifying alignment, configuration, and installation conditions.

_Applies to:_ All scenarios