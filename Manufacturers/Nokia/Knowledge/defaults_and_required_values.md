# CorEvo Section 1 — Defaults and Required Values

## Default Values
- Username: admin
- Password: adminadmin
- WebCT session timeout: 10 minutes
- SNMP version: V2

---

## Required Configuration Values

### Session Timeout
- Set to: 60 minutes

### Password Handling
- Change ONLY if prompted
- Otherwise leave default

### Site Information
- NSP Name: Provided by Verizon
- Location: From PCN
- Latitude/Longitude: Optional (from PCN)

### System Settings
- Password Policy: Disabled
- TACACS+: Disabled
- NETCONF: Disabled
- Debug Shell: Disabled
- Telnet Server: Disabled
- FTP Server: Disabled

### SNMP
- Set to: V3

# ================================
# SECTION 2 — Defaults & Values
# ================================

## TMN Local Ethernet IP

IPv4:
- Format: 192.168.xxx.xxx
- XXX = last 2 octets of NE IP

IPv6:
- Format: FD00:XXX::1
- XXX = site ID

---

## OSPF Configuration

Area ID:
- 1.2.3.4

Stub:
- OFF

Restriction:
- OSPF must NOT be enabled on TMN Port #4

---

## OSPFv3 Router IDs

Hub:
- 1.1.1.1

Spoke:
- 2.2.2.2

Additional sites:
- Increment pattern

---

## Static Routing Defaults

IPv4:
- Destination: 0.0.0.0
- Subnet Mask: 0.0.0.0

IPv6:
- Destination: 0::
- Prefix: 0

Next Hop:
- VzW provided gateway

---

## Static LAG Criteria

- Enabled ONLY if dual TMN Port #4 connections exist

# ================================
# SECTION 3 — Defaults & Values
# ================================

## NSP User Profiles

### Backup User
- ID: MPRbackupUser
- Profile: Craftperson
- Type: Standard
- Password: vzwRestore1#

---

### SNMPv3 User
- ID: snmpV3WaveUser
- Profile: Administrator
- Type: USM (SNMPv3)
- Password: VZWaveUSM95!

---

## Admin Password
- Required for user creation: adminadmin

# ================================
# SECTION 4 — Defaults & Values
# ================================

## Default Behavior
- System auto-selects EAC 1G card

---

## EAC10G Port Options
- 4 x 1G RJ45
- 2 x 2.5G SFP
- 1 x 10G SFP

---

## Slot-Based Limitations

Slots 3, 5, 6:
- 4x1G + 2x2.5G available

Slot 4:
- 4x1G + 1x2.5G available

Slots 7, 8:
- Only 1x2.5G port (port 3)

---

## Port Behavior Rule
- If 10G port is selected:
  → All other ports become unavailable

  # ================================
# SECTION 5 — Defaults & Values
# ================================

## Ethernet Interface
- Auto Negotiation (VzW SAR): OFF

---

## Ethernet Services
- Default: Admit Tagged Only
- Optional: ALL VLANs

---

## RF Configuration
- All RF values must come from PCN:
  - Frequency
  - Modulation
  - Channel spacing
  - TX power

---

## ACM Configuration
- Reference modulation = lowest modulation from PCN

---

## Frequency Configuration
- Must match PCN
- TX High vs TX Low must be verified

---

## Power Settings
- TX power based on PCN
- ACM uses lowest modulation TX power

---

## RF Status Requirement
- Must be ONLINE before proceeding

---

## LAG Requirement
- PPP and OSPF must be disabled before adding RF to LAG

# ================================
# SECTION 6 — Defaults & Values
# ================================

## RLAG Configuration

- LAG ID:
  - Must be unique per shelf
  - Must match both ends of hop

- Radio Units:
  - Based on physical modules (not channels)

- WTR (Wait to Restore):
  - 0.1 = standard
  - 1 = active path areas

---

## RLAG Capacity Limits

- Max 4 protection channels
- Max 8 channels (non-protected, n+0)

---

## Master Port Selection

- X.5 or X.7
- X.7 used only for 2+0 configurations

---

## VLAN Configuration

- VLAN ID: Provided by design (VzW / PCN)
- VLAN Name: Defined per site

- Ports must be explicitly assigned

---

## VLAN Behavior

- VLANs can be assigned to:
  - Physical ports
  - RLAG groups

  # ================================
# SECTION 7 — Defaults & Values
# ================================

## QoS Classification
- IEEE802.1p

---

## QoS Scheduler

### 5Q Mode
- Q5–Q3: SP
- Q2: DWRR (Weight 2)
- Q1: DWRR (Weight 1)

### 8Q Mode
- Q8–Q3: SP
- Q2: DWRR (Weight 2)
- Q1: DWRR (Weight 1)

---

## Synchronization

- Hub: Master
- Remote: Slave

Primary Source:
- RF Port or LAG toward hub

Secondary:
- Free Run Local Oscillator

---

## PM Monitoring
- Must be ENABLED on all MPT and UBT modules

---

## Radio TX
- Must be UNMUTED (OFF)

# ================================
# SECTION 8 — Defaults & Values
# ================================

## Default IP After Reset
- 10.0.1.2

---

## Recovery Requirements

Before performing reset:
- MIB backup must be available
- NE inventory must be saved
- Alarm logs should be exported

---

## Restore Options
- MIB file restore (preferred)
- Manual provisioning (fallback)