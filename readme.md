# Ledger-driven fullstack ad platform

Architecture draft for a B2B advertising platform focused on fast MVP delivery and financial correctness. 
The goal is to have production-oriented architecture, strong money consistency, and scalable module boundaries for a small team of developers.

## 0) Constraints

- Stack: `Django` + `React`
- Team: small fullstack team
- Delivery: short time to MVP release

---

## 1) Architecture Intent

Backend-centric design with clear domain boundaries, explicit workflow transitions, and a ledger-first money model.

Details: [architecture/architecture_intent.md](architecture/architecture_intent.md)

Diagrams: [architecture/c4_diagram.md](architecture/c4_diagram.md)

---

## 2) Backend Architecture (Django)

Domain apps, API boundaries, async workers, and reliability rules are documented here: [architecture/back_arch.md](architecture/back_arch.md)

FSM design[fsm.py](backend/fsm/fsm.py)

---

## 3) Frontend Architecture (React)

Feature structure, component layers, and library choices are documented here: [architecture/front_arch.md](architecture/front_arch.md)

---

## 4) Money Domain: FSM + Ledger + Reconciliation

Workflow control, financial invariants, and consistency checks are documented here: [architecture/ledger_fsm_clarification.md](architecture/ledger_fsm_clarification.md)

---

## 5) Infrastructure Layer

MVP-oriented runtime based on `PostgreSQL`, `Redis`, `Django API`, and `Celery`, with staging-to-production promotion.
Details: [architecture/infrastructure.md](architecture/infrastructure.md)

---

## 6) Testing Strategy

Backend, frontend, and E2E test approach is documented here: [architecture/testing.md](architecture/testing.md)

---

## 7) Deployment Approach

CI validation, staged rollout, rollback readiness, and post-deploy checks for money-critical flows.
Details: [architecture/deployment.md](architecture/deployment.md)