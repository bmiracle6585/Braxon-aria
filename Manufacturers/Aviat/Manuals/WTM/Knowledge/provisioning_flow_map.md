## WTM 4000 — System Configuration Flow

## CORE CONFIGURATION SEQUENCE (REQUIRED ORDER)

1. Management IP
2. Routing (Static Routes if needed)
3. DNS / DHCP Relay (if network-managed)
4. Time Configuration (NTP/SNTP)
5. SNMP / Monitoring
6. Network Sync (SyncE / PTP)
7. Logging / Diagnostics
8. Access (Wi-Fi / Terminal)

---

## STEP 1 — MANAGEMENT IP

Two modes:

### WITH MANAGEMENT VLAN
- Requires VLAN pre-created
- Creates L3 VLAN interface

### WITHOUT MANAGEMENT VLAN
- Pure Layer 3 interface
- No VLAN membership :contentReference[oaicite:0]{index=0}

---

## ARIA RULE

If:
- device unreachable

→ FIRST CHECK:
- management IP mode
- VLAN mismatch

---

## STEP 2 — ROUTING

Static routing required for:

- off-subnet management
- NMS connectivity

Key inputs:
- destination/prefix
- next hop
- interface
- metric :contentReference[oaicite:1]{index=1}

---

## STEP 3 — DNS / DHCP RELAY

DNS:
- resolves hostnames → IP

DHCP Relay:
- forwards DHCP requests to server
- requires:
  - interface with L3 forwarding
  - IP assigned :contentReference[oaicite:2]{index=2}

---

## STEP 4 — TIME CONFIGURATION

Options:
- manual (local clock)
- NTP / SNTP (preferred)

CRITICAL:
- device runs in UTC internally :contentReference[oaicite:3]{index=3}

---

## ARIA RULE

If:
- logs incorrect
- alarms misaligned

→ check time sync BEFORE troubleshooting

---

## STEP 5 — SNMP / MONITORING

Modes:
- disabled
- enabled
- v2c-only
- v3-only (not supported in this version)

Trap configuration required for:
- alarms
- monitoring systems :contentReference[oaicite:4]{index=4}

---

## STEP 6 — NETWORK SYNC (CRITICAL)

Two systems:

### SyncE (frequency)
### PTP (time)

---

## DEPENDENCY RULE

PTP REQUIRES:
→ SyncE configured first :contentReference[oaicite:5]{index=5}

---

## STEP 7 — LOGGING

Remote logging supports:
- UDP
- TCP
- TLS

Used for:
- centralized troubleshooting :contentReference[oaicite:6]{index=6}

---

## STEP 8 — ACCESS METHODS

- GUI (primary)
- CLI via terminal
- Wi-Fi (USB dongle required)

---

## FINAL RULE

Configuration is NOT complete until:

- management reachable
- time synced
- logging active
- sync configured (if required)

## WTM 4000 — Radio Configuration Flow

## CORE RADIO BUILD SEQUENCE

1. Create Radio Interface
2. Assign Carriers
3. Configure Carrier Parameters
4. Set Frequency Plan
5. Configure Modulation
6. Configure Power (ATPC / Fixed)
7. Apply Link Mode (XPIC / SD / MIMO)
8. Commit Configuration

---

## STEP 1 — RADIO INTERFACE

Radio = logical interface  
Carrier = physical RF interface :contentReference[oaicite:0]{index=0}

RULE:
Radio must have ≥1 carrier to function

---

## STEP 2 — CARRIER ASSIGNMENT

Options:
- Carrier1/1 (primary)
- Carrier1/2 (secondary)

RULE:
- Single link → Carrier1/1 only
- Dual/XPIC → both carriers required :contentReference[oaicite:1]{index=1}

---

## STEP 3 — CAPACITY CONFIG

- Bandwidth
- Modulation mode (Fixed / Adaptive)
- Modulation range

---

## STEP 4 — FREQUENCY PLAN

- Tx frequency
- Rx frequency
- Spacing

CRITICAL RULE:
Frequencies must match remote side

---

## STEP 5 — MODULATION

Two modes:

Fixed:
→ stable but lower efficiency

Adaptive (ACM):
→ dynamic optimization

---

## STEP 6 — POWER CONFIG

Two modes:

ATPC:
→ automatic power control (preferred)

Fixed:
→ static output power

---

## STEP 7 — RADIO MODES

Available:

- XPIC (dual polarization)
- Space Diversity
- MIMO

---

## DEPENDENCY RULE

Multi-unit setups REQUIRE:
→ Partner device configuration

---

## FINAL STEP

Click COMMIT

WITHOUT COMMIT:
→ configuration not applied :contentReference[oaicite:2]{index=2}

## WTM 4000 — Traffic / Switching Provisioning Flow

## CORE TRAFFIC BUILD SEQUENCE

1. Configure Interfaces
2. Define VLANs
3. Assign VLAN Membership
4. Configure Link Aggregation (if used)
5. Configure Routing (if required)
6. Apply QoS Policies
7. Commit

---

## STEP 1 — INTERFACES

Interfaces available:

- GigabitEthernet (ge1, ge2)
- TenGigE (xe1, xe2)
- Radio1 (ra1) :contentReference[oaicite:0]{index=0}

RULE:
Interface must be active and correctly configured for speed/media

---

## STEP 2 — VLAN DEFINITION

Each VLAN must be:

→ explicitly created BEFORE use

RULE:
If VLAN not defined → traffic DROPPED

---

## STEP 3 — VLAN MEMBERSHIP

Two modes:

- Access → single VLAN
- Trunk → multiple VLANs

RULE:
Mismatch between ends = traffic failure

---

## STEP 4 — LINK AGGREGATION (OPTIONAL)

Types:

- L1LA (radio aggregation)
- L2 aggregation (Ethernet)

RULE:
All traffic must pass through aggregation when enabled

---

## STEP 5 — ROUTING

Options:

- Static routes
- OSPF

---

## STEP 6 — QoS

Required for:

- prioritization
- traffic shaping
- L1LA stability

---

## FINAL STEP

Commit required or config not active

## WTM 4000 — Administration Workflow

## SAFE CHANGE PROCESS

1. Make configuration change
2. Review diff (Config History / CLI view)
3. Commit changes
4. Validate system behavior
5. Save configuration backup

---

## ROLLBACK PROCESS

1. Identify desired commit
2. Load rollback (Undo)
3. Commit
4. Validate

WARNING:
Rollback affects ALL changes after selected point

---

## SOFTWARE UPGRADE FLOW

1. Upload software package
2. Load to inactive partition
3. Activate (immediate or manual)
4. Device reboots

---

## LICENSE INSTALL FLOW

1. Verify system time
2. Upload license
3. Validate feature activation

## WTM 4000 — Troubleshooting Flow (Status-Based)

## STEP 1 — CHECK DASHBOARD

- link status
- throughput
- modulation

---

## STEP 2 — CHECK ALARMS

- identify active alarms
- determine severity
- expand hierarchy

---

## STEP 3 — CHECK SENSORS

- RSL
- SNR
- BER

---

## STEP 4 — CHECK SYSTEM LOG

- recent commits
- errors
- events

---

## STEP 5 — CORRELATE DATA

- RF vs Traffic vs Config

---

## RULE

Never troubleshoot from ONE screen only

## WTM 4000 — USB Autoconfiguration Flow

## AUTOMATED PROCESS (ON USB INSERT)

1. Detect USB device
2. Check for valid license file
3. Load license (if present)
4. Check for configuration file
5. Load configuration (if valid)
6. Create configuration backup

---

## PROCESS ORDER (CRITICAL)

1. License FIRST
2. Config SECOND
3. Backup LAST :contentReference[oaicite:0]{index=0}

---

## CONFIG LOAD RULE

Configuration is NOT active until:

→ COMMIT is executed

---

## BACKUP BEHAVIOR

Backup occurs:

- on USB insert
- on EVERY commit

---

## NAMING RULES (CRITICAL)

License:
→ <unit_serial>.lic

Auto Config:
→ AUTOConfig<unit_serial>.config

Backup:
→ Config<unit_serial-software_version>.config :contentReference[oaicite:1]{index=1}

---

## REQUIREMENTS

- USB must be FAT32
- Autoconfig enabled (default ON)

---

## FINAL RULE

USB autoconfig is:

→ stateless trigger-based automation

## WTM 4000 — Management ACL Configuration Flow

## SAFE ACL DEPLOYMENT

1. Create ACL
2. Add ACE rules (allow first)
3. Verify rule order
4. Ensure current subnet is allowed
5. Commit
6. Validate access immediately

---

## RULE DESIGN

- allow specific subnets first
- block unwanted access after

---

## CRITICAL RULE

Never:

→ apply ACL without confirming access path

## WTM 4000 — Hardware Protection Flow

## NORMAL OPERATION

- Primary = Active
- Secondary = Standby

Traffic path:

Aggregator → WTM → Radio → WTM → Aggregator

---

## FAILURE EVENT

Trigger examples:

- hardware failure
- RFM failure
- cable failure

---

## SWITCH PROCESS

1. Failure detected
2. Active → Standby
3. Standby → Active
4. L2 path re-established

---

## POST SWITCH

- traffic resumes
- switch count increments

---

## GUARD TIMER (CRITICAL)

After switch:

→ switching is BLOCKED temporarily

Prevents:

→ oscillation

---

## GUARD TIMER BEHAVIOR

- starts at 5 sec
- doubles after each switch
- max 320 sec
- reduces over time if stable :contentReference[oaicite:4]{index=4}

## WTM 4000 — Security Enablement Flow

## FIPS ENABLEMENT

1. Verify license
2. Remove unsupported TLS ciphers
3. Enable FIPS mode
4. Reboot system
5. Validate operational state

---

## STRONG SECURITY ENABLEMENT

1. Verify license
2. Access CLI
3. Enable strong security mode
4. Validate authentication behavior

---

## HTTP HARDENING

1. Navigate to Admin > HTTP
2. Enable HTTP redirect
3. Verify HTTPS access
4. Confirm port 80 blocked

## WTM 4000 — Alarm-Based Troubleshooting Flow

## STEP 1 — IDENTIFY HIGHEST SEVERITY

- Critical first
- Then Major
- Then Warning

---

## STEP 2 — GROUP ALARMS

Group by type:

- RF
- Network
- Hardware
- Security

---

## STEP 3 — FIND COMMON THREAD

Look for:

- same subsystem
- same time occurrence

---

## STEP 4 — DETERMINE ROOT CAUSE

Example:

- demodulator_not_locked
- snr_degraded
- ber exceeded

→ ROOT = RF degradation

---

## STEP 5 — VALIDATE WITH STATUS

- check dashboard
- check sensors
- confirm hypothesis

---

## RULE

Never troubleshoot individual alarm in isolation