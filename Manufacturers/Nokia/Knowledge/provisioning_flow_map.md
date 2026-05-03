# CorEvo Provisioning Flow Map

## High-Level Flow

1. Foundation Setup (Section 1)
2. IP / Routing (Section 2)
3. User + Alarm Profiles (Section 3)
4. Hardware Configuration (Section 4)
5. Ports / RF / Services (Section 5)
6. RLAG + VLAN (Section 6)
7. QoS / Sync / PM (Section 7)
8. Recovery / Reset (Section 8)

---

## Critical Dependencies

### Section 1 → ALL
- Must be completed before anything else

---

### Section 2 (IP / OSPF)
- Required before:
  - RF routing
  - NSP discovery

---

### Section 4 (Hardware)
- Must be complete before:
  - Port creation
  - RF configuration

---

### Section 5 (RF)
- RF must be ONLINE before:
  - Routing validation
  - Performance monitoring

---

### Section 6 (RLAG)
- Requires:
  - RF configured
  - PPP disabled (if needed)

---

### Section 7 (QoS / Sync)
- Applied after:
  - Services
  - VLANs
  - RF links established

---

### Section 8 (Recovery)
- Used ONLY when:
  - Config failure
  - Corruption
  - Rebuild required

---

## Hard Stop Conditions

- Missing VLANs (Verizon)
- Missing IP plan
- RF not ONLINE
- PPP active when adding to LAG
- No MIB backup before reset

---

## Validation Checkpoints

Before moving forward, ARIA should confirm:

- Session stable (timeout set)
- Site info entered
- IP addressing verified
- RF status = ONLINE
- VLAN assigned correctly
- TX unmuted
- PM enabled

---

## Completion State

Provisioning is complete when:

- RF links are ONLINE
- Routing is active (OSPF/PPP)
- VLAN traffic is passing
- QoS applied
- Synchronization correct
- PM monitoring active

# Alarm Clearing Decision Logic

ARIA must follow this order:

1. Identify alarm.
2. Decode friendly name/entity.
3. Identify equipment/facility.
4. Determine traffic/sync impact.
5. Check related alarms.
6. Determine whether the issue is:
   - RF path
   - Ethernet path
   - Sync/PTP path
   - Power
   - Cabling/SFP
   - Provisioning mismatch
   - Protection state
   - Hardware failure
7. Clear root alarms first.
8. Retrieve alarms again.
9. Escalate only if procedure fails.

Never jump directly to replacement unless the Nokia procedure says replacement is the next step.