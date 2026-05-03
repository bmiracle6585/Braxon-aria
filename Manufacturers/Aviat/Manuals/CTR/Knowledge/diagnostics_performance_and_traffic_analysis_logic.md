id="ctr-diagnostics-logic"
# CTR — Diagnostics, Performance & Traffic Analysis Logic

## PURPOSE
This file teaches ARIA how to interpret diagnostics, performance stats, and traffic behavior in the CTR system.

ARIA must use this file when supporting:
- RFC2544 failures
- throughput issues
- packet loss
- latency problems
- intermittent link behavior
- “link is up but performance is bad”

---

## CORE DIAGNOSTIC PRINCIPLE

A link can be:
- UP (RF is established)
- but NOT HEALTHY (performance degraded)

ARIA must always separate:
- link state
- link quality
- traffic performance

---

## LINK STATE VS PERFORMANCE

### Link State (Layer 1/2)
- radio is connected
- signal is present
- interface is up

### Performance (Layer 2/3)
- throughput
- latency
- packet loss
- jitter

---

## PERFORMANCE METRICS

ARIA must understand:

### Throughput
- actual data rate across link
- measured during tests (RFC2544)

---

### Packet Loss
- dropped packets
- indicates congestion or errors

---

### Latency
- time for packet to travel
- affected by:
  - distance
  - processing delay
  - congestion

---

### Jitter
- variation in latency
- critical for voice/video

---

## RFC2544 TEST LOGIC (CRITICAL)

### What It Tests
- throughput
- latency
- frame loss
- back-to-back frames

---

## RFC2544 FAILURE INTERPRETATION

### If RFC2544 FAILS but RF is GOOD:

ARIA must evaluate:

#### 1. Network Layer Issues
- incorrect IP config
- routing problems
- VLAN mismatch

#### 2. Physical Layer Issues
- bad Ethernet cable
- faulty XPIC cable
- connector issues

#### 3. Configuration Issues
- rate limiting
- QoS policies
- incorrect port speed/duplex

#### 4. Radio-Level Degradation
- subtle RF errors not obvious in RSL
- poor XPD isolation
- interference

---

## CRITICAL FIELD INSIGHT

RFC2544 is NOT just RF.

Failure can be caused by:
- cable problems
- switching issues
- VLAN tagging errors
- duplex mismatch

---

## INTERFACE STATISTICS LOGIC

ARIA must interpret:

### Errors
- CRC errors → physical issue
- frame errors → corruption
- drops → congestion or buffer overflow

---

### Utilization
- high utilization → congestion
- low utilization + poor throughput → inefficiency

---

## FAILURE PATTERNS

### High Errors + Good RF
Likely:
- bad cable
- port issue
- hardware fault

---

### No Errors + Low Throughput
Likely:
- configuration issue
- rate limiting
- incorrect test setup

---

### Intermittent Performance
Likely:
- loose cable
- environmental RF interference
- unstable routing

---

## DUPLEX / SPEED MISMATCH LOGIC

### Symptoms
- low throughput
- high retransmissions
- inconsistent results

---

## MTU / FRAME SIZE ISSUES

### Symptoms
- RFC2544 fails at higher frame sizes
- fragmentation
- packet drops

---

## TRAFFIC FLOW LOGIC

ARIA must understand:

Traffic path:
Device → VLAN → Interface → Radio → Remote Radio → Interface → Destination

Failure can occur at ANY point.

---

## LOOPBACK TESTING LOGIC

### Purpose
- isolate problem location

### If loopback passes locally but fails end-to-end:
→ issue is between devices (link path)

---

## RADIO VS NETWORK DECISION LOGIC

### Good RF Indicators
- stable RSL
- clean XPD
- no radio alarms

---

### If performance is bad despite good RF:
ARIA must prioritize:
1. cabling
2. Ethernet ports
3. VLAN config
4. IP/routing
5. QoS / shaping

---

## REAL-WORLD FAILURE SCENARIO (IMPORTANT)

### Scenario:
- Link is up
- RF looks good
- RFC2544 fails

### ARIA MUST THINK:

1. Is traffic even flowing correctly?
2. Are ports clean (no CRC errors)?
3. Are VLANs aligned on both sides?
4. Is there a bad XPIC or Ethernet cable?
5. Is there rate limiting or shaping?

---

## DIAGNOSTIC QUESTION FLOW

ARIA must ask:

1. What are RFC2544 results (loss, throughput)?
2. Are there interface errors?
3. What are port speeds/duplex settings?
4. Are VLANs matching on both sides?
5. Are cables confirmed good?
6. Is there any QoS or rate limiting?
7. Does loopback testing pass?
8. Is RF stable during testing?

---

## CRITICAL DO-NOT-GUESS RULE

ARIA must NOT:
- assume RF is the issue based only on test failure
- ignore physical layer (cables/ports)
- ignore VLAN/IP layer

ARIA must evaluate:
- physical layer
- data link layer
- network layer

before concluding root cause

---

## SOURCE
CTR Diagnostics / Performance / Testing Documentation