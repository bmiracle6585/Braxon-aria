# ================================
# SECTION — VIAVI DEFAULTS
# ================================

## Link Requirements

- Signal Present → required
- Sync Acquired → required
- Link Active → required

---

## Traffic Expectations

- Rx Mbps ≈ CIR
- Lost Frames = 0

---

## RFC2544 Pass Conditions

- Throughput ≥ CIR
- Frame Loss = 0
- Latency within threshold
- Jitter within threshold

---

## Optical Checks

- SFP wavelength must match circuit
- Tx/Rx levels must be within acceptable range

# ================================
# SECTION — VIAVI Interpretation Required Values
# ================================

## Minimum Valid Link Indicators

Required before traffic interpretation:
- Signal Present = green
- Sync Acquired = green
- Link Active = green

---

## Traffic Passing Expectations

- Rx Mbps should be approximately equal to CIR
- Lost Frames must equal 0
- Summary should show ALL SUMMARY RESULTS OK during manual traffic test

---

## RFC2544 Passing Expectations

RFC2544 passes only when selected tests pass or complete as expected:
- Throughput
- Latency
- Frame Loss
- Packet Jitter

---

## Frame Size Rules

Standard selected RFC2544 frame lengths:
- 1st frame length
- 4th frame length
- 8th frame length

If MTU is greater than:
- 1518 without VLAN
- 1522 with VLAN

then the MTU frame length must also be entered and selected.

---

## Copper Rule

1000 Mbps electrical requires auto-negotiation ON.

---

## Optical Rule

SFP must match:
- required wavelength
- required data rate

Optical attenuators may be required if receive levels are too high.

# ================================
# SECTION — End-to-End RFC2544 Required Validation Rules
# ================================

## RFC2544 Is Valid Only If These Are True

Before interpreting RFC2544 failure, confirm:

1. VIAVI interface is correct
2. Signal Present / Sync / Link are valid
3. VLAN matches the radio configuration
4. Local radio port is up
5. Far-end radio port is up
6. Loopback or far-end tester is connected and active
7. CIR/load matches the intended service rate
8. Radio current capacity is greater than or equal to test load
9. Modulation is performing at expected level
10. No RF alarms or excessive errors are present during test

---

## Capacity Rule

Configured test load must not exceed actual available radio capacity.

If:

VIAVI Load > Current Radio Capacity

then:

RFC2544 failure is expected.

---

## Modulation Rule

Expected modulation must be compared to current modulation.

If current modulation is lower than expected:
- available capacity may be reduced
- throughput may fail
- frame loss may occur under load

---

## VLAN Rule

VIAVI VLAN behavior must match radio VLAN behavior.

Compare:
- tagged vs untagged
- VLAN ID
- PVID/native VLAN
- allowed VLAN list
- far-end egress behavior

---

## Loopback Rule

RFC2544 requires a valid return path.

Valid return path may be:
- far-end VIAVI tester
- VIAVI-compatible loopback
- LLB / MAC swap
- hard loop, if applicable

No return path:
→ RFC2544 result is invalid.