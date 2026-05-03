# ================================
# SECTION — CTR VLAN Defaults & Required Values
# ================================

## VLAN Defaults

- VLAN module status: Enabled
- Default VLAN ID: 1
- Default VLAN 1 cannot be deleted
- Default L3 interface VLAN 1 can be deleted
- MAC address table aging time: 300 seconds
- Acceptable frame type: Admit all
- Ingress filtering: Disabled
- Switch port priority: 0
- Switch port mode: Hybrid
- GVRP module status: Disabled
- GMRP module status: Disabled
- MAC-based VLAN classification: Disabled
- Protocol-based VLAN classification: Enabled
- Tunneling: Disabled
- Max traffic classes per port: 8

---

## GARP Timer Defaults

- Join timer: 20 seconds
- Leave timer: 60 seconds
- Leave-all timer: 1000 seconds

Rules:
- Leave timer must be two times greater than Join timer
- Leave-all timer must be greater than Leave timer

---

## VLAN Limits

- VLAN ID range: 1–4094
- Max VLAN ID shown by device: 4094 / 4096 depending output context
- Max supported VLANs shown in examples: 1024 or 250 depending mode/output context

ARIA must not assume the limit without checking device output.

---

## VLAN 1 Rules

- VLAN 1 is the default VLAN
- VLAN 1 cannot be deleted
- Interface VLAN 1 can be deleted
- Default PVID is VLAN 1 unless changed

---

## Static VLAN Requirements

Before static MAC configuration:
- VLAN must exist
- member ports must be configured

Required static VLAN values:
- VLAN ID
- member ports
- untagged ports, if any
- forbidden ports, if any

---

## Tagged / Untagged Defaults

If a port is added to a VLAN but not explicitly set as untagged:
- traffic egresses tagged

If a port is configured as untagged:
- traffic egresses without VLAN tag

---

## Acceptable Frame Type Options

Valid behaviors:
- Admit all
- Admit only VLAN tagged
- Admit only untagged and priority tagged

Important:
- If set to tagged, untagged and priority-tagged frames are discarded.
- This can break ping, RFC2544, and normal customer traffic if the connected device sends untagged frames.

---

## Ingress Filtering Default

- Disabled by default

When enabled:
- frames are dropped if they arrive on a port that is not a member of that VLAN

---

## Bridge Mode Defaults

Supported bridge modes:
- Customer Bridge
- Provider Edge Bridge

Provider bridge / Q-in-Q behavior may require feature support and has release limitations.

---

## Provider Bridge Port Types

Supported / referenced port types:
- Customer Edge Port
- Customer Network Port — port-based
- Customer Network Port — S-tagged
- Provider Network Port
- Proprietary Customer Edge Port
- Proprietary Customer Network Port
- Proprietary Provider Network Port

Default provider bridge port type:
- Provider Network Port

Warning:
- Changing a provider bridge port type automatically removes configurations related to that port.

---

## Provider Edge Port Defaults

Provider Edge Port default values:
- PVID: first C-VLAN ID mapped to the service instance
- Default user priority: 0
- Ingress filtering: Disabled
- Acceptable frame types: Admit all

Provider Edge Port is operationally up only if:
- corresponding Customer Edge Port is operationally up
- corresponding S-VLAN is active

---

## S-VLAN Service Types

Supported service types:
- E-LAN: multipoint-to-multipoint
- E-LINE: point-to-point

Default S-VLAN service type:
- E-LAN

E-LINE rule:
- VLAN cannot have more than two member ports

---

## Provider EtherType Defaults

Provider network S-tag EtherType:
- 0x88a8

Customer VLAN EtherType:
- 0x8100

Default PNP ingress/egress EtherType:
- 0x88a8

Default CEP ingress EtherType:
- 0x8100

Default PPNP ingress/egress EtherType:
- 0x8100

---

## PCP / Priority Defaults

PCP selection row examples:
- 8P0D
- 7P1D
- 6P2D
- 5P3D

Default use-DEI:
- False

Default priority regeneration:
- received priority equals regenerated priority

---

## MAC Learning Defaults

Global MAC learning:
- Enabled

Provider bridge MAC learning:
- Enabled by default on ports shown in examples

MAC learning limit examples:
- 150 on some provider bridge ports
- 8000 on other provider/customer bridge outputs

ARIA must check actual device output before assuming limit.

---

## Restricted Registration Defaults

Restricted VLAN registration:
- Disabled by default

Restricted group registration:
- Disabled by default

If restricted VLAN registration is enabled:
- VLAN is learned dynamically only if statically configured

If restricted group registration is enabled:
- multicast group is learned dynamically only if statically configured

---

## Multiple Instance Behavior

When CTR 8540 uses multiple switch instances:
- ports must be mapped to switch instances
- VLANs are configured per switch instance
- devices in different switch instances do not communicate by default