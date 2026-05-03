# ================================
# SECTION — VIAVI FAILURE MODES
# ================================

## Link Down

Cause:
- wrong SFP
- bad fiber
- incorrect wavelength
- no signal

---

## Link Up, No Traffic

Cause:
- VLAN mismatch
- wrong MAC
- loopback not enabled
- incorrect encapsulation

---

## Loopback Not Working

Cause:
- loopback not enabled
- auto-neg mismatch
- duplex mismatch

---

## RFC2544 Failure

### Throughput Low
- shaping / rate limit
- duplex mismatch
- incorrect CIR

---

### Frame Loss
- congestion
- bad cable
- interface errors

---

### Latency High
- buffering
- queuing

---

## False Failure

Cause:
- wrong test setup
- incorrect thresholds
- VLAN misconfiguration

# ================================
# SECTION — VIAVI RFC2544 / Traffic Interpretation Engine
# ================================

## Purpose
Teach ARIA how to interpret VIAVI traffic and RFC2544 results after the test is configured and running.

---

## Result Layer Rule

ARIA must interpret VIAVI results in this order:

1. Physical link
2. Sync / link state
3. Loopback state
4. Traffic rate
5. Frame loss
6. Latency
7. Jitter
8. Report/pass-fail result

Do not diagnose RFC2544 failure until physical link and loopback are confirmed.

---

## Failure Pattern: No Signal Present

### Meaning
The tester is not receiving valid optical/electrical signal.

### Likely Causes
- wrong SFP
- wrong wavelength
- bad fiber
- dirty fiber end-face
- disconnected fiber
- far-end laser off
- optical level too low
- wrong port patched

### ARIA Questions
- Is the laser on?
- Is the SFP wavelength correct?
- Was the fiber inspected and cleaned?
- Are Tx/Rx crossed correctly?
- What are the Tx/Rx optical levels?

---

## Failure Pattern: Signal Present but No Sync Acquired

### Meaning
Light or electrical signal exists, but the tester cannot synchronize to a valid Ethernet signal.

### Likely Causes
- wrong speed
- wrong line rate
- wrong interface type
- bad SFP compatibility
- incorrect test selection
- damaged signal

### ARIA Questions
- Did you select the correct Ethernet rate?
- Does the SFP support the circuit speed?
- Is the far end configured for the same speed?
- Is the correct test mode selected?

---

## Failure Pattern: Sync Acquired but Link Not Active

### Meaning
The tester sees Ethernet signal but link negotiation/state is not complete.

### Likely Causes
- auto-negotiation mismatch
- duplex mismatch
- speed mismatch
- copper interface negotiation issue
- far-end port disabled

### ARIA Questions
- Is auto-negotiation required?
- Is the circuit copper or optical?
- Is the port full duplex?
- Is the expected speed shown in AutoNeg Status?

Important:
1000 Mbps electrical requires auto-negotiation ON.

---

## Failure Pattern: Link Active but No Traffic

### Meaning
Layer 1/2 link is up, but frames are not passing correctly.

### Likely Causes
- VLAN mismatch
- encapsulation wrong
- loopback not active
- wrong destination MAC
- wrong source/destination addressing in head-to-head test
- traffic not started

### ARIA Questions
- Is traffic started?
- Is VLAN enabled if the circuit requires VLAN tagging?
- Is the VLAN ID correct?
- Is LLB / loopback active?
- Is the destination MAC correct?
- Are results showing Rx Mbps?

---

## Failure Pattern: Loopback Not Detected

### Meaning
The tester cannot confirm a far-end loopback.

### Likely Causes
- far-end device not in loopback
- wrong loopback mode
- path not complete
- VLAN mismatch
- MAC swap not active
- tester not compatible with loop up command

### ARIA Questions
- Is the far end a VIAVI-compatible loopback device?
- Is it already in Local Loop Back mode?
- Did you press Loop Up?
- Is LLB active?
- Is VLAN configured before looping?

---

## Failure Pattern: Rx Mbps Below CIR

### Meaning
Traffic is returning, but measured throughput is below committed rate.

### Likely Causes
- circuit shaping below expected CIR
- wrong load rate configured
- wrong max bandwidth in RFC2544
- duplex mismatch
- congestion
- packet loss
- wrong service profile

### ARIA Questions
- What CIR was entered?
- What does Rx Mbps show?
- Is Max Bandwidth set to CIR?
- Are there lost frames?
- Is the circuit rate-limited by provider config?

Interpretation:
If Rx Mbps is below CIR and Lost Frames are 0, suspect shaping or rate configuration before suspecting physical errors.

---

## Failure Pattern: Lost Frames Greater Than 0

### Meaning
Traffic is being dropped.

### Likely Causes
- congestion
- RF/path errors
- bad cable/fiber
- interface errors
- oversubscription
- wrong CIR/load rate
- VLAN/QoS handling issue

### ARIA Questions
- What frame size is losing frames?
- Does loss occur at all sizes or only large frames?
- Is load set above CIR?
- Are interface errors increasing?
- Is RF clean during the test?

Interpretation:
Frame loss is more serious than low throughput because it means frames are not being delivered.

---

## Failure Pattern: Small Frames Fail, Large Frames Pass

### Meaning
The circuit may struggle with packet rate rather than bandwidth.

### Likely Causes
- packet processing limitation
- switch/router performance issue
- policer behavior
- service device packet-per-second limit

### ARIA Questions
- Which frame sizes failed?
- Did 64-byte frames fail?
- Did larger frames pass?
- Is the equipment rated for the packet rate?

---

## Failure Pattern: Large Frames Fail, Small Frames Pass

### Meaning
MTU, jumbo frame, or fragmentation problem.

### Likely Causes
- MTU too low
- jumbo frames not supported end-to-end
- VLAN tag increases frame size
- provider network drops oversized frames

### ARIA Questions
- What MTU is required?
- Was MTU frame length added to RFC2544?
- Is VLAN tagging used?
- Is expected frame size 1518 or 1522 with VLAN?
- Are jumbo frames enabled end-to-end?

---

## Failure Pattern: Latency Fails but Throughput Passes

### Meaning
Bandwidth is available, but delay is too high.

### Likely Causes
- buffering
- queuing
- congestion
- long network path
- QoS issue
- microwave path delay under load

### ARIA Questions
- Did latency fail at all frame sizes?
- Is frame loss also present?
- Is traffic being queued?
- Is this a protected or routed path?

---

## Failure Pattern: Jitter Fails but Latency Passes

### Meaning
Average delay may be acceptable, but delay variation is unstable.

### Likely Causes
- congestion
- bursty traffic
- QoS issue
- unstable path
- packet scheduling behavior

### ARIA Questions
- Is this service carrying voice/video?
- Does jitter occur only under load?
- Is frame loss also present?
- Is QoS configured?

---

## Failure Pattern: RFC2544 Fails but Manual L2 Traffic Passes

### Meaning
Basic traffic works, but formal service validation fails.

### Likely Causes
- thresholds too strict
- wrong CIR
- wrong frame sizes
- latency/jitter threshold exceeded
- frame loss at specific sizes
- RFC test configuration mismatch

### ARIA Questions
- Which RFC2544 subtest failed?
- What thresholds were entered?
- What frame sizes were selected?
- Did J-QuickCheck pass before RFC test?
- Was measured throughput >= CIR?

---

## Failure Pattern: Manual L2 Traffic Fails Before RFC2544

### Meaning
Do not run RFC2544 yet.

### ARIA Rule
RFC2544 is invalid until:
- Signal Present is green
- Sync Acquired is green
- Link Active is green
- loopback/path is confirmed
- traffic returns

Fix link/path first.

# ================================
# SECTION — End-to-End RFC2544 Failure Modes
# ================================

## Failure Mode: VIAVI VLAN Does Not Match Radio VLAN

### Pattern
Test set is configured for a VLAN that the radio port is not carrying correctly.

### Symptoms
- link active
- no traffic return
- RFC2544 fails immediately
- loopback not detected
- ARP/MAC behavior may appear wrong

### ARIA Checks
- VIAVI VLAN ID
- radio port VLAN membership
- tagged vs untagged
- PVID/native VLAN
- allowed VLAN list
- far-end VLAN egress behavior

---

## Failure Mode: Test Set Untagged / Radio Tagged-Only

### Pattern
VIAVI sends untagged traffic but radio port only admits tagged frames.

### Symptoms
- physical link up
- traffic not passing
- RFC2544 fails
- no loopback response

### ARIA Fix
- either enable VLAN tagging on VIAVI
- or configure radio port to accept/classify untagged traffic correctly

---

## Failure Mode: Test Set Tagged / Radio Expects Untagged

### Pattern
VIAVI sends tagged frames but radio handoff expects untagged traffic.

### Symptoms
- link active
- traffic dropped or misclassified
- RFC2544 fail

### ARIA Fix
- align VIAVI VLAN tagging with radio port mode

---

## Failure Mode: Local Radio Port Not Communicating With Test Set

### Pattern
VIAVI is connected, but radio port is not actually passing traffic.

### Symptoms
- no Link Active
- no Frame Detect
- port LOS
- no Rx Mbps
- local port counters not incrementing

### ARIA Checks
- correct port
- cable/SFP
- speed/duplex
- LOS alarm
- interface counters

---

## Failure Mode: Far-End Loopback Missing

### Pattern
RFC2544 is started without a valid return path.

### Symptoms
- traffic transmits but does not return
- loopback not detected
- Rx Mbps absent or near zero
- RFC2544 fails

### ARIA Checks
- loopback plugged in
- far-end port up
- far-end LOS alarm
- LLB/MAC swap enabled
- correct VLAN at far end

---

## Failure Mode: Far-End Port LOS

### Pattern
Far-end radio Ethernet port is down or has LOS.

### Symptoms
- local test may show link up
- no return traffic
- loopback not detected
- RFC2544 fail

### ARIA Rule
Do not troubleshoot throughput until far-end port LOS is cleared.

---

## Failure Mode: Test Load Exceeds Radio Capacity

### Pattern
VIAVI configured load/CIR is higher than current available microwave capacity.

### Symptoms
- throughput fails
- frame loss may occur
- RFC2544 fails at higher load
- RF link remains up

### Causes
- modulation degraded
- ACM reduced capacity
- expected CIR entered incorrectly
- radio profile not at full modulation

### ARIA Checks
- configured VIAVI load
- expected CIR
- current modulation
- expected modulation
- current link capacity

---

## Failure Mode: Modulation Degraded During Test

### Pattern
Radio expected to run high modulation but has dropped to lower modulation.

### Example
Expected:
- 4096QAM

Current:
- 1024QAM

### Symptoms
- link remains up
- throughput below expected
- frame loss under load
- RFC2544 throughput failure
- capacity lower than expected

### ARIA Rule
If modulation is degraded, compare RFC2544 load against current modulation capacity before blaming VIAVI or VLAN.

---

## Failure Mode: L1 Throughput Configured Too High

### Pattern
VIAVI load is set above what the circuit/radio can carry.

### Symptoms
- throughput fail
- possible frame loss
- test fails only at high load
- lower load may pass

### ARIA Checks
- What is the configured L1 load?
- What is the committed rate?
- What is the actual current link capacity?
- Is the VIAVI using line rate instead of CIR?

---

## Failure Mode: RF Clean at Idle, Fails Under Load

### Pattern
Radio appears healthy before test, but traffic load exposes capacity or error issue.

### Symptoms
- idle alarms clean
- RFC2544 frame loss
- throughput instability
- modulation changes during test

### ARIA Checks
- modulation before and during test
- BER during test
- errored seconds during test
- RSL/XPD stability during test

---

## Failure Mode: RFC2544 Fails Due to Carrier/Test Threshold

### Pattern
Traffic works, but entered pass/fail threshold does not match service requirement.

### Symptoms
- test result fail
- actual traffic may be acceptable
- fail caused by threshold mismatch

### ARIA Checks
- throughput threshold
- latency threshold
- jitter threshold
- frame loss threshold
- correct service order / MOP values

# ================================
# REAL WORLD CASE — [Short Title]
# ================================

## Scenario
Describe what the tech saw:
- “RFC2544 failing”
- “Link up, no traffic”
- “Throughput low under load”

---

## Observed Symptoms
- Signal Present: yes
- Sync: yes
- Link: yes
- Rx Mbps: low
- Lost Frames: yes
- Modulation: dropped from 4096QAM → 1024QAM

---

## Root Cause
- modulation degraded due to fade
- capacity dropped below test load

---

## Key Insight
RFC2544 failure was NOT:
- VLAN
- loopback
- VIAVI config

It was:
→ capacity mismatch caused by modulation drop

---

## ARIA Detection Trigger
If:
- throughput low
- frame loss present
- modulation lower than expected

Then:
→ compare test load to current capacity BEFORE checking VLAN