# Deployment Approach

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

---

Related docs:

- [Main README](../readme.md)
- [Infrastructure layer](./infrastructure.md)
