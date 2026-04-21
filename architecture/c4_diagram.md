# C4 Architecture Diagram

This document describes the project using C4 levels:

- Level 1: System Context
- Level 2: Containers
- Level 3: Key Components (Backend focus)

---

## C4 Level 1 - System Context

```mermaid
flowchart TB
  U[Operations User: Finance / Campaign Manager]
  AP[Ad Platform with Strong Money Consistency]
  PSP[Payment Provider]
  ADS[External Ad Platforms]
  ANA[Analytics / Reporting Tools]

  U -->|Manage campaigns, budget, wallet| AP
  AP -->|Top-up / payment events| PSP
  PSP -->|Webhook events, status updates| AP
  AP -->|Sync campaigns, spend, statuses| ADS
  ADS -->|Performance and spend data| AP
  AP -->|Export reports / KPIs| ANA
```

---

## C4 Level 2 - Container Diagram

```mermaid
flowchart TB
  subgraph Client["Client Side"]
    FE[React Dashboard: TypeScript + TanStack Query]
  end

  subgraph Platform["Ad Platform"]
    API[Django API + DRF: Business and domain logic]
    W[Celery Workers: Sync / Retry / Reconciliation]
    R[(Redis: Broker + Cache)]
    DB[(PostgreSQL: Source of transactional truth)]
  end

  PSP[Payment Provider]
  ADS[External Ad Platforms]

  FE -->|HTTPS JSON API| API
  API -->|enqueue jobs| R
  W -->|consume jobs| R
  API -->|read/write| DB
  W -->|read/write| DB

  API -->|payment requests| PSP
  PSP -->|webhooks| API
  W -->|sync pull/push| ADS
  ADS -->|events / metrics| W
```

---

## C4 Level 3 - Component Diagram (Django Backend)

```mermaid
flowchart TB
  subgraph Django["Django Backend (single deployable)"]
    REST[API Layer: DRF views/serializers/permissions]
    ACC[Accounts: Users, organizations, roles]
    CMP[Campaigns: Campaign lifecycle and budgets]
    INT[Integrations: Connections, OAuth, sync jobs]
    BIL[Billing: TopUp, Reservation, Charge, Refund orchestration]
    FSM[FSM Module: Transition rules and guards]
    LED[Ledger: Accounts, transactions, immutable entries]
    REC[Reconciliation: Consistency checks and mismatch handling]
    AUD[Audit: Idempotency keys, event logs]
    REP[Reporting: Aggregates, snapshots, views]
  end

  REST --> ACC
  REST --> CMP
  REST --> INT
  REST --> BIL
  REST --> REP

  BIL --> FSM
  BIL --> LED
  INT --> BIL
  REC --> LED
  REC --> INT
  REC --> AUD
  BIL --> AUD
```

---

## Notes

- `Billing` orchestrates money operations but does not replace ledger invariants.
- `Ledger` is the financial source of truth (double-entry + immutability).
- `FSM` guards process transitions and keeps workflow logic explicit.
- `Reconciliation` verifies internal records against external systems and raises discrepancies.
