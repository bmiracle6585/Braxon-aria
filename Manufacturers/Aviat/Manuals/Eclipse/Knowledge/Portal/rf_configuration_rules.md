# RF Configuration Rules

## Core Parameters (Link Plug-in)

- Frequency
- Channel bandwidth
- Modulation
- Tx Power
- TR Spacing
- ATPC

These define the RF link completely.

---

## Modulation Behavior

Supported:
QPSK → 4096 QAM :contentReference[oaicite:0]{index=0}

Rules:
- Higher modulation = higher capacity + lower robustness
- Lower modulation = lower capacity + higher stability

---

## Tx Power Logic

- Max Tx power limited by:
  - License
  - Selected modulation :contentReference[oaicite:1]{index=1}

- If Tx set below max:
  → No automatic backoff occurs

---

## ATPC (Adaptive Power Control)

Behavior:
- Increases power when RSL/SNR drops
- Decreases power when fade clears :contentReference[oaicite:2]{index=2}

Inputs:
- RSL (signal level)
- SNR (quality)

Key Logic:
- Good RSL + poor SNR → increase power
- High RSL → reduce power

Limit:
- Cannot exceed configured max Tx power