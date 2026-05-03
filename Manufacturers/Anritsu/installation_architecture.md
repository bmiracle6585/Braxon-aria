# ================================
# SECTION — Anritsu S820E Test Architecture
# ================================

## Instrument Role

The Anritsu Site Master S820E is a field instrument used to validate microwave transmission paths.

It can test:
- coaxial feed lines
- waveguide feed lines
- antennas
- connectors
- adapters
- transmission paths
- return loss
- VSWR
- cable loss
- distance-to-fault

---

## Test Path Architecture

### System Sweep Path
Anritsu → test cable/adapters → waveguide/feedline → antenna

Includes:
- line
- connectors
- bends
- grounds
- antenna

---

### Load Sweep Path
Anritsu → test cable/adapters → waveguide/feedline → load adapter / precision load

Excludes:
- antenna

Used to isolate the line from the antenna.

---

### Cable Loss Sweep Path
Anritsu → test cable/adapters → transmission line → short

Used to measure attenuation/loss through the line.

---

## Measurement File Architecture

Measurement file:
- contains measurement data
- contains setup data

Setup file:
- stores repeatable configuration

Screen shot:
- stores visual proof only