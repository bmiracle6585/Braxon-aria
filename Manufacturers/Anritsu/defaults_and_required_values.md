# ================================
# SECTION — Anritsu S820E Defaults & Required Values
# ================================

## Frequency Range Rule

Braxon field standard:
- Start frequency = 50 MHz below lowest operating RF frequency
- Stop frequency = 50 MHz above highest operating RF frequency

Do not use an entire microwave band unless explicitly required.

Reason:
- Sweep span affects DTF distance resolution.
- Wider span improves distance resolution but can reduce maximum usable distance.
- Narrower span increases maximum usable distance but reduces distance resolution.

---

## Data Points

Available data point settings:
- 130
- 259
- 517
- 1033
- 2065

Default:
- 259

Important:
- More data points improve usable distance coverage.
- 2065 should be selected before calibration if it will be needed.

---

## DTF Resolution Rule

Distance resolution improves as frequency span increases.

If two faults are close together:
- wider span improves ability to separate them

If line length exceeds DMax:
- increase data points, or
- reduce frequency span

---

## Windowing Defaults

Recommended field default:
- Nominal Side Lobe

Use Rectangular when:
- best distance resolution is required
- multiple close faults are suspected

Use Low Side Lobe when:
- small events need to be found near larger reflections

Use Minimum Side Lobe rarely:
- highest side-lobe suppression
- worst distance resolution

---

## Calibration Requirements

Required before measurement:
- valid calibration
- correct calibration type
- correct line type
- correct calibration kit
- calibration performed at end of test cable/adapters

Recalibrate if:
- frequency range changes after calibration
- internal temperature changes more than ±10 °C
- calibration correction is off
- setup changes invalidate calibration

Recommended:
- allow S820E to warm up for 10 minutes before calibration

---

## Instrument / Connector Protection

Maximum typical RF input:
- +23 dBm
- ±50 VDC

Torque:
- Type N connector: 12 lbf-in / 1.4 N-m
- K connector: 8 lbf-in / 0.90 N-m

---

## Power / Battery

Approximate battery operation:
- 4 hours fully charged

External power:
- 11 VDC to 14 VDC
- up to 4.0 A

Automotive adapter:
- minimum 60 W at 12 VDC

---

## File Storage

Measurement files contain:
- measurement data
- setup data

Setup files contain:
- measurement type
- frequency span
- distance span
- DTF setup
- amplitude settings
- markers
- limit lines
- calibration coefficients
- data points
- run/hold status
- RF immunity status

Screen shots save visual screen captures.

# ================================
# SECTION — DTF Aid Rules & Limits
# ================================

## Core Relationship Rule

DTF performance is controlled by:

- Frequency Span
- Data Points

These determine:
- Max Usable Distance
- Distance Resolution

---

## Max Usable Distance Rule

If line length exceeds Max Usable Distance:

ONLY solutions:
- Increase data points
- OR reduce frequency span

---

## Distance Resolution Rule

Distance resolution is inversely proportional to frequency span.

- Wider span → better resolution
- Narrower span → worse resolution

---

## Tradeoff Rule

- Wide span:
  - better resolution
  - shorter max distance

- Narrow span:
  - longer max distance
  - worse resolution

ARIA must recognize:
You cannot optimize both at the same time.

---

## Field Requirement

Max Usable Distance MUST:
- exceed total waveguide length
- exceed tower height
- include all physical components

---

## Critical Warning

Incorrect span or data points will cause:
- incomplete sweep coverage
- incorrect fault interpretation
- misleading results

# ================================
# SECTION — Calibration Rules & Requirements
# ================================

## Calibration Validity Rule

Calibration is only valid if:
- frequency range has not changed
- data points have not changed
- line type has not changed
- test setup has not changed

---

## Recalibration Triggers

Recalibration is REQUIRED if:
- frequency span is changed
- data points are changed
- measurement type changes significantly
- calibration cable or adapter changes
- temperature changes significantly (approx ±10°C)
- calibration is turned OFF

---

## Warm-Up Requirement

Recommended:
- allow instrument to warm up for ~10 minutes before calibration

---

## Calibration Location Rule

Calibration must be performed:
- at the END of the test cable
- including ALL adapters

Failure to do this introduces:
- cable error
- adapter error
- incorrect measurements

---

## Calibration Sequence

Standard OSL sequence:
1. Open
2. Short
3. Load

Each must be:
- clean
- properly seated
- properly torqued

# ================================
# SECTION — Anritsu Measurement Meaning / Acceptance Rules
# ================================

## Return Loss Power Reflection Reference

- 20 dB Return Loss ≈ 1% reflected power
- 10 dB Return Loss ≈ 10% reflected power

Interpretation:
- Higher return loss dB value is better
- Lower return loss dB value is worse

---

## Typical VSWR Reference

- 1:1 VSWR = perfect match
- Approximately 1.43:1 VSWR ≈ 15 dB Return Loss

---

## Pass / Fail Rule

For Return Loss and VSWR:
- Pass only if the entire sweep remains below the carrier limit line
- Fail if any portion of the trace touches or exceeds the limit line

---

## Standard Line Sweep Measurement Types

Required line sweep measurements:
- Return Loss
- Cable Loss
- Distance-To-Fault

Definitions:
- Return Loss = System Sweep
- Cable Loss = Cable Loss Sweep
- DTF = Load Sweep

## Measurement Philosophy

Measurements are not just numbers.

They represent:
- energy transfer efficiency
- system performance
- RF behavior across frequency

---

## Pass/Fail Is Strict

A sweep passes only if:
- the entire trace meets the requirement

A single failure point:
→ fails the entire test

---

## Reflection vs Loss

Two main failure types:

Reflection (more common):
- caused by impedance mismatch

Insertion loss (less common):
- caused by energy loss in the system

ARIA must distinguish between these.