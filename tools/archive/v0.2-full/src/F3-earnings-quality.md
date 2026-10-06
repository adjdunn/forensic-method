# F3: Earnings quality and accruals

## 0. Header

```
ID:        F3
Name:      Earnings quality and accruals
Question:  How much of reported earnings is backed by cash, what do the published screens say and which accounts drive them, and do the adjusted measures, capitalization and estimates move earnings in ways the business does not explain?
Runs:      After F1. Its ledger feeds F5.
Needs:     P1 statements workbook (all sheets, including IS_A, BS_A, CF_A and NONGAAP); context-sheet.md; earnings releases; PP&E, intangibles, interest, contract-cost and provisions note files
Returns:   Computation tables, the screens with each component, and ledger rows. Save the CSV as ledger-F3.csv.
Checklist: B1 to B7, C1 to C8, C17, C19.
```

## 1. Purpose

Earnings that run ahead of cash, adjustments that recur, costs moved onto the balance sheet and estimates that drift in the flattering direction are the core of earnings quality. This step measures each one, runs the two best-known published screens with every component shown, and traces any high score back to the account that produced it. The screens rank where to read. They never conclude. This step does not compute working-capital ratios (F2) or diff the notes year over year (F4).

{{RULES}}

## 3. Inputs

1. Attach and read `context-sheet.md` first. If it is not attached, say so, then run F1's method steps 1, 3 and 4 in brief before continuing, and mark the output "context sheet not attached, abbreviated check run".
2. Read the workbook. The screens need at least three consecutive fiscal years of annual statements. List any missing line and which items it disables.
3. Read the framework. IFRS changes steps 1, 2 and 5 as described in each step.

## 4. Method

All computations in code. Average total assets = (opening + closing) ÷ 2.

1. **Accruals (B1, B2, B3).**
   - Cash-flow accruals = (Income from continuing operations − Cash from operations) ÷ average total assets, for each fiscal year and for each trailing four quarters.
   - Balance-sheet accruals (Sloan form) = [(Δ Total current assets − Δ Cash and equivalents) − (Δ Total current liabilities − Δ Current portion of long-term debt − Δ Income taxes payable) − Depreciation and amortization] ÷ average total assets.
   - Reconcile the two. A gap is expected in any period with an acquisition, disposal, discontinued operation or large currency effect, because balance-sheet changes then include items that never passed through income. Check the context sheet. A gap with no event to explain it is a candidate.
   - Decomposition (B3): ΔWC = Δ[(Total current assets − Cash − Short-term investments) − (Total current liabilities − Current portion of long-term debt)]; ΔNCO = Δ[(Total assets − Total current assets − Long-term investments and advances) − (Total liabilities − Total current liabilities − Long-term debt)]; ΔFIN = Δ[(Short-term investments + Long-term investments) − (Long-term debt + Current portion of long-term debt + Preferred stock)]. Each ÷ average total assets. Report which component drives the total.
   - IFRS: until IFRS 18 (annual periods from 1 January 2027), IAS 7 lets a company classify interest paid as operating or financing, interest and dividends received as operating or investing, and dividends paid as operating or financing. From IFRS 18, non-financial companies must put interest paid in financing and interest and dividends received in investing. IFRS 16 puts lease principal payments in financing. Each of these lifts reported cash from operations relative to a US GAAP company with the same cash flows.
   - For every IFRS reporter, compute **US-basis cash from operations** = reported cash from operations − interest paid classified in financing + interest received and dividends received classified in investing + dividends paid classified in operating − lease principal payments. State that the last term treats every IFRS 16 lease as a US operating lease, which overstates the adjustment for leases that would be finance leases under US GAAP. Compute cash-flow accruals, TATA and the step 7 ratios on both reported and US-basis cash from operations, and report both.
   - For an IFRS reporter, "income before extraordinary items" is profit or loss, because IFRS prohibits extraordinary items.

2. **Beneish M-score (B4).** For each pair of consecutive fiscal years. Year t is the later year.
   - DSRI = (Trade receivables_t ÷ Revenue_t) ÷ (Trade receivables_t−1 ÷ Revenue_t−1)
   - GMI = Gross margin_t−1 ÷ Gross margin_t, where gross margin = (Revenue − COGS) ÷ Revenue
   - AQI = [1 − (Total current assets_t + PP&E, net_t) ÷ Total assets_t] ÷ [1 − (Total current assets_t−1 + PP&E, net_t−1) ÷ Total assets_t−1]
   - SGI = Revenue_t ÷ Revenue_t−1
   - DEPI = [Dep_t−1 ÷ (Dep_t−1 + PP&E, net_t−1)] ÷ [Dep_t ÷ (Dep_t + PP&E, net_t)], where Dep is depreciation excluding amortization of intangibles
   - SGAI = (SG&A_t ÷ Revenue_t) ÷ (SG&A_t−1 ÷ Revenue_t−1)
   - LVGI = [(Long-term debt_t + Total current liabilities_t) ÷ Total assets_t] ÷ [same for t−1]
   - TATA = (Income from continuing operations_t − Cash from operations_t) ÷ Total assets_t
   - M = −4.840 + 0.920·DSRI + 0.528·GMI + 0.404·AQI + 0.892·SGI + 0.115·DEPI − 0.172·SGAI + 4.679·TATA − 0.327·LVGI
   - Report M, each index, and each index's contribution (coefficient × index). The cutoff is −1.78. Report whether M is above it and which contributions are largest.
   - Conventions to state in the output, every time, because they change the score: TATA uses the cash-flow form; right-of-use assets are added to PP&E, net for AQI and DEPI, and right-of-use depreciation to depreciation for DEPI, for both frameworks; non-current lease liabilities are added to long-term debt for LVGI. For an IFRS reporter, compute the score on reported and on US-basis cash from operations from step 1.
   - Nature-of-expense IFRS reporters have no cost-of-sales or SG&A line. Use "Inventories recognized as expense" as the cost figure in GMI, set SGAI to 1, and say so.
   - IFRS 16 moves lease costs out of cost of sales and SG&A into depreciation and interest, so GMI and SGAI for an IFRS reporter are not comparable in level with a US GAAP company, and they shift in the adoption year.
   - If the context sheet shows a lease-standard adoption, an acquisition or a disposal between t−1 and t, say that the M-score for that pair compares non-comparable years.
   - Set AQI to 1 when its prior-year denominator is zero. Set DEPI or SGAI to 1 when the line is blank, and say so.

3. **Dechow F-score (B5).** For each fiscal year with three consecutive year-ends available.
   - RSST accruals = (ΔWC + ΔNCO + ΔFIN) ÷ average total assets, from step 1
   - ΔREC = Δ Trade receivables ÷ average total assets
   - ΔINV = Δ Inventory ÷ average total assets
   - Soft assets = (Total assets − Cash and equivalents − PP&E, net) ÷ Total assets
   - ΔCash sales = percentage change in (Revenue − Δ Trade receivables)
   - ΔEarnings = Income from continuing operations_t ÷ average total assets_t − Income from continuing operations_t−1 ÷ average total assets_t−1
   - Issuance = 1 if Stock issued > 0 or Debt issued > 0 in year t, else 0
   - Logit = −7.893 + 0.790·RSST + 2.518·ΔREC + 1.191·ΔINV + 1.979·Soft assets + 0.171·ΔCash sales − 0.932·ΔEarnings + 1.029·Issuance
   - Enter every ratio and change as a decimal (0.10 for 10 percent), not as a percentage.
   - Probability = e^logit ÷ (1 + e^logit). F-score = Probability ÷ 0.0037.
   - Report the F-score, the probability, and each term's contribution. The cutoffs are 1.0, 1.85 and 2.45. State that the unconditional probability of 0.0037 is the published version's figure as quoted in later work, and that the working-paper version used 0.00345.
   - If Issuance = 0, say that a company that raised no capital scores lower on this model by construction.

4. **Localize (B6, B7).**
   - Cash sales: percentage change in (Revenue − Δ Trade receivables), each fiscal year. Rising cash sales in a year of high accruals is consistent with quarter-end loading, which accrual measures miss.
   - For each screen above its cutoff, name the one or two largest contributions and map them: DSRI or ΔREC to receivables and revenue recognition (F2 A1 to A8); GMI or ΔINV to cost of sales and inventory (F2 A9 to A13); AQI, soft assets or ΔNCO to capitalized costs and intangibles (step 6 here); DEPI to useful lives (step 6); TATA or RSST to the accrual components in step 1.

5. **Adjusted measures (C1 to C4).** From the NONGAAP sheet and the releases.
   - The gap between each GAAP measure and its adjusted counterpart, as a share of revenue, for every quarter.
   - A presence matrix: each reconciling category down the rows, each quarter across the columns, marked present or absent. A category present in five or more of the last eight quarters is labelled recurring. A category appearing for the first time is labelled new.
   - For each new category, and each change in a measure's definition, search the releases for an explanation and a recast of prior periods. Quote it or record it as not found.
   - Prominence: in each release, is the GAAP measure present in the headline and the first paragraph, and is it presented before the adjusted measure? Record the first 60 words of each release's opening.
   - Stock-based compensation added back, as a share of GAAP operating income, by quarter.
   - Regimes, from the manifest:
     - US: Regulation G and Item 10(e) of Regulation S-K. In filed documents, Item 10(e) prohibits adjusting out a charge labelled non-recurring if a similar charge occurred in the prior two years or is reasonably likely in the next two.
     - Canada: National Instrument 52-112, in force since August 2021. It requires the same prominence and reconciliation, but its two-year rule restricts only the label: a company may adjust out a recurring charge as long as it does not call it non-recurring, unusual or infrequent. For a Canadian filer, the C2 test is the label, not the adjustment. NI 52-112 also requires an explanation when a measure's label or composition changes.
     - IFRS reporters from annual periods beginning 1 January 2027: IFRS 18 puts management-defined performance measures in an audited note, reconciled to the nearest IFRS subtotal with the tax and non-controlling-interest effect of each item, and requires restated comparatives when a measure's calculation changes. EBITDA defined simply as operating profit before depreciation, amortization and impairment is a listed subtotal, not a management measure; an "adjusted EBITDA" is. From 2027, take the reconciliation from the audited note.

6. **Capitalization and estimates (C5 to C8).**
   - Depreciation ÷ average PP&E, gross, by year. Capital expenditures ÷ depreciation.
   - Capitalized software or development costs, and capitalized contract costs: growth compared with revenue growth.
   - IFRS: IAS 38 requires development costs to be capitalized once all six of its criteria are met, so capitalized development is normal and its level is not a signal. Compute the **capitalization share** = additions from internal development ÷ (additions from internal development + research and development expensed), and amortization of internally generated intangibles ÷ those additions, by year. The signal is a rising share without a described change in the project portfolio, or amortization lagging additions. Compare with the company's own history, not with US companies.
   - IFRS: if the manifest shows PP&E on the revaluation model, depreciation includes the effect of revaluations; say so before reading the depreciation ratios.
   - Interest capitalized ÷ interest incurred, by year, alongside the construction-in-progress balance if disclosed.
   - Search the PP&E, intangibles and policy notes for: useful life, useful lives, residual value, salvage, estimated life, depreciation method, change in estimate. Quote each statement of lives or residual values for each year.
   - C6: search for "change in estimate" and "change in accounting estimate" near reserves, provisions, allowances or accruals. Quote each hit. IFRS (IAS 8) requires the nature and amount of a change in estimate to be disclosed without the US exemption for ordinary-course estimates, so an IFRS reporter should disclose more of these; a reserve release with no such disclosure is itself worth a row.

7. **Cash flow comparisons (C17, C19).**
   - For each fiscal year and trailing four quarters: Cash from operations ÷ Income from continuing operations; Free cash flow ÷ Income from continuing operations, where free cash flow = Cash from operations − Capital expenditures − Capitalized software or development costs; Capital expenditures ÷ depreciation.
   - Cash from operations to income does not catch costs that were capitalized, because capitalizing moves the cash outflow into investing. Free cash flow to income does. Report both, and say which moved.
   - Search the cash-flow policy note and the notes for: collections on beneficial interests, deferred purchase price, securitization, interest paid, taxes on the gain, classified as operating, classified as financing. Record any classification choice that moves cash from operations.

8. **Check each candidate against the context sheet**, as in the ledger rules.

## 5. Judgment notes

- The screens were estimated on US companies reporting under US GAAP, before IFRS 16 and ASC 842. No published study has tested them on Canadian IFRS reporters; the closest evidence is small Polish samples, one of which found a different cutoff worked best. On an IFRS reporter, and in any year straddling a lease-standard adoption, treat the score as descriptive only and say so.
- A score is a base-rate multiplier. At the published cutoffs, both screens produce more than 100 false flags for every true one on SEC enforcement data. The value is in the components, which tell the analyst which account to read.
- Two schemes in the SEC record inflated cash from operations along with income, so a healthy ratio of cash to earnings is not a clean bill. Free cash flow and the capitalization ratios are the check.
- A non-GAAP category that recurs is not the problem by itself; many companies restructure every year. The questions are whether the company still calls it non-recurring and whether the size is growing.
- A change in useful lives or residual values is accounted for prospectively. The prior years are not restated, so the depreciation series breaks silently. The disclosure is often a single sentence.
- Stock-based compensation has no rule against adding it back. Report its size; do not characterize it.

## 6. Output

**Title:** Earnings quality and accruals: [company], [first period] to [last period]

1. **Header line.** Company, framework, currency and units, periods, the conventions from steps 1 and 2.
2. **Summary.** Items run, rows by priority, the P1 and P2 rows in one line each. No conclusions.
3. **About the screens.** Reproduce this paragraph exactly: "The M-score and F-score rank companies for reading time. On SEC enforcement releases issued from 1982 to 2016, an M-score above −1.78 produced about 130 false flags for every true one, and an F-score above 1.0 about 108 (Beneish and Vorst, The Accounting Review, 2022, Table 2). Both were estimated on US companies reporting under US GAAP. A score above the cutoff is a reason to read the accounts it points to, not evidence about this company."
4. **Computation tables.** Periods across the columns. One table each for: Accruals and decomposition; M-score with each index and contribution; F-score with each term and contribution; Localization; Adjusted-measure gap and presence matrix; Capitalization and estimates; Cash-flow comparisons.
5. **Text found.** Each quoted hit from steps 5, 6 and 7, with its locator.
6. **Ledger rows.**

{{LEDGER}}

{{CLOSE}}

## 9. Self-check before returning

- [ ] The "About the screens" paragraph appears exactly as written.
- [ ] Every index and term is shown, not only the scores.
- [ ] The conventions for TATA, AQI and LVGI are stated.
- [ ] Every year pair that straddles an event on the context sheet is labelled non-comparable.
- [ ] For an IFRS reporter, accruals, TATA and the cash-flow ratios are shown on both reported and US-basis cash from operations.
- [ ] Every computation was done in code, and the code is shown.
- [ ] Every ledger row has a benign reading before its adverse reading.
- [ ] No sentence says a score shows anything about the company beyond where to read.
