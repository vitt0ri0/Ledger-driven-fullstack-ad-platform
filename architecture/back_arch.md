🏗 2. Backend Architecture (Django)

### Libraries choice

* `Django`: core web framework, ORM, migrations, admin tooling
* `Django REST Framework`: API serializers, permissions, pagination, browsable contracts
* `psycopg`/`psycopg2`: stable PostgreSQL driver for transactional workloads
* `Celery`: asynchronous jobs for sync, retries, and reconciliation routines
* `redis-py` + `Redis`: broker/cache layer for async execution and short-lived state
* `django-filter`: consistent filtering for list/reporting endpoints
* `pytest` + `pytest-django`: fast and explicit test setup for domain and API layers
* `factory-boy`: reusable test data factories for complex financial scenarios
* `drf-spectacular`: OpenAPI schema generation for stable backend/frontend contracts

📁 Apps structure

```
backend/
  accounts/
  campaigns/
  integrations/
  billing/
  ledger/
  fsm/
  reporting/
  audit/
```

Why `Django + DRF`:

* mature transaction handling and ORM patterns for finance-related domains
* strong ecosystem for admin operations and business dashboards
* explicit serializers/permissions for stable API contracts
* natural fit for modular app boundaries and incremental domain growth


🔐 accounts

* User
* Organization
* Membership
* Roles

⸻

📊 campaigns

* Campaign
* Budget
* Status
* External mapping

⸻

🔌 integrations

* IntegrationConnection
* OAuthCredential
* SyncJob
* ExternalEntity

responsibilities:

* data pull
* webhook ingestion
* retry logic

Async and reliability:

* `Celery` workers execute integration sync, retries, and delayed operations
* `Redis` is used for queue transport and short-lived coordination state
* jobs should be idempotent and observable to avoid duplicate side effects

⸻

💰 billing (business layer)

* Wallet
* TopUp
* Reservation
* Charge
* Refund

⸻

📒 ledger (money core)

models

* LedgerAccount
* LedgerTransaction
* LedgerEntry

invariants

* double-entry
* immutable
* balanced totals

⸻

🔁 fsm

Options:

* simple implementation (dict transitions)
* or a library (for example `django-fsm`, but optional)
* NB: it is advised to keep FSM and Ledger logic locally and handwritten, for transparency in such critical flow, otherwise you have to thoroughly check library contraints, invariants etc.

⸻

📊 reporting

* aggregates
* snapshots
* materialized views

⸻

🧾 audit

* audit log
* idempotency keys
* external event log

---

Related docs:

- [Main README](../readme.md)
- [Architecture intent](./architecture_intent.md)
- [Frontend architecture](./front_arch.md)
- [Testing strategy](./testing.md)
- [Money domain clarification](./ledger_fsm_clarification.md)