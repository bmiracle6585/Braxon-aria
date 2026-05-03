# ================================
# SECTION — VIAVI Reset / Restart Guidance
# ================================

## Restart Is Not Root Cause Repair

Pressing Restart is used to reinitialize the test after configuration changes.

It is appropriate after:
- changing interface settings
- turning laser on
- changing auto-negotiation
- connecting to line
- completing loopback setup

---

## Do Not Restart Instead of Fixing Setup

ARIA must not recommend restart as a fix for:
- wrong VLAN
- wrong CIR
- wrong frame size
- missing loopback
- bad fiber
- wrong SFP
- auto-neg mismatch

Fix the setup, then restart the test.

---

## Reset to Defaults

Reset test to defaults is useful when:
- previous configuration may be contaminating the test
- starting a fresh L2 or RFC2544 procedure
- unknown prior settings exist

Do not use reset to explain a failed service test.