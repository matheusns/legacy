# ADR-005 — Testability: test adapters, deterministic fixtures, candidate fingerprints, verification vocabulary and GitHub check integration

## Status

Proposed — 2026-10-30. Awaiting explicit Systems Engineering acceptance; this record is not accepted and grants nothing until a human reviewer changes this section and the control manifest records the artifact.

Resolves candidate register item `ADR-CAND-005` and decisions `DEC-005` and `DEC-011` of LEGACY-SE-REVIEW-001; fixes the measurement method for `DEC-009` with ADR-001. Provides the decision basis for findings SE-F-002 and SE-F-003 of that review. It does not register any product command in the manifest; that is a control change after acceptance.

## Traceability

- Functionalities: `LEGACY-CAP-001`, `LEGACY-CAP-003`, `LEGACY-CAP-004`, `LEGACY-CAP-005`
- Requirements: `LEGACY-BIZ-010`, `LEGACY-NFR-013`, `LEGACY-NFR-014`, `LEGACY-NFR-015`, `LEGACY-NFR-018`, `LEGACY-NFR-020`, `LEGACY-UX-020`, `LEGACY-FNC-009`, `LEGACY-FNC-069`
- Work packages: `LEGACY-WORK-002` (acceptance topic: testability); consumers `LEGACY-WORK-003`, `LEGACY-WORK-009`, `LEGACY-WORK-013`
- Decision owner: Systems Engineering
- Prepared in run `DEV-20261030T185520Z-751CB5` against control commit `caca50c7e23a892d37e63cc14091f8cf725374d6`

## Context

`LEGACY-NFR-020` requires automated build, unit, integration, authorization and representative mobile/desktop visual tests with candidate fingerprints. `LEGACY-NFR-013` requires authorization tests for every API and storage lookup. `WORKFLOW.md` requires each registered suite to emit a schema-version-1 report from real checks, invalidates evidence when source, suite, profile, fixture or reference changes, and distinguishes `emulated_browser` evidence from installed-PWA or real-device evidence. `VERIFICATION_AND_ACCEPTANCE.md` lists seven release gates and the planned FVT-LEGACY-001..024, all `Planned - not executable`. The independent harness already emits `{schema_version: 1, tests: [{name, status, message}], metrics, observation}` and refuses non-browser device kinds. The GUI consumes `verification_execution.suites[]` commands, `result_file` and `required_paths`.

LEGACY-SE-REVIEW-001 found that 74 of 129 requirements have no verification record (SE-F-002), that 37 distinct verification-method strings are in use (SE-F-003), and that performance budgets must be measured (`DEC-009`). Verification allocation is architecture-adjacent and was assigned to this work package.

## Decision

### D1. Test levels and ownership

| Level | Where | Tooling | Owner | Gate |
| --- | --- | --- | --- | --- |
| Domain unit | `legacy_app/packages/domain` | Vitest; pure functions, reducers, reward policy, continuity algorithm; property tests for idempotency and rebuild equality | Development | App CI, per PR |
| Component | `legacy_app/apps/web` | Vitest + Testing Library + jsdom; state panels, accessibility roles, display-mode switch | Development / UX implementer | App CI, per PR |
| API integration | `legacy_app/apps/api` | Vitest against an ephemeral PostgreSQL (docker compose or testcontainers) with migrations applied; real RLS role | Development | App CI, per PR |
| Authorization matrix | `legacy_app/apps/api` | Generated from the route registry (ADR-001 D3, ADR-002 D3): for every route, positive case plus negative cases (other workspace, revoked grant, nested foreign ID, reassignment attempt, unauthenticated) | Development; coverage rule owned by SE | App CI; failing or missing case blocks merge |
| Projection rebuild | `legacy_app` | Replay ledger fixtures, assert equality with incremental state (ADR-003 D5) | Development | App CI |
| Independent browser journeys (FVT) | `legacy_verification_tooling/scenarios` | Playwright against a running candidate at a registered URL; phone and desktop profiles | Verification implementer (WORK-009) | Registered suite; SE disposition |
| Visual consistency | `legacy_verification_tooling/harness/capture.cjs` | ADR-004 method and bands | Verification implementer; human fidelity review | Registered capture |
| Accessibility | verification scenarios | axe-core per screen/state plus manual keyboard and screen-reader checklist | Verification + UX reviewer | Gate 5 |
| Security | API integration + scheduled dependency audit | Session/CSRF/rate-limit tests; `npm audit`/OSV in CI | Development; review by SE | Gate 3 |
| Performance | Lighthouse CI on preview; Web Vitals field beacon | ADR-001 D6 | Verification | Measured budgets (`DEC-009`) |

Unit and component tests live beside production code (per `legacy_app/AGENTS.md`); everything that claims a product FVT outcome runs from `legacy_verification_tooling` against a pinned candidate.

### D2. Deterministic fixtures

1. The application exposes a **fixture command** (`pnpm fixture:load --scenario <id>`) and a **test-only HTTP endpoint** enabled solely when `LEGAVIA_FIXTURE_MODE=1`, which: resets an isolated database and storage prefix, seeds a named scenario with **stable UUIDs**, sets the **server clock** through an injectable `Clock` port (the browser clock is frozen by the harness), and returns the scenario manifest (`fixture_id`, `fixture_hash`, seeded principal credentials). Fixture mode refuses to start against a non-local database URL.
2. Scenarios are **synthetic**: no personal data, no imported workbook rows, no real media (`LEGACY-NFR-015`). Scenario definitions are versioned in `legacy_app/packages/testkit/scenarios/*.json`; the verification repository references them by `fixture_id` and verifies `fixture_hash`.
3. The first-journey scenario `S2-first-journey` contains one workspace, one goal → phase → milestone → linked daily task, one habit, one second workspace with a non-member, and one revoked grant, so FVT-LEGACY-001/002/004/005 share a base.

### D3. Candidate fingerprint

4. A **candidate** is identified by the SHA-256 of the canonical JSON `{ app_repo: "matheusns/legacy_app", app_commit, app_tree_hash, build_id (hash of built artefacts), schema_version (last applied migration), fixture_id, fixture_hash, verification_commit, harness_version, browser, browser_version, target_profile_id, artwork_version, reference_revision? }`. The API exposes `GET /api/v1/meta/candidate` (unauthenticated, metadata only) returning `app_commit`, `build_id`, `schema_version`, `artwork_version`, so the harness records what actually ran rather than what was requested.
5. Every report embeds the fingerprint inputs under `observation`; evidence whose inputs differ from the current candidate is **stale** (matches `WORKFLOW.md`). Evidence with a mismatched `app_commit` between request and `/meta/candidate` is an **execution error**, never a product result.

### D4. Report contract

6. Suites emit `result.json` with `schema_version: 1`, `tests[] {name, status ∈ passed|failed|error|inconclusive|skipped, message, requirement_ids[], fvt_id?}`, `metrics {}`, `observation {evidence_kind, ...fingerprint inputs}`. `error` means the harness or environment failed; `failed` means the product did not meet the assertion; `inconclusive` is reserved for human-disposition bands (ADR-004 Review band, manual checks). Missing, empty or invalid reports cannot pass (`WORKFLOW.md`).
7. Device kind `emulated_browser` is the only kind the current adapters may claim; `installed_pwa` and real-device observations need their own registered adapters (`DEC-015` stays with WORK-009).

### D5. Closed verification-method vocabulary (`DEC-011`, SE-F-003)

8. The requirement catalog adopts the vocabulary **Test | Demonstration | Inspection | Analysis | Independent audit**, with a mandatory `verification_record` qualifier naming the FVT ID, review record ID or audit ID that discharges the requirement. The 37 current strings map as follows (statements and IDs unchanged):

| Current string(s) | Method | Typical record |
| --- | --- | --- |
| FVT, Visual FVT, Navigation FVT, Integration FVT, Functional test, Integration test, Algorithm test, Analytics test, Search FVT, Widget FVT, Notification test, Export test, Learning FVT, Finance FVT, Workflow FVT, Permission + FVT, Offline/sync FVT, Security test, Security/FVT, Audit test, State coverage test, Accessibility FVT, Independent functional verification, Independent quality and security verification (testable NFRs) | Test | FVT-LEGACY-nnn or authorization-matrix suite |
| Performance UX test | Test (measured) | Performance report (ADR-001 D6) |
| Visual inspection, Design inspection, Usability inspection, Visual inspection and interaction test, UI audit, Inspection (finance P0 rows that are testable: FNC-032, NFR-010, NFR-011 → Test) | Inspection or Test | UX review record / FVT |
| Architecture review, Architecture test | Analysis | SE review record referencing ADRs |
| Security review, Privacy review | Independent audit | Security/privacy review record (gates 3, 6) |
| Accessibility audit | Independent audit + Test | axe report + manual checklist record |
| Product inspection + telemetry | Demonstration + Analysis | Demo record + telemetry analysis |

9. Applying this mapping to `REQUIREMENTS.md` and `manifest.json` is a **control change after acceptance**, preserving every ID and statement (SE-F-003 proposed resolution).

### D6. Verification allocation for BIZ, UX and NFR requirements (`DEC-011`, SE-F-002)

10. Every P0 requirement receives at least one verification owner record. Proposed allocation (to be materialised as `Planned` non-FVT verification definitions or FVT trace extensions in `business_baseline.json` after acceptance):

| Verification record (new unless an FVT) | Requirements discharged |
| --- | --- |
| FVT-LEGACY-005 extended + `AUTHZ-MATRIX` suite (D1) | `LEGACY-BIZ-003`, `LEGACY-BIZ-008`, `LEGACY-NFR-002`, `LEGACY-NFR-009`, `LEGACY-NFR-013` |
| FVT-LEGACY-001/015/019/023 extended | `LEGACY-NFR-005`, `LEGACY-NFR-010`, `LEGACY-NFR-014`, `LEGACY-NFR-022` (local-date case) |
| `A11Y-AUDIT-001` (axe + manual) and FVT-LEGACY-008 restored links | `LEGACY-NFR-001`, `LEGACY-UX-006`, `LEGACY-UX-008`, `LEGACY-UX-009` |
| FVT-LEGACY-004/020 extended + `UX-REVIEW-SHELL` inspection record | `LEGACY-UX-001`, `LEGACY-UX-002`, `LEGACY-UX-003`, `LEGACY-UX-004`, `LEGACY-UX-005`, `LEGACY-UX-010`, `LEGACY-UX-012`, `LEGACY-UX-018`, `LEGACY-FNC-060` |
| `VISUAL-BASELINE-REVIEW` (ADR-004 D3/D4) | `LEGACY-UX-017`, `LEGACY-UX-019`, `LEGACY-UX-020` |
| `SEC-REVIEW-001` (independent audit, gate 3) | `LEGACY-NFR-003`, session/CSRF controls of ADR-002 |
| `PRIVACY-REVIEW-001` (independent audit, gate 6) | `LEGACY-NFR-008`, `LEGACY-NFR-012`, `LEGACY-NFR-015`, `LEGACY-NFR-019` |
| `RESTORE-DRILL-001` (demonstration, ADR-006) | `LEGACY-NFR-017` |
| `PERF-BUDGET-001` (measured, ADR-001 D6) | `LEGACY-NFR-007`, `LEGACY-NFR-018` |
| `ARCH-REVIEW-002` (analysis = this ADR set reviewed) | `LEGACY-BIZ-001`, `LEGACY-BIZ-004`, `LEGACY-BIZ-006` |
| `RELEASE-GATE-REVIEW` (analysis per release) | `LEGACY-BIZ-010`, `LEGACY-NFR-020` |
| FVT-LEGACY-023 extended with a UC-LEGACY-035 draft/retry step (ADR-006 D1) | `LEGACY-NFR-016` |
| FVT-LEGACY-006/022 | `LEGACY-BIZ-005`, `LEGACY-BIZ-009`, `LEGACY-NFR-006` |

P1/P2 BIZ/UX/NFR requirements not listed (e.g. `LEGACY-NFR-004`, `LEGACY-NFR-021`, `LEGACY-UX-011`, `LEGACY-UX-021`, `LEGACY-UX-022`, `LEGACY-UX-023`, finance UX-013..016) are allocated when their owning work package is planned; the dashboard shows them as pending, not unverifiable.

### D7. GitHub checks and GUI integration (`DEC-005`)

11. `legacy_app` CI (GitHub Actions) runs build, unit, component, API integration, authorization matrix, rebuild and dependency audit on every PR and publishes the candidate metadata as a check summary. `legacy_verification_tooling` CI runs harness self-tests only (as today).
12. The GUI reads PR and check state through `gh` (already the registered mechanism in `WORKFLOW.md`); a green app CI is a **precondition** for running registered product suites, never a product acceptance. Registered suite commands for the product (`build`, `fixture:load`, `start`, FVT scenarios, capture) are added to `verification_execution.suites[]` by a control change under `LEGACY-WORK-013`/`LEGACY-WORK-009` once the commands exist.
13. Acceptance of an FVT result remains a human Systems Engineering disposition in the GUI with the fingerprint recorded; passing checks alone promote nothing (`LEGACY-BIZ-010`).

## Considered alternatives

- **Rely on in-repo Playwright tests inside `legacy_app` as acceptance evidence.** Rejected: independence of verification is a baseline principle; app-local browser tests are allowed as developer tests but cannot claim FVT outcomes.
- **Mock the database in API tests.** Rejected: RLS, unique constraints and transactions are the enforcement points; mocking them tests nothing relevant.
- **Hand-written authorization tests per endpoint.** Rejected: coverage decays; generating the matrix from the route registry makes a missing negative case a build failure.
- **Fingerprint by commit SHA only.** Rejected: fixtures, browser version, artwork and harness changes all invalidate evidence per `WORKFLOW.md`.
- **Keep free-text verification methods.** Rejected: the dashboard cannot reason about 37 strings; a closed vocabulary with a record qualifier is standard practice.

## Consequences

### Positive

- Every acceptance claim is traceable to a fingerprinted candidate and a registered command; stale evidence is detectable mechanically.
- Authorization coverage is enforced structurally; `LEGACY-NFR-013` becomes checkable.
- All P0 requirements gain a verification owner, resolving SE-F-002 at the decision level.

### Negative

- Test-only fixture endpoints and clock injection add code paths that must be provably disabled in production (guarded by environment and startup check).
- Ephemeral PostgreSQL in CI lengthens PR feedback; acceptable for correctness-critical gates.
- Applying the vocabulary and allocations touches 129 catalog rows and both JSON records; it must be done as one reviewed control change with the validator extended.

## Control provenance

Prepared by the Systems Engineering control-plane agent (Claude Fable 5.1, Claude Code) for LEGACY-WORK-002 as a reviewable proposal. Inputs: `VERIFICATION_AND_ACCEPTANCE.md`, `WORKFLOW.md`, `LEGACY-SE-REVIEW-001` sections 4 and 7, `legacy_verification_tooling` README, AGENTS.md, harness and CI workflow (read-only), GUI `docs/TRACEABILITY_MODEL.md` (read-only). Acceptance requires a human Systems Engineering decision.
