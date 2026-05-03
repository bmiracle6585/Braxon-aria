# ================================
# SECTION X — VLAN Configuration
# ================================

## Purpose
Configure VLANs, assign ports, and define tagging behavior for traffic transport across the CTR system.

## Workflow Sequence
1. Enable VLAN Module (if not already enabled)
2. Create VLAN
3. Assign Member Ports
4. Define Tagged / Untagged Ports
5. Configure PVID (Port VLAN ID)
6. Configure Port Behavior (Ingress Filtering / Frame Type)
7. Verify VLAN Configuration

---

## Step Details

### 1. Enable VLAN Module
- VLAN module is enabled by default
- Verify before proceeding

---

### 2. VLAN Creation
- Create VLAN with unique VLAN ID

Example:
- VLAN ID: 100

---

### 3. Assign Member Ports
- Add ports that will carry this VLAN

Example:
- Port 1, Port 2 added as members

---

### 4. Tagged vs Untagged Assignment

#### Untagged Ports
- Used for access devices
- Traffic leaves without VLAN tag

#### Tagged Ports
- Used for trunk/backhaul links
- Traffic carries VLAN ID

---

### 5. Configure PVID
- Assign

# ================================
# SECTION — CTR VLAN Provisioning Flow
# ================================

## Purpose
Define the operational sequence ARIA should follow when guiding VLAN provisioning on CTR.

---

## Workflow Sequence

1. Identify service intent
2. Determine bridge mode
3. Identify VLAN IDs
4. Identify ports
5. Create VLAN
6. Assign member ports
7. Define tagged / untagged behavior
8. Configure PVID
9. Configure frame filtering
10. Configure dynamic learning, if required
11. Configure provider bridge behavior, if required
12. Configure protocol tunneling, if required
13. Configure VLAN translation, if required
14. Verify VLAN and port state

---

## Step Details

### 1. Identify Service Intent

Determine whether the VLAN is being used for:

- Simple customer traffic
- Management access
- Backhaul transport
- Multiple VLAN trunking
- Provider bridge / Q-in-Q service
- E-LINE service
- E-LAN service
- Transparent customer LAN extension

ARIA must not start with commands until the service intent is known.

---

### 2. Determine Bridge Mode

CTR supports customer bridge and provider edge bridge behavior.

Use customer bridge mode when:
- CTR behaves like a normal switch
- traffic is untagged or C-VLAN tagged

Use provider edge bridge mode when:
- customer traffic must be transported through a provider network
- customer frames may be encapsulated with S-VLAN tags
- C-VLAN to S-VLAN mapping is required

Changing bridge mode during runtime requires:
- Spanning Tree shut down
- GVRP disabled
- GMRP disabled
- GARP shut down
- Ethernet CFM stopped, if running

---

### 3. Identify VLAN IDs

Collect:
- Customer VLAN ID
- Service VLAN ID, if provider bridge is used
- Management VLAN ID, if applicable
- Native/untagged VLAN ID

Important:
- VLAN 1 exists by default
- VLAN 1 cannot be deleted
- Interface VLAN 1 can be deleted

---

### 4. Identify Ports

For each port, determine:
- Is it customer-facing?
- Is it provider-facing?
- Is it radio/uplink-facing?
- Is it access or trunk-like?
- Should it transmit tagged or untagged frames?

---

### 5. Create Static VLAN

Create the VLAN before assigning MAC entries or multicast behavior.

Required:
- VLAN ID
- Member ports

---

### 6. Assign Member Ports

Member ports are the ports permanently assigned to the VLAN egress list.

Frames belonging to the VLAN are forwarded to ports in the egress list.

---

### 7. Define Tagged / Untagged Ports

If a port is not explicitly configured as untagged, CTR treats it as tagged for that VLAN.

Use untagged when:
- port connects to end-user equipment
- customer device does not tag traffic

Use tagged when:
- port carries VLAN tags
- port connects to another switch
- port carries multiple VLANs
- port is used as trunk/backhaul

---

### 8. Configure Forbidden Ports

Forbidden ports prevent a port from participating in VLAN activity.

Use forbidden ports when:
- a port must never join a VLAN dynamically
- GVRP could otherwise cause unwanted VLAN propagation
- traffic isolation is required

---

### 9. Configure PVID

PVID assigns untagged or priority-tagged ingress frames to a VLAN.

Use PVID when:
- incoming traffic is untagged
- access-port behavior is required
- customer device does not insert VLAN tags

Default PVID is VLAN 1 unless changed.

---

### 10. Configure Acceptable Frame Type

Options:
- Admit all
- Admit only VLAN tagged
- Admit only untagged and priority tagged

Important:
If acceptable frame type is set to tagged, untagged and priority-tagged frames are discarded.

This can cause:
- ping failure
- RFC2544 failure
- customer traffic loss

---

### 11. Configure Ingress Filtering

Ingress filtering blocks frames for VLANs when the receiving port is not a member of that VLAN.

Use ingress filtering when:
- strict VLAN membership enforcement is required
- unwanted VLAN traffic must be dropped

Risk:
- If the port is not a member of the VLAN, traffic is dropped.

---

### 12. Configure Dynamic VLAN Learning

Use GVRP only when dynamic VLAN propagation is intended.

Before relying on GVRP:
- verify global GVRP status
- verify port GVRP status
- verify restricted VLAN registration status

If restricted VLAN registration is enabled:
- the VLAN must already be statically configured
- otherwise it will not be learned dynamically

---

### 13. Configure Dynamic Multicast Learning

Use GMRP when multicast group learning is required.

Before relying on GMRP:
- verify global GMRP status
- verify port GMRP status
- verify restricted group registration status

If restricted group registration is enabled:
- multicast group must already be statically configured
- otherwise it will not be learned dynamically

---

### 14. Configure Static MAC Entries

Static unicast or multicast MAC entries require:
- VLAN already configured
- member ports already configured

Do not configure static MAC entries before the VLAN exists.

---

### 15. Configure Provider Bridge Port Types

If provider bridge is used, configure ports as:

- Customer Edge Port
- Customer Network Port — port-based
- Customer Network Port — S-tagged
- Provider Network Port
- Proprietary Customer Edge Port
- Proprietary Customer Network Port
- Proprietary Provider Network Port

Warning:
Changing a provider bridge port type removes configurations related to that port.

---

### 16. Configure C-VLAN to S-VLAN Mapping

Use CVID registration when customer VLAN traffic must map into a service VLAN.

Required:
- Customer VLAN
- Service VLAN
- Customer-facing port
- Untag behavior toward CEP/PEP

This creates the provider edge service path.

---

### 17. Configure S-VLAN

Use S-VLAN for provider transport.

Service types:
- E-LAN: multipoint-to-multipoint
- E-LINE: point-to-point

Important:
If S-VLAN service type is E-LINE, the VLAN cannot have more than two member ports.

---

### 18. Configure VLAN Translation

Use VLAN translation when interconnecting provider networks using different service VLAN IDs.

Required:
- Local S-VLAN
- Relay S-VLAN
- Port where translation applies

---

### 19. Configure Protocol Tunneling

Use protocol tunneling when customer control protocols must pass transparently through provider network.

Protocols include:
- STP
- GVRP
- GMRP
- IGMP
- Dot1x
- LACP

Possible behavior:
- Tunnel
- Peer
- Discard

---

### 20. Configure PCP / Priority Handling

If service priority matters, configure:
- PCP encoding
- PCP decoding
- PCP selection row
- use-DEI
- service priority regeneration

Use this for provider services where priority preservation or rewriting is required.

---

### 21. Verify Configuration

Verify:
- VLAN database
- VLAN member ports
- untagged ports
- forbidden ports
- PVID
- acceptable frame type
- ingress filtering
- GVRP/GMRP status
- bridge mode
- provider bridge port type
- MAC table
- service VLAN mapping
- protocol tunneling state

---

## CTR VLAN Provisioning Decision Rule

ARIA must always determine:

1. Is traffic supposed to arrive tagged or untagged?
2. What VLAN should that traffic belong to?
3. Is the port a member of that VLAN?
4. Should the traffic leave tagged or untagged?
5. Is any filtering preventing it?
6. Is dynamic learning expected or static config required?
7. Is provider encapsulation involved?