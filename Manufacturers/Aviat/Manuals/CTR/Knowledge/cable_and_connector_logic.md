# CTR — Cable and Connector Logic

## PURPOSE
This file teaches ARIA how cabling, connectors, pinouts, and physical-layer issues impact CTR system performance.

ARIA must use this file when supporting:
- intermittent link issues
- RFC2544 failures with good RF
- unexplained BER or packet loss
- no link / link flapping conditions
- PoE power issues
- suspected XPIC / Ethernet / fiber cabling faults
- installation validation

---

## CRITICAL SAFETY AND INSTALLATION RULES

### Cable Routing Rules
- Do NOT route port, tributary, or NMS cables with AC mains power lines
- Keep all signal cables away from crossing power lines
- Outdoor copper connections must use approved isolation or surge suppression devices

Failure to follow these rules can cause:
- induced noise
- intermittent errors
- equipment damage
- unsafe installations

---

## ODU CABLE REQUIREMENTS

### Electrical Constraints
- Maximum total loss: **22 dB @ 300 MHz**
- Maximum DC loop resistance: **3 ohms (there and back)**

### Maximum Cable Length
- Standard cables: **300 m (1000 ft)**
- CNT-300: **150 m (500 ft)**

### ARIA INTERPRETATION
If these limits are exceeded:
- RSL may appear lower than expected
- alignment may be incorrectly blamed
- ODU may behave unpredictably

---

## RF CABLE FAILURE PATTERNS

### Symptoms
- Low RSL despite correct alignment
- unstable or drifting signal levels
- intermittent link drops

### Likely Causes
- excessive cable length
- high resistance
- poor connector termination
- water ingress
- damaged coax

---

## CONNECTOR INSTALLATION RISKS

### Type N Connector Issues
Improper installation can cause:
- signal reflections
- intermittent RF loss
- degraded link performance

### ARIA SHOULD SUSPECT CONNECTORS WHEN:
- RSL fluctuates during movement
- tightening connectors changes signal
- link is unstable but alignment is correct

---

## ETHERNET AND RJ-45 LOGIC

### 10/100Base-T
- Separate Tx and Rx pairs (not bi-directional)

### 1000Base-T
- All 4 pairs are used
- Each pair is bi-directional (Tx/Rx)

### Cable Types
- Cat5, Cat5e, Cat6 supported
- Cat5e or higher recommended for gigabit

---

## ETHERNET FAILURE PATTERNS

### Symptoms
- link up but low throughput
- intermittent packet loss
- link flapping

### Likely Causes
- one or more bad pairs
- poor terminations
- incorrect cable type
- damaged cable

---

## PoE POWER LOGIC

### Electrical Characteristics
- Nominal voltage: ~55 Vdc
- Maximum power: 70 W
- >35 W requires all 4 pairs

### ARIA INTERPRETATION

If PoE issues occur:
- partial pair failure may allow link but not power
- high resistance causes voltage drop
- device may reboot or fail under load

### Symptoms of PoE Problems
- device powers on then resets
- device never powers up
- intermittent operation

---

## FIBER AND OPTICAL LOGIC

### Key Concepts
- single-mode and multi-mode must match
- connector types must match (LC, SC, FC)
- attenuators may be required

### Failure Patterns
- no link → wrong fiber type or connector
- high BER / packet loss → dirty fiber or poor connection
- unstable link → improper attenuation

---

## TRIBUTARY (E1/DS1) AND BNC LOGIC

### Key Rules
- each cable supports up to 8 tribs
- TX = data out
- RX = data in

### ARIA INTERPRETATION
If miswired:
- RF link may be healthy
- service will fail or be misrouted

---

## PHYSICAL LAYER VS RF LOGIC

ARIA must distinguish between:

### RF Problem
- low RSL
- poor XPD
- alignment issues

### PHYSICAL LAYER PROBLEM
- good RSL but poor throughput
- RFC2544 failure with clean RF
- intermittent BER
- link instability without RF alarms

---

## FIELD FAILURE PATTERNS

### Good RF, Bad Throughput
Possible causes:
- Ethernet cable issue
- XPIC cable issue
- connector fault
- incorrect pinout

---

### Intermittent Link / BER
Possible causes:
- cable routing near power lines
- poor grounding
- damaged cable
- loose connectors

---

### Device Not Powering (PoE)
Possible causes:
- insufficient pairs connected
- voltage drop due to resistance
- cable damage

---

### No Service but Link Up
Possible causes:
- TX/RX reversed
- incorrect trib mapping
- wrong connector usage

---

## ARIA TROUBLESHOOTING BEHAVIOR

When cabling is suspected, ARIA must ask:

1. Is RSL within expected range?
2. Is XPD normal (if XPIC)?
3. Is the issue throughput, BER, or link state?
4. What cable types are used?
5. Cable length?
6. Any recent cable changes?
7. Are cables routed near power?
8. Are connectors properly terminated?
9. Is PoE involved?
10. Are TX/RX paths verified?

---

## CRITICAL DO-NOT-GUESS RULE

ARIA must NOT assume:
- alignment is the issue when RF is healthy
- cables are good without verification

ARIA must separate:
- RF problems
- cabling problems
- connector problems
- configuration problems

before recommending replacement or adjustment

---

## SOURCE
CTR 8500-8300 Installation Guide  
Chapter 7 — Cable and Connector Data