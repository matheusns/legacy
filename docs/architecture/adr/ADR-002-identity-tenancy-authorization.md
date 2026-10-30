# ADR-002 — Identity, workspace tenancy, resource-level authorization and threat model

## Status

Proposed — 2026-10-30. Awaiting explicit Systems Engineering acceptance; this record is not accepted and grants nothing until a human reviewer changes this section and the control manifest records the artifact.

Resolves candidate register item `ADR-CAND-002` and decision `DEC-002` of LEGACY-SE-REVIEW-001. Governs the design of FVT-LEGACY-005, FVT-LEGACY-021 and FVT-LEGACY-024.

## Traceability

- Functionalities: `LEGACY-CAP-001`, `LEGACY-CAP-014`
- Requirements: `LEGACY-BIZ-003`, `LEGACY-BIZ-008`, `LEGACY-FNC-001`, `LEGACY-FNC-024`, `LEGACY-FNC-056`, `LEGACY-FNC-057`, `LEGACY-FNC-058`, `LEGACY-FNC-059`, `LEGACY-FNC-061`, `LEGACY-NFR-002`, `LEGACY-NFR-003`, `LEGACY-NFR-009`, `LEGACY-NFR-013`, `LEGACY-NFR-019`
- Use cases: UC-LEGACY-001, UC-LEGACY-009, UC-LEGACY-030, UC-LEGACY-032
- Work package: `LEGACY-WORK-002` (acceptance topic: identity/tenancy)
- Decision owner: Systems Engineering
- Prepared in run `DEV-20261030T185520Z-751CB5` against control commit `caca50c7e23a892d37e63cc14091f8cf725374d6`

## Context

The baseline makes isolation the first P0 concern: each user has a private workspace with explicit sharing (`LEGACY-BIZ-003`); access to another person's data is granted at resource level and never arises from friendship, household membership or an invitation (`LEGACY-BIZ-008`); authorization is enforced server-side on every data path (`LEGACY-NFR-002`) and tested for every API and storage lookup including nested objects and workspace reassignment (`LEGACY-NFR-013`); administrators manage quotas, flags and approvals without content access by default (`LEGACY-FNC-059`, Vision "Workspace administrator"). `DOMAIN_MODEL.md` names the aggregate: User, Workspace, Membership, Role, ResourceGrant, AuditEvent, FeatureFlag, StorageUsage, with the invariant "owner/workspace mandatory; grant is resource-specific; admin metadata access ≠ content access". CONOPS defines the operating modes Unauthenticated, Personal, Collaborative and Review/beta, and states that the display-mode override never affects authorization.

The reference baseline skill SK-SEC-01 asks for a threat model and access matrix as the security gate output. No identity provider, session model or enforcement mechanism has been decided, and `LEGACY-WORK-003` cannot build a "secured CRUD API" without one.

## Decision

### D1. Identity

1. **Authentication is first-party** in S1: email + password with Argon2id hashing, server-side sessions stored in PostgreSQL, delivered as `Secure; HttpOnly; SameSite=Lax` cookies with rotation on privilege change and absolute plus idle expiry. State-changing requests additionally require an `Origin`/`Fetch-Metadata` check; no bearer tokens are stored in browser storage.
2. Email verification is required before a workspace can invite or be invited. Passkeys (WebAuthn) and OIDC federation (e.g. Google, Apple) are planned **extension points** behind the same session model, not S1 scope. No third-party identity vendor is adopted for the system of record.
3. Every authenticated request resolves an immutable **`AuthContext { principal_id, session_id, active_workspace_id, memberships, grants_digest }`** once, at the edge of `apps/api`; domain and persistence code receive it as an argument and never read identity from globals.

### D2. Tenancy model

4. **Workspace is the tenancy unit.** Every user owns exactly one **personal workspace** created at sign-up; additional **shared workspaces** (household, family, team) are created explicitly (`LEGACY-FNC-061`). Every domain row carries a non-null `workspace_id`; there are no cross-workspace rows.
5. **Roles are per workspace membership**, closed set `owner | admin | member`:
   - `owner`: full control including deletion, transfer and billing; exactly one per workspace, transferable.
   - `admin`: membership, invitations, quotas, feature flags, retention and audit **metadata**; no read access to member content unless a grant exists (`LEGACY-FNC-059`).
   - `member`: full access to content they author in that workspace; access to others' content only via grants.
   A platform-level `operator` role exists for the product owner's maintenance tasks, is not a workspace role, and has no content read path in the application; database-level access for support is logged out of band.
6. **Sharing is a `ResourceGrant`**: `{ grant_id, workspace_id, resource_type, resource_id, grantee_principal_id, capability ∈ {view, contribute, manage}, granted_by, granted_at, revoked_at, expires_at }`. Grants are explicit, resource-specific and revocable; revocation takes effect on the next request and invalidates cached shared context (OPS-06). Friendship, household membership and pending invitations create **no** grant (`LEGACY-BIZ-008`, `LEGACY-FNC-024`, `LEGACY-FNC-057`). Visibility levels `private | selected | friends | party | public` are expressed as grant templates that expand to explicit grants; `private` is the default.
7. **Administrators and content.** Admin-facing views query only aggregate and metadata projections (`StorageUsage`, counts, flags, audit events). Any admin content access must itself be a grant, visible to the content owner.

### D3. Enforcement, defense in depth

8. **Layer 1 — route registry policy (mandatory).** Each route in the ADR-001 route registry declares a policy from a closed catalogue (`workspace_member`, `resource_capability(view|contribute|manage)`, `workspace_admin`, `workspace_owner`, `self_only`, `public`). A route without a policy fails startup. Deny is the default.
9. **Layer 2 — repository scoping (mandatory).** Persistence functions take the `AuthContext` and append `workspace_id = $active_workspace_id` to every query; a query builder without workspace scope is a lint error. Nested lookups resolve the parent aggregate first and inherit its workspace, so a child ID from another workspace cannot be reached (`LEGACY-NFR-013` nested object access).
10. **Layer 3 — PostgreSQL Row-Level Security (mandatory for all workspace-scoped tables).** Each request runs in a transaction that sets `SET LOCAL app.principal_id` and `SET LOCAL app.workspace_id`; RLS policies restrict rows to the active workspace, plus rows reachable through an active grant. The application connects with a role that cannot bypass RLS; migrations use a separate role. This makes a missed Layer 1/2 check fail closed rather than leak.
11. **Workspace reassignment is forbidden** at the schema level: `workspace_id` columns are immutable after insert (trigger), and "move" is modelled as export + re-import with new identities and provenance.
12. **Audit.** Sign-in, session events, membership changes, grant/revoke, admin actions, export and deletion requests append `AuditEvent` rows that are visible to the affected user and the workspace admin; audit rows are never deleted by application code.
13. **Transport and storage security** (`LEGACY-NFR-003`, `LEGACY-NFR-009`): TLS only (HSTS), platform-managed encryption at rest for database and object storage, secrets via platform injection, no credentials in repositories or fixtures. AI and integration adapters hold **no database credentials**; they call the same API under a delegated, scope-limited principal (`LEGACY-NFR-019`, detailed in ADR-007).

### D4. Threat model (STRIDE-lite, binding for FVT design)

| Threat | Example | Primary control | Verification |
| --- | --- | --- | --- |
| Horizontal access (IDOR) | Request another workspace's goal or milestone by ID, including nested `/goals/{a}/milestones/{b}` | Layers 1–3; parent-first resolution | FVT-LEGACY-005 negative cases for every registered route (ADR-005 matrix) |
| Implicit sharing | Friend or household member reads a private goal | Grants only; visibility templates expand to grants | FVT-LEGACY-021 |
| Grant escalation / stale cache | Revoked collaborator still sees shared goal | Grant check per request; cache keyed by grants digest | FVT-LEGACY-021 revocation step |
| Workspace reassignment | Patch `workspace_id` to move an object into a readable workspace | Immutable column trigger; schema validation rejects field | FVT-LEGACY-005 / NFR-013 test |
| Admin overreach | Admin lists members' memories or transactions | Metadata-only admin projections; content requires grant | FVT-LEGACY-024 |
| Session theft / CSRF | Stolen cookie, cross-site POST | HttpOnly/Secure/SameSite cookies; Origin check; rotation | Security test suite (ADR-005) |
| Credential stuffing | Password guessing | Argon2id; per-account and per-IP rate limits; lockout with notification | Security test suite |
| Privileged automation | AI/integration adapter writes directly to DB | No DB credentials for adapters; delegated principal; staged proposals | FVT-LEGACY-006 / FVT-LEGACY-022 |
| Data in artefacts | Restricted data in logs, fixtures, screenshots | Redaction list from schema annotation; synthetic fixtures only | Privacy review gate 6 |

Threats outside S1–S3 scope (public sharing links, federated identity, multi-region residency) are recorded as open items in the register, not silently accepted.

## Considered alternatives

- **Hosted identity provider (Auth0, Clerk, Supabase Auth, Cognito).** Rejected for S1: adds vendor coupling and cost before any user exists, moves session semantics outside the tested code, and complicates residency. Kept as an OIDC extension point.
- **JWT access tokens in browser storage.** Rejected: XSS exposure and revocation difficulty; server-side sessions give immediate revocation needed for grant and membership changes.
- **User-level tenancy (no workspace entity) with sharing by ACL on each row.** Rejected: shared household workspaces (`LEGACY-FNC-061`) and admin/quota roles need a container; a per-row ACL alone does not express "admin without content".
- **Workspace membership implies read access to all workspace content.** Rejected: contradicts `LEGACY-BIZ-008`; household members must not see each other's finance or memories by default.
- **Application-layer checks only, no RLS.** Rejected: a single missed check would be a silent leak; RLS is the fail-closed backstop at modest migration cost.
- **Database-per-tenant.** Rejected: shared workspaces and resource grants cross tenant lines; operational cost scales with users.

## Consequences

### Positive

- Isolation is enforced three times and testable at each layer; the route registry gives FVT-LEGACY-005 an enumerable negative-test surface.
- The grant model satisfies family collaboration without any implicit access, and makes revocation immediate.
- Admin duties are possible without content exposure, satisfying quota and beta administration requirements.

### Negative

- RLS plus `SET LOCAL` requires discipline in connection pooling (transaction-scoped settings) and in tests.
- First-party authentication means the project owns password reset, rate limiting and account recovery flows.
- Grant expansion for `friends`/`party` templates must be recomputed when relationships change; that is a deliberate cost of refusing implicit access.

## Control provenance

Prepared by the Systems Engineering control-plane agent (Claude Fable 5.1, Claude Code) for LEGACY-WORK-002 as a reviewable proposal. Inputs: `DOMAIN_MODEL.md`, `CONOPS.md` sections 2–3 and OPS-06, `USE_CASES.md` UC-LEGACY-009/030/032, `VERIFICATION_AND_ACCEPTANCE.md` FVT-005/021/024, reference baseline SK-SEC-01 and invariant 8. Acceptance requires a human Systems Engineering decision.
