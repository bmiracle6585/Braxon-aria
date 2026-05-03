# ================================
# ECLIPSE — PERFORMANCE CONFIG CONTEXT
# ================================

## Modulation Profiles

- Fixed modulation (manual)
- Adaptive modulation (ACM)

---

## ACM Configuration

- Allows dynamic adjustment of modulation
- Based on RF conditions

---

## XPIC Configuration

- Enables dual polarization operation
- Improves spectral efficiency

# ================================
# ECLIPSE — RING CONFIG CONTEXT
# ================================

## Ring Configuration Requirements

- Define:
  - Number of nodes
  - Node types
  - Circuit allocation
  - Ring type (North Gateway / Any-to-Any)

---

## Circuit Planning

- Identify:
  - Drop-insert circuits per node
  - Pass-through circuits per node

---

## Protection Configuration

- Partner plug-ins must be assigned
- Protection configured via system interface

---

## Commissioning Requirement

- Each link must be verified operational before closing ring

# ================================
# ECLIPSE — ALARM CONFIG CONTEXT
# ================================

## Alarm Monitoring

- Accessible via system interface
- Displays real-time system status

---

## Alarm Management

- Alarms must be monitored continuously
- Clearing alarms requires resolving root condition

# ================================
# ECLIPSE — CAPACITY CONFIG CONTEXT
# ================================

## Capacity Planning Inputs

- Number of circuits (E1 / DS1)
- Drop-insert requirements
- Pass-through requirements
- Ethernet bandwidth requirements

---

## Configuration Order

1. Configure backplane circuits
2. Allocate PDH traffic
3. Assign remaining capacity to Ethernet (DPP)

---

## DPP Configuration

- Requires compatible hardware (DAC GE / DAG GE3)
- Must ensure licensing is applied

---

## Multi-Link Operation

- Co-channel links increase RF capacity
- Must validate node capacity can support combined load

# ================================
# PROTECTION SWITCHING — TEST INPUTS
# ================================

## Required Hardware

- RAC 60 / 6X modules
- Correct firmware revisions:
  - EXR-600-002 Rev 003+
  - EXR-660-002 Rev 004+

---

## Required Equipment

- Test measurement system (Spirent / equivalent)
- BNC to SMA adapters (for cable tests)

---

## Test Conditions

- Primary/Secondary paths configured
- Protection enabled
- Hardware fully operational before test

---

## Measurement Requirements

- Switching times must be recorded externally
- System logs alone are insufficient

# ================================
# ECLIPSE — CARD REPLACEMENT STEPS
# ================================

## Standard Replacement Flow

1. Lock secondary online
2. Remove faulty primary
3. Insert replacement card
4. Wait for boot
5. Unlock secondary

---

## Optional Reversion

1. Force switch back to primary
2. Lock primary
3. Restore secondary
4. Unlock primary

Note:
→ Causes traffic hit

---

## NPC Replacement

1. Lock clock source to NCC
2. Remove NPC
3. Insert replacement
4. Unlock clock

---

## NCC Replacement (Advanced)

1. Stage replacement in separate chassis
2. Configure:
   - Time/date
   - Licensing
   - Restore config
3. Power down staged unit
4. Lock clock to NPC
5. Replace NCC
6. Power up
7. Unlock clock

---

## DAC / RAC Replacement

- Follow standard protected module process
- Ensure correct module type (DPP vs backplane)

# ================================
# ECLIPSE — SWITCHING TEST CONTEXT
# ================================

## Required Conditions

- Protection enabled
- System fully operational
- Test equipment connected

---

## Test Setup

- Ethernet tester (Spirent or equivalent)
- Defined frame size and rate
- Stable RF link

---

## Configuration Impact

- Fixed Ethernet speed improves switching time
- Clean cable pulls required for valid results

# ================================
# ECLIPSE — ACCESS CONFIG CONTEXT
# ================================

## NMS Access Setup

- Connect via Ethernet port
- Use Portal or ProVision for access

---

## Maintenance Access

- Use V.24 serial connection
- Requires RJ-45 to DB-9 cable

---

## Cable Installation Rules

- Separate signal cables from power cables
- Use surge suppression for external connections

---

## Protection Setup

- Use Y-cable assemblies for redundancy
- Ensure correct cable orientation (TX/RX)

---

## AUX / Alarm Setup

- Configure relay behavior
- Connect auxiliary interfaces as required

# Eclipse Installation — Required Inputs

## Required Before Configuration

- Installation datapack
- Frequency plan
- Power levels
- Modulation / bandwidth settings
- IP addressing scheme
- Routing requirements
- Licensing details

## Required During Install

- Terminal name
- Site name
- Contact details
- Site grid

## RF Validation Data

- Expected RSL values
- Alignment targets

## Testing Requirements

- BER or RFC2544 capability
- Loopback availability