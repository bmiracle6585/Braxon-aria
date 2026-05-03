# WTM 4000 — Decision Engine Logic

## Purpose

This file tells ARIA how to decide where to go first when supporting WTM 4000 issues.

ARIA must use this as a routing layer only.

It does not replace:
- operational_insights.md
- provisioning_flow_map.md
- failure_modes.md
- defaults_and_required_values.md
- navigation_paths.md

It connects them.

---

## Core Rule

ARIA must not troubleshoot WTM issues from a single symptom.

ARIA must correlate:

1. Dashboard state
2. Active alarms
3. Sensor values
4. System log
5. Recent configuration changes
6. Current operating mode

---

## First Question Logic

When a tech reports a WTM issue, ARIA first determines:

- Is the link down, degraded, or passing no traffic?
- Is RF healthy?
- Is traffic affected?
- Was anything changed recently?
- Are there active alarms?
- Is this protected, aggregated, or standalone?

---

## Primary Decision Paths

## 1. Link Down

Check in this order:

1. Dashboard
2. Alarms
3. Carrier status
4. TX mute
5. RSL / SNR
6. Frequency / modulation / encryption match

Likely causes:
- TX muted
- carrier not configured
- demodulator not locked
- frequency mismatch
- encryption mismatch
- RFM failure

ARIA must not assume hardware failure until RF and configuration are checked.

---

## 2. Link Up but No Traffic

Check in this order:

1. VLAN definition
2. VLAN membership
3. access vs trunk mode
4. routing / static route / OSPF
5. management ACL
6. L1LA / L2 aggregation path

Likely causes:
- VLAN not defined
- wrong VLAN membership
- trunk/access mismatch
- missing route
- ACL blocking management
- traffic bypassing L1LA

ARIA must treat this as a traffic-layer issue before RF.

---

## 3. Low Throughput

Check in this order:

1. modulation level
2. SNR
3. BER
4. L1LA member status
5. QoS / policing / scheduling
6. RF fade or interference

Likely causes:
- modulation downshift
- degraded RF
- L1LA member down
- QoS limiting traffic
- storm control / policing

ARIA must separate RF capacity loss from Ethernet/QoS restriction.

---

## 4. Intermittent Drops

Check in this order:

1. system log timeline
2. alarms by timestamp
3. PCR / performance history
4. weather / fade conditions
5. L1LA member state
6. protection switch count
7. SyncE / PTP state

Likely causes:
- rain fade
- interference
- protection switching
- aggregation instability
- sync instability
- recent commits

ARIA must correlate time before recommending action.

---

## 5. Management Access Failure

Check in this order:

1. management IP
2. VLAN path
3. Management ACL
4. TACACS / local fallback
5. FIPS / strong security state
6. session limits / lockout
7. USB autoconfig or recent commit

Likely causes:
- ACL blocking access
- wrong VLAN
- TACACS unreachable
- fallback disabled
- HTTP disabled
- session limit reached
- security hardening change

ARIA must not assume device failure.

---

## 6. Protection / Redundancy Issue

Check in this order:

1. active / standby mode
2. partner communication alarm
3. partner VLAN
4. IF XC cable
5. software version match
6. config match
7. LAG / LACP / microBFD on aggregator
8. switch count / guard timer

Likely causes:
- partner interconnect issue
- config mismatch
- software mismatch
- aggregator LAG issue
- standby not healthy

ARIA must determine whether the event was failure or protection switching.

---

## 7. Security / Encryption Issue

Check in this order:

1. FIPS enabled?
2. Strong Security enabled?
3. encryption alarms
4. TLS cipher compatibility
5. TACACS compatibility
6. HTTP / HTTPS access state
7. system time

Likely causes:
- FIPS blocking TACACS
- hmac-md5 unsupported
- HTTP disabled
- license missing
- time invalid
- encryption key negotiation failed

ARIA must recognize security as a possible cause of sudden access or traffic loss.

---

## 8. USB Autoconfig Issue

Check in this order:

1. Was USB inserted?
2. System log, program root
3. file naming
4. unit serial match
5. FAT32 format
6. backup file present
7. commit status

Likely causes:
- wrong config loaded
- config skipped due to backup file
- license mismatch
- incorrect system time
- config loaded but not committed

ARIA must treat USB insertion as a possible configuration event.

---

## Alarm Correlation Logic

ARIA must group alarms by layer:

### RF
- demodulator_not_locked
- snr_degraded
- ber thresholds
- xpd_too_low
- remote_fade_low

### Traffic
- ethernet_port_link_down
- l1la_member_down
- l1la_partner_unreachable
- acm_mismatch

### Hardware
- rfm_not_detected
- rfm_hw_failure
- module_missing
- badpwr
- temperature_overload

### Security
- pe_decryption_failure
- pe_negotiation_failed
- Fips_config_oper_status_diff

### Sync
- ptp_servo_not_locked
- synce_in_holdover
- reboot_needed_due_ptp_mode_change

---

## Root Cause Rule

If multiple alarms are present:

ARIA must ask:

“What appeared first?”

The first alarm in time is usually closer to root cause.

Do not chase downstream alarms.

---

## Recent Change Rule

If the issue started after a change, ARIA prioritizes:

1. commit history
2. config diff
3. VLAN / ACL / routing change
4. security mode change
5. software / license change
6. USB autoconfig event

---

## Final Behavior

ARIA should guide the tech one step at a time.

She should not dump every possible cause.

She should say things like:

“Let’s separate RF from traffic first. Is the carrier up and showing stable RSL/SNR?”

or:

“If the RF side is clean and traffic is still dead, I want to look at VLAN membership next.”

---

## End