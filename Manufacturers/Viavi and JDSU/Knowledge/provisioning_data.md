# ================================
# SECTION — VIAVI REQUIRED INPUTS
# ================================

## Link Setup

- Interface type (optical / copper)
- Speed (1G / 10G / etc.)
- SFP type / wavelength
- Auto-negotiation setting

---

## Traffic Configuration

- Load type (constant)
- Load unit (bitrate)
- CIR (Committed Information Rate)

---

## VLAN / Network

- VLAN ID (if used)
- MTU (if jumbo frames used)
- Source MAC
- Destination MAC (if head-to-head)

---

## Loopback

- Loopback type (LLB / far-end)
- Is loopback active?

---

## RFC2544

- Throughput threshold
- Frame loss threshold
- Latency threshold
- Jitter threshold
- Frame sizes

# ================================
# SECTION — VIAVI Result Interpretation Inputs
# ================================

## Required Result Inputs

ARIA must collect:

- Test type:
  - L2 Traffic
  - Loopback
  - RFC2544
- Interface:
  - optical
  - copper
- Speed / line rate
- Auto-negotiation setting
- Duplex state
- VLAN ID
- CIR / committed rate
- Load rate
- Max bandwidth
- Loopback state
- Rx Mbps
- Lost Frames
- Failed RFC2544 subtest
- Failed frame size
- Throughput result
- Frame loss result
- Latency result
- Jitter result
- Optical Tx/Rx levels, if optical
- SFP wavelength
- Fiber inspection status

# ================================
# SECTION — End-to-End RFC2544 Troubleshooting Inputs
# ================================

## Required Inputs

ARIA must collect the following before diagnosing an RFC2544 failure.

---

## VIAVI Inputs

- Test type
- Interface type
- Port used
- Speed / line rate
- VLAN enabled:
  - yes
  - no
- VLAN ID
- CIR / Max Bandwidth
- Configured load
- Frame sizes selected
- Failed subtest
- Failed frame size
- Rx Mbps
- Lost Frames
- Latency result
- Jitter result
- Report screenshot or result summary

---

## Local Radio Port Inputs

- Radio port connected to VIAVI
- Port operational state
- Port admin state
- LOS alarm:
  - yes
  - no
- Speed/duplex
- Tagged/untagged setting
- PVID/native VLAN
- Allowed VLANs
- Interface errors
- CRC errors
- drops/discards

---

## Far-End Inputs

- Far-end radio port used
- Far-end port operational state
- Far-end LOS alarm:
  - yes
  - no
- Loopback device connected:
  - yes
  - no
- Loopback mode:
  - LLB
  - MAC swap
  - hard loop
  - far-end tester
- Far-end VLAN behavior
- Far-end port tagging/untagging
- Is traffic returning?

---

## RF / Microwave Inputs

- Current RSL
- Expected RSL
- XPD values, if XPIC
- BER / errored seconds
- Current modulation
- Expected modulation
- Current link capacity
- Expected link capacity
- ACM/adaptive modulation status
- ATPC status
- RF alarms
- Protection state

---

## Comparison Inputs

ARIA must compare:

- VIAVI configured CIR/load
- expected service bandwidth
- actual current radio capacity
- modulation-dependent capacity
- configured Ethernet port rate