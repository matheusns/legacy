---
project: LEGAVIA
artifact_status: baseline-candidate
version: 0.1.0
date: 2026-10-29
control_repository: matheusns/legacy
review_gate: Systems Engineering approval required
---

# External Interfaces, Consent and Failure Contracts

> Controlled **candidate**, not an approved specification. Preserve existing LEGACY IDs; changes require review and traceability updates.

| External interface | Input/output contract | Authority and failure behavior |
| --- | --- | --- |
| GitHub | Selected issues/project metadata → proposed tasks; source URL and revision retained | Read scoped permission; no task creation or issue mutation until approved; disconnect revokes future refresh |
| Calendar | Authorized event times and subjects → Today scheduling context | Explicit per-account read grant; handle timezone, recurrence and revoked tokens; manual planning always available |
| Health | Authorized activity/wellness signals → nonclinical activity view | Least-privilege consent; source and measurement units preserved; no diagnosis |
| Finance CSV/XLSX/Sheets | Preview-mapped transactions and provenance → reviewed import batch | No production import on discovery; duplicate detection and reconciliation; never store personal workbook in Git |
| Speech & AI | Voice/text input → transcript → typed task/memory/feature proposal | Consent, data minimization, preview and human approval; model has no DB write credentials |
| Remarkable / notes | User-exported files or connected provider content → private memory candidate | Provider capability/terms and rights review; manual document upload fallback |
| Media storage | Authenticated upload/download via scoped signed access | Quotas, type checks, retention, no public media links by default |
| Movie ratings | Title matching and timestamped licensed rating snapshot | Unknown titles/rate limits/offline results show manual rank; attribution and legal terms honored |
| Browser/PWA | Responsive accessible web interactions and local draft cache | No assumption of native iOS permission parity; offline claims require tested support |

## Cross-interface requirements
All connectors carry explicit consent scope, provider identity, last successful sync time, last error, source ID and data lineage. Failed/stale integrations never erase manual data. API keys, OAuth tokens and provider responses are not to be committed to any GitHub repo or copied into screenshots. Admin controls connector configuration but not private user content by default.
