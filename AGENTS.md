# LEGACY Agent Guidance

This repository uses repository-resident reference artifacts to keep mockup, UX, requirements, architecture, implementation, and verification agents aligned.

## Mandatory reference loading

Before creating or materially changing a mockup, screen flow, navigation structure, design-system primitive, gamification mechanic, shared product entity, or product architecture decision, read:

1. `docs/reference/README.md`
2. `docs/reference/LEGACY_GAMIFICATION_UX_ARCHITECTURE_BASELINE_v0.1.md`
3. `docs/reference/reference-manifest.yaml` for machine-readable applicability and precedence.

## Decision precedence

When sources conflict, use this order unless a later approved artifact explicitly supersedes it:

1. Approved project requirements / architecture decisions.
2. Approved use cases and verification criteria.
3. This repository's reference baseline artifacts.
4. Mockups and exploratory prototypes.
5. Agent inference.

Do not silently change a baseline invariant to make an implementation easier. Surface the mismatch and propose a requirement update, ADR, or scoped deviation.

## Mockup-specific rules

- Reuse the five-surface shell (`Today`, `Map`, `Life`, `Insights`, `Me`) unless an approved decision changes it.
- Keep operational screens low-friction and visually restrained; concentrate expressive 8-bit/pixel-art theming in progression surfaces.
- Define primary/secondary actions and all relevant UI states before considering a screen complete.
- Preserve navigation state across top-level surfaces.
- Never make an essential workflow drag-only or color-only.
- Treat the map as a representation of `Goal -> Phase -> Milestone -> Action`, not as a separate game database.

## Architecture-specific rules

- Prefer one shared domain model over duplicated per-module concepts.
- Keep gamification as a derived/projection layer over meaningful domain events where practical.
- Model user/workspace/permission isolation as a cross-cutting concern.
- Maintain provenance for imported/automated data and explicit approval for AI-generated project evolution.
- Preserve traceability IDs when promoting candidates into the formal baseline.
