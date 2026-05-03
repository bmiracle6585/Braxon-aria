# ================================
# SECTION — CTR VLAN Reboot Triggers
# ================================

## No Reboot Required for Standard VLAN Changes

Standard VLAN configuration changes generally should not require reboot.

Examples:
- creating VLAN
- adding member ports
- changing untagged ports
- changing PVID
- changing acceptable frame type
- enabling ingress filtering
- configuring static MAC entries

---

## Do Not Reboot for VLAN Misconfiguration

ARIA must not recommend reboot for:
- VLAN mismatch
- wrong PVID
- tagged/untagged mismatch
- acceptable frame type issue
- missing member port
- ingress filtering issue

These are configuration problems, not reboot problems.

---

## Bridge Mode Caution

Changing bridge mode during runtime requires controlled shutdown/disable of related modules:
- spanning tree
- GVRP
- GMRP
- GARP
- Ethernet CFM, if running

ARIA should treat bridge mode changes as service-impacting and should not casually recommend them during active troubleshooting.