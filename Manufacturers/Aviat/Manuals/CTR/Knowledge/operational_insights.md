# CTR 8300 — Operational Insights

## SYSTEM IDENTITY (CRITICAL)

CTR 8300 is:

- Microwave router
- Carrier Ethernet switch
- TDM pseudowire adapter
- IP/MPLS router :contentReference[oaicite:1]{index=1}

---

## CORE FUNCTION

CTR acts as:

→ Aggregation node  
→ Service delivery node  
→ Transport router  

---

## ARCHITECTURE ROLE

CTR sits between:

- Edge radios (WTM / ODU)
- Core network (MPLS / IP)

---

## NETWORK STACK

CTR operates across:

- Layer 2 (Ethernet switching)
- Layer 2.5 (MPLS)
- Layer 3 (IP routing)

---

## CRITICAL INSIGHT

CTR is NOT:

- just a microwave controller
- just a switch

CTR IS:

→ a full-service transport platform

---

## SERVICE TYPES SUPPORTED

- L2 Ethernet services (VLAN, QinQ)
- L2VPN (VPLS, VPWS)
- L3 routing (OSPF, BGP, IS-IS)
- TDM over packet (CES) :contentReference[oaicite:2]{index=2}

---

## TRAFFIC HANDLING MODEL

CTR can:

- switch traffic (L2)
- route traffic (L3)
- transport services (MPLS)

---

## DEPLOYMENT MODES

CTR can act as:

- Cell site router
- Backhaul aggregation node
- Enterprise access router :contentReference[oaicite:3]{index=3}

---

## RF RELATIONSHIP

CTR connects to:

- ODUs (split-mount radios)
- WTM (all-outdoor radios)

BUT:

→ CTR does NOT behave like a radio system

---

## CAPACITY MODEL

- Up to 1 Gbps per channel
- Supports dual radio (2+0)
- Supports XPIC :contentReference[oaicite:4]{index=4}

---

## CRITICAL DIFFERENCE FROM WTM

WTM:
→ packet + RF endpoint

CTR:
→ transport + aggregation + routing

---

## NETWORK CONTROL POINT

CTR is where:

- VLANs are enforced
- MPLS is built
- routing decisions happen
- QoS policies are applied

---

## ARIA BEHAVIOR RULE

If issue involves:

- multiple sites
- service delivery
- routing paths
- MPLS / VPN

ARIA MUST:

→ prioritize CTR over WTM

# CTR 8300 / 8500 — Operational Insights

## CORE IDENTITY

CTR is a converged transport platform operating at:

- Layer 1 (RF transport)
- Layer 2 (Ethernet switching)
- Layer 3 (IP/MPLS routing) :contentReference[oaicite:1]{index=1}

---

## SYSTEM ROLE

CTR functions as:

- Aggregation node
- Service delivery platform
- Microwave transport controller

---

## NETWORK POSITION

Traffic flow:

WTM / ODU → CTR → Core Network

CTR is the transition point between:

- radio links
- packet network

---

## INTERFACE TYPES

CTR supports:

- RF interfaces (via RAC modules)
- Ethernet (RJ45 / SFP)
- Fiber
- Copper
- TDM (E1 / DS1 pseudowire)

---

## RADIO INTEGRATION

CTR connects to:

- ODU 600 / 300hp
- IRU 600
- WTM radios (via PoE)

CTR does NOT perform RF processing itself.

---

## MODULAR ARCHITECTURE

CTR uses plug-in modules:

- RACx1 / RACx2 → radio interfaces
- PoEx2 → PoE radios (WTM)
- PWR → power redundancy

---

## CRITICAL INSIGHT

CTR = CONTROL + TRANSPORT

WTM / ODU = RF DELIVERY

---

## TRAFFIC CAPABILITIES

CTR supports:

- VLAN / QinQ
- LAG (link aggregation)
- MPLS
- OSPF / BGP / IS-IS
- Pseudowire (TDM over packet) :contentReference[oaicite:2]{index=2}

---

## NETWORK CONTROL POINT

CTR is where:

- VLANs are defined
- routing decisions occur
- QoS is enforced
- services are built

---

## RF CAPABILITY EXTENSION

Through RAC modules, CTR supports:

- adaptive modulation (to 1024 QAM)
- XPIC
- 1+1 protection
- co-path aggregation (L1LA) :contentReference[oaicite:3]{index=3}

---

## CAPACITY MODEL

- multiple RF links aggregated
- multiple interfaces combined
- services transported over shared infrastructure

---

## PROTECTION ARCHITECTURE

CTR supports:

- radio protection (1+1)
- space diversity
- frequency diversity
- chassis protection (stacking)

---

## HARDWARE BEHAVIOR INSIGHT

- plug-in modules can thermal shutdown
- shutdown cascades from slot 4 → slot 1
- restart after 30 minutes :contentReference[oaicite:4]{index=4}

---

## POWER BEHAVIOR

- -48V DC system
- hitless power redundancy via PWR module :contentReference[oaicite:5]{index=5}

---

## CRITICAL FIELD INSIGHT

CTR failures affect:

- multiple links
- multiple services
- entire aggregation segments

---

## ARIA DECISION RULE

If issue spans:

- multiple sites
- multiple services
- routing behavior
- VLAN / MPLS

ARIA must:

→ investigate CTR BEFORE WTM

# ================================
# SECTION — CTR VLAN Operational Insights
# ================================

## VLANs Are a Common Cause of “Good RF, No Traffic”

A CTR link can show:
- good RSL
- good XPD
- no RF alarms
- clean cabling

and still fail traffic tests because VLAN handling is wrong.

ARIA must treat VLAN validation as an early step in:
- no traffic
- RFC2544 failure
- ping failure
- customer handoff issue
- “link up but unusable” complaints

---

## Tagged vs Untagged Is Often the Real Problem

Many field failures come from misunderstanding whether the customer device is tagging traffic.

If the customer device sends untagged traffic:
- CTR must assign that traffic using PVID
- egress may need to be untagged toward the customer

If the customer device sends tagged traffic:
- VLAN ID must be accepted
- port must allow tagged traffic
- VLAN must exist and include that port

---

## PVID Is Invisible but Critical

PVID does not tag the incoming frame physically.
It classifies untagged ingress traffic into a VLAN.

Bad PVID causes:
- traffic placed into wrong VLAN
- ARP failure
- ping failure
- RFC2544 failure

ARIA should always ask:
“What VLAN should untagged traffic be placed into?”

---

## A Port Being Up Does Not Mean VLAN Is Passing

A port can show physical link up while:
- VLAN is missing
- frame type is dropping packets
- ingress filtering blocks frames
- wrong PVID classifies traffic incorrectly
- provider bridge mapping is wrong

ARIA must not equate port-up with service-up.

---

## Acceptable Frame Type Can Silently Kill Traffic

If acceptable frame type is set to tagged:
- untagged frames are discarded
- priority-tagged frames are discarded

This can cause immediate traffic failure if the customer device is not tagging.

---

## Ingress Filtering Is Useful but Dangerous

Ingress filtering prevents VLAN leakage, but it can also drop valid traffic if port membership is wrong.

Use with care:
- verify port is a member of the received VLAN
- verify the VLAN exists
- verify traffic is tagged as expected

---

## Dynamic VLAN Learning Should Not Be Assumed

Do not assume GVRP/GMRP will dynamically fix VLAN transport.

Dynamic learning depends on:
- global protocol state
- port protocol state
- restricted registration setting
- static preconfiguration when restricted mode is enabled

ARIA should treat dynamic learning as intentional, not automatic.

---

## Provider Bridge Config Is Not Normal VLAN Config

Provider bridge introduces:
- C-VLAN
- S-VLAN
- CEP
- CNP
- PNP
- PEP
- VLAN translation
- protocol tunneling
- PCP/DEI priority handling

ARIA must not troubleshoot provider bridge services using only basic access/trunk logic.

---

## Changing Provider Port Type Can Wipe Related Configuration

When provider bridge port type is changed, related configurations on that port are removed.

Operational risk:
- a working service can break after changing port type
- mappings may need to be rebuilt
- verification must be repeated

---

## E-LINE vs E-LAN Matters

E-LINE:
- point-to-point
- no more than two member ports

E-LAN:
- multipoint-to-multipoint
- default S-VLAN service type

Wrong service type causes wrong forwarding assumptions.

---

## Multiple Instances Can Look Like VLAN Failure

On CTR 8540 with multiple switch instances:
- same VLAN ID in different switch instances does not guarantee connectivity
- ports must be mapped to the correct switch instance
- hosts in different instances may not communicate

ARIA must check switch instance mapping when VLAN config appears correct but traffic still fails.

---

## Field Rule

For traffic failure with good RF, ARIA should say:

“Before touching alignment, let’s prove the VLAN path:
VLAN ID, tag state, PVID, member ports, acceptable frame type, ingress filtering, and MAC learning.”