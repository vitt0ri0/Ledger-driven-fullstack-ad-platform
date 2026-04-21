# Testing Strategy

Testing focuses on correctness of money flows and predictability of workflow state.

## Backend tests

- Unit tests for domain services and FSM transition guards
- Transactional tests for ledger invariants (double-entry, immutability, balance checks)
- API tests for permissions, idempotency keys, and contract stability
- Integration tests for external sync jobs, retries, and reconciliation pipelines

## Frontend tests

- Component tests for core billing/campaign screens
- Hook tests for query/mutation behavior and loading/error states
- Form validation tests for `React Hook Form` + `Zod` schemas

## End-to-end and quality gates

- E2E scenarios: top-up -> reservation -> charge/refund -> reconciliation
- Smoke tests on every deployment to staging/production
- Minimal CI gate: lint + typecheck + test suites + migration checks

---

Related docs:

- [Main README](../readme.md)
- [Architecture intent](./architecture_intent.md)
- [Backend architecture](./back_arch.md)
- [Frontend architecture](./front_arch.md)
- [Money domain clarification](./ledger_fsm_clarification.md)
