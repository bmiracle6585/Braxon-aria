# ================================
# PROTECTION SWITCHING — HARDWARE EVENTS
# ================================

## Implicit Trigger Events

System failover may be triggered by:

- Loss of RF signal
- Loss of TX path
- Card removal
- Cable disconnect
- Data plane interruption

---

## Behavior

These events:
→ Force automatic protection switching
→ Do NOT require manual intervention

# ================================
# CARD REPLACEMENT — SYSTEM EVENTS
# ================================

## Implicit Triggers

- Card removal
- Card insertion
- System restart (NCC restore)
- Clock source switching

---

## Behavior

These events may:
- Trigger protection switching
- Cause temporary traffic interruption
- Initiate system reinitialization

# ================================
# SWITCHING TIME — EVENT TRIGGERS
# ================================

## Trigger Events

- TX mute
- Manual switch
- ODU cable pull
- RAC pull
- DAC pull
- RF path interruption

---

## Behavior

All triggers:
→ Initiate protection switching
→ Cause temporary traffic interruption

# Eclipse Installation — Reboot / Reset Events

## Required Power Cycle

- After configuration restore:
  → INU must be power cycled

## Implicit Risk Events

- Improper ODU disconnect under power
- Software mismatch requiring reload