# ================================
# SECTION — VIAVI TEST WORKFLOW
# ================================

## Step 1 — L2 Traffic Bring-Up

Purpose:
- confirm link is active

Steps:
- select L2 Traffic test
- verify interface (SFP or copper)
- verify wavelength / speed
- set load to constant
- set bitrate to expected CIR
- turn laser ON (optical)
- confirm:
  - Signal Present
  - Sync Acquired
  - Link Active

---

## Step 2 — Loopback (if required)

Purpose:
- validate path when no far-end tester

Steps:
- configure interface (auto-neg must match circuit)
- verify speed/duplex
- enable LLB (line loopback)
- confirm:
  - link remains active
  - traffic is returned

---

## Step 3 — RFC2544 Testing

Purpose:
- validate service performance

Steps:
- configure VLAN (if required)
- set CIR (Committed Information Rate)
- select tests:
  - throughput
  - latency
  - frame loss
  - jitter
- configure frame sizes
- configure pass/fail thresholds
- run test
- verify all results pass

# ================================
# SECTION — VIAVI Interpretation Workflow
# ================================

## Purpose
Guide ARIA through result interpretation after a VIAVI test fails.

---

## Workflow Sequence

1. Confirm correct test type
2. Confirm interface state
3. Confirm traffic/loopback
4. Confirm configured CIR
5. Review failed metric
6. Review failed frame size
7. Map failure to likely layer
8. Recommend next verification

---

## Step Details

### 1. Confirm Correct Test Type

Ask:
- Is this L2 Traffic?
- Is this LLB / loopback?
- Is this RFC2544?

---

### 2. Confirm Interface State

Required indicators:
- Signal Present
- Sync Acquired
- Link Active

If any are missing:
→ troubleshoot physical/interface before traffic.

---

### 3. Confirm Loopback / Return Path

Before RFC2544:
- verify loopback is active
- verify traffic returns
- verify measured Rx Mbps exists

---

### 4. Confirm CIR

Check:
- load rate
- max bandwidth
- expected committed information rate

If CIR is wrong:
→ test result is invalid.

---

### 5. Identify Failed Metric

Possible failed metrics:
- throughput
- frame loss
- latency
- jitter

---

### 6. Identify Failed Frame Size

Ask:
- Did 64-byte fail?
- Did 512-byte fail?
- Did 1518-byte fail?
- Did MTU/jumbo frame fail?

---

### 7. Map Failure

Small frame issue:
→ packet rate / processing

Large frame issue:
→ MTU / jumbo / tagging

Throughput low, no loss:
→ shaping / rate config

Throughput low, loss present:
→ congestion / errors

Latency high:
→ queuing / path delay

Jitter high:
→ unstable delay / QoS

---

### 8. Recommend Next Verification

Depending on result:
- check VLAN
- check loopback
- check auto-neg/speed/duplex
- check CIR/service profile
- check optical levels
- check interface errors
- check RF if microwave path is involved

# ================================
# SECTION — End-to-End RFC2544 Troubleshooting Flow
# ================================

## Purpose
Guide ARIA through a complete RFC2544 failure investigation across VIAVI, radio Ethernet ports, VLANs, loopback, and RF capacity.

---

## Workflow Sequence

1. Confirm exact RFC2544 failure
2. Validate VIAVI setup
3. Validate local test set link
4. Validate local radio port
5. Validate VLAN on test set and radio
6. Validate far-end port / loopback
7. Validate RF link health
8. Validate modulation and available capacity
9. Compare configured test load to actual available capacity
10. Interpret failed RFC2544 metric

---

## Step Details

### 1. Confirm Exact RFC2544 Failure

ARIA must ask:
- Which RFC2544 subtest failed?
  - Throughput
  - Frame Loss
  - Latency
  - Jitter
- Which frame size failed?
- Did all frame sizes fail or only some?
- Did J-QuickCheck pass?
- Was a report generated?

---

### 2. Validate VIAVI Setup

Check:
- Correct test type selected
- Correct interface selected
- Correct speed selected
- Correct VLAN ID entered, if VLAN is used
- Correct CIR / Max Bandwidth entered
- Correct frame sizes selected
- Correct pass/fail thresholds entered
- Test started properly

Important:
If the test set is configured wrong, the RFC2544 result is invalid.

---

### 3. Validate Local Test Set Link

Check VIAVI indicators:
- Signal Present
- Sync Acquired
- Link Active
- Frame Detect
- Pattern Sync

If these are not valid:
→ do not troubleshoot RFC2544 yet.
Fix physical/test set link first.

---

### 4. Validate Local Radio Port

ARIA must ask:
- Is the VIAVI connected to the correct radio port?
- Is the local radio Ethernet port up?
- Is the port showing LOS?
- Is speed/duplex correct?
- Are there CRC/errors/drops on the port?
- Is the port administratively enabled?

If the local radio port is down or in alarm:
→ RFC2544 cannot pass.

---

### 5. Validate VLAN on Test Set and Radio

ARIA must compare:
- VIAVI VLAN encapsulation
- VIAVI VLAN ID
- radio port VLAN membership
- radio tagged/untagged behavior
- PVID/native VLAN
- trunk/allowed VLAN list

Critical question:
“Is the VLAN configured the same way on the VIAVI and the radio port?”

Examples:
- VIAVI sends VLAN 100 tagged, but radio expects untagged → fail
- VIAVI sends untagged, but radio port only admits tagged → fail
- Radio carries VLAN 100 locally but not across the link → fail
- Far-end radio does not egress VLAN correctly → fail

---

### 6. Validate Far-End Port and Loopback

ARIA must ask:
- What is plugged in at the far end?
- Is the far-end loopback connected to the correct port?
- Is the far-end radio port up?
- Is there LOS on the far-end port?
- Is LLB / loopback enabled?
- Is the loopback device compatible?
- Is MAC swap required?
- Is traffic returning to the test set?

If no loopback or no far-end return path:
→ RFC2544 fails even if RF is good.

---

### 7. Validate RF Link Health

Check:
- RSL
- XPD, if XPIC
- BER / errored seconds
- RF alarms
- ATPC state
- modulation state
- current capacity
- protection state

ARIA must separate:
- RF path is up
from:
- RF path can carry the configured RFC2544 load

---

### 8. Validate Modulation and Capacity

ARIA must ask:
- What modulation should the link be running?
- What modulation is it currently running?
- Has modulation degraded?
- What is the current radio capacity?
- Is ACM/adaptive modulation active?
- Is the test load higher than current capacity?

Example:
If link is designed for 4096QAM but currently running 1024QAM:
- available throughput may be lower
- RFC2544 throughput may fail
- frame loss may occur if test load exceeds current capacity

---

### 9. Compare Test Load to Actual Available Capacity

ARIA must compare:

VIAVI configured load / CIR
vs
actual available radio capacity

If VIAVI load is higher than radio can currently carry:
→ throughput or frame loss failure is expected.

This is not necessarily a VIAVI failure.
This may indicate:
- degraded modulation
- reduced channel capacity
- RF fade
- ACM downgrade
- incorrect expected CIR
- test load configured too high

---

### 10. Interpret Failed Metric

If throughput fails but no loss:
→ suspect shaping, wrong CIR, rate limiting, or test configured too high.

If frame loss fails:
→ suspect overload, errors, RF degradation, VLAN/QoS drops, or capacity mismatch.

If latency fails:
→ suspect buffering, queuing, congestion, or protection/routing delay.

If jitter fails:
→ suspect unstable path, congestion, QoS, or modulation changes under load.

### Added Step — Before RFC Analysis

Check:
- current modulation
- current capacity

If load > capacity:
→ do not troubleshoot VLAN yet