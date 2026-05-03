# ================================
# SECTION — CTR VLAN Configuration Data
# ================================

## Purpose
Capture all required VLAN, bridge-mode, tagging, filtering, and provider-bridge values before configuring or troubleshooting VLAN transport.

---

## Required VLAN Inputs

### Basic VLAN Data
- VLAN ID
- VLAN name, if used
- Required member ports
- Required untagged ports
- Required forbidden ports
- Whether VLAN must be active without member ports
- Whether VLAN is Layer 2 only or has an L3 VLAN interface

---

## Port-Level Inputs

For each involved port collect:

- Physical port ID
- Port mode:
  - Hybrid
  - Access
  - Dot1q-tunnel
- PVID
- Tagged or untagged behavior
- Acceptable frame type:
  - Admit all
  - Admit only VLAN tagged
  - Admit only untagged and priority tagged
- Ingress filtering:
  - Enabled
  - Disabled
- GVRP status
- GMRP status
- Restricted VLAN registration status
- Restricted group registration status
- MAC-based VLAN support
- Port-and-protocol VLAN support
- Default priority

---

## Static VLAN Inputs

To create a static VLAN, ARIA must know:

- VLAN ID
- Member ports
- Which ports egress tagged
- Which ports egress untagged
- Which ports are forbidden

Important:
- If a port is not explicitly configured as untagged, CTR treats it as tagged for that VLAN.
- Untagged ports are normally used toward end devices.
- Tagged ports are normally used toward trunks, uplinks, radios, or downstream switches.

---

## PVID Inputs

For untagged or priority-tagged ingress traffic, collect:

- Port receiving untagged traffic
- VLAN ID that should be assigned to that traffic
- Whether far-end expects that VLAN tagged or untagged

PVID determines what VLAN untagged ingress traffic belongs to.

---

## Dynamic VLAN Learning Inputs

If GVRP is involved, collect:

- Is GVRP enabled globally?
- Is GVRP enabled on the port?
- Is restricted VLAN registration enabled?
- Is the VLAN statically configured on the receiving switch?

Dynamic VLAN learning will fail if:
- GVRP is disabled globally
- GVRP is disabled on the port
- restricted VLAN registration is enabled and the VLAN is not statically configured

---

## Dynamic Multicast Learning Inputs

If GMRP is involved, collect:

- Is GMRP enabled globally?
- Is GMRP enabled on the port?
- Is restricted group registration enabled?
- Is the multicast group statically configured?

Dynamic multicast learning will fail if:
- GMRP is disabled globally
- GMRP is disabled on the port
- restricted group registration is enabled and the group is not statically configured

---

## VLAN Classification Inputs

ARIA must determine how frames are classified into VLANs.

Classification methods:
1. VLAN tag
2. MAC-based classification
3. Protocol-based classification
4. PVID / port-based classification

Required data:
- Is the incoming frame tagged?
- Source MAC, if MAC-based VLAN is used
- Protocol group, if protocol-based VLAN is used
- PVID, if untagged traffic is used

---

## MAC-Based VLAN Inputs

Collect:
- Source MAC address
- VLAN ID assigned to that MAC
- Interface where MAC classification applies
- Whether multicast/broadcast is allowed

---

## Protocol-Based VLAN Inputs

Collect:
- Frame type
- Protocol value
- Protocol group ID
- VLAN mapped to the protocol group
- Interface where protocol classification applies

Example use:
- ARP packets can be classified into a specific VLAN using protocol-based VLAN rules.

---

## Frame Filtering Inputs

Collect:
- Acceptable frame type on each port
- Whether ingress filtering is enabled
- Whether the port is a member of the VLAN being received
- Whether filtering utility criteria is default or enhanced

---

## Provider Bridge Inputs

If provider bridge behavior is used, collect:

- Bridge mode:
  - Customer Bridge
  - Provider Edge Bridge
  - Provider Core Bridge
  - Provider Bridge / Q-in-Q
- Port type:
  - Customer Edge Port
  - Customer Network Port — port-based
  - Customer Network Port — S-tagged
  - Provider Network Port
  - Proprietary Customer Edge Port
  - Proprietary Customer Network Port
  - Proprietary Provider Network Port
- C-VLAN ID
- S-VLAN ID
- CVID-to-SVID mapping
- Customer VLAN PVID
- Service VLAN classification method
- Ingress EtherType
- Egress EtherType
- VLAN translation status
- EtherType swap status
- MAC learning status and limit

---

## Provider Service Inputs

For provider services, collect:

- Service VLAN ID
- Customer VLAN ID
- Service type:
  - E-LINE
  - E-LAN
- Customer-facing port
- Provider-facing port
- Whether traffic should be transparent
- Whether customer control protocols should tunnel, peer, or discard

---

## VLAN Translation Inputs

Collect:
- Local service VLAN
- Relay service VLAN
- Port where translation applies
- Whether service VLAN translation is enabled

VLAN translation provides one-to-one bidirectional mapping between local S-VLAN and relay S-VLAN.

---

## Priority / PCP Inputs

If priority handling is used, collect:

- PCP selection row:
  - 8P0D
  - 7P1D
  - 6P2D
  - 5P3D
- PCP encoding rules
- PCP decoding rules
- Whether DEI is used
- Service priority regeneration rules
- Received priority
- Regenerated priority

---

## Protocol Tunneling Inputs

For L2 protocol tunneling, collect:

- Protocol:
  - STP
  - GVRP
  - GMRP
  - IGMP
  - Dot1x
  - LACP
- Tunnel behavior:
  - Tunnel
  - Peer
  - Discard
- Tunnel MAC address, if non-default
- Customer point of attachment port
- Service VLAN carrying tunneled traffic

---

## Multiple Instance Inputs

If CTR 8540 multiple instances are used, collect:

- Switch instance ID
- Ports mapped to each switch instance
- VLANs configured per switch instance
- Whether traffic is expected between switch instances

Important:
- Hosts in the same switch instance can communicate if VLAN settings allow.
- Hosts in different switch instances will not communicate unless explicitly connected/routed.