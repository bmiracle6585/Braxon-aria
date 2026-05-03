# ARIA Action Triggers

ARIA must convert certain situations into actions.

---

## Trigger: Missing Daily Report

Condition:
- Customer requests update
- No report exists

Action:
- Notify field manager
- Create state: waiting_for_report

---

## Trigger: Pending Approval

Condition:
- Report exists
- Status = pending

Action:
- Notify PM / Owner
- Ask for approval
- Create state: waiting_for_approval

---

## Trigger: Approved Report

Condition:
- Report status = approved_external

Action:
- Respond to customer

---

## Trigger: No Response

Condition:
- State exists
- No response after time threshold

Action:
- Follow up
- Escalate if needed

---

## Trigger: Internal Issue Detected

Condition:
- Problem identified during troubleshooting

Action:
- Route to internal operations
- Notify assigned personnel