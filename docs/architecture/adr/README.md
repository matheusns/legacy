# Architecture Decision Register

This directory holds Legavia architecture decision records in the format the local SDLC workbench discovers (`ADR-NNN-<slug>.md`, a `## Status` section, a `## Traceability` block naming `LEGACY-*` IDs). The workbench treats an ADR as accepted **only** when its Status section begins with `Accepted` **and** the control manifest registers it under `artifacts[]` with an accepted status. Every record here is currently **Proposed**; nothing in this directory is approved until a human Systems Engineering reviewer changes the Status section, records the disposition in `docs/reviews/`, and the manifest is updated by a human-controlled commit.

## Identifier mapping

The business baseline issued the candidate register IDs `ADR-CAND-001..007` (DELIVERY_ROADMAP, `business_baseline.json.required_decisions`, LEGACY-SE-REVIEW-001 section 7). The workbench canonicalises ADR identifiers as `ADR-<digits>`, so the materialised records use `ADR-001..007` and each record cites the `ADR-CAND-*` item and the `DEC-*` decision it resolves. The candidate IDs are preserved as references and are not renumbered.

| ADR | Title | Resolves | Decisions | LEGACY-WORK-002 topic | Status |
| --- | --- | --- | --- | --- | --- |
| [ADR-001](ADR-001-application-stack-hosting-persistence.md) | Application stack, hosting model and persistence | ADR-CAND-001 | DEC-001, DEC-009 (method) | app stack, hosting | Proposed |
| [ADR-002](ADR-002-identity-tenancy-authorization.md) | Identity, workspace tenancy, resource-level authorization and threat model | ADR-CAND-002 | DEC-002 | identity/tenancy | Proposed |
| [ADR-003](ADR-003-source-of-truth-events-idempotency-rewards.md) | Source of truth, immutable domain events, idempotency, projections, undo and rewards | ADR-CAND-003 | DEC-003 | source of truth, event idempotency | Proposed |
| [ADR-004](ADR-004-visual-assets-design-system-golden-baseline.md) | Pixel-art asset provenance and versioning, design system, golden baseline and comparison method | ADR-CAND-004 | DEC-004, DEC-008 | assets | Proposed |
| [ADR-005](ADR-005-testability-verification-adapters-fingerprints.md) | Testability: adapters, fixtures, candidate fingerprints, verification vocabulary, GitHub checks | ADR-CAND-005 | DEC-005, DEC-011, DEC-009 (method) | testability | Proposed |
| [ADR-006](ADR-006-connectivity-drafts-conflicts-backup-deletion.md) | Intermittent connectivity, drafts/retry, conflicts, backup, restore, retention, deletion | ADR-CAND-006 | DEC-006 | (supporting: NFR-004/016/017) | Proposed |
| [ADR-007](ADR-007-ai-consent-provider-scopes-approval-speech-privacy.md) | AI boundary: consent, provider scopes, staged proposals, approval, speech privacy | ADR-CAND-007 | DEC-007 | (supporting: NFR-019) | Proposed |

Companion definition: [`../SECURE_DOMAIN_SKELETON.md`](../SECURE_DOMAIN_SKELETON.md) (LEGACY-ARCH-SKELETON-001) describes the `legacy_app` skeleton that implements these decisions in `LEGACY-WORK-003`.

## Decisions from LEGACY-SE-REVIEW-001 not resolved here

| Decision | Disposition in this work package |
| --- | --- |
| DEC-010 reference image approval | Human owner + UX reviewer action; ADR-004 D3 defines the procedure only |
| DEC-012 validator/manifest semantics for `Approved` | Control-only change; must accompany the first status promotion |
| DEC-013 finance computation contracts | Deferred to a `LEGACY-WORK-010` predecessor; outside CAP-001/003/004 scope of this package (shared `Money` type is fixed in ADR-001) |
| DEC-014 namespace migration | Explicitly deferred by owner |
| DEC-015 installed-PWA adapter | `LEGACY-WORK-009` |
| DEC-016 work-package allocation for CAP-007/010/011/012/014 | Roadmap revision |
| DEC-017 provenance pinning | Control-only change |

## Lifecycle

1. **Proposed**: authored as a reviewable candidate (this state).
2. **Accepted**: human Systems Engineering decision; Status section rewritten to `Accepted — <date>`, manifest `artifacts[]` entry added with `type: design`, `status: Accepted`, `requirement_ids`, `functionality_ids`, and `work_packages[LEGACY-WORK-002].adr_ids` populated.
3. **Superseded / Deprecated**: a new ADR references the old one; historical records are never rewritten.

Do not infer acceptance from the presence of a file. Do not edit an accepted ADR's decision text; add a revision or a superseding record.
