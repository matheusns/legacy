---
artifact_id: LEGACY-REF-FIN-002
title: Legavia Financial — 2026 Workbook Schema Mapping and Migration Acceptance
version: "0.1"
status: baseline-candidate
observed_at: 2026-10-14
source: "User-supplied private Google Sheets workbook titled 2026"
privacy: "schema-only — no source workbook URL/ID, account identifiers, transaction rows, personal payees or monetary figures"
extends:
  - LEGACY-REF-FIN-001
  - UC-013
  - UC-014
  - UC-015
  - UC-016
  - UC-018
  - FVT-LEGACY-009
  - FVT-LEGACY-010
  - FVT-LEGACY-011
  - FVT-LEGACY-012
  - FVT-LEGACY-013
audiences: [product, requirements, ux, architecture, development, verification, security]
approval_required_for_promotion: true
---

# Legavia Financial — Workbook-Informed Migration Mapping

> This document extends [LEGACY-REF-FIN-001](LEGACY_FINANCIAL_LIFE_MANAGEMENT_USE_CASES_v0.1.md) with **observed workbook structure**. It is a baseline **candidate**, not permission to import or publish the user's data. No actual financial values, transaction descriptions, personal counterparties, full or partial card identifiers, credentials, or source workbook URL are retained here.

## 1. Source inventory and coverage

The user's private **2026** Google Sheet was inspected **read-only** on 2026-10-14. The native workbook reports locale **pt_BR** and time zone **America/Bahia** and contains **34 tabs**:

- Ten **Brazil monthly expense** tabs (January–October 2026): mixed Portuguese/English month titles, amounts in BRL.
- Ten **UAE monthly expense/account-summary** tabs (January–October 2026): amounts in AED.
- Ten **CDC UAE monthly** tabs (January–October 2026): detailed card-item records in AED.
- Three **December 2025** historical tabs covering Brazil, UAE, and CDC UAE.
- One **ENTRADAS** tab: cross-month earnings, opening/closing balances, saved-value calculations, and narrative notes in both currencies.

Some prior-month tabs are hidden but contain financial history. **Hidden does not mean obsolete.** Active workbook tabs and header labels use mixed Portuguese and English; source title spelling/casing must not be interpreted as a domain identifier. Month and year need explicit source mapping.

### Sheet family → normalized data ownership

| Workbook family | Observed business role | Primary Legavia entities | Import policy |
| --- | --- | --- | --- |
| Brazil monthly | Expense ledger / category overview | Transaction (BRL), ExpenseCategory, ReviewStatus, RecurringObligation | Candidate expense rows only; summary formulas and category total panels are **derived checks**, not extra transactions |
| UAE monthly | Cash/debit expense rows plus **credit-card settlement amounts** and cross-country movements | Transaction, Transfer, CreditCardPayment, AccountBalanceSnapshot | **Classify each row by economic event** before posting; card payments must not create a second expense |
| CDC UAE monthly | Card purchase/fee/refund journal, category classification, weekly card reconciliation and period rollovers | Transaction, CreditCard, Statement, Installment, ImportBatch | Detailed purchases are **primary spending evidence**; derived card totals and weekly rollups are not additional purchases |
| ENTRADAS | Opening balances, earned and miscellaneous receipts, transfers/investment interest, period summaries and calculated savings | BalanceSnapshot, IncomeEvent, InvestmentReturn, Transfer, ForecastBaseline | Distinguish **SALDO ANTERIOR** from income; do **not** import 'TOTAL DE ENTRADAS' as earned income |

Import the financial **meaning** of cells, not their display location or spreadsheet formulas. Do not treat a calculated subtotal as a ledger transaction.

## 2. Observed columns and provisional mappings

| Family | Source columns / visible fields | Candidate normalized fields | Mapping notes |
| --- | --- | --- | --- |
| Brazil monthly | A marker; B LAST; C ITENS; D DATA; E R$; F CATEGORIA; G OK; H 70/30 | recurrence/installment marker; carryover status; description; transaction date; native amount BRL; category; review status; spending class | Dates often blank for recurring expenses; **never invent a specific posting date** from the monthly tab alone |
| UAE monthly | A marker; B LAST; C ITENS; D DATA; E AED; F CATEGORIA; G STATUS; H 70/30 | same fields, AED; settlement/payment type for card rows | Some 'ITENS' are card or bank **payments**, not underlying purchases; detailed CDC rows take precedence for expenditure analysis |
| CDC UAE monthly | A marker; B LAST; C CARD; D ITENS; E DATA; F AED; G CATEGORIA; H STATUS; I 70/30 | recurrence/installment; carryover marker; payment instrument alias; description; date; amount AED; category; review status; spending class | CARD aliases occur across months; resolve into stable account/card IDs in **private** runtime configuration |
| ENTRADAS | B source text; E BRL; F AED; J–L notes, saved balances and ratios | event description/type, amount BRL or AED, reporting/balance snapshots | A row may contain unrelated descriptions in a shared label, with simultaneous values for both currencies. **Split/approve records** before posting |

Category/analysis panels appear beyond the transaction columns (e.g., Brazil/UAE K onward and CDC UAE L onward); they include allocations, category spending totals, target percentages, card rollups and reporting formulas. Their values are **read-only reconciliation comparators** rather than new ledger rows.

### Provisional marker and status semantics

- Marker **F** is used by formulas to sum fixed monthly costs. Treat this as a **recurrence/fixed-obligation candidate**, not a guarantee that the transaction recurs indefinitely.
- Marker **P** is used to sum monthly installment amounts. Resolve number of installments, start/end date, and card linkage before creating future liabilities.
- **LAST**, **L**, and other markers have ambiguous usage; do not infer lifecycle semantics without reviewed examples.
- **OK** is the workbook's review/selection indicator in calculated spending totals. It does **not** prove bank clearing, statement settlement or fully reconciled account balances.
- Spending classification includes **Essencial**, **Foda-se**, **Imprevistos**, and additional allocation group names such as **Educação**, **Objetivos C,M&L** and **Apostas**. Preserve original labels as user-configurable **legacy aliases**; normalize to stable internal class IDs **without forcing everything into one Boolean**.
- Expense **category** and spending **class/intention** are independent dimensions. A category can contain records with different spending classes.
- Card aliases observed in the CDC UAE **CARD** column are a stable source grouping dimension. Map aliases to private card records; **never include any card-number fragment or personal account ID** in repository fixtures.

### Formatting/locale contracts

- Original workbook locale is **pt_BR** and presents mixed **R$** and **dh/AED** currency formatting, commas as decimal separators, occasional leading minus signs, and textual dash sentinels.
- Parse values from their native numeric cell values where available; preserve the raw presentation string separately for diagnostics. A dash in a computed summary is **missing/not applicable**, not a monetary zero.
- Derive reporting time from source period but keep missing transaction-date precision explicit. A full transaction date must be supplied or confirmed if source only provides month.
- Source spreadsheet time zone **America/Bahia** is not a reason to assign Brazilian calendar date semantics to UAE banking events; imported dates are local business dates with an explicit country context until determined.
- Do not implicitly exchange AED and BRL, and do not treat totals with mixed currency as a meaningful aggregate without exchange-rate provenance.

## 3. Observed business workflows to preserve

### A. Sunday-oriented batch entry and review
The CDC UAE family supports card-specific transaction entry, category selection, class/allocation selection, fixed or installment flags, and an **OK**-gated review calculation. Legavia shall provide quick multi-entry review, reusable payee/category defaults, column keyboard navigation and bulk correction. An incomplete batch can be resumed without prematurely affecting published financial totals.

### B. Weekly spending and prior-cycle carry-over
CDC UAE sheets contain separate 1W, 2W, 3W, 4W, LAST MONTH and TOTAL columns grouped by card. Next-month UAE sheets reference prior CDC monthly totals. Legavia shall:
1. Preserve underlying transaction/posting date and statement cycle.
2. Support weekly aggregation and a **card previous-cycle opening/closing liability**.
3. Reconcile current statement vs outstanding payable rather than manually copying monthly spreadsheet balances.
4. Model partial payments, refunds/credits, installment rollovers, and unsettled transactions explicitly.

### C. Card spending vs card payments (critical)
Some UAE monthly summary entries derive their amounts from the **previous CDC UAE month's card total**. Importing both those entries and all detailed CDC rows as expenses would double-count costs.

**Candidate precedence:** CDC rows classified as purchases/fees/refunds are primary transactions. UAE card settlement rows are recorded as **credit-card liability payments** from a source bank/debit account. Do not automatically create a matching payment unless there is an independently confirmed bank movement or user approval. Statement periods may overlap months; trace rather than infer.

### D. Income, savings, opening balances and cross-border transfer
ENTRADAS contains historical prior balances, earnings, miscellaneous receipts, period roll-ups, savings percentages and reported balance snapshots. Formula totals may sum both opening balances and new receipts. Legavia shall record opening balances as **opening snapshots**, not new income; savings as a derived metric with a documented basis; bank interest as investment/interest income if confirmed; UAE → Brazil remittances as linked transfer legs plus fees and FX, not earned income or general spending.

### E. Budget allocation and fixed commitments
The **70/30** header is present across the sheet families but observed rows also use a richer allocation taxonomy and percentages. Do **not** assume its numerical policy or force 70/30 as a hard validation rule without approval. Preserve editable spending class, configurable allocation targets, and separate category-budget targets. Treat source fixed/instalment flags as forward-obligation evidence, not final future charges.

## 4. Workbook quality hazards and migration gates

Read-only inspection found **real formula-result issues** that should be handled by the importer:

1. **Broken formula references:** the Brazil September sheet has a salary reference returning **#REF!** (visible in the salary summary), which cascades into percentage displays. Never import these calculated outputs as authoritative balances or income.
2. **Text sentinel divided as number:** category calculations in several sheet families return **#VALUE!** when a dash used for "no transactions" is divided by an amount. Recalculate analytics from normalized posted transactions rather than copying spreadsheet percentage formulas.
3. **Mixed opening balances with earned income:** **ENTRADAS** period totals can include the previous balance in their sum. Treat prior balances and new inflows separately, or savings/yield rates become misleading.
4. **Historical/label ambiguity:** at least one ENTRADAS month header uses a **2025** year label despite being in the 2026 sequence. Resolve against explicit month tabs and surrounding periods rather than blindly trusting a heading.
5. **Approximate accounting period:** many individual rows have no entry-level date. Missing date precision is a visible import exception, not an opportunity to silently invent a day.
6. **Card reconciliation adjustments:** manual carry-over, credits, weekly sums and exceptional adjustments appear in the calculation zones. Treat as reconciliation controls that require source-to-destination review, not new expenditures.
7. **Source state:** several earlier tabs are hidden. All source sheet families must be included in inventory and import preview unless explicitly excluded.

**No source workbook has been changed** as part of discovery. No private data is embedded in this requirements artifact.

## 5. Implementable private migration mapping

Canonical staged import row should include:

- import_batch_id, source_sheet_family, source_sheet_title, source_row_index, source_cell_range, source_hash (private)
- account/card_alias_private, native_currency, amount_decimal, raw_display_value, signed_amount, direction
- month_period, transaction_date_nullable, date_precision: exact | month_only | unknown
- description_private, category_source, category_normalized, spending_class_source, spending_class_normalized
- recurrence_flag, installment_marker, payment_event_type: purchase | fee | refund | card_payment | transfer | income | opening_balance | asset_valuation | unknown
- review_state: staged | needs_review | approved | excluded | duplicate_candidate
- clearing_state: pending | posted | settled | unknown
- statement_id_nullable, matching_status, approval_actor, audit_revision
- source_formula_flag and source_error_flag when the source is a spreadsheet formula

### Validation/reporting logic
- **Exactly-once import:** identify repeated rows across sheet import batches using source provenance plus robust content identity and approval, while not dropping legitimate recurring identical charges.
- **Avoid summary double-counting:** import transaction-like rows only; preserve calculated summary panels and card weekly rollups for separate reconciliation.
- **Card ledger:** one purchase expense + credit-card payable; one card repayment is bank cash out + card liability decrease, without expense duplication.
- **Balances:** source opening balance + posted monetary movements = calculated balance. Explain any mismatch against independently supplied bank/card statement.
- **Savings:** income less expenses; separate reported "saved" values from recomputed values, track differences, and exclude transfers/card payments.
- **FX:** store original sent AED, received BRL, fees and actual execution rate if evidence exists; otherwise flag the missing settlement leg.
- **Forecast:** compute future recurring/instalment obligations from verified events and current statuses, never from broken formula results.

## 6. Traceability and FVT extension

| Existing ID | Additional workbook-informed acceptance criterion |
| --- | --- |
| UC-013 / FVT-LEGACY-009 | Stage and bulk-review synthetic rows with a mix of F/P flags, card aliases, category/class, missing dates and OK states. Saving a draft is non-posting; confirming creates only approved ledger entries. |
| UC-014 / FVT-LEGACY-010 | Exercise a multi-period card bill where itemized card purchases and next-month account payment coexist; assert no double-count, correct payable and opening carryover, support partial settlement. |
| UC-015 / FVT-LEGACY-012 | Verify BRL and AED reporting separately, two-category dimensions, real monthly savings, and actual vs 70/30-style configurable target comparisons. A prior cash balance shall not count as monthly income. |
| UC-016 / FVT-LEGACY-011 | Exercise UAE → Brazil remittance and FX fee while retaining original-currency balances and showing incomplete transfer settlement as pending. |
| UC-018 / FVT-LEGACY-013 | Discover 34-sheet structural families including hidden sheets, detect error cells and historical ambiguities, preserve source provenance, preview and explicitly approve, re-import to confirm idempotency. |

### Reference-safe fixtures

Build verification fixtures using **synthetic** or sufficiently anonymized records only:
- mixed Brazilian expenses and UAE card purchases;
- two fictional card accounts with weekly charges and next-cycle settlement;
- recurring F expense and P installment;
- intentional #REF! and #VALUE! spreadsheet summary cells;
- source missing dates and ambiguous account codes;
- prior balance vs earned income separation;
- remittance with explicit AED/BRL leg, FX fee, and asynchronous settlement.

Never use live source descriptions, merchant/payee labels, actual card identifiers, bank values, amounts or source workbook URL in CI fixtures.

## 7. UX implications / acceptance

Preferred Financial operational screens:

1. **Weekly Review:** grouped by account/card, date range and status. Inline editable merchant/description, amount, source, category and spending class. Show staged, invalid, possible duplicate, approved, and statement-mismatch states.
2. **Card Statements:** per-card issued/remaining/payable amounts, cycle close and payment dates, last-month carryover, credits and installments.
3. **Budget & Savings:** actual vs planned; expected vs realized; **separate** expense category, intent class and country; one-to-five-year forecast assumptions traceable back to source events.
4. **Migration Preview:** source sheet inventory, proposed mapping, flagged bad formulas, ambiguous F/P/L and account aliases, calculated-versus-source reconciliation, privacy banner and confirm/rollback controls.

### Next evidence gate

Candidate mappings need a **preview validation run with the user's approval** before production import. No automated debit/credit bank integration is implied by accessing a Google Sheet. Account naming and card-alias linking should be completed inside the private Legavia app, not in repository documentation. Maintain navigation under **Life → Financial**; do not add a sixth primary application tab.
