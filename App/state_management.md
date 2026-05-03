# ARIA State Management

ARIA must track active operational states in real time.

## Trackable States

- Customer request pending
- Waiting for PM approval
- Waiting for field report
- Ticket unresolved
- Follow-up required
- Escalation in progress

---

## State Rules

1. If ARIA initiates an action (request, escalation, approval check):
   → A state must be created

2. ARIA must not forget active states until:
   - Resolved
   - Cancelled
   - Replaced by updated state

3. ARIA must follow up automatically if no response is received within a reasonable time

---

## Example

Customer asks for update →
No report exists →

STATE CREATED:
"Waiting for field report (Project ABC)"

ARIA ACTION:
Message field manager

If no response:
→ Follow up again
→ Optionally escalate to PM

---

## Resolution

Once report is received:
→ State is cleared
→ ARIA proceeds with approval workflow