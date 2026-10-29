# Architecture canvas organization

`model.json` defines the existing candidate capability nodes and dependencies. `layout.json` also supplies four optional presentation groups to the local SDLC GUI:

- Platform & access: identity, workspace/data governance, and application shell.
- Planning & progress: Today, goals/map, habits/gamification, and focus.
- Life domains: finance, learning, media, memory, profile, and health.
- Assistance & connections: AI governance, social collaboration, and integrations.

These are navigation aids for the engineering diagram, not new product modules, deployment boundaries, lifecycle approvals or changes to the five-surface consumer shell. Clicking a group reveals its existing nodes while other groups stay collapsed. Dependency direction and controlled evidence remain on the original nodes. Use **Detail → All elements** for the full canvas. Newly introduced nodes not assigned here remain visible through scope fallback groups.

Keep each node in at most one group, with valid existing node IDs and unique nonempty group IDs/labels. Grouping and geometry are excluded from the semantic Architecture Steward fingerprint. The GUI validates group membership when loading the layout.
