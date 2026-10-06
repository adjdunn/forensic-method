# F2: Working capital

## 0. Header

```
ID:        F2
Name:      Working capital
Question:  Are receivables, contract assets, inventory, payables and accruals moving in line with the business, and where they are not, what explains it?
Runs:      After F1. Its ledger feeds F5.
Needs:     P1 statements workbook (IS_Q, BS_Q, CF_Q, NOTES, and for IFRS reporters PROVISIONS and PROVISION_MATRIX); context-sheet.md from F1; the receivables, revenue, inventory, payables and supplier-finance note files
Returns:   Computation tables and ledger rows. Save the CSV as ledger-F2.csv.
Checklist: A1 to A18, C18.
```

## 1. Purpose

Working capital is where revenue recognised too early, costs held on the balance sheet, and reserves released to meet a number leave a residue a ratio can surface. This step computes every working-capital measure on two conventions, compares each quarter with the same quarter a year earlier, pairs the accounts that move together, and turns the unusual movements into candidates with a benign reading first. It does not compute accrual totals or screens (F3) or read the notes for changes in wording beyond the searches named here (F4).

{{RULES}}

## 3. Inputs

1. Attach and read `context-sheet.md` first. If it is not attached, say so, then run F1's method steps 1, 3 and 4 in brief (basis, acquisitions and disposals, accounting changes) before continuing, and mark the output "context sheet not attached, abbreviated check run".
2. Read the statements workbook. List the quarters available. List every line this step needs that is blank, and which checklist rows that disables.
3. If the context sheet reports a tie-out failure on a line this step uses, carry the warning into every row that uses that cell.

## 4. Method

All ratios are computed in code over the workbook. Use these conventions throughout and state them in the output:
- **Days** means the actual number of days in the fiscal quarter, or 365 for a year (366 in a leap year).
- **Ending** uses the period-end balance. **Average** uses (opening + closing) ÷ 2.
- **Growth** is same fiscal quarter, year over year.
- **Cost of goods sold** means the income-statement line. For an IFRS company that presents expenses by nature (the manifest says so), there is no such line: use "Inventories recognized as expense" from NOTES wherever this prompt says COGS, and say so in the header.
- **IFRS interims:** IAS 34 does not require contract balances or most note rollforwards in interim reports. Where a quarterly input is absent for an IFRS company, run the item on annual figures and say so.

1. **Receivables (A1, A2, A3, A4).**
   - DSO ending = Trade receivables, net ÷ Revenue × days. DSO average = average Trade receivables, net ÷ Revenue × days. DSO gap = ending minus average.
   - Receivables growth minus revenue growth, using gross receivables (net plus the allowance) so the allowance cannot mask the movement.
   - Allowance rate = Allowance ÷ gross receivables. Write-off coverage = write-offs ÷ provision, from the allowance rollforward in NOTES.
   - Read the allowance or credit-loss note for the current and prior year. Record any change in method, segmentation or the factors named.
   - US GAAP: the CECL rollforward is required for trade receivables, but an aging table usually is not, so past-due concentration has to be inferred from the allowance rate and write-offs.
   - IFRS: the loss-allowance reconciliation is in the credit-risk note (IFRS 7 paragraph 35H), and changes in estimation techniques and their reasons are in paragraph 35G(c); read that paragraph for A4. Many companies also give a provision matrix by past-due band (paragraphs 35M and 35N). Where the PROVISION_MATRIX sheet has one, compute, for each band, the gross amount's share of total and the expected loss rate, year over year. A falling loss rate in the oldest bands while those bands grow is the adverse pattern; improved collection experience, if the company describes it, is the benign reading.

2. **Contract balances and revenue timing (A5, A6, A8).**
   - Contract-asset intensity = Contract assets ÷ (Trade receivables, net + Contract assets). Contract-asset growth minus revenue growth.
   - Revenue recognized from obligations satisfied in prior periods, from NOTES, as a share of revenue, by period.
   - Search the revenue note and MD&A for: bill-and-hold, bill and hold, held for customer, customer requested, delivery at a later date, consignment, right of return, extended payment terms, early shipment, pull forward. Quote each hit with its locator.

3. **Receivable transfers (A7).** Search all text for: factor, securitiz, securitis, sale of receivables, sold receivables, derecogni, transferred financial assets, supply chain finance, supplier finance. For each programme found, record whether the receivables were derecognized. Where the derecognized amount is disclosed, recompute DSO ending with that amount added back, and report the difference.
   - IFRS: the derecognition test is different (IFRS 9 looks at risks and rewards first, then control). Receivables transferred but not derecognized stay in receivables with an associated liability (IFRS 7 paragraph 42D), which raises DSO rather than lowering it. A clean sale with no continuing involvement produces no transfer table at all, so the only trace may be in the liquidity discussion of the MD&A; search it.

4. **Inventory (A9 to A13).**
   - DIO ending = Inventory, net ÷ Cost of goods sold × days. DIO average likewise. Inventory growth minus COGS growth.
   - Component shares: raw materials, work in process and finished goods as shares of gross inventory, and the growth of each. If the company reports a single inventory line with no components, record that as a finding under A11.
   - Reserve rate = inventory reserve ÷ gross inventory. Write-down intensity = write-downs ÷ COGS.
   - Pair gross margin change with DIO change, same quarter year over year.
   - US GAAP with LIFO: LIFO reserve change ÷ COGS, and any LIFO liquidation effect ÷ pre-tax income.
   - IFRS: LIFO is not permitted, so skip the LIFO items and say so. IAS 2 does not fix the inventory classes, so the component split may follow the company's own categories; record them as given. IAS 2 requires write-downs and their reversals to be disclosed every year, and a reversal is required when circumstances change and reduces cost of sales. Compute reversal intensity = reversals ÷ COGS alongside write-down intensity. Where gross margin rises in a year with a reversal, quote the circumstances the company gives for it (IAS 2 paragraph 36(g)); the reversal is the benign reading and the size of the net realizable value judgment behind it is the adverse one.

5. **Payables, supplier finance and accruals (A14 to A17, C18).**
   - DPO ending and average = Trade payables ÷ COGS × days. If the change in inventory in a period exceeds 10 percent of that period's COGS, compute DPO on purchases (COGS plus change in inventory) as well, and say which you used.
   - Payables growth minus COGS growth.
   - Supplier finance, US GAAP: SCF share = confirmed obligations ÷ trade payables; DPO excluding confirmed obligations; and, where the rollforward exists, obligations added minus settled, compared with cash from operations for the same period.
   - Supplier finance, IFRS (IAS 7 paragraph 44H, from 2024): there is no rollforward of added and settled. Compute SCF share = programme liabilities ÷ trade and other payables; bank-funded share = amount already paid by finance providers ÷ programme liabilities; term extension = midpoint of the programme's range of payment due dates minus the midpoint of the comparable trade payables' range, in days; net change in the programme = closing − opening − non-cash changes. DPO excluding programme liabilities as for US GAAP.
   - Accrued-liability intensity = Accrued liabilities ÷ revenue. Under IFRS, accruals are often reported inside trade and other payables and cannot be isolated; say so if that is the case.
   - Reserve releases. From each rollforward in NOTES, identify reductions that are not payments (releases, reversals, adjustments) and compute them as a share of pre-tax income for that period. IFRS: IAS 37 requires a rollforward for every class of provision, with "unused amounts reversed" on its own line; from the PROVISIONS sheet compute release rate = unused amounts reversed ÷ opening balance, by class and year, and total releases ÷ pre-tax income. Comparatives are not required in that note, so the series needs one annual report per year.
   - Year-end pattern (C18): does DPO or the payables balance rise at the fiscal year end and fall in the next quarter, in more than one year?
   - Search for: rebate, allowance, vendor consideration, supplier consideration, upfront payment, prebate, volume incentive. Quote how the company describes accounting for supplier consideration (A17).

6. **Cash-conversion cycle (A18).** DSO plus DIO minus DPO, all ending, then all average. Report the three components beside the total, never the total alone.

7. **Pairings.** Look for these combinations in the same quarter. Each one found is evidence for a P2 row if the context sheet does not explain it:
   - receivables up faster than revenue while inventory falls faster than COGS (the shape of goods billed but not shipped);
   - DSO ending rising faster than DSO average in the last quarter of the fiscal year (quarter-end loading);
   - gross margin up while DIO rises (costs held in inventory);
   - allowance rate falling while DSO rises;
   - DPO rising while the supplier-finance share rises.

8. **Check each candidate against the context sheet.** For every candidate, look up the comparability map for that line and period. If an event explains it, the row is P4 and cites the event. Otherwise assign P1 to P3 by the ledger rules.

## 5. Judgment notes

- The ending-balance figure is the one that shows a quarter-end problem. The average figure dilutes it by half. A widening gap between the two at year end is itself a signal.
- A seasonal business must be compared with the same quarter a year earlier. Sequential comparisons in a seasonal business manufacture signals.
- Receivables growing faster than revenue has many ordinary causes: longer terms for a new customer mix, an acquisition, a large order late in the quarter. The benign reading comes first because it is usually right.
- Inventory in dollars rises with input prices. Before reading a DIO increase as volume, check whether costs rose.
- A falling DPO is not a problem; a rising one can be cash borrowed from suppliers. The supplier-finance disclosure tells you whether a bank is standing behind the stretch.
- A single inventory line is the company's assertion that a component split is impracticable. It is a finding, not a gap.
- The strongest signal in this step is usually a combination, not a ratio. Report the pairings even when no single ratio triggers a row.
- IFRS gives the analyst more than US GAAP in two places: a provision matrix for receivables, and a rollforward for every provision with releases on their own line. Use them. It gives less in two others: no supplier-finance rollforward, and fewer quarterly notes.

## 6. Output

**Title:** Working capital: [company], [first period] to [last period]

1. **Header line.** Company, framework, currency and units, periods, conventions used.
2. **Summary.** Number of items run, number of rows by priority, and the P1 and P2 rows in one line each. No conclusions.
3. **Computation tables.** Periods across the columns, oldest to newest; items down the rows; a formula column. One table each for: Receivables; Contract balances; Inventory; Payables, supplier finance and accruals; Cash-conversion cycle.
4. **Text found.** Each quoted hit from the searches in steps 2, 3, 5 and 1, with its locator.
5. **Pairings.** Each pairing found, with the quarter and the figures.
6. **Ledger rows.**

{{LEDGER}}

{{CLOSE}}

## 9. Self-check before returning

- [ ] Every ratio was computed in code, and the code is shown.
- [ ] Every comparison is same quarter year over year, and the output says so.
- [ ] Every ledger row has a benign reading written before its adverse reading.
- [ ] Every row was checked against the comparability map, and P4 rows cite the event.
- [ ] Every "not disclosed" statement lists the files and terms searched.
- [ ] Units and scale are stated in the header and match the workbook.
- [ ] No sentence concludes that anything is wrong.
