# CorEvo Provisioning — Section 1 Data

## Purpose
Initial configuration and setup of Nokia Wavence CorEvo using WebCT (W19 ICS02).

## Workflow Sequence
1. WebCT orientation
2. Password handling
3. WebCT session timeout configuration
4. Site name and location configuration
5. Startup/system settings configuration
6. SNMP version configuration

---

## Step Details

### 1. WebCT Orientation
- Interface uses top-level menus and left-side submenus
- IPv6 URL addresses must be enclosed in brackets

---

### 2. Password Handling
- Default password: adminadmin
- If prompted on first login:
  - Change password to Verizon standard
- If NOT prompted:
  - Leave default password unchanged
- Password changes must be documented
- Password policy will be disabled later

---

### 3. WebCT Timeout Configuration
- Default session timeout: 10 minutes
- Set session timeout to: 60 minutes
- Apply changes

---

### 4. Site Name and Location
- Enter VzW-provided NSP name
- Enter location name from PCN
- Optional: add latitude and longitude from PCN
- Apply changes

---

### 5. Startup/System Settings
- Disable password policy
- Disable TACACS+
- Disable NETCONF
- Ensure the following are disabled:
  - Debug Shell
  - Telnet Server
  - FTP Server

---

### 6. SNMP Version Configuration
- Change SNMP version from V2 to V3
- Apply changes

# ================================
# SECTION 2 — IP Addressing / OSPF / Routing
# ================================

## Purpose
Configure MSS IP addressing, OSPF routing, IPv6 stack, static routing, and TMN Port #4 behavior.

## Workflow Sequence
1. Configure Local IP and TMN IP
2. Configure OSPF Area and Router ID
3. Configure IPv6 addressing and OSPFv3
4. Configure Static Routing
5. Validate and apply configuration
6. Configure Static LAG (if dual TMN Port #4 used)

---

## Step Details

### 1. Local IP and TMN Configuration
- Change NE Local IP Address
- Change TMN Local IP (Management)
- Enable TMN Local Ethernet
- Configure TMN Port #4 IP to match NE Local IP

---

### 2. OSPF Configuration
- Enable OSPF
- Create Area #1
- Set Area ID: 1.2.3.4
- Set Stub: OFF
- Move OSPF into Area #1
- Enable OSPF on TMN Local interface

⚠ Do NOT enable OSPF on TMN Port #4

---

### 3. IPv6 Configuration
- Enable IPv6 Stack
- Apply same addressing logic as IPv4
- Configure OSPFv3

OSPFv3 Router ID:
- Hub: 1.1.1.1
- Spoke: 2.2.2.2
- Increment pattern for additional sites

---

### 4. Static Routing Configuration
- Navigate to Static Routing Configuration
- Add IPv4 or IPv6 route
- Enter:
  - Destination Address
  - Subnet Mask
  - Next Hop Address (VzW provided)
- Leave as "Next Hop"
- Apply changes

---

### 5. Static Route Removal
- Verify route appears in table
- Select route
- Click Delete

---

### 6. Dual TMN Port #4 Configuration (Conditional)
IF dual Cat5 connections exist (Main + Standby CorEvo → SAR):
- Enable Static LAG Criteria
- Apply changes

# ================================
# SECTION 3 — Alarm Profiles / NSP User Profiles
# ================================

## Purpose
Configure alarm profile behavior for TMN management interface and create required user profiles for NSP discovery and backup.

## Workflow Sequence
1. Configure Alarm Profile for TMN Management Port
2. Create NSP User Profiles
3. Verify user profiles

---

## Step Details

### 1. Alarm Profile Configuration
- Navigate to Alarm Management (ASAP)
- Enable Alarm Profile for Maintenance / Management Port
- Apply changes

---

### 2. NSP User Profile Creation
- Navigate to Users Management
- Click Create User

Create the following users:

#### User 1 — Backup User
- ID: MPRbackupUser
- Profile: Craftperson
- Type: Standard
- Password: vzwRestore1#
- Admin Password: adminadmin

---

#### User 2 — SNMPv3 User
- ID: snmpV3WaveUser
- Profile: Administrator
- Type: USM (SNMPv3)
- Password: VZWaveUSM95!
- Admin Password: adminadmin

---

### 3. Verification
- Confirm both users appear in list
- Verify:
  - Correct spelling
  - Correct capitalization
  - Correct user type

  # ================================
# SECTION 4 — MSS Shelf Card Configuration
# ================================

## Purpose
Assign and configure hardware cards within the MSS shelf based on engineering design.

## Workflow Sequence
1. Review inserted cards (auto-detection)
2. Assign required cards to slots
3. Configure EAC10G card (if used)
4. Apply configuration
5. Remove cards if required

---

## Step Details

### 1. Card Recognition
- System automatically detects inserted cards
- Displays available equipment on right panel

---

### 2. Assigning Cards
- Navigate to Equipment Configuration
- Select required card from available equipment
- Drag and drop into desired slot
- Click Apply

---

### 3. Manual Provisioning (if needed)
- If cards do not auto-populate:
  - Manually drag desired card into slot
  - Apply changes

---

### 4. EAC Card Behavior
- System defaults to EAC 1G card
- To use EAC 10G:
  - Un-provision EAC 1G
  - Reassign slot as EAC 10G

---

### 5. EAC10G Configuration
- Drag EAC10G card into slot
- Select port configuration:
  - 1G / 2.5G
  - OR 10G
- Apply in popup window
- Apply at top of screen

---

### 6. Card Removal
- Hover over card
- Select "Remove Board"
- Click Apply

# ================================
# SECTION 5 — Ports / RF / Services Configuration
# ================================

## Purpose
Configure Ethernet/Fiber ports, RF interfaces, protection, power, routing protocols, and performance monitoring.

## Workflow Sequence
1. Create Ethernet/Fiber ports
2. Configure Ethernet interfaces
3. Configure Ethernet services (VLAN behavior)
4. Create RF ports
5. Configure RF protection
6. Configure PFoE (power)
7. Configure RF radio parameters
8. Enable PPP and OSPF on RF channels
9. Enable Performance Monitoring (PM)

---

## Step Details

### 1. Create Ethernet/Fiber Ports
- Navigate to Port Configuration
- Drag ETH icon to available port location (dashed slots)
- Click Apply

---

### 2. Configure Ethernet Interfaces
- Select card slot
- Select port
- Enable port
- Set Auto Negotiation:
  - VzW standard (SAR): OFF
- Apply changes

---

### 3. Configure Ethernet Services
- Default: Admit Tagged Only
- If required: set to ALL VLANs
- Apply changes

---

### 4. Remove Ports
- Ports must be disabled before removal
- Select Remove port
- Apply changes

---

### 5. Create RF Ports
- Drag RF equipment icon to available port
- Apply changes

---

### 6. Configure RF Protection
- Drag RF icon onto another RF icon
- Select protection type (popup)
- Apply changes

---

### 7. Remove RF Protection
- Navigate to Protections field
- Select protected group
- Remove port
- Apply changes

---

### 8. Configure PFoE (Power)
- Navigate to Power Management
- Select card and port providing power
- Apply changes

---

### 9. Configure Radio RF Parameters
Set:
- Radio label
- Modulation type
- Channel spacing
- Modulation(s)
- Frequency range (High/Low)
- Frequencies
- TX Power

For UBT-T:
- Channel A and B
- XPIC

IMPORTANT:
- Wait for radio status to change from OFFLINE → ONLINE before continuing

---

### 10. Configure Modem Profile (ACM)
- Select channel size
- Set reference modulation (lowest modulation from PCN)
- Select desired modulation levels
- Apply changes

---

### 11. Configure Frequency Settings
- Select frequency range per PCN
- Select TX High or TX Low
- Apply changes

---

### 12. Configure Power Settings
- Set TX power per PCN
- If ACM:
  - Use lowest modulation TX power

---

### 13. Enable PPP and OSPF on RF Channels
- Enable PPP protocol
- Enable OSPF
- Select correct OSPF area
- Apply changes

NOTE:
- PPP and OSPF must be DISABLED before placing RF channel into LAG

---

### 14. Enable Performance Monitoring (PM)
- Enable PM Monitoring per RF channel
- Apply changes

# ================================
# SECTION 6 — RLAG / VLAN Configuration
# ================================

## Purpose
Configure Radio Link Aggregation (RLAG / Carrier Aggregation) and VLAN creation/management.

## Workflow Sequence
1. Create RLAG group
2. Assign RF ports to RLAG
3. Configure RLAG settings
4. Create VLANs
5. Assign VLANs to ports / LAG
6. Edit/Delete VLANs

---

## Step Details

### 1. Create RLAG Group
- Navigate to Radio LAG Interface
- Click List → Create
- Enter:
  - LAG ID (must be unique per shelf and match both ends)
  - LAG Name
  - Number of Radio Units (MPT/UBT modules, not channels)
- Apply changes

---

### 2. Select RLAG Group
- Select newly created LAG from list

---

### 3. Assign RF Ports
- Select RF ports from Available Ports
- Move to Member Ports

IMPORTANT:
- Select master port first:
  - X.5 or X.7
  - X.7 only used for 2+0 configuration

---

### 4. Configure RLAG Settings
- Enable LAG group
- Set WTR (Wait to Restore):
  - 0.1 for normal
  - 1 for active path areas
- Apply changes

---

### 5. Create VLAN
- Navigate to VLAN Management
- Click Create
- Enter:
  - VLAN ID
  - VLAN Name
- Select ports for VLAN membership
- Apply changes

NOTE:
- RLAG groups appear at bottom of port selection list

---

### 6. Edit VLAN
- Select VLAN
- Click Edit
- Modify values
- Apply changes

---

### 7. Delete VLAN
- Select VLAN
- Click Delete
- Apply changes

# ================================
# SECTION 7 — QoS / Segregation / Sync / Time / PM
# ================================

## Purpose
Configure QoS behavior, port segregation, synchronization, system time, and enable performance monitoring and radio transmission.

## Workflow Sequence
1. Configure QoS
2. Configure Port Segregation (if required)
3. Configure Radio Synchronization
4. Set NE Time
5. Enable PM Monitoring
6. Unmute Radio TX

---

## Step Details

### 1. Configure QoS
- Navigate to QoS Configuration
- Set Classification to: IEEE802.1p
- Apply changes

Scheduler Configuration:

#### 5 Queue (5Q)
- Q5 – SP
- Q4 – SP
- Q3 – SP
- Q2 – DWRR (Weight 2)
- Q1 – DWRR (Weight 1)

#### 8 Queue (8Q)
- Q8 – SP
- Q7 – SP
- Q6 – SP
- Q5 – SP
- Q4 – SP
- Q3 – SP
- Q2 – DWRR (Weight 2)
- Q1 – DWRR (Weight 1)

Apply changes

---

### 2. Port Segregation
- Navigate to Port Segregation
- Select card
- Select ports requiring segregation
- Apply (one line at a time)

---

### 3. Radio Synchronization
- Navigate to Synchronization

Set:
- Hub site → Master
- Remote sites → Slave

Primary Source:
- Radio Port / LAG facing hub

Secondary Source:
- Free Run Local Oscillator

Apply changes

---

### 4. Set NE Time
- Navigate to System Settings → Date & Time
- Set NE Time using OS time
- Apply to NE

---

### 5. Enable PM Monitoring
- Navigate to Radio Maintenance
- Enable Performance Monitoring (PM)
- Apply

---

### 6. Unmute Radio TX
- Set Radio TX Mute to OFF
- Apply

NOTE:
- For UBT-T, unmute both channels if used

# ================================
# SECTION 8 — Factory Reset / Recovery / MIB Restore
# ================================

## Purpose
Provide procedures for resetting the CorEvo database, performing physical recovery, and restoring configuration using MIB backups.

## Workflow Sequence
1. Perform Database Scratch (software reset)
2. Perform Physical Database Scratch (hardware reset)
3. Restore configuration using MIB backup
4. Verify system restoration

---

## Step Details

### 1. Database Scratch (Web Method)
- Navigate to:
  Monitoring & Maintenance > Debug Info
- Select:
  Clear DB and Restart NE
- Confirm in popup
- System will reboot

Post-reboot:
- Log back in using default IP: 10.0.1.2

---

### 2. Physical Database Scratch (Hardware Method)

Pre-check:
- Pull MIB backup
- Pull NE inventory
- Save alarm logs (CSV)

Procedure:
1. Remove protected CSM (slot 2)
2. Remove main CSM (slot 1)
3. Locate dip switch 1 (front right of card)
4. Move dip switch 1:
   - Right → Left
5. Insert CSM into slot 1
6. Wait for full boot (no flashing green)
7. Remove CSM
8. Move dip switch back:
   - Left → Right
9. Reinsert CSM into slot 1
10. Wait for full boot
11. Log into radio

---

### 3. Re-Provision / Restore

Options:
- Restore from known good MIB file
- OR manually rebuild using NE Inventory

---

### 4. Final Steps
- Verify site configuration restored
- Reinsert protected CSM (slot 2)