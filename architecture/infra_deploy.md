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

# Deployment 

Deployment should optimize for fast iteration without sacrificing financial safety.

### Build and release flow

1. Pull request validation in CI (tests + quality gates)
2. Merge to main -> auto-deploy to staging
3. Run smoke + reconciliation sanity checks in staging
4. Promote to production with versioned release tags

### Deployment principles

- Zero-downtime migrations where possible
- Backward-compatible API changes between frontend/backend releases
- Feature flags for risky workflow or billing behavior changes
- Rollback plan for both app version and migration strategy

### Post-deploy verification

- Validate key business flows (campaign actions, wallet operations)
- Check worker health and queue backlog
- Confirm no new reconciliation discrepancies after release window