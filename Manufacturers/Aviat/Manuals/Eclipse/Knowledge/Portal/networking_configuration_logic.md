# Networking Configuration Logic (Aviat Eclipse)

## Core Concept

Networking configuration defines how nodes communicate, route traffic, and maintain management connectivity across the network.

ARIA must treat this as:
- A **system-wide design decision**, not a single-node task
- A **dependency-heavy configuration** (routing, addressing, VLANs, NMS paths)
- A **high-risk misconfiguration area**

---

## Addressing Fundamentals

### IPv4
- Format: nnn.nnn.nnn.nnn
- Uses CIDR notation (e.g. 192.168.1.0/24)
- Network + host portions defined by prefix

### IPv6
- 128-bit addressing
- Dual-stack supported (IPv4 + IPv6 operate independently)
- No translation between IPv4 and IPv6 :contentReference[oaicite:0]{index=0}
- Uses prefix notation (e.g. /64)

### ARIA Awareness

- Always confirm:
  - IPv4, IPv6, or both?
  - Prefix/mask provided?
- Never assume addressing structure
- IPv6 requires licensing

---

## Network Architecture Logic

### Layer 3 (Routed)
- Each node = unique network
- Uses routing (static or dynamic)
- Required for multi-site deployments

### Layer 2 (LAN)
- Same network across devices
- Unique host addresses only
- No routing required

### ARIA Behavior

- Determine:
  - “Are these nodes on the same LAN or routed network?”
- Misidentification = total failure of connectivity

---

## Routing Logic

### Static Routing
- Manual route entries required
- Includes:
  - Destination
  - Interface
  - Next hop
  - Default gateway

Use when:
- Small/simple networks
- No topology changes expected

---

### Dynamic Routing

Options:
- OSPF (preferred)
- RIP (limited to 15 hops) :contentReference[oaicite:1]{index=1}

Use when:
- Medium/large networks
- Ring topologies (REQUIRED)

---

### Critical Rules

- Never run OSPF and RIP across the network simultaneously
- Only mix at a **single interface boundary node** :contentReference[oaicite:2]{index=2}
- OSPF required for networks >15 hops

---

### ARIA Awareness

- Ask naturally:
  - “Is this network using OSPF or static routing?”
  - “Is this part of a larger routed network or standalone?”
- Detect instability symptoms:
  - Route flapping
  - Missing paths
  - Partial reachability

---

## NMS Transport Logic

### Over Radio Links
- 512 Kbps overhead shared with AUX channels
- More AUX = less NMS bandwidth :contentReference[oaicite:3]{index=3}

### Over SDH/SONET
- MSOH preferred (higher capacity)
- Cannot share with other device NMS

### In-Band NMS
- Runs over Ethernet payload instead of overhead
- Can be:
  - Layer 2 (bridged)
  - Layer 3 (routed)

---

### ARIA Awareness

- Identify NMS path:
  - Overhead vs in-band
- If in-band:
  - VLAN required
  - Routing may be required
- Misconfigured NMS = “device unreachable”

---

## Interface Addressing Logic

### Single IP Mode (Default)
- One IP for all interfaces
- Simpler, most common

### Interface Addressing Mode
- Each interface gets unique IP
- Used for:
  - Advanced routing
  - Network segmentation
  - Diagnostics

---

### Critical Rules

- Link endpoints must be on same subnet :contentReference[oaicite:4]{index=4}
- Unused interfaces:
  - Set to 0.0.0.0/0 or equivalent

---

### ARIA Awareness

- If interface addressing is used:
  - Expect complexity
  - Validate each interface individually
- Detect mismatch:
  - “Local and remote interfaces must be in the same subnet”

---

## DHCP Logic

### Purpose
- Allows laptop (Portal PC) to connect without knowing IP

### Behavior
- Lease time: ~30 seconds :contentReference[oaicite:5]{index=5}
- Auto-assigns IP to technician device

---

### Critical Rules

- Do NOT overlap DHCP ranges across devices
- Avoid enabling multiple DHCP servers at NOC
- Do not include device IP in DHCP pool

---

### ARIA Awareness

- If tech can’t connect:
  - Check DHCP enabled/disabled
  - Check IP conflicts
- Recognize symptom:
  - “Connection drops after config change” → DHCP lease reset

---

## Static Routing Execution Logic

Required Inputs:
- Destination network
- Interface
- Next hop (if Ethernet)
- Default gateway (optional)

---

### Key Behavior

- Link interfaces do NOT require next hop (PPP link) :contentReference[oaicite:6]{index=6}
- Ethernet interfaces DO require next hop

---

### ARIA Awareness

- Validate:
  - Missing next hop (common failure)
  - Incorrect destination prefix
- Detect:
  - One-way communication issues

---

## Default Gateway Logic

- Used for traffic toward NOC
- Reduces need for full routing tables

---

### ARIA Awareness

- Ask:
  - “Is there a defined NOC or central gateway?”
- Detect missing:
  - “Devices reachable locally but not globally”

---

## Trap Destinations (Monitoring)

- Sends alarms to NMS server
- Modes:
  - ProVision (summary)
  - Send All (detailed)

---

### ARIA Awareness

- If alarms not visible:
  - Check trap destination IP + port
  - Default port = 162

---

## In-Band NMS Logic

### L2 Bridged
- Shared LAN
- No routing needed

### L3 Routed
- Requires:
  - IP addressing
  - Static routes
- Dynamic routing NOT supported here

---

### Critical Rules

- VLAN auto-created
- STP must be considered to avoid loops
- Protected links must match configs

---

### ARIA Awareness

- Identify:
  - Bridged vs routed
- Detect:
  - VLAN mismatch
  - Loop conditions
  - Missing static routes

---

## Troubleshooting Tools

Available:
- Ping
- Trace Route
- Show Routes :contentReference[oaicite:7]{index=7}

---

### ARIA Behavior

- Guide technician to:
  - Verify reachability (Ping)
  - Trace path failures (Trace Route)
  - Validate routing table (Show Routes)

---

## ARIA Operational Intelligence (CRITICAL)

ARIA must NEVER:

- Assume addressing
- Assume routing type
- Assume VLAN usage
- Assume NMS transport method

---

ARIA must ALWAYS infer through questioning:

- “Is this a routed network or same-site LAN?”
- “Are we using static routing or OSPF?”
- “Is NMS in-band or over radio?”
- “Are these interfaces uniquely addressed?”

---

## Failure Patterns ARIA Must Recognize

- No connectivity → wrong subnet / missing route
- Partial connectivity → routing inconsistency
- Intermittent → DHCP / routing instability
- No NMS visibility → wrong transport path
- Looping / instability → STP / VLAN misconfig

---

## Bottom Line

Networking is not a step.

It is the **foundation layer** that determines whether anything else works.

ARIA must treat networking issues as:
→ **Root-cause candidates for most failures**