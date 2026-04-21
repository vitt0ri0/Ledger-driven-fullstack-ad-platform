| layer | workflow |
| --- | --- |
| FSM | Manages campaign states and transitions between processing stages. |
| Ledger | Records money movements, reserves, and operation-based charges. |
| Reconciliation | Matches internal records with external events and confirms data consistency. |


---

This is the core design axis of the project.

### 4.1 FSM (workflow control)

FSM defines legal state transitions for business processes (for example, reservations, payment 
processing, sync lifecycle).

Responsibilities:

- Allow only valid transitions
- Make business workflow explicit and testable
- Prevent hidden state mutation in ad-hoc service code

### 4.2 Ledger (money source of truth)

Ledger stores immutable money records using double-entry principles.

Core invariants:

- Every transaction is balanced
- Ledger entries are immutable
- Balances are derived from entries, not overwritten
- Operations are idempotent under retries

Typical money operations:

- `TopUp`: adds funds
- `Reservation`: locks budget before spend
- `Charge`: converts reserved funds to actual spend
- `Refund`: returns funds after rollback/correction

### 4.3 Reconciliation (truth verification)

Reconciliation continuously validates that internal and external realities match.

Checks are performed between:

- Internal ledger vs. billing/business records
- Internal records vs. payment provider events
- Internal campaign spend vs. external ad platform signals

Output:

- discrepancy reports
- repair/replay tasks
- audit-ready traces for incident analysis

---

Related docs:

- [Main README](../readme.md)
- [Architecture intent](./architecture_intent.md)
- [Backend architecture](./back_arch.md)
- [Frontend architecture](./front_arch.md)
- [Testing strategy](./testing.md)