# Nokia Wavence Alarm Clearing Foundation

Source manual: 3DB19291AUAATQZZA01_Vol1_Wavence_25_Alarm_Clearing_User_Manual.pdf

ARIA priority:
This document is the primary troubleshooting foundation for Nokia Wavence. When an alarm is present, ARIA must first identify:
1. Probable cause
2. Friendly name / entity
3. Facility or equipment affected
4. Whether the alarm is Service Affecting or Non-Service Affecting
5. Related alarms on the same path, port, radio, LAG, sync source, or protection group
6. The correct clearing procedure before recommending hardware replacement

Core rule:
Do not troubleshoot an alarm in isolation. Always retrieve all active alarms first, interpret the friendly name/entity, determine the affected facility/equipment, then follow the specific alarm-clearing procedure.

Alarm retrieval path:
Monitoring & Maintenance Domain > Active Alarms

Severity logic:
- SA = Service Affecting: condition affects traffic delivery or synchronization delivery.
- NSA = Non-Service Affecting: condition does not currently affect traffic or synchronization.
- Alarm severities are Major (MJ), Minor (MN), and Warning (WN).
- A radio spare alarm may be NSA when protection is active, but the same alarm on both main and spare can become SA.

Friendly name decoding:
Equipment friendly names use:
r<rack number>s<subrack number>b<board number>d<daughter>

Radio facility friendly names use:
f<facility name>rd<radio direction>b<board number>p<port number>c<channel number>

DS1, DS3, and Ethernet facility friendly names use:
f<facility name>b<board number>p<port number>

Key entity meanings:
- r = rack number
- s = subrack number
- b / board / slot = board or slot number
- d / daughter = SFP daughter port
- rd / Dir = radio direction
- p / Port = facility port
- c / Ch = radio channel
- Ch#1 = main radio channel
- Ch#0 = spare radio channel
- ERP = Ethernet Ring Protection Switch

Example interpretations:
- Replaceable Unit Missing + r01s1/board#8 = missing provisioned card in rack 01, subrack 1, board/slot 8.
- Loss Of Signal + DS1-in/slot#5/Port#22 = incoming DS1 signal loss on P32E1DS1 card in slot 5, port 22.
- Loss Of Frame + DS3-in/slot#6/Port#2 = DS3 frame loss on P2E3DS3 card in slot 6, port 2.

# CorEvo Operational Insights

# ================================
# SECTION 2 — IP / OSPF / Routing Behavior
# ================================

## TMN Port #4 Behavior
- TMN Port #4 is a management interface
- Must NOT have OSPF enabled
- Misconfiguration can break management access

---

## OSPF Configuration Sensitivity
- OSPF must be assigned to correct area (#1)
- Incorrect Area ID or placement will disrupt routing
- TMN Local interface participates in OSPF, not Port #4

---

## IPv4 / IPv6 Alignment
- IPv6 configuration mirrors IPv4 logic
- OSPFv3 must align with site role (hub vs spoke)

---

## OSPFv3 Router ID Strategy
- Hub uses 1.1.1.1
- Spokes use 2.2.2.2
- Pattern increments for scaling network

---

## Static Routing Behavior
- 0.0.0.0 / 0:: indicates default route
- Next Hop defines upstream gateway
- Incorrect gateway = total traffic loss

---

## Static LAG Behavior
- Only required when dual TMN Port #4 connections exist
- Prevents alarms on SAR
- Incorrect use may cause unnecessary reboot

---

## Reboot Sensitivity (Section 2)
- IP/OSPF changes trigger reboot
- IPv6 enable triggers reboot
- Static LAG enable triggers reboot (service impacting)

---

## Failure Risk Areas
- Enabling OSPF on wrong interface
- Incorrect TMN IP alignment
- Wrong OSPF area assignment
- Incorrect gateway in static routing
- Applying changes without awareness of reboot

# ================================
# SECTION 3 — Alarm / User Profile Behavior
# ================================

## TMN Alarm Behavior
- TMN Management Port is used for local onsite access
- Enabling Alarm Profile suppresses LOS (Loss of Signal) alarms

Operational impact:
- Prevents false alarms when no laptop is connected locally
- If not configured, persistent TMN Ethernet alarms may appear

---

## Alarm Misinterpretation Risk
- A standing TMN Ethernet alarm does NOT always indicate failure
- Often caused by no active local connection

---

## NSP User Profile Purpose

### MPRbackupUser
- Used for MIB backups in NSP
- Must exist for proper backup operations

---

### snmpV3WaveUser
- Used for SNMPv3 communication with NSP
- Required for network discovery and monitoring

---

## Discovery Dependency
- NSP discovery depends on correct SNMPv3 user configuration
- Incorrect credentials → device not discovered

---

## Upgrade Exception Behavior
- If site was already discovered before upgrade to W19 ICS02:
  → SNMP profile does NOT change

---

## Failure Risk Areas
- Missing SNMPv3 user → NSP discovery failure
- Incorrect credentials → communication failure
- Alarm profile not set → false LOS alarms on TMN port

# ================================
# SECTION 4 — Card Configuration Behavior
# ================================

## Auto-Detection Behavior
- System automatically detects inserted cards
- Does not always match intended engineering design

Risk:
- Incorrect auto-selection may go unnoticed

---

## EAC Card Selection Risk
- System defaults to EAC 1G
- If 10G is required, manual correction is needed

Failure risk:
- Wrong throughput configuration
- Mismatch with SAR or radio requirements

---

## Hardware Dependency
- Card selection must match engineering design
- Incorrect card placement = service mismatch

---

## EAC10G Port Limitation Behavior
- Selecting 10G disables all other ports

Operational impact:
- Misconfiguration can remove required interfaces

---

## Slot Dependency Behavior
- Port availability depends on slot position
- Same card behaves differently depending on slot

Risk:
- Incorrect slot placement limits usable ports

---

## LAG Dependency (from Section 2 reference)
- EASv2 card required when provisioning 2 UBT modules in LAG group

---

## Provisioning Before Hardware Installed
- System allows provisioning before cards are physically inserted

Risk:
- Logical config may not match physical hardware

---

## Failure Risk Areas
- Wrong card type selected (1G vs 10G)
- Incorrect slot placement
- Port availability mismatch
- Forgetting to override default EAC 1G

# ================================
# SECTION 5 — RF / Port / Service Behavior
# ================================

## Port Creation Behavior
- Ports must be manually assigned via drag-and-drop
- Available ports indicated by dashed outlines

Risk:
- Incorrect port placement = connectivity failure

---

## Auto Negotiation Dependency
- Must match router configuration (SAR)
- VzW standard = OFF

Risk:
- Mismatch causes link failure

---

## VLAN Admission Behavior
- Default = Tagged Only
- Changing to ALL allows untagged traffic

Risk:
- Incorrect setting can allow unintended traffic

---

## RF Activation Dependency
- RF must show ONLINE before proceeding

Risk:
- Configuring offline radio leads to invalid settings

---

## PCN Dependency (CRITICAL)
ALL RF values come from PCN:
- Frequency
- Modulation
- Channel spacing
- TX power

Failure:
- Guessing values = link failure

---

## ACM Behavior
- Reference modulation must be lowest modulation

Risk:
- Incorrect setting affects link stability

---

## Frequency Configuration Risk
- Selecting TX High vs TX Low incorrectly can break link alignment

---

## PPP / OSPF Dependency
- Required for RF channel routing
- Must be disabled before LAG configuration

Risk:
- LAG failure if not disabled first

---

## Protection Configuration Behavior
- RF protection links two radios
- Incorrect pairing causes protection failure

---

## PFoE Dependency
- Required to power UBT units

Risk:
- No power = radio offline

---

## Performance Monitoring Behavior
- Enabling PM activates all monitoring fields

Benefit:
- Enables diagnostics and performance tracking

---

## Failure Risk Areas
- Wrong RF frequency/modulation (PCN mismatch)
- Auto negotiation mismatch
- RF not ONLINE before config
- PPP/OSPF misconfiguration
- Incorrect VLAN admission
- Missing PFoE power

# ================================
# SECTION 6 — RLAG / VLAN Behavior
# ================================

## RLAG Dependency (CRITICAL)
- LAG ID must match on both ends of the link

Failure:
- Mismatch = aggregation failure

---

## Master Port Behavior
- Master port must be selected first
- X.5 or X.7 used as master

Risk:
- Incorrect master selection breaks LAG formation

---

## RF Port Availability Conditions
If RF port is greyed out:
- PPP must be disabled
- No VLAN assigned
- No Port Segregation applied
- Synchronization must be set to master

This is a multi-condition dependency check

---

## LAG Membership Dependency
- RF ports must be clean before adding to LAG

Risk:
- Existing config blocks LAG creation

---

## WTR Behavior
- Lower WTR = faster recovery
- Higher WTR = stability in active paths

Incorrect setting:
- Can cause flapping or delayed recovery

---

## Channel vs Radio Unit Confusion
- Radio Units = physical modules
- Size = channels

In UBT-T:
- Size may be greater than radio units

Risk:
- Misinterpreting capacity or configuration

---

## VLAN Dependency (CRITICAL)
- VLANs must match network design (PCN)

Failure:
- Incorrect VLAN = traffic loss

---

## VLAN Assignment Behavior
- VLAN must be explicitly assigned to:
  - Ports
  - RLAG groups

Risk:
- Missing assignment = no traffic flow

---

## VLAN Deletion Risk
- Deleting VLAN removes:
  - All port memberships
  - Untagged assignments

Impact:
- Immediate traffic disruption

---

## LAG + VLAN Interaction
- RLAG groups appear as VLAN assignment targets

Dependency:
- VLAN must align with LAG configuration

---

## Failure Risk Areas
- LAG ID mismatch
- Master port incorrect
- RF ports not eligible (PPP/VLAN conflict)
- VLAN not assigned
- VLAN deleted incorrectly
- WTR misconfigured

# ================================
# SECTION 7 — QoS / Sync / PM Behavior
# ================================

## QoS Classification Behavior
- IEEE802.1p prioritizes traffic using VLAN tagging

Risk:
- Incorrect classification leads to improper traffic prioritization

---

## Queue Scheduling Behavior
- SP (Strict Priority) always serviced first
- DWRR handles remaining traffic proportionally

Risk:
- Misconfigured queues can starve lower priority traffic

---

## Port Segregation Use Case
- Only required when parallel physical connections exist between MSS and external equipment

Important:
- Not needed if RF links are already in LAG/CA group

Risk:
- Unnecessary segregation can block traffic paths

---

## Synchronization Dependency (CRITICAL)
- Network timing depends on correct Master/Slave configuration

Failure:
- Incorrect sync causes timing issues across network

---

## Sync Source Behavior
- Primary source must face hub
- Secondary is fallback (free run)

Risk:
- Incorrect source leads to unstable timing

---

## NE Time Behavior
- System time is set from connected laptop

Risk:
- Incorrect laptop time propagates to network element

---

## PM Monitoring Requirement
- Must be enabled on ALL radios

Benefit:
- Enables troubleshooting and performance visibility

Failure:
- Disabled PM = no diagnostics capability

---

## Radio TX Behavior
- TX must be unmuted for link to operate

Dependency:
- Both ends must be unmuted to view RSL

---

## RSL Visibility
- Only visible after TX unmuted on BOTH ends

---

## Failure Risk Areas
- QoS misconfiguration (traffic issues)
- Sync misalignment (network instability)
- PM disabled (no troubleshooting visibility)
- TX muted (link appears down)

# ================================
# SECTION 8 — Reset / Recovery Behavior
# ================================

## Database Scratch Behavior
- Completely wipes configuration
- Node returns to default state

Impact:
- Total loss of provisioning

---

## Default Access Behavior
- After reset, node returns to default IP (10.0.1.2)

Risk:
- Technician may lose access if not on correct subnet

---

## Pre-Reset Dependency (CRITICAL)
- MIB backup MUST be taken before reset
- NE inventory must be saved

Failure:
- No backup = full manual rebuild required

---

## Physical Reset Behavior
- Uses dip switch to force database wipe

From page 8:
- Dip switch 1 must be toggled during procedure :contentReference[oaicite:0]{index=0}

Risk:
- Incorrect handling can delay recovery

---

## Dual Controller Behavior
- Protected CSM (slot 2) must be removed during reset
- Reinserted after recovery

---

## Recovery Strategy

Preferred:
- Restore using known good MIB file

Fallback:
- Manual provisioning using NE inventory

---

## MIB Restore Behavior
- Restore loads previous configuration snapshot
- Requires activation

Risk:
- Using incorrect MIB file restores wrong config

---

## Data Loss Risk (CRITICAL)
- Alarm logs
- Configuration
- Inventory data

Must be saved BEFORE reset

---

## Operational Use Cases
- Corrupted configuration
- Failed provisioning
- Recovery from unknown state

---

## Failure Risk Areas
- Performing reset without backup
- Not knowing default IP after reset
- Using wrong MIB file
- Skipping inventory backup