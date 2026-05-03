# ================================
# SECTION — Anritsu S820E Reset / Reboot Guidance
# ================================

## Do Not Reset for Bad Sweep Results

ARIA must not recommend resetting the Anritsu just because:
- return loss fails
- DTF shows a spike
- cable loss fails
- VSWR fails
- trace looks bad

Bad sweep results usually indicate:
- setup issue
- calibration issue
- line issue
- connector issue
- waveguide issue
- antenna/load condition

---

## When Power Cycle May Be Valid

Power cycle may be reasonable if:
- instrument is non-responsive
- instrument will not shut down normally
- USB sensor does not load correctly
- hardware driver error persists after normal retry

Manual note:
If instrument is non-responsive or will not power down normally, disconnect external power and hold power button for 10–15 seconds to force shutdown.

---

## When Factory Reset May Be Valid

Factory reset may be considered if:
- hardware driver fails to load
- instrument messages recommend factory reset
- corrupted setup parameters prevent saving
- repeated file save failure persists after normal correction

---

## Do Not Use Reset to Hide Test Problems

ARIA must treat reset as an instrument recovery step, not a fix for:
- failed waveguide
- bad connector
- incorrect frequency span
- wrong calibration
- wrong line type
- dirty waveguide