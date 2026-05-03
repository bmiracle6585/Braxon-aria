# CTR 8300 — Failure Modes

## LINK UP / SERVICE DOWN

Cause:

→ MPLS / VLAN / routing issue

NOT RF

---

## PARTIAL SERVICE FAILURE

Cause:

→ QoS / policing / shaping

---

## SITE REACHABLE / SERVICE NOT WORKING

Cause:

→ pseudowire / MPLS issue

---

## INTERMITTENT SERVICE

Cause:

→ routing instability
→ LAG instability
→ synchronization issues

---

## TOTAL NETWORK IMPACT

Cause:

→ CTR failure affects MULTIPLE WTM links

---

## CRITICAL INSIGHT

CTR failures scale:

- WTM failure = 1 link affected
- CTR failure = multiple services affected

# ================================
# SECTION — CTR VLAN Failure Modes
# ================================

## Purpose
Teach ARIA how VLAN misconfiguration causes traffic failure even when RF, alignment, and cabling appear healthy.

---

## VLAN Failure Principle

A CTR radio path can be physically and RF healthy while customer traffic fails because VLAN handling is wrong.

ARIA must not assume:
- RF failure
- bad cable
- bad radio

until VLAN path is validated.

---

## Failure Mode: VLAN ID Mismatch

### Pattern
Side A sends traffic on one VLAN.
Side B expects another VLAN.

### Symptoms
- link up
- no customer traffic
- ping fails
- RFC2544 fails
- MAC learning may not appear as expected

### ARIA Checks
- compare VLAN ID on both ends
- verify `show VLAN`
- verify service VLAN mapping if provider bridge is used

---

## Failure Mode: Tagged / Untagged Mismatch

### Pattern
One side sends tagged frames.
The other side expects untagged frames, or vice versa.

### Symptoms
- traffic silently fails
- ping fails
- RFC2544 fails
- port shows up but no usable traffic

### ARIA Checks
- verify untagged ports in VLAN database
- verify acceptable frame type
- verify PVID
- verify connected device tagging behavior

---

## Failure Mode: Wrong PVID

### Pattern
Untagged traffic enters the correct physical port but is assigned to the wrong VLAN.

### Symptoms
- untagged customer traffic disappears
- traffic goes into wrong VLAN
- ARP fails
- ping fails

### ARIA Checks
- `show VLAN port config port <port>`
- confirm Port VLAN ID
- confirm expected VLAN for untagged traffic

---

## Failure Mode: Port Not a VLAN Member

### Pattern
Traffic enters or exits on a port that is not a member of the VLAN.

### Symptoms
- no forwarding
- one direction may work while the other fails
- ingress filtering may drop traffic

### ARIA Checks
- verify member ports
- verify ingress filtering
- verify egress VLAN membership

---

## Failure Mode: Acceptable Frame Type Drops Traffic

### Pattern
Port is configured to admit only tagged frames, but customer sends untagged frames.

### Symptoms
- ping fails after frame type change
- RFC2544 fails
- no traffic from untagged device

### ARIA Checks
- verify acceptable frame type
- if customer sends untagged, port must not be tagged-only
- confirm whether customer device inserts VLAN tag

Manual behavior:
- when acceptable frame type is set to tagged, untagged and priority-tagged frames are discarded.

---

## Failure Mode: Ingress Filtering Drops Frames

### Pattern
Ingress filtering is enabled and traffic arrives for a VLAN where the port is not a member.

### Symptoms
- traffic received but dropped
- VLAN appears configured elsewhere but not on ingress port
- no forwarding

### ARIA Checks
- verify ingress filtering
- verify port membership in received VLAN

---

## Failure Mode: GVRP Not Learning VLAN

### Pattern
Dynamic VLAN learning expected, but VLAN is not learned.

### Causes
- GVRP disabled globally
- GVRP disabled on port
- restricted VLAN registration enabled
- VLAN not statically configured when restricted registration is enabled

### Symptoms
- expected dynamic VLAN missing
- traffic not passed
- remote switch lacks VLAN

### ARIA Checks
- `show VLAN device info`
- `show VLAN port config port <port>`
- `show VLAN`

---

## Failure Mode: GMRP Not Learning Multicast Group

### Pattern
Dynamic multicast learning expected, but multicast group is not learned.

### Causes
- GMRP disabled globally
- GMRP disabled on port
- restricted group registration enabled
- group not statically configured

### Symptoms
- multicast traffic fails
- group MAC missing from MAC table
- multicast only works when static entry is configured

---

## Failure Mode: Forbidden Port Blocks VLAN

### Pattern
Port is forbidden from VLAN participation.

### Symptoms
- dynamic join ignored
- port never participates in VLAN
- traffic does not pass even though GVRP may be active

### ARIA Checks
- verify forbidden ports in VLAN database
- remove forbidden status if port should carry VLAN

---

## Failure Mode: Bridge Mode Mismatch

### Pattern
Customer bridge behavior expected, but provider bridge behavior is configured, or vice versa.

### Symptoms
- unexpected tagging
- S-VLAN/C-VLAN mapping wrong
- provider bridge commands not behaving as expected
- customer traffic not transparent

### ARIA Checks
- show VLAN device info
- confirm Bridge Mode
- confirm service intent

---

## Failure Mode: Provider Bridge Port Type Change Removed Config

### Pattern
Port type is changed after service configuration.

### Symptoms
- previous service stops working
- CVID/SVID mapping disappears
- provider bridge behavior changes

### ARIA Rule
Changing provider bridge port type removes configurations related to that port.

Always re-check provider bridge config after port-type changes.

---

## Failure Mode: C-VLAN / S-VLAN Mapping Wrong

### Pattern
Customer VLAN maps to wrong service VLAN.

### Symptoms
- customer traffic enters provider network but does not exit correctly
- traffic delivered to wrong service
- RFC2544 fails across provider service

### ARIA Checks
- `show service vlan cvlan`
- customer VLAN ID
- service VLAN ID
- customer edge port
- provider edge port

---

## Failure Mode: S-VLAN Inactive

### Pattern
Provider Edge Port cannot come operationally up because the S-VLAN is not active.

### Symptoms
- Provider Edge Port oper status down
- service does not pass
- customer port may be up but provider service inactive

### ARIA Checks
- verify S-VLAN active
- verify CEP operational state
- verify Provider Edge Port status

---

## Failure Mode: E-LINE Has Too Many Member Ports

### Pattern
S-VLAN is configured as E-LINE but more than two member ports are expected.

### Symptoms
- service config invalid or traffic behavior unexpected

### ARIA Rule
E-LINE is point-to-point and cannot have more than two member ports.

---

## Failure Mode: VLAN Translation Wrong

### Pattern
Local S-VLAN and relay S-VLAN mapping does not match provider network expectations.

### Symptoms
- provider interconnect fails
- traffic works in one provider domain but not across boundary
- wrong service VLAN appears downstream

### ARIA Checks
- `show service vlan mapping`
- local S-VLAN
- relay S-VLAN
- translation status

---

## Failure Mode: EtherType Mismatch

### Pattern
Provider network expects a different S-tag EtherType.

### Symptoms
- tagged traffic not recognized
- frames treated incorrectly
- provider bridge interop failure

### ARIA Checks
- ingress EtherType
- egress EtherType
- EtherType swap table
- 0x88a8 vs 0x8100 behavior

---

## Failure Mode: Protocol Tunneling Misconfigured

### Pattern
Customer control protocols are peered or discarded instead of tunneled.

### Symptoms
- customer STP/GVRP/GMRP behavior fails across provider network
- LACP across provider network fails
- Dot1x behavior fails

### ARIA Checks
- tunnel / peer / discard status
- customer point of attachment
- service VLAN
- protocol-specific tunnel state

---

## Failure Mode: MAC Learning Disabled or Limit Reached

### Pattern
Dynamic MAC learning is disabled or MAC limit is too low.

### Symptoms
- unknown unicast flooding
- traffic fails after MAC table limit
- customer devices intermittently unreachable

### ARIA Checks
- MAC learning status
- MAC learning limit
- MAC address table

---

## Failure Mode: Multiple Instance Isolation

### Pattern
Ports are mapped to different switch instances.

### Symptoms
- hosts on same VLAN ID cannot communicate
- ping works within one switch instance but fails across another
- VLAN config appears correct but is in wrong instance

### ARIA Checks
- switch instance mapping
- show VLAN switch <id>
- confirm port-to-switch mapping

---

## VLAN Troubleshooting Priority

When RF is good but traffic fails, ARIA should check in this order:

1. VLAN ID
2. tagged vs untagged behavior
3. PVID
4. port membership
5. acceptable frame type
6. ingress filtering
7. dynamic learning status
8. bridge mode
9. provider C-VLAN/S-VLAN mapping
10. MAC table learning