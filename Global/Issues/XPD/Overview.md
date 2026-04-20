# XPD Overview

## Issue Definition

XPD stands for Cross-Polar Discrimination.

It is a measure of how well the two polarities are isolated from one another on the path. Good XPD indicates strong separation between the polarities. Poor XPD indicates that the polarities are not properly isolated, which can reduce performance and affect modulation outcomes.

---

## Why This Matters

XPD is important because poor XPD can:
- reduce link performance,
- prevent the radio from reaching desired modulation,
- create unstable or unacceptable path performance,
- indicate improper feedhorn alignment.

In most cases, XPD issues are not random. They usually point toward alignment discipline and feedhorn positioning.

---

## ARIA’s Initial Approach

When ARIA encounters an XPD issue, she should first determine:
1. What are the current XPD values on both sides?
2. What is the engineered or expected XPD target for the path?
3. Is RSL healthy and on target?
4. Have the feedhorns been leveled?
5. Has only one side been adjusted for XPD while the other remains level?
6. How far off level is the adjusted feedhorn?

These questions should be answered before assuming root cause.

---

## Primary Troubleshooting Domain

If RSL is healthy, ARIA should treat XPD issues primarily as a feedhorn alignment issue unless there is strong evidence to the contrary.

She should not default to polarity hookup issues when RSL is healthy, because a true polarity hookup problem would be expected to affect RSL.

---

## Expected XPD Behavior

Each path has engineered XPD expectations.

Most commonly, the goal is to achieve balanced values close to the target on both sides. A common target is:
- 32 / 32

The closer the values are to one another and to target, the better.

---

## Severity Guidance

### Slight but acceptable variation
Examples:
- 29 / 35

This may indicate that XPD is not perfectly balanced, but may still be operationally acceptable depending on the path requirements.

### Severe XPD issue
Examples:
- 25 / 45
- XPD reading unavailable

These patterns suggest a meaningful feedhorn alignment problem or another issue affecting cross-polar performance.

Severe XPD issues may also cause the modulation to settle below the desired target, such as:
- 2048QAM instead of 4096QAM

---

## Important Alignment Rule

Leveling the feedhorn is not the same as aligning the feedhorn for XPD.

ARIA should recognize that a tech may report the feedhorn as level while XPD is still poorly aligned.

For XPD tuning:
- one side should remain level,
- the other side should be adjusted.

Adjusting both sides creates unnecessary complexity and can reduce accuracy.

---

## Common Technician Errors

Common mistakes include:
- assuming level means aligned,
- adjusting both sides instead of one,
- moving too quickly during adjustment,
- failing to measure how far off level the adjusted feedhorn is.

---

## Additional Diagnostic Aid

When appropriate, ATPC may be used as a diagnostic aid.

A controlled reduction in transmit power may help assess how performance responds, because ATPC considers more than just RSL in its evaluation.

As a general rule:
- do not reduce transmit power by more than 2 dB for this purpose.

ARIA should treat ATPC as a controlled diagnostic tool, not a substitute for proper XPD alignment.