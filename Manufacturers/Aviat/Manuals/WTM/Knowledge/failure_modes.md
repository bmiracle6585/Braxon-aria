## WTM 4000 — Radio Failure Modes

## NO LINK

Possible causes:

- no carrier configured
- frequency mismatch
- wrong polarization
- encryption mismatch

---

## INTERMITTENT LINK

Likely causes:

- interference
- poor alignment
- fading
- MIMO instability

---

## LOW CAPACITY

Causes:

- modulation downshift
- low SNR
- ATPC limiting power

---

## COMPLETE TRAFFIC LOSS (ENCRYPTION)

Cause:

→ Link ID mismatch

---

## PARTNER DEVICE FAILURE

Symptoms:

- degraded link
- XPIC/MIMO failure
- alarms raised

---

## SYNC FAILURE (MIMO)

Cause:

→ SyncE instability

Result:

→ MIMO collapse

## WTM 4000 — Traffic Failure Modes

## LINK UP / NO TRAFFIC

Most common causes:

- VLAN not defined
- VLAN mismatch
- wrong VLAN membership

---

## INTERMITTENT TRAFFIC

Causes:

- MTU mismatch (especially L1LA)
- QoS misconfiguration
- congestion / storm control

---

## LOW THROUGHPUT

Causes:

- QoS limiting traffic
- L1LA capacity drop
- RF modulation downshift

---

## COMPLETE TRAFFIC LOSS (L1LA)

Causes:

- MTU too small
- VLAN misconfig
- member link failure

---

## LOOP / NETWORK INSTABILITY

Causes:

- STP misconfig
- L2 loops

---

## ROUTING FAILURE

Causes:

- wrong next hop
- OSPF mismatch
- missing route

---

## MANAGEMENT LOSS

Causes:

- VLAN misconfig
- loopback misuse
- LSP triggering port shutdown

## WTM 4000 — Administration Failure Modes

## CONFIG LOST AFTER CHANGE

Cause:

→ changes not committed

---

## MASS CONFIG ROLLBACK

Cause:

→ reverting to older commit

Effect:

→ multiple configs lost unintentionally

---

## CONFIG LOAD FAILURE

Cause:

- invalid file
- version mismatch

---

## FEATURE NOT WORKING

Cause:

→ missing license

---

## SUDDEN FEATURE LOSS

Cause:

→ trial license expired

---

## DEVICE REBOOT / RESET

Cause:

- software upgrade
- license-triggered reset
- manual restart

---

## LOGIN FAILURE

Causes:

- wrong credentials
- TACACS+ unreachable
- fallback disabled

---

## TOTAL LOCKOUT (CRITICAL)

Cause:

→ TACACS enabled + fallback disabled + server unreachable

---

## SESSION BLOCKED

Cause:

→ max session limit reached

---

## PASSWORD REJECTION

Cause:

→ password rules not met

## WTM 4000 — Status Interpretation Failures

## LINK UP / TRAFFIC ZERO

Dashboard shows:
- interface UP
- no throughput

Likely causes:
- VLAN issue
- routing issue

---

## RADIO UP / DEGRADED PERFORMANCE

Dashboard shows:
- link UP
- low modulation
- low throughput

Cause:
→ RF degradation

---

## NO ALARMS BUT ISSUE EXISTS

Possible causes:
- threshold not triggered
- configuration issue (not fault condition)

---

## MULTIPLE ALARMS

Cause:
→ cascading failure

RULE:
Find ROOT alarm, not symptoms

---

## SENSOR NORMAL / TRAFFIC BAD

Cause:
→ L2/L3 issue (not RF)

---

## LOGS SHOW COMMIT EVENTS

Indicates:
→ recent configuration change

Possible cause of issue

## WTM 4000 — USB Autoconfiguration Failure Modes

## CONFIG NOT LOADING

Causes:

- incorrect filename
- wrong serial number
- backup file present
- invalid config file

---

## LICENSE NOT APPLYING

Causes:

- wrong serial number
- incorrect system time
- invalid license file

---

## DEVICE MISCONFIGURED

Cause:

→ wrong USB config inserted

---

## CONFIG LOAD BUT NOT ACTIVE

Cause:

→ commit not performed

---

## NO BACKUP CREATED

Cause:

- USB not mounted
- filesystem issue

---

## PARTIAL DEPLOYMENT

Cause:

- license loaded but config missing
- config loaded but license missing

## WTM 4000 — Management ACL Failure Modes

## TOTAL ACCESS LOSS (CRITICAL)

Cause:

→ ACL blocks all subnets

---

## PARTIAL ACCESS

Symptoms:

- GUI works, SSH doesn't (or vice versa)

Cause:

→ port-specific rule mismatch

---

## INTERMITTENT ACCESS

Cause:

- overlapping rules
- incorrect ordering

---

## SERVICE BLOCKED

Examples:

- SNMP not working → UDP 161 blocked
- NETCONF not working → TCP 830 blocked

---

## LOCKOUT SCENARIO

Cause:

→ ACL applied BEFORE verifying allowed subnet

---

## WEB UI SLOW / UNRESPONSIVE

Cause:

→ traffic shaping enabled with low bandwidth

---

## SILENT FAILURE (HARDEST)

Cause:

→ DROP action (no response)

Result:

→ appears like network issue

## WTM 4000 — Hardware Protection Failure Modes

## NO FAILOVER

Cause:

- standby not healthy
- partner mismatch
- config mismatch

---

## PARTNER COMMUNICATION FAILURE

Alarm:

→ "Communication with partner device failed"

Cause:

- interconnect cable issue
- VLAN misconfig
- interface misconfig :contentReference[oaicite:5]{index=5}

---

## VERSION MISMATCH

Cause:

→ different software versions

Result:

→ protection may fail

---

## CONFIGURATION MISMATCH

Cause:

→ radio settings differ between units

Result:

→ alarms + no protection

---

## SWITCH FLAPPING

Cause:

→ unstable link

Controlled by:

→ guard timer

---

## NO TRAFFIC AFTER SWITCH

Cause:

- LAG misconfig on aggregator
- VLAN mismatch
- interface misconfig

---

## FALSE FAILURE DETECTION

Cause:

→ improper LACP/BFD timers

## WTM 4000 — Security Mode Failure Modes

## LOSS OF MANAGEMENT ACCESS

Cause:

→ TACACS+ disabled under FIPS

---

## AUTHENTICATION FAILURE

Cause:

- unsupported auth method (hmac-md5)
- incompatible crypto

---

## GUI ACCESS FAILURE

Cause:

→ HTTP disabled (port 80 blocked)

---

## CONFIG ENABLE FAIL

Cause:

→ required TLS ciphers not removed before FIPS enable

---

## POST-ENABLE OUTAGE

Cause:

→ reboot required after enabling FIPS

---

## INTEROPERABILITY FAILURE

Cause:

→ remote device not FIPS-compliant

---

## SECURITY LOCKOUT SCENARIO

Cause:

→ strong security rules exceed current credentials capability

## WTM 4000 — Alarm-Based Failure Logic

## CRITICAL ALARMS (IMMEDIATE ACTION)

pe_decryption_failure:
→ encryption mismatch / key failure

rfm_not_detected:
→ hardware missing or failed

self_test_failed:
→ device integrity failure

---

## MAJOR ALARMS (SERVICE IMPACT)

ethernet_port_link_down:
→ physical or config issue

l1la_member_down:
→ reduced capacity / aggregation issue

partner_unit_not_connected:
→ protection broken

remote_fade_low:
→ RF degradation

tx_power_degraded:
→ radio output issue

---

## WARNING ALARMS (EARLY WARNING)

ber thresholds exceeded:
→ RF degradation starting

snr_degraded:
→ link quality degrading

xpd_too_low:
→ polarization issue

---

## CRITICAL DIAGNOSTIC RULE

Multiple alarms:

→ ALWAYS find ROOT cause

Example:

snr_degraded + ber exceeded + acm mismatch  
→ root cause = RF issue

---

## FALSE ROOT CAUSE TRAP

Do NOT treat:

- acm_mismatch
- high_nvram
- warnings

as root cause without correlation