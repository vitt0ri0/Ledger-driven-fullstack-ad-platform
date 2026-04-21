# Architecture Intent

The project is backend-centric and optimized for fast MVP delivery with a small team, while preserving financial correctness.

## Priorities

- Clear domain boundaries in backend apps
- Reliable async integration flows
- Explicit state transitions (`FSM`)
- Ledger-first money storage and operations
- Reconciliation as a safety and trust layer

## High-level system view

- `Backend (Django + DRF)`: domain logic, API contracts, financial invariants
- `Frontend (React + TypeScript)`: operational dashboard for campaigns, billing, integrations
- `Async layer (Celery)`: sync, retry, and reconciliation jobs
- `Storage`: `PostgreSQL` (transactional data), `Redis` (queue/cache)

---

Related docs:

- [Main README](../readme.md)
- [Backend architecture](./back_arch.md)
- [Frontend architecture](./front_arch.md)
- [Money domain clarification](./ledger_fsm_clarification.md)
- [Testing strategy](./testing.md)
