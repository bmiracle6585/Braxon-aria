# Verizon — Required Inputs Enforcement

## Context
Verizon provisioning requires strict adherence to provided design data.

ARIA must enforce input validation ONLY when operating in Verizon context.

---

## Core Rule

All provisioning data must be provided by Verizon (VzW).

ARIA must NOT:
- Assume values
- Generate placeholder data
- Continue with missing inputs

If required data is missing:
→ STOP progression
→ Request correct information

---

## Required Inputs

### Site Context
Determine:
- New site
- Existing site

---

### VLAN Information
- Required for new sites
- Must be provided by VzW

If existing:
- Confirm reuse

If missing:
→ STOP

---

### IP Addressing
Required:
- IPv4
- IPv6 (both sites)

Determine:
- New vs reused addressing

If missing:
→ STOP

---

### IPv6 Gateway
- Must be provided

If missing:
→ STOP

---

### TMN Port #4 Router Connection
- Requires router management port details

If missing:
→ STOP