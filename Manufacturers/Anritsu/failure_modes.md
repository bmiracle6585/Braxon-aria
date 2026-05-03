# ================================
# SECTION — Anritsu Line Sweep Failure Modes
# ================================

## Failure Mode: Wrong Sweep Type

### Pattern
Technician performs a system sweep when a load sweep is needed, or performs a load sweep when antenna/system behavior is being evaluated.

### Symptoms
- confusing return loss behavior
- antenna blamed for feed line problem
- feed line blamed for antenna behavior
- failed acceptance test interpretation

### ARIA Checks
- Is the antenna connected?
- Is a load adapter installed?
- Are we testing full system behavior or isolating the line?

---

## Failure Mode: Incorrect Frequency Span

### Pattern
Technician sweeps the entire microwave band instead of the operating RF window.

### Symptoms
- poor or misleading DTF resolution
- limited usable line length
- fault locations harder to interpret
- trace appears less useful for field diagnosis

### ARIA Checks
- What is the lowest operating RF frequency?
- What is the highest operating RF frequency?
- Was sweep set 50 MHz below low frequency and 50 MHz above high frequency?
- Was a full band accidentally selected?

---

## Failure Mode: Wrong Line Type

### Pattern
Coax selected when testing waveguide, or waveguide selected incorrectly.

### Symptoms
- incorrect fault distance
- incorrect amplitude interpretation
- marker locations do not match physical tower/waveguide layout

### ARIA Checks
- Is DUT Line Type set to Coax or WG correctly?
- Was the correct waveguide selected?
- Was cutoff frequency correct?
- Was waveguide loss entered correctly?

---

## Failure Mode: Wrong Cable / Waveguide Parameters

### Pattern
Incorrect propagation velocity, cable loss, cutoff frequency, or waveguide loss.

### Symptoms
- DTF distance does not match physical location
- fault appears before or after real connector/bend
- amplitude appears misleading

### ARIA Checks
- Verify selected cable/waveguide list item
- If set to NONE, verify manually entered values
- Confirm main feeder/waveguide type

---

## Failure Mode: Calibration Invalid or Missing

### Pattern
Measurement taken without valid calibration or after changing setup.

### Symptoms
- unreliable trace
- calibration status off
- inconsistent measurements
- false pass/fail

### ARIA Checks
- Is calibration status OK?
- Did frequency span change after calibration?
- Did data points change to 2065 after calibration?
- Did temperature drift more than ±10 °C?
- Was calibration performed at end of test cable/adapters?

---

## Failure Mode: Bad Test Port Cable

### Pattern
Phase-stable test cable is damaged, kinked, stretched, loose, or not calibrated out.

### Symptoms
- erratic readings
- inconsistent sweep results
- false connector failures
- unstable trace while moving cable

### ARIA Checks
- Was a phase-stable cable used?
- Was cable visually inspected?
- Does moving the test cable change the trace?
- Was the test cable included in calibration?

---

## Failure Mode: Open/Short Used for Troubleshooting DTF

### Pattern
Open or short is used at the end of the line during fault troubleshooting instead of a 50 ohm load.

### Symptoms
- excessive reflection masks connector faults
- good connector may look bad
- true connector value misinterpreted

### ARIA Rule
Open/short is acceptable for measuring cable length.
A 50 ohm load is preferred for troubleshooting DTF faults.

---

## Failure Mode: Spike Near Connector / Middle of Line

### Pattern
DTF spike appears around the connector or near the middle of the line.

### ARIA Questions
- Was the connector recently made?
- Was the waveguide thoroughly cleaned after making the connector?
- Were shavings, debris, or contamination removed?
- Was the connector inspected before testing?
- Was the connector properly torqued?
- Was the load adapter clean?

### Likely Causes
- debris inside waveguide
- poorly made connector
- dirty connector face
- damaged adapter
- poor mechanical transition

---

## Failure Mode: Spike Near Bend, Ground, or Tower Route

### Pattern
DTF spike aligns with a bend, waveguide clamp, ground kit, tower transition, or physical stress point.

### ARIA Questions
- Is there a waveguide bend at that distance?
- Is there a ground kit near that distance?
- Is the waveguide compressed, dented, or over-tightened?
- Is the line stressed at the tower transition?
- Is there water ingress or physical damage?
- Did the installer over-bend or deform the waveguide?

### Likely Causes
- bend damage
- compression
- grounding clamp issue
- mechanical deformation
- moisture intrusion
- tower routing stress

---

## Failure Mode: RF Interference During Sweep

### Pattern
Nearby transmitter affects measurement.

### Symptoms
- trace looks better or worse than reality
- inconsistent results
- strange ripple or unstable measurement

### ARIA Checks
- Is RF Immunity set to High?
- Are nearby transmitters active?
- Is the test environment co-located with other RF systems?

---

## Failure Mode: Stop Distance Exceeds DMax

### Pattern
Technician enters a stop distance longer than the instrument can analyze with current setup.

### Symptoms
- desired line length cannot be displayed
- DTF Aid indicates insufficient Max Usable Distance

### ARIA Fix
- increase data points, or
- reduce frequency span

---

## Failure Mode: Over-Smoothing

### Pattern
Smoothing hides real defects.

### Symptoms
- trace looks cleaner than actual line condition
- small faults disappear
- acceptance result may be misleading

### ARIA Rule
Use smoothing carefully.
Do not smooth away real ripple or fault signatures.

---

## Failure Mode: File Not Saved Correctly

### Pattern
Measurement completed but not properly saved/exported.

### Symptoms
- no proof of test
- missing trace
- wrong file type
- no setup data retained

### ARIA Checks
- Was File > Save used?
- Was file type Measurement selected?
- Was USB/internal location correct?
- Was naming convention followed?

# ================================
# SECTION — DTF Aid / Distance Failures
# ================================

## Failure Mode: Max Distance Too Short

### Pattern
Sweep does not reach antenna or top of tower.

### Symptoms
- trace cuts off early
- cannot see end of line
- missing antenna reflection

### Cause
- frequency span too wide
- data points too low

### ARIA Fix
- increase data points
- OR reduce frequency span
- recalibrate

---

## Failure Mode: Fault Distance Incorrect

### Pattern
Spike does not match physical location.

### Symptoms
- connector spike appears at wrong distance
- bend/ground spike not aligned with tower structure

### Cause
- incorrect frequency span
- incorrect data points
- incorrect line parameters

---

## Failure Mode: Poor Resolution (Merged Spikes)

### Pattern
Multiple faults appear as one.

### Symptoms
- connectors and bends not distinguishable
- wide, unclear peaks

### Cause
- frequency span too narrow

### ARIA Fix
- increase frequency span

---

## Failure Mode: Over-Expanded Frequency Range

### Pattern
Full band sweep used (6 GHz, 11 GHz, etc.)

### Symptoms
- poor usable distance
- confusing trace behavior
- reduced diagnostic accuracy

### ARIA Fix
- apply ±50 MHz rule around operating frequencies

# ================================
# SECTION — Calibration Failure Modes
# ================================

## Failure Mode: Calibration Performed Before Setup

### Pattern
Tech calibrates, then changes frequency or data points.

### Symptoms
- incorrect DTF distance
- inconsistent trace
- false failures

### ARIA Fix
- recalibrate AFTER final setup

---

## Failure Mode: Calibration Not at End of Cable

### Pattern
Calibration done at instrument port instead of end of test cable.

### Symptoms
- entire trace shifted
- false reflections
- incorrect return loss

### ARIA Fix
- recalibrate at end of test cable including adapters

---

## Failure Mode: Dirty Calibration Standards

### Pattern
Open/Short/Load connectors contaminated.

### Symptoms
- poor return loss
- unstable calibration
- false spikes

### ARIA Questions
- were cal standards cleaned?
- were connectors inspected?

---

## Failure Mode: Loose Calibration Connection

### Pattern
Standard not properly torqued.

### Symptoms
- inconsistent readings
- fluctuating trace

---

## Failure Mode: Bad Test Cable Included in Calibration

### Pattern
Damaged cable calibrated in.

### Symptoms
- entire measurement appears degraded
- real faults hidden or distorted

---

## Failure Mode: Temperature Drift

### Pattern
Calibration done cold, measurement done warm.

### Symptoms
- drift in trace
- inconsistent results

---

## Failure Mode: Calibration Disabled

### Pattern
Calibration accidentally turned OFF.

### Symptoms
- raw, uncorrected measurement
- significantly degraded accuracy

# ================================
# SECTION — Measurement Review Failure Logic
# ================================

## Failure Mode: Treating System Sweep Failure as Antenna Failure

### Pattern
Return Loss fails with antenna connected.

### ARIA Rule
Do not immediately blame antenna.

Possible causes:
- connector
- waveguide damage
- water ingress
- over-torque
- jumper issue
- antenna mismatch

Next step:
- run DTF load sweep to locate reflection source

---

## Failure Mode: Cable Loss Attempted With Antenna Connected

### Pattern
Technician tries to measure cable loss while antenna is connected.

### ARIA Rule
Cable Loss cannot be measured with antenna connected.

Correct setup:
- short or open at cable/waveguide end depending test requirement

---

## Failure Mode: Misreading Return Loss Direction

### Pattern
Technician thinks lower return loss is better.

### ARIA Rule
Higher dB return loss is better.
Lower dB return loss is worse.

Example:
- 20 dB is better than 10 dB
- 10 dB reflects about 10% power
- 20 dB reflects about 1% power

---

## Failure Mode: Calling a Partial Pass Good

### Pattern
Most of the sweep is below the limit line, but one section fails.

### ARIA Rule
If any part of the trace touches or exceeds the limit line:
→ the sweep fails.

# ================================
# SECTION — DTF Procedure / Misuse Failure Modes
# ================================

## Failure Mode: Treating DTF as Automatic Diagnosis

### Pattern
Technician sees a spike and assumes that component has failed.

### ARIA Rule
DTF only shows reflection versus distance.

A spike becomes actionable when:
- it exceeds the required limit/spec
- the test setup is valid
- the distance aligns with a physical component or damage point

---

## Failure Mode: Using Open/Short for Troubleshooting

### Pattern
Open or short is installed at the far end during troubleshooting.

### Symptoms
- connector values misleading
- good connector may appear bad
- true reflection source may be masked

### Correct Use
Open/short is acceptable for measuring line length.

### Correct Troubleshooting Setup
Use a 50 ohm load.

---

## Failure Mode: Antenna Used When Feed Path Should Be Isolated

### Pattern
DTF is performed with antenna connected while trying to troubleshoot the line.

### Issue
Antenna impedance changes across frequency and can affect the trace.

### ARIA Fix
If isolating the line:
- remove antenna
- install load adapter / 50 ohm load
- perform load sweep

---

## Failure Mode: Frequency-Selective Device Distorts DTF

### Pattern
TMA, duplexer, filter, or quarter-wave lightning arrestor is in the path and sweep frequency is not selected correctly.

### Symptoms
- fault distance appears wrong
- trace behavior does not match physical layout
- DTF result is confusing

### ARIA Checks
- What frequency-selective devices are in the path?
- Was the sweep frequency range selected around the correct operating frequencies?