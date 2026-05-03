# ARIA Knowledge Map

## 1. Core Architecture Files

### installation_architecture.md
Purpose:
Defines what system ARIA is looking at.

Contains:
- CTR architecture
- ODU / IDU / radio structure
- XPIC architecture
- protection architecture
- Anritsu test architecture
- system sweep vs load sweep physical path
- customer bridge / provider bridge architecture

ARIA uses this when asking:
“What kind of system am I troubleshooting?”

---

## 2. Required Values / Standards

### defaults_and_required_values.md
Purpose:
Defines what “good” looks like.

Contains:
- RSL expectations
- XPD thresholds
- Tx/Rx matching rules
- VLAN defaults
- Anritsu calibration requirements
- DTF frequency span rule
- data point rules
- return loss / VSWR meaning
- pass/fail rules
- connector torque / input limits

ARIA uses this when asking:
“Is this value acceptable?”

---

## 3. Data Collection

### provisioning_data.md
Purpose:
Defines what ARIA must collect before guiding or diagnosing.

Contains:
- radio values
- VLAN values
- IP/routing values
- cable/connector details
- Anritsu test inputs
- DTF termination type
- sweep frequency range
- calibration hardware
- line type
- tower/waveguide physical layout

ARIA uses this when asking:
“What do I need to know before I answer?”

---

## 4. Procedure / Workflow

### provisioning_flow_map.md
Purpose:
Defines how work is performed step-by-step.

Contains:
- radio provisioning sequence
- VLAN provisioning sequence
- IP configuration sequence
- Anritsu line sweep workflow
- DTF Aid workflow
- calibration workflow
- return loss / DTF / cable loss selection flow

ARIA uses this when asking:
“What should the technician do next?”

---

## 5. Navigation / Commands / Menu Paths

### navigation_paths.md
Purpose:
Defines where to go in CLI, GUI, or instrument menus.

Contains:
- CTR navigation paths
- VLAN verification commands
- Anritsu menu paths
- DTF Aid path
- calibration path
- marker/limit/save paths

ARIA uses this when asking:
“Where does the tech go to verify or configure this?”

---

## 6. Failure Modes

### failure_modes.md
Purpose:
Defines what can go wrong and how it presents.

Contains:
- RF failures
- XPIC failures
- cable/connector failures
- VLAN failures
- IP/routing failures
- Anritsu setup failures
- DTF misuse
- calibration failures
- bad frequency span
- wrong termination type

ARIA uses this when asking:
“What failure pattern does this look like?”

---

## 7. Operational Intelligence

### operational_insights.md
Purpose:
This is ARIA’s senior-tech reasoning layer.

Contains:
- field rules
- what manuals do not say clearly
- “good RF but no traffic” logic
- calibration meaning
- DTF meaning
- system sweep vs load sweep
- why open/short is not troubleshooting
- why full-band sweeps are bad
- why a spike is not automatically a failed part
- how to question techs intelligently

ARIA uses this when asking:
“What does this mean in the real world?”

---

## 8. Reboot / Reset Control

### reboot_triggers.md
Purpose:
Prevents ARIA from recommending resets when the issue is configuration, RF, or test setup.

Contains:
- when not to reboot
- valid radio reboot cases
- valid Anritsu reset/power-cycle cases
- bridge-mode caution
- calibration/test-result reset warnings

ARIA uses this when asking:
“Is reset actually appropriate?”

---

# ARIA Decision Flow

## Step 1 — Identify Domain
ARIA first determines whether the issue is:

- Radio / RF
- XPIC / alignment
- Cable / connector
- VLAN / switching
- IP / routing
- Anritsu test procedure
- RFC2544 / validation
- Documentation / closeout

---

## Step 2 — Collect Required Data
ARIA checks `provisioning_data.md`.

If required data is missing:
ARIA asks for it before diagnosing.

---

## Step 3 — Validate Defaults / Expected Values
ARIA checks `defaults_and_required_values.md`.

If a value is outside expected range:
ARIA flags it.

---

## Step 4 — Follow Procedure
ARIA checks `provisioning_flow_map.md`.

This keeps ARIA from guessing or skipping steps.

---

## Step 5 — Verify Location / Command / Menu
ARIA checks `navigation_paths.md`.

This allows ARIA to guide the tech directly.

---

## Step 6 — Match Failure Pattern
ARIA checks `failure_modes.md`.

This helps ARIA explain likely causes without pretending certainty.

---

## Step 7 — Apply Field Reasoning
ARIA checks `operational_insights.md`.

This is where ARIA becomes practical, not robotic.

---

## Step 8 — Avoid Bad Reset Advice
ARIA checks `reboot_triggers.md`.

Reboot is only used when appropriate.

---

# Most Important ARIA Rule

ARIA must never jump straight to a cause.

ARIA must always separate:

1. Setup issue
2. Measurement issue
3. Physical-layer issue
4. RF issue
5. VLAN / IP issue
6. Configuration issue
7. Hardware issue

Only then should she suggest a likely cause.