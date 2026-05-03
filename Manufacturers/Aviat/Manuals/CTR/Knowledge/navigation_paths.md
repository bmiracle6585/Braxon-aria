# ================================
# SECTION — CTR VLAN Navigation / Verification Commands
# ================================

## VLAN Device Status

### Show VLAN Device Info
Command:
show VLAN device info

Use to verify:
- VLAN status
- VLAN operational status
- GVRP status
- GMRP status
- MAC-VLAN status
- Protocol-VLAN status
- Bridge mode
- traffic classes
- learning mode
- max VLAN ID
- max supported VLANs
- global MAC learning status

---

## VLAN Database

### Show VLAN Summary
Command:
show VLAN summary

Use to verify:
- total number of VLANs configured

---

### Show All VLANs
Command:
show VLAN

Use to verify:
- VLAN ID
- member ports
- untagged ports
- forbidden ports
- VLAN status
- egress EtherType
- service type
- MAC learning status

---

### Show Specific VLAN
Command:
show VLAN id <vlan-id>

Use to verify:
- specific VLAN membership
- untagged behavior
- forbidden ports
- VLAN status

---

## VLAN Port Configuration

### Show Port VLAN Config
Command:
show VLAN port config port gigabitethernet <slot/port>

Use to verify:
- Port VLAN ID / PVID
- acceptable frame type
- ingress filtering
- port mode
- GVRP status
- GMRP status
- restricted VLAN registration
- restricted group registration
- MAC-based support
- protocol-based support
- default priority

---

## FID / Learning

### Show FID Detail
Command:
show fid detail

Use to verify:
- VLAN learning mode
- FID to VLAN mapping

---

## Static MAC Tables

### Show Static Unicast MAC Entries
Command:
show mac-address-table static unicast

Use to verify:
- VLAN
- MAC address
- receive port
- output ports
- static unicast forwarding

---

### Show Static Multicast MAC Entries
Command:
show mac-address-table static multicast

Use to verify:
- VLAN
- multicast MAC
- receive port
- member ports
- forbidden ports

---

### Show MAC Address Table
Command:
show mac-address-table

Use to verify:
- learned MAC addresses
- static MAC addresses
- VLAN association
- learned ports

---

## Dynamic VLAN / Multicast Registration

### Show GVRP/GMRP Port Status
Command:
show VLAN port config port gigabitethernet <slot/port>

Use to verify:
- GVRP enabled/disabled
- GMRP enabled/disabled
- failed GVRP registrations
- last GVRP PDU origin

---

## Forwarding Behavior

### Show Forward-All
Command:
show forward-all

Use to verify:
- VLAN forward-all ports
- static forward-all ports
- forbidden forward-all ports

---

### Show Forward-Unregistered
Command:
show forward-unregistered

Use to verify:
- unregistered forwarding ports
- static unregistered ports
- forbidden unregistered ports

---

## VLAN Classification

### Show Protocol Groups
Command:
show VLAN protocols-group

Use to verify:
- frame type
- protocol
- protocol group ID

---

### Show Protocol VLAN Mapping
Command:
show protocol-VLAN

Use to verify:
- port
- protocol group
- VLAN ID mapping

---

### Show MAC VLAN
Command:
show mac-VLAN

Use to verify:
- MAC address to VLAN mapping

---

### Show MAC VLAN by Interface
Command:
show mac-vlan interface gigabitethernet <slot/port>

Use to verify:
- interface-specific MAC VLAN mapping
- multicast/broadcast handling

---

## Dot1q Tunnel / Protocol Tunnel

### Show Dot1q Tunnel Interface
Command:
show Dot1q-tunnel interface gigabitethernet <slot/port>

Use to verify:
- Dot1q tunneling enabled on interface

---

### Show L2 Protocol Tunnel
Command:
show l2protocol-tunnel

Use to verify:
- tunneled protocol
- encapsulation counter
- decapsulation counter

---

### Show L2 Protocol Tunnel MAC Addresses
Command:
show l2protocol tunnel-mac-address

Use to verify:
- protocol tunnel MAC addresses for Dot1x, LACP, STP, GVRP, GMRP, LLDP, ECFM, etc.

---

## Bridge Mode

### Show Bridge Mode
Command:
show VLAN device info

Use to verify:
- Customer Bridge
- Provider Edge Bridge
- Provider Core Bridge
- Provider Bridge

---

## Provider Bridge

### Show Provider Bridge Port Config
Command:
show provider-bridge port config port gigabitethernet <slot/port>

Use to verify:
- port type
- tunnel status
- service VLAN classification
- ingress EtherType
- egress EtherType
- VLAN translation status
- EtherType swap status
- use-DEI
- PCP selection row
- MAC learning status
- MAC learning limit

---

### Show Provider Edge Port Configuration
Command:
show provider-bridge pep configuration

Use to verify:
- service VLAN ID
- port VLAN ID
- acceptable frame type
- ingress filtering
- default priority
- COS preservation
- operational status

---

### Show Service VLAN CVLAN Mapping
Command:
show service vlan cvlan

Use to verify:
- service VLAN
- customer VLAN
- port
- untagged PEP setting
- untagged CEP setting
- relay CVLAN ID
- service VLAN priority

---

### Show Service VLAN Mapping
Command:
show service vlan mapping

Use to verify:
- local service VLAN
- relay service VLAN
- translation mapping

---

### Show Provider Bridge PCP Encoding
Command:
show provider-bridge pcp encoding

Use to verify:
- PCP encoding table

---

### Show Provider Bridge PCP Decoding
Command:
show provider-bridge pcp decoding

Use to verify:
- PCP decoding table

---

### Show Provider Bridge Priority Regeneration
Command:
show provider-bridge priority regen

Use to verify:
- received priority
- regenerated priority

---

## Spanning Tree

### Show Spanning Tree
Command:
show spanning-tree

Use to verify:
- root bridge
- bridge ID
- port role
- port state
- MST/RSTP state

---

### Show Customer Spanning Tree
Command:
show customer spanning-tree

Use to verify:
- C-VLAN component spanning tree
- CEP/PEP forwarding state