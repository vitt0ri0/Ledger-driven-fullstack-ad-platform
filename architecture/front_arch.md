## ⚛️ 4. Frontend Architecture (React)

Frontend is oriented around operational workflows, not just screens: campaign control, wallet visibility, and integration monitoring.

```text
frontend/
  src/
    app/
    pages/
    features/
    shared/
```

🧠 architecture

app/

* router
* providers
* auth

pages/

* DashboardPage
* CampaignsPage
* BillingPage
* IntegrationsPage

features/

* billing/
* campaigns/
* integrations/
* reports/

shared/

* ui
* api
* config
* utils

Library choices and rationale:

* `React + TypeScript`: predictable UI composition with strong type safety
* `Vite`: fast local feedback and simple build setup
* `React Router`: route-level decomposition for dashboard modules
* `TanStack Query`: server-state caching, retries, stale/fresh policy control
* `React Hook Form + Zod`: efficient forms with schema-based validation

⸻

🔄 data flow

React → API → Django → DB → back

Frontend data flow:

* UI components trigger typed feature actions
* feature hooks call API client methods
* query/mutation state is coordinated by `TanStack Query`
* backend remains the source of truth for workflow and money state

⸻

🔌 API layer

```typescript
// shared/api/client.ts
export async function getWallet() {
  return fetch("/api/wallet").then((r) => r.json());
}
```

📡 TanStack Query

```typescript
function useWallet() {

  return useQuery({

    queryKey: ["wallet"],

    queryFn: getWallet,

  })

}
```

🧾 Forms

```typescript
const schema = z.object({
  amount: z.number().positive(),
})
```

---

Related docs:

- [Main README](../readme.md)
- [Architecture intent](./architecture_intent.md)
- [Backend architecture](./back_arch.md)
- [Testing strategy](./testing.md)
- [Money domain clarification](./ledger_fsm_clarification.md)