# WTM 4000 — Operational Insights

## SYSTEM TYPE

WTM 4000 is a:
- All-outdoor microwave radio (AODR)
- Fully self-contained unit (no indoor unit)
- Designed for mission-critical backhaul

Key implication:
→ No separate indoor node (unlike Eclipse)

---

## ARCHITECTURE DIFFERENCE (CRITICAL)

WTM includes:
- Integrated switching
- Integrated routing
- Integrated RF

Unlike Eclipse:
→ No modular plug-in architecture

ARIA MUST:
- Treat WTM as a **single-unit system**
- Not expect slot/module configuration

---

## CAPACITY CHARACTERISTICS

- Up to 2.5 Gbps throughput per link :contentReference[oaicite:0]{index=0}
- Supports:
  - Single channel
  - Dual channel (aggregation)
- Uses:
  - Adaptive Dual Carrier
  - Header compression

Key insight:
→ Capacity is dynamically influenced by traffic type and frame size

---

## MODULATION BEHAVIOR

Supports:
- QPSK → 4096 QAM :contentReference[oaicite:1]{index=1}
- Fixed and Adaptive modulation

Key difference from Eclipse:
→ Higher modulation ceiling (4096 QAM)

---

## RF CONFIGURATION FLEXIBILITY

- Channel sizes:
  - 10 → 80 MHz :contentReference[oaicite:2]{index=2}
- Frequency bands:
  - 4–26 GHz

---

## SYSTEM CONFIGURATION MODES

WTM supports:

- 1+0 (no protection)
- 1+1 protection
- 2+0 (aggregation or XPIC)
- 4+0 LAG (multi-radio scaling)

Key insight:
→ WTM heavily uses **aggregation instead of traditional circuit mapping**

---

## NETWORKING ARCHITECTURE

WTM is NOT just a radio.

It includes:

- Full L2 switching:
  - VLAN (802.1Q, Q-in-Q)
  - STP / RSTP / MSTP
  - LAG (802.1AX)

- Full L3 routing:
  - Static routing
  - OSPF / IS-IS
  - BGP

- MPLS support:
  - LDP / T-LDP
  - VPLS / VPWS

Key insight:
→ WTM behaves like a **router + switch + radio combined**

---

## MANAGEMENT MODEL

Supports:

- SNMP (v2c / v3)
- NETCONF / YANG
- SSH access
- ProVision NMS

Management types:
- In-band VLAN
- IP-based access

---

## SECURITY MODEL

Includes:

- AAA (TACACS+, RADIUS)
- Payload encryption (AES256)
- FIPS 140-3 compliance :contentReference[oaicite:3]{index=3}

Key insight:
→ Security is not optional — often required (government deployments)

---

## SYNCHRONIZATION

Supports:

- SyncE
- IEEE 1588v2 (PTP)
- ITU-T timing standards

---

## CRITICAL DESIGN DIFFERENCE (FOR ARIA)

WTM is:

→ Packet-first (Ethernet/IP/MPLS)

Eclipse is:

→ Circuit + RF structured

---

## OPERATIONAL IMPLICATION

ARIA must:

- Expect VLAN / routing issues BEFORE RF issues
- Treat traffic problems as:
  → networking first
  → RF second

This is opposite of traditional microwave troubleshooting

## WTM 4800 — Multi-Band / E-Band Behavior

## CORE DIFFERENCE

WTM 4800 introduces:

- E-Band (80 GHz) high-capacity links
- Multi-Band aggregation (E-Band + microwave)

Key implication:
→ Link is no longer a single RF path

---

## MULTI-BAND ARCHITECTURE

WTM 4800 can combine:

- 80 GHz E-Band channel
- 11–23 GHz microwave channels :contentReference[oaicite:1]{index=1}

All within a single unit.

---

## CAPACITY CHARACTERISTICS

- Up to 10 Gbps (single/dual channel)
- Up to 20 Gbps (multi-band aggregation) :contentReference[oaicite:2]{index=2}

Key insight:
→ Traffic is distributed across multiple RF paths

---

## RF BEHAVIOR DIFFERENCE

E-Band:
- Very high capacity
- Shorter range
- Highly sensitive to rain fade

Microwave band:
- Lower capacity
- Longer range
- More stable

---

## CRITICAL OPERATIONAL BEHAVIOR

WTM 4800 dynamically shifts traffic:

- E-Band = primary high-capacity path
- Microwave = fallback / stability layer

---

## TROUBLESHOOTING IMPLICATION (VERY IMPORTANT)

If customer reports:

- intermittent throughput drops
- capacity fluctuations

ARIA MUST consider:

→ E-Band degradation (rain fade, alignment)

NOT just:
- VLAN issues
- routing issues

---

## FAILURE PATTERN (NEW)

Typical WTM 4800 issue:

- RF link is UP
- traffic is passing
- BUT capacity is reduced

Cause:
→ E-Band degraded, microwave carrying load

---

## ARIA BEHAVIOR CHANGE

For WTM 4800:

ARIA must check:

1. Is this multi-band?
2. Are both RF paths healthy?
3. Is traffic shifting between carriers?

---

## DESIGN INSIGHT

WTM 4800 reduces:

- spectrum cost (uses E-Band) :contentReference[oaicite:3]{index=3}
- hardware footprint (single unit)

But introduces:

→ dependency on RF conditions for capacity stability

---

## KEY TAKEAWAY

WTM 4000:
→ single RF logic + networking

WTM 4800:
→ multi-path RF + dynamic traffic distribution

## WTM 4000 — System Configuration Behavior

## MANAGEMENT DESIGN

Device supports:

- VLAN-based management
- non-VLAN L3 management

---

## CRITICAL RISK

Mismatch between:

- VLAN config
- management IP mode

→ causes TOTAL LOSS OF ACCESS

---

## TIME SYSTEM BEHAVIOR

- system runs in UTC internally
- GUI may display local time

---

## CRITICAL FAILURE PATTERN

Incorrect time causes:

- alarm misalignment
- log confusion
- sync issues

---

## NETWORK SYNC BEHAVIOR

SyncE:
- distributes frequency

PTP:
- distributes time

---

## CRITICAL DEPENDENCY

PTP depends on:

→ SyncE stability

---

## SYNC FAILURE PATTERN

If SyncE unstable:
→ PTP WILL FAIL

---

## SNMP LOAD WARNING

Excessive polling:
→ can overload device
→ device may stop responding :contentReference[oaicite:8]{index=8}

---

## WIFI ACCESS MODEL

Wi-Fi only works if:

- maintenance port configured as DHCP server
- USB dongle installed :contentReference[oaicite:9]{index=9}

---

## TWAMP BEHAVIOR

WTM acts as:

→ responder ONLY

NOT controller

---

## ARIA RULE

If testing latency:

→ ensure remote device is controller
→ WTM will NOT initiate test

## WTM 4000 — Radio System Behavior

## RADIO ARCHITECTURE

Radio:
→ logical interface

Carrier:
→ physical RF interface

Radio = controller  
Carrier = signal path :contentReference[oaicite:3]{index=3}

---

## CRITICAL RULE

Radio WILL NOT FUNCTION unless:

→ at least one carrier is configured

---

## DUAL CARRIER BEHAVIOR

Carrier relationships:

- bandwidth must match
- modulation often must match
- power may need to match depending on spacing :contentReference[oaicite:4]{index=4}

---

## XPIC BEHAVIOR

- uses vertical + horizontal polarization
- doubles capacity

CRITICAL:
both carriers must match:
- frequency
- power
- modulation

---

## MIMO BEHAVIOR

- increases throughput using multiple paths
- requires TWO DEVICES working together

CRITICAL DEPENDENCY:
→ SyncE REQUIRED for stability :contentReference[oaicite:5]{index=5}

---

## FAILURE RULE — MIMO

If one unit fails:

→ link drops to degraded mode  
→ capacity reduced  
→ NOT hitless

---

## ADAPTIVE MIMO BEHAVIOR

System can:

→ fall back to XPIC under bad conditions  
→ recover when stable

WARNING:
Switching causes downtime (~10s) :contentReference[oaicite:6]{index=6}

---

## SPACE DIVERSITY BEHAVIOR

- improves reliability
- uses multiple receive paths

---

## RF PERFORMANCE DRIVERS

Primary metrics:

- RSL (signal strength)
- SNR (quality)
- TX power
- Modulation level

---

## FAILURE PATTERN — RF

Low SNR leads to:

→ modulation downshift  
→ capacity drop  
→ possible link failure

---

## SPECTRUM ANALYZER LOGIC

Used to:

→ detect interference  
→ choose frequency & power

ONLY works on:
→ enabled carriers :contentReference[oaicite:7]{index=7}

---

## ANTENNA ALIGNMENT LOGIC

Uses:

- RSL
- SNR

RULE:
Alignment = maximize BOTH

---

## PERFORMANCE DATA SYSTEM

WTM tracks:

- real-time stats
- 15-min stats
- daily stats

---

## PCR (CRITICAL TOOL)

Records:

- RF signals
- alarms
- changes over time

Used for:

→ diagnosing intermittent issues :contentReference[oaicite:8]{index=8}

---

## ARIA RULE

If issue is intermittent:

→ ALWAYS check PCR data

## WTM 4000 — Switching & Traffic Behavior

## INTERFACE REALITY

Physical interfaces:
- GE = copper
- 10GE = SFP+
- Radio = RF link :contentReference[oaicite:1]{index=1}

---

## LOOPBACK BEHAVIOR

Loopback sends traffic back across link

WARNING:
→ can break GUI access if traffic too high

---

## VLAN RULE (CRITICAL)

If VLAN not defined:

→ traffic is DROPPED

---

## ACCESS VS TRUNK

Access:
→ untagged traffic → single VLAN

Trunk:
→ tagged traffic → multiple VLANs

RULE:
Mismatch = silent failure

---

## L1 LINK AGGREGATION (L1LA)

Purpose:
→ combine multiple RF links into one

Key behavior:
- automatic load balancing
- hitless scaling
- dynamic capacity adjustment :contentReference[oaicite:2]{index=2}

---

## L1LA FAILURE PATTERN

- member failure → capacity drop
- packet loss during failure
- recovery < 2ms

---

## L1LA CRITICAL RULES

- all traffic MUST go through L1LA once enabled
- cannot mix direct radio traffic with L1LA

---

## VLAN + L1LA DEPENDENCY

- VLANs MUST be correctly mapped
- incorrect VLAN = no traffic

---

## MTU RULE (HUGE)

L1LA requires:

→ MTU ≥ 2500

DEFAULT = 1514 → WILL BREAK TRAFFIC :contentReference[oaicite:3]{index=3}

---

## LINK STATUS PROPAGATION (LSP)

Purpose:
→ forces Ethernet ports DOWN when RF fails

Used for:
→ faster detection by external equipment

---

## Q-IN-Q BEHAVIOR

Double VLAN tagging:

- inner tag = customer
- outer tag = provider

RULE:
outer tag used for switching decisions :contentReference[oaicite:4]{index=4}

---

## ROUTING BEHAVIOR

Static routing:
→ manual path definition

OSPF:
→ dynamic routing

WTM supports:
→ acting as ABR (advanced use)

---

## SPANNING TREE

Prevents loops

Default:
→ RSTP

---

## QoS BEHAVIOR

Controls:

- prioritization
- traffic shaping
- packet handling

Key components:
- classifiers
- policies
- scheduling
- policing

---

## STORM CONTROL

Limits:

- broadcast
- multicast
- unknown traffic

---

## RMON (TRAFFIC ANALYSIS)

Tracks:

- interface stats
- 15-min stats
- daily stats

IMPORTANT:
Radio throughput shows LOWER than carrier sum due to overhead :contentReference[oaicite:5]{index=5}

## WTM 4000 — Administration System Behavior

## CONFIGURATION MODEL (CRITICAL)

WTM uses:

→ transaction-based configuration

Changes are NOT applied until:

→ COMMIT is executed

---

## CONFIG HISTORY BEHAVIOR

System stores:

- all configuration commits
- user who made change
- timestamp
- CLI diff view

---

## ROLLBACK RULE (CRITICAL)

Reverting to a previous commit:

→ reverts ALL changes AFTER that point

NOT just a single change :contentReference[oaicite:0]{index=0}

---

## CONFIG FILE MANAGEMENT

Supports:

- save (.config / .xml)
- load external configs
- diff between configs

---

## CRITICAL RISK

Loading config from different software version:

→ may FAIL
→ may break system :contentReference[oaicite:1]{index=1}

---

## HELP DESK REPORT FUNCTION

Generates:

- full system snapshot
- logs
- configuration

Used for:

→ vendor troubleshooting :contentReference[oaicite:2]{index=2}

---

## LICENSING BEHAVIOR

Features are:

→ license-controlled

NO LICENSE:
→ feature unavailable

---

## TRIAL LICENSE RISK

- expires after 60 days uptime
- expiry disables feature
- can cause:

→ traffic loss
→ reboot
→ service outage :contentReference[oaicite:3]{index=3}

---

## SOFTWARE MANAGEMENT

Device has:

- ACTIVE partition
- INACTIVE partition

Switching versions:

→ triggers reboot
→ impacts traffic

---

## CRITICAL RULE

Software upgrade:

→ ALWAYS causes service interruption :contentReference[oaicite:4]{index=4}

---

## SYSTEM RESTART BEHAVIOR

Restart:

→ immediate
→ NO commit required
→ traffic interrupted

---

## FACTORY RESET

Removes:

→ ALL configuration

---

## USER ROLE MODEL

Role-based access:

- OPER → read + basic tools
- CONNECTIVITY → IP + VLAN + routing
- RADIO → RF config
- CE → switching / QoS
- SYNC → timing (SyncE/PTP)
- SECURITY → users + logs + SNMP
- ADMIN → full control :contentReference[oaicite:5]{index=5}

---

## CRITICAL INSIGHT

User roles map DIRECTLY to system domains:

- RF
- Network
- Security
- Sync

---

## SESSION LIMITS

Max:

- 8 CLI sessions
- 8 GUI sessions
- 8 NETCONF sessions

Timeout:

→ 10 minutes idle :contentReference[oaicite:6]{index=6}

---

## SESSION CONTROL

Security users can:

→ terminate sessions

---

## LOGIN CONTROL

System can:

- lock users after failed attempts
- block IPs
- enforce password rules

---

## ARIA RULE

If user cannot access device:

→ check:
- session limits
- lockout status
- authentication method

## WTM 4000 — Status & Visibility Behavior

## SYSTEM VISIBILITY MODEL

WTM provides visibility through:

- Equipment view
- Dashboard
- Alarms
- Sensors
- System Logs
- Manufacturing data :contentReference[oaicite:0]{index=0}

---

## EQUIPMENT VIEW

Displays:

→ physical hardware layout

Used for:

- identifying ports
- verifying hardware presence

---

## DASHBOARD BEHAVIOR

Dashboard shows:

- interface status (up/down)
- traffic rates (Tx/Rx)
- carrier state
- modulation
- bandwidth / capacity :contentReference[oaicite:1]{index=1}

---

## CRITICAL INSIGHT

Dashboard = REAL-TIME STATE

NOT historical

---

## RADIO TILE DATA (IMPORTANT)

Each carrier shows:

- Up/Down status
- Modulation (QAM level)
- RSL
- Throughput
- Bandwidth

---

## ALARM SYSTEM

Each alarm has severity:

- Critical
- Major
- Minor
- Warning
- Inactive :contentReference[oaicite:2]{index=2}

---

## ALARM BEHAVIOR

- alarms grouped hierarchically
- clickable for expansion
- always accessible from top bar

---

## CRITICAL INSIGHT

Alarm panel = FASTEST way to detect issues

---

## SENSOR VALUES

Tracks:

- BER (bit error rate)
- RSL (signal strength)
- SNR
- fade margin
- cross polarization discrimination :contentReference[oaicite:3]{index=3}

---

## SENSOR PURPOSE

Used for:

→ RF health monitoring

---

## SYSTEM LOG BEHAVIOR

Logs:

- configuration changes
- system events
- errors
- alarms

---

## LOG FILTERING

Can filter by:

- type (severity)
- date range
- location
- message content :contentReference[oaicite:4]{index=4}

---

## CRITICAL INSIGHT

System log = ROOT CAUSE TOOL

---

## MANUFACTURING DATA

Contains:

- serial numbers
- hardware revisions
- module details :contentReference[oaicite:5]{index=5}

---

## USE CASE

Used for:

→ asset tracking
→ hardware verification

## WTM 4000 — Cross-Layer Correlation Logic

## CORE TROUBLESHOOTING MODEL

ARIA must correlate:

- Dashboard (real-time state)
- Alarms (fault indicators)
- Sensors (RF health)
- Logs (history)

---

## DECISION LOGIC

IF:
- RF metrics bad → RF issue

IF:
- RF good + no traffic → VLAN / routing issue

IF:
- alarms present → follow alarm hierarchy

IF:
- recent commit → config-induced failure

## WTM 4000 — USB Autoconfiguration Behavior

## ZERO-TO-DEPLOY MODEL

New unit:

- no license
- no config

USB provides:

→ full provisioning in one step :contentReference[oaicite:2]{index=2}

---

## TRIGGER BEHAVIOR

USB insertion triggers:

- license load
- config load
- backup creation

NO user interaction required

---

## CRITICAL INSIGHT

USB = AUTOMATIC EXECUTION

---

## NAMING DEPENDENCY

Files MUST match:

→ unit serial number

Otherwise:

→ ignored

---

## LICENSE BEHAVIOR

- license tied to serial number
- cannot reuse across devices :contentReference[oaicite:3]{index=3}

---

## TIME DEPENDENCY (CRITICAL)

If system time incorrect:

→ license may NOT activate :contentReference[oaicite:4]{index=4}

---

## CONFIG LOAD BEHAVIOR

Two types:

- .config (native)
- .xml (ProVision generated)

---

## CONFIG BLOCKING RULE

If backup file exists:

→ auto config may be skipped

---

## BACKUP BEHAVIOR

Every commit:

→ overwrites backup

---

## CRITICAL RISK

Inserting USB with wrong config:

→ device auto-loads it

→ possible full misconfiguration

---

## ARIA RULE

If unexpected config change:

→ check USB insertion history
→ check system log

---

## LOGGING

All USB actions logged in:

→ System Log

Filter:

→ program = root :contentReference[oaicite:5]{index=5}

## WTM 4000 — Management ACL Behavior

## DEFAULT STATE (CRITICAL)

By default:
→ ALL management services are accessible from ANY IP

---

## MANAGEMENT SERVICES & PORTS

- CLI → TCP 22
- NETCONF → TCP 830
- WebUI → TCP 80 / 443
- SNMP → UDP 161 :contentReference[oaicite:0]{index=0}

---

## ACL MODEL

- One or more ACLs
- Each ACL contains ACEs (rules)
- Rules are evaluated TOP → DOWN

FIRST MATCH:
→ action is applied

---

## ACTION TYPES

- Accept → allow
- Drop → silently block (preferred)
- Reject → block + send response :contentReference[oaicite:1]{index=1}

---

## CRITICAL RULE (ORDERING)

Rule order = behavior

Bad ordering:
→ unexpected access behavior

---

## IPv4 / IPv6 BEHAVIOR

ACL type can be:
- IPv4 only
- IPv6 only
- both

---

## CRITICAL INSIGHT

ACL applies to:

→ MANAGEMENT ACCESS ONLY  
NOT user/data traffic

---

## WEB UI TRAFFIC SHAPING

Special case ACL:

- limits bandwidth for Web UI (80/443)
- applies only to router-generated traffic
- IPv4 only (in this version) :contentReference[oaicite:2]{index=2}

---

## CRITICAL BEHAVIOR

Traffic shaping:

→ ACTIVE even if ACL disabled (after commit)

---

## ARIA RULE

If user reports:

- “can’t access device”
- “GUI not loading”
- “SSH not responding”

ARIA MUST:

→ check Management ACL FIRST
→ NOT assume network failure

## WTM 4000 — Hardware Protection Behavior

## CORE CONCEPT

Hardware protection =

→ TWO radios
→ ONE active transmitter
→ ONE standby transmitter

Both units:
→ ALWAYS receiving

---

## PRIMARY / SECONDARY ROLES

- Primary → preferred active unit
- Secondary → standby (takes over on failure)

---

## ACTIVE vs STANDBY

Active:
→ transmitting (Tx enabled)

Standby:
→ Tx muted
→ Rx still active :contentReference[oaicite:0]{index=0}

---

## FAILOVER BEHAVIOR

On failure:

1. Active unit fails
2. Standby becomes Active
3. Traffic rerouted automatically

---

## CONVERGENCE TIME

< 1 second for service restoration :contentReference[oaicite:1]{index=1}

---

## CRITICAL INSIGHT

Failover is:

→ L2 SERVICE RESTORATION  
NOT just RF switching

---

## WHAT IS PROTECTED

- radio hardware failure
- RFM failure
- cable failure (to aggregator)
- internal device failure :contentReference[oaicite:2]{index=2}

---

## DEPENDENCY

WTM depends on:

→ external aggregator (CTR or 3rd party)

for:

→ LAG (link aggregation)

---

## LAG REQUIREMENT

- LACP OR microBFD
- WTM is TRANSPARENT to LAG protocol :contentReference[oaicite:3]{index=3}

---

## CRITICAL ARCHITECTURE RULE

WTM = L2 transport only

L3/MPLS handled on aggregator

## WTM 4000 — Protection Decision Logic

## FAILURE DETECTION SOURCES

- RF failure
- hardware failure
- link failure (LAG)

---

## SWITCH CONDITION

IF:
Active unit unhealthy

THEN:
Switch to standby

---

## REVERTIVE BEHAVIOR

Modes:

- normal → auto return to primary
- time-of-day → scheduled return

---

## CRITICAL INSIGHT

System prefers:

→ PRIMARY

but will remain on secondary if unstable

---

## DIAGNOSTIC TOOL

Manual switch available:

→ used for testing failover

## WTM 4000 — FIPS 140-3 Behavior

## CORE CONCEPT

FIPS mode enforces:

→ government-grade cryptographic compliance

---

## SYSTEM IMPACT

Enabling FIPS:

- changes allowed crypto algorithms
- enforces stricter integrity validation
- disables non-compliant methods :contentReference[oaicite:0]{index=0}

---

## CRITICAL BEHAVIOR

When FIPS is enabled:

- TACACS+ is DISABLED
- hmac-md5 authentication NOT allowed
- certain TLS ciphers MUST be removed before enabling :contentReference[oaicite:1]{index=1}

---

## ENABLEMENT RULE

- FIPS license REQUIRED
- reboot REQUIRED after enabling :contentReference[oaicite:2]{index=2}

---

## ALARM CONDITION

Alarm:

→ FIPS config status ≠ operational status

---

## CRITICAL INSIGHT

FIPS mode:

→ breaks compatibility with legacy systems

## WTM 4000 — Strong Security Behavior

## CORE CONCEPT

Strong Security mode:

→ enforces stricter device-level security rules

---

## ENFORCEMENT

- blocks weak cryptographic algorithms
- enforces stronger password standards :contentReference[oaicite:3]{index=3}

---

## ENABLEMENT

- Strong Security license REQUIRED
- CLI ONLY configuration :contentReference[oaicite:4]{index=4}

---

## HTTP BEHAVIOR

If HTTP disabled:

→ port 80 blocked
→ only HTTPS allowed

---

## CRITICAL INSIGHT

Security modes:

→ REMOVE functionality to increase security

## WTM 4000 — Alarm System Behavior

## ALARM STRUCTURE

Each alarm contains:

- Alarm name
- Description
- Severity

Severity levels:

- Critical
- Major
- Minor
- Warning :contentReference[oaicite:0]{index=0}

---

## CRITICAL INSIGHT

Severity ≠ impact

Example:
- Warning (RF degradation) → can still impact traffic
- Major (interface down) → obvious failure

---

## ALARM CATEGORIES (LOGICAL GROUPING)

### RF / RADIO
- demodulator_not_locked
- rsl_too_high / too_low
- snr_degraded
- xpd_too_low

---

### TRAFFIC / NETWORK
- ethernet_port_link_down
- l1la_member_down
- l1la_partner_unreachable
- acm_mismatch

---

### HARDWARE
- rfm_hw_failure
- module_missing
- temperature_overload
- badpwr

---

### SECURITY / ENCRYPTION
- pe_decryption_failure
- pe_negotiation_failed
- pe_max_time_exceeded

---

### SYSTEM / SOFTWARE
- flash_lifetime
- high_ram
- high_nvram
- system_clock_invalid

---

### SYNC / TIMING
- ptp_servo_not_locked
- synce_in_holdover

---

## CRITICAL INSIGHT

Alarms map directly to system layers:

- RF layer
- L2/L3 layer
- Hardware layer
- Security layer