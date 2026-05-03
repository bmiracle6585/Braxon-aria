# ================================
# ECLIPSE — LINK CAPACITY / PERFORMANCE VALUES
# ================================

## Modulation Levels

- 256 QAM
- 128 QAM
- 64 QAM

---

## Channel Bandwidth Example

- 55 MHz
- 27.5 MHz

---

## Airlink Capacity (Example — 55 MHz)

- 256 QAM ≈ 366.4 Mbps
- 128 QAM ≈ 312.6 Mbps
- 64 QAM ≈ 267.6 Mbps

---

## Ethernet Throughput

Depends on:
- Packet size (1518 byte vs 64 byte)
- Measurement method (L1 vs L2)
- Framing overhead

---

## XPIC

- Must be enabled and stable for optimal performance

---

## Latency

- Varies by modulation level
- Increases as modulation decreases

---

## Encryption

- Adds minor latency overhead

---

## Key Dependencies

- RF conditions directly impact modulation
- Modulation directly impacts throughput and latency

# ================================
# ECLIPSE — RING NETWORK VALUES
# ================================

## Ring Capacity

- Up to 75 x E1 or 84 x DS1 circuits supported

---

## Circuit Rules

- Each circuit must be unique within the ring
- Circuits cannot be reused

---

## Ring Directions

- Primary: West → East
- Secondary: East → West

---

## Node Roles

- Nodes can act as:
  - Pass-through
  - Drop-and-insert

---

## Ring Types

- North Gateway:
  - Single node acts as traffic gateway

- Any-to-Any:
  - Any node can communicate with any other node

---

## Protection Behavior

- Revertive switching enabled
- Traffic returns to primary path after fault clears

---

## Installation Requirements

- All links must be operational for normal ring state
- Partial links result in wrapped state

---

## Hardware Constraints

- Protection partner plug-ins must be installed
- Slot placement must follow system rules

---

## Frequency Planning

- East and West links should match:
  - Both TX High or both TX Low

  # ================================
# ECLIPSE — ALARM SYSTEM VALUES
# ================================

## Alarm Severity Levels

- Critical
- Major
- Minor
- Warning

---

## Alarm Display Fields

- System Time
- NE Name
- Severity
- Alarm ID
- Object
- Description

---

## Alarm States

- Active
- Cleared

---

## Alarm Dependencies

- RF conditions affect communication alarms
- Hardware status affects equipment alarms
- Environmental conditions affect temperature alarms

---

## Key Rule

- Alarm severity determines response priority

# ================================
# ECLIPSE — NODE CAPACITY VALUES
# ================================

## Backplane Capacity Limits

E1 (2 Mbps):
- Max: 100 circuits
- 200 timeslots

DS1 (1.5 Mbps):
- Max: 127 circuits
- 256 timeslots

STM1 / OC3:
- Max: 2x STM1 (312 Mbps equivalent)

---

## DPP Capacity

- Limited by link modulation capacity
- Max: ~1 Gbps (port limit)

---

## Capacity Allocation Rules

- Backplane allocated first
- Remaining capacity used for DPP

---

## Circuit Usage Rules

Pass-through circuit:
- Uses 2 timeslots

Drop-insert circuit:
- Uses 3 timeslots (higher cost)

---

## Ring Capacity Formula (E1)

Valid if:
- R + d/2 ≤ 100
- 2R + d ≤ 200

Where:
- R = total ring circuits
- d = drop-insert circuits

---

## Ring Capacity Formula (DS1)

Valid if:
- R + d/2 ≤ 128
- 2R + d ≤ 256

---

## Mixed Traffic Formula

Valid if:
- P + R + d/2 ≤ limit

Where:
- P = point-to-point circuits
- R = ring circuits
- d = drop-insert circuits

---

## Ethernet Reduction Rule

- Each DS1 reduces Ethernet capacity by 1.544 Mbps

---

## Licensing Requirement

- DPP requires node-based license

---

## Key Limits

- Backplane = hard system limit
- DPP = link + port limited

# ================================
# PROTECTION SWITCHING — STANDARD ACTIONS
# ================================

## Tx Mute Test

- Enable Tx Mute on primary
- Wait ~2 minutes
- Disable and repeat on secondary

---

## Manual Switch

- Force switch from primary to secondary

---

## Cable Pull (ODU / IRU)

- Disconnect active cable
- Observe failover

---

## RF Path (RIPS)

- Break TX RF path on primary

---

## RAC Pull

- Remove active RAC module

---

## DPP Cable Pull

- Remove active Ethernet data connection

---

## DAC GE3 Tests

Single feed:
- Pull active DAC GE3

Dual feed (LAG):
- Pull primary DAC GE3

Manual:
- Force DAC switch

---

## DAC 16x Tests

- Pull active DAC 16x card
- Pull Y cable connection

---

## Measurement Rule

ALL tests:
→ Record switching time immediately after action

# ================================
# ECLIPSE — CARD REPLACEMENT REQUIREMENTS
# ================================

## General Requirements

- Secondary path must be active
- Protection must be operational

---

## Hardware Requirements

- Compatible hardware revision required
- RAC modules:
  - EXR-600-002 Rev 003+
  - EXR-660-002 Rev 004+

---

## Software Requirements

- Minimum software version required for hitless behavior

---

## Configuration Requirements (NCC)

- Backup configuration file
- User credentials
- Licensing information

---

## Clock Requirements

- Clock must be locked to alternate source before removal

---

## Licensing

- Trial licenses may be required during replacement
- Permanent licenses must be installed after

---

## Replacement Conditions

- Primary must be offline before removal
- Secondary must be locked online during replacement

# ================================
# ECLIPSE — SWITCHING TIME VALUES
# ================================

## Typical Switching Times (ms)

TX Mute:
- ~200 ms (DPP)
- ~50–60 ms (Backplane)

Manual Switch:
- ~100–200 ms

ODU Cable Pull:
- ~50–60 ms

RIPS Switch:
- ~50–60 ms

RAC Pull:
- ~200–500 ms

DAC GE3 Pull:
- ~50–500 ms (depends on configuration)

---

## Protection Switching (IRU 600v3)

Typical ranges:
- 50 ms (fast events)
- 100–200 ms (moderate events)
- 500 ms+ (slow events)

---

## First Switch After Power Cycle

- Up to ~1000 ms

---

## Upgrade Outage Times

Older firmware:
- 200–300 seconds

Newer firmware:
- ~50 seconds or hitless

---

## Measurement Conditions

- Frame size: ~128 bytes
- Frame rate: ~1000 fps
- Port speed: auto-negotiation (or fixed for better performance)

---

## Hardware Requirements

- RAC 60E / 6XE (Rev 003+ / Rev 004+)
- Correct firmware version required

---

## Key Rule

Switching times depend on:
- Hardware
- Software
- Test conditions

# ================================
# ECLIPSE — NMS & CONNECTOR VALUES
# ================================

## NMS Ports

- 10/100Base-T Ethernet (RJ-45)
- Auto MDI/MDIX (no crossover requirement)

---

## RJ-45 Pinout (Ethernet)

1: TX+  
2: TX-  
3: RX+  
6: RX-  

---

## V.24 Maintenance Port

- RJ-45 to DB-9 cable
- Provides serial access

---

## Cable Requirements

- Straight Ethernet cables supported
- Multiple lengths available

---

## DAC 16x Cable Rules

- Each cable supports up to 8 tribs
- Two cables required for full capacity (16 tribs)

---

## Optical Cabling

- Single-mode (1310 nm)
- Multi-mode (850 nm)
- LC, SC, FC connectors supported

---

## Protection Cabling

- Y-cables required for protected operation
- Two assemblies per protected connection

---

## Relay Limits

- Max Voltage: 60V DC
- Max Current: 2A
- Max Power: 60W

---

## Safety Requirement

- No AC mains switching through relay contacts

# Eclipse Installation — System Defaults & Rules

## Default States

- Transmit Mute = ENABLED on first power-up

## Connection Timing

- Minimum 90 seconds before Portal connection

## Access Priority

1. Ethernet
2. DHCP
3. V.24

## Configuration Behavior

- Changes require manual "Send" to apply
- Real-time screen updates do not equal applied config

## RF Constraints

- Frequency, power, modulation:
  → Locked to hardware-supported ranges

## Licensing

- Capacity is license-controlled
- Stored in system memory