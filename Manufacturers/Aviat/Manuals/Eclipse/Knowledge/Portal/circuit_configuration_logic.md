# CIRCUIT_CONFIGURATION_LOGIC

## PURPOSE

Define how circuits are created, routed, prioritized, and constrained within Eclipse Node, including traffic, auxiliary, sync, and wayside behaviors.

---

## CORE CONCEPT

Circuits = **backplane bus cross-connections between modules**

* Routed between:

  * RAC (links)
  * DAC (data interfaces)
  * NCM (loop switch)
  * AUX modules
* Governed by:

  * Backplane capacity
  * Module compatibility
  * Port allocation
  * Protection mode

---

## CIRCUIT TYPES

### TRAFFIC CIRCUITS

* Carry customer payload (Ethernet / TDM)
* Routed via backplane bus
* Capacity limited by:

  * Link modulation
  * Bus size
  * Module limits 

---

### AUXILIARY CIRCUITS

* Carry:

  * NMS traffic
  * Management data
* Transported in LINK overhead (not payload)
* NOT protected in ring or loop switch configs 

---

### SYNC MULTICAST CIRCUITS

* Used for SyncE / clock distribution
* Routed across:

  * DAC GE3
  * RAC
  * DAC 4x / 16x
* Reduces available payload capacity per sync circuit 

---

### WAYSIDE CIRCUITS

* E1 access within STM1 links
* Independent of payload
* MUTUALLY EXCLUSIVE with AUX circuits 

---

## BACKPLANE BUS LOGIC

### AVAILABLE BUS SIZES

* 2.048 Mbps (E1)
* 1.544 Mbps (DS1)
* 34.368 Mbps (E3)
* 44.736 Mbps (DS3)
* 155.52 Mbps (STM1)

---

### CORE RULES

* Bus size MUST match:

  * RAC configuration
  * DAC configuration

* Bus capacity is SHARED between:

  * Traffic circuits
  * Sync circuits
  * Auxiliary circuits

* Misalignment → configuration errors / warnings

---

## CIRCUIT CREATION LOGIC

### METHOD 1 — DRAG & DROP

* Connect module → module
* Auto-creates circuit
* If no capacity specified:
  → MAX allowable assigned

---

### METHOD 2 — TABLE CONFIGURATION

* Select source module
* Assign:

  * Destination module
  * Ports
  * Capacity
* Supports:

  * Reordering
  * Splitting
  * Merging

---

## BULK ALLOCATION RULE (CRITICAL)

If NO circuits exist:

* First connection = BULK allocation
* Based on LOWEST capacity module

Example:

* 32xE1 → 16xE1
  → Result = 16xE1 allocation

---

## PORT-BASED PRIORITY LOGIC

### DEFAULT BEHAVIOR

* Port 1 = HIGHEST priority
* Higher port numbers = LOWER priority

---

### ADAPTIVE MODULATION IMPACT

When modulation drops:

* LOW priority circuits dropped FIRST
* Based on port numbering

---

### DPP RELATIONSHIP

* Remaining capacity after circuits = DPP capacity
* Circuits ALWAYS take priority over DPP 

---

## CAPACITY DISTRIBUTION

Total Link Capacity =

* Circuit allocation (backplane)
* Remaining → DPP / Ethernet

---

## CIRCUIT NAMING RULES

* Every circuit MUST have:

  * Unique name
* Must match across ALL nodes carrying it
* Tributary naming should align with circuit naming

---

## CIRCUIT MODIFICATION LOGIC

### OPERATIONS

* Move Up / Down → priority shift
* Split → divide circuit groups
* Simplify → merge contiguous circuits

---

### DELETE BEHAVIOR

* Delete → removes full circuit group
* Delete Individual → removes specific ports

---

## RING CIRCUIT LOGIC

### TYPES

* DROP / INSERT (local traffic)
* PASS-THROUGH (transit traffic)

---

### RULES

* Backplane must be:

  * E1 or DS1
* Ring capacity limited by:

  * Lowest link capacity

---

### RESOURCE USAGE

Drop/Insert circuits:

* Consume 1.5x backplane capacity

---

## DAC GE3 RULES (ETHERNET)

### KEY CONSTRAINTS

* 6 transport channels max
* Ports MUST be:

  * Sequential
  * Contiguous

---

### BANDWIDTH RULE

* MUST match across entire path

---

### MAX CAPACITY

* ~204 Mbps (E1 bus)
* Reduced by:

  * TDM circuits

---

### SPECIAL CONDITION

* Disable MAC learning when using external switching

---

## AUXILIARY CIRCUIT RULES

* Must start at port 1 (CRITICAL)
* Otherwise:
  → NMS bandwidth reduced significantly 

---

## SYNC MULTICAST RULES

* Each sync circuit reduces payload capacity
* Requires:

  * Sync license
  * DAC GE3 enabled

---

### BEST PRACTICE

Route:

* E1/DS1 → DAC GE3 → RAC

NOT:

* Direct DAC → RAC

Reason:

* Preserves clock holdover capability

---

## WAYSIDE RULES

* Requires:

  * DAC 4x
  * STM1 + E1 configuration

---

### CONFLICT RULE (CRITICAL)

* WAYSIDE and AUX cannot coexist

---

## FAILURE / MISCONFIGURATION CONDITIONS

ARIA SHOULD FLAG:

* Bus size mismatch
* Capacity over-allocation
* Non-contiguous port mapping
* Incorrect module pairing
* AUX not starting at port 1
* Circuit mismatch across nodes
* Ring capacity imbalance

---

## CONFIGURATION FLOW (ARIA MODEL)

1. Define required circuits (type + capacity)
2. Set bus size
3. Configure module capacity (Plug-ins)
4. Create circuits (drag/table)
5. Validate:

   * Capacity
   * Port order
   * Compatibility
6. Assign names
7. Commit (Send)

---

## CRITICAL DESIGN INSIGHT (FOR ARIA)

Circuits are the **traffic routing layer**:

* Protection = how traffic survives
* Circuits = where traffic flows

ARIA must:

* Understand circuit-to-port mapping
* Track priority via port order
* Detect capacity conflicts
* Predict traffic loss under modulation shifts
* Validate end-to-end consistency

---

## END OF FILE
