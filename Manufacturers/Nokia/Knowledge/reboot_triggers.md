# CorEvo Section 1 — Reboot Triggers

## Actions That Cause Reboot

### Startup/System Settings Changes
- Any changes made in Startup Settings will cause the node to reboot

---

### SNMP Version Change
- Changing SNMP from V2 to V3 causes CorEvo card reboot

---

## Impact
- Temporary loss of connectivity
- Session interruption
- Requires technician awareness before applying changes

# ================================
# SECTION 2 — Reboot Triggers
# ================================

- Applying IP Addressing / OSPF configuration → CorEvo card reboot
- Enabling IPv6 stack and applying changes → CorEvo card reboot
- Enabling Static LAG Criteria → CorEvo card reboot (service impacting)

# ================================
# SECTION 8 — Reboot Triggers
# ================================

- Database Scratch (Web) → Full node reboot
- Physical DB Scratch → Multiple reboots during process
- Restore and Activate (MIB) → Node restart

# Alarm Procedures That May Require Restart or Power Cycle

Use caution. These actions may interrupt traffic.

Known restart/power-cycle related procedures:
- Clock Failure
- Combiner Loss of Alignment
- Dialog Failure
- Some MPT-HLC/MPT-HLS communication failures
- UBT power-source reset procedures

Before recommending restart or power cycle:
1. Confirm whether the radio/link is protected or unprotected.
2. Confirm whether traffic is affected.
3. Confirm whether a maintenance window is required.
4. If protected, perform required forced/lockout protection switches before service-affecting work.
5. Release forced/lockout switches after clearing.