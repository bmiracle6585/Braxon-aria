# CTR — IP Configuration and Network Logic

## PURPOSE
This file teaches ARIA how IP configuration, routing, ARP, and diagnostics behave in the CTR system.

ARIA must use this file when supporting:
- no connectivity across a link
- RFC2544 failures with good RF
- ping failures
- routing issues
- VLAN misconfigurations
- intermittent packet loss
- DHCP issues

---

## CORE IP BEHAVIOR

### What IP Does
- IP delivers packets based on destination address
- Communication depends on:
  - correct IP addressing
  - proper routing
  - MAC resolution (ARP)

ARIA must understand:
RF can be perfect, but if IP is wrong → traffic fails

---

## DEFAULT SYSTEM BEHAVIOR

From system defaults:

- IP routing: **Enabled**
- TTL: **64**
- ICMP:
  - redirects: enabled
  - unreachable: enabled
  - echo (ping): enabled
- ARP timeout: **300 sec**
- ARP retries: **3**
- DHCP relay: **Disabled**
- Load sharing: **Disabled**
- Path MTU discovery: **Disabled** :contentReference[oaicite:0]{index=0}  

---

## ARIA INTERPRETATION OF DEFAULTS

- Ping should work unless blocked or misconfigured
- Routing is active by default
- Devices should respond to ICMP unless intentionally disabled
- ARP failures will break communication even if routing is correct

---

## IP ADDRESSING LOGIC

### Rules
- Each interface must have a valid IP
- Only one primary IP per interface
- VLAN interfaces are used for IP assignment

### Failure Patterns

#### No IP / Wrong IP
- No communication
- Ping fails immediately

#### Wrong Subnet
- Devices cannot reach each other directly
- Requires routing (if misconfigured → failure)

---

## ROUTING LOGIC

### What Routing Does
- Determines where packets go
- Uses:
  - connected routes
  - static routes

### Static Route Behavior
Example:
ip route 60.0.0.0 255.0.0.0 50.0.0.10 :contentReference[oaicite:1]{index=1}  

Means:
- To reach 60.x.x.x → send to 50.0.0.10

---

## ROUTING FAILURE PATTERNS

### No Route to Destination
- Ping fails
- Traffic never leaves interface

### Wrong Next Hop
- Traffic sent to wrong device
- Blackhole condition

### Routing Disabled
- No forwarding between networks

---

## ARP LOGIC (CRITICAL)

### What ARP Does
- Maps IP → MAC address

### Behavior
- Device must resolve MAC before sending traffic
- Uses ARP cache

---

## ARP FAILURE PATTERNS

### Symptoms
- Ping fails even with correct IP
- Intermittent connectivity
- First packet delay

### Causes
- ARP timeout issues
- MAC mismatch
- VLAN misconfiguration
- device not responding

---

## VLAN LOGIC

### Key Concept
- IP is tied to VLAN interfaces

Example:
interface vlan 1
ip address 40.0.0.1 255.0.0.0 :contentReference[oaicite:2]{index=2}  

---

## VLAN FAILURE PATTERNS

- Correct IP but wrong VLAN → no communication
- Traffic isolated unintentionally
- Mis-tagging between devices

---

## PING (ICMP) LOGIC

### What Ping Tests
- Reachability
- latency
- packet loss

### Behavior
- Uses ICMP echo request/reply :contentReference[oaicite:3]{index=3}  

---

## PING FAILURE INTERPRETATION

### No Response
- device unreachable
- routing issue
- ARP failure
- firewall/ICMP disabled

---

### Intermittent Response
- congestion
- RF errors
- cabling issues
- ARP instability

---

## TRACE ROUTE LOGIC

### What It Does
- Shows path to destination
- identifies where failure occurs

Uses:
- TTL increments
- ICMP time exceeded messages :contentReference[oaicite:4]{index=4}  

---

## TRACE ROUTE INTERPRETATION

- Failure at first hop → local issue
- Failure mid-path → routing problem
- inconsistent path → unstable routing

---

## ICMP CONTROL LOGIC

### ICMP Redirects
- informs device of better route

### ICMP Unreachable
- indicates destination cannot be reached

---

## ICMP FAILURE PATTERNS

- Disabled ICMP → ping fails but traffic may still pass
- Missing unreachable → harder to diagnose failures

---

## DHCP RELAY LOGIC

### What It Does
- forwards DHCP requests across subnets

Example:
ip helper-address 60.0.0.10 :contentReference[oaicite:5]{index=5}  

---

## DHCP FAILURE PATTERNS

- No IP assigned to client
- incorrect gateway assignment
- relay not configured

---

## NETWORK VS RF DECISION LOGIC

ARIA must always separate:

### RF Issue
- low RSL
- poor XPD
- BER errors at radio level

---

### IP / NETWORK ISSUE
- good RSL but no traffic
- ping fails
- routing errors
- VLAN issues
- ARP failures

---

## FIELD FAILURE PATTERNS

### Good RF, No Connectivity
Likely:
- missing IP config
- routing issue
- VLAN mismatch
- ARP failure

---

### Ping Works, Throughput Fails
Likely:
- congestion
- MTU mismatch
- packet fragmentation
- QoS limitations

---

### Intermittent Connectivity
Likely:
- ARP instability
- cabling issues
- routing flaps

---

## ARIA TROUBLESHOOTING QUESTIONS

When diagnosing IP issues, ARIA must ask:

1. What are the IP addresses on both ends?
2. Are they in the same subnet?
3. Is routing enabled?
4. Are static routes configured?
5. Can you ping the far end?
6. Can you ping the gateway?
7. What does traceroute show?
8. Are VLANs configured correctly?
9. Are ARP entries resolving?
10. Is DHCP being used?

---

## CRITICAL DO-NOT-GUESS RULE

ARIA must NOT:
- assume RF is the issue when RSL is good
- assume IP is correct without verification

ARIA must validate:
- IP layer
- routing layer
- ARP layer

before concluding root cause

---

## SOURCE
CTR 8500-8300 IP Configuration Guide  
Version 3.16.0 :contentReference[oaicite:6]{index=6}