# ================================
# SECTION — Anritsu S820E Line Sweep Workflow
# ================================

## Purpose
Guide technicians through proper Anritsu Site Master S820E line sweep testing.

## Workflow Sequence
1. Confirm test objective
2. Select correct measurement mode
3. Select correct test type
4. Set frequency range
5. Set line type
6. Set distance range
7. Set data points
8. Select windowing
9. Calibrate
10. Connect DUT
11. Run sweep
12. Set markers / limits
13. Save result
14. Interpret failures

---

## Step Details

### 1. Confirm Test Objective

ARIA must ask:
- Are we performing a system sweep or load sweep?
- Are we testing with the antenna connected?
- Is a load adapter installed at the top of the waveguide?
- Are we looking for return loss, cable loss, or fault location?

---

### 2. Select Measurement Mode

Use:
Menu > Cable-Antenna Analyzer Advanced Mode

Do not use Classic Mode unless specifically required.

---

### 3. Select Measurement Type

For system return loss:
Measurement > Return Loss

For VSWR:
Measurement > VSWR

For fault location:
Measurement > DTF Return Loss

For cable loss:
Measurement > Cable Loss

---

### 4. Set Frequency Range

Use:
Freq/Dist > Frequency > Start Frequency
Freq/Dist > Frequency > Stop Frequency

Braxon field rule:
- Start = 50 MHz below lowest operating frequency
- Stop = 50 MHz above highest operating frequency

Do NOT use the entire band unless specifically required.

Reason:
- Span affects DTF resolution.
- Too wide or incorrectly chosen span can reduce usable distance behavior and distort field interpretation.

---

### 5. Set Line Type

Use:
Freq/Dist > DTF Setup > DUT Line Type

Select:
- Coax, if testing coax
- WG, if testing waveguide

If coax:
- select cable from Cable List, or manually enter propagation velocity and cable loss

If waveguide:
- select waveguide from Waveguide List, or manually enter cutoff frequency and waveguide loss

---

### 6. Set Distance Range

Use:
Freq/Dist > Distance

Set:
- Start Distance
- Stop Distance

Stop distance must cover the physical line length.

If stop distance exceeds DMax:
- increase data points, or
- reduce frequency span

---

### 7. Set Data Points

Use:
Sweep > Data Points

Available:
- 130
- 259
- 517
- 1033
- 2065

Field preference:
- Use higher data points when longer distance coverage is needed.
- Set 2065 before calibration if it will be needed.

---

### 8. Select Windowing

Use:
Freq/Dist > DTF Setup > Windowing

Options:
- Rectangular
- Nominal Side Lobe
- Low Side Lobe
- Minimum Side Lobe

Recommended default:
- Nominal Side Lobe for most field sweeps

Use Rectangular when:
- multiple faults may be close together
- distance resolution is more important than side-lobe suppression

---

### 9. Calibrate

Use:
Calibration > Start Calibration

Calibration must be performed:
- before measurements
- under same test conditions
- with correct frequency range
- with correct data points
- with correct source power / IFBW where applicable
- at the end of the test port cable and adapters

---

### 10. Connect Device Under Test

For system sweep:
- connect to feed line / waveguide with antenna still connected

For load sweep:
- disconnect antenna
- install load adapter / precision load at top of waveguide or line

For cable loss:
- install short at end of transmission line

---

### 11. Run Sweep

Use:
Sweep > Run/Hold

Confirm:
- trace is stable
- calibration status is valid
- frequency range is correct
- line type is correct
- distance range is correct

---

### 12. Set Markers

Use:
Marker > Marker Setup

Use markers to identify:
- connector locations
- waveguide bends
- tower ground points
- antenna/load location
- fault spikes

Marker to Peak may be used to locate strongest reflection.

---

### 13. Set Limits

Use:
Limit > Limit State

Use limits for:
- pass/fail display
- visual comparison
- carrier acceptance requirements

---

### 14. Save Measurement

Use:
File > Save

Save as:
- Measurement file for reporting and later review
- Screen shot if visual proof is needed
- Setup file if the same test configuration will be reused

Measurement files contain both measurement data and setup data.

# ================================
# SECTION — DTF Aid Setup & Adjustment Workflow
# ================================

## Purpose
Guide the technician in using DTF Aid to correctly configure frequency span, data points, and distance range before running a sweep.

## Workflow Sequence
1. Open DTF Aid
2. Review current setup values
3. Compare Max Usable Distance to actual line length
4. Adjust frequency span or data points
5. Recalibrate after changes
6. Verify distance coverage before running sweep

---

## Step Details

### 1. Open DTF Aid
- Navigate to:
  Freq/Dist > Distance > DTF Aid

---

### 2. Review DTF Info

Check:
- Start Distance (D1)
- Stop Distance (D2)
- Start Frequency (F1)
- Stop Frequency (F2)
- Data Points
- Frequency Span
- Max Usable Distance

---

### 3. Compare Max Usable Distance

- Compare Max Usable Distance to:
  - tower height
  - total waveguide length
  - expected physical path

If Max Usable Distance < actual line length:
→ sweep will NOT cover full system

---

### 4. Adjust Setup

To increase Max Usable Distance:
- Increase data points
- OR reduce frequency span

To improve distance resolution:
- Increase frequency span

---

### 5. Recalibrate

ANY change to:
- frequency span
- data points

REQUIRES recalibration before testing

---

### 6. Verify Before Sweep

- Confirm Max Usable Distance ≥ full line length
- Confirm resolution is acceptable
- Confirm span matches RF frequencies (±50 MHz rule)

# ================================
# SECTION — Anritsu Calibration Workflow (CAA Mode)
# ================================

## Purpose
Guide the technician through proper calibration of the Anritsu S820E before performing measurements.

## Workflow Sequence
1. Confirm calibration requirement
2. Set measurement configuration BEFORE calibration
3. Select calibration type
4. Connect calibration standards
5. Perform calibration sequence
6. Verify calibration status
7. Proceed to measurement

---

## Step Details

### 1. Confirm Calibration Requirement

Calibration is REQUIRED before:
- return loss measurements
- VSWR measurements
- DTF measurements
- cable loss measurements

---

### 2. Set Configuration BEFORE Calibration

Calibration must be performed AFTER setting:
- frequency range (start/stop)
- data points
- line type (coax or waveguide)
- DTF setup (if applicable)

If any of these change after calibration:
→ calibration becomes INVALID

---

### 3. Select Calibration Type

Use:
Calibration > Start Calibration

Select appropriate calibration:
- Open/Short/Load (OSL)
- Load only (for some quick setups)
- Waveguide calibration if applicable

---

### 4. Connect Calibration Standards

Calibration must be performed at:
- the END of the test port cable
- including ALL adapters that will remain in the test path

Sequence:
1. Connect OPEN standard
2. Connect SHORT standard
3. Connect LOAD standard

---

### 5. Perform Calibration

Follow prompts on screen:
- instrument will request each standard in order
- confirm stable connection before accepting each step

---

### 6. Verify Calibration Status

Check:
Calibration > Cal Info

Confirm:
- calibration is ON
- calibration matches current setup
- no warnings present

---

### 7. Proceed to Measurement

Only proceed if:
- calibration is valid
- setup has NOT changed

# ================================
# SECTION — Standard Anritsu Line Sweep Measurement Flow
# ================================

## Purpose
Guide ARIA in choosing the correct sweep type based on what the technician needs to prove.

## Workflow Sequence

1. Run Return Loss / VSWR System Sweep
2. If system sweep passes, save result
3. If system sweep fails, run DTF Load Sweep
4. Use DTF to locate fault
5. Run Cable Loss Sweep when attenuation/insertion loss must be verified

---

## Step Details

### 1. Return Loss — System Sweep

Use when:
- antenna is connected
- full system performance must be verified

Purpose:
- measures aggregate return loss of the entire system
- shows how all components interact together

---

### 2. DTF — Load Sweep

Use when:
- Return Loss / VSWR fails
- technician needs to locate the fault

Setup:
- disconnect antenna
- install 50 ohm precision load at end of line/waveguide

Purpose:
- identifies fault location in transmission path
- isolates feedline components without antenna behavior

---

### 3. Cable Loss — Cable Loss Sweep

Use when:
- attenuation/insertion loss must be verified
- new installation or main transmission line replacement is being tested

Setup:
- short connected at end of transmission line

Important:
- cable loss cannot be measured with antenna connected

# ================================
# SECTION — DTF Procedure Logic
# ================================

## Purpose
Guide a technician through what DTF is doing and how the test must be carried out.

## Workflow Sequence
1. Define DTF purpose
2. Decide whether measuring length or troubleshooting
3. Select termination type
4. Configure frequency range
5. Confirm line type
6. Calibrate
7. Connect DUT
8. Run DTF sweep
9. Compare trace to limit/spec
10. Use markers to locate reflection events

---

## Step Details

### 1. Define DTF Purpose

ARIA must ask:
- Are we measuring total line length?
- Are we troubleshooting a failed sweep?
- Are we locating a reflection?
- Are we testing with antenna connected or load connected?

---

### 2. Measuring Cable / Waveguide Length

If the goal is measuring length:
- open or short may be connected at the far end
- the end-of-line peak should appear clearly
- peak should typically be around 0 dB to 5 dB

---

### 3. Troubleshooting Reflections

If the goal is troubleshooting:
- do NOT use open/short
- install a 50 ohm load at the end of the line/waveguide

Reason:
- open/short reflects most RF energy
- connector values can be misread
- good connectors can appear bad

---

### 4. Configure Frequency Range

Use site-specific operating frequencies.

Braxon field rule:
- start 50 MHz below lowest operating RF frequency
- stop 50 MHz above highest operating RF frequency

Do not sweep an entire microwave band by default.

---

### 5. Confirm Frequency-Selective Devices

Ask:
- Is there a TMA in the path?
- Is there a duplexer?
- Is there a filter?
- Is there a quarter-wave lightning arrestor?

If yes:
- frequency range must be chosen carefully
- wrong frequency range can distort DTF distance results

---

### 6. Run the Sweep

After calibration and connection:
- run DTF Return Loss or DTF VSWR
- verify trace stability
- verify limit line if applicable

---

### 7. Interpret Correctly

ARIA must interpret DTF as:
- location of reflections
- not automatic component failure

If reflection exceeds limit:
- use marker distance
- compare to physical line layout
- ask technician what exists at that distance