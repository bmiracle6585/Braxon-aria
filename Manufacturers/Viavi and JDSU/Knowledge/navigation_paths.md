L2 Traffic:
Test → Ethernet → Layer 2 Traffic → P1 Terminate

Loopback:
Actions → LLB

RFC2544:
Test → Ethernet → RFC2544 → L2 Traffic

# ================================
# SECTION — VIAVI Result Review Paths
# ================================

## Link State

### Summary Indicators
Results > Summary

Check:
- Signal Present
- Sync Acquired
- Link Active
- Frame Detect
- Pattern Sync

---

## Auto Negotiation

### AutoNeg Status
Results > Ethernet > AutoNeg Status

Check:
- Link Adv Status
- Link Config ACK
- Speed
- Duplex
- Pause Capability
- Remote Fault

---

## Traffic Results

### Throughput / Rx Mbps
Results > Ethernet / Summary result window

Check:
- Rx Mbps, L1
- Lost Frames
- Frame Loss Ratio

---

## Loopback

### Local Line Loopback
Actions > LLB

### VIAVI Compatible Loop Up
Actions > Loop Up

---

## RFC2544

### Run J-QuickCheck
RFC2544 configuration flow > Run J-QuickCheck

### Run RFC2544 Tests
RFC2544 configuration flow > Run RFC2544 Tests

### Report
RFC2544 configuration flow > Report > Create Report

# ================================
# SECTION — End-to-End RFC2544 Verification Paths
# ================================

## VIAVI Verification

### Link Indicators
Results > Summary

Check:
- Signal Present
- Sync Acquired
- Link Active
- Frame Detect
- Pattern Sync

---

### VLAN / Encapsulation
Setup > Ethernet

Check:
- Encapsulation
- VLAN ID
- Source MAC
- Destination MAC

---

### Load / CIR
Setup > Traffic

Check:
- Load Type
- Load Unit
- Load Mbps / CIR

---

### Loopback
Actions > LLB
Actions > Loop Up

---

### RFC2544 Subtests
RFC2544 > Select Tests

Check:
- Throughput
- Latency
- Frame Loss
- Packet Jitter

---

## Radio Verification

### Local Port
Check:
- port operational status
- LOS alarm
- speed/duplex
- errors/drops
- VLAN membership

---

### Far-End Port
Check:
- port operational status
- LOS alarm
- speed/duplex
- loopback device connection
- VLAN egress behavior

---

### Radio Capacity
Check:
- current modulation
- expected modulation
- current capacity
- ACM/adaptive modulation status
- BER/errors during test