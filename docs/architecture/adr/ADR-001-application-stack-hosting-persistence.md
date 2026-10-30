# ADR-001 — Application stack, hosting model and persistence

## Status

Proposed — 2026-10-30. Awaiting explicit Systems Engineering acceptance; this record is not accepted and grants nothing until a human reviewer changes this section and the control manifest records the artifact.

Resolves candidate register item `ADR-CAND-001` (DELIVERY_ROADMAP section "ADR decisions required before S1/S2") and decision `DEC-001` of LEGACY-SE-REVIEW-001. Also fixes the method for `DEC-009` (performance budgets) jointly with ADR-005.

## Traceability

- Functionalities: `LEGACY-CAP-001`, `LEGACY-CAP-003`, `LEGACY-CAP-004`, `LEGACY-CAP-005`
- Requirements: `LEGACY-BIZ-001`, `LEGACY-BIZ-004`, `LEGACY-BIZ-006`, `LEGACY-FNC-064`, `LEGACY-NFR-003`, `LEGACY-NFR-007`, `LEGACY-NFR-011`, `LEGACY-NFR-017`, `LEGACY-NFR-018`, `LEGACY-NFR-020`, `LEGACY-NFR-022`
- Work package: `LEGACY-WORK-002` (acceptance topics: app stack, hosting; persistence input to "source of truth")
- Downstream consumers: `LEGACY-WORK-003` (bootstrap), `LEGACY-WORK-004` (shell), `LEGACY-WORK-009` (adapters), `LEGACY-WORK-013` (GUI commands)
- Decision owner: Systems Engineering
- Prepared in run `DEV-20261030T185520Z-751CB5` against control commit `caca50c7e23a892d37e63cc14091f8cf725374d6`

## Context

The product baseline v0.1.0 fixes the delivery target as a responsive browser application for phone and desktop with installable (PWA) behavior before any native client (`LEGACY-BIZ-006`, `LEGACY-FNC-064`). The manifest records `application.delivery_target = responsive_web_pwa` and `application.status = architecture_pending`. `legacy_app` is an empty scaffold whose `docs/IMPLEMENTATION_BOUNDARIES.md` asks for a recorded decision covering platform, workspace isolation, persistence, migrations, domain-event/projection behavior and deterministic test setup before any framework is chosen. `DOMAIN_MODEL.md` states that database/provider selection is an ADR, not a baseline assumption.

Constraints that the stack must satisfy:

- One shared domain model across all surfaces and modules (`LEGACY-BIZ-001`, `LEGACY-BIZ-004`; reference principle DP-02).
- Atomic completion → milestone → analytics → reward update (`LEGACY-FNC-009`) and exactly-once effects under retry (`LEGACY-NFR-005`, `LEGACY-NFR-014`), which call for a transactional store with unique constraints.
- Server-side authorization on every data path (`LEGACY-NFR-002`, `LEGACY-NFR-013`), detailed in ADR-002.
- Deterministic decimal money with per-currency scale (`LEGACY-NFR-011`) and timezone-aware timestamps (`LEGACY-NFR-022`).
- Encryption in transit and at rest with platform-standard mechanisms (`LEGACY-NFR-003`) and documented backup/restore before irreplaceable data is stored (`LEGACY-NFR-017`).
- Automated build, unit, integration, authorization and visual tests with candidate fingerprints (`LEGACY-NFR-020`), executed by the independent harness in `legacy_verification_tooling`, which is already Node.js ≥ 22 with Playwright 1.62.1 and pixelmatch.
- A single owner working with coding agents: the stack should be mainstream, strongly typed end to end, and boring to operate.

The roadmap asked to avoid backend/frontend lock-in "before trade study". The trade study is summarised under *Considered alternatives*; it is a documentary comparison, not a prototype benchmark.

## Decision

### D1. Language and repository layout

1. The production application is written in **TypeScript** end to end, in a single **pnpm workspace monorepo** inside `legacy_app` with at least these packages: `packages/domain` (pure domain model, commands, events, policies, no I/O), `packages/contracts` (API and event schemas shared by server and client, expressed with Zod and exported as TypeScript types), `apps/api` (HTTP server), `apps/web` (browser client), `packages/testkit` (fixtures, clock, builders).
2. The domain package depends on nothing but the language; adapters (HTTP, database, storage, AI, integrations) depend on the domain, never the reverse. Module boundaries follow `DOMAIN_MODEL.md` "Candidate architectural boundaries" and are enforced by package dependency rules (lint rule or `dependency-cruiser`), so that a new life module adds a package without changing the shell or core entities (`LEGACY-BIZ-004`).
3. Node.js **LTS 22 or later** is the server runtime, aligned with the verification tooling's `engines` field.

### D2. Client

4. `apps/web` is a **React 19 + Vite** single-page application with TypeScript, built as an installable PWA (`vite-plugin-pwa`, Workbox). The service worker caches the application shell and static assets only; it never caches or replays authenticated data. Offline behavior is governed by ADR-006.
5. Routing uses the five-surface shell routes already registered in the manifest (`/`, `/map`, `/life`, `/insights`, `/me`) plus nested routes for goal/island detail and focus; navigation state per surface is preserved in memory and restored on return (`LEGACY-UX-003`).
6. Styling uses CSS custom properties as design tokens with a small utility layer; no runtime CSS-in-JS. Pixel-art rendering rules are set in ADR-004.

### D3. Server and API

7. `apps/api` is a **Fastify 5** HTTP server with the Zod type provider, serving a JSON API under `/api/v1` and, in the single-container deployment, the built client as static files.
8. Every route is declared in a **route registry** with its authorization policy, command/query schema and idempotency class; ADR-002 and ADR-005 make this registry the enforcement and test-coverage boundary.
9. The API is command/query shaped: mutations are the canonical domain commands listed in CONOPS section 5 (CreateGoal, LinkTask, CompleteAction, UndoCompletion, LogHabit, RecordFocusEvent, RecordHydration, ProposeCapture, ApproveProposal, ImportBatch, GrantResourceAccess, RevokeResourceAccess) and carry an idempotency key; reads return projections. GraphQL is not adopted.

### D4. Persistence

10. **PostgreSQL 16 or later** is the only system of record. One database holds workspace-scoped state tables, the append-only `domain_events` ledger, the `reward_transactions` ledger and projection tables, so that ADR-003's "one transaction" rule is implementable with ordinary ACID semantics.
11. Schema is managed with **Drizzle ORM** and **versioned SQL migrations** committed to `legacy_app`; migrations are forward-only and run as an explicit deploy step, never implicitly at request time. Row-Level Security policies are part of the migration set (ADR-002).
12. Data typing rules, binding for all modules:
    - Identifiers are UUIDv7 generated by the server, except client-generated idempotency keys and draft IDs (ADR-003).
    - Instants are `timestamptz`; every scheduling-relevant row also stores the IANA time zone used and the derived local calendar date, so DST and travel are deterministic (`LEGACY-NFR-022`).
    - Money is stored as **integer minor units** (`bigint`) with an ISO 4217 currency code and an explicit scale column; arithmetic in TypeScript uses `BigInt` or a decimal library, never IEEE floats; FX conversions store rate, rate source and timestamp beside the converted value (`LEGACY-NFR-011`). This primitive belongs to `packages/domain` even though the finance module is outside this work package, because changing it later would touch every ledger.
    - Restricted-class columns (per `DOMAIN_MODEL.md` sensitivity classification) are listed in a schema annotation so export, deletion and log-redaction tooling can enumerate them.
13. Attachments and media live in **S3-compatible object storage** behind a storage port with a local-filesystem adapter for development and tests; database rows hold metadata and a storage key, never the bytes. Access is by short-lived signed URL only (EXTERNAL_INTERFACES "Media storage").

### D5. Hosting model

14. The deployable unit is one **OCI container image** containing the API and the built client, configured exclusively through environment variables (12-factor); secrets are injected by the platform, never committed. A `docker compose` file provides PostgreSQL and a MinIO/filesystem storage adapter for local development and for integration tests.
15. Production runs on a **managed container platform with managed PostgreSQL** that provides TLS termination, encrypted volumes, automated daily snapshots and point-in-time recovery. Provider and region are an **operator selection to be recorded as an addendum to this ADR before the first hosted environment**, with these binding constraints: (a) managed PostgreSQL with PITR ≥ 7 days; (b) encryption at rest enabled; (c) a region acceptable for a user base in the UAE and Brazil, documented with its latency measurement; (d) exportable backups the owner can restore outside the provider. Candidate providers evaluated for fit are listed in *Considered alternatives*; none is selected here.
16. Before the first environment that stores finance records, personal memories or media, a **restore drill** is executed and recorded as verification evidence (`LEGACY-NFR-017`); ADR-006 defines the backup, retention and deletion policy.
17. There is one production environment and one ephemeral preview environment per candidate; no staging database is shared between candidates. The verification harness receives the candidate URL via `SDLC_*` environment variables as registered in the manifest (ADR-005).

### D6. Performance budget method (`DEC-009`)

18. Budgets are **measured, not assumed**: Lighthouse CI runs against the preview environment with the manifest `mobile-browser` profile under simulated mid-tier mobile throttling and against `desktop-browser`, and a Web Vitals beacon (opt-in, no user content) reports field data after release. Numeric budgets are established from the first three measured candidates on representative devices and then frozen as a control change, satisfying `LEGACY-NFR-018`; until then the provisional working targets are LCP ≤ 2.5 s on the throttled mobile profile and ≤ 100 ms optimistic feedback for completion interactions (`LEGACY-NFR-007`). These provisional numbers are not acceptance thresholds.

## Considered alternatives

- **Python backend (FastAPI) with a React client.** Rejected: splits the domain model across two languages, duplicating validation schemas and losing the shared-type guarantee that `LEGACY-BIZ-004` relies on. The SDLC GUI being Python is irrelevant to the product runtime.
- **Full-stack meta-framework (Next.js, Remix/React Router, SvelteKit).** Rejected for the first slices: server rendering and framework-owned routing add little for an authenticated, app-like PWA and couple the deployment model to the framework's hosting conventions. React with Vite keeps the client a pure static artifact.
- **Hono instead of Fastify.** Viable; Fastify chosen for its mature plugin ecosystem, schema-driven validation, and the explicit route declaration model that the authorization registry needs. Switching is contained to `apps/api` adapters.
- **Prisma instead of Drizzle.** Rejected because Row-Level Security with per-transaction `SET LOCAL` and SQL-first migrations are awkward in Prisma's client model; Drizzle keeps SQL visible to reviewers.
- **Backend-as-a-service (Supabase, Firebase).** Rejected for the system of record: authorization expressed only in provider policy language, provider-held credentials that would conflict with `LEGACY-NFR-019`, and weaker control over backup export and residency. Supabase-style RLS is adopted as a *technique* inside self-managed PostgreSQL instead.
- **Document store (MongoDB, DynamoDB) or SQLite-per-tenant.** Rejected: cross-aggregate transactions and unique idempotency constraints are first-class in PostgreSQL; per-tenant SQLite complicates shared workspaces and resource grants.
- **Event sourcing with an external broker (Kafka/NATS).** Rejected for S1–S3; ADR-003 adopts a ledger with synchronous projections in one database. A broker may be introduced when a projection needs asynchronous fan-out.
- **Native/hybrid shells (Capacitor, React Native, Flutter).** Out of scope by `LEGACY-BIZ-006` and `PRODUCT_VISION_AND_SCOPE.md`; the PWA keeps native packaging an option.
- **Hosting providers compared for D5(15):** Fly.io (regions near both user geographies, managed Postgres is third-party), Render and Railway (simple managed Postgres with PITR on paid tiers), Hetzner + Coolify (lowest cost, self-managed backups), AWS (ECS/RDS, most control, most operational overhead). No selection is made; constraints (a)–(d) are binding on the selection.

## Consequences

### Positive

- One language and one shared schema package make the "one core graph, many views" principle enforceable by the compiler and by dependency rules.
- PostgreSQL unique constraints, transactions and RLS give ADR-002 and ADR-003 cheap, auditable enforcement points.
- The verification repository can drive the app with its existing Node/Playwright toolchain and the container image gives every candidate an identical runtime for fingerprinting.
- Provider independence: the container plus managed PostgreSQL model is portable, and backups are exportable.

### Negative

- The owner must operate PostgreSQL migrations and a container pipeline from day one; a BaaS would have been faster to the first demo.
- Deferring provider selection means the first hosted environment needs an ADR addendum and a restore drill before any real personal data is stored.
- React/Vite/Fastify/Drizzle each move quickly; versions must be pinned and upgraded deliberately, and the `LEGACY-NFR-020` test gate is the only protection against regressions from upgrades.
- Integer-minor-unit money and explicit time zones add schema ceremony to every module, including non-financial ones.

## Control provenance

Prepared by the Systems Engineering control-plane agent (Claude Fable 5.1, Claude Code) for LEGACY-WORK-002 as a reviewable proposal. No product repository was modified. Sources: `docs/business/*` v0.1.0, `docs/reference/LEGACY_GAMIFICATION_UX_ARCHITECTURE_BASELINE_v0.1.md` sections 1, 5–9, 12–15, `legacy_app/docs/IMPLEMENTATION_BOUNDARIES.md`, `legacy_verification_tooling/package.json` and harness (read-only). Acceptance requires a human Systems Engineering decision recorded in this file's Status section and in `traceability/manifest.json` `artifacts[]`.
