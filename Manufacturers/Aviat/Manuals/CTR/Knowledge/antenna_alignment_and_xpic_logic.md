# CTR — Antenna Alignment and XPIC Logic

## PURPOSE

This file teaches ARIA how CTR antenna alignment, RSSI/RSL validation, protected-link alignment, CCDP/XPIC alignment, and main-beam verification work.

ARIA must use this file when supporting:
- antenna alignment
- low RSL
- poor XPD
- XPIC instability
- RFC2544 failures involving RF/XPIC suspicion
- protected radio alignment
- space diversity alignment
- side-lobe misalignment
- unexplained BER or throughput failure after install

---

## ALIGNMENT PREREQUISITES

Before antenna alignment:

- ODUs/RFUs must be powered at both ends
- Tx and Rx frequencies must be correctly configured
- Tx power must be correctly configured
- Tx mute must be disabled
- ATPC should be disabled during alignment

If frequency or power is wrong, the radio may interfere with nearby links.

---

## SIGNAL MEASUREMENT METHODS

CTR supports two alignment measurements:

1. RSL in CTR Portal
2. RSSI voltage at the ODU or IRU RFU

RSL is viewed from:

CTR Portal > Radio Link Performance

RSSI is measured with a voltmeter at:
- ODU BNC connector
- IRU 600 RFU front-panel probe points

---

## RSSI TO RSL CONVERSION

RSSI voltage directly maps to RSL.

- 0.25 Vdc = -10 dBm
- 0.50 Vdc = -20 dBm
- 0.75 Vdc = -30 dBm
- 1.00 Vdc = -40 dBm
- 1.25 Vdc = -50 dBm
- 1.50 Vdc = -60 dBm
- 1.75 Vdc = -70 dBm
- 2.00 Vdc = -80 dBm
- 2.25 Vdc = -90 dBm
- 2.50 Vdc = -100 dBm

Important:
- Lower RSSI voltage means stronger receive level.
- After measurement, replace the ODU BNC weatherproof cap.

---

## RSL VALIDATION RULES

Measured RSL must be compared against the expected RSL from the installation datapack.

Expected tolerance:
- ±2 dB from -40 to -70 dBm under normal temperature range
- ±4 dB across wider operating range

If measured RSL is more than 4 dB below expected:
- verify path survey
- verify path calculations
- verify antenna alignment

If measured RSL differs from expected by 20 dB or more:
- suspect side-lobe alignment
- suspect polarization mismatch

---

## INTERFERENCE CHECK

The RSSI filter bandwidth is approximately 56 MHz.

Because of this, adjacent channel energy may affect RSL/RSSI readings.

ARIA must know:
- RSL/RSSI may include interference
- ATPC can react incorrectly if interference affects RSL
- ATPC should not be enabled during alignment
- For co-channel XPIC operation with measurable adjacent channel RSL, ATPC should not be used

Interference check:
- mute the far-end transmitter
- observe local RSL/RSSI
- remaining signal may indicate interference

---

## STANDARD ANTENNA ALIGNMENT FLOW

1. Adjust azimuth for maximum RSL/RSSI
2. Tighten azimuth hardware while confirming signal does not drop
3. Adjust elevation for maximum RSL/RSSI
4. Tighten elevation hardware while confirming signal does not drop
5. Repeat at far end
6. Record final RSL/RSSI values

ARIA must remind techs:
- final tightening can shift alignment
- record readings after tightening, not before

---

## PROTECTED LINK ALIGNMENT

Protected links require additional care because transmitter switching can confuse alignment results.

### Hot Standby

For hot-standby links:
- one transceiver transmits
- both receivers can receive

If unequal-loss couplers are used:
- lock the low-loss side as Tx online during alignment

Path:
CTR Portal > Radio Link Protection Diagnostics

After alignment:
- remove protection locks

---

### Space Diversity

For space diversity:
- primary and secondary antennas must both be aligned
- top antenna is normally primary
- lower antenna is normally secondary

Critical rule:
- do not disturb the primary antenna while aligning the secondary path

After alignment:
- lock secondary Tx online
- confirm RSL/RSSI matches primary readings within about 2 dB
- remove locks after completion

---

### Frequency Diversity

Frequency diversity links operate independently from a radio-path perspective.

For equal-loss coupler systems:
- standard alignment procedure is normally sufficient
- protected locks are usually not needed

---

## CCDP / XPIC CORE CONCEPT

CCDP XPIC links use two polarizations on the same channel:
- vertical
- horizontal

XPIC depends on proper separation between the two polarized signals.

The key measurement is XPD:
Cross-Polarization Discrimination

Minimum acceptable XPD:
- 25 dB

Preferred / typical:
- 30 dB or better, depending on antenna capability

If XPD is poor:
- XPIC performance degrades
- BER can increase
- throughput tests can fail
- RFC2544 may fail even when RSL appears acceptable

---

## XPIC CONFIGURATION REQUIREMENTS

For XPIC links:

- frequency must be identical
- Tx power must be identical
- bandwidth must match
- modulation must match
- ATPC must not be used
- ODUs must be from the same sub-band
- protected XPIC should use equal-loss couplers

Unequal-loss couplers reduce XPD and should not be used for protected XPIC unless specifically designed and validated.

---

## RACx2 PORT POLARITY RULE

For RACx2:

- left-side SMA connector = vertical
- right-side SMA connector = horizontal

ARIA must treat swapped V/H cabling as a possible root cause for:
- poor XPD
- XPIC failure
- bad BER
- failed throughput testing
- unstable RFC2544 results

---

## XPD MEASUREMENT METHODS

XPD can be checked in:

CTR Portal > Radio Link Performance

Alternative:
CTR Portal > Radio Link Diagnostics > XPD on BNC

When XPD on BNC is enabled:
- RSSI output is replaced by XPD output
- conversion is 1:20
- example: 1.5 V = 30 dB XPD

---

## DUAL-POLARIZED ANTENNA ALIGNMENT FLOW

1. Confirm feedhead skew using spirit level
2. Align antennas using only one feed, V or H
3. Power up both V and H links
4. Confirm all links are normal and alarm-free
5. Confirm Tx power values are within about 1 dB
6. Confirm RSL values are within about 2 dB
7. Measure XPD
8. If XPD is low, optimize feedhead or XDM skew
9. Record final RSL and XPD

---

## FEEDHEAD / XDM SKEW RULE

Only one antenna should be treated as the reference antenna.

Do not adjust both ends repeatedly.

Reason:
- adjusting both sides creates progressive misalignment
- XPD optimization becomes unstable
- results become difficult to interpret

ARIA should guide:
- select one reference antenna
- leave it fixed
- adjust the opposite end only

---

## XDM ALIGNMENT RULE

For Aviat Edge-series antennas using XDM:

- check XDM vertical alignment with spirit level
- slotted holes allow about 8 degrees of movement
- if insufficient, adjust antenna pole mount
- tighten while confirming XPD does not change

---

## XPD OPTIMIZATION RULE

When optimizing XPD:

- rotate feedhead or XDM slowly
- performance screen updates about every 1.5 seconds
- XPD peak may be sharp
- final value should keep the lowest readings above 25 dB
- worst two readings should ideally be within 2 dB

If XPD changes during tightening:
- fastening shifted the feedhead/XDM
- recheck alignment

---

## WARNING ABOUT FALSE XPD READINGS

A spurious XPD reading around 50 dB may appear during major misalignment.

ARIA must not trust impossible XPD values.

Validation:
- XPD should not exceed the antenna specification
- a false high reading may occur over a very narrow angle

---

## PROTECTED XPIC RULES

If XPIC is protected:
- both V and H links must be protected

If only one co-channel link is protected:
- XPIC cross-connect failure can cause both V and H receive streams to error

For hot standby protected XPIC:
- use equal-loss combiners
- lock Tx online during alignment
- remove locks after alignment

---

## SPACE DIVERSITY XPIC LOGIC

For CCDP space diversity:

- top antenna normally connects to primary RACx2
- lower antenna normally connects to secondary RACx2

All antennas must be checked for:
- pan
- tilt
- skew
- XPD

Alignment must be performed in a controlled order.

ARIA must prevent the tech from moving the reference antenna.

---

## MAIN BEAM VS SIDE LOBE

Antenna alignment must be on the main beam, not a side lobe.

Side-lobe alignment can look valid at first but causes poor link margin and bad performance.

Indicators of side-lobe alignment:
- RSL is much lower than expected
- measured level is 20–25 dB below expected main beam
- signal peaks are misleading
- performance is unstable

Rule:
If RSL is 20 dB or more worse than expected:
- suspect side lobe
- verify main beam before deeper troubleshooting

---

## MAIN BEAM TRACKING RULE

If alignment sweep shows two side-lobe peaks:
- set azimuth midway between them
- adjust elevation for maximum signal

If side-lobe peaks merge and appear like one peak:
- do not assume it is the main beam
- re-sweep carefully in both azimuth and elevation

---

## FIELD FAILURE PATTERNS

### RFC2544 Fails on XPIC Link

Possible causes:
- poor XPD
- V/H cabling mismatch
- XPIC cable issue
- side-lobe alignment
- skew misalignment
- ATPC enabled incorrectly
- mismatched Tx power
- mismatched bandwidth/modulation
- ODUs from different sub-bands

ARIA must not assume Ethernet/service failure until RF/XPD is validated.

---

### Good RSL but Bad Throughput

Possible causes:
- poor XPD
- interference
- BER
- side-lobe alignment
- polarization mismatch
- XPIC path issue

---

### XPD Low but RSL Good

Likely causes:
- feedhead skew
- XDM skew
- V/H feed mismatch
- antenna not level
- incorrect reference antenna adjustment

---

### One Polarization Performs Worse

Likely causes:
- wrong RACx2 port assignment
- bad cable
- ODU issue
- feed alignment issue
- path-specific fading
- polarization mismatch

---

## ARIA TROUBLESHOOTING BEHAVIOR

When XPIC or alignment is suspected, ARIA must ask for:

1. RSL V and H
2. XPD V and H
3. Tx power V and H
4. BER / errored seconds
5. Whether ATPC is enabled
6. Whether this is protected or unprotected XPIC
7. Whether V/H cabling has been verified
8. Whether measured RSL matches datapack expectation
9. Whether alignment was verified on main beam
10. Whether feedhead/XDM skew was optimized

ARIA must guide one step at a time.

---

## CRITICAL DO-NOT-GUESS RULE

ARIA must not guess whether an XPIC cable is bad.

She must separate:
- alignment problem
- XPD problem
- cabling problem
- configuration problem
- ODU/RAC problem

before recommending replacement.

---

## SOURCE

CTR 8500-8300 Installation Guide  
Chapter 6 — Antenna Alignment