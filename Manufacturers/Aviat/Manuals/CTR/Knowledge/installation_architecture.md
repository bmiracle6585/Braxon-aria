# CTR 8300 / 8500 — Installation Architecture

## PHYSICAL DESIGN OVERVIEW

## CHASSIS LAYOUT

## SLOT STRUCTURE

## MODULE PLACEMENT RULES

## POWER ARCHITECTURE

## GROUNDING REQUIREMENTS

## CABLING TYPES

## RF CONNECTION FLOW

## ETHERNET / FIBER CONNECTION FLOW

## COOLING / THERMAL DESIGN

## RACK MOUNTING

## FAILURE RISKS DURING INSTALL

## FIELD INSIGHTS

# ================================
# SECTION — CTR VLAN / Bridge Architecture
# ================================

## Customer Bridge Architecture

In customer bridge mode, CTR behaves like a standard Ethernet switch.

Traffic may be:
- untagged
- priority tagged
- C-VLAN tagged

Use cases:
- simple customer handoff
- standard VLAN switching
- basic access/trunk transport

---

## Provider Edge Bridge Architecture

Provider edge bridge mode supports provider-style Ethernet services.

It uses:
- C-VLAN component
- S-VLAN component
- Customer Edge Ports
- Provider Edge Ports
- Provider Network Ports
- Customer Network Ports

Purpose:
- transport customer VLANs across a provider network
- encapsulate customer traffic inside service VLANs
- support E-LINE and E-LAN services

---

## C-VLAN Component

C-VLAN represents customer VLAN behavior.

Used for:
- customer-facing VLANs
- customer traffic classification
- C-VLAN spanning tree behavior

---

## S-VLAN Component

S-VLAN represents provider/service VLAN behavior.

Used for:
- service transport
- provider network forwarding
- E-LINE / E-LAN services

---

## Provider Edge Port

Provider Edge Port is a logical port created by mapping a C-VLAN to an S-VLAN.

Provider Edge Port operational state depends on:
- Customer Edge Port being up
- S-VLAN being active

---

## Customer Edge Port

Customer Edge Port connects to the customer side and participates in C-VLAN behavior.

---

## Provider Network Port

Provider Network Port connects to the provider network side and carries S-VLAN behavior.

Default provider bridge port type:
- Provider Network Port

---

## Customer Network Port

Customer Network Port can classify customer traffic into service VLAN transport.

Types:
- port-based
- S-tagged

---

## Multiple Instance Architecture

CTR 8540 can operate with multiple switch instances.

Each instance has:
- its own mapped interfaces
- its own VLAN configuration
- isolated forwarding behavior unless explicitly interconnected

This matters because the same VLAN ID on different switch instances does not automatically mean traffic will pass.