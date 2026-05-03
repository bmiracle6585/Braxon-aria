# ================================
# SECTION — Cross-System Troubleshooting Model
# ================================

## Purpose
Connect radio, VLAN, VIAVI, loopback, RFC2544, and RF capacity into one troubleshooting model.

---

## Grand Troubleshooting Principle

ARIA must diagnose across the entire path, not within one device.

When a test fails, ARIA must ask:

1. Is the test set configured correctly?
2. Is the local physical connection up?
3. Is the local radio port up?
4. Is the VLAN correct on both the test set and radio?
5. Is the far-end port up?
6. Is the loopback active?
7. Is traffic returning?
8. Is the RF path healthy?
9. Is the radio modulation/capacity sufficient for the test load?
10. Which RFC2544 metric actually failed?

---

## Failure Domain Map

### Test Set Domain
- wrong test type
- wrong interface
- wrong VLAN
- wrong CIR
- wrong thresholds
- wrong frame sizes

### Local Physical Domain
- bad cable
- wrong SFP
- dirty fiber
- auto-neg mismatch
- no signal/sync/link

### Local Radio Domain
- port down
- LOS alarm
- VLAN mismatch
- wrong tagged/untagged behavior
- port errors

### RF Domain
- low RSL
- poor XPD
- BER
- degraded modulation
- reduced capacity
- ACM downgrade

### Far-End Domain
- far-end port LOS
- loopback missing
- wrong port
- wrong VLAN egress
- incompatible loopback

### Service Validation Domain
- throughput below CIR
- frame loss
- latency
- jitter
- threshold mismatch

---

## ARIA Required Behavior

ARIA must not answer from a single file.

For RFC2544 failures, ARIA must consult:
- VIAVI provisioning flow
- VIAVI required values
- radio VLAN logic
- port/cable logic
- RF/modulation logic
- failure modes
- operational insights