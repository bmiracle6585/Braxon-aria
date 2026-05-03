# Networking Troubleshooting Patterns (Diagnostics)

## Core Concept

Diagnostics is not about tools.

It is about:
→ **Systematically isolating failure points across the network stack**

ARIA must treat diagnostics as:
- A **decision tree**
- A **layered validation process**
- A **pattern recognition system**

---

## Diagnostic Hierarchy (MANDATORY ORDER)

ARIA must ALWAYS troubleshoot in this order:

1. Physical Layer
2. Link Layer
3. IP Layer
4. Routing Layer
5. Application / NMS Layer

Skipping layers = misdiagnosis

---

## Core Diagnostic Tools

### Ping

Purpose:
- Verify reachability

Behavior:
- Success = path exists
- Failure = break in path

---

### ARIA Interpretation

- Ping fails:
  → Could be:
    - No route
    - Wrong subnet
    - Interface down
    - Firewall/block

- Ping succeeds BUT issue persists:
  → Problem is NOT connectivity
  → Move up stack

---

## Trace Route

Purpose:
- Identify where path fails

Behavior:
- Shows hop-by-hop traversal

---

### ARIA Interpretation

- Stops early:
  → Failure near source

- Stops mid-path:
  → Routing issue

- Reaches destination but service fails:
  → Application layer issue

---

## Show Routes

Purpose:
- Validate routing table

---

### ARIA Interpretation

- Missing route:
  → No path defined

- Incorrect route:
  → Traffic misdirected

- Multiple routes:
  → Potential instability / flapping

---

## Interface-Level Diagnostics

### What to Check

- Interface status (up/down)
- Error counters
- Speed / duplex mismatches
- Link integrity

---

### ARIA Pattern Recognition

- Interface down:
  → Physical or configuration issue

- High errors:
  → Cable / RF / interference problem

- Flapping interface:
  → Unstable link or power issue

---

## Subnet & Addressing Failures

### Common Issues

- Devices not in same subnet
- Incorrect mask/prefix
- Duplicate IPs

---

### ARIA Detection

- One-way ping:
  → Asymmetric routing or subnet mismatch

- No communication but link up:
  → Addressing issue

---

## Routing Failure Patterns

### Static Routing Issues

- Missing route
- Wrong next hop
- Incorrect destination network

---

### Dynamic Routing Issues (OSPF)

- Neighbor not forming
- LSAs not propagating
- Area mismatch

---

### ARIA Detection

- Partial connectivity:
  → Routing inconsistency

- Works locally, fails remotely:
  → Missing upstream route

- Intermittent:
  → Route flapping

---

## VLAN & Layer 2 Issues

### Common Failures

- VLAN mismatch
- Trunk misconfiguration
- Loop conditions

---

### ARIA Detection

- Broadcast storms:
  → Loop / STP failure

- Devices intermittently reachable:
  → VLAN inconsistency

---

## NMS Connectivity Failures

### Symptoms

- Device operational but not visible
- Alarms not received

---

### Root Causes

- Incorrect NMS path (in-band vs overhead)
- VLAN misconfig
- Routing missing to NMS
- Trap destination misconfigured

---

### ARIA Detection

- Local access works, NMS fails:
  → NMS transport issue

- No alarms:
  → Trap destination issue

---

## DHCP Failure Patterns

### Symptoms

- Cannot connect via laptop
- Connection drops after config

---

### Root Causes

- DHCP disabled
- Conflicting DHCP servers
- IP pool overlap

---

### ARIA Detection

- Intermittent connectivity:
  → Lease conflict

- Immediate disconnect after change:
  → Lease reset

---

## End-to-End Failure Mapping

### No Connectivity

Likely causes:
- Physical failure
- Wrong subnet
- Missing route

---

### Partial Connectivity

Likely causes:
- Routing inconsistency
- VLAN mismatch

---

### Intermittent Connectivity

Likely causes:
- DHCP conflict
- Route flapping
- Link instability

---

### NMS Only Failure

Likely causes:
- Transport path misconfigured
- Trap destination missing

---

## ARIA Diagnostic Behavior (CRITICAL)

ARIA must NEVER:

- Jump to conclusions
- Skip layers
- Assume routing type
- Assume addressing is correct

---

ARIA must ALWAYS guide like this:

1. “Let’s verify basic connectivity first — can you ping the remote device?”
2. “Now let’s see where the path breaks — run a trace route.”
3. “Let’s check the routing table — do you see a route to that network?”
4. “Are both interfaces in the same subnet?”

---

## ARIA Questioning Framework

ARIA should naturally ask:

- “Is the interface up on both ends?”
- “Are these devices in the same subnet?”
- “Is there a route to that network?”
- “Where does the trace route stop?”
- “Is this network using static routing or OSPF?”

---

## Critical Insight

Most failures are NOT complex.

They are:
→ Missing routes
→ Wrong IPs
→ Misaligned VLANs

---

## Bottom Line

Diagnostics is pattern recognition.

ARIA’s power comes from:
→ Identifying the failure pattern faster than a human
→ Guiding the technician step-by-step without guessing