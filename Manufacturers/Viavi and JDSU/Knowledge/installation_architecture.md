# ================================
# SECTION — VIAVI TEST ARCHITECTURE
# ================================

## Purpose
Define how VIAVI testing fits into the network validation process.

---

## Testing Layers

VIAVI testing is performed in three stages:

1. L2 Traffic Testing
2. Loopback Testing
3. RFC2544 Testing

---

## Functional Roles

### L2 Traffic
- Verifies link is operational
- Confirms signal, sync, and link state

---

### Loopback
- Reflects traffic back to source
- Allows testing without second device
- Validates path continuity

---

### RFC2544
- Performs service validation
- Measures:
  - throughput
  - frame loss
  - latency
  - jitter

---

## Test Progression

All testing must follow this order:

1. Link up (L2 Traffic)
2. Path validation (Loopback)
3. Service validation (RFC2544)

Skipping steps leads to invalid results.