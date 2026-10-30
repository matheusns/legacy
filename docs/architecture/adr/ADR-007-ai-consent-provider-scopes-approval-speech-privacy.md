# ADR-007 — AI boundary: consent, provider scopes, staged proposals, approval workflow and speech-input privacy

## Status

Proposed — 2026-10-30. Awaiting explicit Systems Engineering acceptance; this record is not accepted and grants nothing until a human reviewer changes this section and the control manifest records the artifact.

Resolves candidate register item `ADR-CAND-007` and decision `DEC-007` of LEGACY-SE-REVIEW-001. Scope note: fixes the boundary the S1 skeleton must reserve and the S5 policy; selects no AI vendor or model.

## Traceability

- Functionalities: `LEGACY-CAP-013`, `LEGACY-CAP-015`, `LEGACY-CAP-001`
- Requirements: `LEGACY-BIZ-005`, `LEGACY-BIZ-009`, `LEGACY-FNC-025`, `LEGACY-FNC-026`, `LEGACY-FNC-049`, `LEGACY-FNC-054`, `LEGACY-FNC-055`, `LEGACY-FNC-058`, `LEGACY-FNC-066`, `LEGACY-FNC-067`, `LEGACY-NFR-006`, `LEGACY-NFR-008`, `LEGACY-NFR-019`, `LEGACY-UX-022`
- Use cases: UC-LEGACY-010, UC-LEGACY-024, UC-LEGACY-028, UC-LEGACY-029
- Work package: `LEGACY-WORK-002`; consumers: future AI/integration work packages (CAP-013/015 are unallocated per SE-F-008)
- Decision owner: Systems Engineering
- Prepared in run `DEV-20261030T185520Z-751CB5` against control commit `caca50c7e23a892d37e63cc14091f8cf725374d6`

## Context

AI-generated feature proposals require explicit authorised approval before becoming baseline items (`LEGACY-BIZ-005`), with auditable history (`LEGACY-NFR-006`). AI providers receive only authorised minimum content and hold no privileged write credentials (`LEGACY-NFR-019`). Text or voice commands create reviewable proposals; nothing persists until confirmed (`LEGACY-FNC-054`, `LEGACY-FNC-055`). Permission requests are contextual, revocable, with manual fallback (`LEGACY-UX-022`, `LEGACY-BIZ-009`). CONOPS OPS-04 and OPS-08 describe the capture and product-evolution flows; `EXTERNAL_INTERFACES.md` row "Speech & AI" states consent, data minimisation, preview, human approval and "model has no DB write credentials"; `DOMAIN_MODEL.md` lists ExternalConnection, ConsentGrant, ImportJob, Proposal, ApprovalDecision, ProviderReference with the invariant "no provider auto-commits". The reference baseline risk RISK-08 (AI scope creep) and invariant 10 apply. Raw voice recordings are classified Restricted.

## Decision

### D1. Architectural boundary

1. All AI and speech functionality lives in one **`ai-boundary` module** (`packages/ai-boundary` plus `apps/api` routes) with a **provider port** `{ transcribe(audio, consent) , propose(structured_input, consent) }` and vendor adapters behind it. The module has **no database connection**: it receives explicitly selected input from an application use case and returns a `Proposal` value; the application use case stores the proposal through the ordinary command path under the **user's own principal** with `origin = ai_proposal` (ADR-003 D3), so ADR-002 authorization applies unchanged (`LEGACY-NFR-019`).
2. Provider credentials are server-side secrets scoped to the boundary module and rotated by the operator; they never reach the client. Vendor and model identifiers are **configuration** (`ProviderReference { provider, model, version, region, terms_ref }`), recorded on every proposal for provenance; no vendor or model is selected by this ADR.
3. Every AI-assisted feature has a **manual alternative** of equal capability (typed task entry, manual course structure, manual feature request form); the AI path is an accelerator, never the only path (`LEGACY-BIZ-009`, `LEGACY-UX-022`).

### D2. Consent and data minimisation

4. **Consent is a `ConsentGrant`** per `(principal, feature_scope, provider)` with `granted_at`, `revoked_at`, `data_classes_allowed[]`, `retention_choice`; it is requested in context at first use with a plain-language description of what is sent, to whom and for how long, and is revocable from Me → Privacy. No consent, no provider call.
5. **Minimum necessary content**: the application use case constructs the provider payload from an allow-list per feature (e.g. the dictated text and the user's goal titles for task capture; a single linked document for course extraction). Finance ledgers, health records, memories and other workspaces' content are never included unless the feature's allow-list names them and the consent covers that data class. Payloads are logged as **hashes plus field names**, not content.
6. Provider contracts must guarantee **no training on customer data** and bounded retention; the `terms_ref` is recorded. Providers that cannot meet this are not configurable.

### D3. Staged proposals and approval workflow

7. A `Proposal { proposal_id, kind ∈ task|goal|habit|journal|course_structure|feature_request|issue_import, source_input_ref, provider_ref, content, confidence?, status ∈ draft|previewed|modified|approved|rejected|withdrawn, decided_by, decided_at }` is stored in a **staging collection** that no projection reads as fact. Approval appends the real domain command(s) with `origin = ai_proposal` and `causation = proposal_id`; rejection keeps the proposal for audit (`LEGACY-FNC-055`, `LEGACY-NFR-006`).
8. **Feature requests** (UC-LEGACY-010/029) follow OPS-08: user proposal → administrator review (approve/reject/revise) → Systems Engineering control-repository change (requirement/use-case candidates with new IDs, never silently edited) → beta cohort via feature flag → monitor/rollback. The application records the administrator decision and the control change reference; **the control repository, not the application, is where a proposal becomes baseline**, preserving precedence and `LEGACY-BIZ-005`.
9. **External suggestions** (GitHub issues, `LEGACY-FNC-066`) are proposals with `source_url` and revision; approving imports a task with provenance; the application never writes to the external system.

### D4. Speech input privacy

10. Voice capture asks for the microphone **in context** with a text fallback visible first. Audio is streamed to the transcription provider under consent and **not retained by default**; the user may opt in to retain audio for a memory entry, in which case it is stored as a Restricted attachment under ADR-001 D4(13) with ADR-006 retention. Transcripts are shown for correction **before** any proposal is derived and are Restricted data.
11. Speech and AI telemetry records only feature usage, latency and error class (`LEGACY-NFR-008`); never transcript text.

### D5. Beta and feature flags

12. Feature flags are workspace-scoped `FeatureFlag` rows evaluated server-side; a flag can change behaviour, never authorization. Rollback is flag removal plus, where a flag introduced data, a documented compensating migration. Beta cohorts are explicit workspace lists (`LEGACY-FNC-058`).

## Considered alternatives

- **Let the AI module write to the database through its own service account.** Rejected by `LEGACY-NFR-019` and `EXTERNAL_INTERFACES.md`; also bypasses RLS and audit.
- **Client-side direct calls to the AI provider with a public key.** Rejected: leaks keys and loses server-side consent enforcement and minimisation.
- **Single blanket "AI features" consent.** Rejected: contradicts contextual, scoped, revocable consent in `LEGACY-UX-022`; per-feature scopes chosen.
- **Auto-apply high-confidence proposals.** Rejected: contradicts `LEGACY-FNC-054` ("no persistent change until confirmed"); confidence is shown, not acted on.
- **Keep raw audio by default for quality review.** Rejected: Restricted data retention without need; opt-in only.
- **Select a model now.** Deferred: vendor/model choice is configuration with recorded provenance; selecting it before S5 adds no architectural constraint and would age quickly.

## Consequences

### Positive

- AI cannot mutate the system of record except through the user's own authorised commands, so isolation, idempotency and audit are inherited rather than re-implemented.
- Consent and payload allow-lists make the privacy review (gate 6) checkable.
- Product evolution stays governed by the control repository.

### Negative

- Every AI feature needs an allow-list, a consent scope and a manual alternative, which slows feature delivery deliberately.
- Streaming transcription without retention limits later quality diagnostics unless users opt in.
- Deferring vendor choice means S5 planning must include a provider evaluation.

## Control provenance

Prepared by the Systems Engineering control-plane agent (Claude Fable 5.1, Claude Code) for LEGACY-WORK-002 as a reviewable proposal. Inputs: `CONOPS.md` OPS-04/OPS-08 and section 6, `EXTERNAL_INTERFACES.md`, `DOMAIN_MODEL.md` Integration/AI row, `USE_CASES.md` UC-LEGACY-010/024/028/029, reference baseline RISK-08 and invariant 10. Acceptance requires a human Systems Engineering decision.
