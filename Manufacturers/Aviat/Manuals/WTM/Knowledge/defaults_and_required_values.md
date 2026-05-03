# WTM 4000 — Required Values & Constraints

## RF PARAMETERS (REQUIRED)

- Frequency band
- Channel bandwidth (10–80 MHz)
- Modulation (QPSK–4096 QAM)
- Tx power limits

---

## CAPACITY CONSTRAINTS

- Max throughput:
  → up to 2.5 Gbps :contentReference[oaicite:4]{index=4}
- Dependent on:
  - channel size
  - modulation
  - traffic profile

---

## INTERFACE REQUIREMENTS

- RJ45 ports (10/100/1000)
- SFP+ (1G / 2.5G / 10G)

---

## POWER REQUIREMENTS

- ±24 / ±48 VDC input :contentReference[oaicite:5]{index=5}
- PoE supported (802.3at / bt)

---

## ENVIRONMENTAL LIMITS

- Temp:
  - -33°C to +55°C (standard)
  - extended to +65°C :contentReference[oaicite:6]{index=6}

- Altitude:
  - up to 4500m

---

## NETWORKING REQUIREMENTS

Must define:

- IP addressing (IPv4 / IPv6)
- VLAN structure
- Routing type (static / OSPF / BGP)

---

## MANAGEMENT REQUIREMENTS

Must define:

- Management IP
- Access method (SSH / SNMP / NMS)
- Authentication (AAA)

---

## CRITICAL CONSTRAINTS

- All configuration occurs on ONE device (no distributed node system)
- No plug-in modules (fixed architecture)
- VLAN / routing misconfig will break traffic even if RF is healthy

---

## ARIA ENFORCEMENT RULE

If missing:

- VLAN information
- IP addressing
- routing type

ARIA MUST:

→ STOP and request this information  
→ NOT proceed with assumptions

## WTM 4800 — Additional Required Parameters

## RF STRUCTURE (CRITICAL)

Must define:

- E-Band frequency (71–86 GHz)
- Microwave band frequency (11–23 GHz) :contentReference[oaicite:4]{index=4}
- Channel sizes:
  - E-Band: up to 2000 MHz
  - Microwave: 7–112 MHz

---

## CAPACITY EXPECTATIONS

- Single channel:
  → up to 10 Gbps
- Multi-band:
  → up to 20 Gbps :contentReference[oaicite:5]{index=5}

---

## MODULATION LIMITS

- E-Band: up to 512 QAM
- Microwave: up to 4096 QAM :contentReference[oaicite:6]{index=6}

---

## CRITICAL DEPENDENCIES

Performance depends on:

- RF alignment (more critical than WTM 4000)
- weather conditions (rain fade impact)
- multi-path configuration

---

## REQUIRED DESIGN INPUTS

Before provisioning, must know:

- Is link E-Band only or Multi-Band?
- Are both radios configured?
- Expected capacity vs required capacity

---

## ARIA ENFORCEMENT RULE (UPDATED)

If WTM 4800:

ARIA MUST ask:

→ “Is this running multi-band or single carrier?”
→ “Are you seeing full capacity or reduced throughput?”

If capacity issue:

→ DO NOT assume network issue first  
→ VERIFY RF path distribution

## WTM 4000 — Radio Requirements

## REQUIRED FOR LINK UP

- at least one carrier enabled
- matching frequency (both ends)
- compatible modulation
- correct polarization (XPIC)

---

## REQUIRED FOR XPIC

- both carriers enabled
- identical frequency plan
- matching modulation
- matching power

---

## REQUIRED FOR MIMO

- two devices configured (primary/secondary)
- SyncE operational
- XPIC configured

---

## REQUIRED FOR ENCRYPTION

- Payload encryption enabled BOTH SIDES
- Matching Link ID

FAILURE:
→ traffic drops completely :contentReference[oaicite:9]{index=9}

## WTM 4000 — Traffic Requirements

## VLAN REQUIREMENTS

- VLAN must be defined
- VLAN must be assigned to ports
- VLAN must match both ends

---

## L1LA REQUIREMENTS

- MTU ≥ 2500
- VLAN configured correctly
- ICF enabled (for bandwidth awareness)
- proper QoS applied

---

## ROUTING REQUIREMENTS

Static:
→ valid next hop required

OSPF:
→ matching area + timers

---

## Q-IN-Q REQUIREMENTS

- correct TPID
- correct mapping rules

---

## QoS REQUIREMENTS

- classifiers must exist
- policies must be applied to ports

## WTM 4000 — Administration Requirements

## CONFIG MANAGEMENT

- changes require COMMIT
- rollback requires COMMIT

---

## LICENSING

- required for feature enablement
- time/date must be correct for license validation :contentReference[oaicite:7]{index=7}

---

## SOFTWARE

- valid software package required (.swpack)
- device must reach remote server if used

---

## USER MANAGEMENT

- at least one ADMIN user required
- SECURITY role required for user control

---

## TACACS+

- server reachable
- shared key must match
- fallback recommended (avoid lockout)

---

## MFA / SAML

- time sync REQUIRED (token validation)
- provider ID must match
- certificate must match

## WTM 4000 — USB Autoconfiguration Requirements

## USB DEVICE

- FAT32 format REQUIRED

---

## LICENSE FILE

- must match unit serial
- correct filename format required

---

## CONFIG FILE

.config:
→ AUTOConfig<serial>.config

.xml:
→ must be generated via ProVision

---

## SYSTEM REQUIREMENTS

- correct system time
- autoconfig enabled

---

## BACKUP RULE

backup file presence may block auto config

## WTM 4000 — Management ACL Requirements

## REQUIRED FOR SAFE CONFIG

- at least ONE subnet allowed
- correct service ports defined
- rule order verified

---

## RECOMMENDED PRACTICE

- configure ACL in TEST mode first
- validate access BEFORE commit

---

## TRAFFIC SHAPING RULES

- applies only to ports 80/443
- only one ACL allowed for shaping
- IPv4 only (current version) :contentReference[oaicite:3]{index=3}

## WTM 4000 — Hardware Protection Requirements

## MINIMUM HARDWARE

- 4 WTM units
- 2 aggregators :contentReference[oaicite:6]{index=6}

---

## REQUIRED CONNECTIONS

- partner interconnect cable
- IF cross connect cable (≤18 GHz)

---

## NETWORK REQUIREMENTS

- all devices in same L2 domain
- LAG configured on aggregators

---

## CONFIG REQUIREMENTS

- identical config on both sides
- identical radio parameters

---

## LICENSE REQUIREMENT

FEAT-HW-PROTECT license REQUIRED

---

## INTERFACE RULES

- Data interface defined
- Partner VLAN defined
- LACP forwarding enabled

---

## CRITICAL RULE

Partner VLAN:

→ must NOT overlap with data VLAN :contentReference[oaicite:7]{index=7}

## WTM 4000 — Security Requirements

## FIPS MODE

- FIPS license REQUIRED
- reboot REQUIRED
- incompatible ciphers MUST be removed

---

## STRONG SECURITY MODE

- strong security license REQUIRED
- CLI access REQUIRED

---

## HTTP ACCESS

- port 80 disabled when HTTP redirect enabled

---

## AUTHENTICATION

- legacy methods NOT supported in FIPS

## WTM 4000 — Alarm Interpretation Rules

## REQUIRED PRACTICE

- always check severity
- always correlate alarms
- always validate with system state

---

## CRITICAL RULE

Alarm alone is NOT diagnosis

It is:

→ indicator only