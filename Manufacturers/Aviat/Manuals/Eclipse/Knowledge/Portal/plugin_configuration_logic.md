# Plugin Configuration Logic (Core System Intelligence)

## Overview
Node Plug-ins define how the Eclipse system operates at a functional level. All link behavior, RF performance, protection, and data handling are controlled here.

Access Path:
Configuration > Plug-Ins

## Core Concept
Each plug-in = a functional module:

- LINK / RING → Radio behavior
- DATA (DAC) → Tributary / transport
- AUX → Alarm + IO
- NCM → Control / management

System operates based on **module relationships**, not individual settings.

---

## Slot-Based Architecture
- Each plug-in is assigned to a physical slot
- Configuration must match installed hardware
- Mismatch = system instability or failure

---

## Configuration Flow (REAL WORLD)

1. Verify installed modules (System Summary)
2. Open Plug-ins screen
3. Select module (LINK / DATA / AUX)
4. Configure:
   - RF parameters
   - Capacity
   - Protection
   - Interfaces
5. Apply (Send)

---

## Critical Rule

Protection MUST be defined BEFORE link configuration

Reason:
System auto-synchronizes radios based on protection mode