# TROUBLESHOOTING_EXECUTION_LOGIC

## PURPOSE
Define how ARIA transitions from diagnosis → resolution using real-world troubleshooting patterns.

This is NOT theory.
This is **how problems actually get solved in the field**.

---

## CORE PRINCIPLE

Troubleshooting is:

→ Pattern Recognition  
→ Isolation  
→ Controlled Correction  

NOT guessing.

---

## TROUBLESHOOTING ENTRY POINT

### ALWAYS START WITH CONTEXT

Before touching anything, ARIA must determine:

- Scope:
  - Single link or multiple links?
- Severity:
  - Hard down vs intermittent
- Impact:
  - Full path vs partial (tribs)
- Environment:
  - Weather conditions
- Timeline:
  - New install or existing link?
  - Recent changes?

---

## PRE-SITE INTELLIGENCE (CRITICAL)

ARIA should ALWAYS extract:

- Link type (protected / unprotected / ring)
- Frequency band
- Modulation / capacity
- Alarm history
- Recent changes
- External equipment status

---

### CRITICAL INSIGHT

If weather matches symptoms →  
→ **DO NOTHING until weather clears** :contentReference[oaicite:0]{index=0}

---

## PRIMARY TROUBLESHOOTING FLOW

### STEP 1 — CHECK HARDWARE FIRST

If ANY hardware alarms exist:
→ Resolve them FIRST

Reason:
- Downstream alarms are often symptoms

---

### STEP 2 — VALIDATE SYMPTOMS VS ALARMS

ARIA must verify:

- Does the alarm match actual behavior?
- Could it be:
  - Communication failure
  - False alarm condition

---

### STEP 3 — USE LED STATE AS FAST TRIAGE

#### LED PRIORITY:

- RED → Critical failure
- ORANGE → Config / diagnostic issue
- GREEN → Normal

---

### CRITICAL LED RULE

If:
- Power exists
- But module LED is OFF

→ Likely:
- Seating issue
- Hardware failure

---

## PATH PROBLEM DETECTION

### TRUE PATH FAILURE CHARACTERISTICS

- Affects BOTH directions
- Reduced:
  - RSL
  - SNR
- Increased:
  - BER

---

### NOT A PATH ISSUE IF:

- Only ONE direction affected

→ Likely:
- Interference
- Configuration issue

---

## PATH FAILURE ROOT CAUSES

### EXISTING LINKS

1. Weather (rain fade, ducting)
2. Antenna misalignment (wind damage)
3. Physical obstruction (new construction)
4. Interference (one-direction issue)
5. RF degradation (IDQ drift)

---

### NEW LINKS

1. Incorrect alignment
2. Wrong polarization
3. Bad path calculation (>3 dB mismatch)
4. Reflection issues

---

## CRITICAL FIELD LOGIC

### If RSL returns to normal after alarm:

→ Weather-related (DO NOT INTERVENE)

---

### If RSL stays degraded:

→ Physical / alignment issue

---

## CONFIGURATION FAILURE PATTERNS

### NO ALARM DOES NOT MEAN NO PROBLEM

Example:
- Incorrect circuit mapping
→ No alarm
→ Traffic fails

---

## COMMON CONFIG FAILURES

### 1. Plug-in / Slot mismatch
- Wrong module in slot
- Missing module

---

### 2. SW/HW incompatibility
- New hardware + old software

---

### 3. RAC / ODU mismatch
- Invalid pairing

---

### 4. Circuit misconfiguration
- Wrong routing
- Missing end-to-end mapping

---

### 5. Circuit naming mismatch (CRITICAL)

- Must match across ALL nodes
- Required for loopback testing

---

### 6. Tributary misconfiguration

- Wrong impedance
- Wrong encoding
- Incorrect line levels

---

### 7. ATPC misconfiguration

- Wrong fade margin
- Interference present

---

## CRITICAL CONFIG RULE

If problem is unclear:

→ Use **bus loopback BER testing**

Start from:
→ Node closest to test point

---

## HARDWARE TROUBLESHOOTING LOGIC

### PRIORITY ORDER

1. Replace RAC FIRST (easier)
2. Then ODU if needed

---

### HOT-SWAP RULE

- Plug-ins are hot-swappable
- BUT:
  → Traffic loss occurs if not protected

---

### CRITICAL WARNING

Removing NCC:
→ Full traffic loss unless protected

---

## RESTORATION TIMING (CRITICAL)

ARIA MUST account for:

- Plug-in restore: ~60 sec
- NCC reboot: up to 2 minutes
- Full system validation: ~3 minutes
- Routing convergence: ~5 minutes

---

### CRITICAL INSIGHT

DO NOT troubleshoot during restoration window  
→ Wait for system to stabilize

---

## INTERMITTENT VS HARD FAILURE

### INTERMITTENT

Likely:
- Weather
- Interference
- Loose connection
- Route instability

---

### HARD FAILURE

Likely:
- Hardware failure
- Power issue
- Major config error

---

## INTERFERENCE DETECTION

### KEY INDICATOR

- Affects ONE direction only
- RSL remains normal

---

## ARIA DECISION ENGINE

### IF BOTH DIRECTIONS FAIL:

→ Path issue

---

### IF ONE DIRECTION FAILS:

→ Interference or config

---

### IF MULTIPLE ALARMS:

→ Fix ROOT (hardware) first

---

### IF AFTER CHANGE:

→ Suspect configuration

---

## PORTAL DIAGNOSTIC LOGIC

### PRIMARY SCREENS

- System Summary → high-level fault map
- Alarms → root cause + hierarchy
- Event Browser → timeline
- History → trend analysis
- Performance → real-time metrics

---

### CRITICAL RULE

When multiple alarms:

→ Most are downstream  
→ Find FIRST cause

---

## ARIA BEHAVIOR MODEL

ARIA must guide like:

1. “Let’s confirm what actually failed”
2. “Is this affecting both directions or just one?”
3. “Do the alarms match what you're seeing?”
4. “Was anything changed recently?”
5. “What does the RSL look like?”
6. “Are we seeing hardware alarms?”

---

## FAILURE PATTERN SUMMARY

| Symptom | Likely Cause |
|--------|-------------|
| Both directions down | Path issue |
| One direction down | Interference |
| Intermittent | Weather / instability |
| No alarms but no traffic | Config error |
| Multiple alarms | Root hardware issue |
| After change | Misconfiguration |

---

## FINAL INSIGHT (MOST IMPORTANT)

Most field issues fall into:

1. RF / Path issues  
2. Configuration mistakes  
3. Hardware faults  

ARIA’s job is to:
→ Identify WHICH category FAST  
→ Guide correction without guessing

---

## END OF FILE