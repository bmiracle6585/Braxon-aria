# Low RSL – Alarm Logic

## Core Principle

Alarms should be used to determine whether the path is currently achievable and to help narrow the troubleshooting domain.

ARIA should treat alarms as directional indicators, not absolute conclusions.

---

## Step 1: Determine if alarms are present

ARIA should first identify:
- Are there any active alarms?
- Are they local or remote?
- Are they transmit-related or receive-related?

---

## Step 2: Interpret Alarm Impact

### If NO alarms are present:
- The path is likely achievable.
- The issue is more likely related to:
  - alignment,
  - pathing accuracy,
  - minor installation losses.

ARIA should prioritize alignment verification before deeper troubleshooting.

---

### If alarms ARE present:
ARIA should determine whether the alarm indicates:

#### 1. Transmit-side issue
Indicators:
- low or missing transmit power,
- transmitter muted,
- power mismatch vs expected values.

Implication:
- The far end may not be receiving a proper signal.
- Alignment may not be achievable until resolved.

---

#### 2. Receive-side issue
Indicators:
- inability to properly demodulate signal,
- abnormal receive behavior,
- signal present but not usable.

Implication:
- The issue may be local to the receiving radio.
- May indicate demodulator or receiver-related problems.

---

#### 3. Link-level or communication failure
Indicators:
- complete loss of signal,
- no detectable RF link,
- both sides reporting abnormal conditions.

Implication:
- The path may not currently be viable.
- Alignment efforts may not produce valid results until resolved.

---

## Step 3: Alarm vs Alignment Decision

ARIA should determine:

### If alarms suggest the path is NOT currently achievable:
- Troubleshoot the alarm condition first.
- Do NOT continue alignment efforts until basic signal conditions are restored.

---

### If alarms do NOT prevent signal viability:
- Continue with alignment and RSL-based troubleshooting.
- Use alarms only as supporting indicators.

---

## Step 4: Cross-Site Comparison

ARIA should compare:
- alarms on Site A vs Site B,
- whether alarms are present on one side or both sides.

### Interpretation:
- If alarms exist on only one side → likely localized issue.
- If alarms exist on both sides → possible path, configuration, or major signal issue.

---

## Step 5: Alarm Consistency Check

ARIA should verify:
- Do alarm conditions match measured values?
- Does reported TX power match expected output?
- Does RSL behavior align with alarm indications?

If inconsistencies exist:
- Do not trust a single indicator.
- Continue verification before drawing conclusions.

---

## Step 6: Priority Rule

ARIA should always determine:

1. Is the link currently capable of passing signal?
2. Are alarms preventing valid alignment or measurement?
3. Should troubleshooting occur before alignment continues?

---

## Final Rule

ARIA should never assume alignment is the issue if alarms suggest the link is not operational.

She should resolve conditions that prevent signal viability before proceeding with alignment-based troubleshooting.