---
artifact_id: LEGACY-REF-FIN-001
title: Legavia Financial Life Management — Requirements and Use Cases
version: "0.1"
status: baseline-candidate
created: 2026-10-14
owner_scope: Legavia / Life / Financial
canonical_format: markdown
agent_readable: true
source: "User financial-module discovery request, 2026-10-14; existing 2026 spreadsheet identified as a future mapping/validation input"
extends:
  - LEGACY-REF-UX-001
  - LEGACY-FNC-017
  - LEGACY-FNC-021
  - LEGACY-FNC-028
  - UC-012
audiences: [product, requirements, ux, mockup, architecture, development, verification, security]
approval_required_for_promotion: true
---

# Legavia Financial Life Management — Candidate Requirements and Use Cases

> **Governance:** This document records user discovery as an agent-readable **baseline candidate**, not a statement of shipped functionality or approved architecture. Reconcile the reference spreadsheet before approving mappings, categories, fields, and import rules. No personal transaction data or credentials belong in this repository. Preserve all existing LEGACY and UC identifiers.

## 1. Intent and user outcomes

Build a complete financial-management **view** in Legavia, not a sixth top-level navigation tab. Route: **Life → Financial**, with selected cross-domain KPIs discoverable in **Insights** and goal progress linked to the existing shared Goal → Phase → Milestone → Action model.

Answer reliably:
- How much did I earn, spend, **save**, and accumulate this month and year?
- What percentage of expenses were **essential** versus **non-essential**, and which categories are contributing most to discretionary spending?
- What is the balance of each debit/current/savings account and the amount still **payable on each credit card**, with billing period, due date, and installments?
- How are my finances distributed across **UAE/AED** and **Brazil/BRL**, including local earnings, transfers/remittances, and foreign-exchange effects?
- How much is committed to **car** expenses (rental, ownership, financing, insurance, maintenance, fuel/charging) and the **apartment** (rent, ownership, mortgage, taxes/fees, property valuation, rental income)?
- How do my cash flow, assets, liabilities, goals, and forecasts evolve over **1–5 years** under explicit assumptions?

Use terminology precisely: salary or other earned income is **income**, not investment profit; monthly savings is **income minus recognized expenses** under a specified method; credit-card repayments and internal transfers must not inflate expenses; net-worth movement, realized investment profit, and unrealized valuation changes are distinct metrics.

## 2. Navigation and interaction design

Existing shell stays **Today / Map / Life / Insights / Me** (LEGACY-REF-UX-001). The Financial module contains subviews: **Overview**, **Transactions**, **Accounts & Cards**, **Budgets & Categories**, **Assets & Liabilities**, **Forecasts**, and **Review & Import**. These are module-level views, **not** new top-level tabs.

- **Overview:** top-level KPI cards for monthly savings, savings rate, current cash balances, upcoming card bills, net worth, and yearly progress; drill-downs by AED, BRL, country, account, category, time range and status.
- **Transactions:** quick-add and batch-entry interfaces with a **single primary action** appropriate to context. Default entry controls: date, amount, currency, payee/description, category/subcategory, essential yes/no, payment source/account/card, country/domain, transaction type, status; optional tags, installment metadata, receipt and linked goal/project. Remember previously used values; support edit, duplicate, split, undo, and reclassification.
- **Weekly Financial Review:** Sunday-oriented review, **not** a mandatory Sunday schedule. Select a date range (default: prior unreviewed week); choose account/card and import or paste multiple lines; classify in a spreadsheet-like queue with keyboard and touch support; preview potential duplicates; reconcile against issuer/bank statement; commit approved rows as a batch; track reviewed/unreviewed status.
- **Accounts & Cards:** balance per bank account (UAE/Brazil), available vs statement balance, debt per card, current and next invoice, billing close and due dates, installment commitments, credit limit and payment history.
- **Budgets & Categories:** monthly category baselines, fixed/variable costs, essential vs discretionary segmentation, actual vs budget deltas, savings goals and trends.
- **Forecasts:** explicit scenario input (income changes, rent/property costs, car acquisition, spending changes, remittances, FX, inflation/returns) and one-to-five-year outputs with assumed and actual values visually differentiated.
- **Assets & Liabilities:** property and investment holdings, car asset where owned, loans and mortgage principal; acquisition, depreciation, valuation changes, debt-service cash flow and expenses shown without double counting.

Require loading, empty, populated, validation error, permission denied, offline/sync, and reconciliation-conflict states as applicable. Keep operational screens restrained and accessible; 44×44 pt minimum touch targets on iOS-class screens, no drag-only essential interaction.

## 3. Candidate functional requirements

| ID | Requirement | Priority candidate | Verification |
| --- | --- | --- | --- |
| LEGACY-FNC-029 | Support multiple accounts/cards across UAE and Brazil with type, currency, opening balance, as-of date, status, issuer, and ownership/workspace. | P0 | FVT-LEGACY-009,010 |
| LEGACY-FNC-030 | Capture, edit, split, undo and batch-create categorized transactions, with essential flag independent of category, payment source, date, status, and provenance. | P0 | FVT-LEGACY-009 |
| LEGACY-FNC-031 | Support weekly review of card and account activity including duplicate preview, classification, bulk approval, and statement reconciliation. | P0 | FVT-LEGACY-009,013 |
| LEGACY-FNC-032 | Correctly model credit-card purchases as expenses and card liabilities, while card payments settle liabilities without creating duplicate expenses. | P0 | FVT-LEGACY-010 |
| LEGACY-FNC-033 | Track balances for debit/savings accounts through posted activity, transfers, adjustments, and reconciliation with independently supplied statements. | P0 | FVT-LEGACY-010 |
| LEGACY-FNC-034 | Represent cross-border remittances and account transfers as linked legs; preserve native amounts/currencies, fees, actual conversion rate, rate timestamp/source, and FX impact. | P0 | FVT-LEGACY-011 |
| LEGACY-FNC-035 | Summarize monthly and annual income, expenses, savings/savings rate, budget variance and essential/non-essential spending by country, account and category. | P0 | FVT-LEGACY-012 |
| LEGACY-FNC-036 | Maintain monthly budgets and planned/recurring/fixed/variable/installment commitments, with actual vs forecast cash flow and bill reminders. | P1 | FVT-LEGACY-012,014 |
| LEGACY-FNC-037 | Track vehicle costs as ownership/rental operating expenses separately from financing principal, depreciation and one-time acquisition costs. | P1 | FVT-LEGACY-014 |
| LEGACY-FNC-038 | Track apartment-related payments, property asset valuation, related debt, equity and optional rental revenue while avoiding double counting. | P1 | FVT-LEGACY-014 |
| LEGACY-FNC-039 | Project one-to-five-year cash flow, saving potential, net worth and goal trajectories, supporting multiple scenarios and recorded assumptions. | P1 | FVT-LEGACY-014; existing FNC-028 |
| LEGACY-FNC-040 | Preview and map spreadsheet/CSV/Google Sheets financial data, support manual adjustment and explicit import approval, and suppress duplicate import rows. | P0 | FVT-LEGACY-013 |
| LEGACY-FNC-041 | Expose source/provenance, creation/edit history, reconciliation status and reversible correction for imported and manually entered transactions. | P0 | FVT-LEGACY-009,013 |
| LEGACY-FNC-042 | Calculate account-level balances and a consolidated balance/net-worth view in selectable presentation currency without overwriting native-currency ledger entries. | P1 | FVT-LEGACY-011,014 |
| LEGACY-FNC-043 | Distinguish earned income, refunds, reimbursements, investment profit/loss (realized/unrealized), internal transfers and valuation changes in reporting. | P0 | FVT-LEGACY-011,012 |

### Candidate UX and security constraints

| ID | Requirement | Priority |
| --- | --- | --- |
| LEGACY-UX-013 | Weekly reconciliation supports efficient multi-row review; classify multiple transactions without reopening a modal for every field. | P0 |
| LEGACY-UX-014 | Overview metrics have drill-downs to the constituent transactions, accounts and calculation definitions; the displayed reporting currency and FX assumptions remain visible. | P0 |
| LEGACY-UX-015 | Present actuals, commitments, projections and uncertainty as distinguishable states; do not present forecasts as account balances. | P0 |
| LEGACY-UX-016 | Saving, discarding and undoing a batch must have explicit feedback and guard against loss of partially reviewed work. | P0 |
| LEGACY-NFR-009 | Financial transactions are private by default; workspace permissions must be enforced server-side and data encrypted in transit and at rest. | P0 |
| LEGACY-NFR-010 | Posting/importing transactions and transfer legs must be idempotent; partial failures cannot leave inconsistent account or card balances. | P0 |
| LEGACY-NFR-011 | Amount arithmetic uses deterministic decimal/fixed-point values with explicit per-currency scale; reporting FX conversions preserve provenance and rounding. | P0 |
| LEGACY-NFR-012 | Imported statements and personal finance data must not be committed to public code repositories or exposed through telemetry/logs; support data export and deletion. | P0 |

## 4. Use cases

### UC-013 — Record and reconcile weekly transactions

**Actor:** Authenticated user.  
**Trigger:** Weekly review, commonly performed on Sunday.  
**Preconditions:** At least one configured account or credit card; user has permission to modify its ledger.

**Main flow:**
1. Open Life → Financial → Review & Import and select the account/card and statement/date window.
2. Enter transactions individually, paste several lines, or select an approved import source.
3. System displays an editable queue with date, description, amount, original currency, payment source, category, essential flag, posting status and candidate duplicates.
4. User adjusts categories/essentiality in bulk, optionally splits rows, and reviews totals.
5. System previews changes to card payable/debit balance and flags unreconciled differences.
6. User explicitly approves the selected entries; system commits atomically, updates balances and analytics, and retains provenance and review status.

**Alternates:** Save draft and resume; reject duplicate; missing category → Uncategorized with warning; mismatched statement → pending reconciliation, not forced balance; invalid currency/amount → row-level error without corrupting others; repeated import → no duplicate posting.  
**Postconditions:** Each accepted entry appears exactly once; original source and audit trail are retained.  
**Trace:** FNC-029,030,031,040,041; UX-013,016; NFR-009,010; FVT-LEGACY-009,013.

### UC-014 — Manage bank accounts, credit cards and invoices

**Actor:** Authenticated user.  
**Main flow:** Create UAE/BRL bank account or card → record opening balance/date and issuer settings → record debit purchases or credit purchases → inspect running balances, card billing cycle, purchases and installments → record credit-card settlement from an existing debit account → inspect updated balances and remaining payable.  
**Invariant:** A credit purchase increases the card liability and expense once; payment decreases the card liability and cash and **does not create a second expense**. Due bills and future installments must be differentiated from already-posted expenses.  
**Trace:** FNC-029,032,033,036; FVT-LEGACY-010.

### UC-015 — Review savings, budget performance and financial trajectory

**Actor:** Authenticated user.  
**Main flow:** Select month/quarter/year and UAE, Brazil or consolidated scope → inspect opening/closing balances, incomes, recognized expenses, monthly net savings, saving rate, discretionary/essential ratios, largest spending categories, budgets and rolling trends → drill into contributing transactions → inspect longer horizon scenarios and goal links.  
**Invariant:** State which metric is cash flow, savings, investment profit, or net-worth change; currency aggregation uses displayed FX rules.  
**Trace:** FNC-035,036,039,042,043; existing FNC-021,028 and UC-012; FVT-LEGACY-012,014.

### UC-016 — Remit money between UAE and Brazil

**Actor:** Authenticated user.  
**Main flow:** Select source account/currency and destination account/currency → enter sent amount, received amount, transfer fees, transfer date and FX rate/source → system previews net effects → user records transfer → two linked account legs settle/reconcile; fees are tracked as expenses.  
**Invariant:** A transfer between owned accounts is **neither new earned income nor ordinary consumption spending**. Rate movement and fees remain visible.  
**Alternates:** Pending transfer, unequal settlement dates, incomplete destination reconciliation, cancellation/reversal.  
**Trace:** FNC-033,034,042,043; FVT-LEGACY-011.

### UC-017 — Plan vehicle, property and recurring obligations

**Actor:** Authenticated user.  
**Main flow:** Register car use (rental or owned) and apartment (rent or owned) → add planned recurring charges, acquisition costs, insurance, fuel/charging, maintenance, mortgage/loan terms, property valuation and optional Brazilian rental income → choose baseline/scenario → review current costs, remaining commitments, net-worth effects and cashflow for years 1–5.  
**Invariant:** Loan principal changes cash and liability, loan interest is expense, depreciation/valuation changes net worth but not cash; rent does not create owned property equity.  
**Trace:** FNC-036,037,038,039,043; FVT-LEGACY-014.

### UC-018 — Migrate the user's 2026 financial spreadsheet

**Actor:** Authenticated user.  
**Main flow:** Upload the reference workbook or authorize its Google Sheets source → inspect detected sheets/columns/date conventions → map UAE and Brazil monthly sheets, categories, essentiality flags, sources and beginning balances to canonical fields → preview normalized entries and duplicate/missing-field warnings → explicitly approve the import → compare calculated closing account/card balances against spreadsheet statements.  
**Pending evidence:** User has said the reference workbook will be supplied; **no actual column mapping, financial amounts or import result is asserted here**.  
**Trace:** FNC-030,031,040,041; FVT-LEGACY-013.

### UC-019 — Correct and audit a transaction

**Actor:** Authenticated user.  
**Main flow:** Locate transaction from dashboard/card/account → inspect imported/manual provenance and affected balances → edit classification or reverse a posted error → system recalculates affected account, card, reporting and projections consistently while preserving the prior version.  
**Trace:** FNC-030,032,033,041; NFR-009,010; FVT-LEGACY-009,010.

## 5. Data model guidance (architecture candidate)

Prefer a transaction/ledger-centered shared finance domain with **month derived from transaction dates**, not physically duplicated per-month ledgers. Candidate entities:

- **FinancialAccount:** id, owner/workspace, country, account_type, institution label, currency, opening_balance, opening_as_of, reconciliation state.
- **CreditCard:** account link, statement_close_day, due_rule, credit_limit, installments, payment source, billing-cycle ledger view.
- **Transaction:** id, effective_date, posted_at, amount_decimal, native_currency, type, merchant/description, category_id, essentiality, source_account/card, status, country/domain, recurrence/installment metadata, provenance, version.
- **Transfer:** id and linked source/destination ledger legs, sent/received amounts, FX quote/actual rate, fees, pending/settled state.
- **Budget / SavingsGoal / RecurringObligation:** scope, period, target, linked goal, schedule, expected vs actual events.
- **Asset / Liability / Valuation:** apartment, vehicle, investments, mortgage, financing, as-of date, liability outstanding, provenance, valuation method.
- **Statement / Reconciliation / ImportBatch:** source, statement period, line fingerprint, mapping revision, review status, approval timestamp, immutable import provenance.
- **ForecastScenario:** assumptions, initial state, time horizon, output series, scenario version.

Keep a clear distinction between: **transaction date**, **posting date**, **card statement closing/due date**, **bill payment date**, **as-of balance date**, and **conversion date/rate**. Transfers are matched linked records; asynchronous two-country settlements must not be silently treated as complete.

### Canonical computation contracts to confirm before approval

- Monthly economic savings = recognized income − recognized expenses, excluding intra-owned-account transfers and card payments. Cash accumulation is a separate cashflow metric and can differ due to asset purchases, debt principal and investments.
- Savings rate = net monthly savings / eligible recognized income; show N/A on zero/nonpositive denominator rather than dividing by zero.
- Liquid balance = starting balance + posted account inflows − posted outflows, reconciled against bank statement; pending amounts are shown separately.
- Card amount payable = issuer-posted card purchases/fees/interest − refunds − cleared payments, with billing cycle and current total separately reported.
- Net worth = financial balances + valued owned assets − liabilities; valuation assumptions and FX treatment are exposed.
- Report **realized** investment result separately from **unrealized** asset revaluation and salary/earned income.
- Forecasts are labeled estimates; each 1–5-year scenario retains its inputs, FX assumptions and inflation/return assumptions for reproducibility.

## 6. Candidate functionality verification tests

| ID | Scenario | Representative test and acceptance |
| --- | --- | --- |
| FVT-LEGACY-009 | Weekly review | Create mixed AED/BRL, card/debit, essential/non-essential transaction queue; batch classify/review/undo; assert exact-once posting, category totals, review status and source provenance. |
| FVT-LEGACY-010 | Balance and credit settlement | Charge AED 300 on credit → expense +300, card payable +300; pay card AED 300 from debit → cash −300, card payable 0, total expenses still +300. Test pending and partial payments. |
| FVT-LEGACY-011 | Remittance and FX | Transfer funds from UAE AED account to Brazilian BRL account with explicit received amount, FX and fee; assert linked entries, correct native balances, fee expense and **no artificial income**. |
| FVT-LEGACY-012 | Monthly reporting | Mix Brazil/UAE income, car spending, fixed and discretionary spending, category baselines; assert income, savings rate, essentiality, category ranking and yearly aggregate from the same ledger. |
| FVT-LEGACY-013 | Spreadsheet migration | Import a representative anonymized workbook including UAE monthly sheets and BRL entries, re-import it, assert zero duplicates; reconcile with independently recorded opening/closing account/card balances. |
| FVT-LEGACY-014 | Asset and forecast consistency | Model owned/rented car, owned/rented apartment, mortgage principal and interest, Brazilian income, planned remittance and a 1–5 year forecast; verify cashflow/net-worth distinction and reproducible assumptions. |

## 7. Reference spreadsheet integration / acceptance gate

The user's financial spreadsheet (previously described as a **2026 multi-sheet workbook** with UAE monthly controls and Brazil finances) will be treated as **discovery and migration evidence**, not the runtime persistence layer. The user intends to provide it; this revision does not claim to have examined it.

When provided:
1. Inventory sheets and transaction column semantics; inspect card statements, category flags, Brazil/UAE sections, financing, transfers, monthly closing balances and recurring entries.
2. Establish explicit source-column → canonical-field mappings, date/currency conventions and missing-data policies.
3. Import into a staging preview using safe, idempotent row identifiers; **never** push raw amounts, source attachments, credentials or private financial data into this repository.
4. Extend UC/FNC/FVT cases with observed field variants and anonymized fixtures; preserve original ids and record mapping decisions/ADRs.
5. Seek explicit project approval before promoting these candidate requirements into the controlled baseline.

## 8. Work-package suggestions / phased delivery

- **Financial MVP / first slice (P0):** Financial module shell, configured accounts/cards, single & batch transaction entry, essentiality/category, weekly review, credit-card payable, native account balances, monthly income/expenses/savings dashboard, simple spreadsheet import, duplicate detection and privacy controls.
- **Extended first-class finance (P1):** transfer FX reconciliation, advanced budgets, installments/recurrence, apartment/car detailed economics, net-worth and scenario projection, goal linkage, additional source integrations.
- **Later (P2):** optional bank connector automation, intelligent category suggestions from confirmed history, rule-based recurring detection, periodic financial summaries and advanced scenario simulation.

A user-facing Financial view is **not** implemented by this document. Release requires UX review, privacy review, representative demonstrations and passing FVTs.
