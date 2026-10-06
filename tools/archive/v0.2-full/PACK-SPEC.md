# The company pack

What the prompts expect to find. We build packs in the back office; attendees receive them ready. One pack per company.

## Files

| ID | File | Contents | Needed by |
|---|---|---|---|
| P0 | `manifest.md` | Company name, reporting framework (US GAAP or IFRS, taken from the basis-of-preparation note, never assumed from the listing), expense presentation (by function or by nature), PP&E measurement model (cost or revaluation), non-GAAP regime, audit standard (PCAOB, CAS or ISA), currency, units, fiscal year end, periods covered, the file list with IDs, and known limits of the pack | All |
| P1 | `statements.xlsx` | The statement workbook, below | F1, F2, F3, F4 |
| P2 onward | Text files, one per filing section | Below | F1, F3, F4 |
| | `releases/ER-<period>.txt` | Earnings releases, including the non-GAAP reconciliation tables as text | F1, F3, F5 |
| | `proxy/PROXY-<year>.txt` | Compensation sections of the proxy statement or management information circular | F5 |
| | `events.txt` | Current reports that matter: auditor changes, non-reliance, restatements, material changes. US: 8-K Items 4.01 and 4.02. Canada: NI 51-102 section 4.11 change-of-auditor reporting packages, section 11.5 re-filing or restatement news releases, and material change reports | F1 |
| | `consensus.csv` (optional) | Consensus revenue and EPS by quarter, supplied by the analyst, with its source. Tier 5 | F5 |

The manifest assigns every file an ID (P2, P3 ...) and the prompts cite by ID.

## The statement workbook

Periods run across the columns, oldest to newest. Line items run down the rows, using the names below exactly. A line the company does not report is left blank, not zero.

| Sheet | Periods | Contents |
|---|---|---|
| `IS_Q`, `BS_Q`, `CF_Q` | Twelve fiscal quarters | Income statement, balance sheet, cash flow. Cash flow is discrete quarters, not year-to-date. A fourth quarter derived as annual minus nine months is marked in `LOCATORS` |
| `IS_A`, `BS_A`, `CF_A` | Five fiscal years | Same, annual |
| `NOTES` | Quarterly where disclosed, else annual | Note data, below |
| `NONGAAP` | Twelve quarters | Each reconciling line between the GAAP measure and each non-GAAP measure, with the company's own labels. From 2027, IFRS reporters' management-defined performance measures come from the audited note |
| `RESTATED` (optional) | Five fiscal years | The prior-year comparative column as printed in each later annual report, for the main annual lines. The `_A` sheets hold figures as originally reported, so F1 can compare the two and find corrections the company did not label |
| `PROVISIONS` | Fiscal years | IFRS: the IAS 37 paragraph 84 reconciliation for every class of provision: opening, additions, used, unused amounts reversed, unwinding of discount, closing |
| `PROVISION_MATRIX` | Year-ends | IFRS: the credit-loss provision matrix by past-due band, where the company gives one |
| `LOCATORS` | | One row per filled cell: sheet, line, period, source file ID, page or note, and "derived" where the value is computed from other reported values |

### Line names

**Income statement:** Revenue; Cost of goods sold; Gross profit; Selling, general and administrative; Research and development; Depreciation (excluding amortization of intangibles); Amortization of intangibles; Restructuring and other charges; Operating income; Interest expense; Interest income; Other income (expense); Pre-tax income; Income tax expense; Income from continuing operations; Discontinued operations; Net income; Diluted shares; Diluted EPS.

**Balance sheet:** Cash and equivalents; Short-term investments; Trade receivables, net; Allowance for credit losses; Contract assets; Inventory, net; Other current assets; Total current assets; PP&E, gross; Accumulated depreciation; PP&E, net; Right-of-use assets; Goodwill; Intangible assets, net; Capitalized software or development costs; Capitalized contract costs; Long-term investments and advances; Other non-current assets; Total assets; Trade payables; Supplier finance obligations (if presented separately); Accrued liabilities; Contract liabilities; Provisions, current (IFRS); Income taxes payable; Current portion of long-term debt; Current lease liabilities; Total current liabilities; Long-term debt; Non-current lease liabilities; Provisions, non-current (IFRS); Other non-current liabilities; Total liabilities; Preferred stock; Common equity; Non-controlling interests; Total equity.

**Cash flow:** Net income; Depreciation and amortization; Stock-based compensation; Change in receivables; Change in inventory; Change in payables; Change in accrued liabilities; Change in contract balances; Other operating changes; Cash from operations; Capital expenditures (PP&E); Capitalized software or development costs; Acquisitions, net of cash; Proceeds from disposals; Cash from investing; Debt issued; Debt repaid; Stock issued; Stock repurchased; Dividends paid; Lease principal payments; Cash from financing; Interest paid; Interest paid classified in (Operating / Financing); Interest received; Interest received classified in (Operating / Investing); Dividends received; Dividends received classified in (Operating / Investing); Dividends paid classified in (Operating / Financing); Income taxes paid; Effect of exchange rates; Net change in cash.

**Lessors and rental companies** (car and equipment rental, leasing) carry their main operating asset outside PP&E. Record it on these lines, and leave PP&E for the company's other property: Balance sheet: Equipment held for rental or lease, gross; Accumulated depreciation, equipment held for rental or lease; Equipment held for rental or lease, net. Income statement: Depreciation of equipment held for rental or lease. Cash flow: Purchases of equipment held for rental or lease; Proceeds from disposal of equipment held for rental or lease.

**EXTRA sheet.** Any line on the face of the statements that does not map to a line above goes on a sheet named `EXTRA`, with the company's own label, the statement it came from, and the same period columns. Nothing on the face of the statements is dropped.

**Signs.** Income-statement expenses are positive numbers. Cash-flow lines carry the sign shown in the statement (outflows negative).

A company that presents expenses by nature (permitted under IFRS) has no cost-of-sales or SG&A line. Leave those blank and fill "Inventories recognized as expense" in NOTES from the inventory note (IAS 2 paragraph 36(d)); the prompts use it as the cost figure.

**NOTES:** Allowance: opening, provision, write-offs, recoveries, other, closing. Credit-loss provision matrix (IFRS 7 paragraphs 35M and 35N, where given): gross amount and expected loss rate by past-due band, as a small table. Inventory: raw materials, work in process, finished goods, supplies, reserve or write-down allowance, write-downs recognized, reversals of write-downs (IFRS), inventories recognized as expense (IFRS). LIFO reserve; LIFO liquidation effect. Supplier finance: confirmed obligations outstanding, added and settled (US), paid by finance providers (IFRS), non-cash changes (IFRS), payment terms text, range of payment due dates (IFRS). Trade payables: range of payment due dates (IFRS, for comparison with the programme). Receivables derecognized (sold or factored), amount outstanding; receivables transferred but not derecognized, and the associated liability (IFRS). Interest incurred; interest capitalized. Leases: depreciation of right-of-use assets; interest on lease liabilities. Warranty: opening, accruals, changes for pre-existing, payments, closing. Restructuring: opening, charges, payments, adjustments, closing. Provisions by class (IFRS): opening, additions, used, reversed unused, unwinding of discount, closing. Revenue from obligations satisfied in prior periods. Revenue recognized from opening contract liabilities. Development: additions from internal development, research and development expensed, amortization of internally generated intangibles (IFRS). Employees at year end.

## Text files

One file per section per filing, named `<filing>_<section>.txt`, for example `AR-FY2025_risk-factors.txt` or `Q3-FY2025_notes-07-receivables.txt`. Page markers from the original document are kept inline as `[p. 45]`.

Standard section keys, so the delta step can pair them across years:

| Key | US 10-K | Canadian IFRS filer |
|---|---|---|
| `business` | Item 1 | Annual information form, business section |
| `risk-factors` | Item 1A | AIF risk factors (Form 51-102F2 item 5.2), or the MD&A risks section for a venture issuer with no AIF |
| `legal` | Item 3 | Legal proceedings in the AIF, plus the contingencies note |
| `mdna` | Item 7 | The MD&A document |
| `critical-estimates` | The critical accounting estimates part of Item 7 | Two files: the MD&A's critical accounting estimates (Form 51-102F1 item 1.12, non-venture issuers), and the judgments and estimation-uncertainty note (IAS 1 paragraphs 122 and 125), keyed `critical-estimates-note` |
| `market-risk` | Item 7A | Financial instruments and risk management in the MD&A |
| `auditor-report` | The audit report, with CAMs | The audit report, with key audit matters |
| `controls` | Item 9A | Disclosure controls and ICFR in the MD&A |
| `notes-NN-title` | Each note to the financial statements | Each note |
| `related-parties` | Related-party note and Item 13 | Related-party note |

## Why the pack is built this way

- One workbook with fixed line names lets every step run the same code on any company.
- `LOCATORS` keeps every number traceable to a page without putting sources in value cells.
- Section files let a step load two years of one section side by side instead of two whole annual reports, which is where long-document accuracy degrades.
- The pack carries no market data, so nothing in the pass depends on a data feed. Anything that needs a share price or consensus is reported as "Could not run" unless the analyst supplies it.
