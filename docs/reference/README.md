# LEGACY Reference Artifacts

This directory contains durable, agent-readable material that should influence product discovery and implementation decisions across LEGACY.

## Current reference set

### `LEGACY_GAMIFICATION_UX_ARCHITECTURE_BASELINE_v0.1.md`

State-of-the-art benchmark and baseline candidate covering:

- habit/productivity/gamification product patterns;
- design principles and anti-patterns;
- application shell and information architecture;
- gamification model;
- reusable UX/agent capabilities;
- candidate business, functional, UX, and non-functional requirements;
- use cases and FVT seeds;
- traceability and release slicing.

**Use it when:** conceiving or reviewing mockups, adding a module, changing navigation, designing gamification mechanics, defining shared domain concepts, deriving requirements/use cases, or creating verification flows.

## Status semantics

`baseline-candidate` means the artifact is authoritative as a **reference constraint and traceability source**, but its candidate requirements are not automatically equivalent to formally approved project requirements. Promotion to the formal project baseline should preserve the IDs already assigned in the artifact.

## Maintenance rule

Do not overwrite historical versions. Add a new version and update `reference-manifest.yaml` so agents can determine the active reference.
