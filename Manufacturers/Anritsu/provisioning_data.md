# ================================
# SECTION — Anritsu S820E Line Sweep Test Data
# ================================

## Purpose
Collect all information required before ARIA guides a technician through Anritsu Site Master S820E line sweep testing.

## Required Test Inputs

### Test Type
- System sweep
- Load sweep
- Cable loss sweep
- DTF sweep
- Return Loss
- VSWR
- Cable Loss
- DTF Return Loss
- DTF VSWR

---

## Sweep Type Definitions

### System Sweep
A system sweep includes:
- transmission line
- waveguide
- connectors
- bends
- grounds
- antenna

Use when validating the full installed RF path including the antenna.

### Load Sweep
A load sweep removes the antenna from the test path.

A precision load / load adapter is installed at the top of the waveguide or transmission line.

Use when isolating:
- waveguide
- connectors
- bends
- grounding locations
- physical line problems

ARIA must know:
- System sweep includes antenna.
- Load sweep does NOT include antenna.
- Load sweep isolates the feed path.

---

## Frequency Range Inputs

Collect:
- Lowest licensed TX/RX frequency
- Highest licensed TX/RX frequency
- Required start frequency
- Required stop frequency

Braxon field rule:
- Do NOT sweep an entire microwave band unless specifically required.
- Do NOT use the whole 6 GHz, 11 GHz, or other full band as the sweep range.
- Start frequency should be 50 MHz below the lowest operating RF frequency.
- Stop frequency should be 50 MHz above the highest operating RF frequency.

Example:
- Lowest site frequency: 10.700 GHz
- Highest site frequency: 10.900 GHz
- Sweep start: 10.650 GHz
- Sweep stop: 10.950 GHz

Reason:
- Incorrectly large spans reduce distance resolution.
- Incorrectly large spans can limit useful line length / DMax.
- Sweep span must cover the real operating RF range without wasting resolution.

---

## DTF Inputs

Collect:
- Start distance
- Stop distance
- Estimated physical line length
- Tower height
- Waveguide route length
- Known bend locations
- Ground kit locations
- Connector locations
- Adapter locations
- Antenna / load location
- Expected fault locations

---

## Line Type Inputs

Collect:
- Coax or waveguide
- Cable type if coax
- Propagation velocity if custom coax
- Cable loss if custom coax
- Waveguide type if waveguide
- Waveguide cutoff frequency
- Waveguide loss

ARIA must verify the correct line type because incorrect propagation velocity or incorrect waveguide cutoff frequency causes inaccurate DTF distance results.

---

## Calibration Inputs

Collect:
- Calibration type required
- Cal line:
  - Coax
  - Waveguide
- DUT connector type
- Calibration kit used
- Test port cable used
- Whether phase-stable test cable is used
- Whether calibration was performed at the end of test cable/adapters

---

## Required Save / Documentation Inputs

Collect:
- Site name
- Hop name
- Radio side
- Polarization
- System sweep file name
- Load sweep file name
- Cable loss file name
- DTF file name
- Technician name
- Date/time
- GPS location if available
- Photos of setup if needed

# ================================
# SECTION — Calibration Inputs
# ================================

## Purpose
Define all inputs required for proper calibration.

---

## Required Calibration Data

### Measurement Setup Inputs
- Start frequency
- Stop frequency
- Data points
- Measurement type (Return Loss, DTF, etc.)
- Line type (Coax or Waveguide)

---

### Calibration Hardware Inputs
- Calibration kit type
- Connector type (N, K, etc.)
- Test port cable type
- Adapters used

---

### Calibration Location

Calibration must be performed at:
- the end of the test port cable
- including all adapters used during measurement

---

## Environmental Inputs

- Ambient temperature
- Instrument warm-up time
- Cable stability

---

## Validation Inputs

- Calibration status (ON/OFF)
- Calibration match to setup
- Calibration timestamp (if available)

# ================================
# SECTION — Line Sweep Measurement Selection Inputs
# ================================

## Purpose
Collect the information ARIA needs to choose the correct Anritsu sweep type.

## Required Inputs

- Is antenna connected?
- Is load connected?
- Is short/open connected?
- Are we proving full system performance?
- Are we locating a fault?
- Are we measuring insertion loss?
- Is this a new install?
- Is this a main transmission line replacement?
- Did Return Loss / VSWR already fail?
- What carrier limit line/spec applies?

---

## Sweep Selection Logic

If antenna is connected:
→ Return Loss / VSWR System Sweep

If antenna is removed and precision load is installed:
→ DTF Load Sweep

If short/open is installed:
→ Cable Loss Sweep

If system sweep fails:
→ run DTF to locate the fault

# ================================
# SECTION — DTF Procedure Required Inputs
# ================================

## Required Inputs Before DTF

ARIA must collect:

- Purpose of test:
  - measure length
  - troubleshoot fault
  - verify system
- Termination type:
  - antenna
  - 50 ohm load
  - open
  - short
- Is antenna connected?
- Is load adapter installed?
- Lowest operating frequency
- Highest operating frequency
- Line type:
  - coax
  - waveguide
- Physical line length
- Tower height
- Known connector locations
- Known bend locations
- Known ground locations
- Any frequency-selective devices in path:
  - TMA
  - duplexer
  - filter
  - quarter-wave lightning arrestor
- Carrier/spec limit line