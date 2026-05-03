# NODE PROTECTION LOGIC

## PURPOSE

Define how Eclipse node protection operates, including protection types, switching logic, and system rules governing failover behavior.

---

## PROTECTION DOMAINS

* Link Protection
* Ring Protection (SPDH / Loop Switch)
* Tributary Protection
* Ethernet Module Protection (DAC GE3)
* Node Platform Protection (NPC)

---

## LINK PROTECTION TYPES

### HOT STANDBY (HS)

* Single active transmitter
* Secondary remains idle until failure
* Tx switch = NOT hitless
* Rx switching = hitless

### SPACE DIVERSITY (SD)

* Two physical paths (antennas)
* Improves fade resistance
* Tx + Rx behavior similar to HS

### FREQUENCY DIVERSITY (FD)

* Two frequencies active simultaneously
* Both transmitters ON
* Tx failure = NON-TRAFFIC AFFECTING
* Rx selects best signal

### DUAL PROTECTION

* Protection layered on top of protected links
* Requires 4 RACs
* Only ONE link feeds node at a time
* Master switch = NOT hitless

---

## RING PROTECTION

### LOOP SWITCH

* Traffic sent both directions
* Receiver selects best path
* Switching occurs on:

  * AIS
  * LOF
* NOT hitless
* ~50 ms recovery

### SPDH RING

* Primary clockwise path
* Secondary counter path
* On failure:

  * Traffic wraps around fault
* Switching time:

  * ~40–100 ms
* Controlled by:

  * Error-Free Timer
  * Delay Unwrap Timer

---

## TRIBUTARY PROTECTION

### TT (TRIBUTARY PROTECTED)

* Single active DAC/NCM
* Backup activates on failure

### TA (ALWAYS ON)

* Both paths transmit
* External equipment selects path

### RULES

* Requires identical modules
* Tx/Rx switching independent (except DAC 155oM)

---

## ETHERNET PROTECTION (DAC GE3)

### CAPABILITIES

* 1+1 module protection
* DPP (Data Protection Path)
* Supports:

  * LACP (aggregation + failover)
  * BFD (fast failover)
  * Optical Y-cable

### BEHAVIOR

* Protection applied to:

  * User ports
  * DPP ports
  * Module
* Switching = NOT hitless

### KEY LOGIC

* Port failure → traffic reroutes internally
* Module failure → full switchover
* RAC failure → DPP reroute without module change

---

## NODE PLATFORM PROTECTION (NPC)

### PROTECTS

* Power supply
* Backplane clock

### BEHAVIOR

* Power failure → hitless
* Clock failure → ~200 ms hit

---

## CORE PROTECTION RULES

### RULE 1 — MODULE PAIRING

* Protection requires TWO compatible modules
* No pairing = no protection

---

### RULE 2 — PRIMARY OWNERSHIP

* Primary module:

  * Retains circuits
  * Defines configuration
* Secondary:

  * Mirrors primary
  * Loses prior config

---

### RULE 3 — TX / RX SWITCHING

#### STANDARD

* Tx and Rx switch independently

#### FORCED COUPLING (CRITICAL)

Tx and Rx MUST switch together when:

* DPP enabled
* Payload encryption enabled
* Adaptive modulation enabled

---

### RULE 4 — ONLINE CONTROL

* Primary RAC:

  * Default TX

* Secondary RAC:

  * Default RX controller

* FD:

  * Both TX active
  * Secondary controls RX voting

---

### RULE 5 — SWITCH TYPES

| Type            | Behavior    |
| --------------- | ----------- |
| Tx Switch       | NOT hitless |
| Rx Switch       | Hitless     |
| Ring Wrap       | NOT hitless |
| Dual Protection | NOT hitless |

---

### RULE 6 — SWITCH TRIGGERS

#### TRANSMIT SWITCH

* Tx failure
* Synthesizer unlock
* Power failure
* Cable disconnect
* Modulator failure

#### RECEIVE SWITCH

* Receiver failure
* Demodulator unlock
* Hardware/software failure

#### SILENT SWITCH (RIPS)

* Both ends lose signal
* Forces remote Tx switch

---

### RULE 7 — GUARD TIMER

Purpose:
Prevent oscillation

Behavior:

* Starts after each switch
* Doubles after each event
* Halves during stability

Limits:

* Min: 5 sec
* Max: 320 sec

---

### RULE 8 — REVERTIVE MODES

* NO REVERT → stay on secondary
* NORMAL → revert after timer
* TIME OF DAY → revert at scheduled time

---

### RULE 9 — FAILURE BEHAVIOR

| Failure Type   | Result             |
| -------------- | ------------------ |
| RAC failure    | Switch to partner  |
| DPP cable loss | Tx + Rx switch     |
| DAC failure    | Module switch      |
| Link failure   | Protection trigger |
| Ring failure   | Wrap               |

---

### RULE 10 — RESTORATION TIMES

| Event          | Time              |
| -------------- | ----------------- |
| Tx switch      | <150 ms (typical) |
| Rx switch      | Hitless           |
| Ring wrap      | 40–100 ms         |
| NPC clock fail | ~200 ms           |

---

## CONFIGURATION LOGIC (PORTAL)

### PROTECTION SETUP FLOW

1. Select module (becomes PRIMARY)
2. Select partner
3. Select protection type
4. Apply configuration
5. Click SEND

---

### IMPORTANT BEHAVIOR

* Primary keeps all circuits
* Secondary circuits are dropped and replaced
* Breaking protection:

  * Primary retains all config
  * Secondary becomes empty

---

## CRITICAL DESIGN INSIGHT (FOR ARIA)

Protection is layered:

1. Link-level protection (HS / SD / FD)
2. Module-level protection (DAC / NCM)
3. Network-level protection (Ring / Dual)
4. Platform-level protection (NPC)

ARIA must:

* Identify protection layer involved
* Determine switch trigger source
* Predict failover path
* Validate configuration consistency

---

## END OF FILE
