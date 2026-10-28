---
artifact_id: LEGACY-SDLC-001
project: LEGAVIA
title: Legavia SDLC Execution and Configuration Contract
version: 0.2
status: candidate-for-SE-review
date: 2026-10-29
control_repository: matheusns/legacy
---

# Legavia SDLC Execution and Configuration Contract

> This artifact is a candidate systems-engineering baseline. Existing stable identifiers are preserved. Review and approve before treating any proposal as an accepted specification or an executable FVT.

## Repository allocation

| Repository | Role | Write authorities |
|---|---|---|
| `legacy` | ConOps, requirements, controlled functionality, ADRs, WPs, manifest, governance | Product and Systems Engineering review only |
| `legavia_sdlc_gui` | Local orchestrator, GitHub/workspace adapters, progress/evidence views | Tooling engineer + tests |
| `legacy_app` | Production web/phone application, migrations and API | Development/UX scoped by WP |
| `legacy_mockups` | Exploratory visuals, pinned image/prototype references | UX agent, with controlled approval for reference promotion |
| `legacy_verification_tooling` | Independent tests, browser fixtures and visual comparisons | QA/Verification agent |

## Agents and duties

**Product/Business Analyst:** translates voice notes and proposals into candidate business need, use cases, measurable acceptance hypotheses; no automatic promotion.

**Systems Engineer:** owns traceability, requirement status, WP splits/dependencies, controlled FVT semantics and formal acceptance.

**Architecture Steward:** reads all affected references/ADRs and performs a conformance gate before Development; proposes ADRs where gaps exist.

**UX/Design Agent:** owns approved responsive screen contracts, tokens, artwork use and visual reference comparisons; cannot bypass accessibility.

**Developer Agent:** receives an immutable WP context, allowed target repos, acceptance criteria and accepted ADRs; edits code only in write-allowed worktrees.

**Verification Agent:** independently runs approved unit, integration, security, E2E and visual checks; may file findings, not revise protected tests or requirements without SE approval.

**Release/Operations Agent:** handles preview/prod environment, approved beta flags and rollback records; does not infer approval from code merge.

## Workflow and gates

Discovery → ConOps/use case candidate → requirement review → functionality allocation → Architecture ADR gate → WP approval/branch/worktree isolation → implementation → independent verification → UX/SE acceptance → GitHub PR review → beta/release and rollback evidence → post-release lessons learned.

Every handoff records source baseline, dependency predecessor states, repository revision, provider/model, timestamps, execution/fixture versions, and candidate fingerprint. Agent-run test success is not equivalent to independent acceptance. In a review/fix cycle, Architecture evaluates the comment, SE determines whether the change needs an FVT, and the reply remains blocked if an implementation WP is required and unfinished.

## Work package execution policy

- Predecessors in `depends_on` must be satisfied before a successor is eligible.
- `target_repositories` are exact write candidates; any new repo requires explicit review.
- Each new WP has test strategy, acceptance criteria, security/privacy impacts and user-observable behavior.
- `systems_engineering` packages may be documentation/decision-only, and should not require simulated implementation changes or a mandatory FVT unless their risk calls for one.
- UI/UX WPs require a phone/desktop comparison contract and independent capture evidence.
- Never invent successful evidence: `Backlog`, `Done` and FVT status are independent states.

## GUI compatibility and operational startup

From sibling checkouts:

```bash
cd ~/dev_ai/legacy
PYTHONPATH=../legavia_sdlc_gui/src python3 -m sdlc_gui --manifest traceability/manifest.json --validate-only
PYTHONPATH=../legavia_sdlc_gui/src python3 -m sdlc_gui --manifest traceability/manifest.json
```

The existing GUI currently reflects upstream library/node assumptions; `scope=all` permits correct data validation while **not** pretending its product component mapping is finished. Do not register real agent runners or production external writes until `WORK-011` GitHub/provider adapters and verification profile are accepted.

## Acceptance disposition

This v0.2 baseline is a **proposal under configuration control**. Approval is an explicit product/SE review, not an automatic consequence of committing this branch or opening its PR.
