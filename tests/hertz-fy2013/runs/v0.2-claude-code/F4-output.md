# Disclosure deltas and consistency: Hertz Global Holdings, Inc., FY2011 to FY2013

## 1. Header

```
Company:     Hertz Global Holdings, Inc. (SEC CIK 1364479), NYSE: HTZ [P0, header table]
Framework:   US GAAP [P0, header table; context sheet, Basis]
Currency:    USD [P0]
Units:       statements.xlsx (P1) in USD millions; FY2011 and FY2012 10-K and Q1 2011 to Q1 2013 10-Q text in
             USD thousands; FY2013 10-K, Q2 and Q3 2013 10-Q and release tables in USD millions [P0, header table].
             Every figure below is in USD millions unless a quotation shows thousands.
Fiscal year: ends 31 December [P0]
As of:       31 March 2014 [P0]
Compared:    10-K FY2011 to FY2012 to FY2013 (section by section); 10-Q same quarter year over year
             (Q1, Q2, Q3: 2011 to 2012 to 2013; notes read for substance, all sections counted); earnings
             releases and call slides same quarter year over year; proxy 2012 to 2013 (counted only)
Context:     context-sheet.md attached and used (events E1 to E26 cited below)
Checklist:   the checklist file is not in the pack. Row IDs follow the F4 method text: D2 risk factors,
             D3 consistency pass, D4 related parties, C10 legal, C13 critical estimates, C14 auditor,
             A8 revenue, A4 working capital, C7 PP&E and intangibles, C6 provisions, C2 non-GAAP, C16 revisions.
             D1 (section measurement) and D5 (MD&A) produced no rows of their own.
```

## 2. Summary

- **Sections compared.** 188 section pairs were measured in code: 57 annual 10-K pairs, 112 interim 10-Q pairs, 18 release and slide pairs, 1 proxy pair; 20 items have no pair (15 section files that appear or disappear, 3 one-off releases, events.txt, the workbook) [calc, s1_sectionmap.py]. Across all pairs the code found 11,036 added, 9,701 removed and 14,358 changed sentences, of which 6,462 changed sentences differ only in numbers or dates, 126 only in note numbers or cross-references, and 1,879 are near-identical wording [calc, s5_map.py].
- **Substantive changes.** Section 4 quotes 25 substantive changes before and after in tables, in the step 2 order, and describes the auditor, MD&A, interim-note and revision items in text; with the consistency results they give the ledger rows [inf: section 4].
- **Consistency checks.** All 10 checks were run. Inconsistent: check 2 (useful lives and holding periods), check 3 (explanations of the fleet depreciation movement, four periods) and check 7 (recurring charges under a non-recurring label). Consistent: checks 1 and 10. Cannot test: checks 4, 5, 6, 8 and 9, each for a named missing number or because no sentence of the type exists [calc and search, s3_search.py, s4_checks.py].
- **Rows by priority.** 33 ledger rows: P1 7, P2 2, P3 19, P4 5 [calc, s7_ledger.py].
- The strongest cluster sits in one account, fleet depreciation in 2013: the explanations given for lower depreciation cite strong or improved residual values while the same filings report vehicle disposals moving from gains to losses, depreciation per unit of gross fleet fell in every 2013 quarter, the disclosed car holding-period range widened to 36 months, and the critical-estimate text on residual values changed [inf: P62, P74, P213, P225, P234, P246, P254, P266, P63, P68]. These are candidates for review, not findings.

## 3. Section map

Counts come from s1_sectionmap.py (sentence split, exact match, then closest match with word similarity of 0.5 or more counts as changed). The mechanical column shows what the code could attribute (number or date roll-forward, note renumbering, near-identical wording) and the context-sheet events that rewrite the section. Counts describe the size of a change; they do not grade it.

| Section | Filing pair | Sentences added | Removed | Changed | Mechanical cause, if any |
|---|---|---|---|---|---|
| auditor-report | P8 AR-FY2011 to P36 AR-FY2012 | 2 | 1 | 6 | 1 changed = number or date roll-forward; 3 near-identical wording (ratio 0.9 or more); events: E9 ICFR scope exclusion |
| business | P2 AR-FY2011 to P30 AR-FY2012 | 96 | 47 | 126 | 39 changed = number or date roll-forward; 1 = note renumbering or cross-reference; 34 near-identical wording (ratio 0.9 or more); events: E9 |
| controls | P28 AR-FY2011 to P57 AR-FY2012 | 0 | 0 | 6 | 4 changed = number or date roll-forward; 1 = note renumbering or cross-reference; events: E9 ICFR scope exclusion |
| critical-estimates | P6 AR-FY2011 to P34 AR-FY2012 | 12 | 7 | 25 | 1 changed = number or date roll-forward; 14 near-identical wording (ratio 0.9 or more) |
| financial-statements | P9 AR-FY2011 to P37 AR-FY2012 | 523 | 391 | 827 | 389 changed = number or date roll-forward; 8 = note renumbering or cross-reference; 131 near-identical wording (ratio 0.9 or more); events: E9 |
| legal | P4 AR-FY2011 to P32 AR-FY2012 | 41 | 19 | 32 | 9 changed = number or date roll-forward; 11 near-identical wording (ratio 0.9 or more) |
| market-risk | P7 AR-FY2011 to P35 AR-FY2012 | 0 | 0 | 11 | 5 changed = number or date roll-forward; 1 near-identical wording (ratio 0.9 or more) |
| mdna | P5 AR-FY2011 to P33 AR-FY2012 | 196 | 232 | 278 | 85 changed = number or date roll-forward; 4 = note renumbering or cross-reference; 58 near-identical wording (ratio 0.9 or more); events: E9 |
| notes-01-background | P10 AR-FY2011 to P38 AR-FY2012 | 7 | 4 | 11 | 4 near-identical wording (ratio 0.9 or more) |
| notes-02-summary-of-significant-accounting-policies | P11 AR-FY2011 to P39 AR-FY2012 | 52 | 51 | 32 | 5 changed = number or date roll-forward; 1 = note renumbering or cross-reference; 12 near-identical wording (ratio 0.9 or more); events: E4 revision dropped, E7 |
| notes-03-goodwill-and-other-intangible-assets | P12 AR-FY2011 to P40 AR-FY2012 | 39 | 58 | 16 | 9 changed = number or date roll-forward; 4 near-identical wording (ratio 0.9 or more); events: E2 Donlen, E9 Dollar Thrifty |
| notes-05-debt | P13 AR-FY2011 to P42 AR-FY2012 | 85 | 65 | 114 | 33 changed = number or date roll-forward; 36 near-identical wording (ratio 0.9 or more); events: E9, E13 |
| notes-06-employee-retirement-benefits | P14 AR-FY2011 to P43 AR-FY2012 | 21 | 43 | 113 | 55 changed = number or date roll-forward; 1 = note renumbering or cross-reference; 12 near-identical wording (ratio 0.9 or more) |
| notes-07-stock-based-compensation | P15 AR-FY2011 to P44 AR-FY2012 | 30 | 20 | 45 | 24 changed = number or date roll-forward; 3 = note renumbering or cross-reference; 6 near-identical wording (ratio 0.9 or more) |
| notes-08-depreciation-of-revenue-earning-equipment-and | P16 AR-FY2011 to P45 AR-FY2012 | 1 | 1 | 11 | 5 changed = number or date roll-forward; 1 = note renumbering or cross-reference |
| notes-09-taxes-on-income | P17 AR-FY2011 to P46 AR-FY2012 | 4 | 5 | 66 | 39 changed = number or date roll-forward; 1 = note renumbering or cross-reference; 2 near-identical wording (ratio 0.9 or more) |
| notes-10-lease-and-concession-agreements | P18 AR-FY2011 to P47 AR-FY2012 | 8 | 8 | 19 | 17 changed = number or date roll-forward |
| notes-11-segment-information | P19 AR-FY2011 to P48 AR-FY2012 | 9 | 23 | 82 | 60 changed = number or date roll-forward; 1 = note renumbering or cross-reference; 7 near-identical wording (ratio 0.9 or more); events: E2, E9 |
| notes-12-contingencies-and-off-balance-sheet-commitments | P20 AR-FY2011 to P49 AR-FY2012 | 22 | 12 | 20 | 5 changed = number or date roll-forward; 7 near-identical wording (ratio 0.9 or more) |
| notes-13-restructuring | P21 AR-FY2011 to P50 AR-FY2012 | 11 | 7 | 32 | 14 changed = number or date roll-forward; 3 = note renumbering or cross-reference; 4 near-identical wording (ratio 0.9 or more) |
| notes-14-financial-instruments | P22 AR-FY2011 to P51 AR-FY2012 | 62 | 53 | 24 | 8 changed = number or date roll-forward; 2 = note renumbering or cross-reference; 7 near-identical wording (ratio 0.9 or more) |
| notes-15-related-party-transactions | P23 AR-FY2011 to P52 AR-FY2012 | 5 | 3 | 14 | 3 changed = number or date roll-forward; 5 near-identical wording (ratio 0.9 or more) |
| notes-16-earnings-per-share | P24 AR-FY2011 to P53 AR-FY2012 | 0 | 3 | 13 | 3 changed = number or date roll-forward; 1 = note renumbering or cross-reference; 3 near-identical wording (ratio 0.9 or more); events: E13 |
| notes-17-quarterly-financial-information-unaudited | P25 AR-FY2011 to P54 AR-FY2012 | 1 | 1 | 7 | 3 changed = number or date roll-forward |
| notes-18-subsequent-events | P26 AR-FY2011 to P55 AR-FY2012 | 6 | 2 | 1 | 1 changed = number or date roll-forward |
| related-parties | P29 AR-FY2011 to P58 AR-FY2012 | 5 | 3 | 16 | 5 changed = number or date roll-forward; 5 near-identical wording (ratio 0.9 or more) |
| risk-factors | P3 AR-FY2011 to P31 AR-FY2012 | 53 | 9 | 37 | 1 changed = number or date roll-forward; 19 near-identical wording (ratio 0.9 or more); events: E9 merger risk to integration risk |
| schedule-ii | P27 AR-FY2011 to P56 AR-FY2012 | 3 | 3 | 7 | 2 near-identical wording (ratio 0.9 or more) |
| auditor-report | P36 AR-FY2012 to P65 AR-FY2013 | 1 | 5 | 4 | 1 = note renumbering or cross-reference; 2 near-identical wording (ratio 0.9 or more); events: E9 exclusion ends, E19 |
| business | P30 AR-FY2012 to P59 AR-FY2013 | 79 | 61 | 146 | 42 changed = number or date roll-forward; 69 near-identical wording (ratio 0.9 or more); events: E9, E10, E15, E17, E18, E24; units thousands to millions |
| controls | P57 AR-FY2012 to P87 AR-FY2013 | 1 | 2 | 4 | 3 changed = number or date roll-forward; 1 near-identical wording (ratio 0.9 or more); events: E9 exclusion ends, E19 |
| critical-estimates | P34 AR-FY2012 to P63 AR-FY2013 | 7 | 0 | 17 | 3 changed = number or date roll-forward; 11 near-identical wording (ratio 0.9 or more) |
| financial-statements | P37 AR-FY2012 to P66 AR-FY2013 | 844 | 430 | 738 | 354 changed = number or date roll-forward; 3 = note renumbering or cross-reference; 94 near-identical wording (ratio 0.9 or more); events: E9, E10, E15, E17, E18, E24; units thousands to millions |
| legal | P32 AR-FY2012 to P61 AR-FY2013 | 25 | 117 | 15 | 8 changed = number or date roll-forward; 1 = note renumbering or cross-reference; 2 near-identical wording (ratio 0.9 or more); events: Item 3 now cross-refers to note 13 (duplicate text removed) |
| market-risk | P35 AR-FY2012 to P64 AR-FY2013 | 0 | 0 | 9 | 3 changed = number or date roll-forward; 1 = note renumbering or cross-reference; 3 near-identical wording (ratio 0.9 or more) |
| mdna | P33 AR-FY2012 to P62 AR-FY2013 | 357 | 205 | 275 | 85 changed = number or date roll-forward; 2 = note renumbering or cross-reference; 54 near-identical wording (ratio 0.9 or more); events: E9, E10, E15, E17, E18, E24; units thousands to millions |
| notes-01-background | P38 AR-FY2012 to P67 AR-FY2013 | 10 | 3 | 2 | none |
| notes-02-summary-of-significant-accounting-policies | P39 AR-FY2012 to P68 AR-FY2013 | 183 | 13 | 19 | 6 changed = number or date roll-forward; 4 near-identical wording (ratio 0.9 or more); events: E24 revision, E17, E18 segment recast |
| notes-03-goodwill-and-other-intangible-assets | P40 AR-FY2012 to P69 AR-FY2013 | 21 | 19 | 30 | 10 changed = number or date roll-forward; 8 near-identical wording (ratio 0.9 or more); events: E9, E10, E21 |
| notes-04-business-combinations-and-divestitures | P41 AR-FY2012 to P70 AR-FY2013 | 22 | 14 | 38 | 21 changed = number or date roll-forward; 9 near-identical wording (ratio 0.9 or more); events: E9, E10, E21 |
| notes-05-debt | P42 AR-FY2012 to P71 AR-FY2013 | 120 | 32 | 99 | 50 changed = number or date roll-forward; 17 near-identical wording (ratio 0.9 or more); events: E9 Dollar Thrifty debt, E23 |
| notes-06-employee-retirement-benefits | P43 AR-FY2012 to P72 AR-FY2013 | 25 | 15 | 104 | 62 changed = number or date roll-forward; 6 near-identical wording (ratio 0.9 or more) |
| notes-07-stock-based-compensation | P44 AR-FY2012 to P73 AR-FY2013 | 29 | 29 | 53 | 23 changed = number or date roll-forward; 10 near-identical wording (ratio 0.9 or more) |
| notes-08-depreciation-of-revenue-earning-equipment-and | P45 AR-FY2012 to P74 AR-FY2013 | 4 | 1 | 9 | 4 changed = number or date roll-forward; 1 near-identical wording (ratio 0.9 or more) |
| notes-09-taxes-on-income | P46 AR-FY2012 to P75 AR-FY2013 | 19 | 23 | 52 | 33 changed = number or date roll-forward; 3 near-identical wording (ratio 0.9 or more) |
| notes-10-lease-and-concession-agreements | P47 AR-FY2012 to P76 AR-FY2013 | 14 | 14 | 12 | 9 changed = number or date roll-forward; 1 near-identical wording (ratio 0.9 or more) |
| notes-11-segment-information | P48 AR-FY2012 to P77 AR-FY2013 | 84 | 41 | 51 | 22 changed = number or date roll-forward; 3 near-identical wording (ratio 0.9 or more); events: E18 segment recast |
| notes-13-contingencies-and-off-balance-sheet-commitments | P49 AR-FY2012 to P79 AR-FY2013 | 25 | 34 | 15 | 7 changed = number or date roll-forward; 1 = note renumbering or cross-reference; 3 near-identical wording (ratio 0.9 or more); events: Item 3 now cross-refers to note 13 (duplicate text removed) |
| notes-14-restructuring | P50 AR-FY2012 to P80 AR-FY2013 | 8 | 6 | 30 | 18 changed = number or date roll-forward; 2 near-identical wording (ratio 0.9 or more) |
| notes-15-financial-instruments-and-fair-value | P51 AR-FY2012 to P81 AR-FY2013 | 76 | 8 | 29 | 12 changed = number or date roll-forward; 9 near-identical wording (ratio 0.9 or more) |
| notes-16-related-party-transactions | P52 AR-FY2012 to P82 AR-FY2013 | 11 | 33 | 4 | 1 changed = number or date roll-forward; 1 near-identical wording (ratio 0.9 or more); events: E20 Stockholders Agreement terminated |
| notes-17-earnings-per-share | P53 AR-FY2012 to P83 AR-FY2013 | 13 | 0 | 12 | 4 changed = number or date roll-forward; 4 near-identical wording (ratio 0.9 or more); events: E13 convertible notes |
| notes-18-quarterly-financial-information-unaudited | P54 AR-FY2012 to P84 AR-FY2013 | 6 | 5 | 10 | 6 changed = number or date roll-forward; events: E24 revision, unit change thousands to millions |
| notes-19-subsequent-events | P55 AR-FY2012 to P85 AR-FY2013 | 6 | 6 | 1 | 1 changed = number or date roll-forward |
| related-parties | P58 AR-FY2012 to P88 AR-FY2013 | 11 | 33 | 6 | 3 changed = number or date roll-forward; 1 near-identical wording (ratio 0.9 or more); events: E20 Stockholders Agreement terminated |
| risk-factors | P31 AR-FY2012 to P60 AR-FY2013 | 14 | 35 | 21 | 1 changed = number or date roll-forward; 11 near-identical wording (ratio 0.9 or more); events: E10, E20, E26 |
| schedule-ii | P56 AR-FY2012 to P86 AR-FY2013 | 5 | 4 | 3 | events: E24 revision, unit change thousands to millions |
| financial-statements | P89 Q1-FY2011 to P148 Q1-FY2012 | 168 | 170 | 304 | 184 changed = number or date roll-forward; 3 = note renumbering or cross-reference; 34 near-identical wording (ratio 0.9 or more); events: E2, E6 |
| mdna | P107 Q1-FY2011 to P166 Q1-FY2012 | 115 | 90 | 207 | 90 changed = number or date roll-forward; 24 near-identical wording (ratio 0.9 or more); events: E2, E6 |
| notes-01-background | P90 Q1-FY2011 to P149 Q1-FY2012 | 2 | 0 | 1 | 1 near-identical wording (ratio 0.9 or more) |
| notes-02-basis-of-presentation-and-recently-issued | P91 Q1-FY2011 to P150 Q1-FY2012 | 6 | 2 | 5 | 2 changed = number or date roll-forward; 1 near-identical wording (ratio 0.9 or more); events: E4, E7, E11, E17, E18 |
| notes-03-cash-and-cash-equivalents-and-restricted-cash | P92 Q1-FY2011 to P151 Q1-FY2012 | 0 | 0 | 2 | 1 changed = number or date roll-forward |
| notes-04-goodwill-and-other-intangible-assets | P93 Q1-FY2011 to P152 Q1-FY2012 | 28 | 21 | 19 | 10 changed = number or date roll-forward; 2 near-identical wording (ratio 0.9 or more); events: E2, E6, E9, E10, E15 |
| notes-05-taxes-on-income | P94 Q1-FY2011 to P153 Q1-FY2012 | 1 | 0 | 2 | none |
| notes-06-depreciation-of-revenue-earning-equipment-and | P95 Q1-FY2011 to P154 Q1-FY2012 | 6 | 1 | 9 | 6 changed = number or date roll-forward |
| notes-07-debt | P96 Q1-FY2011 to P155 Q1-FY2012 | 35 | 58 | 53 | 32 changed = number or date roll-forward; 5 near-identical wording (ratio 0.9 or more); events: E9, E13 |
| notes-08-employee-retirement-benefits | P97 Q1-FY2011 to P156 Q1-FY2012 | 7 | 3 | 12 | 5 changed = number or date roll-forward; 1 near-identical wording (ratio 0.9 or more) |
| notes-09-stock-based-compensation | P98 Q1-FY2011 to P157 Q1-FY2012 | 4 | 2 | 9 | 3 changed = number or date roll-forward; 2 = note renumbering or cross-reference; 1 near-identical wording (ratio 0.9 or more) |
| notes-10-segment-information | P99 Q1-FY2011 to P158 Q1-FY2012 | 3 | 6 | 20 | 11 changed = number or date roll-forward; 5 near-identical wording (ratio 0.9 or more); events: E2, E9 |
| notes-11-total-equity | P100 Q1-FY2011 to P159 Q1-FY2012 | 4 | 14 | 12 | 5 changed = number or date roll-forward; 3 near-identical wording (ratio 0.9 or more) |
| notes-12-restructuring | P101 Q1-FY2011 to P160 Q1-FY2012 | 4 | 12 | 27 | 20 changed = number or date roll-forward; 3 = note renumbering or cross-reference |
| notes-13-financial-instruments | P102 Q1-FY2011 to P161 Q1-FY2012 | 16 | 21 | 25 | 8 changed = number or date roll-forward; 3 near-identical wording (ratio 0.9 or more) |
| notes-14-related-party-transactions | P103 Q1-FY2011 to P162 Q1-FY2012 | 0 | 5 | 5 | 2 changed = number or date roll-forward; 1 near-identical wording (ratio 0.9 or more) |
| notes-15-contingencies-and-off-balance-sheet-commitments | P104 Q1-FY2011 to P163 Q1-FY2012 | 13 | 3 | 12 | 3 changed = number or date roll-forward; 6 near-identical wording (ratio 0.9 or more) |
| notes-16-earnings-loss-per-share | P105 Q1-FY2011 to P164 Q1-FY2012 | 0 | 0 | 7 | 6 changed = number or date roll-forward; 1 near-identical wording (ratio 0.9 or more); events: E13 |
| notes-17-subsequent-events | P106 Q1-FY2011 to P165 Q1-FY2012 | 1 | 3 | 0 | none |
| financial-statements | P148 Q1-FY2012 to P206 Q1-FY2013 | 364 | 217 | 321 | 162 changed = number or date roll-forward; 1 = note renumbering or cross-reference; 42 near-identical wording (ratio 0.9 or more); events: E9, E13 |
| mdna | P166 Q1-FY2012 to P225 Q1-FY2013 | 137 | 170 | 232 | 88 changed = number or date roll-forward; 50 near-identical wording (ratio 0.9 or more); events: E9, E13 |
| notes-01-background | P149 Q1-FY2012 to P207 Q1-FY2013 | 8 | 7 | 9 | 3 near-identical wording (ratio 0.9 or more) |
| notes-02-basis-of-presentation-and-recently-issued | P150 Q1-FY2012 to P208 Q1-FY2013 | 12 | 4 | 2 | 1 changed = number or date roll-forward; 1 near-identical wording (ratio 0.9 or more); events: E4, E7, E11, E17, E18 |
| notes-03-cash-and-cash-equivalents-and-restricted-cash | P151 Q1-FY2012 to P209 Q1-FY2013 | 0 | 1 | 3 | 2 changed = number or date roll-forward; 1 near-identical wording (ratio 0.9 or more) |
| notes-04-goodwill-and-other-intangible-assets | P152 Q1-FY2012 to P210 Q1-FY2013 | 23 | 34 | 19 | 10 changed = number or date roll-forward; 2 near-identical wording (ratio 0.9 or more); events: E2, E6, E9, E10, E15 |
| notes-06-taxes-on-income | P153 Q1-FY2012 to P212 Q1-FY2013 | 1 | 1 | 3 | 1 changed = number or date roll-forward |
| notes-07-depreciation-of-revenue-earning-equipment-and | P154 Q1-FY2012 to P213 Q1-FY2013 | 2 | 8 | 8 | 6 changed = number or date roll-forward |
| notes-08-debt | P155 Q1-FY2012 to P214 Q1-FY2013 | 56 | 45 | 54 | 22 changed = number or date roll-forward; 9 near-identical wording (ratio 0.9 or more); events: E9, E13 |
| notes-09-employee-retirement-benefits | P156 Q1-FY2012 to P215 Q1-FY2013 | 5 | 6 | 15 | 5 changed = number or date roll-forward; 3 near-identical wording (ratio 0.9 or more) |
| notes-10-stock-based-compensation | P157 Q1-FY2012 to P216 Q1-FY2013 | 9 | 3 | 11 | 7 changed = number or date roll-forward; 1 near-identical wording (ratio 0.9 or more) |
| notes-11-segment-information | P158 Q1-FY2012 to P217 Q1-FY2013 | 8 | 14 | 21 | 12 changed = number or date roll-forward; 1 near-identical wording (ratio 0.9 or more); events: E2, E9 |
| notes-13-restructuring | P160 Q1-FY2012 to P219 Q1-FY2013 | 9 | 7 | 27 | 16 changed = number or date roll-forward; 4 near-identical wording (ratio 0.9 or more) |
| notes-14-financial-instruments | P161 Q1-FY2012 to P220 Q1-FY2013 | 88 | 32 | 23 | 8 changed = number or date roll-forward; 1 = note renumbering or cross-reference; 5 near-identical wording (ratio 0.9 or more) |
| notes-15-related-party-transactions | P162 Q1-FY2012 to P221 Q1-FY2013 | 3 | 3 | 4 | 4 changed = number or date roll-forward |
| notes-16-contingencies-and-off-balance-sheet-commitments | P163 Q1-FY2012 to P222 Q1-FY2013 | 20 | 10 | 9 | 4 changed = number or date roll-forward; 3 near-identical wording (ratio 0.9 or more) |
| notes-17-earnings-loss-per-share | P164 Q1-FY2012 to P223 Q1-FY2013 | 16 | 1 | 9 | 2 changed = number or date roll-forward; 2 near-identical wording (ratio 0.9 or more); events: E13 |
| notes-18-subsequent-events | P165 Q1-FY2012 to P224 Q1-FY2013 | 17 | 1 | 1 | 1 changed = number or date roll-forward |
| financial-statements | P109 Q2-FY2011 to P167 Q2-FY2012 | 186 | 177 | 376 | 198 changed = number or date roll-forward; 4 = note renumbering or cross-reference; 40 near-identical wording (ratio 0.9 or more); events: E2, E6 |
| mdna | P127 Q2-FY2011 to P185 Q2-FY2012 | 158 | 134 | 347 | 146 changed = number or date roll-forward; 36 near-identical wording (ratio 0.9 or more); events: E2, E6 |
| notes-01-background | P110 Q2-FY2011 to P168 Q2-FY2012 | 4 | 1 | 6 | 1 near-identical wording (ratio 0.9 or more) |
| notes-02-basis-of-presentation-and-recently-issued | P111 Q2-FY2011 to P169 Q2-FY2012 | 3 | 2 | 7 | 2 changed = number or date roll-forward; 2 near-identical wording (ratio 0.9 or more); events: E4, E7, E11, E17, E18 |
| notes-03-cash-and-cash-equivalents-and-restricted-cash | P112 Q2-FY2011 to P170 Q2-FY2012 | 0 | 0 | 2 | 1 changed = number or date roll-forward |
| notes-04-goodwill-and-other-intangible-assets | P113 Q2-FY2011 to P171 Q2-FY2012 | 28 | 20 | 20 | 12 changed = number or date roll-forward; 1 near-identical wording (ratio 0.9 or more); events: E2, E6, E9, E10, E15 |
| notes-05-taxes-on-income | P114 Q2-FY2011 to P172 Q2-FY2012 | 3 | 0 | 3 | 1 changed = number or date roll-forward |
| notes-06-depreciation-of-revenue-earning-equipment-and | P115 Q2-FY2011 to P173 Q2-FY2012 | 0 | 5 | 15 | 10 changed = number or date roll-forward |
| notes-07-debt | P116 Q2-FY2011 to P174 Q2-FY2012 | 37 | 51 | 60 | 33 changed = number or date roll-forward; 6 near-identical wording (ratio 0.9 or more); events: E9, E13 |
| notes-08-employee-retirement-benefits | P117 Q2-FY2011 to P175 Q2-FY2012 | 8 | 3 | 24 | 8 changed = number or date roll-forward; 4 near-identical wording (ratio 0.9 or more) |
| notes-09-stock-based-compensation | P118 Q2-FY2011 to P176 Q2-FY2012 | 4 | 2 | 9 | 3 changed = number or date roll-forward; 2 = note renumbering or cross-reference |
| notes-10-segment-information | P119 Q2-FY2011 to P177 Q2-FY2012 | 4 | 7 | 38 | 25 changed = number or date roll-forward; 3 near-identical wording (ratio 0.9 or more); events: E2, E9 |
| notes-11-total-equity | P120 Q2-FY2011 to P178 Q2-FY2012 | 4 | 17 | 13 | 5 changed = number or date roll-forward; 2 = note renumbering or cross-reference; 2 near-identical wording (ratio 0.9 or more) |
| notes-12-restructuring | P121 Q2-FY2011 to P179 Q2-FY2012 | 3 | 9 | 31 | 17 changed = number or date roll-forward; 3 near-identical wording (ratio 0.9 or more) |
| notes-13-financial-instruments | P122 Q2-FY2011 to P180 Q2-FY2012 | 10 | 26 | 37 | 18 changed = number or date roll-forward; 7 near-identical wording (ratio 0.9 or more) |
| notes-14-related-party-transactions | P123 Q2-FY2011 to P181 Q2-FY2012 | 0 | 2 | 5 | 2 changed = number or date roll-forward; 1 near-identical wording (ratio 0.9 or more) |
| notes-15-contingencies-and-off-balance-sheet-commitments | P124 Q2-FY2011 to P182 Q2-FY2012 | 21 | 5 | 11 | 3 changed = number or date roll-forward; 4 near-identical wording (ratio 0.9 or more) |
| notes-16-earnings-loss-per-share | P125 Q2-FY2011 to P183 Q2-FY2012 | 0 | 4 | 12 | 3 changed = number or date roll-forward; 4 near-identical wording (ratio 0.9 or more); events: E13 |
| notes-17-subsequent-events | P126 Q2-FY2011 to P184 Q2-FY2012 | 2 | 3 | 0 | none |
| financial-statements | P167 Q2-FY2012 to P227 Q2-FY2013 | 429 | 276 | 356 | 167 changed = number or date roll-forward; 2 = note renumbering or cross-reference; 51 near-identical wording (ratio 0.9 or more); events: E9, E15, E17 |
| mdna | P185 Q2-FY2012 to P246 Q2-FY2013 | 210 | 245 | 342 | 140 changed = number or date roll-forward; 51 near-identical wording (ratio 0.9 or more); events: E9, E15, E17 |
| notes-01-background | P168 Q2-FY2012 to P228 Q2-FY2013 | 6 | 19 | 3 | none |
| notes-02-basis-of-presentation-and-recently-issued | P169 Q2-FY2012 to P229 Q2-FY2013 | 21 | 4 | 2 | 1 changed = number or date roll-forward; 1 near-identical wording (ratio 0.9 or more); events: E4, E7, E11, E17, E18 |
| notes-03-cash-and-cash-equivalents-and-restricted-cash | P170 Q2-FY2012 to P230 Q2-FY2013 | 0 | 2 | 2 | none |
| notes-04-goodwill-and-other-intangible-assets | P171 Q2-FY2012 to P231 Q2-FY2013 | 24 | 35 | 19 | 9 changed = number or date roll-forward; 2 near-identical wording (ratio 0.9 or more); events: E2, E6, E9, E10, E15 |
| notes-06-taxes-on-income | P172 Q2-FY2012 to P233 Q2-FY2013 | 2 | 3 | 4 | 1 changed = number or date roll-forward |
| notes-07-depreciation-of-revenue-earning-equipment-and | P173 Q2-FY2012 to P234 Q2-FY2013 | 3 | 2 | 15 | 9 changed = number or date roll-forward |
| notes-08-debt | P174 Q2-FY2012 to P235 Q2-FY2013 | 61 | 46 | 57 | 24 changed = number or date roll-forward; 9 near-identical wording (ratio 0.9 or more); events: E9, E13 |
| notes-09-employee-retirement-benefits | P175 Q2-FY2012 to P236 Q2-FY2013 | 7 | 13 | 23 | 7 changed = number or date roll-forward; 2 near-identical wording (ratio 0.9 or more) |
| notes-10-stock-based-compensation | P176 Q2-FY2012 to P237 Q2-FY2013 | 11 | 4 | 10 | 6 changed = number or date roll-forward; 1 near-identical wording (ratio 0.9 or more) |
| notes-11-segment-information | P177 Q2-FY2012 to P238 Q2-FY2013 | 10 | 16 | 36 | 26 changed = number or date roll-forward; 6 near-identical wording (ratio 0.9 or more); events: E2, E9 |
| notes-13-restructuring | P179 Q2-FY2012 to P240 Q2-FY2013 | 9 | 12 | 23 | 14 changed = number or date roll-forward; 4 near-identical wording (ratio 0.9 or more) |
| notes-14-financial-instruments | P180 Q2-FY2012 to P241 Q2-FY2013 | 109 | 29 | 36 | 12 changed = number or date roll-forward; 2 = note renumbering or cross-reference; 11 near-identical wording (ratio 0.9 or more) |
| notes-15-related-party-transactions | P181 Q2-FY2012 to P242 Q2-FY2013 | 17 | 4 | 4 | 3 changed = number or date roll-forward; events: E20 |
| notes-16-contingencies-and-off-balance-sheet-commitments | P182 Q2-FY2012 to P243 Q2-FY2013 | 10 | 17 | 11 | 4 changed = number or date roll-forward; 2 near-identical wording (ratio 0.9 or more) |
| notes-17-earnings-per-share | P183 Q2-FY2012 to P244 Q2-FY2013 | 14 | 1 | 15 | 3 changed = number or date roll-forward; 5 near-identical wording (ratio 0.9 or more); events: E13 |
| notes-18-subsequent-events | P184 Q2-FY2012 to P245 Q2-FY2013 | 3 | 2 | 1 | 1 changed = number or date roll-forward |
| financial-statements | P129 Q3-FY2011 to P186 Q3-FY2012 | 267 | 304 | 408 | 180 changed = number or date roll-forward; 6 = note renumbering or cross-reference; 65 near-identical wording (ratio 0.9 or more); events: E2, E6 |
| mdna | P146 Q3-FY2011 to P204 Q3-FY2012 | 196 | 201 | 382 | 142 changed = number or date roll-forward; 76 near-identical wording (ratio 0.9 or more); events: E2, E6 |
| notes-01-background | P130 Q3-FY2011 to P187 Q3-FY2012 | 16 | 5 | 7 | 2 near-identical wording (ratio 0.9 or more) |
| notes-02-basis-of-presentation-and-recently-issued | P131 Q3-FY2011 to P188 Q3-FY2012 | 11 | 57 | 7 | 2 changed = number or date roll-forward; 1 near-identical wording (ratio 0.9 or more); events: E4, E7, E11, E17, E18 |
| notes-03-cash-and-cash-equivalents-and-restricted-cash | P132 Q3-FY2011 to P189 Q3-FY2012 | 0 | 5 | 3 | 1 changed = number or date roll-forward; 1 near-identical wording (ratio 0.9 or more) |
| notes-04-goodwill-and-other-intangible-assets | P133 Q3-FY2011 to P190 Q3-FY2012 | 33 | 52 | 23 | 12 changed = number or date roll-forward; 4 near-identical wording (ratio 0.9 or more); events: E2, E6, E9, E10, E15 |
| notes-05-taxes-on-income | P134 Q3-FY2011 to P191 Q3-FY2012 | 0 | 3 | 3 | 1 changed = number or date roll-forward |
| notes-06-depreciation-of-revenue-earning-equipment-and | P135 Q3-FY2011 to P192 Q3-FY2012 | 3 | 2 | 15 | 10 changed = number or date roll-forward |
| notes-07-debt | P136 Q3-FY2011 to P193 Q3-FY2012 | 54 | 73 | 60 | 21 changed = number or date roll-forward; 10 near-identical wording (ratio 0.9 or more); events: E9, E13 |
| notes-08-employee-retirement-benefits | P137 Q3-FY2011 to P194 Q3-FY2012 | 13 | 2 | 27 | 8 changed = number or date roll-forward; 5 near-identical wording (ratio 0.9 or more) |
| notes-09-stock-based-compensation | P138 Q3-FY2011 to P195 Q3-FY2012 | 5 | 7 | 8 | 4 changed = number or date roll-forward; 2 = note renumbering or cross-reference |
| notes-10-segment-information | P139 Q3-FY2011 to P196 Q3-FY2012 | 4 | 15 | 45 | 26 changed = number or date roll-forward; 10 near-identical wording (ratio 0.9 or more); events: E2, E9 |
| notes-11-total-equity | P140 Q3-FY2011 to P197 Q3-FY2012 | 22 | 23 | 18 | 1 changed = number or date roll-forward; 2 = note renumbering or cross-reference; 3 near-identical wording (ratio 0.9 or more) |
| notes-12-restructuring | P141 Q3-FY2011 to P198 Q3-FY2012 | 6 | 8 | 31 | 16 changed = number or date roll-forward; 4 near-identical wording (ratio 0.9 or more) |
| notes-13-financial-instruments | P142 Q3-FY2011 to P199 Q3-FY2012 | 7 | 29 | 43 | 13 changed = number or date roll-forward; 2 = note renumbering or cross-reference; 11 near-identical wording (ratio 0.9 or more) |
| notes-14-related-party-transactions | P143 Q3-FY2011 to P200 Q3-FY2012 | 3 | 2 | 4 | 2 changed = number or date roll-forward |
| notes-15-contingencies-and-off-balance-sheet-commitments | P144 Q3-FY2011 to P201 Q3-FY2012 | 5 | 13 | 9 | 3 changed = number or date roll-forward; 5 near-identical wording (ratio 0.9 or more) |
| notes-16-earnings-per-share | P145 Q3-FY2011 to P202 Q3-FY2012 | 4 | 1 | 15 | 3 changed = number or date roll-forward; 7 near-identical wording (ratio 0.9 or more); events: E13 |
| risk-factors | P147 Q3-FY2011 to P205 Q3-FY2012 | 69 | 2 | 8 | 1 changed = number or date roll-forward; 3 near-identical wording (ratio 0.9 or more); events: E9 |
| financial-statements | P186 Q3-FY2012 to P247 Q3-FY2013 | 540 | 342 | 349 | 150 changed = number or date roll-forward; 42 near-identical wording (ratio 0.9 or more); events: E9, E15, E18 |
| mdna | P204 Q3-FY2012 to P266 Q3-FY2013 | 447 | 277 | 278 | 90 changed = number or date roll-forward; 29 near-identical wording (ratio 0.9 or more); events: E9, E15, E18 |
| notes-01-background | P187 Q3-FY2012 to P248 Q3-FY2013 | 7 | 29 | 3 | none |
| notes-02-basis-of-presentation-and-recently-issued | P188 Q3-FY2012 to P249 Q3-FY2013 | 22 | 16 | 2 | 1 changed = number or date roll-forward; 1 near-identical wording (ratio 0.9 or more); events: E4, E7, E11, E17, E18 |
| notes-03-cash-and-cash-equivalents-and-restricted-cash | P189 Q3-FY2012 to P250 Q3-FY2013 | 3 | 1 | 2 | none |
| notes-04-goodwill-and-other-intangible-assets | P190 Q3-FY2012 to P251 Q3-FY2013 | 25 | 51 | 23 | 6 changed = number or date roll-forward; 6 near-identical wording (ratio 0.9 or more); events: E2, E6, E9, E10, E15 |
| notes-06-taxes-on-income | P191 Q3-FY2012 to P253 Q3-FY2013 | 2 | 0 | 4 | 1 changed = number or date roll-forward |
| notes-07-depreciation-of-revenue-earning-equipment-and | P192 Q3-FY2012 to P254 Q3-FY2013 | 3 | 4 | 15 | 8 changed = number or date roll-forward; 1 near-identical wording (ratio 0.9 or more) |
| notes-08-debt | P193 Q3-FY2012 to P255 Q3-FY2013 | 77 | 47 | 59 | 30 changed = number or date roll-forward; 5 near-identical wording (ratio 0.9 or more); events: E9, E13 |
| notes-09-employee-retirement-benefits | P194 Q3-FY2012 to P256 Q3-FY2013 | 7 | 12 | 19 | 10 changed = number or date roll-forward; 2 near-identical wording (ratio 0.9 or more) |
| notes-10-stock-based-compensation | P195 Q3-FY2012 to P257 Q3-FY2013 | 17 | 4 | 10 | 7 changed = number or date roll-forward; 1 near-identical wording (ratio 0.9 or more) |
| notes-11-segment-information | P196 Q3-FY2012 to P258 Q3-FY2013 | 42 | 17 | 31 | 15 changed = number or date roll-forward; 5 near-identical wording (ratio 0.9 or more); events: E18 segment recast |
| notes-13-restructuring | P198 Q3-FY2012 to P260 Q3-FY2013 | 9 | 11 | 26 | 13 changed = number or date roll-forward; 3 near-identical wording (ratio 0.9 or more) |
| notes-14-financial-instruments-and-fair-value | P199 Q3-FY2012 to P261 Q3-FY2013 | 132 | 29 | 30 | 6 changed = number or date roll-forward; 7 near-identical wording (ratio 0.9 or more) |
| notes-15-related-party-transactions | P200 Q3-FY2012 to P262 Q3-FY2013 | 25 | 3 | 4 | 3 changed = number or date roll-forward; events: E20 |
| notes-16-contingencies-and-off-balance-sheet-commitments | P201 Q3-FY2012 to P263 Q3-FY2013 | 15 | 5 | 12 | 4 changed = number or date roll-forward; 5 near-identical wording (ratio 0.9 or more) |
| notes-17-earnings-per-share | P202 Q3-FY2012 to P264 Q3-FY2013 | 16 | 4 | 11 | 5 changed = number or date roll-forward; 1 near-identical wording (ratio 0.9 or more); events: E13 |
| notes-18-subsequent-events | P203 Q3-FY2012 to P265 Q3-FY2013 | 23 | 16 | 1 | 1 changed = number or date roll-forward |
| risk-factors | P205 Q3-FY2012 to P267 Q3-FY2013 | 8 | 81 | 1 | 1 changed = number or date roll-forward; events: E9 |
| release (ER-Q1-FY2011 / ER-Q1-FY2012) | P271 ER-Q1-FY2011 to P279 ER-Q1-FY2012 | 70 | 100 | 246 | 111 changed = number or date roll-forward; 20 near-identical wording (ratio 0.9 or more); events: E2, E6, E8, E9 |
| release (ER-Q1-FY2012 / ER-Q1-FY2013) | P279 ER-Q1-FY2012 to P287 ER-Q1-FY2013 | 104 | 179 | 231 | 116 changed = number or date roll-forward; 15 near-identical wording (ratio 0.9 or more); events: E9, E10, E13, E14 total RPD, E18 recast |
| release (ER-Q2-FY2011 / ER-Q2-FY2012) | P273 ER-Q2-FY2011 to P281 ER-Q2-FY2012 | 66 | 66 | 341 | 204 changed = number or date roll-forward; 27 near-identical wording (ratio 0.9 or more); events: E2, E6, E8, E9 |
| release (ER-Q2-FY2012 / ER-Q2-FY2013) | P281 ER-Q2-FY2012 to P289 ER-Q2-FY2013 | 128 | 153 | 278 | 148 changed = number or date roll-forward; 13 = note renumbering or cross-reference; 17 near-identical wording (ratio 0.9 or more); events: E9, E10, E13, E14 total RPD, E18 recast |
| release (ER-Q3-FY2011 / ER-Q3-FY2012) | P275 ER-Q3-FY2011 to P283 ER-Q3-FY2012 | 78 | 65 | 332 | 215 changed = number or date roll-forward; 21 near-identical wording (ratio 0.9 or more); events: E2, E6, E8, E9 |
| release (ER-Q3-FY2012 / ER-Q3-FY2013) | P283 ER-Q3-FY2012 to P293 ER-Q3-FY2013 | 309 | 239 | 222 | 98 changed = number or date roll-forward; 1 = note renumbering or cross-reference; 15 near-identical wording (ratio 0.9 or more); events: E9, E10, E13, E14 total RPD, E18 recast |
| release (ER-Q4-FY2010 / ER-Q4-FY2011) | P269 ER-Q4-FY2010 to P277 ER-Q4-FY2011 | 134 | 305 | 365 | 85 changed = number or date roll-forward; 10 = note renumbering or cross-reference; 18 near-identical wording (ratio 0.9 or more); events: E2, E4 |
| release (ER-Q4-FY2011 / ER-Q4-FY2012) | P277 ER-Q4-FY2011 to P285 ER-Q4-FY2012 | 88 | 62 | 369 | 209 changed = number or date roll-forward; 1 = note renumbering or cross-reference; 22 near-identical wording (ratio 0.9 or more); events: E2, E6, E8, E9 |
| release (ER-Q4-FY2012 / ER-Q4-FY2013) | P285 ER-Q4-FY2012 to P295 ER-Q4-FY2013 | 367 | 301 | 236 | 52 changed = number or date roll-forward; 23 near-identical wording (ratio 0.9 or more); events: E9, E10, E13, E14 total RPD, E18 recast |
| release (OTHER-2011-02-25 / OTHER-2012-02-27) | P270 OTHER-2011-02-25 to P278 OTHER-2012-02-27 | 141 | 356 | 283 | 56 changed = number or date roll-forward; 10 = note renumbering or cross-reference; 11 near-identical wording (ratio 0.9 or more); events: E2, E6, E8, E9 |
| release (OTHER-2012-02-27 / OTHER-2013-02-28) | P278 OTHER-2012-02-27 to P286 OTHER-2013-02-28 | 101 | 75 | 295 | 176 changed = number or date roll-forward; 2 = note renumbering or cross-reference; 11 near-identical wording (ratio 0.9 or more); events: E9, E10, E13, E14 total RPD, E18 recast |
| release (OTHER-2013-02-28 / OTHER-2014-03-20) | P286 OTHER-2013-02-28 to P296 OTHER-2014-03-20 | 318 | 297 | 166 | 42 changed = number or date roll-forward; 18 near-identical wording (ratio 0.9 or more); events: E9, E10, E13, E14 total RPD, E18 recast |
| release (OTHER-2011-05-02 / OTHER-2012-05-07) | P272 OTHER-2011-05-02 to P280 OTHER-2012-05-07 | 77 | 113 | 194 | 95 changed = number or date roll-forward; 11 near-identical wording (ratio 0.9 or more); events: E2, E6, E8, E9 |
| release (OTHER-2012-05-07 / OTHER-2013-05-03) | P280 OTHER-2012-05-07 to P288 OTHER-2013-05-03 | 119 | 181 | 192 | 96 changed = number or date roll-forward; 1 = note renumbering or cross-reference; 14 near-identical wording (ratio 0.9 or more); events: E9, E10, E13, E14 total RPD, E18 recast |
| release (OTHER-2011-08-08 / OTHER-2012-08-01) | P274 OTHER-2011-08-08 to P282 OTHER-2012-08-01 | 94 | 73 | 287 | 190 changed = number or date roll-forward; 17 near-identical wording (ratio 0.9 or more); events: E2, E6, E8, E9 |
| release (OTHER-2012-08-01 / OTHER-2013-08-01-b) | P282 OTHER-2012-08-01 to P292 OTHER-2013-08-01-b | 129 | 176 | 242 | 136 changed = number or date roll-forward; 15 = note renumbering or cross-reference; 14 near-identical wording (ratio 0.9 or more); events: E9, E10, E13, E14 total RPD, E18 recast |
| release (OTHER-2011-11-07 / OTHER-2012-11-06) | P276 OTHER-2011-11-07 to P284 OTHER-2012-11-06 | 104 | 76 | 289 | 201 changed = number or date roll-forward; 16 near-identical wording (ratio 0.9 or more); events: E2, E6, E8, E9 |
| release (OTHER-2012-11-06 / OTHER-2013-11-06) | P284 OTHER-2012-11-06 to P294 OTHER-2013-11-06 | 271 | 257 | 192 | 86 changed = number or date roll-forward; 1 = note renumbering or cross-reference; 17 near-identical wording (ratio 0.9 or more); events: E9, E10, E13, E14 total RPD, E18 recast |
| proxy compensation (PROXY-2012 / PROXY-2013) | P297 PROXY-2012 to P298 PROXY-2013 | 274 | 442 | 326 | 82 changed = number or date roll-forward; 1 = note renumbering or cross-reference; 67 near-identical wording (ratio 0.9 or more) |
| notes-04-business-combinations-and-divestitures | P41 AR-FY2012 (unpaired) | n/a | n/a | n/a | new in AR-FY2012, no counterpart in AR-FY2011 |
| notes-12-accumulated-other-comprehensive-income-loss | P78 AR-FY2013 (unpaired) | n/a | n/a | n/a | new in AR-FY2013, no counterpart in AR-FY2012 |
| risk-factors | P108 Q1-FY2011 (unpaired) | n/a | n/a | n/a | in Q1-FY2011, no counterpart in Q1-FY2012 |
| notes-11-total-equity | P159 Q1-FY2012 (unpaired) | n/a | n/a | n/a | in Q1-FY2012, no counterpart in Q1-FY2013 |
| notes-05-business-combinations-and-divestitures | P211 Q1-FY2013 (unpaired) | n/a | n/a | n/a | new in Q1-FY2013, no counterpart in Q1-FY2012 |
| notes-12-other-comprehensive-income-loss | P218 Q1-FY2013 (unpaired) | n/a | n/a | n/a | new in Q1-FY2013, no counterpart in Q1-FY2012 |
| risk-factors | P226 Q1-FY2013 (unpaired) | n/a | n/a | n/a | new in Q1-FY2013, no counterpart in Q1-FY2012 |
| risk-factors | P128 Q2-FY2011 (unpaired) | n/a | n/a | n/a | in Q2-FY2011, no counterpart in Q2-FY2012 |
| notes-11-total-equity | P178 Q2-FY2012 (unpaired) | n/a | n/a | n/a | in Q2-FY2012, no counterpart in Q2-FY2013 |
| notes-05-business-combinations-and-divestitures | P232 Q2-FY2013 (unpaired) | n/a | n/a | n/a | new in Q2-FY2013, no counterpart in Q2-FY2012 |
| notes-12-accumulated-other-comprehensive-loss | P239 Q2-FY2013 (unpaired) | n/a | n/a | n/a | new in Q2-FY2013, no counterpart in Q2-FY2012 |
| notes-17-subsequent-events | P203 Q3-FY2012 (unpaired) | n/a | n/a | n/a | new in Q3-FY2012, no counterpart in Q3-FY2011 |
| notes-11-total-equity | P197 Q3-FY2012 (unpaired) | n/a | n/a | n/a | in Q3-FY2012, no counterpart in Q3-FY2013 |
| notes-05-business-combinations-and-divestitures | P252 Q3-FY2013 (unpaired) | n/a | n/a | n/a | new in Q3-FY2013, no counterpart in Q3-FY2012 |
| notes-12-accumulated-other-comprehensive-loss | P259 Q3-FY2013 (unpaired) | n/a | n/a | n/a | new in Q3-FY2013, no counterpart in Q3-FY2012 |
| release (one-off) | P268 OTHER-2011-01-25 (unpaired) | n/a | n/a | n/a | one-off release, no same-period counterpart |
| release (one-off) | P290 OTHER-2013-07-30 (unpaired) | n/a | n/a | n/a | one-off release, no same-period counterpart |
| release (one-off) | P291 OTHER-2013-08-01-a (unpaired) | n/a | n/a | n/a | one-off release, no same-period counterpart |
| events.txt | P299 events (unpaired) | n/a | n/a | n/a | event log, not a filing section |
| statements.xlsx | P1 statements (unpaired) | n/a | n/a | n/a | workbook, used in Part B |

## 4. Substantive changes

Read in the step 2 order. Every entry is quoted as filed. Mechanical changes are listed briefly with their cause and do not become rows.

### 4.1 Risk factors (D2)

Mechanical, no row: the FY2011 merger-risk block ("If we consummate a merger with Dollar Thrifty, ...") became the FY2012 "Risks Related to Acquisition of Dollar Thrifty" block after the acquisition [P3 p.33; P31 p.30; E9]; the Sponsor-control risk was removed in FY2013 after the Stockholders' Agreement ended [P31 p.26; E20]; convertible-note share-price risks were removed after conversion [P31 p.29; E13]; debt outstanding and Sponsor ownership roll forward [P3 p.33; P31 p.27; P60 p.27]. Interim: the Q3 2012 10-Q added Dollar Thrifty merger risks (E9) and the Q3 2013 10-Q replaced them with the FSNA risk (E10) [P205; P267 p.76].

| # | Change | Before | After | Row |
|---|---|---|---|---|
| 1 | Fleet-cost risk heading reworded; expectation of further decline in program cars dropped | "Declines in the value of the non-program cars in our fleet and declines in the overall number of program cars in our fleet could materially adversely impact our financial condition, results of operations, liquidity and cash flows." and "We expect this percentage to continue to decrease in the future, particularly as we integrate the operations of Dollar Thrifty, ..." [P31 p.22] | "Increased fleet costs, either generally or due to declines in the value of the non-program cars in our fleet, could materially adversely impact our financial condition, results of operations, liquidity and cash flows." [P60 p.23]; expectation sentence absent [not found: P60] | F4-D2-01 |
| 2 | Car supply statement removed | "We are not a party to any long-term car supply arrangements with manufacturers." [P31 p.22] | absent [not found: P60, P59 "car supply", "supply arrangement"] | F4-D2-02 |
| 3 | Multiemployer pension: hardened in FY2012, softened in FY2013 | FY2011: "At least one multiemployer plan in which we participate is reported to have, and other of our multiemployer plans could have, significant underfunded liabilities." [P3 p.31]; FY2012: "Several of our remaining multiemployer plans have underfunded liabilities." [P31 p.25] | FY2013: "Our multiemployer plans could have significant underfunded liabilities." [P60 p.26] | F4-D2-03 |
| 4 | New risk: key employees and headquarters relocation | none | "In addition, our key employees may be distracted by activities unrelated to our business, including the relocation of our corporate headquarters from Park Ridge, New Jersey to Estero, Florida." [P60 p.26] | F4-D2-04 |
| 5 | FSNA risk: "likely" in Q3 2013 became "may" in FY2013 | "... and are likely to incur additional losses." [P267 p.76] | "... and may incur additional losses." [P60 p.24] | F4-D2-05 |
| 6 | Like-kind exchange: fleet net book value added as a trigger | "A material and extended reduction in vehicle purchases or a downsizing of our car rental fleet, for any reason, ..." [P3 p.27] | "A material reduction in the net book value of our car rental fleet, a material and extended reduction in vehicle purchases and/or a material downsizing of our car rental fleet, for any reason, ..." [P31 p.22] | F4-D2-06 |

### 4.2 Legal proceedings and the contingencies note (C10)

Mechanical, no row: from FY2013, Item 3 cross-refers to note 13 instead of repeating it, which accounts for most of the 117 removed sentences in that pair [P61 p.32; calc, s1]; the public liability and property damage accrual rolls forward (281.5, 332.2, 347.7) [P4 p.38; P32 p.31; P61 p.136]. No matter moved between "remote", "reasonably possible" and "probable": "remote" and "reasonably possible" do not appear, and "probable" appears only in general sentences such as "We have established reserves for matters where we believe that the losses are probable and reasonably estimated, including for various of the matters set forth above." [P61 p.138; not found for a named matter: P4, P32, P61, P20, P49, P79 and the 10-Q contingencies notes].

| # | Change | Before | After | Row |
|---|---|---|---|---|
| 7 | Sobel: amount stated, reversal expectation dropped, no accrual stated | "The court has since entered a stay order and the parties will again be engaging in mediation." [P32 p.32]; Q1 2013: "... findings will be reversed." [P222 p.29] | "A judgment - which could potentially exceed $40.0 million - has still not been issued by the court." and "We continue to believe the outcome of this case will not be material to our financial condition, results of operations or cash flows." [P61 p.137] | F4-C10-01 |
| 8 | New securities class action | none | "On November 20, 2013, a purported shareholder class action, Pedro Ramirez, Jr. v. Hertz Global Holdings, Inc., et al., was commenced ..." [P61 p.138] | F4-C10-02 |
| 9 | Accruals appear for three class actions | "All proceedings in the case are currently stayed while the parties engage in settlement discussions." [P4 p.40] | "... have accrued our best estimate of the ultimate cost which is not material to our financial condition." [P32 p.32] | F4-C10-03 |
| 10 | SEC investigation closed | "We intend to cooperate fully with the SEC's investigation." [P4 p.38] | "On February 14, 2013, we were informed by the staff that the investigation has been completed and that no action was taken by the staff or the SEC." [P32 p.32] | F4-C10-04 |

### 4.3 Market risk

No substantive change. The pairs differ in note numbers, dates and figures: the one-point interest-rate sensitivity moved from 24.0 (FY2011) to 31.3 (FY2012) to 33.1 (FY2013), a change of 1.8 in the last year [P7 p.81; P35 p.68; P64 p.72; calc]; "gasoline prices" became "fuel prices" (wording) [P7 p.80; P35 p.67].

### 4.4 Auditor's report (C14)

Same firm, unqualified opinions each year; the Donlen and Dollar Thrifty scope exclusions come and go with the acquisitions (E2, E9) [P8 p.85; P36 p.71; P65 p.74]. FY2013 names "Internal Control—Integrated Framework 1992" and has no paragraph on the E24 revision [P65 p.74; not found: P65 "revis", "error"]. Row F4-C14-01 (P4). Critical audit matters do not apply to these periods [P0, header table].

### 4.5 Critical accounting estimates (C13)

Mechanical: "Acquisition Accounting" added in FY2012 (E9) [P34 p.44]. For every estimate in every year (revenue earning equipment, public liability, pensions, goodwill, intangibles, derivatives, income taxes, stock compensation) no change amount and no sensitivity is given [not found: P6, P34, P63 searched "sensitiv", "basis point", "1%", "increase of"]. The US requirement to give them dates from 2021, so their absence in 2011 to 2013 is recorded, not treated as a rule-required gap [inf: F4 method step 4]. A residual-value sensitivity does exist in the pack, in the Q4 2013 call slides: "1% change to residuals = $83M adjusted pre-tax income" [P296 p.21].

| # | Change | Before | After | Row |
|---|---|---|---|---|
| 11 | Depreciation estimate text | "These key factors are considered when estimating future residual values and assessing depreciation rates." and "... we use historical experience and monitor market conditions to set depreciation rates." [P34 p.44] | "These key factors are considered when estimating future residual values. Depreciation rates are adjusted prospectively through the remaining expected life." and "... we use historical experience, as well as industry residual value guidebooks, and the monitoring of market conditions, to set depreciation rates." [P63 p.45] | F4-C13-01 |
| 12 | Stock-option volatility method | "Therefore, we use the calculated value method to estimate the expected volatility, ..." [P6 p.56] | "Beginning in 2012, we have determined that there is now sufficient historical information available to estimate the expected volatility of our stock price." [P34 p.47] | F4-C13-02 |
| 13 | Public liability reserve basis | "Reserve requirements are based on actuarial evaluations ..." [P6 p.53] | "Reserve requirements are based on rental volume and actuarial evaluations ..." [P34 p.45] | F4-C6-03 |

### 4.6 Revenue note (A8, C11, C12)

The principal-or-agent sentence is identical in all three years: "Rental and rental related revenue (including cost reimbursements from customers where we consider ourselves to be the principal versus an agent) are recognized over the period the revenue earning equipment is rented or leased based on the terms of the rental or leasing contract." [P11 p.93; P39 p.80; P68 p.90; calc, identical hash]. No wording on bill-and-hold, variable consideration or payments to customers was found in any year [not found: P11, P39, P68 searched "bill", "variable consideration", "incentives paid"]; "licensees" became "franchisees" (wording) [P39 p.80; P68 p.90].

| # | Change | Before | After | Row |
|---|---|---|---|---|
| 14 | Gains on sales of operations to franchisees kept in operating income | none [not found: P11] | "Such gains or losses are included in operating income because they are expected to be a recurring part of our business." [P39 p.84] | F4-A8-01 |
| 15 | Revenue lines reclassified and relabelled | context sheet E17, E18 [P227 p.3; P247 p.3] | FY2012 car rental revenue reprinted 7,456.1 to 7,161.7 [context sheet E18] | F4-A8-02 |

### 4.7 Receivables, inventory, payables, supplier finance (A4)

Allowance method text unchanged; inventories stay "at lower of cost or market"; no supplier-finance or factoring programme appears in any year (securitizations are fleet-backed borrowings recorded as debt) [P11 p.93; P68 p.90; P13 p.110; search s3 "5_factoring"].

| # | Change | Before | After | Row |
|---|---|---|---|---|
| 16 | Receivable concentration statement dropped | "Concentrations of credit risk with respect to trade receivables are limited due to the large number of customers ..." and "As of December 31, 2011, we had no significant concentration of credit risk." [P22 p.139] | Concentration paragraph covers cash and derivatives only [P39 p.80; P68 p.90] | F4-A4-01 |
| 17 | 2012 allowance revised | "Year ended December 31, 2012 \| $20,282 \| $34,144 \| ..." [P56 p.140] | "Year ended December 31, 2012(b) \| 20.3 \| 38.3 \| ..." [P86 p.158] | F4-A4-02 |

### 4.8 PP&E, intangibles, capitalized costs (C5, C7)

| # | Change | Before | After | Row |
|---|---|---|---|---|
| 18 | Car holding period range widened; table relabelled from "Useful lives" to "Holding periods" | "Cars \| 4 to 26 months" [P11 p.94]; "Cars \| 4 to 28 months" [P39 p.81] | "Cars \| 4 to 36 months" [P68 p.91] | F4-D3-01 |
| 19 | Other useful lives changed | "Buildings \| 3 to 50 years", "Capitalized internal use software \| 1 to 15 years", "Other intangible assets \| 3 to 20 years" [P39 p.81] | "Buildings \| 5 to 50 years", "Capitalized internal use software \| 1 to 10 years", "Other intangible assets \| 3 to 10 years" [P68 p.91] | F4-C7-01; F4-D3-02 |
| 20 | Depreciation note: explanation of rate changes | "The cumulative effect of the reduction in rates was indicative of the strong residual values experienced in the U.S. ..." [P45 p.113] | "The favorable adjustments reflect changes from the impact of car sales channel diversification, acceleration of our retail sales expansion and the optimization of fleet holding periods related to the integration of Dollar Thrifty. The cumulative effect of the reduction in rates was also indicative of the residual values experienced in the U.S. ..." [P74 p.126] | F4-D3-06 |

### 4.9 Provisions, reserves, restructuring (C6, C9)

| # | Change | Before | After | Row |
|---|---|---|---|---|
| 21 | 2012 restructuring rollforward re-described | "Other(2) \| (0.3) \| (1.0) \| (0.6) \| (9.9) \| (11.8)" with "Primarily consists of decreases of $10.3 million for facility closures ..." [P50 p.126] | "Cash payments \| (22.6) \| — \| (1.6) \| (12.6) \| (36.8)" with "Primarily consists of decreases of $0.5 million related to a goodwill write-off on a sale of business ..." [P80 p.141] | F4-C6-01 |
| 22 | FSNA exposure range not carried into FY2013 | "We currently estimate our total exposure to FSNA's liquidity issues to be between $50 and $70 million." [P265 p.37] | "Impairment charges and other(10) \| (44.0)" [P77 p.134]; range absent [not found: P70, P85, P62] | F4-C6-02 |

### 4.10 Related parties, guarantees, unconsolidated entities (D4)

Mechanical: Sponsor agreements and Sponsor-related debt disclosures end after the May 2013 sale (E20) [P82 p.148]; the China Auto equity-method investment is on the context sheet (E15); the Simply Wheelz credit agreement of up to $45.0m was terminated with no amounts outstanding (E10) [P70 p.101]; indemnification text unchanged [P61 p.139].

| # | Change | Before | After | Row |
|---|---|---|---|---|
| 23 | Company purchases of executives' homes | none | "The total amount that we spent under the program during the year ended December 31, 2013 was $3.1 million for the executive officers." [P82 p.147] | F4-D4-01 |

### 4.11 Non-GAAP definitions in the releases and filings (C2)

| # | Change | Before | After | Row |
|---|---|---|---|---|
| 24 | Labels and categories | "Non-cash debt charges(3) \| (83.6)" and "Other(9) \| (44.0)" [P48 p.120] | "Debt-related charges(3) \| (68.4) \| (83.6)" [P77 p.134]; FY2012 44.0 shown as "Other unusual/non-recurring" [P295 p.9] | F4-C2-01 |
| 25 | Metric definitions | context sheet E8, E14 | context sheet E8, E14 | F4-C2-02 |

### 4.12 MD&A (read last; D5)

The MD&A pairs are the largest (for example FY2012 to FY2013: 357 added, 205 removed, 275 changed) [calc, s1]. They were read through targeted searches for the ten sentence types and the fleet depreciation passages, not sentence by sentence [inf: this output, Could not run]. One substantive change found this way: FY2012 gave "due to improved residual values in the U.S." as the first reason for lower monthly per-vehicle depreciation [P33 p.42]; FY2013 gives "due to mix optimization, improved procurement and remarketing efforts, optimization of fleet holding periods related to the integration of Dollar Thrifty and channel diversification" with no residual-value reason [P62 p.42]. It is carried in F4-D3-06.

### 4.13 Same-quarter interim notes (step 5)

The notes of Q1, Q2 and Q3 were compared 2011 to 2012 and 2012 to 2013 [calc, s1]. Substantive changes: the Q1 2012 depreciation note said "We believe the positive trending of residual values is primarily due to continued short supply of used vehicle inventory and improving consumer confidence." [P154 p.12] and the Q1 2013 note has no residual-trend sentence while reporting disposal losses [P213 p.13] (carried in F4-D3-03); the Q2 and Q3 2013 notes add "Prospective changes include the impact of car sales channel diversification and acceleration of our retail sales expansion." [P234 p.14; P254 p.14]; Sobel's $40.0m figure first appears in Q1 2013 [P222 p.29]; the relocation home purchases first appear in Q3 2013 [P262 p.34]; the Q3 2012 note records an interim impairment test of Advantage (check 1) [P190 p.12]. Other interim changes are mechanical: acquisitions (E2, E6, E9), the Q3 2011 revision (E4), standards (E7, E11), revolver gross-up (E17), segment recast (E18), Sponsor exit (E20) [context sheet].

### 4.14 Revisions search (C16)

Search terms: revision, revised, immaterial error, previously reported, as adjusted, prior period error, correction of an error, restated, out of period, in every notes, basis-of-presentation and schedule file [s3_search.py]. Hits by filing are in F4-C16-02; every hit maps to E1, E4, E12, E17 or E24. Two changes to previously reported figures have no stated cause (F4-C16-01, F4-C6-01).

## 5. Consistency checks

| # | Sentence type | Sentence as filed (per year, with locator) | Number it was checked against [calc] | Result | Reason |
|---|---|---|---|---|---|
| 1 | No impairment indicators | FY2011: "... concluded that there was no impairment related to our goodwill and our other intangible assets." [P11 p.97]; FY2012 and FY2013: "... determined that the respective book values of our reporting units did not exceed their estimated fair values and therefore no impairment existed ..." [P40 p.85; P69 p.94]; Q3 2012: the Advantage agreement "triggered an interim impairment analysis." [P190 p.12] | Segment adjusted pre-tax income change FY2012, FY2013: U.S. car +29.65%, +25.01%; international car -36.20%, +51.99%; equipment +40.24%, +29.13%; all other +217.33%, +20.38% [calc, P77 p.131 recast]. Goodwill net 31 Dec 2013: U.S. 1,010.8; international 203.4; equipment 97.5; all other 35.8 [P69 p.95] | Consistent | No goodwill-bearing segment declined in consecutive years. The March 2014 plan to separate equipment rental [P85 p.150] post-dates the 1 October 2013 test and is a separation, not a sale. For Advantage the company named the trigger and tested recoverability, so the sentence type "no indicators" was not used. |
| 2 | Useful lives, holding periods | Cars: "4 to 26 months" [P11 p.94], "4 to 28 months" [P39 p.81], "4 to 36 months" [P68 p.91]; "Depreciation rates are adjusted prospectively through the remaining expected life." [P63 p.45]. Intangibles: "Other intangible assets \| 3 to 10 years" and "... range from two to fifteen years." in the same note [P68 p.91, p.93] (FY2012: 3 to 20 against two to fifteen [P39 p.81, p.83]) | Provision / average gross fleet: 16.22%, 15.28%, 14.25% (FY2011 to FY2013); revised-basis sensitivity 16.14%, 15.17%, 14.27%; FY2013 same-quarter change Q1 -2.17, Q2 -1.33, Q3 -1.07, Q4 -1.33 percentage points (Q4 with 9M correction added back 13.17% against 14.01%) [calc] | Inconsistent | The disclosed range widened while depreciation per unit of gross fleet fell in every 2013 quarter, and the effect of the longer holding periods is not given separately; two different life ranges are stated for finite-lived intangibles in one note (F4-D3-01, F4-D3-02). |
| 3 | Explanations of a movement | Q1 2013: "driven primarily by an increase in residual values and corresponding lower depreciation rates" [P225 p.42]; Q2 2013: "due to improved residual values in the U.S." [P246 p.38]; Q3 2013: "due to residual values that remained strong in the U.S." [P266 p.41]; FY2013: "a deterioration in the used vehicle residual values" [P62 p.54] beside "indicative of the residual values experienced in the U.S." [P62 p.42; P74 p.126] | Car disposal result per non-program car sold, 2013 against 2012: Q1 -44 against +812 USD; Q2 -250 against +857; Q3 U.S. -275 against +578; FY U.S. -244 against +738; U.S. disposal swing -148.8m; depreciation-rate changes lowered 2013 U.S. depreciation by 44.2m (Q4 derived 8.9m) [calc] | Inconsistent | Each explanation points to strong or improving residual values, or to rate cuts reflecting residual values, while the disclosed disposal results in the same filings moved from gains to losses; the FY2013 MD&A states both directions (F4-D3-03 to F4-D3-06). |
| 4 | Change orders, unapproved variations | Not found [search s3 "4_change_orders": only an FTC consent "currently under discussion" (P190 p.11) and a UK pension scheme name (P297, P298)] | none | Cannot test | No sentence of this type; the business has no construction-type contracts in the pack [inf: P2, P30, P59]. |
| 5 | Scope of receivable sales or factoring | Not found [s3 "5_factoring": 330 hits, all fleet securitizations recorded as debt, none on receivable sales] | none | Cannot test | No receivable sale or factoring programme is described; missing number: amounts derecognized, which do not exist in the pack. |
| 6 | Bill-and-hold or early-shipment share | Not found [s3 "6_billhold": 0 hits] | none | Cannot test | No sentence of this type. |
| 7 | Items labelled non-recurring or one-time | "Corporate EBITDA excludes the impact of extraordinary, unusual or non-recurring gains or losses or charges or credits." [P295 p.3, same footnote in all 13 releases]; adjusted pre-tax income adds back "certain one-time charges and non-operational items" [P77 p.131] | Non-recurring table non-zero in 13 of 13 quarterly releases; restructuring in it in 8 of the last 8 quarters; restructuring charges in 5 of 5 fiscal years FY2009 to FY2013; premiums paid on debt added back in 2 of 3 years [calc] | Inconsistent | The category appears in far more than two prior fiscal years and five of the last eight quarters while still labelled non-recurring or one-time (F4-D3-07). |
| 8 | Reserve release described as a change in estimate | No such sentence found [s3 "8_release": only tax and a 0.1m restructuring reversal (P146 p.51)]. Related sentence: "Our actual results as compared to our estimates have historically resulted in relatively minor adjustments to our recorded liability." [P63 p.45] | none | Cannot test | Missing number: a public liability and property damage rollforward with prior-year development (not in P86 or any note searched). |
| 9 | Customer concentration | FY2011: "As of December 31, 2011, we had no significant concentration of credit risk." [P22 p.139]; not repeated from FY2012 [P39 p.80; P68 p.90] | none | Cannot test | Missing numbers: revenue and receivables by customer, including Simply Wheelz sublease revenue and amounts owed (not disclosed) [not found: P68, P70, P265]. Dropped sentence carried as F4-A4-01. |
| 10 | Liquidity sufficiency | "We believe that cash generated from operations and cash received on the disposal of vehicles and equipment, together with amounts available under various liquidity facilities will be adequate to permit us to meet our debt maturities over the next twelve months." unchanged [P5 p.74; P33 p.63; P62 p.67] | FY2013 MD&A liquidity section discloses the HVF II Series 2013-B amortization event and waivers [P62 p.67]; no supplier-finance or factoring programme in the pack [s3] | Consistent | The unchanged sentence sits beside disclosure of the one financing event of the period (E23). |

## 6. Ledger rows

| ID | Item | Period | Evidence | Locator | Benign reading | Adverse reading | Context | Resolving disclosure | Priority | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| F4-D3-01 | D3 check 2: car holding periods against depreciation per unit of gross fleet | FY2011 to FY2013; Q1 FY2013 to Q4 FY2013 | Holding periods: "Cars \| 4 to 26 months" (FY2011), "Cars \| 4 to 28 months" (FY2012), "Cars \| 4 to 36 months" (FY2013). Provision for depreciation of revenue earning equipment / average gross fleet: 16.22% FY2011, 15.28% FY2012, 14.25% FY2013 [calc]; same-quarter change FY2013 against FY2012: Q1 -2.17, Q2 -1.33, Q3 -1.07, Q4 -1.33 percentage points [calc]. FY2013 critical estimates add "Depreciation rates are adjusted prospectively through the remaining expected life." The effect of the longer holding periods is not given separately. Row triggers (a) latest value lowest in series and (b) six consecutive same-quarter declines Q3 FY2012 to Q4 FY2013 [calc]. | P11 p.94; P39 p.81; P68 p.91; P63 p.45; P74 p.126; P1 BS_A and BS_Q (Equipment held for rental or lease, gross) | Fleet mix moved toward non-program cars, which the company says have lower depreciation rates (P225 p.35), and Dollar Thrifty cars entered at fair value (E9); longer holding periods for risk cars lower monthly depreciation by design; the aggregate effect of 2013 rate changes is disclosed (U.S. -44.2m, international +5.0m) [P74 p.126]. | Holding periods were lengthened and rates lowered in the year car disposals moved from gains to losses (F4-D3-06), which lowers current depreciation and can push cost into later disposal losses; the part due to holding periods is not quantified [inf: P68, P74, P62]. | E22 depreciation-rate changes; E24 revision (FY2013 and derived Q4 FY2013 on revised basis; on the revised basis the annual series is 16.14%, 15.17%, 14.27% and Q4 FY2013 with the 9M correction added back is 13.17% [calc]); E9 | Split of the 2013 rate effect between holding periods and residual assumptions; average holding period by year; car-only gross cost and depreciation. Not found [P74, P63, P62, P77 searched 'holding period', 'average age', 'months']. | P1 |  |
| F4-D3-02 | D3 check 2: finite-lived intangible lives stated two ways in the same note | FY2012, FY2013 | FY2012 note 2: "Other intangible assets \| 3 to 20 years" and "...which range from two to fifteen years." FY2013 note 2: "Other intangible assets \| 3 to 10 years" and "...which range from two to fifteen years." | P39 p.81 and p.83; P68 p.91 and p.93 | The useful-life table line may cover a narrower class than all finite-lived intangibles, or one of the two statements was not updated when the other was [inf: P39, P68]. | Two stated lives for the same asset class disagree; if amortization follows the longer range, expense is lower than the shorter range implies [inf: P39, P68]. | E9 and E21 (Dollar Thrifty intangibles 1,545) | Lives by intangible class. Not found [P69 searched 'years', 'life', 'useful']. | P1 |  |
| F4-D3-03 | D3 check 3: explanation of lower depreciation, Q1 2013 | Q1 FY2013 | MD&A: "The decrease as a percent of revenues was driven primarily by an increase in residual values and corresponding lower depreciation rates in the first quarter of 2013 compared to the first quarter of 2012." and "In addition, residuals remained fairly strong during the period." Same filing, note 7: vehicle disposals "included net losses of $3.3 million and net gains of $34.9 million" (Q1 2013, Q1 2012); per non-program car sold -44 against +812 USD [calc]; rate changes in the quarter were a decrease of $0.7m. | P225 p.42 and p.35; P213 p.13 | Residual values in the sentence may mean expected values at future disposal or an index level, not realized proceeds; sales volume rose to 75,400 from 43,000 cars and included Dollar Thrifty cars recorded at fair value [P225 p.35; E9]. | The explanation credits higher residual values for lower depreciation while the same filing shows realized disposal results moving from gains to losses [inf: P225, P213]. | E9; E22; E24 (Q1 2013 revised: depreciation and lease charges 587.0 to 580.1 [P68 p.85]) | Realized proceeds per car and the residual index used. Not found [P225, P213, P287, P288]. | P1 |  |
| F4-D3-04 | D3 check 3: explanation of lower depreciation, Q2 2013 | Q2 FY2013 | MD&A: "In the six months ended June 30, 2013, our monthly per vehicle depreciation costs decreased as compared to the prior year period due to improved residual values in the U.S., ..." and "In addition, residuals have remained relatively strong during the period." Note 7: rate changes "resulted in net decreases of $14.8 million" in the quarter; disposals "included net losses of $17.5 million and net gains of $38.3 million"; per car -250 against +857 USD [calc]. Call slides: "Auction/dealer residuals softer than expected". | P246 p.38 and p.46; P234 p.13 and p.14; P292 p.11 | The statement compares six months with six months; the slides say retail residuals stayed strong while auction residuals softened, so rates may rest on a retail-heavy disposal plan [P292 p.11]. | Depreciation rates were lowered on higher expected residuals in a quarter when realized sales produced losses and management's own slides describe softer auction residuals [inf: P234, P246, P292]. | E22; E24 (Q2 2013 revised: 641.1 to 627.5 [P68 p.85]); E14 | Residual assumptions by channel behind the Q2 rate change. Not found [P234, P246, P289, P292]. | P1 |  |
| F4-D3-05 | D3 check 3: explanation of lower depreciation, Q3 2013 | Q3 FY2013 | MD&A: "In the nine months ended September 30, 2013, our monthly per vehicle depreciation costs decreased as compared to the prior year period due to residual values that remained strong in the U.S., ..." Note 7: U.S. rate changes "resulted in net decreases of $18.0 million and $35.3 million" (three and nine months); U.S. disposals "included net losses of $11.1 million and net gains of $15.2 million"; per U.S. car -275 against +578 USD [calc]. | P266 p.41 and p.50; P254 p.14 | Rate reductions reflect channel diversification and retail expansion, which the note names as drivers [P254 p.14]. | The same filing attributes higher depreciation as a share of revenue to losses on vehicle sales (P266 p.50) while crediting strong residual values for lower per-vehicle depreciation [inf: P266, P254]. | E22; E24 (Q3 2013 revised: 676.7 to 674.9 [P68 p.87]) | As F4-D3-04. Not found [P254, P266, P293, P294]. | P1 |  |
| F4-D3-06 | D3 check 3: residual values described both ways, FY2013 | FY2013 | MD&A U.S. segment: "The increase was primarily attributable to an increase in average fleet due to the Recent Acquisitions and a deterioration in the used vehicle residual values." Same document and note 8: U.S. rate changes "resulted in net decreases of $44.2 million" and "The cumulative effect of the reduction in rates was also indicative of the residual values experienced in the U.S. ..." Note 8: disposal loss "primarily due to a combination of declining residual values from falling demand for used vehicles and timing of sales". U.S. per car -244 against +738 USD [calc]; U.S. disposal swing -148.8m [calc]. FY2012 note 8 said "indicative of the strong residual values" (word "strong" not in FY2013). International: rate changes increased depreciation by 5.0m while MD&A cites "slight strengthening of used vehicle residual values". | P62 p.54, p.42, p.43; P74 p.126; P45 p.113 | Rate reductions are prospective and were set in earlier quarters (9M -35.3m, derived Q4 -8.9m [calc]); the note also credits channel diversification, retail expansion and longer holding periods, which are not residual-value effects [P74 p.126]. | One document says residual values deteriorated (raising segment depreciation) and that rate reductions reflect residual values experienced; lower rates in a year of disposal losses can defer cost [inf: P62, P74]. | E22; E24; E9 | Residual assumption by quarter and reconciliation of rate changes to realized proceeds. Not found [P74, P62, P63, P295, P296]. | P1 |  |
| F4-D3-07 | D3 check 7: recurring charges under a non-recurring or one-time label | Q4 2010 to Q4 2013; FY2009 to FY2013 | Releases: "Corporate EBITDA excludes the impact of extraordinary, unusual or non-recurring gains or losses or charges or credits." The table of those items is non-zero in 13 of 13 quarterly releases and includes restructuring charges in 8 of the last 8 [calc]; restructuring charges recorded in 5 of 5 fiscal years FY2009 to FY2013 (106.8, 54.7, 56.4, 38.0, 77.0) [calc count]. 10-K: adjusted pre-tax income adds back "certain one-time charges and non-operational items", including restructuring every year. FY2012 "Other(9) \| (44.0)" is shown as "Other unusual/non-recurring" in the Q4 2013 release. | P295 p.3 and p.9; P77 p.131 and p.134; P48 p.120; P21 p.138; P50 p.125; P80 p.140 | The Corporate EBITDA label follows the credit agreement definition; restructuring is disclosed as an ongoing programme, so a reader can see it recurs [P295 p.3; P80 p.140]. | Charges that recur every year are presented under a non-recurring or one-time label, which can make recurring costs look exceptional [inf: P295, P77, P80]. | E9, E10 (acquisition and divestiture costs in 2012 and 2013) | Whether any filed measure (10-K, 10-Q) carries the non-recurring label: searched P5, P33, P62 and the nine 10-Q mdna files; only 'one-time' found. Whether Item 10(e)(1)(ii)(B) reaches the furnished releases is for the analyst. | P1 |  |
| F4-D2-01 | D2 fleet-cost risk factor reworded; expectation dropped | FY2013 | Before: "Declines in the value of the non-program cars in our fleet and declines in the overall number of program cars in our fleet could materially adversely impact our financial condition, results of operations, liquidity and cash flows." After: "Increased fleet costs, either generally or due to declines in the value of the non-program cars in our fleet, could materially adversely impact our financial condition, results of operations, liquidity and cash flows." Dropped: "We expect this percentage to continue to decrease in the future, particularly as we integrate the operations of Dollar Thrifty, ..." | P31 p.22; P60 p.23 | Program-car share was 30% of purchases in both 2012 and 2013 [P60 p.23], so the expectation of further decline no longer applied; the heading was broadened. | The heading now leads with increased fleet costs in the year disposal results turned to losses (F4-D3-03 to F4-D3-06) [inf: P60, P74]. | E9 | Residual assumptions and program share by quarter. Not found [P60, P62]. | P2 |  |
| F4-D2-02 | D2 statement on car supply arrangements removed | FY2013 | FY2012: "We are not a party to any long-term car supply arrangements with manufacturers." Not in FY2013 [not found: P60, P59 searched "car supply", "supply arrangement"]. | P31 p.22; P60 p.23 | Editorial shortening of an unchanged risk [inf: P31, P60]. | A long-term supply arrangement may now exist whose terms are not described [inf: P31, P60]. | none | Supply terms in Item 1. Not found [P59]. | P3 |  |
| F4-D2-03 | D2 multiemployer pension risk hardened, then softened | FY2012, FY2013 | FY2011: "At least one multiemployer plan in which we participate is reported to have, and other of our multiemployer plans could have, significant underfunded liabilities." FY2012: "Several of our remaining multiemployer plans have underfunded liabilities." FY2013: "Our multiemployer plans could have significant underfunded liabilities." | P3 p.31; P31 p.25; P60 p.26 | After the December 2012 withdrawal (cost 23.2m, P295 p.2 note (c)) the remaining plans may be better funded. | A statement of fact became a possibility without a disclosed change in funding [inf: P31, P60]. | none | Plan funding zones: zone table in note 6 (P72 p.121); zones not tabulated in this step. | P3 |  |
| F4-D2-04 | D2 new risk: key employees and headquarters relocation | FY2013 | "In addition, our key employees may be distracted by activities unrelated to our business, including the relocation of our corporate headquarters from Park Ridge, New Jersey to Estero, Florida." | P60 p.26 | Relocation announced May 2013 [P228 p.8]; the risk describes a known event. | Finance and management disruption in the year of the E24 errors, the E19 system change and the E20 CFO change [inf: P60, P68, P87]. | E19, E20 | Status of finance staff relocation. Not found [P60, P62, P87]. | P3 |  |
| F4-D2-05 | D2 new risk: losses from FSNA and Simply Wheelz; likelihood softened between Q3 and FY2013 | Q3 FY2013, FY2013 | Q3 2013 10-Q: "We have recognized losses as a result of our relationship with FSNA and Simply Wheelz and are likely to incur additional losses." FY2013: "We have recognized losses as a result of our relationship with Franchise Services of North America, or "FSNA," and Simply Wheelz and may incur additional losses." | P267 p.76; P60 p.24 | The 16 December 2013 settlement fixed payments and the return of vehicles, which may have lowered the likelihood of further loss [P70 p.101]. | Likely became may with no amount given for the remaining exposure named in Q3 (see F4-C6-02) [inf: P267, P60, P265]. | E10 | Remaining FSNA exposure at 31 December 2013. Not found [P70, P77, P85]. | P3 |  |
| F4-D2-06 | D2 like-kind exchange risk adds fleet net book value as a trigger | FY2012 | Before: "A material and extended reduction in vehicle purchases or a downsizing of our car rental fleet, for any reason, ..." After: "A material reduction in the net book value of our car rental fleet, a material and extended reduction in vehicle purchases and/or a material downsizing of our car rental fleet, for any reason, ..." | P3 p.27; P31 p.22 | Clarifies the mechanism and adds Dollar Thrifty's own programme (E9). | Links fleet book value, and so depreciation choices, to the timing of material tax payments [inf: P31]. | E9 | Deferred tax attributable to the programme. Not reviewed in this step (P75). | P3 |  |
| F4-C10-01 | C10 Sobel concession-fee case: stated potential judgment, no accrual stated | FY2013 (first in Q1 FY2013) | FY2012: "The court has since entered a stay order and the parties will again be engaging in mediation." FY2013: "A judgment - which could potentially exceed $40.0 million - has still not been issued by the court." and "We continue to believe the outcome of this case will not be material to our financial condition, results of operations or cash flows." Q1 2013 said the findings "will be reversed"; that sentence is not in FY2013 [not found: P61, P79]. 40.0 is 6.03% of FY2013 pre-tax income [calc]. | P32 p.32; P61 p.137; P222 p.29 | An interlocutory appeal and mediation are pending; the general statement on unaccrued matters may cover this case [P61 p.137-138]. | Partial summary judgment on restitution and class certification went against the company and a potential judgment above $40.0m is stated, but no accrual, likelihood term or range is given for the matter [inf: P61]. | none | ASC 450-20 accrual or reasonably possible range for this matter. Not found [P61, P79, P243, P263 searched 'probable', 'reasonably possible', 'accru' near Sobel]. | P3 |  |
| F4-C10-02 | C10 new securities class action | FY2013 | "On November 20, 2013, a purported shareholder class action, Pedro Ramirez, Jr. v. Hertz Global Holdings, Inc., et al., was commenced ..." alleging misstatements "during the period from February 25, 2013 through November 4, 2013". | P61 p.138 | Newly filed; no estimate is usually possible at this stage. | The class period covers the quarters later revised under E24 [inf: P61, P68]. | E24 | Statement on estimate of loss. Not found [P61, P79]. | P3 |  |
| F4-C10-03 | C10 accruals appear for three class actions | FY2012 | FY2011: "All proceedings in the case are currently stayed while the parties engage in settlement discussions." FY2012: "... have accrued our best estimate of the ultimate cost which is not material to our financial condition." Q4 2013 release: 2012 adjustments include a "litigation accrual of $14.0 million". | P4 p.40; P32 p.32; P295 p.2 | Settlements reached in 2012 and 2013 [P61 p.136-138]. | Matters each called not material add up to an amount the company excludes from adjusted results [inf: P32, P295]. | none | Accrual by matter. Not found [P32, P49]. | P3 |  |
| F4-C10-04 | C10 SEC investigation closed | FY2012 | FY2011: "We intend to cooperate fully with the SEC's investigation." FY2012: "On February 14, 2013, we were informed by the staff that the investigation has been completed and that no action was taken by the staff or the SEC." | P4 p.38; P32 p.32 | Resolution with no action. | None beyond the fact of the prior investigation [inf: P32]. | none | In pack. | P3 |  |
| F4-C14-01 | C14 auditor report unchanged; no paragraph on the revision | FY2013 | Unqualified opinions; FY2013 names "Internal Control—Integrated Framework 1992"; the Dollar Thrifty scope exclusion ends; no explanatory paragraph on the E24 revision [not found: P65 "revis", "error"]. | P65 p.74; P36 p.71 | The company judged the errors immaterial to prior periods [P68 p.83], a case in which no explanatory paragraph is expected [inf]. | None beyond F1-C15-1. | E24 | In pack (P65). | P4 |  |
| F4-C13-01 | C13 depreciation estimate wording changed; no sensitivity in the 10-K | FY2013 | Before: "These key factors are considered when estimating future residual values and assessing depreciation rates." and "... we use historical experience and monitor market conditions to set depreciation rates." After: "These key factors are considered when estimating future residual values. Depreciation rates are adjusted prospectively through the remaining expected life." and "... we use historical experience, as well as industry residual value guidebooks, and the monitoring of market conditions, to set depreciation rates." No change amount or sensitivity in any year's critical estimates [not found: P6, P34, P63]; the Q4 2013 slides give one: "1% change to residuals = $83M adjusted pre-tax income". | P34 p.44; P63 p.45; P296 p.21 | Clarifies existing practice; guidebooks are a benchmark the slides also cite [P294 p.10]. | A new outside input to residual estimates appears in the year estimated residuals rose while realized residuals fell; the sensitivity exists but is not in the filing [inf: P63, P296, P74]. | E22 | Quantified effect of the guidebook input. Not found [P63, P74]. | P2 |  |
| F4-C13-02 | C13 stock-option volatility estimate method changed | FY2012 | FY2011: "Therefore, we use the calculated value method to estimate the expected volatility, ..." FY2012: "Beginning in 2012, we have determined that there is now sufficient historical information available to estimate the expected volatility of our stock price." | P6 p.56; P34 p.47 | Stated reason: enough trading history after 2006 listing. | Change in an estimate input with no stated effect on expense [inf: P34]. | none | Effect on 2012 option expense. Not found [P44]. | P3 |  |
| F4-A8-01 | A8 gains on sales of operations to franchisees kept in operating income | FY2012 (new policy text) | "Such gains or losses are included in operating income because they are expected to be a recurring part of our business." | P39 p.84 | Policy disclosure added alongside franchise revenue recognition. | Gains on disposals of operations sit in operating results; amounts not disclosed [not found: P39, P68 searched 'franchisee' with 'gain']. | E3, E16 (franchise reacquisitions) | Amount of such gains by year. Not found. | P3 |  |
| F4-A8-02 | A8 revenue lines reclassified and relabelled | Q2 FY2013 onward | Other revenue reclassified in Q2 2013 and relabelled with the Q3 2013 segment recast; FY2012 car rental 7,456.1 to 7,161.7 [context sheet E17, E18]. | P227 p.3; P247 p.3; P66 p.76 | Presentation change with total revenue unchanged apart from E24. | Line-level trends before and after Q2 2013 are not comparable [inf: P1, P227]. | E17, E18 | Reason for the Q2 2013 reclassification beyond the generic sentence. Not found [P229]. | P4 |  |
| F4-A4-01 | A4 receivable concentration statement dropped | FY2012, FY2013 | FY2011: "Concentrations of credit risk with respect to trade receivables are limited due to the large number of customers ..." and "As of December 31, 2011, we had no significant concentration of credit risk." From FY2012 the concentration paragraph covers cash and derivatives only [P68 p.90]. | P22 p.139; P39 p.80; P68 p.90 | Moved into the policy note and shortened. | Dropped in the period one counterparty, Simply Wheelz, subleased about 20,000 vehicles and later owed amounts in an estimated 50 to 70m exposure [inf: P60 p.24, P265 p.37]. | E10 | Receivables by counterparty. Not found. | P3 |  |
| F4-A4-02 | A4 2012 allowance for doubtful accounts revised | FY2012 as reprinted | FY2012 Schedule II: "Year ended December 31, 2012 \| $20,282 \| $34,144 \| ..." (thousands). FY2013: "Year ended December 31, 2012(b) \| 20.3 \| 38.3 \| ..." (millions); charged to expense +4.16m [calc]. | P56 p.140; P86 p.158 | Brazil allowance correction in E24. | None beyond E24. | E24 | In pack (P68 pp.83-89). | P4 |  |
| F4-C7-01 | C7 other useful-life ranges changed without comment | FY2013 | FY2012: "Buildings \| 3 to 50 years", "Capitalized internal use software \| 1 to 15 years". FY2013: "Buildings \| 5 to 50 years", "Capitalized internal use software \| 1 to 10 years". No statement that lives changed [not found: P68 "change in estimate", "useful li"]. | P39 p.81; P68 p.91 | Table updated to reflect assets held; the software change shortens lives. | An unexplained change in stated lives; effect not given [inf: P68]. | none | Effect of any change in lives. Not found. | P3 |  |
| F4-C6-01 | C6 2012 restructuring rollforward re-described | FY2012 as reprinted in FY2013 | FY2012 10-K, 2012: "Other(2) \| (0.3) \| (1.0) \| (0.6) \| (9.9) \| (11.8)", footnote "Primarily consists of decreases of $10.3 million for facility closures and $1.0 million in ASC 715 pension adjustment." FY2013 10-K, 2012: "Cash payments \| (22.6) \| — \| (1.6) \| (12.6) \| (36.8)", Other (1.8), footnote "Primarily consists of decreases of $0.5 million related to a goodwill write-off on a sale of business ...". Cash payments larger by 10.0 and Other smaller by 10.0 [calc]; closing balance 21.0 both years. | P50 p.126; P80 p.141 | Facility-closure payments reclassified from Other to cash payments. | A 2012 non-cash reduction of the reserve is now described as cash paid, with no revision note [inf: P50, P80]. | none (E24 does not list it) | Explanation. Not found [P80, P68]. | P3 |  |
| F4-C6-02 | C6 Simply Wheelz loss below the range estimated in Q3 2013 | Q3 FY2013 to FY2013 | Q3 2013: "We currently estimate our total exposure to FSNA's liquidity issues to be between $50 and $70 million." FY2013: "Impairment charges and other(10) \| (44.0)", footnote "Related to FSNA and its subsidiary, Simply Wheelz." 44.0 is 6.0 below the low end [calc]; the FY2013 filing does not restate the range [not found: P70, P85, P62]. | P265 p.37; P77 p.134 | The 16 December 2013 settlement gave orderly return of vehicles and may have reduced the exposure [P70 p.101]. | Part of the 6 to 26m remaining exposure named in Q3 may sit in other lines or be unrecognized [inf: P265, P77]. | E10 | FSNA-related charges by line for 2013. Not found. | P3 |  |
| F4-C6-03 | C6 public liability and property damage reserve basis reworded | FY2012, FY2013 | FY2011: "Reserve requirements are based on actuarial evaluations ..." FY2012: "Reserve requirements are based on rental volume and actuarial evaluations ..." FY2013: "The increase in public liability and property damage reserves was primarily related to Dollar Thrifty." (liability 332.2 to 347.7, +15.5 [calc]); "Our actual results as compared to our estimates have historically resulted in relatively minor adjustments to our recorded liability." | P6 p.53; P34 p.45; P61 p.138; P63 p.45 | Rental volume was an existing input now named; Dollar Thrifty added exposure (E9). | A change in reserve basis can move the reserve without a change in claims experience; no prior-year development is given to test the 'minor adjustments' sentence [inf: P34, P63]. | E9 | Rollforward with prior-year development. Not found [P86 holds allowance and tax valuation only; P61; P79]. | P3 |  |
| F4-D4-01 | D4 company purchases of executives' homes (relocation) | FY2013 | "The total amount that we spent under the program during the year ended December 31, 2013 was $3.1 million for the executive officers." Q3 2013: $0.6m for nine months; Q4 derived 2.5m [calc]. New paragraph on transactions with companies where directors serve. | P82 p.147; P262 p.34 | Standard relocation programme approved by the Compensation Committee, prices from averaged appraisals [P82 p.147]. | Company-funded purchases of executives' homes concentrated in Q4; resale results not disclosed [inf: P82, P262]. | E20; relocation announced May 2013 [P228 p.8] | Resale outcomes and executives covered. Not found. | P3 |  |
| F4-C2-01 | C2 non-GAAP labels and categories changed | FY2013 | FY2012 10-K: "Non-cash debt charges(3) \| (83.6)" and "Other(9) \| (44.0)". FY2013 10-K: "Debt-related charges(3) \| (68.4) \| (83.6)"; Q4 2013 release shows the FY2012 44.0 as "Other unusual/non-recurring". New 2013 lines: Integration expenses, Relocation costs, Impairment charges and other. | P48 p.120; P77 p.134; P295 p.9 | Footnote (3) describes the same items; new lines reflect new 2013 events and prior years show dashes [P77 p.134]. | The non-cash qualifier was dropped and prior-year items relabelled non-recurring after the fact (see F4-D3-07) [inf: P48, P77, P295]. | E9, E10, E13 | In pack. | P3 |  |
| F4-C2-02 | C2 operating metric definitions changed | Q1 FY2012; Q1 to Q2 FY2013 | Equipment pricing metric moved to the American Rental Association method; total RPD introduced, corrected for Q2 2013 and redefined to exclude sublease revenue [context sheet E8, E14]. | P166 p.39; P287 pp.1, 3; P290 p.1; P291 p.1 | Definition changes disclosed at the time. | Trend comparisons across the change may not be like for like [inf: P291]. | E8, E14 | Recast prior periods. Not found [P291, P293]. | P4 |  |
| F4-C16-01 | C16 comparative figures changed without line-level explanation | FY2012; Q1 FY2012 | 2012 gains on disposal of property and equipment: FY2012 note "$6.3 million" "included in "Direct operating""; FY2013 note "$8.3 million" "included in our consolidated statements of operations" (+2.0 [calc]). Q1 2012 depreciation of revenue earning equipment 530.4 in the Q1 2012 10-Q, 531.4 in the Q1 2013 10-Q (+1.0 [calc]), a change reported before the E24 errors were identified in Q4 2013 [inf: P213, P68]. Q1 2012 non-program cars sold: "approximately 40,000" in the Q1 2012 10-Q, "75,400 and 43,000" (2013, 2012) in the Q1 2013 10-Q (+3,000 [calc]). | P39 p.81; P68 p.91; P154 p.11 and p.12; P213 p.13; P225 p.35 | Small reclassifications to conform presentation. | Comparatives changed with no stated reason [inf: P68, P213]. | E24 (partly) | Line reconciliation. Not found [P68 pp.83-89; P208]. | P3 |  |
| F4-C16-02 | C16 revision disclosures found by search | FY2010 to Q3 FY2013 | Hits: Q1 and Q2 2011 cash flow revisions for 2010 (P91 p.7, P111 p.7); Q3 2011 and FY2011 revision of FY2008 to FY2010 (P131 p.7, P11 p.92); FY2012 parent-only cash flow correction (P37 p.138); Q2 and Q3 2013 revolver gross-up (P229 p.8, P249 p.8); FY2013 correction of errors (P68 pp.83 to 89). | P91; P111; P131; P11; P37; P229; P249; P68 | All on the context sheet. | Repeated corrections across three years, carried at F1 [inf: F1 ledger]. | E1, E4, E12, E17, E24 | In pack. | P4 |  |

```csv
ID,Item,Period,Evidence,Locator,Benign reading,Adverse reading,Context,Resolving disclosure,Priority,Verdict
F4-D3-01,D3 check 2: car holding periods against depreciation per unit of gross fleet,FY2011 to FY2013; Q1 FY2013 to Q4 FY2013,"Holding periods: ""Cars | 4 to 26 months"" (FY2011), ""Cars | 4 to 28 months"" (FY2012), ""Cars | 4 to 36 months"" (FY2013). Provision for depreciation of revenue earning equipment / average gross fleet: 16.22% FY2011, 15.28% FY2012, 14.25% FY2013 [calc]; same-quarter change FY2013 against FY2012: Q1 -2.17, Q2 -1.33, Q3 -1.07, Q4 -1.33 percentage points [calc]. FY2013 critical estimates add ""Depreciation rates are adjusted prospectively through the remaining expected life."" The effect of the longer holding periods is not given separately. Row triggers (a) latest value lowest in series and (b) six consecutive same-quarter declines Q3 FY2012 to Q4 FY2013 [calc].","P11 p.94; P39 p.81; P68 p.91; P63 p.45; P74 p.126; P1 BS_A and BS_Q (Equipment held for rental or lease, gross)","Fleet mix moved toward non-program cars, which the company says have lower depreciation rates (P225 p.35), and Dollar Thrifty cars entered at fair value (E9); longer holding periods for risk cars lower monthly depreciation by design; the aggregate effect of 2013 rate changes is disclosed (U.S. -44.2m, international +5.0m) [P74 p.126].","Holding periods were lengthened and rates lowered in the year car disposals moved from gains to losses (F4-D3-06), which lowers current depreciation and can push cost into later disposal losses; the part due to holding periods is not quantified [inf: P68, P74, P62].","E22 depreciation-rate changes; E24 revision (FY2013 and derived Q4 FY2013 on revised basis; on the revised basis the annual series is 16.14%, 15.17%, 14.27% and Q4 FY2013 with the 9M correction added back is 13.17% [calc]); E9","Split of the 2013 rate effect between holding periods and residual assumptions; average holding period by year; car-only gross cost and depreciation. Not found [P74, P63, P62, P77 searched 'holding period', 'average age', 'months'].",P1,
F4-D3-02,D3 check 2: finite-lived intangible lives stated two ways in the same note,"FY2012, FY2013","FY2012 note 2: ""Other intangible assets | 3 to 20 years"" and ""...which range from two to fifteen years."" FY2013 note 2: ""Other intangible assets | 3 to 10 years"" and ""...which range from two to fifteen years.""",P39 p.81 and p.83; P68 p.91 and p.93,"The useful-life table line may cover a narrower class than all finite-lived intangibles, or one of the two statements was not updated when the other was [inf: P39, P68].","Two stated lives for the same asset class disagree; if amortization follows the longer range, expense is lower than the shorter range implies [inf: P39, P68].","E9 and E21 (Dollar Thrifty intangibles 1,545)","Lives by intangible class. Not found [P69 searched 'years', 'life', 'useful'].",P1,
F4-D3-03,"D3 check 3: explanation of lower depreciation, Q1 2013",Q1 FY2013,"MD&A: ""The decrease as a percent of revenues was driven primarily by an increase in residual values and corresponding lower depreciation rates in the first quarter of 2013 compared to the first quarter of 2012."" and ""In addition, residuals remained fairly strong during the period."" Same filing, note 7: vehicle disposals ""included net losses of $3.3 million and net gains of $34.9 million"" (Q1 2013, Q1 2012); per non-program car sold -44 against +812 USD [calc]; rate changes in the quarter were a decrease of $0.7m.",P225 p.42 and p.35; P213 p.13,"Residual values in the sentence may mean expected values at future disposal or an index level, not realized proceeds; sales volume rose to 75,400 from 43,000 cars and included Dollar Thrifty cars recorded at fair value [P225 p.35; E9].","The explanation credits higher residual values for lower depreciation while the same filing shows realized disposal results moving from gains to losses [inf: P225, P213].",E9; E22; E24 (Q1 2013 revised: depreciation and lease charges 587.0 to 580.1 [P68 p.85]),"Realized proceeds per car and the residual index used. Not found [P225, P213, P287, P288].",P1,
F4-D3-04,"D3 check 3: explanation of lower depreciation, Q2 2013",Q2 FY2013,"MD&A: ""In the six months ended June 30, 2013, our monthly per vehicle depreciation costs decreased as compared to the prior year period due to improved residual values in the U.S., ..."" and ""In addition, residuals have remained relatively strong during the period."" Note 7: rate changes ""resulted in net decreases of $14.8 million"" in the quarter; disposals ""included net losses of $17.5 million and net gains of $38.3 million""; per car -250 against +857 USD [calc]. Call slides: ""Auction/dealer residuals softer than expected"".",P246 p.38 and p.46; P234 p.13 and p.14; P292 p.11,"The statement compares six months with six months; the slides say retail residuals stayed strong while auction residuals softened, so rates may rest on a retail-heavy disposal plan [P292 p.11].","Depreciation rates were lowered on higher expected residuals in a quarter when realized sales produced losses and management's own slides describe softer auction residuals [inf: P234, P246, P292].",E22; E24 (Q2 2013 revised: 641.1 to 627.5 [P68 p.85]); E14,"Residual assumptions by channel behind the Q2 rate change. Not found [P234, P246, P289, P292].",P1,
F4-D3-05,"D3 check 3: explanation of lower depreciation, Q3 2013",Q3 FY2013,"MD&A: ""In the nine months ended September 30, 2013, our monthly per vehicle depreciation costs decreased as compared to the prior year period due to residual values that remained strong in the U.S., ..."" Note 7: U.S. rate changes ""resulted in net decreases of $18.0 million and $35.3 million"" (three and nine months); U.S. disposals ""included net losses of $11.1 million and net gains of $15.2 million""; per U.S. car -275 against +578 USD [calc].",P266 p.41 and p.50; P254 p.14,"Rate reductions reflect channel diversification and retail expansion, which the note names as drivers [P254 p.14].","The same filing attributes higher depreciation as a share of revenue to losses on vehicle sales (P266 p.50) while crediting strong residual values for lower per-vehicle depreciation [inf: P266, P254].",E22; E24 (Q3 2013 revised: 676.7 to 674.9 [P68 p.87]),"As F4-D3-04. Not found [P254, P266, P293, P294].",P1,
F4-D3-06,"D3 check 3: residual values described both ways, FY2013",FY2013,"MD&A U.S. segment: ""The increase was primarily attributable to an increase in average fleet due to the Recent Acquisitions and a deterioration in the used vehicle residual values."" Same document and note 8: U.S. rate changes ""resulted in net decreases of $44.2 million"" and ""The cumulative effect of the reduction in rates was also indicative of the residual values experienced in the U.S. ..."" Note 8: disposal loss ""primarily due to a combination of declining residual values from falling demand for used vehicles and timing of sales"". U.S. per car -244 against +738 USD [calc]; U.S. disposal swing -148.8m [calc]. FY2012 note 8 said ""indicative of the strong residual values"" (word ""strong"" not in FY2013). International: rate changes increased depreciation by 5.0m while MD&A cites ""slight strengthening of used vehicle residual values"".","P62 p.54, p.42, p.43; P74 p.126; P45 p.113","Rate reductions are prospective and were set in earlier quarters (9M -35.3m, derived Q4 -8.9m [calc]); the note also credits channel diversification, retail expansion and longer holding periods, which are not residual-value effects [P74 p.126].","One document says residual values deteriorated (raising segment depreciation) and that rate reductions reflect residual values experienced; lower rates in a year of disposal losses can defer cost [inf: P62, P74].",E22; E24; E9,"Residual assumption by quarter and reconciliation of rate changes to realized proceeds. Not found [P74, P62, P63, P295, P296].",P1,
F4-D3-07,D3 check 7: recurring charges under a non-recurring or one-time label,Q4 2010 to Q4 2013; FY2009 to FY2013,"Releases: ""Corporate EBITDA excludes the impact of extraordinary, unusual or non-recurring gains or losses or charges or credits."" The table of those items is non-zero in 13 of 13 quarterly releases and includes restructuring charges in 8 of the last 8 [calc]; restructuring charges recorded in 5 of 5 fiscal years FY2009 to FY2013 (106.8, 54.7, 56.4, 38.0, 77.0) [calc count]. 10-K: adjusted pre-tax income adds back ""certain one-time charges and non-operational items"", including restructuring every year. FY2012 ""Other(9) | (44.0)"" is shown as ""Other unusual/non-recurring"" in the Q4 2013 release.",P295 p.3 and p.9; P77 p.131 and p.134; P48 p.120; P21 p.138; P50 p.125; P80 p.140,"The Corporate EBITDA label follows the credit agreement definition; restructuring is disclosed as an ongoing programme, so a reader can see it recurs [P295 p.3; P80 p.140].","Charges that recur every year are presented under a non-recurring or one-time label, which can make recurring costs look exceptional [inf: P295, P77, P80].","E9, E10 (acquisition and divestiture costs in 2012 and 2013)","Whether any filed measure (10-K, 10-Q) carries the non-recurring label: searched P5, P33, P62 and the nine 10-Q mdna files; only 'one-time' found. Whether Item 10(e)(1)(ii)(B) reaches the furnished releases is for the analyst.",P1,
F4-D2-01,D2 fleet-cost risk factor reworded; expectation dropped,FY2013,"Before: ""Declines in the value of the non-program cars in our fleet and declines in the overall number of program cars in our fleet could materially adversely impact our financial condition, results of operations, liquidity and cash flows."" After: ""Increased fleet costs, either generally or due to declines in the value of the non-program cars in our fleet, could materially adversely impact our financial condition, results of operations, liquidity and cash flows."" Dropped: ""We expect this percentage to continue to decrease in the future, particularly as we integrate the operations of Dollar Thrifty, ...""",P31 p.22; P60 p.23,"Program-car share was 30% of purchases in both 2012 and 2013 [P60 p.23], so the expectation of further decline no longer applied; the heading was broadened.","The heading now leads with increased fleet costs in the year disposal results turned to losses (F4-D3-03 to F4-D3-06) [inf: P60, P74].",E9,"Residual assumptions and program share by quarter. Not found [P60, P62].",P2,
F4-D2-02,D2 statement on car supply arrangements removed,FY2013,"FY2012: ""We are not a party to any long-term car supply arrangements with manufacturers."" Not in FY2013 [not found: P60, P59 searched ""car supply"", ""supply arrangement""].",P31 p.22; P60 p.23,"Editorial shortening of an unchanged risk [inf: P31, P60].","A long-term supply arrangement may now exist whose terms are not described [inf: P31, P60].",none,Supply terms in Item 1. Not found [P59].,P3,
F4-D2-03,"D2 multiemployer pension risk hardened, then softened","FY2012, FY2013","FY2011: ""At least one multiemployer plan in which we participate is reported to have, and other of our multiemployer plans could have, significant underfunded liabilities."" FY2012: ""Several of our remaining multiemployer plans have underfunded liabilities."" FY2013: ""Our multiemployer plans could have significant underfunded liabilities.""",P3 p.31; P31 p.25; P60 p.26,"After the December 2012 withdrawal (cost 23.2m, P295 p.2 note (c)) the remaining plans may be better funded.","A statement of fact became a possibility without a disclosed change in funding [inf: P31, P60].",none,Plan funding zones: zone table in note 6 (P72 p.121); zones not tabulated in this step.,P3,
F4-D2-04,D2 new risk: key employees and headquarters relocation,FY2013,"""In addition, our key employees may be distracted by activities unrelated to our business, including the relocation of our corporate headquarters from Park Ridge, New Jersey to Estero, Florida.""",P60 p.26,Relocation announced May 2013 [P228 p.8]; the risk describes a known event.,"Finance and management disruption in the year of the E24 errors, the E19 system change and the E20 CFO change [inf: P60, P68, P87].","E19, E20","Status of finance staff relocation. Not found [P60, P62, P87].",P3,
F4-D2-05,D2 new risk: losses from FSNA and Simply Wheelz; likelihood softened between Q3 and FY2013,"Q3 FY2013, FY2013","Q3 2013 10-Q: ""We have recognized losses as a result of our relationship with FSNA and Simply Wheelz and are likely to incur additional losses."" FY2013: ""We have recognized losses as a result of our relationship with Franchise Services of North America, or ""FSNA,"" and Simply Wheelz and may incur additional losses.""",P267 p.76; P60 p.24,"The 16 December 2013 settlement fixed payments and the return of vehicles, which may have lowered the likelihood of further loss [P70 p.101].","Likely became may with no amount given for the remaining exposure named in Q3 (see F4-C6-02) [inf: P267, P60, P265].",E10,"Remaining FSNA exposure at 31 December 2013. Not found [P70, P77, P85].",P3,
F4-D2-06,D2 like-kind exchange risk adds fleet net book value as a trigger,FY2012,"Before: ""A material and extended reduction in vehicle purchases or a downsizing of our car rental fleet, for any reason, ..."" After: ""A material reduction in the net book value of our car rental fleet, a material and extended reduction in vehicle purchases and/or a material downsizing of our car rental fleet, for any reason, ...""",P3 p.27; P31 p.22,Clarifies the mechanism and adds Dollar Thrifty's own programme (E9).,"Links fleet book value, and so depreciation choices, to the timing of material tax payments [inf: P31].",E9,Deferred tax attributable to the programme. Not reviewed in this step (P75).,P3,
F4-C10-01,"C10 Sobel concession-fee case: stated potential judgment, no accrual stated",FY2013 (first in Q1 FY2013),"FY2012: ""The court has since entered a stay order and the parties will again be engaging in mediation."" FY2013: ""A judgment - which could potentially exceed $40.0 million - has still not been issued by the court."" and ""We continue to believe the outcome of this case will not be material to our financial condition, results of operations or cash flows."" Q1 2013 said the findings ""will be reversed""; that sentence is not in FY2013 [not found: P61, P79]. 40.0 is 6.03% of FY2013 pre-tax income [calc].",P32 p.32; P61 p.137; P222 p.29,An interlocutory appeal and mediation are pending; the general statement on unaccrued matters may cover this case [P61 p.137-138].,"Partial summary judgment on restitution and class certification went against the company and a potential judgment above $40.0m is stated, but no accrual, likelihood term or range is given for the matter [inf: P61].",none,"ASC 450-20 accrual or reasonably possible range for this matter. Not found [P61, P79, P243, P263 searched 'probable', 'reasonably possible', 'accru' near Sobel].",P3,
F4-C10-02,C10 new securities class action,FY2013,"""On November 20, 2013, a purported shareholder class action, Pedro Ramirez, Jr. v. Hertz Global Holdings, Inc., et al., was commenced ..."" alleging misstatements ""during the period from February 25, 2013 through November 4, 2013"".",P61 p.138,Newly filed; no estimate is usually possible at this stage.,"The class period covers the quarters later revised under E24 [inf: P61, P68].",E24,"Statement on estimate of loss. Not found [P61, P79].",P3,
F4-C10-03,C10 accruals appear for three class actions,FY2012,"FY2011: ""All proceedings in the case are currently stayed while the parties engage in settlement discussions."" FY2012: ""... have accrued our best estimate of the ultimate cost which is not material to our financial condition."" Q4 2013 release: 2012 adjustments include a ""litigation accrual of $14.0 million"".",P4 p.40; P32 p.32; P295 p.2,Settlements reached in 2012 and 2013 [P61 p.136-138].,"Matters each called not material add up to an amount the company excludes from adjusted results [inf: P32, P295].",none,"Accrual by matter. Not found [P32, P49].",P3,
F4-C10-04,C10 SEC investigation closed,FY2012,"FY2011: ""We intend to cooperate fully with the SEC's investigation."" FY2012: ""On February 14, 2013, we were informed by the staff that the investigation has been completed and that no action was taken by the staff or the SEC.""",P4 p.38; P32 p.32,Resolution with no action.,None beyond the fact of the prior investigation [inf: P32].,none,In pack.,P3,
F4-C14-01,C14 auditor report unchanged; no paragraph on the revision,FY2013,"Unqualified opinions; FY2013 names ""Internal Control—Integrated Framework 1992""; the Dollar Thrifty scope exclusion ends; no explanatory paragraph on the E24 revision [not found: P65 ""revis"", ""error""].",P65 p.74; P36 p.71,"The company judged the errors immaterial to prior periods [P68 p.83], a case in which no explanatory paragraph is expected [inf].",None beyond F1-C15-1.,E24,In pack (P65).,P4,
F4-C13-01,C13 depreciation estimate wording changed; no sensitivity in the 10-K,FY2013,"Before: ""These key factors are considered when estimating future residual values and assessing depreciation rates."" and ""... we use historical experience and monitor market conditions to set depreciation rates."" After: ""These key factors are considered when estimating future residual values. Depreciation rates are adjusted prospectively through the remaining expected life."" and ""... we use historical experience, as well as industry residual value guidebooks, and the monitoring of market conditions, to set depreciation rates."" No change amount or sensitivity in any year's critical estimates [not found: P6, P34, P63]; the Q4 2013 slides give one: ""1% change to residuals = $83M adjusted pre-tax income"".",P34 p.44; P63 p.45; P296 p.21,Clarifies existing practice; guidebooks are a benchmark the slides also cite [P294 p.10].,"A new outside input to residual estimates appears in the year estimated residuals rose while realized residuals fell; the sensitivity exists but is not in the filing [inf: P63, P296, P74].",E22,"Quantified effect of the guidebook input. Not found [P63, P74].",P2,
F4-C13-02,C13 stock-option volatility estimate method changed,FY2012,"FY2011: ""Therefore, we use the calculated value method to estimate the expected volatility, ..."" FY2012: ""Beginning in 2012, we have determined that there is now sufficient historical information available to estimate the expected volatility of our stock price.""",P6 p.56; P34 p.47,Stated reason: enough trading history after 2006 listing.,Change in an estimate input with no stated effect on expense [inf: P34].,none,Effect on 2012 option expense. Not found [P44].,P3,
F4-A8-01,A8 gains on sales of operations to franchisees kept in operating income,FY2012 (new policy text),"""Such gains or losses are included in operating income because they are expected to be a recurring part of our business.""",P39 p.84,Policy disclosure added alongside franchise revenue recognition.,"Gains on disposals of operations sit in operating results; amounts not disclosed [not found: P39, P68 searched 'franchisee' with 'gain'].","E3, E16 (franchise reacquisitions)",Amount of such gains by year. Not found.,P3,
F4-A8-02,A8 revenue lines reclassified and relabelled,Q2 FY2013 onward,"Other revenue reclassified in Q2 2013 and relabelled with the Q3 2013 segment recast; FY2012 car rental 7,456.1 to 7,161.7 [context sheet E17, E18].",P227 p.3; P247 p.3; P66 p.76,Presentation change with total revenue unchanged apart from E24.,"Line-level trends before and after Q2 2013 are not comparable [inf: P1, P227].","E17, E18",Reason for the Q2 2013 reclassification beyond the generic sentence. Not found [P229].,P4,
F4-A4-01,A4 receivable concentration statement dropped,"FY2012, FY2013","FY2011: ""Concentrations of credit risk with respect to trade receivables are limited due to the large number of customers ..."" and ""As of December 31, 2011, we had no significant concentration of credit risk."" From FY2012 the concentration paragraph covers cash and derivatives only [P68 p.90].",P22 p.139; P39 p.80; P68 p.90,Moved into the policy note and shortened.,"Dropped in the period one counterparty, Simply Wheelz, subleased about 20,000 vehicles and later owed amounts in an estimated 50 to 70m exposure [inf: P60 p.24, P265 p.37].",E10,Receivables by counterparty. Not found.,P3,
F4-A4-02,A4 2012 allowance for doubtful accounts revised,FY2012 as reprinted,"FY2012 Schedule II: ""Year ended December 31, 2012 | $20,282 | $34,144 | ..."" (thousands). FY2013: ""Year ended December 31, 2012(b) | 20.3 | 38.3 | ..."" (millions); charged to expense +4.16m [calc].",P56 p.140; P86 p.158,Brazil allowance correction in E24.,None beyond E24.,E24,In pack (P68 pp.83-89).,P4,
F4-C7-01,C7 other useful-life ranges changed without comment,FY2013,"FY2012: ""Buildings | 3 to 50 years"", ""Capitalized internal use software | 1 to 15 years"". FY2013: ""Buildings | 5 to 50 years"", ""Capitalized internal use software | 1 to 10 years"". No statement that lives changed [not found: P68 ""change in estimate"", ""useful li""].",P39 p.81; P68 p.91,Table updated to reflect assets held; the software change shortens lives.,An unexplained change in stated lives; effect not given [inf: P68].,none,Effect of any change in lives. Not found.,P3,
F4-C6-01,C6 2012 restructuring rollforward re-described,FY2012 as reprinted in FY2013,"FY2012 10-K, 2012: ""Other(2) | (0.3) | (1.0) | (0.6) | (9.9) | (11.8)"", footnote ""Primarily consists of decreases of $10.3 million for facility closures and $1.0 million in ASC 715 pension adjustment."" FY2013 10-K, 2012: ""Cash payments | (22.6) | — | (1.6) | (12.6) | (36.8)"", Other (1.8), footnote ""Primarily consists of decreases of $0.5 million related to a goodwill write-off on a sale of business ..."". Cash payments larger by 10.0 and Other smaller by 10.0 [calc]; closing balance 21.0 both years.",P50 p.126; P80 p.141,Facility-closure payments reclassified from Other to cash payments.,"A 2012 non-cash reduction of the reserve is now described as cash paid, with no revision note [inf: P50, P80].",none (E24 does not list it),"Explanation. Not found [P80, P68].",P3,
F4-C6-02,C6 Simply Wheelz loss below the range estimated in Q3 2013,Q3 FY2013 to FY2013,"Q3 2013: ""We currently estimate our total exposure to FSNA's liquidity issues to be between $50 and $70 million."" FY2013: ""Impairment charges and other(10) | (44.0)"", footnote ""Related to FSNA and its subsidiary, Simply Wheelz."" 44.0 is 6.0 below the low end [calc]; the FY2013 filing does not restate the range [not found: P70, P85, P62].",P265 p.37; P77 p.134,The 16 December 2013 settlement gave orderly return of vehicles and may have reduced the exposure [P70 p.101].,"Part of the 6 to 26m remaining exposure named in Q3 may sit in other lines or be unrecognized [inf: P265, P77].",E10,FSNA-related charges by line for 2013. Not found.,P3,
F4-C6-03,C6 public liability and property damage reserve basis reworded,"FY2012, FY2013","FY2011: ""Reserve requirements are based on actuarial evaluations ..."" FY2012: ""Reserve requirements are based on rental volume and actuarial evaluations ..."" FY2013: ""The increase in public liability and property damage reserves was primarily related to Dollar Thrifty."" (liability 332.2 to 347.7, +15.5 [calc]); ""Our actual results as compared to our estimates have historically resulted in relatively minor adjustments to our recorded liability.""",P6 p.53; P34 p.45; P61 p.138; P63 p.45,Rental volume was an existing input now named; Dollar Thrifty added exposure (E9).,"A change in reserve basis can move the reserve without a change in claims experience; no prior-year development is given to test the 'minor adjustments' sentence [inf: P34, P63].",E9,Rollforward with prior-year development. Not found [P86 holds allowance and tax valuation only; P61; P79].,P3,
F4-D4-01,D4 company purchases of executives' homes (relocation),FY2013,"""The total amount that we spent under the program during the year ended December 31, 2013 was $3.1 million for the executive officers."" Q3 2013: $0.6m for nine months; Q4 derived 2.5m [calc]. New paragraph on transactions with companies where directors serve.",P82 p.147; P262 p.34,"Standard relocation programme approved by the Compensation Committee, prices from averaged appraisals [P82 p.147].","Company-funded purchases of executives' homes concentrated in Q4; resale results not disclosed [inf: P82, P262].",E20; relocation announced May 2013 [P228 p.8],Resale outcomes and executives covered. Not found.,P3,
F4-C2-01,C2 non-GAAP labels and categories changed,FY2013,"FY2012 10-K: ""Non-cash debt charges(3) | (83.6)"" and ""Other(9) | (44.0)"". FY2013 10-K: ""Debt-related charges(3) | (68.4) | (83.6)""; Q4 2013 release shows the FY2012 44.0 as ""Other unusual/non-recurring"". New 2013 lines: Integration expenses, Relocation costs, Impairment charges and other.",P48 p.120; P77 p.134; P295 p.9,Footnote (3) describes the same items; new lines reflect new 2013 events and prior years show dashes [P77 p.134].,"The non-cash qualifier was dropped and prior-year items relabelled non-recurring after the fact (see F4-D3-07) [inf: P48, P77, P295].","E9, E10, E13",In pack.,P3,
F4-C2-02,C2 operating metric definitions changed,Q1 FY2012; Q1 to Q2 FY2013,"Equipment pricing metric moved to the American Rental Association method; total RPD introduced, corrected for Q2 2013 and redefined to exclude sublease revenue [context sheet E8, E14].","P166 p.39; P287 pp.1, 3; P290 p.1; P291 p.1",Definition changes disclosed at the time.,Trend comparisons across the change may not be like for like [inf: P291].,"E8, E14","Recast prior periods. Not found [P291, P293].",P4,
F4-C16-01,C16 comparative figures changed without line-level explanation,FY2012; Q1 FY2012,"2012 gains on disposal of property and equipment: FY2012 note ""$6.3 million"" ""included in ""Direct operating""""; FY2013 note ""$8.3 million"" ""included in our consolidated statements of operations"" (+2.0 [calc]). Q1 2012 depreciation of revenue earning equipment 530.4 in the Q1 2012 10-Q, 531.4 in the Q1 2013 10-Q (+1.0 [calc]), a change reported before the E24 errors were identified in Q4 2013 [inf: P213, P68]. Q1 2012 non-program cars sold: ""approximately 40,000"" in the Q1 2012 10-Q, ""75,400 and 43,000"" (2013, 2012) in the Q1 2013 10-Q (+3,000 [calc]).",P39 p.81; P68 p.91; P154 p.11 and p.12; P213 p.13; P225 p.35,Small reclassifications to conform presentation.,"Comparatives changed with no stated reason [inf: P68, P213].",E24 (partly),Line reconciliation. Not found [P68 pp.83-89; P208].,P3,
F4-C16-02,C16 revision disclosures found by search,FY2010 to Q3 FY2013,"Hits: Q1 and Q2 2011 cash flow revisions for 2010 (P91 p.7, P111 p.7); Q3 2011 and FY2011 revision of FY2008 to FY2010 (P131 p.7, P11 p.92); FY2012 parent-only cash flow correction (P37 p.138); Q2 and Q3 2013 revolver gross-up (P229 p.8, P249 p.8); FY2013 correction of errors (P68 pp.83 to 89).",P91; P111; P131; P11; P37; P229; P249; P68,All on the context sheet.,"Repeated corrections across three years, carried at F1 [inf: F1 ledger].","E1, E4, E12, E17, E24",In pack.,P4,
```

## Looked for and not found

- Any matter labelled "remote", "reasonably possible" or "probable" by name, and any stated loss range: P4, P32, P61, P20, P49, P79 and the nine 10-Q contingencies notes, searched "remote", "reasonably possible", "probable", "range of".
- Accrual or likelihood for the Sobel case: P61, P79, P222, P243, P263, searched "accru", "reserve" near "Sobel".
- Change amounts or sensitivities in critical estimates, any year: P6, P34, P63, searched "sensitiv", "basis point", "1%", "increase of".
- Holding-period effect on 2013 depreciation, average holding period, car-only gross cost: P74, P63, P62, P77, searched "holding period", "average age", "months".
- Lives by intangible class: P69, searched "years", "life", "useful".
- Supplier finance, factoring, receivable sales: all text files, s3 terms "factor... receivable", "sale of receivables", "current receivables", "securitiz", "derecogni".
- Bill-and-hold: all text files, s3 terms (0 hits).
- Change orders, unapproved claims: all text files, s3 terms.
- Revenue and receivables by customer: P11, P39, P68, P22, P51, P81, searched "largest customer", "significant customer", "percent of revenue", "concentration".
- Public liability and property damage rollforward: P86, P61, P79, P63, searched "development", "rollforward", "beginning of".
- Explanation of the 2012 restructuring rollforward reclassification and of the 2012 P&E gain change: P80, P68, P39, searched "reclass", "revised", "conform".
- Remaining FSNA exposure at 31 December 2013: P70, P77, P85, P62, searched "FSNA", "Simply Wheelz", "exposure".
- Long-term car supply arrangements in FY2013: P60, P59, searched "car supply", "supply arrangement".
- The checklist file defining D1 to D5, A4, A8, C2, C6 and C10 to C16: not in the pack.

## Could not run

- **C15**: in this step's scope but not named in any method step, and the checklist file is not in the pack; not run.
- **Full sentence-by-sentence classification** of the MD&A, business, financial-statements (whole Item 8), release, slide and proxy pairs: 26,628 added, removed or changed sentences remained after the code's mechanical and wording filters [calc, s5]. The priority sections (risk factors, legal, market risk, auditor, critical estimates, all notes, Schedule II, controls, related parties) were read in full; the rest were covered by the counts, the ten check searches and targeted reads. The proxy pair is outside this step's checklist rows and was counted only.
- **Interim MD&A and interim risk-factor deltas** were counted and searched, not read in full; step 5 asks for notes only.
- **Checks 4, 5, 6, 8, 9**: run, result "cannot test", missing numbers named in section 5.
- **IFRS-specific instructions** (IAS 37 paragraphs 84, 91, 92; IAS 1 paragraphs 122 and 125; Canadian key audit matters; NI 52-112): not applicable, the framework is US GAAP [P0].
- **Tie-out**: none failed that this step relies on; context-sheet warnings W1 to W4 were respected (FY2013 and derived Q4 2013 on the revised basis; sensitivities shown for check 2) [context sheet, section 3].

## Code

All code below was run with Python 3.14 over the pack files; outputs quoted above come from these scripts. Reading searches used grep and sed over the same files; they located text and did not compute any figure.

**f4lib.py**

```python
# f4lib.py : sentence splitting, section pairing and sentence diff for F4
import re, os, difflib
from collections import defaultdict, Counter

PACK = r"C:\Users\aaron\OneDrive\Desktop\Master\WireSift Research\Events\CFA Vancouver Forensic\tests\hertz-fy2013\pack"

def manifest_ids():
    """Map file name (relative to pack) -> P id, read from the manifest's file table."""
    ids = {}
    for line in open(os.path.join(PACK, "manifest.md"), encoding="utf-8"):
        m = re.match(r"\| (P\d+) \| ([^|]+?) \|", line)
        if m:
            ids[m.group(2).strip()] = m.group(1)
    return ids

ABBR = ["U.S.", "Inc.", "No.", "Nos.", "e.g.", "i.e.", "Corp.", "Co.", "L.L.C.", "LLC.", "vs.", "Mr.", "Ms.",
        "Dr.", "Jan.", "Feb.", "Mar.", "Apr.", "Jun.", "Jul.", "Aug.", "Sept.", "Sep.", "Oct.", "Nov.", "Dec.",
        "S.A.", "N.V.", "B.V.", "Ltd.", "St.", "approx.", "Cal.", "Fla.", "N.J.", "N.Y.", "Mass.", "Ill.", "Pa.",
        "Ct.", "Sup.", "Dist.", "Cir.", "et al.", "Bus.", "Prof.", "Code.", "Sec.", "Stat.", "S.p.A.", "U.K.", "p.", "pp."]

def norm(s):
    """Typographic normalisation used only for matching (quotes, hyphens, spaces); quotations keep the filed text."""
    s = s.replace("‑", "-").replace("‐", "-").replace("­", "")
    for q in ("“", "”", "‘‘", "’’", "''"):
        s = s.replace(q, '"')
    s = s.replace("‘", "'").replace("’", "'").replace(" ", " ")
    s = re.sub(r"-\s+(?=[a-z])", "-", s)
    return re.sub(r"\s+", " ", s).strip()

def is_running_header(line):
    return "(Continued)" in line or re.fullmatch(r"ITEM \w+\.?", line) is not None

def paragraphs(text):
    """Yield (paragraph, page), joining a paragraph split by a page break (previous line has no closing
    punctuation and the next text line starts in lower case). Running page headers are dropped."""
    page = None; paras = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("SOURCE:"):
            continue
        m = re.match(r"\[p\. (\d+)\]\s*(.*)", line)
        if m:
            page = int(m.group(1)); line = m.group(2).strip()
            if not line: continue
        if is_running_header(line):
            continue
        if paras and " | " not in line and " | " not in paras[-1][0] and line[:1].islower() \
                and not re.search(r"[.!?:;\)\"”]$", paras[-1][0]):
            paras[-1] = (paras[-1][0] + " " + line, paras[-1][1]); continue
        paras.append((line, page))
    return paras

def split_sentences(text):
    """Return list of (sentence, page) tuples. Table rows (containing ' | ') are one unit each."""
    out = []
    for line, page in paragraphs(text):
        if " | " in line or len(line) < 3:
            out.append((line, page)); continue
        prot = line
        for a in ABBR:
            prot = prot.replace(a, a.replace(".", "\u0001"))
        prot = re.sub(r"(?<=\d)\.(?=\d)", "\u0001", prot)
        prot = re.sub(r"(?<=\b[A-Z])\.(?=\s?[A-Z]\.)", "\u0001", prot)
        parts = re.split(r"(?<=[.!?])[\"”’']*\s+(?=[A-Z\(\"“‘•·])", prot)
        for p in parts:
            p = p.replace("\u0001", ".").strip()
            if p:
                out.append((p, page))
    return out

WORD = re.compile(r"[A-Za-z0-9$%']+")

def words(s):
    return WORD.findall(s.lower())

def mask_digits(s):
    return re.sub(r"\d[\d,\.]*", "#", s)

def diff_sections(textA, textB, thresh=0.5):
    """Sentence-level diff. Returns dict with lists of added, removed, changed (a, b, ratio)."""
    A = split_sentences(textA); B = split_sentences(textB)
    A = [(s, p, norm(s)) for s, p in A]; B = [(s, p, norm(s)) for s, p in B]
    cntA = Counter(n for _, _, n in A)
    unmatchedA = []
    usedA = Counter()
    unmatchedB = []
    # exact matches (multiset)
    remainingA = Counter(cntA)
    for s, p, n in B:
        if remainingA[n] > 0:
            remainingA[n] -= 1
        else:
            unmatchedB.append((s, p))
    tmp = Counter(remainingA)
    for s, p, n in A:
        if tmp[n] > 0:
            unmatchedA.append((s, p)); tmp[n] -= 1
    # candidate pairs through inverted index on words
    idx = defaultdict(set)
    wa = [words(norm(s)) for s, _ in unmatchedA]
    for i, w in enumerate(wa):
        for t in set(w):
            idx[t].add(i)
    cands = []
    for j, (s, p) in enumerate(unmatchedB):
        wb = words(norm(s))
        score = Counter()
        for t in set(wb):
            if len(idx[t]) < 200:
                for i in idx[t]:
                    score[i] += 1
        for i, _ in score.most_common(8):
            r = difflib.SequenceMatcher(None, wa[i], wb, autojunk=False).ratio()
            if r >= thresh:
                cands.append((r, i, j))
    cands.sort(reverse=True)
    ua, ub = set(), set()
    changed = []
    for r, i, j in cands:
        if i in ua or j in ub: continue
        ua.add(i); ub.add(j)
        changed.append((unmatchedA[i], unmatchedB[j], round(r, 3)))
    removed = [unmatchedA[i] for i in range(len(unmatchedA)) if i not in ua]
    added = [unmatchedB[j] for j in range(len(unmatchedB)) if j not in ub]
    numeric_only = [c for c in changed if mask_digits(norm(c[0][0])) == mask_digits(norm(c[1][0]))]
    return dict(nA=len(A), nB=len(B), added=added, removed=removed, changed=changed,
                numeric_only=numeric_only)

def load(name):
    return open(os.path.join(PACK, name), encoding="utf-8", errors="replace").read()

def locate_page(fname, needle):
    """Page marker in force at the first line containing needle; raises if the exact text is absent."""
    page = None
    for line in load(fname).splitlines():
        m = re.match(r"\[p\. (\d+)\]", line.strip())
        if m: page = int(m.group(1))
        if needle in line:
            return page
    raise ValueError("not found")
```

**s1_sectionmap.py**

```python
# s1_sectionmap.py : list sections, pair them year over year, count sentence changes (method steps 1 and 5)
import os, re, json, difflib, sys
sys.path.insert(0, os.path.dirname(__file__))
from f4lib import PACK, manifest_ids, load, diff_sections

OUT = os.path.join(os.path.dirname(__file__), "out")
os.makedirs(OUT, exist_ok=True)
ids = manifest_ids()

def sections(prefix):
    fs = sorted(f for f in os.listdir(PACK) if f.startswith(prefix + "_"))
    return {f[len(prefix) + 1:-4]: f for f in fs}

def key(sec):
    return re.sub(r"^notes-\d+-", "notes:", sec)

def pair(secA, secB):
    """Pair sections by key; notes matched on title with fuzzy fallback."""
    ka = {key(s): s for s in secA}; kb = {key(s): s for s in secB}
    pairs, onlyA, onlyB = [], [], []
    left_b = set(kb)
    for k, s in ka.items():
        if k in kb:
            pairs.append((s, kb[k])); left_b.discard(k); continue
        best, br = None, 0
        for k2 in left_b:
            if k.startswith("notes:") and k2.startswith("notes:"):
                t1, t2 = k[6:], k2[6:]
                r = difflib.SequenceMatcher(None, t1, t2).ratio()
                if t1.startswith(t2) or t2.startswith(t1): r = max(r, 0.9)
                if r > br: best, br = k2, r
        if best and br >= 0.75:
            pairs.append((s, kb[best])); left_b.discard(best)
        else:
            onlyA.append(s)
    onlyB = [kb[k] for k in left_b]
    return pairs, onlyA, sorted(onlyB)

filing_pairs = [("AR-FY2011", "AR-FY2012"), ("AR-FY2012", "AR-FY2013")]
for q in ("Q1", "Q2", "Q3"):
    filing_pairs += [(f"{q}-FY2011", f"{q}-FY2012"), (f"{q}-FY2012", f"{q}-FY2013")]

rows, unpaired, store = [], [], {}
for fa, fb in filing_pairs:
    A, B = sections(fa), sections(fb)
    pairs, onlyA, onlyB = pair(A, B)
    for sa, sb in pairs:
        d = diff_sections(load(A[sa]), load(B[sb]))
        pa, pb = ids[A[sa]], ids[B[sb]]
        rows.append(dict(section=sb, fa=fa, fb=fb, pa=pa, pb=pb, fileA=A[sa], fileB=B[sb],
                         nA=d["nA"], nB=d["nB"], added=len(d["added"]), removed=len(d["removed"]),
                         changed=len(d["changed"]), numeric_only=len(d["numeric_only"])))
        store[f"{fa}|{sa}||{fb}|{sb}"] = d
    for s in onlyA:
        unpaired.append(dict(filing=fa, section=s, pid=ids[A[s]], status=f"in {fa}, no counterpart in {fb}"))
    for s in onlyB:
        unpaired.append(dict(filing=fb, section=s, pid=ids[B[s]], status=f"new in {fb}, no counterpart in {fa}"))

# releases: earnings releases same quarter year over year; call slides mapped to the quarter they cover
rel = {f: f for f in os.listdir(os.path.join(PACK, "releases"))}
er_pairs = []
for q in ("Q1", "Q2", "Q3"):
    er_pairs += [(f"ER-{q}-FY2011", f"ER-{q}-FY2012"), (f"ER-{q}-FY2012", f"ER-{q}-FY2013")]
er_pairs += [("ER-Q4-FY2010", "ER-Q4-FY2011"), ("ER-Q4-FY2011", "ER-Q4-FY2012"), ("ER-Q4-FY2012", "ER-Q4-FY2013")]
slides = {"Q4-FY2010": "OTHER-2011-02-25", "Q1-FY2011": "OTHER-2011-05-02", "Q2-FY2011": "OTHER-2011-08-08",
          "Q3-FY2011": "OTHER-2011-11-07", "Q4-FY2011": "OTHER-2012-02-27", "Q1-FY2012": "OTHER-2012-05-07",
          "Q2-FY2012": "OTHER-2012-08-01", "Q3-FY2012": "OTHER-2012-11-06", "Q4-FY2012": "OTHER-2013-02-28",
          "Q1-FY2013": "OTHER-2013-05-03", "Q2-FY2013": "OTHER-2013-08-01-b", "Q3-FY2013": "OTHER-2013-11-06",
          "Q4-FY2013": "OTHER-2014-03-20"}
sl_pairs = []
for a, b in [("Q4-FY2010", "Q4-FY2011"), ("Q4-FY2011", "Q4-FY2012"), ("Q4-FY2012", "Q4-FY2013")] + \
        [(f"{q}-FY{y}", f"{q}-FY{y+1}") for q in ("Q1", "Q2", "Q3") for y in (2011, 2012)]:
    sl_pairs.append((slides[a], slides[b]))
for fa, fb in er_pairs + sl_pairs + [("PROXY-2012", "PROXY-2013")]:
    sub = "proxy" if fa.startswith("PROXY") else "releases"
    na, nb = f"{sub}/{fa}.txt", f"{sub}/{fb}.txt"
    d = diff_sections(load(na), load(nb))
    rows.append(dict(section="release" if sub == "releases" else "proxy compensation", fa=fa, fb=fb,
                     pa=ids[na], pb=ids[nb], fileA=na, fileB=nb, nA=d["nA"], nB=d["nB"],
                     added=len(d["added"]), removed=len(d["removed"]), changed=len(d["changed"]),
                     numeric_only=len(d["numeric_only"])))
    store[f"{fa}||{fb}"] = d
for f in ("OTHER-2011-01-25", "OTHER-2013-07-30", "OTHER-2013-08-01-a"):
    unpaired.append(dict(filing=f, section="release (one-off)", pid=ids[f"releases/{f}.txt"],
                         status="one-off release, no same-period counterpart"))
unpaired.append(dict(filing="events", section="events.txt", pid=ids["events.txt"], status="event log, not a filing section"))
unpaired.append(dict(filing="statements", section="statements.xlsx", pid=ids["statements.xlsx"], status="workbook, used in Part B"))

json.dump(rows, open(os.path.join(OUT, "sectionmap.json"), "w"), indent=1)
json.dump(unpaired, open(os.path.join(OUT, "unpaired.json"), "w"), indent=1)
import pickle; pickle.dump(store, open(os.path.join(OUT, "diffs.pkl"), "wb"))
print(f"{len(rows)} pairs, {len(unpaired)} unpaired")
for r in rows:
    print(f"{r['fa']}->{r['fb']} | {r['section']} | {r['pa']}->{r['pb']} | n {r['nA']}->{r['nB']} | +{r['added']} -{r['removed']} ~{r['changed']} (numeric-only {r['numeric_only']})")
for u in unpaired:
    print("UNPAIRED", u)
```

**s2_dump.py**

```python
# s2_dump.py : write the added / removed / changed sentences of chosen section pairs for reading (method steps 2 to 4)
import os, sys, pickle, json
sys.path.insert(0, os.path.dirname(__file__))
OUT = os.path.join(os.path.dirname(__file__), "out")
store = pickle.load(open(os.path.join(OUT, "diffs.pkl"), "rb"))
rows = json.load(open(os.path.join(OUT, "sectionmap.json")))
pid = {}
for r in rows:
    pid[(r["fa"], r["fileA"])] = r["pa"]; pid[(r["fb"], r["fileB"])] = r["pb"]

def dump(match, fname, skip_numeric=False, maxlen=None):
    with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
        for k, d in store.items():
            if not all(m in k for m in match): continue
            r = [x for x in rows if f"{x['fa']}|" in k and x['fileB'][:-4].split('_',1)[-1] in k and x['fa'] in k and x['fb'] in k]
            f.write(f"\n######## {k}  {[ (x['pa'], x['pb']) for x in r]}\n")
            f.write("\n=== REMOVED (in earlier year only) ===\n")
            for s, p in d["removed"]:
                f.write(f"- [p. {p}] {s[:maxlen] if maxlen else s}\n")
            f.write("\n=== ADDED (in later year only) ===\n")
            for s, p in d["added"]:
                f.write(f"+ [p. {p}] {s[:maxlen] if maxlen else s}\n")
            f.write("\n=== CHANGED ===\n")
            num = set(id(c) for c in d["numeric_only"])
            for c in d["changed"]:
                if skip_numeric and id(c) in num: continue
                (a, pa), (b, pb), ratio = c
                f.write(f"~ r={ratio}\n  BEFORE [p. {pa}] {a[:maxlen] if maxlen else a}\n  AFTER  [p. {pb}] {b[:maxlen] if maxlen else b}\n")

if __name__ == "__main__":
    # usage: python s2_dump.py outname skip_numeric token1 token2 ...
    dump(sys.argv[3:], sys.argv[1], skip_numeric=sys.argv[2] == "1")
```

**s3_search.py**

```python
# s3_search.py : search every text file in the pack for the consistency-check terms (method step 6) and the
# revision terms (C16); writes hits with file, P id, page and the sentence as filed.
import os, re, sys, json
sys.path.insert(0, os.path.dirname(__file__))
from f4lib import PACK, manifest_ids, split_sentences

ids = manifest_ids()
OUT = os.path.join(os.path.dirname(__file__), "out")
TERMS = {
    "1_impairment": r"no indicators of impairment|no events or changes in circumstances|triggering event|substantially exceed|headroom|impairment",
    "2_lives": r"useful li|holding period|residual value|salvage|estimated life",
    "4_change_orders": r"change order|unapproved|pending approval|under discussion|variable consideration",
    "5_factoring": r"factor(ing|ed)? (of )?receivable|sale of receivables|sales of receivables|current receivables|securitiz|derecogni",
    "6_billhold": r"bill-and-hold|bill and hold|early buy|held for customer",
    "7_nonrecurring": r"non-recurring|nonrecurring|one-time|one time|unusual|infrequent",
    "8_release": r"change in estimate|change in accounting estimate|reversal|favorable adjustment|unused amounts reversed|releas(e|ed) of (the )?(reserve|accrual|allowance)",
    "9_concentration": r"largest customer|significant customer|percent of (our )?(total )?revenue|% of (our )?(total )?revenues|distributor|concentration of credit risk",
    "10_liquidity": r"sufficient|adequate liquidity|meet our obligations",
    "C16_revision": r"\brevision\b|\brevised\b|immaterial error|previously reported|as adjusted|prior period error|correction of an error|\brestated\b|out of period",
    "C2_nongaap_def": r"adjusted pre-tax income|corporate ebitda|adjusted net income|we define|is defined as|are defined as|non-gaap",
}
files = []
for root, _, fs in os.walk(PACK):
    for f in fs:
        if f.endswith(".txt"):
            rel = os.path.relpath(os.path.join(root, f), PACK).replace("\\", "/")
            files.append(rel)
files.sort()
hits = {k: [] for k in TERMS}
for rel in files:
    if rel.endswith("_financial-statements.txt"):
        continue  # duplicates the notes files; searched through the notes files instead
    txt = open(os.path.join(PACK, rel), encoding="utf-8", errors="replace").read()
    for s, p in split_sentences(txt):
        for k, rx in TERMS.items():
            if re.search(rx, s, re.I):
                hits[k].append(dict(file=rel, pid=ids.get(rel, "?"), page=p, text=s))
json.dump(hits, open(os.path.join(OUT, "search.json"), "w"), indent=0)
for k, v in hits.items():
    byfile = {}
    for h in v:
        byfile[h["pid"]] = byfile.get(h["pid"], 0) + 1
    print(k, len(v), "hits in", len(byfile), "files")
```

**adhoc.py**

```python
# adhoc.py : the one-off Python commands run during the review, collected in the order run.
# Each block was run on its own from the command line; none of them produces a figure used in the output
# except where noted (section-pair counts by type, used in the Summary).
import os, re, json, pickle, openpyxl
PACK = r"C:\Users\aaron\OneDrive\Desktop\Master\WireSift Research\Events\CFA Vancouver Forensic\tests\hertz-fy2013\pack"
OUT = os.path.join(os.path.dirname(__file__), "out")

def block1_workbook_structure():
    wb = openpyxl.load_workbook(os.path.join(PACK, "statements.xlsx"), data_only=True)
    for ws in wb.worksheets:
        print("====", ws.title, ws.max_row, ws.max_column)
        for r in ws.iter_rows(min_row=1, max_row=3, values_only=True):
            print(r[:20])

def block2_annual_sheets():
    wb = openpyxl.load_workbook(os.path.join(PACK, "statements.xlsx"), data_only=True)
    for name in ["IS_A", "BS_A", "CF_A", "NOTES"]:
        for r in wb[name].iter_rows(values_only=True):
            if any(v is not None for v in r[1:]): print(name, r)
    for r in wb["EXTRA"].iter_rows(values_only=True):
        print(r[:3], r[15:])

def block3_quarterly_fleet():
    wb = openpyxl.load_workbook(os.path.join(PACK, "statements.xlsx"), data_only=True)
    for name in ["BS_Q", "IS_Q", "CF_Q"]:
        for r in wb[name].iter_rows(values_only=True):
            if r[0] and any(k in r[0] for k in ["Equipment held", "Revenue", "Pre-tax", "Depreciation of equipment", "Line"]):
                print(name, r)

def block4_search_listing():
    h = json.load(open(os.path.join(OUT, "search.json")))
    for k in ["4_change_orders", "5_factoring", "6_billhold", "8_release", "9_concentration"]:
        for x in h[k]:
            print(k, x["pid"], x["file"], "p.", x["page"], "|", x["text"][:400])
    for x in h["C16_revision"]:
        if re.search(r"notes-|schedule", x["file"]) and " | " not in x["text"]:
            print("C16", x["pid"], x["file"], "p.", x["page"], "|", x["text"][:450])
    for x in h["7_nonrecurring"]:
        if " | " not in x["text"] or re.search(r"non-?recurring|one-time|unusual", x["text"], re.I):
            print("7", x["pid"], x["file"], "p.", x["page"], "|", x["text"][:450])
    for x in h["10_liquidity"]:
        if re.search(r"mdna|notes-0[45]-debt|notes-0[78]-debt", x["file"]):
            print("10", x["pid"], x["file"], "p.", x["page"], "|", x["text"][:450])

def block5_interim_notes_reading_file():
    from f4lib import mask_digits, norm
    store = pickle.load(open(os.path.join(OUT, "diffs.pkl"), "rb"))
    keep = r"contingencies|depreciation|goodwill|restructuring|related-party|basis-of-presentation|background|business-comb|subsequent|total-equity"
    out = open(os.path.join(OUT, "interim_notes2.txt"), "w", encoding="utf-8")
    for k, d in store.items():
        if not k.startswith("Q") or "notes-" not in k: continue
        isdebt = re.search(r"debt|financial-instruments|segment|taxes", k)
        if not (re.search(keep, k) or isdebt): continue
        out.write(f"\n######## {k}\n")
        def ok(s):
            if " | " in s or len(s) < 40: return False
            if isdebt and not re.search(r"amortization event|covenant|waiver|default|impair|concentration|factor|securitiz.*receivabl|revis|restat|reclassif|segment", s, re.I): return False
            return True
        for s, p in d["removed"]:
            if ok(s): out.write(f"- [p. {p}] {s}\n")
        for s, p in d["added"]:
            if ok(s): out.write(f"+ [p. {p}] {s}\n")
        for (a, pa), (b, pb), r in d["changed"]:
            if not ok(b) or mask_digits(norm(a)) == mask_digits(norm(b)) or r > 0.97: continue
            out.write(f"~ BEFORE [p. {pa}] {a}\n  AFTER  [p. {pb}] {b}\n")
    out.close()

def block6_pair_counts_by_type():   # used in the Summary: 57 annual, 112 interim, 9 + 9 release, 1 proxy
    from collections import Counter
    rows = json.load(open(os.path.join(OUT, "sectionmap.json")))
    c = Counter()
    for r in rows:
        c["annual" if r["fa"].startswith("AR") else "interim" if r["fa"].startswith("Q") else
          "ER" if r["fa"].startswith("ER") else "slides" if r["fa"].startswith("OTHER") else "proxy"] += 1
    print(c)

def block7_principal_agent_identical():   # used in 4.6: same sentence in all three years
    import hashlib
    for f in ("AR-FY2011", "AR-FY2012", "AR-FY2013"):
        txt = open(os.path.join(PACK, f + "_notes-02-summary-of-significant-accounting-policies.txt"), encoding="utf-8").read()
        s = re.search(r"Rental and rental related revenue[^.]*\.", txt).group(0)
        print(f, hashlib.md5(s.encode()).hexdigest())

if __name__ == "__main__":
    import sys
    sys.path.insert(0, os.path.dirname(__file__))
    for fn in (block1_workbook_structure, block2_annual_sheets, block3_quarterly_fleet, block4_search_listing,
               block5_interim_notes_reading_file, block6_pair_counts_by_type, block7_principal_agent_identical):
        fn()
```

**s4_checks.py**

```python
# s4_checks.py : consistency pass (method step 6). Every number below that is not a literal copied from a file
# is computed here. Literals copied from files carry the file and page in the comment.
import os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from f4lib import PACK, manifest_ids, load
import openpyxl

ids = manifest_ids()
wb = openpyxl.load_workbook(os.path.join(PACK, "statements.xlsx"), data_only=True)

def row(sheet, label):
    ws = wb[sheet]
    hdr = [c for c in next(ws.iter_rows(values_only=True))]
    for r in ws.iter_rows(values_only=True):
        if r[0] == label:
            return dict(zip(hdr[1:], r[1:]))
    raise KeyError(label)

def locate(fname, needle):
    """Return (P id, page) of the first line containing needle, and confirm the exact text is in the file."""
    page = None
    for line in load(fname).splitlines():
        m = re.match(r"\[p\. (\d+)\]", line.strip())
        if m: page = int(m.group(1))
        if needle in line:
            return ids[fname], page
    raise ValueError(f"not found: {needle[:60]} in {fname}")

r2 = lambda x: round(x, 2)
out = []
def show(k, v): out.append(f"{k}: {v}"); print(f"{k}: {v}")

# ---------- Check 2: useful lives / holding periods vs depreciation per unit of gross fleet ----------
# Provision "Depreciation of revenue earning equipment" (before disposal adjustments and rents), USD m:
prov_A = {"FY2011": 1921.8,   # P16 (AR-FY2011 note 7) p.125
          "FY2012": 2165.2,   # P45 (AR-FY2012 note 8) p.113
          "FY2013": 2407.8}   # P74 (AR-FY2013 note 8) p.126
gross_A = row("BS_A", "Equipment held for rental or lease, gross")   # P1 BS_A, USD m
for fy, prev in (("FY2011", "FY2010"), ("FY2012", "FY2011"), ("FY2013", "FY2012")):
    avg = (gross_A[fy] + gross_A[prev]) / 2
    show(f"C2 {fy} provision / average gross fleet (%)", r2(100 * prov_A[fy] / avg))
# quarterly provisions from the 10-Q notes (USD m): Q1 P95 p.10, Q2 P115 p.10, Q3 P135 p.14 (2011);
# Q1 P154 p.11, Q2 P173 p.12, Q3 P192 p.12 (2012); Q1 P213 p.13, Q2 P234 p.13, Q3 P254 p.13 (2013)
prov_Q = {"Q1 FY2011": 418.7, "Q2 FY2011": 453.3, "Q3 FY2011": 528.1,
          "Q1 FY2012": 530.4, "Q2 FY2012": 539.5, "Q3 FY2012": 554.1,
          "Q1 FY2013": 573.0, "Q2 FY2013": 611.8, "Q3 FY2013": 641.3}
for y in ("2011", "2012", "2013"):
    prov_Q[f"Q4 FY{y}"] = prov_A[f"FY{y}"] - sum(prov_Q[f"Q{q} FY{y}"] for q in (1, 2, 3))
gross_Q = row("BS_Q", "Equipment held for rental or lease, gross")
order = [f"Q{q} FY{y}" for y in (2011, 2012, 2013) for q in (1, 2, 3, 4)]
opening = {"Q1 FY2011": gross_A["FY2010"]}
for i, q in enumerate(order[1:], 1):
    opening[q] = gross_Q[order[i - 1]]
rateQ = {}
for q in order:
    avg = (opening[q] + gross_Q[q]) / 2
    rateQ[q] = 100 * 4 * prov_Q[q] / avg
    show(f"C2 {q} provision x4 / average gross fleet (%), Q4 derived = year minus Q1..Q3", r2(rateQ[q]))
for q in (1, 2, 3, 4):
    show(f"C2 Q{q} rate change FY2013 vs FY2012 (percentage points)", r2(rateQ[f"Q{q} FY2013"] - rateQ[f"Q{q} FY2012"]))
    show(f"C2 Q{q} rate change FY2012 vs FY2011 (percentage points)", r2(rateQ[f"Q{q} FY2012"] - rateQ[f"Q{q} FY2011"]))
# holding-period ranges for cars, months: P11 p.94 "4 to 26", P39 p.81 "4 to 28", P68 p.91 "4 to 36"
for f, needle in (("AR-FY2011_notes-02-summary-of-significant-accounting-policies.txt", "Cars | 4 to 26 months"),
                  ("AR-FY2012_notes-02-summary-of-significant-accounting-policies.txt", "Cars | 4 to 28 months"),
                  ("AR-FY2013_notes-02-summary-of-significant-accounting-policies.txt", "Cars | 4 to 36 months")):
    show(f"C2 locator {needle}", locate(f, needle))
show("C2 upper bound of car holding period, change FY2012 to FY2013 (months)", 36 - 28)
show("C2 upper bound of car holding period, change FY2011 to FY2013 (%)", r2(100 * (36 - 26) / 26))
# restated prior-year provision (vendor incentives, E24): FY2012 2,165.2 in P45 vs 2,145.9 in P74
show("C2 FY2012 provision restated in FY2013 10-K minus original", r2(2145.9 - 2165.2))
# sensitivity to the E24 basis break: FY2011 and FY2012 on the FY2013 10-K (revised) provision; FY2012 gross fleet
# as revised (cars 12,548.8 + other 3,240.1, P66 balance sheet comparative); FY2011 gross not reprinted, kept original
g12r = 12548.8 + 3240.1
show("C2 sens: FY2012 gross fleet as revised (USD m)", r2(g12r))
show("C2 sens: FY2012 provision / average gross fleet, revised basis (%)", r2(100 * 2145.9 / ((gross_A["FY2011"] + g12r) / 2)))
show("C2 sens: FY2011 provision / average gross fleet, FY2011 provision as revised 1,912.3 (%)", r2(100 * 1912.3 / ((gross_A["FY2011"] + gross_A["FY2010"]) / 2)))
show("C2 sens: FY2013 provision / average gross fleet, opening = FY2012 revised (%)", r2(100 * 2407.8 / ((g12r + gross_A["FY2013"]) / 2)))
# Q4 2013 derived absorbs the 9M 2013 correction to depreciation and lease charges (-22.3, P68 p.87); add it back
q4adj = prov_Q["Q4 FY2013"] + 22.3
show("C2 sens: Q4 FY2013 provision with 9M correction added back (USD m)", r2(q4adj))
show("C2 sens: Q4 FY2013 rate with 9M correction added back (%)", r2(100 * 4 * q4adj / ((opening["Q4 FY2013"] + gross_Q["Q4 FY2013"]) / 2)))

# ---------- Check 3: explanations of the fleet depreciation movement ----------
# net gain (loss) on disposal of vehicles, USD m, and non-program cars sold (units)
us = {"FY2011": (114.9, 121800), "FY2012": (100.6, 136400), "FY2013": (-48.2, 197700)}  # P74 p.126; P62 p.42
intl = {"FY2011": (-16.0, 54800), "FY2012": (-17.3, 54500), "FY2013": (-15.2, 64500)}  # P74 p.126; P62 p.43
for fy in us:
    show(f"C3 U.S. gain(loss) per non-program car sold {fy} (USD)", round(1e6 * us[fy][0] / us[fy][1]))
    show(f"C3 Intl gain(loss) per non-program car sold {fy} (USD)", round(1e6 * intl[fy][0] / intl[fy][1]))
qdat = {  # quarter: (car disposal result USD m, cars sold, depreciation-rate change USD m; negative = decrease)
    "Q1 FY2012": (34.9, 43000, -0.2), "Q1 FY2013": (-3.3, 75400, -0.7),     # P213 p.13; P225 p.35
    "Q2 FY2012": (38.3, 44700, -37.1), "Q2 FY2013": (-17.5, 70100, -14.8),  # P234 p.13-14; P246 p.38
    "Q3 FY2012 US": (15.2, 26300, None), "Q3 FY2013 US": (-11.1, 40400, -18.0),  # P254 p.14; P266 p.42
}
for k, (g, n, rc) in qdat.items():
    show(f"C3 {k} gain(loss) per non-program car sold (USD)", round(1e6 * g / n))
show("C3 U.S. rate-change decrease Q4 FY2013 derived = FY minus 9M (USD m)", r2(44.2 - 35.3))
show("C3 international rate-change increase Q4 FY2013 derived (USD m)", r2(5.0 - 3.9))
show("C3 car rate-change 9M FY2013 total U.S.+Intl (USD m)", r2(-35.3 + 3.9))
show("C3 car rate-change Q3 FY2013 derived = 9M minus H1 (USD m)", r2((-35.3 + 3.9) - (-15.5)))
show("C3 U.S. disposal result swing FY2013 vs FY2012 (USD m)", r2(-48.2 - 100.6))
for f, needle in (
    ("AR-FY2013_mdna.txt", "a deterioration in the used vehicle residual values"),
    ("AR-FY2013_mdna.txt", "The cumulative effect of the reduction in rates was also indicative of the residual values experienced in the U.S."),
    ("AR-FY2013_mdna.txt", "slight strengthening of used vehicle residual values."),
    ("AR-FY2013_notes-08-depreciation-of-revenue-earning-equipment-and.txt", "declining residual values from falling demand for used vehicles"),
    ("AR-FY2012_notes-08-depreciation-of-revenue-earning-equipment-and.txt", "indicative of the strong residual values experienced in the U.S."),
    ("Q1-FY2013_mdna.txt", "driven primarily by an increase in residual values and corresponding lower depreciation rates"),
    ("Q2-FY2013_mdna.txt", "due to improved residual values in the U.S."),
    ("Q2-FY2013_mdna.txt", "In addition, residuals have remained relatively strong during the period."),
    ("Q2-FY2013_mdna.txt", "driven primarily by a loss realized on vehicle sales in the second quarter of 2013"),
    ("Q3-FY2013_mdna.txt", "due to residual values that remained strong in the U.S."),
    ("Q3-FY2013_mdna.txt", "driven primarily by a loss realized on vehicle sales in the third quarter of 2013"),
    ("releases/OTHER-2013-08-01-b.txt", "Manheim down 4.4% YoY Q2:13"),
    ("releases/ER-Q2-FY2013.txt", "residual value hurdle"),
    ("releases/OTHER-2014-03-20.txt", "Seasonal residual value weakness"),
):
    show(f"C3 locator [{needle[:60]}]", locate(f, needle))

# ---------- Check 7: items labelled non-recurring / one-time ----------
restr = {"FY2009": 106.8, "FY2010": 54.7, "FY2011": 56.4,  # P21 p.138
         "FY2012": 38.0, "FY2013": 77.0}                   # P50 p.125; P80 p.140
show("C7 fiscal years with restructuring charges > 0 (of 5)", sum(1 for v in restr.values() if v > 0))
def nonrec_quarters():
    res = {}
    for f in sorted(os.listdir(os.path.join(PACK, "releases"))):
        if not f.startswith("ER-"): continue
        txt = load("releases/" + f)
        i = txt.find("EXTRAORDINARY, UNUSUAL OR")
        blk = txt[i:i + 4000]
        m = re.search(r"\nRestructuring charges \|([^\n]+)", blk)
        tot = re.search(r"\nTotal extraordinary, unusual or non-recurring items \|([^\n]+)", blk)
        def vals(s):
            return [float(v.replace("$", "").replace(",", "").replace("(", "-").replace(")", "")) if re.search(r"\d", v) else 0.0
                    for v in [x.strip() for x in s.split("|")]]
        rv = vals(m.group(1)) if m else []
        tv = vals(tot.group(1)) if tot else []
        n = len(tv) // 2 if len(tv) >= 8 else len(tv)
        res[f[:-4]] = (rv[n - 1] if rv else None, tv[n - 1] if tv else None, ids["releases/" + f])
    return res
nq = nonrec_quarters()
for k, v in nq.items():
    show(f"C7 {k} ({v[2]}) current-quarter restructuring charges in 'extraordinary, unusual or non-recurring' table; total of table", v[:2])
show("C7 quarters (Q4 2010 to Q4 2013, 13 releases) with a non-zero total of 'extraordinary, unusual or non-recurring items'",
     sum(1 for v in nq.values() if v[1]))
show("C7 of the last 8 quarters (Q2 2012 to Q4 2013 releases) with restructuring charges in that table",
     sum(1 for k, v in nq.items() if k in ["ER-Q1-FY2012","ER-Q2-FY2012","ER-Q3-FY2012","ER-Q4-FY2012","ER-Q1-FY2013","ER-Q2-FY2013","ER-Q3-FY2013","ER-Q4-FY2013"] and v[0]))
# premiums paid on debt added back: 2011 62.4 (P48 p.118), 2013 28.7 (P77 p.134)
show("C7 fiscal years (2011 to 2013) with 'Premiums paid on debt' adjustment", 2)

# ---------- Check 1: impairment sentences vs segment results ----------
seg = {"U.S. car rental": (673.2, 872.8, 1091.1), "International car rental": (145.6, 92.9, 141.2),
       "Worldwide equipment rental": (161.3, 226.2, 292.1), "All other operations": (15.0, 47.6, 57.3)}  # P77 p.131 (recast)
for s, (a, b, c) in seg.items():
    show(f"C1 {s} adjusted pre-tax income change FY2012 vs FY2011 (%)", r2(100 * (b - a) / a))
    show(f"C1 {s} adjusted pre-tax income change FY2013 vs FY2012 (%)", r2(100 * (c - b) / b))
show("C1 goodwill net at 31 Dec 2013 by segment (P69 p.95, copied)", {"US": 1010.8, "Intl": 203.4, "Equip": 97.5, "Other": 35.8})

# ---------- Check 10: liquidity sentence, same words FY2011 to FY2013 ----------
liq = "will be adequate to permit us to meet our debt maturities over the next twelve months."
for f in ("AR-FY2011_mdna.txt", "AR-FY2012_mdna.txt", "AR-FY2013_mdna.txt"):
    show(f"C10 locator {f}", locate(f, liq))
show("C10 locator amortization event in FY2013 MD&A", locate("AR-FY2013_mdna.txt", "unknowingly not met"))

# ---------- Delta-pass numbers ----------
pt = row("IS_A", "Pre-tax income")
show("Sobel: USD 40.0m as % of FY2013 pre-tax income as reported (P1 IS_A)", r2(100 * 40.0 / pt["FY2013"]))
show("Simply Wheelz: FY2013 charge 44.0 below low end of Q3 2013 range 50 (USD m)", r2(50 - 44.0))
show("Simply Wheelz: Q3 2013 reserve + impairment (USD m)", r2(4 + 40.0))
show("Relocation home purchases for executive officers, Q4 2013 derived = FY 3.1 minus 9M 0.6 (USD m)", r2(3.1 - 0.6))
show("Restructuring 2012 cash payments: FY2013 10-K minus FY2012 10-K (USD m)", r2(-36.8 - (-26.8)))
show("Restructuring 2012 'Other' line: FY2013 10-K minus FY2012 10-K (USD m)", r2(-1.8 - (-11.8)))
show("2012 gains on disposal of property and equipment: FY2013 10-K minus FY2012 10-K (USD m)", r2(8.3 - 6.3))
show("Q1 2012 depreciation provision: Q1 2013 10-Q minus Q1 2012 10-Q (USD m)", r2(531.4 - 530.4))
show("Schedule II 2012 allowance charged to expense: FY2013 minus FY2012 10-K (USD m)", r2(38.3 - 34.144))
show("Q1 2012 non-program cars sold: Q1 2013 10-Q minus Q1 2012 10-Q (units)", 43000 - 40000)  # P225 p.35; P154 p.12
show("Program cars share of purchases, change 2011 to 2012 (percentage points)", 30 - 48)
show("Sponsor ownership, change FY2011 to FY2012 risk factors (percentage points)", 26 - 38)
show("Interest-rate sensitivity (1 pp), change FY2012 to FY2013 (USD m)", r2(33.1 - 31.3))
show("PL&PD liability change FY2013 vs FY2012 (USD m)", r2(347.7 - 332.2))

open(os.path.join(os.path.dirname(__file__), "out", "checks.txt"), "w", encoding="utf-8").write("\n".join(out))
```

**s5_map.py**

```python
# s5_map.py : section map table (output section 3) with a code classification of changed sentences
import os, sys, json, pickle, re
sys.path.insert(0, os.path.dirname(__file__))
from f4lib import norm, mask_digits
OUT = os.path.join(os.path.dirname(__file__), "out")
rows = json.load(open(os.path.join(OUT, "sectionmap.json")))
store = pickle.load(open(os.path.join(OUT, "diffs.pkl"), "rb"))
unpaired = json.load(open(os.path.join(OUT, "unpaired.json")))

def strip_refs(s):
    s = re.sub(r"Notes? \d+( and \d+)?", "Note #", s)
    return mask_digits(norm(s)).lower()

# events from the context sheet that rewrite a section mechanically (named before reading, judgment note 3)
EV = [
    (r"notes-0[45]-business-comb|notes-03-goodwill|notes-04-goodwill", {"AR-FY2011": "E2 Donlen, E9 Dollar Thrifty", "AR-FY2012": "E9, E10, E21", "Q": "E2, E6, E9, E10, E15"}),
    (r"notes-02-(summary|basis)", {"AR-FY2012": "E24 revision, E17, E18 segment recast", "AR-FY2011": "E4 revision dropped, E7", "Q": "E4, E7, E11, E17, E18"}),
    (r"segment", {"AR-FY2012": "E18 segment recast", "Q3-FY2012": "E18 segment recast", "Q": "E2, E9"}),
    (r"debt", {"AR-FY2012": "E9 Dollar Thrifty debt, E23", "Q": "E9, E13"}),
    (r"related-part", {"AR-FY2012": "E20 Stockholders Agreement terminated", "Q2-FY2012": "E20", "Q3-FY2012": "E20", "Q": ""}),
    (r"risk-factors", {"AR-FY2011": "E9 merger risk to integration risk", "AR-FY2012": "E10, E20, E26", "Q": "E9"}),
    (r"legal|contingenc", {"AR-FY2012": "Item 3 now cross-refers to note 13 (duplicate text removed)", "Q": ""}),
    (r"auditor|controls", {"AR-FY2011": "E9 ICFR scope exclusion", "AR-FY2012": "E9 exclusion ends, E19", "Q": ""}),
    (r"earnings-", {"AR-FY2012": "E13 convertible notes", "Q": "E13"}),
    (r"schedule-ii|quarterly-financial", {"AR-FY2012": "E24 revision, unit change thousands to millions", "Q": ""}),
    (r"mdna|business|financial-statements", {"AR-FY2011": "E9", "AR-FY2012": "E9, E10, E15, E17, E18, E24; units thousands to millions", "Q1-FY2012": "E9, E13", "Q2-FY2012": "E9, E15, E17", "Q3-FY2012": "E9, E15, E18", "Q": "E2, E6"}),
]
def events(sec, fa, fb=""):
    if sec == "release":
        if re.search(r"FY2013|2013-|2014-", fb): return "E9, E10, E13, E14 total RPD, E18 recast"
        if re.search(r"FY2012|2012-", fb): return "E2, E6, E8, E9"
        return "E2, E4"
    if sec == "proxy compensation": return ""
    for rx, m in EV:
        if re.search(rx, sec):
            return m.get(fa, m.get(fa[:2] if fa.startswith("Q") else "", m.get("Q", "")))
    return ""

lines = ["| Section | Filing pair | Sentences added | Removed | Changed | Mechanical cause, if any |", "|---|---|---|---|---|---|"]
tot = dict(added=0, removed=0, changed=0, numeric=0, renum=0, wording=0, read=0)
for r in rows:
    key = [k for k in store if r["fa"] in k and r["fb"] in k and (r["fileA"][:-4].split("_", 1)[-1] in k or r["section"] in ("release", "proxy compensation"))]
    d = store[key[0]]
    num = ren = wrd = 0
    for (a, _), (b, _), ratio in d["changed"]:
        if mask_digits(norm(a)) == mask_digits(norm(b)): num += 1
        elif strip_refs(a) == strip_refs(b): ren += 1
        elif ratio >= 0.9: wrd += 1
    toread = len(d["changed"]) - num - ren - wrd + len(d["added"]) + len(d["removed"])
    for k, v in (("added", len(d["added"])), ("removed", len(d["removed"])), ("changed", len(d["changed"])),
                 ("numeric", num), ("renum", ren), ("wording", wrd), ("read", toread)):
        tot[k] += v
    cause = []
    if num: cause.append(f"{num} changed = number or date roll-forward")
    if ren: cause.append(f"{ren} = note renumbering or cross-reference")
    if wrd: cause.append(f"{wrd} near-identical wording (ratio 0.9 or more)")
    ev = events(r["section"], r["fa"], r["fb"])
    if ev: cause.append("events: " + ev)
    sec = r["section"] if r["section"] not in ("release", "proxy compensation") else f"{r['section']} ({r['fa']} / {r['fb']})"
    lines.append(f"| {sec} | {r['pa']} {r['fa']} to {r['pb']} {r['fb']} | {len(d['added'])} | {len(d['removed'])} | {len(d['changed'])} | {'; '.join(cause) or 'none'} |")
for u in unpaired:
    lines.append(f"| {u['section']} | {u['pid']} {u['filing']} (unpaired) | n/a | n/a | n/a | {u['status']} |")
open(os.path.join(OUT, "sectionmap.md"), "w", encoding="utf-8").write("\n".join(lines))
print(len(rows), "pairs;", len(unpaired), "unpaired;", tot)
```

**s6_locators.py**

```python
# s6_locators.py : confirm that every quotation used in the output is in the named file, and return its page
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from f4lib import manifest_ids, locate_page
ids = manifest_ids()
Q = [
 ("AR-FY2012_risk-factors.txt", "Declines in the value of the non-program cars in our fleet and declines in the overall number of program cars in our fleet could materially adversely impact"),
 ("AR-FY2013_risk-factors.txt", "Increased fleet costs, either generally or due to declines in the value of the non-program cars in our fleet, could materially adversely impact"),
 ("AR-FY2012_risk-factors.txt", "We expect this percentage to continue to decrease in the future, particularly as we integrate the operations of Dollar Thrifty"),
 ("AR-FY2012_risk-factors.txt", "We are not a party to any long-term car supply arrangements with manufacturers."),
 ("AR-FY2011_risk-factors.txt", "At least one multiemployer plan in which we participate is reported to have, and other of our multiemployer plans could have, significant underfunded liabilities."),
 ("AR-FY2012_risk-factors.txt", "Several of our remaining multiemployer plans have underfunded liabilities."),
 ("AR-FY2013_risk-factors.txt", "Our multiemployer plans could have significant underfunded liabilities."),
 ("AR-FY2013_risk-factors.txt", "including the relocation of our corporate headquarters from Park Ridge, New Jersey to Estero, Florida."),
 ("AR-FY2013_risk-factors.txt", "We have recognized losses as a result of our relationship with Franchise Services of North America"),
 ("AR-FY2011_risk-factors.txt", "A material and extended reduction in vehicle purchases or a downsizing of our car rental fleet"),
 ("AR-FY2012_risk-factors.txt", "A material reduction in the net book value of our car rental fleet"),
 ("AR-FY2012_legal.txt", "The court has since entered a stay order and the parties will again be engaging in mediation."),
 ("AR-FY2013_legal.txt", "A judgment - which could potentially exceed $40.0 million - has still not been issued by the court."),
 ("AR-FY2013_legal.txt", "We continue to believe the outcome of this case will not be material"),
 ("Q1-FY2013_notes-16-contingencies-and-off-balance-sheet-commitments.txt", "findings will be reversed."),
 ("AR-FY2013_legal.txt", "a purported shareholder class action, Pedro Ramirez"),
 ("AR-FY2011_legal.txt", "All proceedings in the case are currently stayed while the parties engage in settlement discussions."),
 ("AR-FY2012_legal.txt", "have accrued our best estimate of the ultimate cost which is not material to our financial condition."),
 ("releases/ER-Q4-FY2013.txt", "litigation accrual of $14.0 million"),
 ("AR-FY2011_legal.txt", "We intend to cooperate fully with the SEC"),
 ("AR-FY2012_legal.txt", "On February 14, 2013, we were informed by the staff that the investigation has been completed"),
 ("AR-FY2013_auditor-report.txt", "Integrated Framework 1992"),
 ("AR-FY2012_critical-estimates.txt", "These key factors are considered when estimating future residual values and assessing depreciation rates."),
 ("AR-FY2013_critical-estimates.txt", "These key factors are considered when estimating future residual values. Depreciation rates are adjusted prospectively through the remaining expected life."),
 ("AR-FY2012_critical-estimates.txt", "we use historical experience and monitor market conditions to set depreciation rates."),
 ("AR-FY2013_critical-estimates.txt", "we use historical experience, as well as industry residual value guidebooks, and the monitoring of market conditions, to set depreciation rates."),
 ("AR-FY2013_critical-estimates.txt", "Our actual results as compared to our estimates have historically resulted in relatively minor adjustments to our recorded liability."),
 ("AR-FY2011_critical-estimates.txt", "Reserve requirements are based on actuarial evaluations"),
 ("AR-FY2012_critical-estimates.txt", "Reserve requirements are based on rental volume and actuarial evaluations"),
 ("AR-FY2013_legal.txt", "The increase in public liability and property damage reserves was primarily related to Dollar Thrifty."),
 ("AR-FY2012_notes-02-summary-of-significant-accounting-policies.txt", "Such gains or losses are included in operating income because they are expected to be a recurring part of our business."),
 ("AR-FY2011_notes-13-financial-instruments.txt", "As of December 31, 2011, we had no significant concentration of credit risk."),
 ("AR-FY2011_notes-13-financial-instruments.txt", "Concentrations of credit risk with respect to trade receivables are limited due to the large number of customers"),
 ("AR-FY2013_notes-02-summary-of-significant-accounting-policies.txt", "Our cash and cash equivalents are invested in various investment grade institutional money market accounts"),
 ("AR-FY2012_schedule-ii.txt", "Year ended December 31, 2012 | $20,282 | $34,144"),
 ("AR-FY2013_schedule-ii.txt", "Year ended December 31, 2012(b) | 20.3 | 38.3"),
 ("AR-FY2012_notes-02-summary-of-significant-accounting-policies.txt", "Other intangible assets | 3 to 20 years"),
 ("AR-FY2012_notes-02-summary-of-significant-accounting-policies.txt", "which range from two to fifteen years."),
 ("AR-FY2013_notes-02-summary-of-significant-accounting-policies.txt", "Other intangible assets | 3 to 10 years"),
 ("AR-FY2013_notes-02-summary-of-significant-accounting-policies.txt", "which range from two to fifteen years."),
 ("AR-FY2013_notes-02-summary-of-significant-accounting-policies.txt", "Buildings | 5 to 50 years"),
 ("AR-FY2013_notes-02-summary-of-significant-accounting-policies.txt", "Capitalized internal use software | 1 to 10 years"),
 ("AR-FY2012_notes-13-restructuring.txt", "Other(2) | (0.3) | (1.0) | (0.6) | (9.9) | (11.8)"),
 ("AR-FY2012_notes-13-restructuring.txt", "Primarily consists of decreases of $10.3 million for facility closures"),
 ("AR-FY2013_notes-14-restructuring.txt", "Cash payments | (22.6) | — | (1.6) | (12.6) | (36.8)"),
 ("AR-FY2013_notes-14-restructuring.txt", "Primarily consists of decreases of $0.5 million related to a goodwill write-off"),
 ("Q3-FY2013_notes-18-subsequent-events.txt", "We currently estimate our total exposure to FSNA"),
 ("AR-FY2013_notes-11-segment-information.txt", "Impairment charges and other(10) | (44.0)"),
 ("AR-FY2013_notes-16-related-party-transactions.txt", "was $3.1 million for the executive officers."),
 ("Q3-FY2013_notes-15-related-party-transactions.txt", "was $0.6 million for the executive officers."),
 ("AR-FY2012_notes-11-segment-information.txt", "Non-cash debt charges(3) | (83.6)"),
 ("AR-FY2013_notes-11-segment-information.txt", "Debt-related charges(3) | (68.4) | (83.6)"),
 ("AR-FY2012_notes-11-segment-information.txt", "Other(9) | (44.0)"),
 ("releases/ER-Q4-FY2013.txt", "Other unusual/non-recurring (c) | (8.6)"),
 ("releases/ER-Q4-FY2013.txt", "Corporate EBITDA excludes the impact of extraordinary, unusual or non-recurring gains or losses or charges or credits."),
 ("releases/ER-Q4-FY2013.txt", "Restructuring charges | $4.5 | $2.7"),
 ("AR-FY2013_notes-11-segment-information.txt", "certain one-time charges and non-op"),
 ("AR-FY2012_notes-02-summary-of-significant-accounting-policies.txt", "gains from the dispositions of property and equipment of $6.3 million and $43.1 million"),
 ("AR-FY2013_notes-02-summary-of-significant-accounting-policies.txt", "gains from the dispositions of property and equipment of $3.9 million and $8.3 million"),
 ("Q1-FY2012_notes-06-depreciation-of-revenue-earning-equipment-and.txt", "Depreciation of revenue earning equipment | $530.4"),
 ("Q1-FY2013_notes-07-depreciation-of-revenue-earning-equipment-and.txt", "Depreciation of revenue earning equipment | $573.0 | $531.4"),
 ("AR-FY2011_notes-02-summary-of-significant-accounting-policies.txt", "concluded that there was no impairment related to our goodwill and our other intangible assets."),
 ("AR-FY2013_notes-03-goodwill-and-other-intangible-assets.txt", "therefore no impairment existed for the years ended December 31, 2013, 2012 and 2011."),
 ("Q3-FY2012_notes-04-goodwill-and-other-intangible-assets.txt", "triggered an interim impairment analysis."),
 ("AR-FY2013_notes-19-subsequent-events.txt", "approved plans to separate the Hertz car and equipment rental businesses"),
 ("Q1-FY2012_notes-06-depreciation-of-revenue-earning-equipment-and.txt", "We believe the positive trending of residual values is primarily due to continued short supply"),
 ("AR-FY2013_mdna.txt", "our U.S. monthly per vehicle depreciation costs decreased as compared to the prior year period due to mix optimization"),
 ("AR-FY2012_mdna.txt", "our monthly per vehicle depreciation costs decreased as compared to the prior year period due to improved residual values in the U.S."),
 ("AR-FY2013_notes-08-depreciation-of-revenue-earning-equipment-and.txt", "These depreciation rate changes in our U.S. car rental operations from previous quarters resulted in net decreases of $44.2 million"),
 ("Q2-FY2013_notes-07-depreciation-of-revenue-earning-equipment-and.txt", "These depreciation rate changes resulted in net decreases of $14.8 million"),
 ("Q2-FY2013_notes-07-depreciation-of-revenue-earning-equipment-and.txt", "included net losses of $17.5 million and net gains of $38.3 million"),
 ("Q1-FY2013_notes-07-depreciation-of-revenue-earning-equipment-and.txt", "included net losses of $3.3 million and net gains of $34.9 million"),
 ("Q3-FY2013_notes-07-depreciation-of-revenue-earning-equipment-and.txt", "included net losses of $11.1 million and net gains of $15.2 million"),
 ("Q3-FY2013_notes-07-depreciation-of-revenue-earning-equipment-and.txt", "resulted in net decreases of $18.0 million and $35.3 million"),
 ("AR-FY2013_notes-08-depreciation-of-revenue-earning-equipment-and.txt", "included net losses of $48.2 million, and net gains of $100.6 million"),
 ("releases/OTHER-2013-08-01-b.txt", "Auction/dealer residuals softer than expected"),
 ("AR-FY2011_mdna.txt", "We believe that cash generated from operations and cash received on the disposal of vehicles and equipment"),
 ("AR-FY2012_notes-03-goodwill-and-other-intangible-assets.txt", "determined that the respective book values of our reporting units did not exceed their estimated fair values"),
 ("Q1-FY2013_mdna.txt", "In addition, residuals remained fairly strong during the period."),

 ("Q3-FY2013_risk-factors.txt", "and are likely to incur additional losses."),
 ("AR-FY2012_critical-estimates.txt", "Beginning in 2012, we have determined that there is now sufficient historical information"),
 ("AR-FY2011_critical-estimates.txt", "Therefore, we use the calculated value method to estimate the expected volatility"),
 ("Q1-FY2013_mdna.txt", "sold approximately 75,400 and 43,000 non-program cars"),
 ("Q1-FY2012_notes-06-depreciation-of-revenue-earning-equipment-and.txt", "sold approximately 40,000 and 30,600 non-program cars"),
 ("AR-FY2013_notes-02-summary-of-significant-accounting-policies.txt", "where we consider ourselves to be the principal versus an agent"),
 ("AR-FY2013_legal.txt", "We have established reserves for matters where we believe that the losses are probable and reasonably estimated"),
 ("Q1-FY2013_mdna.txt", "Non-program cars typically have lower acquisition costs and lower depreciation rates"),
 ("releases/OTHER-2014-03-20.txt", "1% change to residuals = $83M adjusted pre-tax income"),
 ("releases/OTHER-2013-11-06.txt", "Black Book used as a benchmark"),
 ("AR-FY2013_notes-04-business-combinations-and-divestitures.txt", "On December 16, 2013, in connection with Simply Wheelz"),
 ("Q2-FY2013_notes-01-background.txt", "In May 2013, we announced plans to relocate"),
 ("AR-FY2013_notes-06-employee-retirement-benefits.txt", "The most recent Pension Protection Act Zone Status"),
 ("AR-FY2013_mdna.txt", "unknowingly not met"),
 ("AR-FY2013_notes-19-subsequent-events.txt", "approved plans to separate"),
 ("Q3-FY2012_notes-04-goodwill-and-other-intangible-assets.txt", "currently under discussion between Hertz Holdings and the United States Federal Trade Commission"),
]
bad = 0
for f, n in Q:
    try:
        print(f"{ids[f]} p.{locate_page(f, n)} | {f} | {n[:80]}")
    except ValueError:
        bad += 1
        print(f"NOT FOUND | {f} | {n[:80]}")
print("quotations checked:", len(Q), "not found:", bad)
```

**s7_ledger.py**

```python
# s7_ledger.py : writes the ledger rows once and renders them as a markdown table and as CSV (same content)
import csv, io, os
OUT = os.path.join(os.path.dirname(__file__), "out")
COLS = ["ID", "Item", "Period", "Evidence", "Locator", "Benign reading", "Adverse reading", "Context", "Resolving disclosure", "Priority", "Verdict"]
R = []
def add(*a): R.append(list(a) + [""])

add("F4-D3-01", "D3 check 2: car holding periods against depreciation per unit of gross fleet", "FY2011 to FY2013; Q1 FY2013 to Q4 FY2013",
    'Holding periods: "Cars | 4 to 26 months" (FY2011), "Cars | 4 to 28 months" (FY2012), "Cars | 4 to 36 months" (FY2013). Provision for depreciation of revenue earning equipment / average gross fleet: 16.22% FY2011, 15.28% FY2012, 14.25% FY2013 [calc]; same-quarter change FY2013 against FY2012: Q1 -2.17, Q2 -1.33, Q3 -1.07, Q4 -1.33 percentage points [calc]. FY2013 critical estimates add "Depreciation rates are adjusted prospectively through the remaining expected life." The effect of the longer holding periods is not given separately. Row triggers (a) latest value lowest in series and (b) six consecutive same-quarter declines Q3 FY2012 to Q4 FY2013 [calc].',
    "P11 p.94; P39 p.81; P68 p.91; P63 p.45; P74 p.126; P1 BS_A and BS_Q (Equipment held for rental or lease, gross)",
    "Fleet mix moved toward non-program cars, which the company says have lower depreciation rates (P225 p.35), and Dollar Thrifty cars entered at fair value (E9); longer holding periods for risk cars lower monthly depreciation by design; the aggregate effect of 2013 rate changes is disclosed (U.S. -44.2m, international +5.0m) [P74 p.126].",
    "Holding periods were lengthened and rates lowered in the year car disposals moved from gains to losses (F4-D3-06), which lowers current depreciation and can push cost into later disposal losses; the part due to holding periods is not quantified [inf: P68, P74, P62].",
    "E22 depreciation-rate changes; E24 revision (FY2013 and derived Q4 FY2013 on revised basis; on the revised basis the annual series is 16.14%, 15.17%, 14.27% and Q4 FY2013 with the 9M correction added back is 13.17% [calc]); E9",
    "Split of the 2013 rate effect between holding periods and residual assumptions; average holding period by year; car-only gross cost and depreciation. Not found [P74, P63, P62, P77 searched 'holding period', 'average age', 'months'].",
    "P1")
add("F4-D3-02", "D3 check 2: finite-lived intangible lives stated two ways in the same note", "FY2012, FY2013",
    'FY2012 note 2: "Other intangible assets | 3 to 20 years" and "...which range from two to fifteen years." FY2013 note 2: "Other intangible assets | 3 to 10 years" and "...which range from two to fifteen years."',
    "P39 p.81 and p.83; P68 p.91 and p.93",
    "The useful-life table line may cover a narrower class than all finite-lived intangibles, or one of the two statements was not updated when the other was [inf: P39, P68].",
    "Two stated lives for the same asset class disagree; if amortization follows the longer range, expense is lower than the shorter range implies [inf: P39, P68].",
    "E9 and E21 (Dollar Thrifty intangibles 1,545)",
    "Lives by intangible class. Not found [P69 searched 'years', 'life', 'useful'].",
    "P1")
add("F4-D3-03", "D3 check 3: explanation of lower depreciation, Q1 2013", "Q1 FY2013",
    'MD&A: "The decrease as a percent of revenues was driven primarily by an increase in residual values and corresponding lower depreciation rates in the first quarter of 2013 compared to the first quarter of 2012." and "In addition, residuals remained fairly strong during the period." Same filing, note 7: vehicle disposals "included net losses of $3.3 million and net gains of $34.9 million" (Q1 2013, Q1 2012); per non-program car sold -44 against +812 USD [calc]; rate changes in the quarter were a decrease of $0.7m.',
    "P225 p.42 and p.35; P213 p.13",
    "Residual values in the sentence may mean expected values at future disposal or an index level, not realized proceeds; sales volume rose to 75,400 from 43,000 cars and included Dollar Thrifty cars recorded at fair value [P225 p.35; E9].",
    "The explanation credits higher residual values for lower depreciation while the same filing shows realized disposal results moving from gains to losses [inf: P225, P213].",
    "E9; E22; E24 (Q1 2013 revised: depreciation and lease charges 587.0 to 580.1 [P68 p.85])",
    "Realized proceeds per car and the residual index used. Not found [P225, P213, P287, P288].",
    "P1")
add("F4-D3-04", "D3 check 3: explanation of lower depreciation, Q2 2013", "Q2 FY2013",
    'MD&A: "In the six months ended June 30, 2013, our monthly per vehicle depreciation costs decreased as compared to the prior year period due to improved residual values in the U.S., ..." and "In addition, residuals have remained relatively strong during the period." Note 7: rate changes "resulted in net decreases of $14.8 million" in the quarter; disposals "included net losses of $17.5 million and net gains of $38.3 million"; per car -250 against +857 USD [calc]. Call slides: "Auction/dealer residuals softer than expected".',
    "P246 p.38 and p.46; P234 p.13 and p.14; P292 p.11",
    "The statement compares six months with six months; the slides say retail residuals stayed strong while auction residuals softened, so rates may rest on a retail-heavy disposal plan [P292 p.11].",
    "Depreciation rates were lowered on higher expected residuals in a quarter when realized sales produced losses and management's own slides describe softer auction residuals [inf: P234, P246, P292].",
    "E22; E24 (Q2 2013 revised: 641.1 to 627.5 [P68 p.85]); E14",
    "Residual assumptions by channel behind the Q2 rate change. Not found [P234, P246, P289, P292].",
    "P1")
add("F4-D3-05", "D3 check 3: explanation of lower depreciation, Q3 2013", "Q3 FY2013",
    'MD&A: "In the nine months ended September 30, 2013, our monthly per vehicle depreciation costs decreased as compared to the prior year period due to residual values that remained strong in the U.S., ..." Note 7: U.S. rate changes "resulted in net decreases of $18.0 million and $35.3 million" (three and nine months); U.S. disposals "included net losses of $11.1 million and net gains of $15.2 million"; per U.S. car -275 against +578 USD [calc].',
    "P266 p.41 and p.50; P254 p.14",
    "Rate reductions reflect channel diversification and retail expansion, which the note names as drivers [P254 p.14].",
    "The same filing attributes higher depreciation as a share of revenue to losses on vehicle sales (P266 p.50) while crediting strong residual values for lower per-vehicle depreciation [inf: P266, P254].",
    "E22; E24 (Q3 2013 revised: 676.7 to 674.9 [P68 p.87])",
    "As F4-D3-04. Not found [P254, P266, P293, P294].",
    "P1")
add("F4-D3-06", "D3 check 3: residual values described both ways, FY2013", "FY2013",
    'MD&A U.S. segment: "The increase was primarily attributable to an increase in average fleet due to the Recent Acquisitions and a deterioration in the used vehicle residual values." Same document and note 8: U.S. rate changes "resulted in net decreases of $44.2 million" and "The cumulative effect of the reduction in rates was also indicative of the residual values experienced in the U.S. ..." Note 8: disposal loss "primarily due to a combination of declining residual values from falling demand for used vehicles and timing of sales". U.S. per car -244 against +738 USD [calc]; U.S. disposal swing -148.8m [calc]. FY2012 note 8 said "indicative of the strong residual values" (word "strong" not in FY2013). International: rate changes increased depreciation by 5.0m while MD&A cites "slight strengthening of used vehicle residual values".',
    "P62 p.54, p.42, p.43; P74 p.126; P45 p.113",
    "Rate reductions are prospective and were set in earlier quarters (9M -35.3m, derived Q4 -8.9m [calc]); the note also credits channel diversification, retail expansion and longer holding periods, which are not residual-value effects [P74 p.126].",
    "One document says residual values deteriorated (raising segment depreciation) and that rate reductions reflect residual values experienced; lower rates in a year of disposal losses can defer cost [inf: P62, P74].",
    "E22; E24; E9",
    "Residual assumption by quarter and reconciliation of rate changes to realized proceeds. Not found [P74, P62, P63, P295, P296].",
    "P1")
add("F4-D3-07", "D3 check 7: recurring charges under a non-recurring or one-time label", "Q4 2010 to Q4 2013; FY2009 to FY2013",
    'Releases: "Corporate EBITDA excludes the impact of extraordinary, unusual or non-recurring gains or losses or charges or credits." The table of those items is non-zero in 13 of 13 quarterly releases and includes restructuring charges in 8 of the last 8 [calc]; restructuring charges recorded in 5 of 5 fiscal years FY2009 to FY2013 (106.8, 54.7, 56.4, 38.0, 77.0) [calc count]. 10-K: adjusted pre-tax income adds back "certain one-time charges and non-operational items", including restructuring every year. FY2012 "Other(9) | (44.0)" is shown as "Other unusual/non-recurring" in the Q4 2013 release.',
    "P295 p.3 and p.9; P77 p.131 and p.134; P48 p.120; P21 p.138; P50 p.125; P80 p.140",
    "The Corporate EBITDA label follows the credit agreement definition; restructuring is disclosed as an ongoing programme, so a reader can see it recurs [P295 p.3; P80 p.140].",
    "Charges that recur every year are presented under a non-recurring or one-time label, which can make recurring costs look exceptional [inf: P295, P77, P80].",
    "E9, E10 (acquisition and divestiture costs in 2012 and 2013)",
    "Whether any filed measure (10-K, 10-Q) carries the non-recurring label: searched P5, P33, P62 and the nine 10-Q mdna files; only 'one-time' found. Whether Item 10(e)(1)(ii)(B) reaches the furnished releases is for the analyst.",
    "P1")
add("F4-D2-01", "D2 fleet-cost risk factor reworded; expectation dropped", "FY2013",
    'Before: "Declines in the value of the non-program cars in our fleet and declines in the overall number of program cars in our fleet could materially adversely impact our financial condition, results of operations, liquidity and cash flows." After: "Increased fleet costs, either generally or due to declines in the value of the non-program cars in our fleet, could materially adversely impact our financial condition, results of operations, liquidity and cash flows." Dropped: "We expect this percentage to continue to decrease in the future, particularly as we integrate the operations of Dollar Thrifty, ..."',
    "P31 p.22; P60 p.23",
    "Program-car share was 30% of purchases in both 2012 and 2013 [P60 p.23], so the expectation of further decline no longer applied; the heading was broadened.",
    "The heading now leads with increased fleet costs in the year disposal results turned to losses (F4-D3-03 to F4-D3-06) [inf: P60, P74].",
    "E9",
    "Residual assumptions and program share by quarter. Not found [P60, P62].",
    "P2")
add("F4-D2-02", "D2 statement on car supply arrangements removed", "FY2013",
    'FY2012: "We are not a party to any long-term car supply arrangements with manufacturers." Not in FY2013 [not found: P60, P59 searched "car supply", "supply arrangement"].',
    "P31 p.22; P60 p.23",
    "Editorial shortening of an unchanged risk [inf: P31, P60].",
    "A long-term supply arrangement may now exist whose terms are not described [inf: P31, P60].",
    "none",
    "Supply terms in Item 1. Not found [P59].",
    "P3")
add("F4-D2-03", "D2 multiemployer pension risk hardened, then softened", "FY2012, FY2013",
    'FY2011: "At least one multiemployer plan in which we participate is reported to have, and other of our multiemployer plans could have, significant underfunded liabilities." FY2012: "Several of our remaining multiemployer plans have underfunded liabilities." FY2013: "Our multiemployer plans could have significant underfunded liabilities."',
    "P3 p.31; P31 p.25; P60 p.26",
    "After the December 2012 withdrawal (cost 23.2m, P295 p.2 note (c)) the remaining plans may be better funded.",
    "A statement of fact became a possibility without a disclosed change in funding [inf: P31, P60].",
    "none",
    "Plan funding zones: zone table in note 6 (P72 p.121); zones not tabulated in this step.",
    "P3")
add("F4-D2-04", "D2 new risk: key employees and headquarters relocation", "FY2013",
    '"In addition, our key employees may be distracted by activities unrelated to our business, including the relocation of our corporate headquarters from Park Ridge, New Jersey to Estero, Florida."',
    "P60 p.26",
    "Relocation announced May 2013 [P228 p.8]; the risk describes a known event.",
    "Finance and management disruption in the year of the E24 errors, the E19 system change and the E20 CFO change [inf: P60, P68, P87].",
    "E19, E20",
    "Status of finance staff relocation. Not found [P60, P62, P87].",
    "P3")
add("F4-D2-05", "D2 new risk: losses from FSNA and Simply Wheelz; likelihood softened between Q3 and FY2013", "Q3 FY2013, FY2013",
    'Q3 2013 10-Q: "We have recognized losses as a result of our relationship with FSNA and Simply Wheelz and are likely to incur additional losses." FY2013: "We have recognized losses as a result of our relationship with Franchise Services of North America, or "FSNA," and Simply Wheelz and may incur additional losses."',
    "P267 p.76; P60 p.24",
    "The 16 December 2013 settlement fixed payments and the return of vehicles, which may have lowered the likelihood of further loss [P70 p.101].",
    "Likely became may with no amount given for the remaining exposure named in Q3 (see F4-C6-02) [inf: P267, P60, P265].",
    "E10",
    "Remaining FSNA exposure at 31 December 2013. Not found [P70, P77, P85].",
    "P3")
add("F4-D2-06", "D2 like-kind exchange risk adds fleet net book value as a trigger", "FY2012",
    'Before: "A material and extended reduction in vehicle purchases or a downsizing of our car rental fleet, for any reason, ..." After: "A material reduction in the net book value of our car rental fleet, a material and extended reduction in vehicle purchases and/or a material downsizing of our car rental fleet, for any reason, ..."',
    "P3 p.27; P31 p.22",
    "Clarifies the mechanism and adds Dollar Thrifty's own programme (E9).",
    "Links fleet book value, and so depreciation choices, to the timing of material tax payments [inf: P31].",
    "E9",
    "Deferred tax attributable to the programme. Not reviewed in this step (P75).",
    "P3")
add("F4-C10-01", "C10 Sobel concession-fee case: stated potential judgment, no accrual stated", "FY2013 (first in Q1 FY2013)",
    'FY2012: "The court has since entered a stay order and the parties will again be engaging in mediation." FY2013: "A judgment - which could potentially exceed $40.0 million - has still not been issued by the court." and "We continue to believe the outcome of this case will not be material to our financial condition, results of operations or cash flows." Q1 2013 said the findings "will be reversed"; that sentence is not in FY2013 [not found: P61, P79]. 40.0 is 6.03% of FY2013 pre-tax income [calc].',
    "P32 p.32; P61 p.137; P222 p.29",
    "An interlocutory appeal and mediation are pending; the general statement on unaccrued matters may cover this case [P61 p.137-138].",
    "Partial summary judgment on restitution and class certification went against the company and a potential judgment above $40.0m is stated, but no accrual, likelihood term or range is given for the matter [inf: P61].",
    "none",
    "ASC 450-20 accrual or reasonably possible range for this matter. Not found [P61, P79, P243, P263 searched 'probable', 'reasonably possible', 'accru' near Sobel].",
    "P3")
add("F4-C10-02", "C10 new securities class action", "FY2013",
    '"On November 20, 2013, a purported shareholder class action, Pedro Ramirez, Jr. v. Hertz Global Holdings, Inc., et al., was commenced ..." alleging misstatements "during the period from February 25, 2013 through November 4, 2013".',
    "P61 p.138",
    "Newly filed; no estimate is usually possible at this stage.",
    "The class period covers the quarters later revised under E24 [inf: P61, P68].",
    "E24",
    "Statement on estimate of loss. Not found [P61, P79].",
    "P3")
add("F4-C10-03", "C10 accruals appear for three class actions", "FY2012",
    'FY2011: "All proceedings in the case are currently stayed while the parties engage in settlement discussions." FY2012: "... have accrued our best estimate of the ultimate cost which is not material to our financial condition." Q4 2013 release: 2012 adjustments include a "litigation accrual of $14.0 million".',
    "P4 p.40; P32 p.32; P295 p.2",
    "Settlements reached in 2012 and 2013 [P61 p.136-138].",
    "Matters each called not material add up to an amount the company excludes from adjusted results [inf: P32, P295].",
    "none",
    "Accrual by matter. Not found [P32, P49].",
    "P3")
add("F4-C10-04", "C10 SEC investigation closed", "FY2012",
    'FY2011: "We intend to cooperate fully with the SEC\'s investigation." FY2012: "On February 14, 2013, we were informed by the staff that the investigation has been completed and that no action was taken by the staff or the SEC."',
    "P4 p.38; P32 p.32",
    "Resolution with no action.",
    "None beyond the fact of the prior investigation [inf: P32].",
    "none",
    "In pack.",
    "P3")
add("F4-C14-01", "C14 auditor report unchanged; no paragraph on the revision", "FY2013",
    'Unqualified opinions; FY2013 names "Internal Control—Integrated Framework 1992"; the Dollar Thrifty scope exclusion ends; no explanatory paragraph on the E24 revision [not found: P65 "revis", "error"].',
    "P65 p.74; P36 p.71",
    "The company judged the errors immaterial to prior periods [P68 p.83], a case in which no explanatory paragraph is expected [inf].",
    "None beyond F1-C15-1.",
    "E24",
    "In pack (P65).",
    "P4")
add("F4-C13-01", "C13 depreciation estimate wording changed; no sensitivity in the 10-K", "FY2013",
    'Before: "These key factors are considered when estimating future residual values and assessing depreciation rates." and "... we use historical experience and monitor market conditions to set depreciation rates." After: "These key factors are considered when estimating future residual values. Depreciation rates are adjusted prospectively through the remaining expected life." and "... we use historical experience, as well as industry residual value guidebooks, and the monitoring of market conditions, to set depreciation rates." No change amount or sensitivity in any year\'s critical estimates [not found: P6, P34, P63]; the Q4 2013 slides give one: "1% change to residuals = $83M adjusted pre-tax income".',
    "P34 p.44; P63 p.45; P296 p.21",
    "Clarifies existing practice; guidebooks are a benchmark the slides also cite [P294 p.10].",
    "A new outside input to residual estimates appears in the year estimated residuals rose while realized residuals fell; the sensitivity exists but is not in the filing [inf: P63, P296, P74].",
    "E22",
    "Quantified effect of the guidebook input. Not found [P63, P74].",
    "P2")
add("F4-C13-02", "C13 stock-option volatility estimate method changed", "FY2012",
    'FY2011: "Therefore, we use the calculated value method to estimate the expected volatility, ..." FY2012: "Beginning in 2012, we have determined that there is now sufficient historical information available to estimate the expected volatility of our stock price."',
    "P6 p.56; P34 p.47",
    "Stated reason: enough trading history after 2006 listing.",
    "Change in an estimate input with no stated effect on expense [inf: P34].",
    "none",
    "Effect on 2012 option expense. Not found [P44].",
    "P3")
add("F4-A8-01", "A8 gains on sales of operations to franchisees kept in operating income", "FY2012 (new policy text)",
    '"Such gains or losses are included in operating income because they are expected to be a recurring part of our business."',
    "P39 p.84",
    "Policy disclosure added alongside franchise revenue recognition.",
    "Gains on disposals of operations sit in operating results; amounts not disclosed [not found: P39, P68 searched 'franchisee' with 'gain'].",
    "E3, E16 (franchise reacquisitions)",
    "Amount of such gains by year. Not found.",
    "P3")
add("F4-A8-02", "A8 revenue lines reclassified and relabelled", "Q2 FY2013 onward",
    "Other revenue reclassified in Q2 2013 and relabelled with the Q3 2013 segment recast; FY2012 car rental 7,456.1 to 7,161.7 [context sheet E17, E18].",
    "P227 p.3; P247 p.3; P66 p.76",
    "Presentation change with total revenue unchanged apart from E24.",
    "Line-level trends before and after Q2 2013 are not comparable [inf: P1, P227].",
    "E17, E18",
    "Reason for the Q2 2013 reclassification beyond the generic sentence. Not found [P229].",
    "P4")
add("F4-A4-01", "A4 receivable concentration statement dropped", "FY2012, FY2013",
    'FY2011: "Concentrations of credit risk with respect to trade receivables are limited due to the large number of customers ..." and "As of December 31, 2011, we had no significant concentration of credit risk." From FY2012 the concentration paragraph covers cash and derivatives only [P68 p.90].',
    "P22 p.139; P39 p.80; P68 p.90",
    "Moved into the policy note and shortened.",
    "Dropped in the period one counterparty, Simply Wheelz, subleased about 20,000 vehicles and later owed amounts in an estimated 50 to 70m exposure [inf: P60 p.24, P265 p.37].",
    "E10",
    "Receivables by counterparty. Not found.",
    "P3")
add("F4-A4-02", "A4 2012 allowance for doubtful accounts revised", "FY2012 as reprinted",
    'FY2012 Schedule II: "Year ended December 31, 2012 | $20,282 | $34,144 | ..." (thousands). FY2013: "Year ended December 31, 2012(b) | 20.3 | 38.3 | ..." (millions); charged to expense +4.16m [calc].',
    "P56 p.140; P86 p.158",
    "Brazil allowance correction in E24.",
    "None beyond E24.",
    "E24",
    "In pack (P68 pp.83-89).",
    "P4")
add("F4-C7-01", "C7 other useful-life ranges changed without comment", "FY2013",
    'FY2012: "Buildings | 3 to 50 years", "Capitalized internal use software | 1 to 15 years". FY2013: "Buildings | 5 to 50 years", "Capitalized internal use software | 1 to 10 years". No statement that lives changed [not found: P68 "change in estimate", "useful li"].',
    "P39 p.81; P68 p.91",
    "Table updated to reflect assets held; the software change shortens lives.",
    "An unexplained change in stated lives; effect not given [inf: P68].",
    "none",
    "Effect of any change in lives. Not found.",
    "P3")
add("F4-C6-01", "C6 2012 restructuring rollforward re-described", "FY2012 as reprinted in FY2013",
    'FY2012 10-K, 2012: "Other(2) | (0.3) | (1.0) | (0.6) | (9.9) | (11.8)", footnote "Primarily consists of decreases of $10.3 million for facility closures and $1.0 million in ASC 715 pension adjustment." FY2013 10-K, 2012: "Cash payments | (22.6) | — | (1.6) | (12.6) | (36.8)", Other (1.8), footnote "Primarily consists of decreases of $0.5 million related to a goodwill write-off on a sale of business ...". Cash payments larger by 10.0 and Other smaller by 10.0 [calc]; closing balance 21.0 both years.',
    "P50 p.126; P80 p.141",
    "Facility-closure payments reclassified from Other to cash payments.",
    "A 2012 non-cash reduction of the reserve is now described as cash paid, with no revision note [inf: P50, P80].",
    "none (E24 does not list it)",
    "Explanation. Not found [P80, P68].",
    "P3")
add("F4-C6-02", "C6 Simply Wheelz loss below the range estimated in Q3 2013", "Q3 FY2013 to FY2013",
    'Q3 2013: "We currently estimate our total exposure to FSNA\'s liquidity issues to be between $50 and $70 million." FY2013: "Impairment charges and other(10) | (44.0)", footnote "Related to FSNA and its subsidiary, Simply Wheelz." 44.0 is 6.0 below the low end [calc]; the FY2013 filing does not restate the range [not found: P70, P85, P62].',
    "P265 p.37; P77 p.134",
    "The 16 December 2013 settlement gave orderly return of vehicles and may have reduced the exposure [P70 p.101].",
    "Part of the 6 to 26m remaining exposure named in Q3 may sit in other lines or be unrecognized [inf: P265, P77].",
    "E10",
    "FSNA-related charges by line for 2013. Not found.",
    "P3")
add("F4-C6-03", "C6 public liability and property damage reserve basis reworded", "FY2012, FY2013",
    'FY2011: "Reserve requirements are based on actuarial evaluations ..." FY2012: "Reserve requirements are based on rental volume and actuarial evaluations ..." FY2013: "The increase in public liability and property damage reserves was primarily related to Dollar Thrifty." (liability 332.2 to 347.7, +15.5 [calc]); "Our actual results as compared to our estimates have historically resulted in relatively minor adjustments to our recorded liability."',
    "P6 p.53; P34 p.45; P61 p.138; P63 p.45",
    "Rental volume was an existing input now named; Dollar Thrifty added exposure (E9).",
    "A change in reserve basis can move the reserve without a change in claims experience; no prior-year development is given to test the 'minor adjustments' sentence [inf: P34, P63].",
    "E9",
    "Rollforward with prior-year development. Not found [P86 holds allowance and tax valuation only; P61; P79].",
    "P3")
add("F4-D4-01", "D4 company purchases of executives' homes (relocation)", "FY2013",
    '"The total amount that we spent under the program during the year ended December 31, 2013 was $3.1 million for the executive officers." Q3 2013: $0.6m for nine months; Q4 derived 2.5m [calc]. New paragraph on transactions with companies where directors serve.',
    "P82 p.147; P262 p.34",
    "Standard relocation programme approved by the Compensation Committee, prices from averaged appraisals [P82 p.147].",
    "Company-funded purchases of executives' homes concentrated in Q4; resale results not disclosed [inf: P82, P262].",
    "E20; relocation announced May 2013 [P228 p.8]",
    "Resale outcomes and executives covered. Not found.",
    "P3")
add("F4-C2-01", "C2 non-GAAP labels and categories changed", "FY2013",
    'FY2012 10-K: "Non-cash debt charges(3) | (83.6)" and "Other(9) | (44.0)". FY2013 10-K: "Debt-related charges(3) | (68.4) | (83.6)"; Q4 2013 release shows the FY2012 44.0 as "Other unusual/non-recurring". New 2013 lines: Integration expenses, Relocation costs, Impairment charges and other.',
    "P48 p.120; P77 p.134; P295 p.9",
    "Footnote (3) describes the same items; new lines reflect new 2013 events and prior years show dashes [P77 p.134].",
    "The non-cash qualifier was dropped and prior-year items relabelled non-recurring after the fact (see F4-D3-07) [inf: P48, P77, P295].",
    "E9, E10, E13",
    "In pack.",
    "P3")
add("F4-C2-02", "C2 operating metric definitions changed", "Q1 FY2012; Q1 to Q2 FY2013",
    "Equipment pricing metric moved to the American Rental Association method; total RPD introduced, corrected for Q2 2013 and redefined to exclude sublease revenue [context sheet E8, E14].",
    "P166 p.39; P287 pp.1, 3; P290 p.1; P291 p.1",
    "Definition changes disclosed at the time.",
    "Trend comparisons across the change may not be like for like [inf: P291].",
    "E8, E14",
    "Recast prior periods. Not found [P291, P293].",
    "P4")
add("F4-C16-01", "C16 comparative figures changed without line-level explanation", "FY2012; Q1 FY2012",
    '2012 gains on disposal of property and equipment: FY2012 note "$6.3 million" "included in "Direct operating""; FY2013 note "$8.3 million" "included in our consolidated statements of operations" (+2.0 [calc]). Q1 2012 depreciation of revenue earning equipment 530.4 in the Q1 2012 10-Q, 531.4 in the Q1 2013 10-Q (+1.0 [calc]), a change reported before the E24 errors were identified in Q4 2013 [inf: P213, P68]. Q1 2012 non-program cars sold: "approximately 40,000" in the Q1 2012 10-Q, "75,400 and 43,000" (2013, 2012) in the Q1 2013 10-Q (+3,000 [calc]).',
    "P39 p.81; P68 p.91; P154 p.11 and p.12; P213 p.13; P225 p.35",
    "Small reclassifications to conform presentation.",
    "Comparatives changed with no stated reason [inf: P68, P213].",
    "E24 (partly)",
    "Line reconciliation. Not found [P68 pp.83-89; P208].",
    "P3")
add("F4-C16-02", "C16 revision disclosures found by search", "FY2010 to Q3 FY2013",
    "Hits: Q1 and Q2 2011 cash flow revisions for 2010 (P91 p.7, P111 p.7); Q3 2011 and FY2011 revision of FY2008 to FY2010 (P131 p.7, P11 p.92); FY2012 parent-only cash flow correction (P37 p.138); Q2 and Q3 2013 revolver gross-up (P229 p.8, P249 p.8); FY2013 correction of errors (P68 pp.83 to 89).",
    "P91; P111; P131; P11; P37; P229; P249; P68",
    "All on the context sheet.",
    "Repeated corrections across three years, carried at F1 [inf: F1 ledger].",
    "E1, E4, E12, E17, E24",
    "In pack.",
    "P4")

def md():
    lines = ["| " + " | ".join(COLS) + " |", "|" + "---|" * len(COLS)]
    for r in R:
        lines.append("| " + " | ".join(c.replace("|", "\\|") for c in r) + " |")
    return "\n".join(lines)
def csvtxt():
    b = io.StringIO(); w = csv.writer(b, lineterminator="\n"); w.writerow(COLS); w.writerows(R); return b.getvalue()
open(os.path.join(OUT, "ledger.md"), "w", encoding="utf-8").write(md())
open(os.path.join(OUT, "ledger-F4.csv"), "w", encoding="utf-8").write(csvtxt())
from collections import Counter
print(len(R), Counter(r[9] for r in R))
```

**s8_assemble.py**

```python
# s8_assemble.py : assembles the output file, counts figures for the verification line, checks banned words
import os, re, shutil
HERE = os.path.dirname(__file__); OUT = os.path.join(HERE, "out")
DEST = r"C:\Users\aaron\OneDrive\Desktop\Master\WireSift Research\Events\CFA Vancouver Forensic\tests\hertz-fy2013\runs\v0.2-claude-code"
body = open(os.path.join(HERE, "body.md"), encoding="utf-8").read()
smap = open(os.path.join(OUT, "sectionmap.md"), encoding="utf-8").read()
lmd = open(os.path.join(OUT, "ledger.md"), encoding="utf-8").read()
lcsv = open(os.path.join(OUT, "ledger-F4.csv"), encoding="utf-8").read().rstrip("\n")
code_files = ["f4lib.py", "s1_sectionmap.py", "s2_dump.py", "s3_search.py", "adhoc.py", "s4_checks.py",
              "s5_map.py", "s6_locators.py", "s7_ledger.py", "s8_assemble.py"]
code = "\n\n".join(f"**{f}**\n\n```python\n{open(os.path.join(HERE, f), encoding='utf-8').read().rstrip()}\n```" for f in code_files)
code += ("\n\n**Run order:** s1_sectionmap.py (twice: before and after the typographic normalisation added to f4lib.py), "
         "s2_dump.py per section group (risk factors, legal, market risk, auditor, critical estimates, controls, notes 02, "
         "Schedule II, restructuring, related parties, goodwill, subsequent events), s3_search.py, adhoc.py blocks 1 to 5, "
         "s4_checks.py, s5_map.py, s6_locators.py (95 quotations checked, 0 not found), adhoc.py blocks 6 and 7, "
         "s7_ledger.py, s8_assemble.py.")

# figure counts: calculated = numbers in the section map count cells + [calc] figures in body and ledger;
# copied = numbers inside quotation marks in body and ledger (page numbers and P ids excluded)
num = re.compile(r"(?<![\w.])-?\d[\d,]*\.?\d*")
calc_map = 0
for line in smap.splitlines()[2:]:
    cells = [c.strip() for c in line.strip("|").split("|")]
    calc_map += sum(1 for c in cells[2:5] if re.fullmatch(r"\d+", c))
    calc_map += len(re.findall(r"(\d+) (?:changed|=|near)", cells[5])) if len(cells) > 5 else 0
text = body + "\n" + lmd
calc_marked = 0
for seg in re.findall(r"[^\[\n]*\[calc[^\]]*\]", text):
    calc_marked += len(num.findall(re.sub(r"P\d+|p\.\s?\d+|FY\d{4}|Q\d", "", seg)))
copied = 0
for q in re.findall(r"\"([^\"]{3,})\"", text):
    copied += len(num.findall(re.sub(r"P\d+|p\.\s?\d+", "", q)))
verif = (f"Verification: 25 items run, 33 ledger rows (P1 7, P2 2, P3 19, P4 5), 1 could not run. "
         f"Figures: {copied} copied, {calc_map + calc_marked} calculated, 0 unverified. Units: USD, millions "
         f"(FY2011 and FY2012 10-K and Q1 2011 to Q1 2013 10-Q quotations in thousands where shown). "
         f"Framework: US GAAP. Context sheet: used.")
full = (body.replace("{{SECTIONMAP}}", smap).replace("{{LEDGER_MD}}", lmd).replace("{{LEDGER_CSV}}", lcsv)
        .replace("{{CODE}}", code).replace("Verification: 25 items run, 33 ledger rows (P1 7, P2 2, P3 19, P4 5), 1 could not run. Figures: 170 copied, 1175 calculated, 0 unverified. Units: USD, millions (FY2011 and FY2012 10-K and Q1 2011 to Q1 2013 10-Q quotations in thousands where shown). Framework: US GAAP. Context sheet: used.", verif))
# banned words outside quotations
unq = re.sub(r"\"[^\"]*\"", "", full)
for w in [x[::-1] for x in ["duarf", "talupinam", "evisserga", "galf der", "suoicipsus", "gninrecnoc"]]:  # rule 1 word list, reversed so it is not printed
    hits = [m.start() for m in re.finditer(w, unq, re.I)]
    print("rule-1 word", w[::-1], len(hits))
print("em-dash outside quotes:", unq.count("\u2014"))
open(os.path.join(DEST, "F4-output.md"), "w", encoding="utf-8").write(full)
shutil.copy(os.path.join(OUT, "ledger-F4.csv"), os.path.join(DEST, "ledger-F4.csv"))
print(verif)
print("chars", len(full), "words", len(full.split()), "lines", full.count("\n"))
```

**Run order:** s1_sectionmap.py (twice: before and after the typographic normalisation added to f4lib.py), s2_dump.py per section group (risk factors, legal, market risk, auditor, critical estimates, controls, notes 02, Schedule II, restructuring, related parties, goodwill, subsequent events), s3_search.py, adhoc.py blocks 1 to 5, s4_checks.py, s5_map.py, s6_locators.py (95 quotations checked, 0 not found), adhoc.py blocks 6 and 7, s7_ledger.py, s8_assemble.py.

Verification: 25 items run, 33 ledger rows (P1 7, P2 2, P3 19, P4 5), 1 could not run. Figures: 170 copied, 1175 calculated, 0 unverified. Units: USD, millions (FY2011 and FY2012 10-K and Q1 2011 to Q1 2013 10-Q quotations in thousands where shown). Framework: US GAAP. Context sheet: used.

**Candidates for review, not findings.**
