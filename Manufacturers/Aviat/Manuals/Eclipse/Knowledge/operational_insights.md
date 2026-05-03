# ================================
# ECLIPSE — LINK CAPACITY / ACM / PERFORMANCE BEHAVIOR
# ================================

## Modulation vs Capacity Behavior

- Higher modulation = higher capacity
- Lower modulation = reduced capacity

Example (55 MHz):
- 256 QAM ≈ 366 Mbps
- 128 QAM ≈ 312 Mbps
- 64 QAM ≈ 267 Mbps

Operational impact:
- Modulation downgrade directly reduces available bandwidth

---

## ACM (Adaptive Coding and Modulation)

- System dynamically adjusts modulation based on RF conditions

Behavior:
- Good RF → higher modulation → higher throughput
- Degraded RF → lower modulation → reduced throughput

---

## ACM Cascade Effect (CRITICAL)

RF degradation triggers:

1. Modulation drop
2. Capacity reduction
3. Throughput reduction
4. Latency increase
5. Jitter increase

---

## Throughput vs Capacity

- Airlink capacity ≠ Ethernet throughput

Differences due to:
- Framing overhead
- Packet size
- Measurement method

Rule:
- Do not directly compare RF capacity to Ethernet throughput

---

## Packet Size Impact

- Throughput varies based on packet size

Example:
- 1518 byte vs 64 byte produces different throughput values

Impact:
- Small packet traffic behaves differently than large packet traffic

---

## XPIC Behavior

- XPIC improves spectral efficiency using dual polarization

Impact:
- Increased capacity
- More stable high modulation operation

Risk:
- XPIC degradation reduces performance stability

---

## Latency Behavior

- Latency increases as modulation decreases

Causes:
- More robust coding schemes
- Increased processing overhead

---

## Encryption Impact

- Enabling encryption slightly increases latency

Impact:
- Small but measurable delay added to traffic

---

## Performance Misinterpretation Risk

Common mistake:
- Low throughput assumed to be network issue

Reality:
- Often caused by RF degradation and ACM behavior

---

## Field-Level Diagnosis Logic

If:
- Throughput drops
- Latency increases

Check:
- Current modulation level
- RF signal quality
- XPIC status

Before:
- Investigating routing or switching issues

---

## Failure Risk Areas

- RF degradation causing ACM downgrade
- Misinterpreting throughput values
- Ignoring packet size impact
- XPIC imbalance or failure
- Assuming Ethernet issue instead of RF issue

# ================================
# ECLIPSE — RING NETWORK BEHAVIOR
# ================================

## Ring Protection Behavior

- Ring networks provide protection by rerouting traffic in the opposite direction around the ring when a failure occurs
- No external switching device is required; rerouting is handled internally by the node

---

## Primary vs Secondary Ring

Primary Ring:
- Direction: West → East (clockwise)
- Carries all traffic during normal operation

Secondary Ring:
- Direction: East → West (counter-clockwise)
- Only used during failure conditions

---

## Circuit Wrapping (CRITICAL)

- Traffic is rerouted at both sides of a break
- Traffic leaves the primary ring and travels on the secondary ring to bypass the fault
- Rejoins the primary ring past the failure point

---

## Revertive Behavior

- Once the fault clears, the system automatically returns to normal operation
- Traffic moves back to the primary ring

---

## Node Traffic Behavior

At each node, traffic can:

1. Pass-through:
   - Traffic continues through the node unchanged

2. Drop-and-Insert:
   - Traffic is removed for local use
   - New traffic is injected into the ring

---

## Traffic Flow Awareness

- Traffic paths are dynamic in failure scenarios
- Link failure does not immediately equal traffic loss
- Traffic may still be flowing on alternate path

---

## Ring Capacity Constraints

- Each circuit (E1/DS1) is unique within the ring
- Circuits cannot be reused within the same ring

---

## Partial Ring Behavior

- If all links are not operational:
  - Ring remains in a wrapped state
  - Traffic flows in protection mode until full ring is complete

---

## Dependency Awareness

- All links must be operational for normal (unwrapped) operation
- Single link failure triggers protection behavior

---

## Failure Interpretation Logic

Observed Issue:
- Traffic shift
- Increased latency
- Unexpected routing path

Possible Cause:
- Ring wrap due to link failure

---

## Risk Areas

- Misinterpreting wrapped state as normal operation
- Missing partial ring completion
- Incorrect circuit allocation
- Unrecognized protection switching behavior

# ================================
# ECLIPSE — ALARM BEHAVIOR & DIAGNOSTICS
# ================================

## Alarm System Purpose

- Provides real-time visibility into faults, degradation, and system conditions
- Used for troubleshooting, monitoring, and fault isolation

---

## Alarm Severity Logic

Critical:
- Service affecting
- Traffic interruption or outage
- Requires immediate action

Major:
- Significant degradation
- Partial service impact
- Requires urgent attention

Minor:
- No immediate service impact
- Potential risk condition
- Monitor and schedule resolution

Warning:
- Early indication or threshold trigger
- No service impact
- Observation only

---

## Alarm Categories

Communication:
- Loss of signal (LOS)
- Link failures
- Network connectivity issues

Equipment:
- Hardware faults
- Power supply issues
- Fan or thermal faults

Processing:
- Software errors
- CPU or memory issues

Environmental:
- Temperature alarms
- External environmental triggers

---

## Alarm State Behavior

Active:
- Fault condition is present

Cleared:
- Fault condition resolved

---

## Alarm Persistence

- Alarms remain active until root cause is resolved
- May clear automatically or require manual acknowledgment

---

## Correlation Logic (CRITICAL)

Multiple alarms should NOT be treated independently

ARIA must:
- Identify root cause alarm
- Suppress dependent symptom alarms

---

## Field Interpretation Rules

- “Red alarm” = Critical condition
- “Flapping alarms” = unstable RF or intermittent link
- Multiple alarms = likely single root cause

---

## RF Correlation

Alarm + Performance issue:

- RF degradation → triggers alarms → triggers ACM changes
- Must validate RF before network layer troubleshooting

---

## Ring Network Correlation

- Link failure → triggers alarm → causes ring wrap
- Traffic may still pass despite alarms

---

## Hardware Correlation

- Equipment alarms indicate physical component failure
- Requires inspection or replacement

---

## Diagnostic Priority Flow

1. Check Critical alarms
2. Identify root cause alarm
3. Correlate with:
   - RF conditions
   - Ring topology behavior
   - Hardware status
4. Ignore secondary symptom alarms until root cause identified

---

## Failure Risk Areas

- Misinterpreting symptom alarms as root cause
- Ignoring alarm correlation
- Treating alarms in isolation
- Skipping RF validation

# ================================
# ECLIPSE — NODE CAPACITY & LIMITATIONS
# ================================

## Core Capacity Principle

Node capacity is NOT determined by RF alone.

Capacity is limited by:
- Backplane bus capacity
- DPP (Ethernet data plane) capacity
- Link modulation capacity

---

## Backplane vs DPP Behavior

Backplane:
- Used for PDH and some Ethernet traffic
- Hard capacity limits apply
- Shared across all circuits

DPP:
- Ethernet-only transport
- Not limited by backplane
- Limited by link capacity and port limits

---

## Mixed Traffic Behavior

- Backplane capacity is allocated first
- Remaining link capacity is available for DPP (Ethernet)
- Increasing PDH traffic reduces available Ethernet capacity

---

## Capacity Bottleneck Logic (CRITICAL)

Performance issues may be caused by:
- Backplane saturation (NOT RF issue)
- DPP link limits
- Port limitations (1 Gbps max)

---

## Aggregation Node Behavior

- Capacity used = pass-through + drop traffic
- Aggregation nodes consume more backplane capacity than terminal nodes

---

## Terminal Node Behavior

- Capacity used = only terminated circuits
- Lower overall backplane demand

---

## CCDP / XPIC Impact

- Co-channel dual polarization increases RF capacity
- Can EXCEED backplane limits

Critical insight:
- RF capacity can be higher than node can handle

---

## Scaling Limitation

If capacity exceeds node limits:
- Traffic must be split across multiple nodes
- Single node cannot handle full load

---

## Ring Capacity Impact

- Drop-insert circuits consume MORE capacity than pass-through
- Ring traffic increases backplane load

---

## SPDH Ring Constraints

- Drop-insert = 1.5x backplane cost
- Pass-through = standard cost

---

## ACM Limitation

- Adaptive modulation NOT supported on SPDH rings

---

## Ethernet vs PDH Tradeoff

- More PDH circuits = less Ethernet capacity
- Ethernet capacity = remaining link capacity after PDH allocation

---

## Invalid Configuration Risk

If:
- Backplane usage exceeds limits

Result:
- System instability
- Loss of management (NMS)
- Link failures

---

## Field Diagnosis Logic

If:
- RF is healthy
- Throughput is capped

Check:
- Backplane usage
- Circuit allocation
- DPP vs PDH balance

---

## Critical Insight

Not all performance issues are RF-related.

Node architecture and internal capacity limits are often the root cause.

# ================================
# ECLIPSE — PROTECTION SWITCHING BEHAVIOR
# ================================

## Core Concept

Protection switching validation is based on:
- Simulated failure conditions
- Measured recovery time
- Hardware-level triggers

---

## Critical Insight

Switching performance is NOT theoretical.

It is:
- Measured using physical failure simulation
- Dependent on hardware state
- Dependent on configuration accuracy

---

## Testing Philosophy

To validate protection:
- You must BREAK something intentionally
- Measure how fast system recovers

---

## Types of Failure Simulation

Protection switching is tested using:

- Tx mute (logical failure)
- Manual switch (controlled failover)
- Cable pull (physical failure)
- Card removal (hardware failure)
- RF path interruption

---

## Risk Awareness

Some tests:
- Carry electrical risk (high current)
- Can cause arcing or damage
- Should NOT be performed casually

---

## Key Behavioral Insight

Different failure types produce different switching behaviors:

- Logical triggers → clean switching
- Physical pulls → real-world failure conditions
- RF interruption → path-level failure validation

---

## Real-World Relevance

Field issues often resemble:
- Cable failure
- Card failure
- RF path loss

NOT:
- Clean manual switching

---

## Diagnostic Value

If protection switching fails:
- Identify trigger type
- Verify hardware path
- Confirm redundancy configuration

---

## Critical Limitation

Published switching times are ONLY valid if:
- Exact test conditions are followed
- Proper hardware and revisions are used

---

## Field Application

If protection is suspected faulty:
- Simulate failure safely
- Observe switching behavior
- Compare against expected response

# ================================
# ECLIPSE — CARD REPLACEMENT BEHAVIOR
# ================================

## Core Principle

Card replacement is designed to be:
- Hitless (no traffic interruption)
- Controlled through protection switching

---

## Primary vs Secondary Logic

- Secondary is always active during failure
- Primary is replaced while offline
- System relies on protection state to maintain traffic

---

## Hitless Replacement Behavior

Most replacements follow:

1. Lock secondary online
2. Remove faulty primary (offline)
3. Insert replacement
4. Unlock secondary

Result:
→ No traffic impact

---

## Reversion Behavior

Returning traffic to primary:

- Requires manual or forced switch
- Causes traffic hit

Insight:
- Hitless replacement ≠ hitless restoration to original state

---

## Critical Insight

Traffic impact depends on:
- Whether system is already in protection state
- Whether reversion is forced

---

## Hardware Dependency

Hitless operation depends on:
- Hardware revision compatibility
- Software version compatibility

Older hardware:
→ May cause traffic hit during replacement

---

## Clock Dependency (CRITICAL)

For NPC/NCC replacement:

- Clock source MUST be locked before removal
- Failure to do this:
→ Causes traffic interruption

---

## Configuration Dependency

For NCC replacement:

- Requires:
  - Backup configuration
  - User credentials
  - Licensing information

---

## Staging Requirement

Best practice:
- Pre-configure replacement card in separate chassis
- Restore configuration before swap

---

## Failure Risk Areas

- Removing card without locking protection
- Ignoring clock source dependency
- Using incompatible hardware revisions
- Missing configuration backup

---

## Field Diagnosis Logic

If traffic hit occurs during replacement:

Check:
- Protection state
- Clock source lock
- Hardware compatibility
- Whether manual reversion was triggered

---

## Critical Rule

Replacement can be hitless ONLY if:
- Proper sequence is followed
- System dependencies are respected

# ================================
# ECLIPSE — SWITCHING TIME BEHAVIOR
# ================================

## Core Principle

Switching time = how long traffic is disrupted during a failure or protection event

Measured in:
- milliseconds (ms)
- varies by failure type and system layer

---

## Key Insight

Not all failures behave the same.

Different triggers produce different outage times:
- Logical switch → slower
- Physical failure → faster (often)
- Cable pulls → highly variable

---

## Typical Switching Behavior

Fast (<100ms):
- ODU cable pull
- RIPS switch

Moderate (100–300ms):
- Manual switch
- TX mute

Slow (400–500ms+):
- DPP cable pull
- DAC GE3 Y cable pull
- RAC pull

---

## DPP vs Backplane Behavior

- Ethernet DPP switching is generally slower than backplane
- TDM switching is often faster and more predictable

---

## First Switch Exception (CRITICAL)

- First protection switch after power cycle can be ~1000 ms
- Subsequent switches return to normal timing

---

## Measurement Dependency

Switching time depends on:
- Test method
- Equipment used
- Frame size and rate
- Hardware configuration

---

## Real-World Insight

Field switching times may differ from documented values due to:
- Poor cable pull execution
- Environmental conditions
- Incorrect configuration
- Hardware revision differences

---

## Performance Interpretation

If outage observed:

<100ms:
- Normal protection behavior

100–300ms:
- Expected switching delay

>500ms:
- Potential issue or non-optimal condition

---

## Upgrade Impact

Firmware upgrades can cause:
- Significant traffic outage (seconds)
- Newer versions reduce outage time
- Some upgrades are hitless (depending on hardware)

---

## Critical Rule

Switching times are VALID ONLY under controlled test conditions

Do not assume field performance will match lab values exactly

# ================================
# ECLIPSE — MANAGEMENT & PHYSICAL ACCESS BEHAVIOR
# ================================

## Core Concept

System access and management depend on:
- Physical connections (cables, ports)
- Logical access (NMS / Portal)
- Proper wiring and separation from power systems

---

## NMS Access Behavior

- NMS ports provide Ethernet-based management access
- Used for:
  - Portal
  - ProVision
- Ports auto-detect cable type (straight or crossover)

---

## Connectivity Indicators

- LED behavior varies by hardware
- Typical:
  - Orange = link status
  - Green = activity

Note:
- Some systems reverse this behavior

---

## Critical Insight

Loss of management access is often:
- Physical (cabling issue)
- NOT a system failure

---

## Cable Dependency

System behavior depends heavily on:
- Correct cable type
- Proper termination
- Correct pinout

Incorrect wiring:
→ Causes loss of signal or incorrect data flow

---

## Data Direction Awareness

- TX = data leaving device
- RX = data entering device

Misinterpretation:
→ Leads to wiring errors

---

## Protection Cabling (Y-Cables)

- Used for protected operation
- Splits traffic across primary/secondary paths

Critical:
- Required for redundancy
- Incorrect use breaks protection

---

## Safety Rules (CRITICAL)

- Do NOT route signal cables with AC power lines
- Do NOT connect directly to outside plant without protection
- Surge suppression required for external connections

---

## Auxiliary / Alarm Behavior

- Auxiliary ports provide external interface capability
- Alarm I/O provides relay-based signaling

---

## Relay Behavior

- Relays can be:
  - Normally Open (NO)
  - Normally Closed (NC)

- Can be configured:
  - Energized on alarm
  - De-energized on alarm

---

## Environmental Risk

Improper wiring or grounding:
→ Causes:
- Signal interference
- Equipment damage
- False alarms

---

## Field Diagnosis Logic

If management access fails:

Check:
- Ethernet cable
- Port LED status
- Pinout correctness
- Physical connection integrity

Before:
- Assuming system failure

# Eclipse Installation — Critical Behaviors

## Power-On Behavior

- Node requires ~90 seconds before Portal can connect
- Early connection attempts will fail

## Transmit Mute (CRITICAL)

- Enabled by default on new systems
- Prevents unintended RF transmission
- MUST be removed during configuration

## RF Risk

- If Tx Mute is not enabled and configuration is incorrect:
  → Interference can occur with live networks

## Configuration Behavior

- Changes are NOT active until "Send" is clicked
- Unsaved changes exist only in module memory

## Link Configuration Dependency

- Both ends must be configured locally initially
- Remote configuration only possible AFTER link is established

## Hardware Constraint

- RF parameters are read from hardware
- Cannot configure outside allowed limits

## NVME Behavior

- Configuration stored on NVME (NCCv4)
- Persists across hardware changes

## Critical Safety Rule

- NEVER disconnect ODU cable under power
  → Risk of arcing and traffic disruption