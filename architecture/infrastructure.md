# Infrastructure Layer

Infrastructure should stay simple for MVP, but ready for growth.

### Core runtime components

- `PostgreSQL`: primary transactional database for domain and ledger data
- `Redis`: Celery broker/cache and short-lived coordination state
- `Django API` + `Celery workers`: separated runtime units
- `React app`: static frontend bundle served via CDN or edge

### Environment strategy

- `local`: docker-compose for quick setup
- `staging`: production-like environment for integration and reconciliation checks
- `production`: isolated services with strict secrets and access controls

### Operational basics

- Centralized logs for API and worker jobs
- Metrics for queue depth, job failures, and reconciliation drift rate
- Alerts for failed money operations, stuck retries, and ledger/reconciliation mismatches

---

Related docs:

- [Main README](../readme.md)
- [Deployment approach](./deployment.md)
