---
artifact_id: LEGACY-DECISIONS-001
project: LEGAVIA
title: Legavia Open Architecture and Product Decision Register
version: 0.2
status: candidate-for-SE-review
date: 2026-10-29
control_repository: matheusns/legacy
---

# Legavia Open Architecture and Product Decision Register

> This artifact is a candidate systems-engineering baseline. Existing stable identifiers are preserved. Review and approve before treating any proposal as an accepted specification or an executable FVT.

No ADR in this register is approved. All implementation-affecting choices require reviewed ADR evidence before relevant WPs begin.

| Proposed ADR | Decision needed | Mandatory evidence / tradeoffs | Blocks |
|---|---|---|---|
| ADR-LEGAVIA-001 | Web/PWA/native strategy and application stack | Cross-device, hosting cost, iOS capabilities, maintainability, release path | WORK-003 |
| ADR-LEGAVIA-002 | Backend persistence and tenant-scoped authorization | DB isolation, RLS/policy checks, migrations, backup/restore, media access | WORK-003 |
| ADR-LEGAVIA-003 | Event, XP and undo ledger semantics | Idempotency and transaction envelope, conflict handling, outbox/replay | WORK-005 |
| ADR-LEGAVIA-004 | UX design system and image asset rights/ownership | User reference source, artwork rights, mobile/desktop states, performance | WORK-002 / WORK-006 |
| ADR-LEGAVIA-005 | Connector security and consent model | OAuth/token storage, scope, revocation, provenance, provider TOS and limits | WORK-013 / WORK-017 |
| ADR-LEGAVIA-006 | AI processing, provenance and feature-approval boundaries | Consent, external data sharing, prompt injection, audit and rollbacks | WORK-016 |
| ADR-LEGAVIA-007 | Finance currency and projection semantics | FX precision/time, cost categories, transfers, estimated asset values | WORK-013 |
| ADR-LEGAVIA-008 | Observability, test adapters and release gates | GitHub PR integration, preview artifact retention, device captures | WORK-010 / WORK-011 |
| ADR-LEGAVIA-009 | Offline writes, time semantics and sync | Conflict resolution, IANA timezone, retries and explicit offline limit | WORK-003 / WORK-005 |
| ADR-LEGAVIA-010 | Family sharing, content retention and deletion | Legal/compliance, default private, deletion/retention exceptions, quotas | WORK-017 |

## Decisions that must not be inferred

No automatic real bank transfers; no unrestricted private connector access; no guaranteed external IMDb provider; no irreversible penalties for negative habits; no autonomous release of AI-generated features; no promise of pixel-perfect reference reproduction without reviewing actual assets and app captures.

## Required ADR record fields

ID, title, owner, status, date, context, considered options, decision, consequences, affected requirements/functions/use cases/WPs, privacy/security assessment, test impacts and reviewer disposition. Unknown constraints remain `Open` and block dependent WPs rather than being guessed.
