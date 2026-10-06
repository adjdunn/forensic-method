# Working capital: Hertz Global Holdings, Inc., Q1 FY2011 to Q4 FY2013

## 1. Header

```
Company:      Hertz Global Holdings, Inc. (CIK 1364479) [P0, header table]
Framework:    US GAAP [P0, header table; context sheet, Basis]
Currency:     USD; P1 statements.xlsx in USD millions; text files in each filing's own units (thousands for the
              FY2011 and FY2012 10-Ks and the 10-Qs Q1 2011 to Q1 2013, millions for the FY2013 10-K and the
              Q2 and Q3 2013 10-Qs); every text figure used below was converted to USD millions in code [P0]
Fiscal year:  ends 31 December [P0]
Periods:      quarters Q1 FY2011 to Q4 FY2013 (year-over-year comparisons from Q1 FY2012);
              years FY2009 to FY2013 (year-over-year from FY2010) [P1, IS_Q, IS_A]
Conventions:  Days = actual days in the quarter (90, 91 or 92) or 365 for a year, 366 for FY2012 [calc].
              Ending = period-end balance; Average = (opening + closing) / 2; Q1 FY2011 opens on the FY2010
              balance in BS_A. Growth = same fiscal quarter (or year) one year earlier. Every percentage names
              its base in the Formula column.
Cost base:    The statements have no cost-of-goods-sold or gross-profit line [P0, "Known limits"]. This is a
              US GAAP filer, so the IFRS "inventories recognized as expense" substitute does not apply. Every
              ratio the prompt defines on COGS is therefore also computed on "Direct operating" expense
              [P1, EXTRA], the statement's main cost-of-service line, and labelled "direct-operating basis".
              These are substitutes, not the specified measures; the specified COGS measures are reported
              under "Could not run". Where the prompt pairs gross margin with DIO, a margin proxy is used:
              (Revenue - Direct operating - Depreciation of revenue earning equipment and lease charges) /
              Revenue [P1, IS and EXTRA].
Context:      context-sheet.md from F1 attached and used.
```

**Inputs.** Quarters available in P1: Q1 FY2011 to Q4 FY2013; years FY2009 to FY2013 [P1]. Lines this step needs that are blank in P1: Cost of goods sold and Gross profit (IS_Q, IS_A); Contract assets and Contract liabilities (BS); Supplier finance obligations (BS); Change in inventory and Change in contract balances (CF; inventory is combined with prepaid expenses in EXTRA "Inventories, prepaid expenses and other assets"); every NOTES inventory line (components, reserve, write-downs, reversals, LIFO); every NOTES supplier-finance line; Receivables derecognized and transferred; Revenue from obligations satisfied in prior periods; Revenue from opening contract liabilities; the NOTES restructuring and warranty lines (restructuring is taken from the note text instead); Allowance for credit losses FY2009 in BS_A (taken from NOTES closing instead) [P1]. Rows these disable: A5 and A6 entirely; A9, A10, A13 and A14 as specified (run on the direct-operating substitute); A11 components; A12; the LIFO parts of A13; A15; the DSO add-back in A7 [inf: P1, P0].

**Tie-out warnings carried** (from the context sheet): W4, every P1 cell for FY2009 to FY2012 and Q1 FY2011 to Q3 FY2013 is on the pre-revision basis (E4, E24), so FY2013 against FY2012 mixes bases; for that reason the annual tables add a "FY2012 as revised" column [P1, RESTATED; P68, p. 84; P86]. Q4 FY2013 income-statement lines are derived as corrected year minus uncorrected nine months, so Q4 FY2013 revenue, direct operating and fleet depreciation absorb the nine-month corrections (Read-first item 2). FY2010 accounts payable in P1 (945.0) is pre-E4 (954.3 as revised) and is the opening balance for Q1 FY2011 average DPO. W1 to W3 concern cash, treasury stock and EXTRA equity cells, none of which this step uses.

## 2. Summary

Checklist rows in scope: 19 (A1 to A18, C18). Run: 15, of which 5 (A9, A10, A13, A14, A18) only on the direct-operating substitute. Could not run: 4 (A5, A6, A12, A15). Ledger rows: 13 (P1 0, P2 1, P3 6, P4 6).

- P2, F2-A16-01: accrued liabilities / revenue fell to 10.26% in FY2013, lowest in FY2009 to FY2013 and down four years running, and the FY2013 balance sheet presents one accrued line where the FY2011 and FY2012 10-Ks presented two [calc; P66, p. 75; P37, p. 72].

No P1 rows.

## 3. Computation tables

Checklist mapping used (the checklist is not attached, so the split inside each step is an assumption): A1 DSO, A2 receivables against revenue growth, A3 allowance rate and write-off coverage, A4 allowance method; A5 contract-asset intensity, A6 revenue from prior-period obligations, A7 receivable transfers, A8 revenue-timing text; A9 DIO, A10 inventory against cost growth, A11 inventory components, A12 reserve and write-downs, A13 margin and DIO pairing and LIFO; A14 DPO and payables growth, A15 supplier finance, A16 accruals and reserve releases, A17 supplier consideration; A18 cash-conversion cycle; C18 year-end payables pattern [inf: prompt method steps 1 to 6].

All ratio values below are [calc]; rows marked "copied" are copied from the file named in the row.

### 3.1 Receivables (A1 to A4)

Quarterly:

| Item | Q1 2011 | Q2 2011 | Q3 2011 | Q4 2011 | Q1 2012 | Q2 2012 | Q3 2012 | Q4 2012 | Q1 2013 | Q2 2013 | Q3 2013 | Q4 2013 | Formula |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Revenue [P1, IS_Q] | 1,780.0 | 2,072.3 | 2,432.3 | 2,013.8 | 1,960.9 | 2,225.1 | 2,516.2 | 2,318.5 | 2,436.5 | 2,714.6 | 3,069.4 | 2,551.3 | copied |
| Receivables, net [P1, BS_Q] | 1,311.8 | 1,447.2 | 1,996.0 | 1,616.4 | 1,398.7 | 1,448.3 | 1,731.8 | 1,886.6 | 1,555.5 | 1,656.0 | 1,700.9 | 1,512.6 | copied |
| Allowance [P1, BS_Q] | 21.3 | 19.1 | 21.9 | 20.3 | 23.1 | 21.9 | 23.7 | 25.1 | 29.0 | 26.2 | 35.4 | 30.8 | copied |
| Days in quarter | 90 | 91 | 92 | 92 | 91 | 91 | 92 | 92 | 90 | 91 | 92 | 92 | calendar days |
| DSO ending (days) | 66.3 | 63.6 | 75.5 | 73.8 | 64.9 | 59.2 | 63.3 | 74.9 | 57.5 | 55.5 | 51.0 | 54.5 | Rec net ÷ Revenue × days |
| DSO average (days) | 67.5 | 60.6 | 65.1 | 82.5 | 70.0 | 58.2 | 58.1 | 71.8 | 63.6 | 53.8 | 50.3 | 57.9 | ((opening + closing) ÷ 2) ÷ Revenue × days |
| DSO gap (days) | -1.1 | 3.0 | 10.4 | -8.7 | -5.1 | 1.0 | 5.2 | 3.1 | -6.1 | 1.7 | 0.7 | -3.4 | ending − average |
| Revenue growth YoY (%) |  |  |  |  | 10.2 | 7.4 | 3.4 | 15.1 | 24.3 | 22.0 | 22.0 | 10.0 | Rev ÷ Rev same quarter prior year − 1 |
| Gross receivables growth YoY (%) |  |  |  |  | 6.7 | 0.3 | -13.0 | 16.8 | 11.4 | 14.4 | -1.1 | -19.3 | (net + allowance) ÷ same, prior year − 1 |
| Gross receivables growth minus revenue growth (pp) |  |  |  |  | -3.5 | -7.1 | -16.5 | 1.7 | -12.8 | -7.6 | -23.1 | -29.3 | difference of the two lines above |
| Allowance rate (%) | 1.60 | 1.30 | 1.09 | 1.24 | 1.62 | 1.49 | 1.35 | 1.31 | 1.83 | 1.56 | 2.04 | 2.00 | Allowance ÷ (net + allowance) |
| Fleet-disposal receivables [text, see note] | 387.6 | 264.0 | 949.8 | 620.7 | 299.6 | 178.4 | 504.9 | 617.3 | 230.7 | 118.8 | 391.0 | 357.3 | copied, converted to millions |
| Fleet-disposal receivables share of net receivables (%) | 29.5 | 18.2 | 47.6 | 38.4 | 21.4 | 12.3 | 29.2 | 32.7 | 14.8 | 7.2 | 23.0 | 23.6 | fleet-disposal ÷ Rec net |
| DSO ending excluding fleet-disposal receivables (days) | 46.7 | 52.0 | 39.6 | 45.5 | 51.0 | 51.9 | 44.9 | 50.4 | 48.9 | 51.5 | 39.3 | 41.7 | (Rec net − fleet-disposal) ÷ Revenue × days |
| Allowance rate excluding fleet-disposal receivables (%) | 2.25 | 1.59 | 2.05 | 2.00 | 2.06 | 1.70 | 1.90 | 1.94 | 2.14 | 1.68 | 2.63 | 2.60 | Allowance ÷ (gross − fleet-disposal) |

Annual (the last value column is FY2012 as revised in the FY2013 10-K: revenue, receivables [P1, RESTATED], allowance, provision and write-offs [P86, p. 158], cash-flow provision [P66, p. 80], fleet-disposal receivables [P66, p. 81]):

| Item | FY2009 | FY2010 | FY2011 | FY2012 | FY2013 | FY2012 as revised | Formula |
|---|---:|---:|---:|---:|---:|---:|---|
| Revenue [P1, IS_A] | 7,101.5 | 7,562.5 | 8,298.4 | 9,020.8 | 10,771.9 | 9,024.9 | copied |
| Receivables, net [P1, BS_A] | 1,325.3 | 1,356.6 | 1,616.4 | 1,886.6 | 1,512.6 | 1,879.7 | copied |
| Allowance [P1, BS_A; FY2009 from NOTES] | 21.3 | 19.7 | 20.3 | 25.1 | 30.8 | 29.3 | copied |
| DSO ending (days) | 68.1 | 65.5 | 71.1 | 76.5 | 51.3 | 76.2 | Rec net ÷ Revenue × 365 (366 in 2012) |
| DSO average (days) |  | 64.7 | 65.4 | 71.1 | 57.6 |  | average balance ÷ Revenue × days |
| DSO gap (days) |  | 0.8 | 5.7 | 5.5 | -6.3 |  | ending − average |
| Revenue growth YoY (%) |  | 6.5 | 9.7 | 8.7 | 19.4 |  | year over year |
| Gross receivables growth YoY (%) |  | 2.2 | 18.9 | 16.8 | -19.3 |  | year over year |
| Gross receivables growth minus revenue growth (pp) |  | -4.3 | 9.2 | 8.1 | -38.7 |  | difference |
| Allowance rate (%) | 1.58 | 1.43 | 1.24 | 1.31 | 2.00 | 1.53 | Allowance ÷ gross receivables |
| Provision [P1, NOTES] | 28.0 | 19.7 | 28.2 | 34.1 | 41.9 | 38.3 | copied (Schedule II charged to expense) |
| Write-offs, net of recoveries [P1, NOTES] | 25.1 | 20.5 | 27.7 | 29.3 | 40.3 | 29.3 | copied (Schedule II deductions) |
| Write-off coverage (x) | 0.90 | 1.04 | 0.98 | 0.86 | 0.96 | 0.77 | write-offs ÷ provision |
| Provision, cash flow statement [P1, EXTRA] | 28.0 | 19.7 | 28.2 | 34.1 | 45.9 | 38.3 | copied |
| Fleet-disposal receivables [text] |  | 504.2 | 620.7 | 617.3 | 357.3 | 618.6 | copied |
| DSO ending excluding fleet-disposal receivables (days) |  | 41.1 | 43.8 | 51.5 | 39.1 | 51.1 | (Rec net − fleet-disposal) ÷ Revenue × days |

FY2013 against FY2012 as revised (same basis):

| Item | FY2013 vs FY2012 as revised | Formula |
|---|---:|---|
| Revenue growth (%) | 19.4 | FY2013 ÷ 9,024.9 − 1 |
| Gross receivables growth (%) | -19.2 | (1,512.6 + 30.8) ÷ (1,879.7 + 29.3) − 1 |
| Gross receivables minus revenue growth (pp) | -38.5 | difference |
| Inventory minus direct operating growth (pp) | -32.4 | direct operating FY2012 revised 4,806.0 |
| Payables minus direct operating growth (pp) | -23.2 | payables FY2012 revised 1,003.2 |
| DSO average FY2013 on revised opening (days) | 57.5 | ((1,879.7 + 1,512.6) ÷ 2) ÷ 10,771.9 × 365 |
| DPO average FY2013 on revised opening (days) | 62.5 | ((1,003.2 + 967.9) ÷ 2) ÷ 5,752.0 × 365 |

Notes to the receivables table:
- "Fleet-disposal receivables" is each statement of cash flows' supplemental line "Sales of revenue earning equipment included in receivables" [P89, p. 5; P109, p. 5; P129, p. 5; P9, p. 90; P148, p. 6; P167, p. 6; P186, p. 6; P37, p. 78; P206, p. 7; P227, p. 7; P247, p. 7; P66, p. 81]. The amounts behave as period-end balances: each 10-Q's prior-year column equals the same date's own figure (Q1 FY2012 10-Q shows 387,620 thousand for March 2011) and they are not cumulative [inf: P89, P148]. Receivables "represent credit extended to manufacturers and customers" [P68, p. 90], so these amounts sit inside the receivables line [inf: P68, P66].
- Allowance at Q1 FY2013 (29.0) is 3.9 above Q4 FY2012 as first reported (25.1) [calc], with a Q1 FY2013 provision of 12.7 against 6.9 a year earlier [P1, NOTES]; the FY2013 10-K later revised the FY2012 closing allowance to 29.3 [P86, p. 158]. Q3 FY2013 provision was 17.0 against 9.9 in Q3 FY2012 [P1, NOTES], the quarter in which the company impaired the vehicles subleased to Simply Wheelz (E10) [P66, p. 146]; its parent's request that Hertz "forbear from seeking collection of all amounts owed to it by Simply Wheelz" came in October 2013 [P66, p. 101].
- Write-off coverage is annual only: the quarterly write-off line is blank in P1 [P1, NOTES].
- Trigger check (rule 7): no receivables ratio meets (a), (b) or (c) in its latest period; ending DSO, average DSO and the growth gap all fell in Q4 FY2013 and FY2013 against a year earlier [calc]. Rows come from the pairings and text instead.

### 3.2 Contract balances and revenue timing (A5, A6, A8)

| Item | All periods | Formula |
|---|---|---|
| Contract assets | blank in P1 [P1, BS_Q, BS_A] | none |
| Contract-asset intensity | could not run | Contract assets / (Receivables + Contract assets) |
| Contract-asset growth minus revenue growth | could not run | |
| Revenue from obligations satisfied in prior periods, share of revenue | could not run: blank in P1 NOTES and not found in text [not found: 298 text files searched for "performance obligation", "contract asset", "unbilled"] | |

Revenue policy, for context: "Rental and rental related revenue (including cost reimbursements from customers where we consider ourselves to be the principal versus an agent) are recognized over the period the revenue earning equipment is rented or leased based on the terms of the rental or leasing contract." and "Revenue related to new equipment sales and consumables is recognized at the time of delivery to, or pick-up by, the customer and when collectability is reasonably assured." [P68, p. 90]. The step 2 search terms returned no hits (section 4).

### 3.3 Inventory (A9 to A13), direct-operating basis

Quarterly:

| Item | Q1 2011 | Q2 2011 | Q3 2011 | Q4 2011 | Q1 2012 | Q2 2012 | Q3 2012 | Q4 2012 | Q1 2013 | Q2 2013 | Q3 2013 | Q4 2013 | Formula |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Direct operating (cost base) [P1, EXTRA] | 1,073.7 | 1,187.3 | 1,247.6 | 1,057.8 | 1,115.1 | 1,188.9 | 1,241.1 | 1,250.6 | 1,351.2 | 1,405.9 | 1,525.4 | 1,469.4 | copied; substitute for COGS |
| Inventory, net [P1, BS_Q] | 97.5 | 100.0 | 94.5 | 84.0 | 99.5 | 101.7 | 106.0 | 105.7 | 110.0 | 128.3 | 106.7 | 92.3 | copied |
| DIO ending, direct-operating basis (days) | 8.2 | 7.7 | 7.0 | 7.3 | 8.1 | 7.8 | 7.9 | 7.8 | 7.3 | 8.3 | 6.4 | 5.8 | Inventory ÷ Direct operating × days |
| DIO average, direct-operating basis (days) | 7.7 | 7.6 | 7.2 | 7.8 | 7.5 | 7.7 | 7.7 | 7.8 | 7.2 | 7.7 | 7.1 | 6.2 | average inventory ÷ Direct operating × days |
| Inventory growth YoY (%) |  |  |  |  | 2.1 | 1.7 | 12.2 | 25.8 | 10.6 | 26.2 | 0.7 | -12.7 | year over year, same quarter |
| Direct operating growth YoY (%) |  |  |  |  | 3.9 | 0.1 | -0.5 | 18.2 | 21.2 | 18.3 | 22.9 | 17.5 | year over year, same quarter |
| Inventory growth minus direct operating growth (pp) |  |  |  |  | -1.8 | 1.6 | 12.7 | 7.6 | -10.6 | 7.9 | -22.2 | -30.2 | difference |
| Change in inventory as % of direct operating | 0.94 | 0.21 | -0.44 | -0.99 | 1.39 | 0.18 | 0.35 | -0.02 | 0.32 | 1.30 | -1.42 | -0.98 | (closing − opening) ÷ Direct operating |
| Margin proxy (%) | 15.2 | 22.5 | 27.2 | 21.3 | 16.9 | 23.2 | 28.4 | 22.2 | 20.5 | 24.6 | 28.3 | 18.1 | (Revenue − Direct operating − Fleet depreciation and lease charges) ÷ Revenue |
| Margin proxy change YoY (pp) |  |  |  |  | 1.7 | 0.8 | 1.2 | 0.9 | 3.5 | 1.4 | -0.1 | -4.1 | same quarter prior year |
| DIO ending change YoY (days) |  |  |  |  | -0.1 | 0.1 | 0.9 | 0.5 | -0.8 | 0.5 | -1.4 | -2.0 | same quarter prior year |

Annual:

| Item | FY2009 | FY2010 | FY2011 | FY2012 | FY2013 | FY2012 as revised | Formula |
|---|---:|---:|---:|---:|---:|---:|---|
| Direct operating [P1, EXTRA] | 4,084.2 | 4,282.4 | 4,566.4 | 4,795.8 | 5,752.0 | 4,806.0 | copied |
| Inventory, net [P1, BS_A] | 93.4 | 87.4 | 84.0 | 105.7 | 92.3 | 105.7 | copied |
| DIO ending (days) | 8.3 | 7.4 | 6.7 | 8.1 | 5.9 | 8.0 | Inventory ÷ Direct operating × days |
| DIO average (days) |  | 7.7 | 6.9 | 7.2 | 6.3 |  | average ÷ Direct operating × days |
| Inventory growth minus direct operating growth (pp) |  | -11.3 | -10.5 | 20.8 | -32.6 |  | difference |
| Margin proxy (%) | 15.3 | 18.7 | 22.0 | 23.0 | 23.2 | 23.2 | as quarterly |
| Margin proxy change YoY (pp) |  | 3.4 | 3.3 | 1.0 | 0.1 |  | year over year |

Notes:
- Purchases-based DPO test: the largest change in inventory in any period is 1.42% of that period's direct operating expense, below the 10% threshold, so DPO is on the cost base, not on purchases [calc].
- Components: one line, "Inventories, at lower of cost or market" [P66, p. 75; P37, p. 72; P9, p. 86]; no raw materials, work in process or finished goods split, no reserve and no write-downs disclosed (finding under A11, row F2-A11-01). LIFO: not disclosed; "LIFO", "last-in" and "first-in" return 0 hits in the 298 text files [calc: search].
- Inventory growth minus cost growth exceeded 10 pp in Q3 FY2012 (12.7) and FY2012 (20.8), but not in the latest period (Q4 FY2013 -30.2; FY2013 -32.6) [calc]. FY2012 includes Dollar Thrifty inventory (8.0 at acquisition) [P41, p. 88].
- Trigger check: DIO ending and average are at their series lows in Q4 FY2013 and FY2013 [calc]; no trigger.

### 3.4 Payables, supplier finance and accruals (A14 to A17, C18)

Quarterly:

| Item | Q1 2011 | Q2 2011 | Q3 2011 | Q4 2011 | Q1 2012 | Q2 2012 | Q3 2012 | Q4 2012 | Q1 2013 | Q2 2013 | Q3 2013 | Q4 2013 | Formula |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Accounts payable [P1, BS_Q] | 1,204.9 | 1,560.9 | 997.3 | 897.5 | 1,320.8 | 1,487.1 | 975.1 | 999.1 | 1,304.8 | 1,484.5 | 952.4 | 967.9 | copied |
| Accrued liabilities [P1, BS_Q] | 983.4 | 1,043.9 | 1,224.2 | 1,128.5 | 1,211.4 | 1,064.4 | 1,020.5 | 1,180.5 | 1,213.9 | 1,184.4 | 1,285.8 | 1,104.7 | copied |
| DPO ending, direct-operating basis (days) | 101.0 | 119.6 | 73.5 | 78.1 | 107.8 | 113.8 | 72.3 | 73.5 | 86.9 | 96.1 | 57.4 | 60.6 | Payables ÷ Direct operating × days |
| DPO average, direct-operating basis (days) | 90.1 | 106.0 | 94.3 | 82.4 | 90.5 | 107.5 | 91.3 | 72.6 | 76.7 | 90.3 | 73.5 | 60.1 | average payables ÷ Direct operating × days |
| Payables growth YoY (%) |  |  |  |  | 9.6 | -4.7 | -2.2 | 11.3 | -1.2 | -0.2 | -2.3 | -3.1 | year over year, same quarter |
| Payables growth minus direct operating growth (pp) |  |  |  |  | 5.8 | -4.9 | -1.7 | -6.9 | -22.4 | -18.4 | -25.2 | -20.6 | difference |
| Accrued-liability intensity (%) | 55.2 | 50.4 | 50.3 | 56.0 | 61.8 | 47.8 | 40.6 | 50.9 | 49.8 | 43.6 | 41.9 | 43.3 | Accrued ÷ quarter revenue |
| Fleet purchases in payables and accruals [text, see note] | 487.9 | 628.7 | 217.7 | 153.6 | 518.2 | 598.6 | 289.8 | 249.6 | 443.1 | 561.6 | 184.2 | 289.1 | copied, converted to millions |
| Fleet purchases share of payables + accruals (%) | 22.3 | 24.1 | 9.8 | 7.6 | 20.5 | 23.5 | 14.5 | 11.5 | 17.6 | 21.0 | 8.2 | 13.9 | fleet purchases ÷ (AP + accrued) |
| Payables + accruals excluding fleet purchases, % of quarter revenue | 95.5 | 95.4 | 82.4 | 93.0 | 102.7 | 87.8 | 67.8 | 83.2 | 85.2 | 77.6 | 66.9 | 69.9 | (AP + accrued − fleet purchases) ÷ Revenue |

Annual (last value column: FY2012 as revised; payables and accruals [P1, RESTATED], fleet purchases 247.0 [P66, p. 81], reserve [P66, p. 75]):

| Item | FY2009 | FY2010 | FY2011 | FY2012 | FY2013 | FY2012 as revised | Formula |
|---|---:|---:|---:|---:|---:|---:|---|
| Accounts payable [P1, BS_A] | 658.7 | 945.0 | 897.5 | 999.1 | 967.9 | 1,003.2 | copied |
| Accrued liabilities [P1, BS_A] | 1,024.8 | 1,070.1 | 1,128.5 | 1,180.5 | 1,104.7 | 1,163.1 | copied |
| DPO ending (days) | 58.9 | 80.5 | 71.7 | 76.2 | 61.4 | 76.4 | Payables ÷ Direct operating × days |
| DPO average (days) |  | 68.3 | 73.6 | 72.4 | 62.4 |  | average ÷ Direct operating × days |
| Payables growth minus direct operating growth (pp) |  | 38.6 | -11.7 | 6.3 | -23.1 |  | difference |
| Accrued-liability intensity (%) | 14.43 | 14.15 | 13.60 | 13.09 | 10.26 | 12.89 | Accrued ÷ annual revenue |
| Payables + accruals excl. fleet purchases, % of revenue |  | 23.12 | 22.56 | 21.39 | 16.56 | 21.27 | (AP + accrued − fleet purchases) ÷ Revenue |
| Public liability and property damage reserve [P1, EXTRA] | 277.8 | 278.7 | 281.5 | 332.2 | 347.7 | 332.2 | copied |
| Reserve ÷ revenue (%) | 3.91 | 3.69 | 3.39 | 3.68 | 3.23 | 3.68 | reserve ÷ annual revenue |

Restructuring accrual rollforward (reserve releases; the only liability rollforward in the text other than the allowance) [P21, p. 139; P50, p. 126; P80, p. 141]. "Other" is every reduction that is not a cash payment; it includes asset write-downs charged and removed in the same year, so it is an upper bound on releases [inf: P21 footnotes (1), (2)]. Pre-tax income from P1 IS_A; FY2012 as reprinted uses revised pre-tax income 441.4 [P68, p. 84]:

| Year (source) | Opening | Charges | Cash payments | Other (non-payment) | Closing | Other ÷ pre-tax income (%) | Other ÷ opening (%) |
|---|---:|---:|---:|---:|---:|---:|---:|
| FY2010 | 29.7 | 54.7 | -37.4 | -29.5 | 17.5 | n/m (pre-tax loss) | 99.3 |
| FY2011 | 17.5 | 56.4 | -18.4 | -33.9 | 21.6 | 10.45 | 193.7 |
| FY2012 (FY2012 10-K) | 21.6 | 38.0 | -26.8 | -11.8 | 21.0 | 2.62 | 54.6 |
| FY2012 (FY2013 10-K) | 21.6 | 38.0 | -36.8 | -1.8 | 21.0 | 0.41 | 8.3 |
| FY2013 | 21.0 | 77.0 | -48.6 | -1.0 | 48.4 | 0.15 | 4.8 |

Notes:
- "Fleet purchases in payables and accruals" is the supplemental line "Purchases of revenue earning equipment included in accounts payable and accrued liabilities" (same locators as the fleet-disposal receivables), a period-end balance on the same reading [inf: P89, P148]. It is split across accounts payable and accrued liabilities in unknown shares, so it is removed from their sum, not from payables alone.
- Supplier finance (A15): no programme disclosed; SCF share, DPO excluding confirmed obligations and the added-minus-settled comparison could not run (section "Could not run").
- Allowance rollforward releases: Schedule II has no release or reversal column; "Deductions" are "Amounts written off, net of recoveries" [P86, p. 158], so no allowance release can be isolated [inf: P86].
- Public liability and property damage: balance only, no rollforward found [not found: P62, P63, P68, P79].
- C18 year-end pattern: payables fell from Q3 to Q4 FY2011 (997.3 to 897.5) and rose from Q3 to Q4 FY2012 (975.1 to 999.1) and FY2013 (952.4 to 967.9); in neither available year did payables or DPO fall in the following Q1 (Q1 FY2012 1,320.8; Q1 FY2013 1,304.8) [calc; P1, BS_Q]. Ending DPO rose Q3 to Q4 in 2011 (73.5 to 78.1) and 2012 (72.3 to 73.5) and rose again in the next Q1 (107.8, 86.9) [calc]. The pattern the row tests for (rise at year end, fall next quarter, in more than one year) is not present; payables peak in Q2 with fleet purchases [calc: fleet-purchase share 24.1%, 23.5%, 21.0% in Q2 of each year].
- Trigger check: DPO and payables growth minus cost growth are not adverse in the latest period (DPO fell against a year earlier in all four 2013 quarters) [calc]. Accrued-liability intensity meets (a) and (b) annually; the public liability reserve / revenue meets (a) [calc].

### 3.5 Cash-conversion cycle (A18), direct-operating basis

Quarterly:

| Item | Q1 2011 | Q2 2011 | Q3 2011 | Q4 2011 | Q1 2012 | Q2 2012 | Q3 2012 | Q4 2012 | Q1 2013 | Q2 2013 | Q3 2013 | Q4 2013 | Formula |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| DSO ending | 66.3 | 63.6 | 75.5 | 73.8 | 64.9 | 59.2 | 63.3 | 74.9 | 57.5 | 55.5 | 51.0 | 54.5 | from receivables table |
| DIO ending (direct-operating basis) | 8.2 | 7.7 | 7.0 | 7.3 | 8.1 | 7.8 | 7.9 | 7.8 | 7.3 | 8.3 | 6.4 | 5.8 | from inventory table |
| DPO ending (direct-operating basis) | 101.0 | 119.6 | 73.5 | 78.1 | 107.8 | 113.8 | 72.3 | 73.5 | 86.9 | 96.1 | 57.4 | 60.6 | from payables table |
| CCC ending (days) | -26.5 | -48.4 | 8.9 | 3.1 | -34.8 | -46.8 | -1.1 | 9.1 | -22.1 | -32.3 | 0.0 | -0.3 | DSO + DIO − DPO, ending |
| DSO average | 67.5 | 60.6 | 65.1 | 82.5 | 70.0 | 58.2 | 58.1 | 71.8 | 63.6 | 53.8 | 50.3 | 57.9 |  |
| DIO average | 7.7 | 7.6 | 7.2 | 7.8 | 7.5 | 7.7 | 7.7 | 7.8 | 7.2 | 7.7 | 7.1 | 6.2 |  |
| DPO average | 90.1 | 106.0 | 94.3 | 82.4 | 90.5 | 107.5 | 91.3 | 72.6 | 76.7 | 90.3 | 73.5 | 60.1 |  |
| CCC average (days) | -14.9 | -37.8 | -22.0 | 7.9 | -13.1 | -41.5 | -25.4 | 7.0 | -6.0 | -28.7 | -16.1 | 4.1 | DSO + DIO − DPO, average |

Annual:

| Item | FY2009 | FY2010 | FY2011 | FY2012 | FY2013 | Formula |
|---|---:|---:|---:|---:|---:|---|
| DSO ending | 68.1 | 65.5 | 71.1 | 76.5 | 51.3 |  |
| DIO ending | 8.3 | 7.4 | 6.7 | 8.1 | 5.9 |  |
| DPO ending | 58.9 | 80.5 | 71.7 | 76.2 | 61.4 |  |
| CCC ending (days) | 17.6 | -7.6 | 6.1 | 8.4 | -4.3 | DSO + DIO − DPO |
| DSO average |  | 64.7 | 65.4 | 71.1 | 57.6 |  |
| DIO average |  | 7.7 | 6.9 | 7.2 | 6.3 |  |
| DPO average |  | 68.3 | 73.6 | 72.4 | 62.4 |  |
| CCC average (days) |  | 4.1 | -1.4 | 5.9 | 1.5 | DSO + DIO − DPO |

The cycle is negative or near zero in most quarters because payables (which include fleet purchases) exceed receivables plus a small inventory [calc]. No trigger: ending CCC in Q4 FY2013 (-0.3) is below Q4 FY2012 (9.1), and FY2013 (-4.3) is the lowest year [calc].

## 4. Text found

Step 1 (allowance note, A4):
- FY2011, FY2012 and FY2013 10-K Note 2, identical apart from punctuation [calc: normalised comparison]: "Receivables are stated net of allowances for doubtful accounts and represent credit extended to manufacturers and customers that satisfy defined credit criteria. The estimate of the allowance for doubtful accounts is based on our historical experience and our judgment as to the likelihood of ultimate payment. Actual receivables are written-off against the allowance for doubtful accounts when we determine the balance will not be collected." [P11, p. 93; P39, p. 81; P68, p. 90]. No change in method, segmentation or factors.
- "charges related to certain assets and allowances for doubtful accounts in Brazil (reduced pre-tax income by $4.4 million in 2010, $6.2 million in 2011 and $3.6 million in 2012)" [P68, p. 83; same text P66, p. 83; P295, p. 9].
- Schedule II footnote: "Prior period amounts have been revised, for a description of the revisions to prior periods, see Note 2" [P86, p. 158].
- Call slide, receivables composition: "Receivables include customer receivables, subro receivables, warranty, and other misc." [P270, p. 37].

Step 2 (revenue timing, A8): no hits for "bill-and-hold", "bill and hold", "held for customer", "customer requested", "delivery at a later date", "consignment", "right of return", "extended payment terms", "early shipment", "pull forward" in any of the 298 text files [calc: search].

Step 3 (receivable transfers, A7):
- "securitiz": 726 hits in 75 files, all fleet financing on the hits read; for example "The European Securitization is the primary fleet financing for our car rental operations in France and The Netherlands." [P71, p. 112] and "Substantially all of our revenue earning equipment and certain related assets are owned by special purpose entities, or are encumbered in favor of our lenders under our various credit facilities." [P71, p. 114]. Receivables derecognized: none found, so no DSO add-back [calc: search].
- "derecogni": 16 hits in 8 files, all in the description of ASU 2013-05 on cumulative translation adjustments, for example "Parent's Accounting for the Cumulative Translation Adjustment upon Derecognition of Certain Subsidiaries or Groups of Assets within a Foreign Entity" [P68, p. 94].
- "factor": 530 hits, none within 80 characters of "receivab" [calc]; "factoring" and "factored" 0 hits.

Step 5 (payables, supplier consideration, A14 to A17):
- Vendor incentives: "These recorded pre-tax adjustments relate to vendor incentives (reduced pre-tax income by $12.9 million in 2011 and $2.4 million in 2012) which had been accounted for as a reduction of marketing expenses instead of reducing the cost of revenue earning equipment" [P68, p. 83].
- Fleet cost policy: "Revenue earning equipment is stated at cost, net of related discounts." [P39, p. 81; P68, p. 91]; not in the FY2011 10-K [calc: search of P11].
- "Primarily consists of $3.1 million adjustments related to under accruals and certain reclassifications of $23.1 million to conform to the current presentation." [P68, p. 87].
- Vendor terms: "The increase was primarily due to a change in accounts payable driven by effective management of vendor terms taken in 2010" [P5, p. 71].
- Payment timing: "The increase was primarily a result of higher earnings before interest, depreciation and amortization as well as due to the timing of our payments." [P62, p. 64]; FY2012: "The increase was primarily a result of higher earnings before interest, depreciation and amortization and reduced interest expense as well as due to the timing of our payments." [P33, p. 60].
- Restructuring footnotes for 2012 "Other": "Primarily consists of decreases of $10.3 million for facility closures and $1.0 million in ASC 715 pension adjustment." [P50, p. 126] against "Primarily consists of decreases of $0.5 million related to a goodwill write-off on a sale of business and $1.0 million in ASC 715 pension adjustment." [P80, p. 141].
- Public liability reserve basis: "Reserve requirements are based on rental volume and actuarial evaluations of historical accident claim experience and trends" [P63, p. 45; P34, p. 45] against "Reserve requirements are based on actuarial evaluations of historical accident claim experience and trends" [P6, p. 53; P68, p. 92].
- "rebate", "vendor consideration", "supplier consideration", "upfront payment", "prebate", "volume incentive": 0 hits. "allowance": 140 hits, all on doubtful accounts, tax valuation allowances, a fair-value method description ("less an allowance for loss in value due to depreciation"), a rental mileage allowance, or an "allowance for uncollectible program car receivables related to a bankrupt European dealer affiliated with a U.S. car manufacturer" in a non-GAAP footnote [P5, p. 60]; none on supplier consideration [calc: search].

## 5. Pairings

| Pairing | Period | Figures | Context | Row |
|---|---|---|---|---|
| Receivables up faster than revenue while inventory falls faster than cost | FY2011 | gross receivables +18.9% against revenue +9.7% (+9.2 pp); inventory -3.9% against direct operating +6.6% (-10.5 pp) [calc] | E2 | F2-A2-01 (P4) |
| Year-end DSO ending rising faster than DSO average | Q4 FY2012 | ending +1.0 days, average -10.7 days against Q4 FY2011 [calc] | E9 | F2-A1-01 (P4) |
| Same | FY2011 | ending +5.6, average +0.7 against FY2010 [calc] | E2 | F2-A1-01 (P4) |
| Margin proxy up while DIO rises | Q2 FY2012, Q3 FY2012, Q4 FY2012, FY2012, Q2 FY2013 | margin +0.8, +1.2, +0.9, +1.0, +1.4 pp; DIO +0.1, +0.9, +0.5, +1.4, +0.5 days [calc] | E22, E9 | F2-A13-01 (P4) |
| Allowance rate falling while DSO rises | FY2011 | allowance rate -0.19 pp, ending DSO +5.6 days [calc] | E2, E24 | F2-A3-01 (P4) |
| DPO rising while supplier-finance share rises | none | could not run: no supplier-finance disclosure | | |

No pairing was found in Q4 FY2013 or FY2013 [calc].

## 6. Ledger rows

| ID | Item | Period | Evidence | Locator | Benign reading | Adverse reading | Context | Resolving disclosure | Priority | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| F2-A1-01 | A1 DSO, ending against average at fiscal year end (pairing 2) | Q4 FY2012; FY2011 | Trigger: step 7 pairing. Q4 FY2012 ending DSO 74.9 days against 73.8 in Q4 FY2011 (+1.0), while average DSO fell from 82.5 to 71.8 (-10.7) [calc]. FY2011 ending DSO 71.1 against 65.5 in FY2010 (+5.6), average 65.4 against 64.7 (+0.7) [calc]. | P1 BS_Q and IS_Q Q4 FY2011, Q4 FY2012; P1 BS_A and IS_A FY2010, FY2011; Receivables table | The Q4 FY2012 balance sheet carries Dollar Thrifty receivables (170 at acquisition) against 43 days of its revenue, and the FY2011 balance sheet carries Donlen receivables (64.0) against four months of its revenue [inf: context sheet E2, E9]. Fleet-disposal receivables from manufacturers were 32.7% and 38.4% of net receivables at those dates [calc] and track vehicle returns, not revenue. Excluding them, FY2011 ending DSO rose 2.7 days, close to the 2.8 days of FY2011 revenue that Donlen receivables represent [calc]. | If the acquisitions and fleet-disposal timing do not account for the rise, receivables at year end grew faster than the business in a way consistent with billing concentrated at the end of the year. | E9 (Q4 FY2012); E2 (FY2011); E24 revised FY2012 receivables by -7.0; W4: FY2011 and FY2012 cells are pre-revision | Receivables by type (customer, manufacturer, other) and acquired receivables outstanding at each year end; not in pack [not found: P9, P37, P66 balance sheets and notes give one receivables line] | P4 |  |
| F2-A2-01 | A2 and A10 receivables up faster than revenue while inventory falls faster than cost (pairing 1) | FY2011 | Trigger: step 7 pairing. Gross receivables growth 18.9% against revenue growth 9.7% (+9.2 pp); inventory growth -3.9% against direct operating growth 6.6% (-10.5 pp) [calc]. Cost base is direct operating, not COGS (no COGS line). | P1 BS_A, IS_A, EXTRA (Direct operating) FY2010, FY2011; Receivables and Inventory tables | The goods-billed-not-shipped shape does not fit a rental business: revenue is "recognized over the period the revenue earning equipment is rented or leased" [P68, p. 90], and inventory, 0.48% of total assets [calc], is fuel, parts and equipment held for sale [inf: P107, p. 44; P68, p. 90]. The receivables rise matches Donlen (64.0) and fleet-disposal receivables rising from 504.2 to 620.7 [P9, p. 90]. | If Donlen and fleet-disposal receivables do not account for the rise, customer receivables grew about twice as fast as revenue in FY2011. | E2, E3; W4: FY2011 is pre-revision (E24) | Receivables by type at FY2010 and FY2011; not in pack [not found: P9, P11] | P4 |  |
| F2-A3-01 | A3 allowance rate falling while DSO rises (pairing 4) | FY2011 | Trigger: step 7 pairing. Allowance rate 1.24% against 1.43% in FY2010 (-0.19 pp) while ending DSO rose 5.6 days; excluding fleet-disposal receivables the rate is 2.00% against 2.26% (-0.26 pp) and DSO rose 2.7 days [calc]. | P1 BS_A FY2010, FY2011; P1 NOTES FY2010, FY2011; P9, p. 90 (fleet-disposal receivables); Receivables table | Donlen receivables entered the balance sheet at acquisition in September 2011 and would carry little allowance so soon after purchase, diluting the rate while adding to DSO [inf: context sheet E2; P1 NOTES]. | The company later corrected "allowances for doubtful accounts in Brazil" that reduced pre-tax income by $6.2 million in 2011 together with certain asset charges [P68, p. 83]; the 2011 fall in the rate may partly reflect that under-provision. | E2; E24 (Brazil allowances); W4 | Allowance by country or segment, and the Brazil allowance amount separate from "charges related to certain assets"; not in pack [not found: P66, P68, P86, P295 searched for "Brazil" and "doubtful"] | P4 |  |
| F2-A3-02 | A3 bad-debt provision: cash flow statement against Schedule II | FY2013 | The FY2013 cash flow statement shows "Provision for losses on doubtful accounts" of 45.9; Schedule II in the same 10-K shows 2013 "Charged to Expense" 41.9; difference 4.0 [calc]. The 2012 (38.3 and 38.3) and 2011 (28.2 and 28.2) comparatives agree [calc]. Q3 FY2013 provision 17.0 against 9.9 in Q3 FY2012 [P1, NOTES]. | P66, p. 80; P86, p. 158; P1 EXTRA and NOTES FY2013 | The cash-flow line may cover provisions on amounts outside the trade-receivable allowance, for example amounts owed by Simply Wheelz, whose parent in October 2013 "requested that Hertz forbear from seeking collection of all amounts owed to it by Simply Wheelz" [P66, p. 101]; the manifest notes the two figures can differ [P0, "How statements.xlsx is made"]. | If both lines describe the same allowance, 4.0 of 2013 bad-debt expense did not pass through the allowance rollforward, or the rollforward is incomplete. | E10 (Simply Wheelz); E24 (2012 allowance revised); Q4 FY2013 derived on mixed basis | Reconciliation of the cash-flow provision to Schedule II; not found [P66, P86, P62, P70 searched for "doubtful" and "Simply Wheelz"] | P3 |  |
| F2-A4-01 | A4 allowance method and factors; Brazil allowance correction | FY2011 to FY2013 (method); FY2010 to FY2012 (correction) | Method text is the same in all three 10-Ks: "The estimate of the allowance for doubtful accounts is based on our historical experience and our judgment as to the likelihood of ultimate payment." [P11, p. 93; P39, p. 81; P68, p. 90; calc: text comparison]. Correction: "charges related to certain assets and allowances for doubtful accounts in Brazil (reduced pre-tax income by $4.4 million in 2010, $6.2 million in 2011 and $3.6 million in 2012)" [P68, p. 83]. Schedule II 2012 charged to expense 34.1 as first reported, 38.3 as revised; closing allowance 25.1 against 29.3 (+4.2) [calc; P56; P86]. The revision table places the 2011 and 2012 Brazil adjustments in the "Direct operating" line ("Primarily consists of $6.2 million adjustment related to Brazil.") [P68, p. 85], while the policy says "Bad debt expense is reflected as a component of 'Selling, general and administrative' in our consolidated statements of operations." [P68, p. 90]; the allowance share of the Brazil amount is not given. | P11, p. 93; P39, p. 81; P68, pp. 83, 90; P56, p. 140; P86, p. 158 | The method did not change; the company found under-provision in one country, corrected it with period tables and judged it immaterial [P68, p. 83]. | The allowance was understated in one country for three years under an unchanged method description, so the stated method did not capture that exposure; the Brazil allowance amount alone is not given. | E24 | Brazil allowance amount by year; not in pack [not found: P66, P68, P295, P296] | P4 |  |
| F2-A7-01 | A7 receivable transfers: securitization hits are fleet financing | FY2011 to FY2013 | Search hit (text rows always become rows). "securitiz" has 726 hits in 75 files; the only hit within 250 characters of "receivab" is a call slide [P270, p. 38] [calc]. Example: "The European Securitization is the primary fleet financing for our car rental operations in France and The Netherlands." [P71, p. 112]. "Substantially all of our revenue earning equipment and certain related assets are owned by special purpose entities, or are encumbered in favor of our lenders under our various credit facilities." [P71, p. 114]. No sale, factoring or derecognition of receivables found [calc]. | P71, pp. 112, 114; P270, p. 38 | The programmes are asset-backed fleet debt through consolidated entities; receivables stay on the balance sheet, so no DSO add-back applies [inf: P71]. | The "certain related assets" encumbered under fleet facilities could include manufacturer receivables; if any were sold rather than pledged, DSO would be understated. Nothing in the pack indicates a sale. | none | Collateral schedule of each fleet facility; not in pack beyond the debt note | P3 |  |
| F2-A11-01 | A11 inventory reported as a single line, no cost method or reserve | FY2011 to FY2013 | The balance sheet shows one line, "Inventories, at lower of cost or market" (92.3 at FY2013) [P66, p. 75]; no classes, cost-flow method, reserve or write-down found [not found: 298 text files searched for "LIFO", "last-in", "first-in", "obsolescence", "inventory reserve", "write-down of inventor"]. Inventory is 0.38% of total assets at FY2013 [calc]. | P66, p. 75; P9, p. 86; P37, p. 72 | Inventory is immaterial for a rental company and is mainly fuel and parts, as in "gasoline and parts inventory purchases" [P107, p. 44]. | Without the cost method and any obsolescence reserve, DIO movements cannot be split between volume and valuation, and a write-down or reversal would be invisible. | E9 (8 of inventory acquired with Dollar Thrifty) | Inventory note with classes and cost method; not in pack. Whether Regulation S-X requires it at this size is [unverified: the regulation is not in the pack] | P3 |  |
| F2-A13-01 | A13 margin proxy up while DIO rises (pairing 3) | Q2, Q3, Q4 FY2012; FY2012; Q2 FY2013 | Trigger: step 7 pairing. Margin proxy change against the same period a year earlier: Q2 FY2012 +0.8 pp, Q3 FY2012 +1.2, Q4 FY2012 +0.9, FY2012 +1.0, Q2 FY2013 +1.4; DIO change +0.1, +0.9, +0.5, +1.4, +0.5 days [calc]. Proxy = (revenue - direct operating - fleet depreciation and lease charges) / revenue, because there is no gross margin line. | P1 IS_Q, IS_A, EXTRA (Direct operating; Depreciation of revenue earning equipment and lease charges), BS_Q, BS_A; Inventory table | Fleet depreciation fell from depreciation-rate changes (car rental -130.6 in 2012) [inf: context sheet E22]; in the paired periods DIO rose by 1.4 days or less, on inventory of 84.0 to 128.3 across the series [calc]; Dollar Thrifty added inventory in Q4 FY2012 [inf: context sheet E9]. | If rate changes do not account for the margin gain, cost could be held on the balance sheet; inventory is too small to hold material cost here, so the place to test that reading is fleet carrying value (F3, F4) [inf: P1 BS_Q]. | E22, E9; E24 moved vendor incentives between SG&A and fleet depreciation, so P1 2012 cost lines are pre-revision (W4) | Depreciation-rate change effects by quarter; the pack has annual amounts only [P45, p. 113; P74, p. 126] | P4 |  |
| F2-A14-01 | A14 MD&A attributes cash from operations to "timing of our payments" | FY2013 | Text row. "The increase was primarily a result of higher earnings before interest, depreciation and amortization as well as due to the timing of our payments." [P62, p. 64]. In each 2013 quarter, payables growth ran 18.4 to 25.2 pp below direct operating growth and ending DPO fell against the same quarter of 2012 (-20.9, -17.7, -14.8, -12.9 days) [calc]. Cash flow change in accrued liabilities +25.2 against -29.6 in FY2012 as revised (+54.8); payables +23.2 against +34.0 (-10.8) [calc; P66, p. 80]. | P62, p. 64; P66, p. 80; Payables table | The payment timing the MD&A refers to shows in accrued liabilities (a 54.8 swing), not in trade payables, so the sentence and the payables trend are consistent [inf: P66, P62]. | If "timing of our payments" means deferral of payments to suppliers, it does not show in the balance-sheet payables, which fell relative to cost; the source of the timing benefit is not identified. | E9 (Dollar Thrifty full year in 2013); W4; Q4 FY2013 direct operating derived on mixed basis | Breakdown of the cash-flow effect of payment timing by liability; not in pack [not found: P62, P66] | P3 |  |
| F2-A16-01 | A16 accrued-liability intensity | FY2013 | Triggers (a) and (b). Two independent signals: the ratio trend, and less line detail in the same year. Accrued liabilities / revenue 10.26% in FY2013 against 13.09% FY2012 as first reported, 12.89% as revised, 13.60% FY2011 and 14.43% FY2009: lowest in the series and down four years running [calc]. At the FY2012 revised intensity, FY2013 accruals would be 1,388.2 against 1,104.7 reported (283.5 lower) [calc]. Payables plus accruals excluding fleet purchases / revenue 16.56% against 21.27% FY2012 as revised, and down against the same quarter a year earlier in seven consecutive quarters, Q2 FY2012 to Q4 FY2013 [calc]. The FY2013 balance sheet shows one "Accrued liabilities" line where the FY2011 and FY2012 10-Ks split "Accrued salaries and other compensation" from "Other accrued liabilities" [P66, p. 75; P37, p. 72; P9, p. 86]. The revision table cites "$3.1 million adjustments related to under accruals" for nine months 2013 [P68, p. 87]. | P1 BS_A and IS_A FY2009 to FY2013; P1 RESTATED FY2012; P66, p. 75; P68, p. 87; Payables table | The FY2012 balance sheet held Dollar Thrifty accruals (298 at acquisition) against 43 days of its revenue, and FY2013 has a full year of its revenue [inf: context sheet E9, E21]; accrued interest fell from 88.5 to 73.8 [P71, p. 114]; integration and transaction accruals would run off after the acquisition [inf: context sheet E9]. | Accruals falling relative to activity to below the pre-acquisition level can reflect expenses not yet recorded, which raises reported income; the company itself identified under-accruals in 2013, and the FY2013 balance sheet gives less detail on this line than the two prior years. | E9, E21, E24; W4; the context sheet does not explain a fall below the pre-acquisition FY2011 level | Accrued liabilities by component at FY2012 and FY2013; not in pack [not found: P66, P68, P62 searched for "accrued salaries" and "other accrued"] | P2 |  |
| F2-A16-02 | A16 public liability and property damage reserve relative to revenue | FY2013 | Trigger (a). Reserve / revenue 3.23% in FY2013 against 3.68% FY2012 and 3.39% FY2011; lowest in FY2009 to FY2013 [calc]. The critical-estimates text reads "Reserve requirements are based on rental volume and actuarial evaluations" from the FY2012 10-K [P34, p. 45; P63, p. 45], against "Reserve requirements are based on actuarial evaluations" in FY2011 [P6, p. 53] and in the FY2013 notes [P68, p. 92]. No rollforward found. | P1 EXTRA (Public liability and property damage) FY2009 to FY2013; P6, p. 53; P34, p. 45; P63, p. 45; P68, p. 92 | The FY2012 reserve included Dollar Thrifty (line 281.5 to 332.2) against 43 days of its revenue [inf: context sheet E9]; the reserve is actuarial and "Our actual results as compared to our estimates have historically resulted in relatively minor adjustments to our recorded liability." [P63, p. 45]; revenue growth includes price as well as volume [inf: P62]. | If claims exposure grew with the fleet, a reserve growing more slowly than revenue could reflect a lower estimate that raises income; without a rollforward, releases cannot be seen. | E9 | Reserve rollforward (provisions, payments, prior-year development); not found [P62, P63, P68, P79 searched for "public liability and property damage" near "reserve"] | P3 |  |
| F2-A16-03 | A16 restructuring accrual: 2012 rollforward reprinted with different movements | FY2012 | FY2012 10-K: 2012 cash payments (26.8), other (11.8), "Primarily consists of decreases of $10.3 million for facility closures and $1.0 million in ASC 715 pension adjustment." [P50, p. 126]. FY2013 10-K: 2012 cash payments (36.8), other (1.8), "Primarily consists of decreases of $0.5 million related to a goodwill write-off on a sale of business and $1.0 million in ASC 715 pension adjustment." [P80, p. 141]. 10.0 moved from non-payment reductions to cash payments; opening, charges and closing unchanged [calc]. Non-payment reductions / pre-tax income: FY2011 10.45%, FY2012 2.62% as first reported and 0.41% as reprinted, FY2013 0.15% [calc]; the 10.3 facility-closure decrease equals 2.29% of FY2012 pre-tax income as first reported [calc]. | P50, p. 126; P80, p. 141; P21, p. 139; P1 IS_A | A reclassification: "Certain prior period amounts have been reclassified to conform with current year presentation." [P68, p. 83]; facility-closure amounts may have been settled in cash and first shown as other reductions. | If the first description was right, 2012 included a 10.3 reduction of the facility-closure reserve that was not a payment, and the reprint removes the trace of it. | E24 (FY2012 revised; restructuring not itemised) | Reconciliation of the two 2012 rollforwards; not found [P80, P68, P66 searched for "restructuring" and "reclassif"] | P3 |  |
| F2-A17-01 | A17 supplier consideration: vendor incentives classified against marketing expense | FY2011 to Q3 FY2013 | "These recorded pre-tax adjustments relate to vendor incentives (reduced pre-tax income by $12.9 million in 2011 and $2.4 million in 2012) which had been accounted for as a reduction of marketing expenses instead of reducing the cost of revenue earning equipment" [P68, p. 83]. Revision footnotes: 2012 fleet depreciation "$23.6 million adjustment related to vendor incentives", SG&A "$25.9 million" [P68, p. 85]; nine months 2013 "$22.1 million" and "$21.2 million" [P68, p. 87]. The policy sentence "Revenue earning equipment is stated at cost, net of related discounts." appears from the FY2012 10-K [P39, p. 81; P68, p. 91] and not in FY2011 [calc: search of P11]. | P68, pp. 83, 85, 87, 91; P39, p. 81; P11 | A classification error between fleet cost and marketing expense, found and corrected with period tables; the net pre-tax effect is the timing difference between an immediate credit to SG&A and a credit through fleet depreciation [P68, pp. 83 to 87]. | Supplier consideration taken to income at once instead of reducing asset cost raised pre-tax income by 12.9 in 2011 and 2.4 in 2012; the same treatment may affect fleet carrying values and disposal gains beyond the amounts corrected. | E24; W4 (P1 2011 to Q3 2013 cost lines are pre-revision) | Amount of vendor incentives received by year and a policy on supplier consideration; not found [298 text files searched for "rebate", "vendor consideration", "supplier consideration", "volume incentive", "upfront payment", "prebate"] | P4 |  |

```csv
ID,Item,Period,Evidence,Locator,Benign reading,Adverse reading,Context,Resolving disclosure,Priority,Verdict
F2-A1-01,"A1 DSO, ending against average at fiscal year end (pairing 2)",Q4 FY2012; FY2011,"Trigger: step 7 pairing. Q4 FY2012 ending DSO 74.9 days against 73.8 in Q4 FY2011 (+1.0), while average DSO fell from 82.5 to 71.8 (-10.7) [calc]. FY2011 ending DSO 71.1 against 65.5 in FY2010 (+5.6), average 65.4 against 64.7 (+0.7) [calc].","P1 BS_Q and IS_Q Q4 FY2011, Q4 FY2012; P1 BS_A and IS_A FY2010, FY2011; Receivables table","The Q4 FY2012 balance sheet carries Dollar Thrifty receivables (170 at acquisition) against 43 days of its revenue, and the FY2011 balance sheet carries Donlen receivables (64.0) against four months of its revenue [inf: context sheet E2, E9]. Fleet-disposal receivables from manufacturers were 32.7% and 38.4% of net receivables at those dates [calc] and track vehicle returns, not revenue. Excluding them, FY2011 ending DSO rose 2.7 days, close to the 2.8 days of FY2011 revenue that Donlen receivables represent [calc].","If the acquisitions and fleet-disposal timing do not account for the rise, receivables at year end grew faster than the business in a way consistent with billing concentrated at the end of the year.",E9 (Q4 FY2012); E2 (FY2011); E24 revised FY2012 receivables by -7.0; W4: FY2011 and FY2012 cells are pre-revision,"Receivables by type (customer, manufacturer, other) and acquired receivables outstanding at each year end; not in pack [not found: P9, P37, P66 balance sheets and notes give one receivables line]",P4,
F2-A2-01,A2 and A10 receivables up faster than revenue while inventory falls faster than cost (pairing 1),FY2011,"Trigger: step 7 pairing. Gross receivables growth 18.9% against revenue growth 9.7% (+9.2 pp); inventory growth -3.9% against direct operating growth 6.6% (-10.5 pp) [calc]. Cost base is direct operating, not COGS (no COGS line).","P1 BS_A, IS_A, EXTRA (Direct operating) FY2010, FY2011; Receivables and Inventory tables","The goods-billed-not-shipped shape does not fit a rental business: revenue is ""recognized over the period the revenue earning equipment is rented or leased"" [P68, p. 90], and inventory, 0.48% of total assets [calc], is fuel, parts and equipment held for sale [inf: P107, p. 44; P68, p. 90]. The receivables rise matches Donlen (64.0) and fleet-disposal receivables rising from 504.2 to 620.7 [P9, p. 90].","If Donlen and fleet-disposal receivables do not account for the rise, customer receivables grew about twice as fast as revenue in FY2011.","E2, E3; W4: FY2011 is pre-revision (E24)","Receivables by type at FY2010 and FY2011; not in pack [not found: P9, P11]",P4,
F2-A3-01,A3 allowance rate falling while DSO rises (pairing 4),FY2011,Trigger: step 7 pairing. Allowance rate 1.24% against 1.43% in FY2010 (-0.19 pp) while ending DSO rose 5.6 days; excluding fleet-disposal receivables the rate is 2.00% against 2.26% (-0.26 pp) and DSO rose 2.7 days [calc].,"P1 BS_A FY2010, FY2011; P1 NOTES FY2010, FY2011; P9, p. 90 (fleet-disposal receivables); Receivables table","Donlen receivables entered the balance sheet at acquisition in September 2011 and would carry little allowance so soon after purchase, diluting the rate while adding to DSO [inf: context sheet E2; P1 NOTES].","The company later corrected ""allowances for doubtful accounts in Brazil"" that reduced pre-tax income by $6.2 million in 2011 together with certain asset charges [P68, p. 83]; the 2011 fall in the rate may partly reflect that under-provision.",E2; E24 (Brazil allowances); W4,"Allowance by country or segment, and the Brazil allowance amount separate from ""charges related to certain assets""; not in pack [not found: P66, P68, P86, P295 searched for ""Brazil"" and ""doubtful""]",P4,
F2-A3-02,A3 bad-debt provision: cash flow statement against Schedule II,FY2013,"The FY2013 cash flow statement shows ""Provision for losses on doubtful accounts"" of 45.9; Schedule II in the same 10-K shows 2013 ""Charged to Expense"" 41.9; difference 4.0 [calc]. The 2012 (38.3 and 38.3) and 2011 (28.2 and 28.2) comparatives agree [calc]. Q3 FY2013 provision 17.0 against 9.9 in Q3 FY2012 [P1, NOTES].","P66, p. 80; P86, p. 158; P1 EXTRA and NOTES FY2013","The cash-flow line may cover provisions on amounts outside the trade-receivable allowance, for example amounts owed by Simply Wheelz, whose parent in October 2013 ""requested that Hertz forbear from seeking collection of all amounts owed to it by Simply Wheelz"" [P66, p. 101]; the manifest notes the two figures can differ [P0, ""How statements.xlsx is made""].","If both lines describe the same allowance, 4.0 of 2013 bad-debt expense did not pass through the allowance rollforward, or the rollforward is incomplete.",E10 (Simply Wheelz); E24 (2012 allowance revised); Q4 FY2013 derived on mixed basis,"Reconciliation of the cash-flow provision to Schedule II; not found [P66, P86, P62, P70 searched for ""doubtful"" and ""Simply Wheelz""]",P3,
F2-A4-01,A4 allowance method and factors; Brazil allowance correction,FY2011 to FY2013 (method); FY2010 to FY2012 (correction),"Method text is the same in all three 10-Ks: ""The estimate of the allowance for doubtful accounts is based on our historical experience and our judgment as to the likelihood of ultimate payment."" [P11, p. 93; P39, p. 81; P68, p. 90; calc: text comparison]. Correction: ""charges related to certain assets and allowances for doubtful accounts in Brazil (reduced pre-tax income by $4.4 million in 2010, $6.2 million in 2011 and $3.6 million in 2012)"" [P68, p. 83]. Schedule II 2012 charged to expense 34.1 as first reported, 38.3 as revised; closing allowance 25.1 against 29.3 (+4.2) [calc; P56; P86]. The revision table places the 2011 and 2012 Brazil adjustments in the ""Direct operating"" line (""Primarily consists of $6.2 million adjustment related to Brazil."") [P68, p. 85], while the policy says ""Bad debt expense is reflected as a component of 'Selling, general and administrative' in our consolidated statements of operations."" [P68, p. 90]; the allowance share of the Brazil amount is not given.","P11, p. 93; P39, p. 81; P68, pp. 83, 90; P56, p. 140; P86, p. 158","The method did not change; the company found under-provision in one country, corrected it with period tables and judged it immaterial [P68, p. 83].","The allowance was understated in one country for three years under an unchanged method description, so the stated method did not capture that exposure; the Brazil allowance amount alone is not given.",E24,"Brazil allowance amount by year; not in pack [not found: P66, P68, P295, P296]",P4,
F2-A7-01,A7 receivable transfers: securitization hits are fleet financing,FY2011 to FY2013,"Search hit (text rows always become rows). ""securitiz"" has 726 hits in 75 files; the only hit within 250 characters of ""receivab"" is a call slide [P270, p. 38] [calc]. Example: ""The European Securitization is the primary fleet financing for our car rental operations in France and The Netherlands."" [P71, p. 112]. ""Substantially all of our revenue earning equipment and certain related assets are owned by special purpose entities, or are encumbered in favor of our lenders under our various credit facilities."" [P71, p. 114]. No sale, factoring or derecognition of receivables found [calc].","P71, pp. 112, 114; P270, p. 38","The programmes are asset-backed fleet debt through consolidated entities; receivables stay on the balance sheet, so no DSO add-back applies [inf: P71].","The ""certain related assets"" encumbered under fleet facilities could include manufacturer receivables; if any were sold rather than pledged, DSO would be understated. Nothing in the pack indicates a sale.",none,Collateral schedule of each fleet facility; not in pack beyond the debt note,P3,
F2-A11-01,"A11 inventory reported as a single line, no cost method or reserve",FY2011 to FY2013,"The balance sheet shows one line, ""Inventories, at lower of cost or market"" (92.3 at FY2013) [P66, p. 75]; no classes, cost-flow method, reserve or write-down found [not found: 298 text files searched for ""LIFO"", ""last-in"", ""first-in"", ""obsolescence"", ""inventory reserve"", ""write-down of inventor""]. Inventory is 0.38% of total assets at FY2013 [calc].","P66, p. 75; P9, p. 86; P37, p. 72","Inventory is immaterial for a rental company and is mainly fuel and parts, as in ""gasoline and parts inventory purchases"" [P107, p. 44].","Without the cost method and any obsolescence reserve, DIO movements cannot be split between volume and valuation, and a write-down or reversal would be invisible.",E9 (8 of inventory acquired with Dollar Thrifty),Inventory note with classes and cost method; not in pack. Whether Regulation S-X requires it at this size is [unverified: the regulation is not in the pack],P3,
F2-A13-01,A13 margin proxy up while DIO rises (pairing 3),"Q2, Q3, Q4 FY2012; FY2012; Q2 FY2013","Trigger: step 7 pairing. Margin proxy change against the same period a year earlier: Q2 FY2012 +0.8 pp, Q3 FY2012 +1.2, Q4 FY2012 +0.9, FY2012 +1.0, Q2 FY2013 +1.4; DIO change +0.1, +0.9, +0.5, +1.4, +0.5 days [calc]. Proxy = (revenue - direct operating - fleet depreciation and lease charges) / revenue, because there is no gross margin line.","P1 IS_Q, IS_A, EXTRA (Direct operating; Depreciation of revenue earning equipment and lease charges), BS_Q, BS_A; Inventory table","Fleet depreciation fell from depreciation-rate changes (car rental -130.6 in 2012) [inf: context sheet E22]; in the paired periods DIO rose by 1.4 days or less, on inventory of 84.0 to 128.3 across the series [calc]; Dollar Thrifty added inventory in Q4 FY2012 [inf: context sheet E9].","If rate changes do not account for the margin gain, cost could be held on the balance sheet; inventory is too small to hold material cost here, so the place to test that reading is fleet carrying value (F3, F4) [inf: P1 BS_Q].","E22, E9; E24 moved vendor incentives between SG&A and fleet depreciation, so P1 2012 cost lines are pre-revision (W4)","Depreciation-rate change effects by quarter; the pack has annual amounts only [P45, p. 113; P74, p. 126]",P4,
F2-A14-01,"A14 MD&A attributes cash from operations to ""timing of our payments""",FY2013,"Text row. ""The increase was primarily a result of higher earnings before interest, depreciation and amortization as well as due to the timing of our payments."" [P62, p. 64]. In each 2013 quarter, payables growth ran 18.4 to 25.2 pp below direct operating growth and ending DPO fell against the same quarter of 2012 (-20.9, -17.7, -14.8, -12.9 days) [calc]. Cash flow change in accrued liabilities +25.2 against -29.6 in FY2012 as revised (+54.8); payables +23.2 against +34.0 (-10.8) [calc; P66, p. 80].","P62, p. 64; P66, p. 80; Payables table","The payment timing the MD&A refers to shows in accrued liabilities (a 54.8 swing), not in trade payables, so the sentence and the payables trend are consistent [inf: P66, P62].","If ""timing of our payments"" means deferral of payments to suppliers, it does not show in the balance-sheet payables, which fell relative to cost; the source of the timing benefit is not identified.",E9 (Dollar Thrifty full year in 2013); W4; Q4 FY2013 direct operating derived on mixed basis,"Breakdown of the cash-flow effect of payment timing by liability; not in pack [not found: P62, P66]",P3,
F2-A16-01,A16 accrued-liability intensity,FY2013,"Triggers (a) and (b). Two independent signals: the ratio trend, and less line detail in the same year. Accrued liabilities / revenue 10.26% in FY2013 against 13.09% FY2012 as first reported, 12.89% as revised, 13.60% FY2011 and 14.43% FY2009: lowest in the series and down four years running [calc]. At the FY2012 revised intensity, FY2013 accruals would be 1,388.2 against 1,104.7 reported (283.5 lower) [calc]. Payables plus accruals excluding fleet purchases / revenue 16.56% against 21.27% FY2012 as revised, and down against the same quarter a year earlier in seven consecutive quarters, Q2 FY2012 to Q4 FY2013 [calc]. The FY2013 balance sheet shows one ""Accrued liabilities"" line where the FY2011 and FY2012 10-Ks split ""Accrued salaries and other compensation"" from ""Other accrued liabilities"" [P66, p. 75; P37, p. 72; P9, p. 86]. The revision table cites ""$3.1 million adjustments related to under accruals"" for nine months 2013 [P68, p. 87].","P1 BS_A and IS_A FY2009 to FY2013; P1 RESTATED FY2012; P66, p. 75; P68, p. 87; Payables table","The FY2012 balance sheet held Dollar Thrifty accruals (298 at acquisition) against 43 days of its revenue, and FY2013 has a full year of its revenue [inf: context sheet E9, E21]; accrued interest fell from 88.5 to 73.8 [P71, p. 114]; integration and transaction accruals would run off after the acquisition [inf: context sheet E9].","Accruals falling relative to activity to below the pre-acquisition level can reflect expenses not yet recorded, which raises reported income; the company itself identified under-accruals in 2013, and the FY2013 balance sheet gives less detail on this line than the two prior years.","E9, E21, E24; W4; the context sheet does not explain a fall below the pre-acquisition FY2011 level","Accrued liabilities by component at FY2012 and FY2013; not in pack [not found: P66, P68, P62 searched for ""accrued salaries"" and ""other accrued""]",P2,
F2-A16-02,A16 public liability and property damage reserve relative to revenue,FY2013,"Trigger (a). Reserve / revenue 3.23% in FY2013 against 3.68% FY2012 and 3.39% FY2011; lowest in FY2009 to FY2013 [calc]. The critical-estimates text reads ""Reserve requirements are based on rental volume and actuarial evaluations"" from the FY2012 10-K [P34, p. 45; P63, p. 45], against ""Reserve requirements are based on actuarial evaluations"" in FY2011 [P6, p. 53] and in the FY2013 notes [P68, p. 92]. No rollforward found.","P1 EXTRA (Public liability and property damage) FY2009 to FY2013; P6, p. 53; P34, p. 45; P63, p. 45; P68, p. 92","The FY2012 reserve included Dollar Thrifty (line 281.5 to 332.2) against 43 days of its revenue [inf: context sheet E9]; the reserve is actuarial and ""Our actual results as compared to our estimates have historically resulted in relatively minor adjustments to our recorded liability."" [P63, p. 45]; revenue growth includes price as well as volume [inf: P62].","If claims exposure grew with the fleet, a reserve growing more slowly than revenue could reflect a lower estimate that raises income; without a rollforward, releases cannot be seen.",E9,"Reserve rollforward (provisions, payments, prior-year development); not found [P62, P63, P68, P79 searched for ""public liability and property damage"" near ""reserve""]",P3,
F2-A16-03,A16 restructuring accrual: 2012 rollforward reprinted with different movements,FY2012,"FY2012 10-K: 2012 cash payments (26.8), other (11.8), ""Primarily consists of decreases of $10.3 million for facility closures and $1.0 million in ASC 715 pension adjustment."" [P50, p. 126]. FY2013 10-K: 2012 cash payments (36.8), other (1.8), ""Primarily consists of decreases of $0.5 million related to a goodwill write-off on a sale of business and $1.0 million in ASC 715 pension adjustment."" [P80, p. 141]. 10.0 moved from non-payment reductions to cash payments; opening, charges and closing unchanged [calc]. Non-payment reductions / pre-tax income: FY2011 10.45%, FY2012 2.62% as first reported and 0.41% as reprinted, FY2013 0.15% [calc]; the 10.3 facility-closure decrease equals 2.29% of FY2012 pre-tax income as first reported [calc].","P50, p. 126; P80, p. 141; P21, p. 139; P1 IS_A","A reclassification: ""Certain prior period amounts have been reclassified to conform with current year presentation."" [P68, p. 83]; facility-closure amounts may have been settled in cash and first shown as other reductions.","If the first description was right, 2012 included a 10.3 reduction of the facility-closure reserve that was not a payment, and the reprint removes the trace of it.",E24 (FY2012 revised; restructuring not itemised),"Reconciliation of the two 2012 rollforwards; not found [P80, P68, P66 searched for ""restructuring"" and ""reclassif""]",P3,
F2-A17-01,A17 supplier consideration: vendor incentives classified against marketing expense,FY2011 to Q3 FY2013,"""These recorded pre-tax adjustments relate to vendor incentives (reduced pre-tax income by $12.9 million in 2011 and $2.4 million in 2012) which had been accounted for as a reduction of marketing expenses instead of reducing the cost of revenue earning equipment"" [P68, p. 83]. Revision footnotes: 2012 fleet depreciation ""$23.6 million adjustment related to vendor incentives"", SG&A ""$25.9 million"" [P68, p. 85]; nine months 2013 ""$22.1 million"" and ""$21.2 million"" [P68, p. 87]. The policy sentence ""Revenue earning equipment is stated at cost, net of related discounts."" appears from the FY2012 10-K [P39, p. 81; P68, p. 91] and not in FY2011 [calc: search of P11].","P68, pp. 83, 85, 87, 91; P39, p. 81; P11","A classification error between fleet cost and marketing expense, found and corrected with period tables; the net pre-tax effect is the timing difference between an immediate credit to SG&A and a credit through fleet depreciation [P68, pp. 83 to 87].",Supplier consideration taken to income at once instead of reducing asset cost raised pre-tax income by 12.9 in 2011 and 2.4 in 2012; the same treatment may affect fleet carrying values and disposal gains beyond the amounts corrected.,E24; W4 (P1 2011 to Q3 2013 cost lines are pre-revision),"Amount of vendor incentives received by year and a policy on supplier consideration; not found [298 text files searched for ""rebate"", ""vendor consideration"", ""supplier consideration"", ""volume incentive"", ""upfront payment"", ""prebate""]",P4,
```

## 7. Looked for and not found

| Disclosure | Files searched | Terms |
|---|---|---|
| Revenue-timing arrangements (A8) | all 298 text files, P2 to P299 | "bill-and-hold", "bill and hold", "held for customer", "customer requested", "delivery at a later date", "consignment", "right of return", "extended payment terms", "early shipment", "pull forward" |
| Receivable sales, factoring, derecognition (A7) | all 298 text files | "factor" (and "factoring", "factored"), "securitiz", "securitis", "sale of receivables", "sold receivables", "derecogni", "transferred financial assets" |
| Supplier finance programme (A15) | all 298 text files | "supply chain finance", "supplier finance", "confirmed obligations", "payment terms", "reverse factoring", "structured payable", "vendor financ" |
| Supplier consideration policy (A17) | all 298 text files | "rebate", "allowance", "vendor consideration", "supplier consideration", "upfront payment", "prebate", "volume incentive"; "vendor incentive" hits only in the E24 revision text (P66, P68, P295, P296) |
| Contract assets, revenue from prior-period obligations (A5, A6) | all 298 text files | "contract asset", "unbilled", "performance obligation", "deferred revenue" (24 hits, all Donlen acquisition pro forma text), "unearned revenue", "customer deposits" |
| Inventory classes, cost method, reserve, write-downs, LIFO (A11 to A13) | all 298 text files | "inventor" (61 hits in 39 files, none mentioning a cost method, reserve, classes or write-down), "LIFO", "last-in", "first-in", "obsolescence", "obsolete" (1 hit: telecom equipment, P270), "inventory reserve", "write-down of inventor"; "lower of cost" (12 hits, all the balance-sheet caption) |
| Receivables by type (customer, manufacturer, other) | P5, P9, P11, P33, P37, P39, P62, P66, P68 | "manufacturer receivables", "receivables from manufacturers", "customer receivables", "Receivables consist"; only a call slide lists types without amounts [P270, p. 37] |
| Accrued liabilities by component, FY2013 | P62, P66, P68 | "accrued salaries", "other accrued liabilities" |
| Public liability and property damage rollforward | P62, P63, P68, P79 | "public liability and property damage" near "rollforward", "beginning of", "balance at", "payments" |
| Reconciliation of the two 2012 restructuring rollforwards | P66, P68, P80 | "restructuring", "reclassif" |
| Reconciliation of 2013 bad-debt provision (45.9) to Schedule II (41.9) | P62, P66, P70, P79, P84, P86, P295 | "doubtful"; P62, P66, P70 "Simply Wheelz" |
| Brazil allowance amount on its own | P66, P68, P86, P295 | "Brazil" (19 hits), "doubtful" |

## 8. Could not run

| Row | Reason |
|---|---|
| A5 contract-asset intensity and growth gap | Missing input: no contract-asset line in P1 or the filings [P1, BS_Q; not found above] |
| A6 revenue from obligations satisfied in prior periods | Missing input: blank in P1 NOTES, not disclosed [not found above] |
| A12 inventory reserve rate and write-down intensity | Missing input: no reserve or write-down disclosed |
| A15 supplier finance (SCF share, DPO excluding confirmed obligations, added minus settled against cash from operations) | Missing input: no programme disclosed; the US GAAP supplier-finance rollforward did not apply to these periods [unverified: effective date not in the pack] |
| A9, A10, A13, A14, A18 as specified on COGS | Missing input: no COGS line; run on the direct-operating substitute instead (tables 3.3 to 3.5) |
| A11 component shares and component growth | Missing input: single inventory line (reported as finding F2-A11-01) |
| A13 LIFO reserve change / COGS and LIFO liquidation / pre-tax income | Not disclosed; no LIFO reference found |
| A7 DSO recomputed with derecognized receivables added back | No derecognized amount: no transfer found |
| IFRS instructions (provision matrix, IAS 37 releases, IAS 2 reversals, IAS 7 44H) | Framework does not apply: US GAAP filer; no PROVISIONS or PROVISION_MATRIX sheet [P0, "Known limits"] |
| Quarterly write-off coverage | Missing input: quarterly write-offs blank in P1 NOTES |
| Average ratios for FY2009 | Missing input: no FY2008 balance sheet in P1 |

## 9. Code

All code ran in Python 3 over the attached files, in this order. `packlib.py` is the file loader and search helper used by every later script.

`packlib.py`

```python
import re, os
PACK = r"C:/Users/aaron/OneDrive/Desktop/Master/WireSift Research/Events/CFA Vancouver Forensic/tests/hertz-fy2013/pack"
def load_ids():
    ids = {}
    for line in open(os.path.join(PACK, "manifest.md"), encoding="utf-8"):
        m = re.match(r"\| (P\d+) \| ([^|]+?) \|", line)
        if m: ids[m.group(2).strip()] = m.group(1)
    return ids
IDS = load_ids()
FILE_OF = {v: k for k, v in IDS.items()}
def text(pid):
    return open(os.path.join(PACK, FILE_OF[pid]), encoding="utf-8", errors="replace").read()
def textfiles():
    return [(p, f) for f, p in IDS.items() if f.endswith(".txt")]
def page_at(t, pos):
    last = None
    for m in re.finditer(r"\[p\. (\d+)\]", t[:pos]):
        last = m.group(1)
    return last
def search(term, pids=None, flags=re.I, ctx=200):
    out = []
    for pid, f in textfiles():
        if pids and pid not in pids: continue
        t = text(pid)
        for m in re.finditer(term, t, flags):
            s = max(0, m.start()-ctx); e = min(len(t), m.end()+ctx)
            out.append((pid, f, page_at(t, m.start()), t[s:e].replace("\n", " ")))
    return out
```

`exploratory_log.py`

```python
# Exploratory reads run before the main scripts, in order (one-line commands collected here as run).
import pandas as pd, re
from packlib import *
x = pd.ExcelFile(PACK + '/statements.xlsx')
# 1. dump IS_Q, IS_A, BS_Q, BS_A, CF_Q, CF_A, NOTES, then EXTRA, LOCATORS (head), RESTATED (working-capital lines)
for s in ['IS_Q', 'IS_A', 'BS_Q', 'BS_A', 'CF_Q', 'CF_A', 'NOTES', 'EXTRA']:
    print(x.parse(s, header=None).to_string())
print(x.parse('LOCATORS').head())
r = x.parse('RESTATED'); print(r[r.iloc[:, 1].astype(str).str.contains('eceivable|nventor|payable|ccrued|llowance|Revenue|Direct')])
# 2. search helper checks and term counts: see s1_counts.py (run next)
# 3. context for hits
for h in search(r'derecogni', ctx=350): print(h)
for h in search(r'factoring|factored|factor (?:our |its )?receivable'): print(h)
print([h for h in search(r'securitiz', ctx=250) if re.search(r'receivable', h[3], re.I)])
for pid in ['P68', 'P71', 'P11']: print(search(r'receivable', [pid], ctx=300))
for pid in ['P62', 'P33', 'P5']: print(search(r'receivable|accounts payable|payables|working capital|inventor', [pid], ctx=250))
# s_ocf.py, s_inc.py (run here)
t = text('P68'); i = t.find('During the fourth quarter of 2013'); print(t[i - 200:i + 14000])   # revision tables
# s_inv.py (run here)
print(search(r'\bLIFO\b|first-in|\bFIFO\b|average cost|obsolescen', flags=0, ctx=150))
for pid in ['P27', 'P56', 'P86', 'P80', 'P50', 'P21']: print(text(pid))                           # Schedule II, restructuring notes
for pid in ['P68', 'P63', 'P79']: print(search(r'public liability and property damage', [pid], ctx=500))
for pid in ['P6', 'P34', 'P63']: t = text(pid); i = t.find('The adequacy of the liability'); print(t[i:i + 900])
print(search(r'bankrupt European dealer|uncollectible program car', ctx=1200)[:3])
for pid in ['P66', 'P37', 'P9', 'P206', 'P227', 'P247', 'P89', 'P148']:
    print(search(r'Purchases of revenue earning equipment included in', [pid], ctx=500)[:1])
# s_supp.py (first extraction attempt; replaced by the whitespace-tolerant pattern in f2_part2.py)
print(search(r'Direct operating \| ', ['P148'], ctx=60)[:2])                                     # Q1 2012 direct operating as filed
print(search(r'vendor financ|reverse factoring|structured payable|payment terms|vendor terms|timing of (our )?(vendor )?payments|confirmed obligations'))
print(search(r'vendor incentive', ['P296', 'P66'], ctx=300)); t = text('P68'); print(t[t.find('Revenue Earning Equipment'):][:1200])
t = text('P71')
for m in re.finditer(r'receivable', t): print(t[m.start() - 500:m.start() + 300])
for pat in [r'European Securitization', r'Canadian Securitization', r'Australian Securitization', r'collateral(ized)? (by|for)', r'secured by']:
    print([m.start() for m in re.finditer(pat, t)])
for pid in ['P71', 'P62']: print(search(r'borrowing base', [pid], ctx=400))
for term in [r'deferred revenue', r'unearned revenue', r'customer deposits', r'contract asset', r'unbilled', r'Accrued salaries', r'performance obligation']:
    print(term, len(search(term)))
for pid in ['P66', 'P37', 'P9', 'P206', 'P227', 'P247', 'P186', 'P129']:
    t = text(pid); i = t.find('LIABILITIES AND'); print(t[i:i + 700])                            # liability captions
for pid in ['P6', 'P34', 'P63', 'P11', 'P39', 'P68']:
    t = text(pid); i = t.find('Reserve requirements are based'); print(t[i:i + 330])
for pid in ['P66', 'P37', 'P9', 'P206', 'P227', 'P247', 'P186']:
    print(search(r'Provision for losses on doubtful accounts', [pid], ctx=120)[:1])
print(search(r'obsolete', ['P270'], ctx=200)); t = text('P11'); print(t[t.find('Depreciable Assets'):][:700])
print(search(r'doubtful', ['P66', 'P62', 'P70', 'P79', 'P84', 'P86', 'P295'], ctx=200))
print([h for h in search(r'Simply Wheelz', ['P66', 'P70', 'P62'], ctx=300) if re.search(r'reserve|allowance|provision|impair|receivable|collect', h[3], re.I)])
print([h for h in search(r'Brazil', ['P66', 'P68', 'P86', 'P295'], ctx=150) if 'doubtful' in h[3]])
print(search(r'manufacturer receivables|receivables from manufacturers|customer receivables|Receivables consist', ['P9', 'P37', 'P66', 'P11', 'P39', 'P68', 'P62', 'P33', 'P5'], ctx=100))
print(search(r'accrued salaries|other accrued liabilities', ['P66', 'P68', 'P62']), search(r'reclassif', ['P80']))
inv = search(r'inventor(y|ies)', ctx=200)
print([h for h in inv if re.search(r'LIFO|FIFO|first-in|reserve|obsolete|raw material|finished goods|work in process|consist of|write-?down', h[3], re.I)])
print(search(r'lower of cost')); print(search(r'deferred revenue', ctx=250))
```

`s1_counts.py`

```python
from packlib import *
from collections import Counter
groups = {
 "A8 revenue timing": ["bill-and-hold","bill and hold","held for customer","customer requested","delivery at a later date","consignment","right of return","extended payment terms","early shipment","pull forward","pull-forward"],
 "A7 transfers": ["factor","securitiz","securitis","sale of receivables","sold receivables","derecogni","transferred financial assets","supply chain finance","supplier finance"],
 "A17 supplier consideration": ["rebate","allowance","vendor consideration","supplier consideration","upfront payment","prebate","volume incentive","vendor incentive","incentive"],
}
for g, terms in groups.items():
    print("==", g)
    for term in terms:
        hits = search(re.escape(term))
        files = Counter(h[0] for h in hits)
        print(f"  {term!r}: {len(hits)} hits in {len(files)} files", sorted(files, key=lambda p:int(p[1:]))[:40])
```

`s_ocf.py`

```python
from packlib import *
for pid in ['P62','P33','P225','P246','P266','P204','P185','P166']:
  print('#####',pid, FILE_OF[pid])
  for h in search(r'more cash from operating|less cash from operating|cash from operating activities compared', [pid], ctx=900)[:2]:
    print('p.',h[2],'::',h[3]); print()
```

`s_inc.py`

```python
from packlib import *
for pid in ['P68','P11','P39','P295','P63','P6','P34']:
  print('#####',pid, FILE_OF[pid])
  seen=set()
  for h in search(r'incentive|rebate|allowance|repurchase program|guaranteed depreciation', [pid], ctx=350):
    k=h[3][300:420]
    if k in seen: continue
    if re.search(r'stock|equity incentive|incentive plan|incentive compensation|valuation allowance|Omnibus', h[3][250:450], re.I): continue
    seen.add(k); print('p.',h[2],'::',h[3]); print()
```

`s_inv.py`

```python
from packlib import *
from collections import Counter
hits=search(r'inventor(y|ies)', ctx=300)
print(len(hits), Counter(h[0] for h in hits).most_common(60))
for pid in ['P68','P39','P11','P66']:
  print('#####',pid)
  seen=set()
  for h in search(r'inventor(y|ies)|LIFO|first-in|FIFO|obsolete|lower of cost', [pid], ctx=300):
    k=h[3][250:350]
    if k in seen: continue
    seen.add(k); print('p.',h[2],'::',h[3]); print()
```

`s_supp.py`

```python
from packlib import *
filings = {'Q1 FY2011':'P89','Q2 FY2011':'P109','Q3 FY2011':'P129','Q4 FY2011':'P9',
           'Q1 FY2012':'P148','Q2 FY2012':'P167','Q3 FY2012':'P186','Q4 FY2012':'P37',
           'Q1 FY2013':'P206','Q2 FY2013':'P227','Q3 FY2013':'P247','Q4 FY2013':'P66'}
scale = {p:(1000.0 if p in ('P89','P109','P129','P9','P148','P167','P186','P37','P206') else 1.0) for p in filings.values()}
pats = {'fleet_purch_in_AP': r'Purchases of revenue earning equipment included in accounts payable and (?:other )?accrued liabilities \| \$?([\d,\.]+) \| \$?([\d,\.]+)',
        'fleet_sales_in_AR': r'Sales of revenue earning equipment included in receivables \| \$?([\d,\.]+) \| \$?([\d,\.]+)'}
res = {}
for per, pid in filings.items():
    t = text(pid)
    for k, p in pats.items():
        m = re.search(p, t)
        if not m: print("FAIL", k, per, pid); continue
        v = float(m.group(1).replace(',',''))/scale[pid]
        prior = float(m.group(2).replace(',',''))/scale[pid]
        res[(k,per)] = (round(v,1), round(prior,1), pid, page_at(t, m.start()))
for k in pats:
    for per in filings:
        print(k, per, res.get((k,per)))
```

`f2_compute.py`

```python
# F2 working capital: all ratios computed from P1 (statements.xlsx) plus a few text-file values, as noted.
import pandas as pd, calendar, re
from packlib import PACK, text, page_at
X = pd.ExcelFile(PACK + "/statements.xlsx")
def sheet(name):
    df = X.parse(name, header=0)
    return df.set_index(df.columns[0])
ISQ, BSQ, CFQ, NOTES = sheet("IS_Q"), sheet("BS_Q"), sheet("CF_Q"), sheet("NOTES")
ISA, BSA, CFA = sheet("IS_A"), sheet("BS_A"), sheet("CF_A")
EX = X.parse("EXTRA", header=0)
def extra(label, stmt="IS"):
    r = EX[(EX["Company label"] == label) & (EX["Statement"] == stmt)]
    assert len(r) == 1, label
    return r.iloc[0]
Q = [f"Q{q} FY{y}" for y in (2011, 2012, 2013) for q in (1, 2, 3, 4)]
A = [f"FY{y}" for y in range(2009, 2014)]

def qdays(p):
    q, y = int(p[1]), int(p[-4:])
    months = range(3*q-2, 3*q+1)
    return sum(calendar.monthrange(y, m)[1] for m in months)
def ydays(p):
    y = int(p[-4:]); return 366 if calendar.isleap(y) else 365
DAYS = {p: qdays(p) for p in Q}; DAYS.update({p: ydays(p) for p in A})

# ---- base series (USD millions) ----
rev   = {**ISQ.loc["Revenue", Q].to_dict(), **ISA.loc["Revenue", A].to_dict()}
ar    = {**BSQ.loc["Trade receivables, net", Q].to_dict(), **BSA.loc["Trade receivables, net", A].to_dict()}
allow = {**BSQ.loc["Allowance for credit losses", Q].to_dict(), **BSA.loc["Allowance for credit losses", A].to_dict()}
allow["FY2009"] = NOTES.loc["Allowance: closing", "FY2009"]   # BS_A blank for FY2009; Schedule II closing used
inv   = {**BSQ.loc["Inventory, net", Q].to_dict(), **BSA.loc["Inventory, net", A].to_dict()}
ap    = {**BSQ.loc["Trade payables", Q].to_dict(), **BSA.loc["Trade payables", A].to_dict()}
accr  = {**BSQ.loc["Accrued liabilities", Q].to_dict(), **BSA.loc["Accrued liabilities", A].to_dict()}
pti   = {**ISQ.loc["Pre-tax income", Q].to_dict(), **ISA.loc["Pre-tax income", A].to_dict()}
dop_r = extra("Direct operating"); dop = {p: dop_r[p] for p in Q + A}
fdep_r = extra("Depreciation of revenue earning equipment and lease charges"); fdep = {p: fdep_r[p] for p in Q + A}
# openings: Q1 FY2011 opens on FY2010 year end
def prev_bal(p):
    if p in Q:
        i = Q.index(p); return "FY2010" if i == 0 else Q[i-1]
    i = A.index(p); return None if i == 0 else A[i-1]
def bal(series, p): return series[p]
def avg(series, p):
    o = prev_bal(p)
    return None if o is None else (series[o] + series[p]) / 2
def yoy_base(p):
    if p in Q:
        i = Q.index(p); return None if i < 4 else Q[i-4]
    i = A.index(p); return None if i == 0 else A[i-1]
def g(series, p):
    b = yoy_base(p)
    return None if b is None else (series[p] / series[b] - 1) * 100

# ---- FY2012 as revised (E24) for a like-for-like FY2013 vs FY2012 column ----
# values from P1 RESTATED (receivables, payables, accrued, revenue) and P68 p.84 / P86 (direct operating, fleet dep, allowance)
REV12 = dict(rev=9024.9, ar=1879.7, allow=29.3, inv=105.7, ap=1003.2, accr=1163.1, dop=4806.0, fdep=2128.9, pti=441.4)

R = {}
def put(k, p, v): R.setdefault(k, {})[p] = None if v is None else round(v, 4)
for p in Q + A:
    d = DAYS[p]
    gross = ar[p] + allow[p]
    put("DSO_end", p, ar[p] / rev[p] * d)
    a = avg(ar, p); put("DSO_avg", p, None if a is None else a / rev[p] * d)
    put("DSO_gap", p, None if a is None else ar[p]/rev[p]*d - a/rev[p]*d)
    put("gross_AR", p, gross)
    put("allow_rate_pct", p, allow[p] / gross * 100)
    put("DIO_end", p, inv[p] / dop[p] * d)
    a = avg(inv, p); put("DIO_avg", p, None if a is None else a / dop[p] * d)
    put("DPO_end", p, ap[p] / dop[p] * d)
    a = avg(ap, p); put("DPO_avg", p, None if a is None else a / dop[p] * d)
    o = prev_bal(p)
    put("dInv_pct_of_DO", p, None if o is None else (inv[p] - inv[o]) / dop[p] * 100)
    put("accr_intensity_pct", p, accr[p] / rev[p] * 100)
    put("margin_proxy_pct", p, (rev[p] - dop[p] - fdep[p]) / rev[p] * 100)
for p in Q + A:
    grossser = R["gross_AR"]
    put("g_rev", p, g(rev, p)); put("g_grossAR", p, g(grossser, p)); put("g_netAR", p, g(ar, p))
    put("gap_AR_rev", p, None if g(rev, p) is None else g(grossser, p) - g(rev, p))
    put("g_inv", p, g(inv, p)); put("g_dop", p, g(dop, p))
    put("gap_inv_dop", p, None if g(rev, p) is None else g(inv, p) - g(dop, p))
    put("g_ap", p, g(ap, p)); put("gap_ap_dop", p, None if g(rev, p) is None else g(ap, p) - g(dop, p))
    b = yoy_base(p)
    put("margin_chg_pp", p, None if b is None else R["margin_proxy_pct"][p] - R["margin_proxy_pct"][b])
    for k in ("DSO_end", "DSO_avg", "DIO_end", "DPO_end", "allow_rate_pct"):
        put("chg_" + k, p, None if (b is None or R[k][p] is None or R[k][b] is None) else R[k][p] - R[k][b])
    for k in ("end", "avg"):
        s, i_, pp = R["DSO_"+k][p], R["DIO_"+k][p], R["DPO_"+k][p]
        put("CCC_"+k, p, None if None in (s, i_, pp) else s + i_ - pp)

# annual allowance rollforward (NOTES = Schedule II as originally reported)
for p in A:
    prov = NOTES.loc["Allowance: provision", p]; wo = -NOTES.loc["Allowance: write-offs", p]
    put("writeoff_coverage", p, wo / prov)
    put("provision_pct_rev", p, prov / rev[p] * 100)

# FY2012 as revised, and FY2013 against it
d12, d13 = 366, 365
rv = REV12
R["rev12"] = dict(
    DSO_end=rv["ar"]/rv["rev"]*d12, allow_rate_pct=rv["allow"]/(rv["ar"]+rv["allow"])*100,
    DIO_end=rv["inv"]/rv["dop"]*d12, DPO_end=rv["ap"]/rv["dop"]*d12, accr_intensity_pct=rv["accr"]/rv["rev"]*100,
    margin_proxy_pct=(rv["rev"]-rv["dop"]-rv["fdep"])/rv["rev"]*100)
R["fy13_vs_rev12"] = dict(
    g_rev=(rev["FY2013"]/rv["rev"]-1)*100, g_grossAR=((ar["FY2013"]+allow["FY2013"])/(rv["ar"]+rv["allow"])-1)*100,
    g_inv=(inv["FY2013"]/rv["inv"]-1)*100, g_dop=(dop["FY2013"]/rv["dop"]-1)*100, g_ap=(ap["FY2013"]/rv["ap"]-1)*100,
    DSO_avg=((rv["ar"]+ar["FY2013"])/2)/rev["FY2013"]*365, DIO_avg=((rv["inv"]+inv["FY2013"])/2)/dop["FY2013"]*365,
    DPO_avg=((rv["ap"]+ap["FY2013"])/2)/dop["FY2013"]*365)
f = R["fy13_vs_rev12"]; f["gap_AR_rev"] = f["g_grossAR"]-f["g_rev"]; f["gap_inv_dop"] = f["g_inv"]-f["g_dop"]; f["gap_ap_dop"] = f["g_ap"]-f["g_dop"]

if __name__ == "__main__":
    print("Days:", DAYS)
    def fmt(v, nd=1): return "" if v is None or (isinstance(v, float) and pd.isna(v)) else f"{v:.{nd}f}"
    for k in R:
        if k in ("rev12", "fy13_vs_rev12"): continue
        print(k.ljust(20), " | ".join(fmt(R[k].get(p), 2) for p in Q), " || ", " | ".join(fmt(R[k].get(p), 2) for p in A))
    print("rev12", {k: round(v, 2) for k, v in R["rev12"].items()})
    print("fy13_vs_rev12", {k: round(v, 2) for k, v in R["fy13_vs_rev12"].items()})
```

`f2_part2.py`

```python
# Supplementary series, pairings, triggers, C18
import re
from f2_compute import *
from packlib import text, page_at

# (1) Fleet-disposal receivables and fleet-purchase payables, as filed in each statement of cash flows
#     ("Supplemental disclosures of non-cash flow information"). Scale: thousands through Q1 2013, millions after.
FIL = {'Q1 FY2011': 'P89', 'Q2 FY2011': 'P109', 'Q3 FY2011': 'P129', 'Q4 FY2011': 'P9', 'Q1 FY2012': 'P148', 'Q2 FY2012': 'P167',
       'Q3 FY2012': 'P186', 'Q4 FY2012': 'P37', 'Q1 FY2013': 'P206', 'Q2 FY2013': 'P227', 'Q3 FY2013': 'P247', 'Q4 FY2013': 'P66'}
THOUS = {'P89', 'P109', 'P129', 'P9', 'P148', 'P167', 'P186', 'P37', 'P206'}
PAT = {'fleetAR': r'Sales of revenue earning equipment included in receivables\s*\|\s*\$?([\d,\.]+)\s*\|\s*\$?([\d,\.]+)',
       'fleetAP': r'Purchases of revenue earning equipment included in accounts payable and\s+(?:other\s+)?accrued liabilities\s*\|\s*\$?([\d,\.]+)\s*\|\s*\$?([\d,\.]+)'}
SUP, LOC = {}, {}
for per, pid in FIL.items():
    t = text(pid)
    for k, p in PAT.items():
        m = re.search(p, t)
        sc = 1000.0 if pid in THOUS else 1.0
        SUP[(k, per)] = float(m.group(1).replace(',', '')) / sc
        LOC[(k, per)] = (pid, page_at(t, m.start()))
        if per == 'Q4 FY2011':   # FY2010 comparative column of the FY2011 10-K
            SUP[(k, 'FY2010')] = float(m.group(2).replace(',', '')) / sc
for per in Q:
    if per.startswith('Q4'):
        y = 'FY' + per[-4:]
        for k in PAT:
            SUP[(k, y)] = SUP[(k, per)]
for k in PAT:
    print(k, {p: round(SUP[(k, p)], 1) for p in Q}, 'FY2010', round(SUP[(k, 'FY2010')], 1))
print('locators', {k: v for k, v in LOC.items()})

S = {}
def sput(k, p, v): S.setdefault(k, {})[p] = round(v, 4)
for p in Q + ['FY2010', 'FY2011', 'FY2012', 'FY2013']:
    fa = SUP[('fleetAR', p)]; fp = SUP[('fleetAP', p)]
    sput('fleetAR_share_pct', p, fa / ar[p] * 100)
    sput('DSO_end_exfleet', p, (ar[p] - fa) / rev[p] * DAYS[p])
    sput('allow_rate_exfleet_pct', p, allow[p] / (ar[p] + allow[p] - fa) * 100)
    sput('fleetAP_share_of_AP_accr_pct', p, fp / (ap[p] + accr[p]) * 100)
    sput('AP_accr_exfleet_pct_rev', p, (ap[p] + accr[p] - fp) / rev[p] * 100)
for k in ('DSO_end_exfleet', 'AP_accr_exfleet_pct_rev', 'allow_rate_exfleet_pct'):
    for p in Q[4:]:
        b = Q[Q.index(p) - 4]; sput('chg_' + k, p, S[k][p] - S[k][b])
    for p in ['FY2011', 'FY2012', 'FY2013']:
        b = 'FY' + str(int(p[-4:]) - 1); sput('chg_' + k, p, S[k][p] - S[k][b])
for k in S:
    print(k.ljust(30), {p: round(v, 2) for p, v in S[k].items()})

# (2) Public liability and property damage reserve (EXTRA, BS) as % of annual revenue
pl = extra("Public liability and property damage", "BS")
PL = {p: pl[p] / rev[p] * 100 for p in A}
print('PLPD_pct_rev', {p: round(v, 2) for p, v in PL.items()})

# (3) Restructuring accrual: non-payment reductions ("Other") as % of pre-tax income (text: P21 p.139, P50 p.126, P80 p.141)
RESTR = {  # year: (opening, charges, cash payments, other, closing)
    'FY2010': (29.7, 54.7, -37.4, -29.5, 17.5),
    'FY2011': (17.5, 56.4, -18.4, -33.9, 21.6),
    'FY2012 (FY2012 10-K)': (21.6, 38.0, -26.8, -11.8, 21.0),
    'FY2012 (FY2013 10-K)': (21.6, 38.0, -36.8, -1.8, 21.0),
    'FY2013': (21.0, 77.0, -48.6, -1.0, 48.4)}
PTI = {'FY2010': pti['FY2010'], 'FY2011': pti['FY2011'], 'FY2012 (FY2012 10-K)': pti['FY2012'],
       'FY2012 (FY2013 10-K)': 441.4, 'FY2013': pti['FY2013']}   # 441.4 = FY2012 pre-tax as revised, P68 p.84
for y, (o, c, cp, oth, cl) in RESTR.items():
    chk = o + c + cp + oth - cl
    print('restr', y, 'rollforward check', round(chk, 2), 'other/PTI %',
          round(-oth / PTI[y] * 100, 2) if PTI[y] > 0 else 'n/m (pre-tax loss)', 'other/opening %', round(-oth / o * 100, 1))
print('restr 2012 diff between filings: cash', round(-36.8 - -26.8, 1), 'other', round(-1.8 - -11.8, 1))

# (4) Allowance: cash-flow provision vs Schedule II charged to expense
cf_prov = extra("Provision for losses on doubtful accounts", "CF")
for p in A:
    print('provision CF vs SchII', p, cf_prov[p], NOTES.loc['Allowance: provision', p], round(cf_prov[p] - NOTES.loc['Allowance: provision', p], 2))
print('FY2013 CF 45.9 vs Sch II 41.9:', round(45.9 - 41.9, 2), '| FY2012 revised CF 38.3 vs Sch II 38.3:', round(38.3 - 38.3, 2))
print('FY2012 Sch II original vs revised: charged', round(38.3 - 34.1, 1), 'closing', round(29.3 - 25.1, 1))
print('FY2013 provision as % of revenue (CF basis)', round(45.9 / rev['FY2013'] * 100, 3), '(Sch II basis)', round(41.9 / rev['FY2013'] * 100, 3))

# (5) Purchases-based DPO test: |change in inventory| > 10% of period cost?
print('max |dInv|/DO %', max(abs(v) for v in R['dInv_pct_of_DO'].values() if v is not None))

# (6) Pairings
pairs = []
for p in Q[4:] + A[1:]:
    ga, gi = R['gap_AR_rev'][p], R['gap_inv_dop'][p]
    if ga is not None and ga > 0 and gi is not None and gi < 0:
        pairs.append(('1 AR>rev & inv<cost', p, ga, gi))
    if p.startswith('Q4') or p.startswith('FY'):
        ce, ca = R['chg_DSO_end'][p], R['chg_DSO_avg'][p]
        if ce is not None and ca is not None and ce > ca and ce > 0:
            pairs.append(('2 year-end DSO end rising faster than avg', p, ce, ca))
    m, dio = R['margin_chg_pp'][p], R['chg_DIO_end'][p]
    if m is not None and m > 0 and dio is not None and dio > 0:
        pairs.append(('3 margin proxy up & DIO up', p, m, dio))
    al, ds = R['chg_allow_rate_pct'][p], R['chg_DSO_end'][p]
    if al is not None and al < 0 and ds is not None and ds > 0:
        pairs.append(('4 allowance rate down & DSO up', p, al, ds))
for x in pairs:
    print('PAIR', x[0], '|', x[1], '|', round(x[2], 2), '|', round(x[3], 2))
# pairing 4 on the ex-fleet basis for FY2011
print('FY2011 ex-fleet: allowance rate chg', S['chg_allow_rate_exfleet_pct']['FY2011'], 'DSO ex-fleet chg', S['chg_DSO_end_exfleet']['FY2011'])
print('Donlen receivables 64.0 in days of FY2011 revenue', round(64.0 / rev['FY2011'] * 365, 2))

# (7) Row triggers
ADV = {'DSO_end': 1, 'DSO_avg': 1, 'DSO_gap': 1, 'allow_rate_pct': -1, 'DIO_end': 1, 'DIO_avg': 1, 'DPO_end': 1, 'DPO_avg': 1,
       'accr_intensity_pct': -1, 'writeoff_coverage': 1, 'CCC_end': 1, 'CCC_avg': 1}
GAPS = ['gap_AR_rev', 'gap_inv_dop', 'gap_ap_dop']
def trig(series, periods, sign):
    vals = [(p, series.get(p)) for p in periods if series.get(p) is not None]
    if not vals: return 'no values in this series'
    latest_p, latest = vals[-1]
    a = all(sign * latest >= sign * v for _, v in vals)
    run = 0
    for p, v in reversed(vals):
        b = yoy_base(p)
        if b is None or series.get(b) is None: break
        if sign * (v - series[b]) > 0: run += 1
        else: break
    return latest_p, round(latest, 2), 'a' if a else '-', 'run', run
for k, sgn in ADV.items():
    for per in (Q, A):
        print('TRIG', k, trig(R[k], per, sgn))
for k in GAPS:
    for per in (Q, A):
        vals = [(p, R[k][p]) for p in per if R[k].get(p) is not None]
        lp, lv = vals[-1]
        a = all(lv >= v for _, v in vals)
        run = 0
        for p, v in reversed(vals):
            if v > 0: run += 1
            else: break
        print('TRIG', k, lp, round(lv, 2), 'a' if a else '-', 'consecutive positive', run, 'c(>10pp)', lv > 10)
print('TRIG PLPD_pct_rev', trig(PL, A, -1))
S_A = ['FY2010', 'FY2011', 'FY2012', 'FY2013']
print('TRIG AP_accr_exfleet_pct_rev (annual)', trig(S['AP_accr_exfleet_pct_rev'], S_A, -1))
print('TRIG AP_accr_exfleet_pct_rev (qtr)', trig(S['AP_accr_exfleet_pct_rev'], Q, -1))
print('TRIG DSO_end_exfleet (qtr)', trig(S['DSO_end_exfleet'], Q, 1))
print('TRIG allow_rate_exfleet (qtr)', trig(S['allow_rate_exfleet_pct'], Q, -1))

# (8) C18: payables balance and DPO at Q3 -> Q4 -> next Q1
for y in (2011, 2012):
    q3, q4, q1 = f'Q3 FY{y}', f'Q4 FY{y}', f'Q1 FY{y+1}'
    print('C18', y, 'AP', ap[q3], ap[q4], ap[q1], 'rise at YE', ap[q4] > ap[q3], 'fall next Q', ap[q1] < ap[q4],
          '| DPO', round(R['DPO_end'][q3], 1), round(R['DPO_end'][q4], 1), round(R['DPO_end'][q1], 1),
          'rise', R['DPO_end'][q4] > R['DPO_end'][q3], 'fall', R['DPO_end'][q1] < R['DPO_end'][q4])
print('C18 2013 AP', ap['Q3 FY2013'], ap['Q4 FY2013'], 'DPO', round(R['DPO_end']['Q3 FY2013'], 1),
      round(R['DPO_end']['Q4 FY2013'], 1), '(no Q1 FY2014 in pack)')
```

`f2_text.py`

```python
# Text searches and wording comparisons for F2 (steps 1, 2, 3, 5)
import re
from collections import Counter
from packlib import search, text, page_at, textfiles

def norm(s): return re.sub(r'[^a-z0-9 ]', '', re.sub(r'\s+', ' ', s.lower()))

# A4: allowance policy paragraph, FY2011 / FY2012 / FY2013 10-K Note 2
paras = {}
for pid in ('P11', 'P39', 'P68'):
    t = text(pid); i = t.find('Receivables are stated net of allowances'); j = t.find('statements of operations', i)
    paras[pid] = (page_at(t, i), t[i:j + len('statements of operations')])
    print(pid, 'p.', paras[pid][0], '::', paras[pid][1].replace('\n', ' '))
print('A4 identical after normalising punctuation:', len({norm(v[1]) for v in paras.values()}) == 1)

# A17 context: fleet cost policy wording by year
for pid in ('P11', 'P39', 'P68'):
    hits = search(r'stated at cost, net of related discounts', [pid], ctx=0)
    print('A17 policy', pid, [(h[0], h[2]) for h in hits])

# Search lists named in the prompt; counts over all 298 text files (P2 to P299)
LISTS = {
 'step 2 (A8)': ['bill-and-hold', 'bill and hold', 'held for customer', 'customer requested', 'delivery at a later date',
                 'consignment', 'right of return', 'extended payment terms', 'early shipment', 'pull forward'],
 'step 3 (A7)': ['factor', 'securitiz', 'securitis', 'sale of receivables', 'sold receivables', 'derecogni',
                 'transferred financial assets', 'supply chain finance', 'supplier finance'],
 'step 5 (A17)': ['rebate', 'allowance', 'vendor consideration', 'supplier consideration', 'upfront payment', 'prebate',
                  'volume incentive'],
 'extra (A12, A13, A15, A16)': ['LIFO', 'last-in', 'first-in', 'obsolete', 'obsolescence', 'write-down of inventor',
                  'inventory reserve', 'confirmed obligations', 'payment terms', 'vendor terms', 'vendor incentive',
                  'contract asset', 'unbilled', 'performance obligation', 'factoring', 'factored']}
print('text files searched:', len(textfiles()))
for g, terms in LISTS.items():
    for term in terms:
        flags = 0 if term == 'LIFO' else re.I
        hits = search(re.escape(term) if term != 'LIFO' else r'\bLIFO\b', flags=flags, ctx=120)
        files = sorted(Counter(h[0] for h in hits), key=lambda p: int(p[1:]))
        print(f'{g} | {term!r} | {len(hits)} hits | {len(files)} files | {files[:12]}{" ..." if len(files) > 12 else ""}')

# 'factor' hits: are any about receivables?
fr = [h for h in search(r'factor', ctx=80) if re.search(r'receivab', h[3], re.I)]
print("'factor' hits with 'receivab' within 80 chars:", [(h[0], h[2]) for h in fr])
# 'securitiz' hits with 'receivab' within 250 chars
sr = [h for h in search(r'securitiz', ctx=250) if re.search(r'receivab', h[3], re.I)]
print("'securitiz' hits with 'receivab' within 250 chars:", [(h[0], h[2]) for h in sr])
# 'allowance' hits outside doubtful-accounts and tax valuation contexts
ah = [h for h in search(r'allowance', ctx=60) if not re.search(r'doubtful|valuation allowance|tax', h[3], re.I)]
print("'allowance' hits not about doubtful accounts or tax:", Counter(h[0] for h in ah).most_common())
for h in ah[:12]: print('   ', h[0], h[2], h[3][:170].replace('\n', ' '))
```

`f2_tables.py`

```python
# Build the markdown computation tables from the computed series (no hand arithmetic)
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    from f2_part2 import *          # runs f2_compute and f2_part2 silently
import pandas as pd

QS = [p.replace(' FY', ' ') for p in Q]
def cell(v, nd):
    if v is None or (isinstance(v, float) and pd.isna(v)): return ''
    return f'{float(v):,.{nd}f}'
def table(rows, periods, heads, extra_col=None):
    h = '| Item | ' + ' | '.join(heads) + (' | ' + extra_col[0] if extra_col else '') + ' | Formula |'
    s = '|---|' + '---:|' * len(heads) + ('---:|' if extra_col else '') + '---|'
    out = [h, s]
    for name, series, nd, formula, *ex in rows:
        line = f'| {name} | ' + ' | '.join(cell(series.get(p), nd) for p in periods)
        if extra_col: line += ' | ' + (cell(ex[0], nd) if ex and ex[0] is not None else '')
        out.append(line + f' | {formula} |')
    return '\n'.join(out)

raw = lambda d: {p: d[p] for p in d}
AP_ = ['FY2009', 'FY2010', 'FY2011', 'FY2012', 'FY2013']
rv12 = R['rev12']; f13 = R['fy13_vs_rev12']
T = {}
T['recv_q'] = table([
    ('Revenue [P1, IS_Q]', rev, 1, 'copied'),
    ('Receivables, net [P1, BS_Q]', ar, 1, 'copied'),
    ('Allowance [P1, BS_Q]', allow, 1, 'copied'),
    ('Days in quarter', DAYS, 0, 'calendar days'),
    ('DSO ending (days)', R['DSO_end'], 1, 'Rec net ÷ Revenue × days'),
    ('DSO average (days)', R['DSO_avg'], 1, '((opening + closing) ÷ 2) ÷ Revenue × days'),
    ('DSO gap (days)', R['DSO_gap'], 1, 'ending − average'),
    ('Revenue growth YoY (%)', R['g_rev'], 1, 'Rev ÷ Rev same quarter prior year − 1'),
    ('Gross receivables growth YoY (%)', R['g_grossAR'], 1, '(net + allowance) ÷ same, prior year − 1'),
    ('Gross receivables growth minus revenue growth (pp)', R['gap_AR_rev'], 1, 'difference of the two lines above'),
    ('Allowance rate (%)', R['allow_rate_pct'], 2, 'Allowance ÷ (net + allowance)'),
    ('Fleet-disposal receivables [text, see note]', {p: SUP[('fleetAR', p)] for p in Q}, 1, 'copied, converted to millions'),
    ('Fleet-disposal receivables share of net receivables (%)', S['fleetAR_share_pct'], 1, 'fleet-disposal ÷ Rec net'),
    ('DSO ending excluding fleet-disposal receivables (days)', S['DSO_end_exfleet'], 1, '(Rec net − fleet-disposal) ÷ Revenue × days'),
    ('Allowance rate excluding fleet-disposal receivables (%)', S['allow_rate_exfleet_pct'], 2, 'Allowance ÷ (gross − fleet-disposal)'),
], Q, QS)
T['recv_a'] = table([
    ('Revenue [P1, IS_A]', rev, 1, 'copied', REV12['rev']),
    ('Receivables, net [P1, BS_A]', ar, 1, 'copied', REV12['ar']),
    ('Allowance [P1, BS_A; FY2009 from NOTES]', allow, 1, 'copied', REV12['allow']),
    ('DSO ending (days)', R['DSO_end'], 1, 'Rec net ÷ Revenue × 365 (366 in 2012)', rv12['DSO_end']),
    ('DSO average (days)', R['DSO_avg'], 1, 'average balance ÷ Revenue × days', None),
    ('DSO gap (days)', R['DSO_gap'], 1, 'ending − average', None),
    ('Revenue growth YoY (%)', R['g_rev'], 1, 'year over year', None),
    ('Gross receivables growth YoY (%)', R['g_grossAR'], 1, 'year over year', None),
    ('Gross receivables growth minus revenue growth (pp)', R['gap_AR_rev'], 1, 'difference', None),
    ('Allowance rate (%)', R['allow_rate_pct'], 2, 'Allowance ÷ gross receivables', rv12['allow_rate_pct']),
    ('Provision [P1, NOTES]', NOTES.loc['Allowance: provision', AP_].to_dict(), 1, 'copied (Schedule II charged to expense)', 38.3),
    ('Write-offs, net of recoveries [P1, NOTES]', (-NOTES.loc['Allowance: write-offs', AP_]).to_dict(), 1, 'copied (Schedule II deductions)', 29.3),
    ('Write-off coverage (x)', R['writeoff_coverage'], 2, 'write-offs ÷ provision', 29.3 / 38.3),
    ('Provision, cash flow statement [P1, EXTRA]', {p: cf_prov[p] for p in AP_}, 1, 'copied', 38.3),
    ('Fleet-disposal receivables [text]', {p: SUP[('fleetAR', p)] for p in ['FY2010', 'FY2011', 'FY2012', 'FY2013']}, 1, 'copied', 618.6),
    ('DSO ending excluding fleet-disposal receivables (days)', S['DSO_end_exfleet'], 1, '(Rec net − fleet-disposal) ÷ Revenue × days', (REV12['ar'] - 618.6) / REV12['rev'] * 366),
], AP_, AP_, extra_col=('FY2012 as revised',))
T['inv_q'] = table([
    ('Direct operating (cost base) [P1, EXTRA]', dop, 1, 'copied; substitute for COGS'),
    ('Inventory, net [P1, BS_Q]', inv, 1, 'copied'),
    ('DIO ending, direct-operating basis (days)', R['DIO_end'], 1, 'Inventory ÷ Direct operating × days'),
    ('DIO average, direct-operating basis (days)', R['DIO_avg'], 1, 'average inventory ÷ Direct operating × days'),
    ('Inventory growth YoY (%)', R['g_inv'], 1, 'year over year, same quarter'),
    ('Direct operating growth YoY (%)', R['g_dop'], 1, 'year over year, same quarter'),
    ('Inventory growth minus direct operating growth (pp)', R['gap_inv_dop'], 1, 'difference'),
    ('Change in inventory as % of direct operating', R['dInv_pct_of_DO'], 2, '(closing − opening) ÷ Direct operating'),
    ('Margin proxy (%)', R['margin_proxy_pct'], 1, '(Revenue − Direct operating − Fleet depreciation and lease charges) ÷ Revenue'),
    ('Margin proxy change YoY (pp)', R['margin_chg_pp'], 1, 'same quarter prior year'),
    ('DIO ending change YoY (days)', R['chg_DIO_end'], 1, 'same quarter prior year'),
], Q, QS)
T['inv_a'] = table([
    ('Direct operating [P1, EXTRA]', dop, 1, 'copied', REV12['dop']),
    ('Inventory, net [P1, BS_A]', inv, 1, 'copied', REV12['inv']),
    ('DIO ending (days)', R['DIO_end'], 1, 'Inventory ÷ Direct operating × days', rv12['DIO_end']),
    ('DIO average (days)', R['DIO_avg'], 1, 'average ÷ Direct operating × days', None),
    ('Inventory growth minus direct operating growth (pp)', R['gap_inv_dop'], 1, 'difference', None),
    ('Margin proxy (%)', R['margin_proxy_pct'], 1, 'as quarterly', rv12['margin_proxy_pct']),
    ('Margin proxy change YoY (pp)', R['margin_chg_pp'], 1, 'year over year', None),
], AP_, AP_, extra_col=('FY2012 as revised',))
T['pay_q'] = table([
    ('Accounts payable [P1, BS_Q]', ap, 1, 'copied'),
    ('Accrued liabilities [P1, BS_Q]', accr, 1, 'copied'),
    ('DPO ending, direct-operating basis (days)', R['DPO_end'], 1, 'Payables ÷ Direct operating × days'),
    ('DPO average, direct-operating basis (days)', R['DPO_avg'], 1, 'average payables ÷ Direct operating × days'),
    ('Payables growth YoY (%)', R['g_ap'], 1, 'year over year, same quarter'),
    ('Payables growth minus direct operating growth (pp)', R['gap_ap_dop'], 1, 'difference'),
    ('Accrued-liability intensity (%)', R['accr_intensity_pct'], 1, 'Accrued ÷ quarter revenue'),
    ('Fleet purchases in payables and accruals [text, see note]', {p: SUP[('fleetAP', p)] for p in Q}, 1, 'copied, converted to millions'),
    ('Fleet purchases share of payables + accruals (%)', S['fleetAP_share_of_AP_accr_pct'], 1, 'fleet purchases ÷ (AP + accrued)'),
    ('Payables + accruals excluding fleet purchases, % of quarter revenue', S['AP_accr_exfleet_pct_rev'], 1, '(AP + accrued − fleet purchases) ÷ Revenue'),
], Q, QS)
T['pay_a'] = table([
    ('Accounts payable [P1, BS_A]', ap, 1, 'copied', REV12['ap']),
    ('Accrued liabilities [P1, BS_A]', accr, 1, 'copied', REV12['accr']),
    ('DPO ending (days)', R['DPO_end'], 1, 'Payables ÷ Direct operating × days', rv12['DPO_end']),
    ('DPO average (days)', R['DPO_avg'], 1, 'average ÷ Direct operating × days', None),
    ('Payables growth minus direct operating growth (pp)', R['gap_ap_dop'], 1, 'difference', None),
    ('Accrued-liability intensity (%)', R['accr_intensity_pct'], 2, 'Accrued ÷ annual revenue', rv12['accr_intensity_pct']),
    ('Payables + accruals excl. fleet purchases, % of revenue', S['AP_accr_exfleet_pct_rev'], 2, '(AP + accrued − fleet purchases) ÷ Revenue', (REV12['ap'] + REV12['accr'] - 247.0) / REV12['rev'] * 100),
    ('Public liability and property damage reserve [P1, EXTRA]', {p: pl[p] for p in AP_}, 1, 'copied', 332.2),
    ('Reserve ÷ revenue (%)', PL, 2, 'reserve ÷ annual revenue', 332.2 / REV12['rev'] * 100),
], AP_, AP_, extra_col=('FY2012 as revised',))
T['ccc_q'] = table([
    ('DSO ending', R['DSO_end'], 1, 'from receivables table'),
    ('DIO ending (direct-operating basis)', R['DIO_end'], 1, 'from inventory table'),
    ('DPO ending (direct-operating basis)', R['DPO_end'], 1, 'from payables table'),
    ('CCC ending (days)', R['CCC_end'], 1, 'DSO + DIO − DPO, ending'),
    ('DSO average', R['DSO_avg'], 1, ''),
    ('DIO average', R['DIO_avg'], 1, ''),
    ('DPO average', R['DPO_avg'], 1, ''),
    ('CCC average (days)', R['CCC_avg'], 1, 'DSO + DIO − DPO, average'),
], Q, QS)
T['ccc_a'] = table([
    ('DSO ending', R['DSO_end'], 1, ''), ('DIO ending', R['DIO_end'], 1, ''), ('DPO ending', R['DPO_end'], 1, ''),
    ('CCC ending (days)', R['CCC_end'], 1, 'DSO + DIO − DPO'),
    ('DSO average', R['DSO_avg'], 1, ''), ('DIO average', R['DIO_avg'], 1, ''), ('DPO average', R['DPO_avg'], 1, ''),
    ('CCC average (days)', R['CCC_avg'], 1, 'DSO + DIO − DPO'),
], AP_, AP_)
# FY2013 against FY2012 as revised (same basis)
T['fy13'] = '\n'.join(['| Item | FY2013 vs FY2012 as revised | Formula |', '|---|---:|---|'] + [
    f'| {n} | {v:,.1f} | {fm} |' for n, v, fm in [
        ('Revenue growth (%)', f13['g_rev'], 'FY2013 ÷ 9,024.9 − 1'),
        ('Gross receivables growth (%)', f13['g_grossAR'], '(1,512.6 + 30.8) ÷ (1,879.7 + 29.3) − 1'),
        ('Gross receivables minus revenue growth (pp)', f13['gap_AR_rev'], 'difference'),
        ('Inventory minus direct operating growth (pp)', f13['gap_inv_dop'], 'direct operating FY2012 revised 4,806.0'),
        ('Payables minus direct operating growth (pp)', f13['gap_ap_dop'], 'payables FY2012 revised 1,003.2'),
        ('DSO average FY2013 on revised opening (days)', f13['DSO_avg'], '((1,879.7 + 1,512.6) ÷ 2) ÷ 10,771.9 × 365'),
        ('DPO average FY2013 on revised opening (days)', f13['DPO_avg'], '((1,003.2 + 967.9) ÷ 2) ÷ 5,752.0 × 365')]])
# Restructuring
rows = ['| Year (source) | Opening | Charges | Cash payments | Other (non-payment) | Closing | Other ÷ pre-tax income (%) | Other ÷ opening (%) |',
        '|---|---:|---:|---:|---:|---:|---:|---:|']
for y, (o, c, cp, oth, cl) in RESTR.items():
    pr = f'{-oth / PTI[y] * 100:.2f}' if PTI[y] > 0 else 'n/m (pre-tax loss)'
    rows.append(f'| {y} | {o:.1f} | {c:.1f} | {cp:.1f} | {oth:.1f} | {cl:.1f} | {pr} | {-oth / o * 100:.1f} |')
T['restr'] = '\n'.join(rows)
if __name__ == '__main__':
    for k, v in T.items():
        print('=====', k); print(v)
```

`f2_extra.py`

```python
# Small figures quoted in ledger rows, all computed here
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    from f2_part2 import *
ta = {**BSA.loc['Total assets', A].to_dict(), **BSQ.loc['Total assets', Q].to_dict()}
print('inventory % of total assets FY2011', round(inv['FY2011'] / ta['FY2011'] * 100, 2), 'FY2013', round(inv['FY2013'] / ta['FY2013'] * 100, 2))
print('FY2011 growth: inventory', round(R['g_inv']['FY2011'], 2), 'direct operating', round(R['g_dop']['FY2011'], 2),
      'gross AR', round(R['g_grossAR']['FY2011'], 2), 'revenue', round(R['g_rev']['FY2011'], 2))
print('restructuring: 10.3 facility-closure decrease as % of FY2012 pre-tax (orig 450.5)', round(10.3 / pti['FY2012'] * 100, 2))
print('accrued: FY2011 split in FY2012 10-K: salaries 426.696 + other 701.762 =', round(426.696 + 701.762, 1),
      '| FY2012: 440.936 + 739.602 =', round(440.936 + 739.602, 1))
print('accrued intensity FY2013 minus FY2011 (pp)', round(R['accr_intensity_pct']['FY2013'] - R['accr_intensity_pct']['FY2011'], 2),
      '| FY2013 minus FY2012 revised', round(R['accr_intensity_pct']['FY2013'] - R['rev12']['accr_intensity_pct'], 2))
print('accrued at FY2012-revised intensity on FY2013 revenue', round(R['rev12']['accr_intensity_pct'] / 100 * rev['FY2013'], 1),
      'difference vs reported', round(R['rev12']['accr_intensity_pct'] / 100 * rev['FY2013'] - accr['FY2013'], 1))
print('accrued interest change FY2012->FY2013 (P71 p.114)', round(73.8 - 88.5, 1))
print('PL&PD: FY2013 vs FY2012 pp', round(PL['FY2013'] - PL['FY2012'], 2), 'vs FY2011', round(PL['FY2013'] - PL['FY2011'], 2))
print('Q3 2013 provision vs Q3 2012 (P1 CF_Q/NOTES):', NOTES.loc['Allowance: provision', 'Q3 FY2013'], NOTES.loc['Allowance: provision', 'Q3 FY2012'],
      round(NOTES.loc['Allowance: provision', 'Q3 FY2013'] - NOTES.loc['Allowance: provision', 'Q3 FY2012'], 1))
print('2013 quarters: payables-minus-DO gap range', round(min(R['gap_ap_dop'][p] for p in Q[8:]), 1), round(max(R['gap_ap_dop'][p] for p in Q[8:]), 1),
      '| DPO end YoY changes', [round(R['chg_DPO_end'][p], 1) for p in Q[8:]])
print('CF changes FY2013 vs FY2012 revised: payables 23.2 vs 34.0 diff', round(23.2 - 34.0, 1), '| accrued 25.2 vs -29.6 diff', round(25.2 - -29.6, 1))
print('Q1 2013 allowance vs Q4 2012 original', round(allow['Q1 FY2013'] - allow['Q4 FY2012'], 1))
print('vendor incentives 2011+2012 pre-tax', round(12.9 + 2.4, 1))
```

`ledger.py`

```python
# F2 ledger rows. Figures in Evidence are copied from the computation output of f2_compute.py, f2_part2.py and f2_extra.py.
COLS = ['ID', 'Item', 'Period', 'Evidence', 'Locator', 'Benign reading', 'Adverse reading', 'Context',
        'Resolving disclosure', 'Priority', 'Verdict']
ROWS = [
 ['F2-A1-01', 'A1 DSO, ending against average at fiscal year end (pairing 2)', 'Q4 FY2012; FY2011',
  'Trigger: step 7 pairing. Q4 FY2012 ending DSO 74.9 days against 73.8 in Q4 FY2011 (+1.0), while average DSO fell from 82.5 to 71.8 (-10.7) [calc]. FY2011 ending DSO 71.1 against 65.5 in FY2010 (+5.6), average 65.4 against 64.7 (+0.7) [calc].',
  'P1 BS_Q and IS_Q Q4 FY2011, Q4 FY2012; P1 BS_A and IS_A FY2010, FY2011; Receivables table',
  'The Q4 FY2012 balance sheet carries Dollar Thrifty receivables (170 at acquisition) against 43 days of its revenue, and the FY2011 balance sheet carries Donlen receivables (64.0) against four months of its revenue [inf: context sheet E2, E9]. Fleet-disposal receivables from manufacturers were 32.7% and 38.4% of net receivables at those dates [calc] and track vehicle returns, not revenue. Excluding them, FY2011 ending DSO rose 2.7 days, close to the 2.8 days of FY2011 revenue that Donlen receivables represent [calc].',
  'If the acquisitions and fleet-disposal timing do not account for the rise, receivables at year end grew faster than the business in a way consistent with billing concentrated at the end of the year.',
  'E9 (Q4 FY2012); E2 (FY2011); E24 revised FY2012 receivables by -7.0; W4: FY2011 and FY2012 cells are pre-revision',
  'Receivables by type (customer, manufacturer, other) and acquired receivables outstanding at each year end; not in pack [not found: P9, P37, P66 balance sheets and notes give one receivables line]',
  'P4', ''],
 ['F2-A2-01', 'A2 and A10 receivables up faster than revenue while inventory falls faster than cost (pairing 1)', 'FY2011',
  'Trigger: step 7 pairing. Gross receivables growth 18.9% against revenue growth 9.7% (+9.2 pp); inventory growth -3.9% against direct operating growth 6.6% (-10.5 pp) [calc]. Cost base is direct operating, not COGS (no COGS line).',
  'P1 BS_A, IS_A, EXTRA (Direct operating) FY2010, FY2011; Receivables and Inventory tables',
  'The goods-billed-not-shipped shape does not fit a rental business: revenue is "recognized over the period the revenue earning equipment is rented or leased" [P68, p. 90], and inventory, 0.48% of total assets [calc], is fuel, parts and equipment held for sale [inf: P107, p. 44; P68, p. 90]. The receivables rise matches Donlen (64.0) and fleet-disposal receivables rising from 504.2 to 620.7 [P9, p. 90].',
  'If Donlen and fleet-disposal receivables do not account for the rise, customer receivables grew about twice as fast as revenue in FY2011.',
  'E2, E3; W4: FY2011 is pre-revision (E24)',
  'Receivables by type at FY2010 and FY2011; not in pack [not found: P9, P11]',
  'P4', ''],
 ['F2-A3-01', 'A3 allowance rate falling while DSO rises (pairing 4)', 'FY2011',
  'Trigger: step 7 pairing. Allowance rate 1.24% against 1.43% in FY2010 (-0.19 pp) while ending DSO rose 5.6 days; excluding fleet-disposal receivables the rate is 2.00% against 2.26% (-0.26 pp) and DSO rose 2.7 days [calc].',
  'P1 BS_A FY2010, FY2011; P1 NOTES FY2010, FY2011; P9, p. 90 (fleet-disposal receivables); Receivables table',
  'Donlen receivables entered the balance sheet at acquisition in September 2011 and would carry little allowance so soon after purchase, diluting the rate while adding to DSO [inf: context sheet E2; P1 NOTES].',
  'The company later corrected "allowances for doubtful accounts in Brazil" that reduced pre-tax income by $6.2 million in 2011 together with certain asset charges [P68, p. 83]; the 2011 fall in the rate may partly reflect that under-provision.',
  'E2; E24 (Brazil allowances); W4',
  'Allowance by country or segment, and the Brazil allowance amount separate from "charges related to certain assets"; not in pack [not found: P66, P68, P86, P295 searched for "Brazil" and "doubtful"]',
  'P4', ''],
 ['F2-A3-02', 'A3 bad-debt provision: cash flow statement against Schedule II', 'FY2013',
  'The FY2013 cash flow statement shows "Provision for losses on doubtful accounts" of 45.9; Schedule II in the same 10-K shows 2013 "Charged to Expense" 41.9; difference 4.0 [calc]. The 2012 (38.3 and 38.3) and 2011 (28.2 and 28.2) comparatives agree [calc]. Q3 FY2013 provision 17.0 against 9.9 in Q3 FY2012 [P1, NOTES].',
  'P66, p. 80; P86, p. 158; P1 EXTRA and NOTES FY2013',
  'The cash-flow line may cover provisions on amounts outside the trade-receivable allowance, for example amounts owed by Simply Wheelz, whose parent in October 2013 "requested that Hertz forbear from seeking collection of all amounts owed to it by Simply Wheelz" [P66, p. 101]; the manifest notes the two figures can differ [P0, "How statements.xlsx is made"].',
  'If both lines describe the same allowance, 4.0 of 2013 bad-debt expense did not pass through the allowance rollforward, or the rollforward is incomplete.',
  'E10 (Simply Wheelz); E24 (2012 allowance revised); Q4 FY2013 derived on mixed basis',
  'Reconciliation of the cash-flow provision to Schedule II; not found [P66, P86, P62, P70 searched for "doubtful" and "Simply Wheelz"]',
  'P3', ''],
 ['F2-A4-01', 'A4 allowance method and factors; Brazil allowance correction', 'FY2011 to FY2013 (method); FY2010 to FY2012 (correction)',
  'Method text is the same in all three 10-Ks: "The estimate of the allowance for doubtful accounts is based on our historical experience and our judgment as to the likelihood of ultimate payment." [P11, p. 93; P39, p. 81; P68, p. 90; calc: text comparison]. Correction: "charges related to certain assets and allowances for doubtful accounts in Brazil (reduced pre-tax income by $4.4 million in 2010, $6.2 million in 2011 and $3.6 million in 2012)" [P68, p. 83]. Schedule II 2012 charged to expense 34.1 as first reported, 38.3 as revised; closing allowance 25.1 against 29.3 (+4.2) [calc; P56; P86]. The revision table places the 2011 and 2012 Brazil adjustments in the "Direct operating" line ("Primarily consists of $6.2 million adjustment related to Brazil.") [P68, p. 85], while the policy says "Bad debt expense is reflected as a component of \'Selling, general and administrative\' in our consolidated statements of operations." [P68, p. 90]; the allowance share of the Brazil amount is not given.',
  'P11, p. 93; P39, p. 81; P68, pp. 83, 90; P56, p. 140; P86, p. 158',
  'The method did not change; the company found under-provision in one country, corrected it with period tables and judged it immaterial [P68, p. 83].',
  'The allowance was understated in one country for three years under an unchanged method description, so the stated method did not capture that exposure; the Brazil allowance amount alone is not given.',
  'E24',
  'Brazil allowance amount by year; not in pack [not found: P66, P68, P295, P296]',
  'P4', ''],
 ['F2-A7-01', 'A7 receivable transfers: securitization hits are fleet financing', 'FY2011 to FY2013',
  'Search hit (text rows always become rows). "securitiz" has 726 hits in 75 files; the only hit within 250 characters of "receivab" is a call slide [P270, p. 38] [calc]. Example: "The European Securitization is the primary fleet financing for our car rental operations in France and The Netherlands." [P71, p. 112]. "Substantially all of our revenue earning equipment and certain related assets are owned by special purpose entities, or are encumbered in favor of our lenders under our various credit facilities." [P71, p. 114]. No sale, factoring or derecognition of receivables found [calc].',
  'P71, pp. 112, 114; P270, p. 38',
  'The programmes are asset-backed fleet debt through consolidated entities; receivables stay on the balance sheet, so no DSO add-back applies [inf: P71].',
  'The "certain related assets" encumbered under fleet facilities could include manufacturer receivables; if any were sold rather than pledged, DSO would be understated. Nothing in the pack indicates a sale.',
  'none',
  'Collateral schedule of each fleet facility; not in pack beyond the debt note',
  'P3', ''],
 ['F2-A11-01', 'A11 inventory reported as a single line, no cost method or reserve', 'FY2011 to FY2013',
  'The balance sheet shows one line, "Inventories, at lower of cost or market" (92.3 at FY2013) [P66, p. 75]; no classes, cost-flow method, reserve or write-down found [not found: 298 text files searched for "LIFO", "last-in", "first-in", "obsolescence", "inventory reserve", "write-down of inventor"]. Inventory is 0.38% of total assets at FY2013 [calc].',
  'P66, p. 75; P9, p. 86; P37, p. 72',
  'Inventory is immaterial for a rental company and is mainly fuel and parts, as in "gasoline and parts inventory purchases" [P107, p. 44].',
  'Without the cost method and any obsolescence reserve, DIO movements cannot be split between volume and valuation, and a write-down or reversal would be invisible.',
  'E9 (8 of inventory acquired with Dollar Thrifty)',
  'Inventory note with classes and cost method; not in pack. Whether Regulation S-X requires it at this size is [unverified: the regulation is not in the pack]',
  'P3', ''],
 ['F2-A13-01', 'A13 margin proxy up while DIO rises (pairing 3)', 'Q2, Q3, Q4 FY2012; FY2012; Q2 FY2013',
  'Trigger: step 7 pairing. Margin proxy change against the same period a year earlier: Q2 FY2012 +0.8 pp, Q3 FY2012 +1.2, Q4 FY2012 +0.9, FY2012 +1.0, Q2 FY2013 +1.4; DIO change +0.1, +0.9, +0.5, +1.4, +0.5 days [calc]. Proxy = (revenue - direct operating - fleet depreciation and lease charges) / revenue, because there is no gross margin line.',
  'P1 IS_Q, IS_A, EXTRA (Direct operating; Depreciation of revenue earning equipment and lease charges), BS_Q, BS_A; Inventory table',
  'Fleet depreciation fell from depreciation-rate changes (car rental -130.6 in 2012) [inf: context sheet E22]; in the paired periods DIO rose by 1.4 days or less, on inventory of 84.0 to 128.3 across the series [calc]; Dollar Thrifty added inventory in Q4 FY2012 [inf: context sheet E9].',
  'If rate changes do not account for the margin gain, cost could be held on the balance sheet; inventory is too small to hold material cost here, so the place to test that reading is fleet carrying value (F3, F4) [inf: P1 BS_Q].',
  'E22, E9; E24 moved vendor incentives between SG&A and fleet depreciation, so P1 2012 cost lines are pre-revision (W4)',
  'Depreciation-rate change effects by quarter; the pack has annual amounts only [P45, p. 113; P74, p. 126]',
  'P4', ''],
 ['F2-A14-01', 'A14 MD&A attributes cash from operations to "timing of our payments"', 'FY2013',
  'Text row. "The increase was primarily a result of higher earnings before interest, depreciation and amortization as well as due to the timing of our payments." [P62, p. 64]. In each 2013 quarter, payables growth ran 18.4 to 25.2 pp below direct operating growth and ending DPO fell against the same quarter of 2012 (-20.9, -17.7, -14.8, -12.9 days) [calc]. Cash flow change in accrued liabilities +25.2 against -29.6 in FY2012 as revised (+54.8); payables +23.2 against +34.0 (-10.8) [calc; P66, p. 80].',
  'P62, p. 64; P66, p. 80; Payables table',
  'The payment timing the MD&A refers to shows in accrued liabilities (a 54.8 swing), not in trade payables, so the sentence and the payables trend are consistent [inf: P66, P62].',
  'If "timing of our payments" means deferral of payments to suppliers, it does not show in the balance-sheet payables, which fell relative to cost; the source of the timing benefit is not identified.',
  'E9 (Dollar Thrifty full year in 2013); W4; Q4 FY2013 direct operating derived on mixed basis',
  'Breakdown of the cash-flow effect of payment timing by liability; not in pack [not found: P62, P66]',
  'P3', ''],
 ['F2-A16-01', 'A16 accrued-liability intensity', 'FY2013',
  'Triggers (a) and (b). Two independent signals: the ratio trend, and less line detail in the same year. Accrued liabilities / revenue 10.26% in FY2013 against 13.09% FY2012 as first reported, 12.89% as revised, 13.60% FY2011 and 14.43% FY2009: lowest in the series and down four years running [calc]. At the FY2012 revised intensity, FY2013 accruals would be 1,388.2 against 1,104.7 reported (283.5 lower) [calc]. Payables plus accruals excluding fleet purchases / revenue 16.56% against 21.27% FY2012 as revised, and down against the same quarter a year earlier in seven consecutive quarters, Q2 FY2012 to Q4 FY2013 [calc]. The FY2013 balance sheet shows one "Accrued liabilities" line where the FY2011 and FY2012 10-Ks split "Accrued salaries and other compensation" from "Other accrued liabilities" [P66, p. 75; P37, p. 72; P9, p. 86]. The revision table cites "$3.1 million adjustments related to under accruals" for nine months 2013 [P68, p. 87].',
  'P1 BS_A and IS_A FY2009 to FY2013; P1 RESTATED FY2012; P66, p. 75; P68, p. 87; Payables table',
  'The FY2012 balance sheet held Dollar Thrifty accruals (298 at acquisition) against 43 days of its revenue, and FY2013 has a full year of its revenue [inf: context sheet E9, E21]; accrued interest fell from 88.5 to 73.8 [P71, p. 114]; integration and transaction accruals would run off after the acquisition [inf: context sheet E9].',
  'Accruals falling relative to activity to below the pre-acquisition level can reflect expenses not yet recorded, which raises reported income; the company itself identified under-accruals in 2013, and the FY2013 balance sheet gives less detail on this line than the two prior years.',
  'E9, E21, E24; W4; the context sheet does not explain a fall below the pre-acquisition FY2011 level',
  'Accrued liabilities by component at FY2012 and FY2013; not in pack [not found: P66, P68, P62 searched for "accrued salaries" and "other accrued"]',
  'P2', ''],
 ['F2-A16-02', 'A16 public liability and property damage reserve relative to revenue', 'FY2013',
  'Trigger (a). Reserve / revenue 3.23% in FY2013 against 3.68% FY2012 and 3.39% FY2011; lowest in FY2009 to FY2013 [calc]. The critical-estimates text reads "Reserve requirements are based on rental volume and actuarial evaluations" from the FY2012 10-K [P34, p. 45; P63, p. 45], against "Reserve requirements are based on actuarial evaluations" in FY2011 [P6, p. 53] and in the FY2013 notes [P68, p. 92]. No rollforward found.',
  'P1 EXTRA (Public liability and property damage) FY2009 to FY2013; P6, p. 53; P34, p. 45; P63, p. 45; P68, p. 92',
  'The FY2012 reserve included Dollar Thrifty (line 281.5 to 332.2) against 43 days of its revenue [inf: context sheet E9]; the reserve is actuarial and "Our actual results as compared to our estimates have historically resulted in relatively minor adjustments to our recorded liability." [P63, p. 45]; revenue growth includes price as well as volume [inf: P62].',
  'If claims exposure grew with the fleet, a reserve growing more slowly than revenue could reflect a lower estimate that raises income; without a rollforward, releases cannot be seen.',
  'E9',
  'Reserve rollforward (provisions, payments, prior-year development); not found [P62, P63, P68, P79 searched for "public liability and property damage" near "reserve"]',
  'P3', ''],
 ['F2-A16-03', 'A16 restructuring accrual: 2012 rollforward reprinted with different movements', 'FY2012',
  'FY2012 10-K: 2012 cash payments (26.8), other (11.8), "Primarily consists of decreases of $10.3 million for facility closures and $1.0 million in ASC 715 pension adjustment." [P50, p. 126]. FY2013 10-K: 2012 cash payments (36.8), other (1.8), "Primarily consists of decreases of $0.5 million related to a goodwill write-off on a sale of business and $1.0 million in ASC 715 pension adjustment." [P80, p. 141]. 10.0 moved from non-payment reductions to cash payments; opening, charges and closing unchanged [calc]. Non-payment reductions / pre-tax income: FY2011 10.45%, FY2012 2.62% as first reported and 0.41% as reprinted, FY2013 0.15% [calc]; the 10.3 facility-closure decrease equals 2.29% of FY2012 pre-tax income as first reported [calc].',
  'P50, p. 126; P80, p. 141; P21, p. 139; P1 IS_A',
  'A reclassification: "Certain prior period amounts have been reclassified to conform with current year presentation." [P68, p. 83]; facility-closure amounts may have been settled in cash and first shown as other reductions.',
  'If the first description was right, 2012 included a 10.3 reduction of the facility-closure reserve that was not a payment, and the reprint removes the trace of it.',
  'E24 (FY2012 revised; restructuring not itemised)',
  'Reconciliation of the two 2012 rollforwards; not found [P80, P68, P66 searched for "restructuring" and "reclassif"]',
  'P3', ''],
 ['F2-A17-01', 'A17 supplier consideration: vendor incentives classified against marketing expense', 'FY2011 to Q3 FY2013',
  '"These recorded pre-tax adjustments relate to vendor incentives (reduced pre-tax income by $12.9 million in 2011 and $2.4 million in 2012) which had been accounted for as a reduction of marketing expenses instead of reducing the cost of revenue earning equipment" [P68, p. 83]. Revision footnotes: 2012 fleet depreciation "$23.6 million adjustment related to vendor incentives", SG&A "$25.9 million" [P68, p. 85]; nine months 2013 "$22.1 million" and "$21.2 million" [P68, p. 87]. The policy sentence "Revenue earning equipment is stated at cost, net of related discounts." appears from the FY2012 10-K [P39, p. 81; P68, p. 91] and not in FY2011 [calc: search of P11].',
  'P68, pp. 83, 85, 87, 91; P39, p. 81; P11',
  'A classification error between fleet cost and marketing expense, found and corrected with period tables; the net pre-tax effect is the timing difference between an immediate credit to SG&A and a credit through fleet depreciation [P68, pp. 83 to 87].',
  'Supplier consideration taken to income at once instead of reducing asset cost raised pre-tax income by 12.9 in 2011 and 2.4 in 2012; the same treatment may affect fleet carrying values and disposal gains beyond the amounts corrected.',
  'E24; W4 (P1 2011 to Q3 2013 cost lines are pre-revision)',
  'Amount of vendor incentives received by year and a policy on supplier consideration; not found [298 text files searched for "rebate", "vendor consideration", "supplier consideration", "volume incentive", "upfront payment", "prebate"]',
  'P4', ''],
]
```

`build.py`

```python
# Assemble F2-output.md and ledger-F2.csv from the template, the computed tables and the ledger rows
import io, csv, contextlib, re, os
with contextlib.redirect_stdout(io.StringIO()):
    from f2_tables import T
from ledger import COLS, ROWS

OUT = r"C:/Users/aaron/OneDrive/Desktop/Master/WireSift Research/Events/CFA Vancouver Forensic/tests/hertz-fy2013/runs/v0.2-claude-code"
tpl = open('template.md', encoding='utf-8').read()
for k, v in T.items():
    tpl = tpl.replace('{{' + k + '}}', v.replace('| -0.0 |', '| 0.0 |'))

# ledger: markdown and CSV from the same rows
def md_cell(s): return s.replace('|', '/').replace('\n', ' ')
md = ['| ' + ' | '.join(COLS) + ' |', '|' + '---|' * len(COLS)]
md += ['| ' + ' | '.join(md_cell(c) for c in r) + ' |' for r in ROWS]
buf = io.StringIO(); w = csv.writer(buf, lineterminator='\n'); w.writerow(COLS); w.writerows(ROWS)
csv_text = buf.getvalue().rstrip('\n')
tpl = tpl.replace('{{ledger_md}}', '\n'.join(md)).replace('{{ledger_csv}}', csv_text)
open(os.path.join(OUT, 'ledger-F2.csv'), 'w', encoding='utf-8', newline='').write(csv_text + '\n')

# figure counts for the verification line: numeric cells in the computation tables
copied = calc = 0
for name, t in T.items():
    for line in t.split('\n')[2:]:
        cells = [c.strip() for c in line.strip('|').split('|')]
        formula = cells[-1]
        nums = [c for c in cells[1:-1] if re.fullmatch(r'-?[\d,]+(\.\d+)?', c)]
        if name == 'restr':
            copied += 5 * (len(nums) > 0); calc += max(len(nums) - 5, 0)
        elif formula.startswith('copied'):
            copied += len(nums)
        else:
            calc += len(nums)
pri = [r[9] for r in ROWS]
ver = (f"`Verification: 15 items run (5 of them only on a direct-operating substitute for COGS), "
       f"{len(ROWS)} ledger rows (P1 {pri.count('P1')}, P2 {pri.count('P2')}, P3 {pri.count('P3')}, P4 {pri.count('P4')}), 4 could not run. "
       f"Figures: {copied} copied, {calc} calculated, 0 unverified (computation-table cells; figures in prose and ledger rows repeat table cells or quote the filings). "
       f"Units: USD, millions. Framework: US GAAP. Context sheet: used.`")
tpl = tpl.replace('{{verification}}', ver)

# code section: every script in the order run
order = ['packlib.py', 'exploratory_log.py', 's1_counts.py', 's_ocf.py', 's_inc.py', 's_inv.py', 's_supp.py',
         'f2_compute.py', 'f2_part2.py', 'f2_text.py', 'f2_tables.py', 'f2_extra.py', 'ledger.py', 'build.py']
code = []
for f in order:
    code.append(f'`{f}`\n\n```python\n' + open(f, encoding='utf-8').read().rstrip() + '\n```')
tpl = tpl.replace('{{code}}', '\n\n'.join(code))
open(os.path.join(OUT, 'F2-output.md'), 'w', encoding='utf-8').write(tpl)
print('written', len(tpl), 'chars;', len(tpl.split()), 'words; copied', copied, 'calc', calc)
```

## 10. Verification

`Verification: 15 items run (5 of them only on a direct-operating substitute for COGS), 13 ledger rows (P1 0, P2 1, P3 6, P4 6), 4 could not run. Figures: 204 copied, 525 calculated, 0 unverified (computation-table cells; figures in prose and ledger rows repeat table cells or quote the filings). Units: USD, millions. Framework: US GAAP. Context sheet: used.`

**Candidates for review, not findings.**
