# Low RSL Overview

## Issue Definition

Low RSL refers to a received signal level that is below the engineered or expected value for the path.

This may present as:
- slightly low received signal,
- unstable performance,
- reduced margin,
- degraded modulation,
- or complete link concerns depending on severity.

---

## Why This Matters

Low RSL is important because it can indicate:
- incomplete or inaccurate alignment,
- physical installation loss,
- transmit-side deficiency,
- receive-side abnormality,
- path-related issues,
- configuration or hookup problems.

Not all Low RSL issues have the same cause.  
The size of the RSL deficiency, alarm state, and measured values help determine the most likely troubleshooting path.

---

## ARIA’s Initial Approach

When ARIA encounters a Low RSL issue, she should first determine:
1. Are any alarms present?
2. What is the engineered RSL?
3. What is the current measured RSL?
4. How large is the deficiency?
5. Has alignment been completed thoroughly and confidently?

These questions should be answered before assuming root cause.

---

## Primary Troubleshooting Domains

ARIA should generally sort Low RSL issues into one or more of the following domains:
- alignment or pathing issue,
- minor physical installation loss,
- transmit-side issue,
- receive-side issue,
- hookup or polarity issue,
- diversity-path-specific issue,
- broader path viability issue.

---

## RSL Severity Logic

### Subtle deficiency
A small RSL shortfall often points toward:
- incomplete alignment,
- side-lobe confusion,
- center beam not fully confirmed,
- small physical loss differences.

### Moderate deficiency
A more meaningful shortfall may indicate:
- installation issues,
- filter or circulator problems,
- output power mismatch,
- additional RF loss.

### Substantial deficiency
A large RSL shortfall may indicate:
- major hookup problems,
- muted or impaired transmitter,
- cross-polarity issues,
- major RF path or hardware issues,
- non-viable path conditions.

---

## Alarm Relationship

Alarms should be used to determine whether the link is currently capable of valid alignment and signal passage.

If alarms suggest the path is not operational, ARIA should troubleshoot those conditions before treating alignment as the primary issue.

---

## Site Comparison Logic

ARIA should compare:
- Site A vs Site B RSL,
- transmit power vs PCN,
- expected vs actual values,
- main vs diversity readings when applicable.

These comparisons help narrow the likely fault domain and avoid wasted effort.

---

## Space Diversity Consideration

When space diversity is present, ARIA should use comparative logic across all antennas to isolate the likely problem path.

If three of four antenna paths are within expected range and one is not, the outlier path should be treated as the likely issue.

---

## Guiding Principle

ARIA should not assume every Low RSL issue is an alignment problem.

She should determine:
- whether the path is currently viable,
- how severe the deficiency is,
- whether alignment confidence is truly high,
- whether measurements point more strongly to installation, transmit, receive, or hookup issues.

Her goal is to guide the user toward the most likely successful path first.