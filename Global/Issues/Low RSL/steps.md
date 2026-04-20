# Low RSL – Troubleshooting Steps

## Step 1: Check for alarms
- Determine whether any active alarms are present.
- If alarms are present, use `alarms.md` logic first.
- If alarms suggest the link is not currently achievable, troubleshoot the alarm condition before continuing alignment.

---

## Step 2: Compare engineered RSL to actual RSL
Identify:
- engineered RSL,
- current measured RSL,
- size of the RSL deficiency.

ARIA should classify the deficiency as:
- subtle,
- moderate,
- substantial.

---

## Step 3: Determine whether alignment is still the most likely issue

- Use proper field terminology when describing alignment.
- Refer to the process as “pathing” or “aligning,” not sweeping.

ARIA should not assume alignment is complete based on a single pathing attempt.

Ask:
- How many times has each antenna been pathed?
- Was alignment performed using both coarse movement (panning) and fine adjustment?
- Were side lobes identified and counted?
- Was the peak passed and returned to, confirming the true center beam?
- Are we confident the highest possible RSL has been achieved consistently?

---

### If alignment confidence is low:

- Continue pathing on both sides.
- Do not stop at the first strong RSL reading.
- Move past the peak and confirm you can return to the highest value.
- Count side lobes to ensure the antenna is not sitting on a shoulder.
- Perform multiple pathing passes to confirm repeatability.

- As you approach peak:
  - transition to fine adjustment,
  - make slow, controlled movements,
  - allow RSL to settle before making further changes.

- If tower personnel are assisting:
  - coordinate controlled panning movements,
  - avoid large or rushed adjustments,
  - confirm peak from both directions before locking in.

- Alignment is only considered complete when:
  - the highest RSL has been consistently achieved,
  - the center beam has been confirmed,
  - results are repeatable across multiple passes.

---

### If alignment confidence is high:

- Do not continue pathing unnecessarily.
- Move on to evaluating:
  - installation-related loss (filters, line length, antenna gain),
  - transmit power vs PCN,
  - RF path and hardware conditions,
  - polarity and hookup correctness.

---

## Step 4: If the RSL deficiency is subtle
If the RSL is only slightly below the engineered value, ARIA should first suspect:
- incomplete or inaccurate alignment,
- side-lobe confusion,
- center beam not fully achieved,
- minor physical installation losses.

Ask:
- How many times was each antenna pathed?
- Are we certain the center beam was identified correctly?
- Is there confidence that alignment has been maximized?

If no:
- continue pathing.

If yes:
- check for minor installation loss contributors:
  - filter insertion loss,
  - transmission line length differences,
  - antenna size differences,
  - antenna gain differences.

---

## Step 5: If the RSL deficiency is moderate
If the RSL is meaningfully below the engineered value, ARIA should evaluate:
- filter connections,
- circulator direction,
- TX power vs PCN,
- abnormal installation loss.

Ask:
- Are all filter connections correct and secure?
- Are the circulators installed in the proper direction?
- Does measured TX power match the PCN?
- Is the radio producing expected output power?

If TX power is lower than planned:
- suspect transmit-side deficiency,
- do not treat alignment as the only issue.

---

## Step 6: If the RSL deficiency is substantial
If the RSL is well below the engineered value, ARIA should expand troubleshooting to include:
- cross-polarity issues,
- incorrect hookup,
- muted transmitter,
- major filter or waveguide issues,
- major TX power deficiency,
- major path viability concerns.

Ask:
- Is cross-polarity correct?
- Are transmit and receive paths connected correctly?
- Is the transmitter muted?
- What does the measurements page show for TX power?
- Does measured TX power match PCN expectations?

If major mismatch exists:
- troubleshoot RF generation and transmission path before assuming alignment alone.

---

## Step 7: Compare both sides of the path
ARIA should compare:
- Site A RSL,
- Site B RSL,
- whether both sides are equally degraded.

Interpretation:
- If both sides are similarly low, suspect alignment, path, or shared condition.
- If one side is much lower than the other, suspect a localized issue on that path side.
- If one side appears normal and the other does not, consider receiver or demodulator-related issues.

---

## Step 8: Consider demodulator or receiver issues
If the path appears partially present but one side behaves abnormally, ARIA should consider:
- receiver issues,
- demodulator issues,
- abnormal local receive behavior.

This is especially important if:
- only one side is showing abnormal RSL behavior,
- TX values look normal,
- alignment confidence is high.

---

## Step 9: Use space diversity logic when applicable
If the path uses space diversity, ARIA should compare:
- main antenna readings on both sites,
- diversity antenna readings on both sites,
- whether one antenna path is the outlier.

Process:
- analyze all four antennas,
- determine whether three of four are within expected range,
- isolate the outlier.

Interpretation:
- If three antennas are within spec and one is low, the issue is likely associated with that specific antenna path.
- If a site’s diversity antenna is strong but its main antenna is weak, the far-end transmit alignment may already be confirmed, which points more strongly to the weak local path.

This should be treated as a process-of-elimination method.

---

## Step 10: Re-evaluate the most likely domain
After each major check, ARIA should decide whether the issue is now most likely:
- alignment-related,
- installation-loss related,
- transmit-side related,
- receive-side related,
- hookup / polarity related,
- diversity-path specific.

ARIA should not continue broad troubleshooting once the likely domain has been narrowed.

---

## Final Rule
ARIA should not assume every Low RSL issue is an alignment issue.

She should first determine:
- whether alarms are changing the path,
- how far the measured RSL is from engineered RSL,
- whether alignment confidence is truly high,
- whether measured values support a transmit, receive, installation, or path-related problem.

She should guide the user toward the most likely next step, not every possible step.