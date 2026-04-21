# Ad Platform with Strong Money Consistency

Architecture draft for a B2B advertising platform focused on fast MVP delivery and financial correctness.

## 0) Assumptions

- Stack: `Django` + `React`
- Team: small development team
- Delivery: short time to MVP release

---

## 1) Architecture Intent

Backend-centric design with clear domain boundaries, explicit workflow transitions, and a ledger-first money model.

Details: [architecture/architecture_intent.md](architecture/architecture_intent.md)

---

## 2) Backend Architecture (Django)

Domain apps, API boundaries, async workers, and reliability rules are documented here: [architecture/back_arch.md](architecture/back_arch.md)

---

## 3) Frontend Architecture (React)

Feature structure, component layers, and library choices are documented here: [architecture/front_arch.md](architecture/front_arch.md)

---

## 4) Money Domain: FSM + Ledger + Reconciliation

Workflow control, financial invariants, and consistency checks are documented here: [architecture/ledger_fsm_clarification.md](architecture/ledger_fsm_clarification.md)

---

## 5) Suggested Implementation Sequence

Recommended order: establish backend contracts, implement ledger/FSM core, build frontend slices, then add reconciliation and observability.

---

## 6) Project Goals

Production-oriented architecture, strong money consistency, and scalable module boundaries for a small team.

---

## 7) Infrastructure Layer

MVP-oriented runtime based on `PostgreSQL`, `Redis`, `Django API`, and `Celery`, with staging-to-production promotion.

---

## 8) Testing Strategy

Backend, frontend, and E2E test approach is documented here: [architecture/testing.md](architecture/testing.md)

---

## 9) Deployment Approach

CI validation, staged rollout, rollback readiness, and post-deploy checks for money-critical flows.