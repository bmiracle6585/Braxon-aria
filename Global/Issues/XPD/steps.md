# XPD – Troubleshooting Steps

## Step 1: Confirm baseline values

- Identify the measured XPD on both sides.
- Identify the engineered or expected XPD target (commonly ~32 / 32).
- Determine severity:
  - Slight variation → e.g., 29 / 35
  - Severe variation → e.g., 25 / 45 or unavailable reading

- Confirm RSL condition:
  - Are RSL values healthy and on target?
  - If RSL is not on, do not treat this as a pure XPD issue.

---

## Step 2: Determine if alignment is the primary domain

If RSL is healthy:
- Treat this as a feedhorn alignment issue first.
- Do not default to polarity hookup issues.

If RSL is not healthy:
- Address RSL before continuing XPD-specific troubleshooting.

---

## Step 3: Confirm feedhorn leveling vs alignment

Ask:
- Were the feedhorns leveled?
- How was level verified?
- How far off level is the adjusted feedhorn?

Important:
- Leveling the feedhorn is not the same as aligning for XPD.
- A feedhorn can be perfectly level and still have poor XPD.

---

## Step 4: Verify correct alignment method was used

Ask:
- Was only one side adjusted for XPD?
- Was the opposite side left level?

If both sides were adjusted:
- Reset approach.
- Return one side to level.
- Perform XPD alignment from a single side only.

---

## Step 5: Execute controlled XPD alignment

- Select one side to adjust.
- Keep the opposite side fixed and level.

During adjustment:
- Make small, controlled movements.
- Do not move quickly.
- Allow values to settle before continuing.

Goal:
- Bring both XPD values toward balance and toward the engineered target.
- Prioritize symmetry (e.g., moving 25 / 45 toward 32 / 32).

Do not:
- chase one number at the expense of the other,
- treat one polarity independently.

---

## Step 6: Evaluate alignment result

After adjustment:
- Are values moving toward balance?
- Are both values approaching target?
- Are changes repeatable and stable?

If values improve:
- continue fine alignment.

If values do not improve:
- reassess method before assuming hardware.

---

## Step 7: Identify technician execution issues

Common causes of poor results:
- adjusting both sides simultaneously,
- moving too quickly,
- assuming level equals alignment,
- not measuring or tracking feedhorn position,
- failing to verify repeatability.

ARIA should correct process before escalating problem domain.

---

## Step 8: Consider hardware or physical issues (only after alignment is confirmed)

If:
- alignment method was correct,
- only one side was adjusted,
- values do not respond to adjustment,

Then consider:
- feedhorn condition,
- antenna internal issues,
- OMT or internal polarization components.

Do not move to hardware until alignment has been properly executed.

---

## Step 9: Use ATPC as a controlled diagnostic (optional)

If needed:
- enable ATPC temporarily,
- reduce transmit power in controlled increments (≤ 2 dB).

Observe:
- how performance responds,
- whether balance improves or shifts.

ATPC should be used as a diagnostic aid, not a correction method.

---

## Step 10: Re-evaluate domain

After each major step, determine:

Is the issue most likely:
- feedhorn alignment,
- technician execution,
- hardware condition,
- environmental or path-related?

Do not continue broad troubleshooting once the domain is clear.

---

## Final Rule

If RSL is healthy, ARIA should treat XPD issues as a feedhorn alignment problem first.

She should:
- enforce correct alignment method,
- avoid adjusting both sides,
- prioritize balance between values,
- and only move to hardware after alignment has been properly executed.