# Context sheet: Hertz Global Holdings, Inc., FY2009 to Q4 2013

```
Step:        F1, Context and comparability
Company:     Hertz Global Holdings, Inc. (SEC CIK 1364479), NYSE: HTZ [P0, header table]
Framework:   US GAAP [P0, header table; P68, p. 83; P65, p. 74]
Currency:    USD [P0, header table]
Units:       P1 statements.xlsx in USD millions; text files in each filing's own units
             (thousands: FY2011 and FY2012 10-Ks, 10-Qs Q1 2011 to Q1 2013; millions: FY2013 10-K,
             Q2 and Q3 2013 10-Qs, earnings-release tables) [P0, header table]
Fiscal year: ends 31 December [P0, header table]
Periods:     quarters Q1 2011 to Q4 2013; years FY2009 to FY2013 [P0, header table]
As of:       31 March 2014; nothing filed later is in the pack [P0, header table]
```

## Read first: breaks the later steps must carry

1. **P1 holds every period as originally reported, but the company revised FY2011, FY2012, all four 2012 quarters and Q1 to Q3 2013 in the FY2013 10-K** [P0, "How statements.xlsx is made"; P68, pp. 83 to 89]. FY2013 in P1 sits on the corrected basis, Q4 2013 is mixed (item 2), and every earlier period in P1 sits on the pre-revision basis [inf: P0, P68]. Any FY2013 versus FY2012 comparison taken straight from P1 mixes the two bases [inf: P1, P68]. See E24.
2. **Q4 FY2013 in P1 is derived as the FY2013 10-K year (corrected) minus the Q3 2013 10-Q nine months (uncorrected)**, so it absorbs the nine-month corrections: revenue USD -5.0m and pre-tax income USD -11.6m against the company's own revised Q4 2013 [calc, C4; P84, p. 149; P68, p. 87].
3. **Cash tie-out fails in FY2013 and Q4 FY2013 by USD 12.2m** because the FY2013 10-K cash flow statement starts from FY2012 cash as revised (545.5) while P1's FY2012 balance is the original 533.3 [calc, C1; P1, RESTATED]. The difference is fully explained by the revision; recomputed from the revised opening balance it is 0.0 [calc, C1].
4. **FY2009 and FY2010 in P1 predate a second revision** (identified Q3 2011) that changed FY2009 and FY2010 net income, goodwill, fleet assets, payables and deferred taxes [P131, p. 7; P11, p. 92]. P1's RESTATED sheet captures the FY2010 reprint but not FY2009 [P1, RESTATED], and it compares only the next year's 10-K, so FY2011 as reprinted in the FY2013 10-K is not in it [P0, "How statements.xlsx is made"]. Both are computed below from the text [calc, C3, C6].
5. **Revenue by business line is not on one basis across the workbook**: the "Other" revenue line was reclassified in the Q2 2013 10-Q and relabelled with the segment recast from the Q3 2013 10-Q [P227, p. 3; P247, p. 3; P1, EXTRA]. Total revenue is unaffected apart from the revision [calc, C7].
6. **Pack errors in the EXTRA sheet** (the one main-sheet gap, CF_Q Stock repurchased Q1 FY2013, is tie-out warning W2): Common Stock value left in thousands for Q2 2011 to Q1 2013, FY2011 and FY2012; Treasury Stock Q1 FY2013 left in thousands (-467248); the derived Q2 FY2013 "Purchase of treasury shares" (466780.8) inherits that error; FY2013 "Proceeds under the revolving lines of credit" carries the wrong sign (-9511.6 against 9,511.6 in the filing) [calc, C12, C15; P66, p. 81; P9, p. 150].
7. **Workbook "Net income" is consolidated net income including the noncontrolling interest** for FY2009 to Q4 2011 (for example FY2011 195.7 against 176.2 attributable to common stockholders) [P1, IS_A and EXTRA, FY2011]. EPS work must use the attributable line.
8. No mismatch was found between the manifest and the filings on framework, currency, units or fiscal year end [calc, unit headers checked in P9, P37, P66, P89, P206, P227, P247; P68, p. 83].

## 1. Basis

| Item | Finding | Mark |
|---|---|---|
| Framework | US GAAP. Note 2 of the FY2013 10-K: "The preparation of financial statements in conformity with accounting principles generally accepted in the United States of America, or GAAP, requires management to make estimates and assumptions..." (quotation marks around "GAAP" in the filing are rendered as unreadable characters in the text file). All three audit opinions refer to "accounting principles generally accepted in the United States of America". | [P68, p. 83; P8, p. 84; P36, p. 71; P65, p. 74] |
| Listing and filer status | Delaware company, NYSE-listed SEC registrant; NI 52-107 and Canadian rules do not apply | [P0, header table; P299, E9 8-K text] |
| IFRS-only items (function or nature, revaluation model) | Not applicable (US GAAP). For reference the manifest records neither a by-function nor a by-nature format, and cost-model PP&E | [P0, header table] |
| Currency | USD | [P0, header table] |
| Units | P1 in USD millions. Statement headers read "(In Thousands of Dollars...)" in P9, P37, P89 and P206, and "(In Millions of Dollars...)" in P66, P227 and P247, as the manifest states | [calc, unit-header check; P0] |
| Fiscal year end | 31 December in every filing; no change of fiscal year end and no 52/53-week calendar found | [P0; search: "change in fiscal year", "53-week", "53 week", "fifty-three", "extra week" 0 hits in P2 to P299; "transition period" 2 hits, both unrelated (P294, p. 27 slide title; P297, p. 36 salary text)] |
| Periods in P1 | Quarters Q1 2011 to Q4 2013; years FY2009 to FY2013; Q4 of each year derived as year minus nine months; FY2009 from the FY2010 10-K comparative column (not a pack text file) | [P0, "How statements.xlsx is made"; P1, LOCATORS] |
| Earliest text-file annual report | FY2011 10-K (covers FY2009 to FY2011 flows, FY2010 and FY2011 balance sheets) | [P0, header table] |
| Presentation | Unclassified balance sheet; no cost-of-sales or gross-profit line; debt is one line on EXTRA | [P0, "Known limits"] |
| Non-GAAP regime | Regulation G and Item 10(e) of Regulation S-K | [P0, header table] |
| Other pack scope notes | FY2013 10-K/A filed 20 March 2014 is not a text file; per the manifest its sole purpose was to correct the auditor's consent (Exhibit 23.1). 10-Q Part I Item 4 (controls) is not extracted. Proxy files hold compensation sections only | [P0, "Known limits"] |

## 2. Pack inventory

All 300 files listed in the manifest (P0 to P299) were opened: P0 read directly, P1 to P299 opened by script; none was missing, empty or unreadable [calc, inventory.py]. P1 opened with 11 sheets: IS_Q, IS_A, BS_Q, BS_A, CF_Q, CF_A, EXTRA, NOTES, NONGAAP, RESTATED, LOCATORS [calc, inventory.py].

| Group | IDs | Files | Status |
|---|---|---|---|
| Manifest | P0 | manifest.md | opened |
| Statement workbook | P1 | statements.xlsx | opened |
| FY2011 10-K sections | P2 to P29 | 28: business, risk-factors, legal, mdna, critical-estimates, market-risk, auditor-report, financial-statements, notes-01 to notes-17, schedule-ii, controls, related-parties | all opened |
| FY2012 10-K sections | P30 to P58 | 29: as above with notes-01 to notes-18 | all opened |
| FY2013 10-K sections | P59 to P88 | 30: as above with notes-01 to notes-19 | all opened |
| Q1 2011 10-Q | P89 to P108 | 20: financial-statements, notes-01 to notes-17, mdna, risk-factors | all opened |
| Q2 2011 10-Q | P109 to P128 | 20: financial-statements, notes-01 to notes-17, mdna, risk-factors | all opened |
| Q3 2011 10-Q | P129 to P147 | 19: financial-statements, notes-01 to notes-16, mdna, risk-factors | all opened |
| Q1 2012 10-Q | P148 to P166 | 19: financial-statements, notes-01 to notes-17, mdna | all opened |
| Q2 2012 10-Q | P167 to P185 | 19: financial-statements, notes-01 to notes-17, mdna | all opened |
| Q3 2012 10-Q | P186 to P205 | 20: financial-statements, notes-01 to notes-17, mdna, risk-factors | all opened |
| Q1 2013 10-Q | P206 to P226 | 21: financial-statements, notes-01 to notes-18, mdna, risk-factors | all opened |
| Q2 2013 10-Q | P227 to P246 | 20: financial-statements, notes-01 to notes-18, mdna | all opened |
| Q3 2013 10-Q | P247 to P267 | 21: financial-statements, notes-01 to notes-18, mdna, risk-factors | all opened |
| Releases | P268 to P296 | 29: ER-Q4-FY2010 to ER-Q4-FY2013 (13 earnings releases) and 16 OTHER files (call slides, the 29 July 2013 correction release, the 31 July 2013 clarification release, the 25 January 2011 release) | all opened |
| Proxies | P297, P298 | PROXY-2012, PROXY-2013 (compensation sections) | all opened |
| Events | P299 | events.txt | opened |

The full ID-by-file list printed by the inventory script is reproduced after the code in section 10; every ID from P1 to P299 appears there [calc, inventory.py].

## 3. Tie-out

Tolerance: USD 1m, one unit of P1's scale. All tests run in code (tieout.py). 183 tests passed, 3 failed, and the rest could not run for the reasons given [calc, tieout.py].

| Test | Periods | Result | Mark |
|---|---|---|---|
| Balance sheet: total assets = total liabilities + total equity | BS_Q Q1 2011 to Q4 2013 (12); BS_A FY2009 to FY2013 (5) | Passed, 17 of 17; largest difference 0.1 | [calc] |
| Balance sheet: total assets = "Total liabilities and equity" (EXTRA) | same 17 | Passed, 17 of 17 | [calc] |
| Cash flow: operating + investing + financing + FX = net change in cash | CF_Q 12 quarters; CF_A 5 years | Passed, 17 of 17; largest difference 0.1 | [calc] |
| Cash flow: net change = change in balance-sheet cash | CF_Q Q1 2011 to Q3 2013 (11); CF_A FY2010 to FY2012 (3) | Passed, 14 of 14 | [calc] |
| Same | CF_Q, Net change in cash, Q4 FY2013 | **Failed**: -137.7 against a balance-sheet change of -125.5 (difference -12.2) | [calc] |
| Same | CF_A, Net change in cash, FY2013 | **Failed**: -122.3 against -110.1 (difference -12.2). Cause: FY2012 cash revised from 533.3 to 545.5 in the FY2013 10-K; recomputed on the revised opening balance the difference is 0.0 | [calc, C1; P1, RESTATED; P68, p. 84] |
| Same | CF_A FY2009 | Not run: no FY2008 balance sheet in P1 | [P1, BS_A] |
| Income statement: revenue - COGS = gross profit | all 17 periods | Not runnable: P1 has no COGS or gross-profit lines because the statements have none | [P0, "Known limits"] |
| Substitute check: pre-tax income - tax = net income | 17 periods | Passed, 17 of 17 | [calc] |
| Substitute check: revenue - total expenses = pre-tax income | FY2009 to FY2013 | Passed, 5 of 5 | [calc] |
| Quarters to years, income statement (11 flow lines x FY2011 to FY2013) | 33 tests | Passed, 33 of 33; largest difference 0.2 (income tax expense FY2011) | [calc] |
| Quarters to years, cash flow (21 flow lines x FY2011 to FY2013) | 63 tests | Passed, 63 of 63 | [calc] |
| Same | CF_Q, Stock repurchased, FY2013 | **Failed**: Q1 to Q3 blank, Q4 -87.5 (derived), year -554.7; the implied nine-month amount is -467.2, which the Q1 2013 10-Q shows as "Purchase of treasury shares \| (467,248)" in thousands. P1 is missing the Q1 FY2013 value | [calc, C13; P206, financial statements, cash flow] |
| Same | Diluted shares and diluted EPS | Not run: Q4 not derived by design | [P0, "How statements.xlsx is made"] |
| Scale scan (rule 4), every row of every sheet | all | EXTRA only: Common Stock value in thousands (4164 to 4230) for Q2 2011 to Q1 2013, FY2011, FY2012; Treasury Stock Q1 FY2013 -467248 [calc, C12]. EXTRA "Basic (in shares)" Q4 values (0.3, 0.4, 8.4) look like year-minus-nine-month differences of weighted shares, not share counts; LOCATORS has no rows for EXTRA, so this is not confirmed | [calc, C12; inf: P0 "How statements.xlsx is made", P1 EXTRA and LOCATORS] |
| Sign check | EXTRA, Proceeds under the revolving lines of credit, FY2013 | -9511.6 in P1 against 9,511.6 in the filing | [calc, C15; P66, p. 81] |

**Warnings inherited by later steps** [inf: P1, P68]:
- W1: CF_Q Q4 FY2013 and CF_A FY2013 "Net change in cash" do not reconcile to P1 balance-sheet cash; use FY2012 cash of 545.5 (as revised) as the FY2013 opening balance.
- W2: CF_Q "Stock repurchased" Q1 FY2013 is blank; the true Q1 FY2013 value is -467.2.
- W3: Any use of EXTRA Common Stock, Treasury Stock or treasury-purchase cells, or FY2013 revolver proceeds, needs the scale or sign fixed first.
- W4: Every P1 cell for FY2011, FY2012, Q1 2012 to Q3 2013 is pre-revision (E24); FY2009 and FY2010 are pre-revision (E4).

**RESTATED sheet check (method step 5, in code).** 37 lines differ by more than USD 1m between the year as originally reported and the same year reprinted in the following 10-K: 9 for FY2010, 0 for FY2011, 28 for FY2012 [calc, C2]. The FY2010 differences are labelled by the Q3 2011 revision (E4) and the FY2012 differences by the FY2013 revision (E24) [P131, p. 7; P68, pp. 83 to 84]. Line-level differences the company's text does not itemise [calc, C2, C14; P68, p. 84]:
- FY2012 "Capital expenditures (PP&E)" -312.8 to -297.1 (+15.7) and "Proceeds from disposals" 137.7 to 122.0 (-15.7): the note gives only section totals ("investing activities (increased $20.4 million)").
- FY2012 changes in receivables (+8.5), payables (-15.9) and accrued liabilities (-7.0) inside operating cash flow: the note gives only "operating activities (decreased $8.1 million)".
- Two lines not in RESTATED at all: FY2011 as reprinted in the FY2013 10-K (revenue +0.9, SG&A +22.4, pre-tax income -18.7, net income -11.9, operating cash flow -22.2, investing cash flow +22.3) [calc, C3, C14; P66, pp. 76, 80], and FY2009 as revised in the Q3 2011 10-Q (total assets +12.7, total liabilities +24.9, total equity -10.2; net loss attributable -3.5) [calc, C6; P131, p. 7].

## 4. Event log

| ID | Date | Event | Type | Periods affected | Lines affected | Locator |
|---|---|---|---|---|---|---|
| E1 | 2011-05-06 (Q1 2011 10-Q) | Cash flow revision for Q1 2010: "For the three months ended March 31, 2010, we have revised net cash provided by operating activities and net cash used in investing activities within our consolidated statement of cash flows due to a gross-up of cash lease payments relating to our revenue earning equipment in the non-cash add back previously included in depreciation of revenue earning equipment and proceeds from disposal of revenue earning equipment." Amount not stated | revision | Q1 2010 to Q3 2010 comparatives (outside P1 quarters) | Operating and investing cash flow, fleet depreciation add-back, fleet disposal proceeds | [P91, p. 7; P131, p. 9] |
| E2 | 2011-09-01 | Acquisition of Donlen Corporation (fleet leasing and management). Purchase price USD 250.0m; goodwill 51.1, other intangibles 75.0, revenue earning equipment 1,120.6, receivables 64.0, accounts payable 39.3, accrued liabilities 226.8, debt 728.8. Revenue 142.7 and earnings 2.0 from 1 September to 31 December 2011 (122 days; 1.7% of FY2011 revenue). Excluded from FY2011 internal-control assessment (7.7% of assets, 1.7% of revenue). Goodwill first reported in car rental, later in all other operations | acquisition | Q3 2011 (one month in income statement, full balance sheet at 30 Sep), Q4 2011, FY2011; year-over-year breaks through Q3 2012 and FY2012 | Revenue, receivables, fleet assets, intangibles, goodwill, payables, accruals, debt, operating cash flow | [P12, pp. 99 to 101; P28; P8, p. 85; P299; calc, C9] |
| E3 | FY2011 | "ten international car rental locations and four domestic equipment rental locations" added by acquiring a former franchisee and external acquisitions; "not material" | acquisition | FY2011 | Revenue, intangibles | [P12, p. 101] |
| E4 | 2011-11-07 (Q3 2011 10-Q); repeated in FY2011 10-K | Revision of FY2008 to FY2010: "During the third quarter of 2011, we identified certain errors in our previously issued consolidated financial statements." "These errors relate to additional telecommunication charges and depreciation of revenue earning equipment, as well as certain corrections to deferred taxes on income for years 2005 through 2010 and the related impact on the 2008 goodwill impairment." FY2010 total assets 17,332.2 to 17,345.0, total liabilities 15,200.9 to 15,226.5, total equity 2,131.3 to 2,118.5; FY2009 total assets 16,002.4 to 16,015.1, liabilities 13,905.0 to 13,929.9, equity 2,097.4 to 2,087.2; net loss attributable FY2010 -0.6, FY2009 -3.5. The two filings describe the cumulative effect differently (Q3 2011 10-Q: USD (26.9)m to 31 Dec 2007 retained earnings; FY2011 10-K: USD (8.7)m to 31 Dec 2008 accumulated deficit) and the 2009 direct operating adjustment differently (6,300 against 2,634, in thousands; difference USD 3.7m) | revision | FY2008 to FY2010 and 2010 quarters; P1 FY2009 is pre-revision and not in RESTATED; P1 FY2010 is pre-revision, reprint in RESTATED | Direct operating, fleet depreciation, SG&A (2009), income tax, goodwill, fleet assets net, accounts payable, deferred taxes, equity | [P131, pp. 7 to 8; P11, p. 92; P1, RESTATED; calc, C6] |
| E5 | 2011-12 | Purchase of the noncontrolling interest in Navigation Solutions, L.L.C. (65% to 100%); USD 38.0m in accounts payable at 31 Dec 2011, paid in 2012; noncontrolling interest goes to zero | other | Q4 2011, FY2011, FY2012 | Equity, noncontrolling interest, accounts payable, financing cash flow | [P10, p. 91; P9, pp. 89 to 90; P1, BS_Q and EXTRA] |
| E6 | 2012-01-19 | HERC acquired Cinelease Holdings, LLC; the Q1 2012 release also names Arpielle; nineteen domestic equipment rental locations added in 2012, "not material". Consideration not disclosed in the files searched. Acquisitions, net of cash, Q1 2012: 147.3 | acquisition | Q1 2012 onward; FY2012 | Revenue, fleet assets, intangibles, direct operating | [P166, pp. 39 to 40; P279, p. 3; P41, p. 91; P1, CF_Q Q1 FY2012] |
| E7 | 2012-Q1 | ASU 2011-05 (presentation of comprehensive income) effective "beginning with this quarterly report for the period ended March 31, 2012". ASU 2011-08 (goodwill qualitative test): "We did not avail ourselves of this option" for the 2011 test | adoption | Q1 2012 onward | Presentation of other comprehensive income only | [P150, p. 8; P11, p. 97] |
| E8 | 2012-Q1 | Equipment rental pricing metric changed: "Our pricing metric now reflects our adoption of the American Rental Association methodology." Whether prior periods were restated to the new method is not stated | other (operating metric) | Q1 2012 onward | Non-GAAP / operating metrics (equipment rental pricing) | [P166, p. 39] |
| E9 | 2012-11-19 | Acquisition of Dollar Thrifty Automotive Group, Inc. at USD 87.50 per share; total purchase price about USD 2,592m (cash 2,551m including about 404m of Dollar Thrifty cash, plus 41m fair value of the previously held interest; gain on remeasurement about 8.4m). Final allocation: goodwill 889 (preliminary 885), intangibles 1,545 (trade names 1,140; concessions 405), revenue earning equipment 1,614, receivables 170, inventories 8, accounts payable 43, accrued liabilities 298 (preliminary 277), deferred taxes 846 (preliminary 864), debt 1,484. Revenue 170.6 and earnings (25.9) for 43 days (1.9% of FY2012 revenue as originally reported). Excluded from the FY2012 internal-control assessment (21% of total assets, 2% of revenue) | acquisition | Q4 2012 (full balance sheet, 43 days of income statement), FY2012; year-over-year breaks through Q4 2013 and FY2013 | Revenue, receivables, inventory, fleet assets, intangibles, goodwill, payables, accruals, deferred taxes, debt, reserves (public liability line 281.5 to 332.2), operating cash flow | [P299; P41, p. 88; P70, pp. 97 to 99; P57; P36, p. 71; P1, EXTRA; calc, C9] |
| E10 | 2012-12-12; 2013-11-02 to 2013-12-16 | Advantage divestiture (Simply Wheelz LLC) for about USD 16.0m plus current assets of about 3.6m; pre-tax loss about 31.4m; support payments 17.0m over three years (present value 15.6m); credit line up to 45.0m; vehicle subleases to the buyer; results kept in continuing operations because of continuing involvement. Divestiture of selected Dollar Thrifty airport locations (loss including support payments 24.1m at 31 Dec 2012; remaining reserve 2.8m at 31 Dec 2013). Sublease revenue 22.2m in Q2 2013. Subleases terminated 2 Nov 2013; Simply Wheelz filed Chapter 11 on 5 Nov 2013; settlement 16 Dec 2013 | disposal | Q4 2012 onward; FY2012, FY2013 | Revenue, other (income) expense, reserves, receivables (support and loan arrangements) | [P41, p. 91; P70, pp. 100 to 101; P291, p. 1; P295, p. 5 note (f)] |
| E11 | 2013-01-01 | Standards effective in 2013: ASU 2011-11 (offsetting disclosures, "We plan to adopt ASU 2011-11 on January 1, 2013"); ASU 2012-02 (indefinite-lived intangibles test, fiscal years beginning after 15 Sep 2012); ASU 2013-02 (disclosure of reclassifications out of AOCI, periods beginning after 15 Dec 2012). Each described as not expected to be material. Adoption confirmations in the 2013 filings not found | adoption | FY2013 | Disclosures only, per the company | [P39, p. 84; P208, p. 9] |
| E12 | 2013-03-04 (FY2012 10-K) | Parent-only (Schedule I) cash flow revision: return of capital from a subsidiary moved from operating to investing, USD 23.0m in each of 2011 and 2010. "The classification of these amounts have been corrected so that they are presented as cash flows from investing activities." | revision | FY2010, FY2011 parent-only statements | Parent-company operating and investing cash flow (not the consolidated statements) | [P37, p. 138] |
| E13 | 2013-03 | Hertz repurchased 23,200,000 shares from the underwriters of a Sponsor secondary offering (USD 467.2m, shown in the Q1 2013 10-Q); settlement policy for the 5.25% Convertible Senior Notes changed: "Upon completion of the share repurchase from the underwriters, we announced a change to our former settlement policy and stated our intention to settle the Convertible Senior Notes in 100% shares of our common stock." EPS numerator add-back 7.7m in 2013. Convertible notes converted during 2013 (non-cash 372.5) | policy change (EPS); other | Q1 2013 onward, FY2013 | Diluted EPS, diluted shares, equity, financing cash flow | [P83, pp. 148 to 149; P206, cash flow; P1, EXTRA FY2013; P295, p. 2 note (a)] |
| E14 | 2013-04-29; 2013-07-29; 2013-07-31 | Non-GAAP metric "total RPD" introduced in Q1 2013; Q2 2013 release corrected: "Worldwide revenue per day (RPD) for the six months ended June 30, 2013, was incorrectly reported as $48.55 in table 4 accompanying the press release." Clarification: "Given the unique and temporary nature of the sublease revenue, and to provide clarity, we will not include it in our total RPD calculation going forward." | other (non-GAAP definition) | Q1 2013 onward | Non-GAAP RPD metrics | [P287, pp. 1, 3; P290, p. 1; P291, p. 1] |
| E15 | 2013-05-01 | Strategic investment in China Auto Rental Holdings, Inc.: 10% of ordinary shares plus convertible notes (18.64% fully diluted); Hertz China Rent-a-Car entities de-consolidated and contributed; equity method; convertible notes available for sale at fair value 151.0m at 31 Dec 2013 (Level 3), unrealized gain 21.0m. Cash consideration not disclosed in the files searched | disposal (de-consolidation); acquisition of investment | Q2 2013 onward | Revenue and assets of the China operations, other assets, AOCI | [P70, p. 100; P227 notes-05, p. 12; P81, p. 145] |
| E16 | FY2013 | "twenty seven locations" re-acquired from former franchisees and three through external acquisitions; "not material". Acquisitions, net of cash acquired, FY2013: 254.0 | acquisition | FY2013 | Revenue, intangibles | [P70, p. 101; P1, CF_A FY2013] |
| E17 | 2013-08-02 (Q2 2013 10-Q) | (a) Cash flow revision: revolving-line borrowings and repayments presented gross, not net, in financing, "This revision had no impact on the Company's total operating, investing or financing cash flows." Repeated for FY2012 and FY2011 in the FY2013 10-K. (b) Revenue lines reclassified: Q2 2013 "Other" revenue 0.8 against 79.2 in Q1 2013; Q2 2012 reprinted as car rental 1,889.6 (originally 1,849.3) and other 0.5 (originally 41.6). The only explanation found: "Certain prior period amounts have been reclassified to conform with current period presentation." | revision (a); reclassification (b) | (a) FY2011, FY2012 and 2013 financing lines; (b) Q2 2012 onward revenue lines | (a) Financing cash flow lines only; (b) Car rental and Other revenue lines (not total revenue) | [P229, p. 8; P68, p. 83; P227, p. 3; P1, EXTRA; calc, C7] |
| E18 | 2013-Q3 (10-Q filed 2013-11-07) | Segment recast: "We now present our operations as four reportable segments (U.S. car rental, international car rental, worldwide equipment rental and all other operations)." Prior periods revised. Income-statement revenue lines relabelled worldwide car rental, worldwide equipment rental, all other operations. FY2012 recast: car rental 7,456.1 to 7,161.7 (-294.4), equipment 1,383.2 to 1,385.4 (+2.2), other 181.5 to 477.8 (+296.3); total +4.1, which is the E24 revision | segment recast | Q3 2013 onward; prior periods as reprinted | Revenue by line, segment adjusted pre-tax income, goodwill by segment | [P249, p. 8; P68, p. 83; P247, p. 3; P66, p. 76; calc, C7] |
| E19 | 2013-Q3 | "In the third quarter of 2013, the Company implemented Oracle general ledger, accounts payable and a portion of fixed assets, purchasing and procurement modules for most of its Hertz brand U.S. car rental and HERC U.S. and Canada equipment businesses." | control | Q3 2013 onward | Accounting systems (payables, fixed assets) | [P87] |
| E20 | 2013-05-09; 2013-08-15; 2013-10-01; 2013-12-09 | Stockholders Agreement terminated 9 May 2013; CD&R and Carlyle nominees resigned 15 Aug 2013; CFO Elyse Douglas resigned effective 1 Oct 2013 with an interim successor; Thomas C. Kennedy appointed CFO effective 9 Dec 2013 | other (governance, management) | Q2 to Q4 2013 | None directly | [P299] |
| E21 | 2013-11-19 | Dollar Thrifty purchase-price allocation finalised; changes from preliminary mainly "valuation of certain contracts, accrued liabilities and income taxes, and the resulting changes to goodwill." "Prior period financial statements were not revised for these adjustments as they would not have had a material impact on the prior period reported operating results and financial condition." | estimate change (acquisition accounting) | FY2012 balance sheet as reprinted; 2013 | Goodwill, intangibles, accrued liabilities, deferred taxes | [P70, p. 98; P41, p. 88; calc, C9] |
| E22 | FY2009 to FY2013 | Depreciation-rate changes on revenue earning equipment (change in estimate, reviewed quarterly). Car rental: 2009 +13.2, 2010 +19.1, 2011 -13.8, 2012 -130.6, 2013 -39.2 (U.S. -44.2, international +5.0); equipment rental: 2009 +6.1, 2010 +3.6, 2011 -4.4, 2012 +0.5, 2013 -0.4. FY2013 10-K splits 2012 as U.S. -139.4 and international +8.8, and 2011 as -26.7 and +12.9, which reconcile to the earlier totals. The 2012 car rental reduction equals 29.0% of FY2012 pre-tax income as originally reported | estimate change | Every year and quarter | Fleet depreciation, fleet assets net, disposal gains and losses | [P16, p. 125; P45, p. 113; P74, p. 126; calc, C8] |
| E23 | 2013-12-31; January 2014 | "As of December 31, 2013, a requirement under the HVF II Series 2013-B Notes was unknowingly not met, resulting in the occurrence of an amortization event under the HVF II Series 2013-B Notes that also triggered amortization events under certain other series of our outstanding U.S. rental car variable funding notes." Borrowing under these notes temporarily restricted at 31 Dec 2013; waivers from 100% of required noteholders obtained in January 2014 | other (covenant / waiver) | Q4 2013, FY2013; subsequent event | Debt availability; fleet financing | [P71, p. 108; P85, p. 150] |
| E24 | 2014-03-18 (release); 2014-03-19 (10-K) | Revision for out-of-period errors: "During the fourth quarter of 2013, we identified certain out of period errors totaling $46.3 million, of which $34.7 million ($21.0 million, net of tax) related to our previously issued consolidated financial statements for the years ended December 31, 2012, 2011 and prior." Components: vendor incentives recorded as a reduction of marketing expense instead of fleet cost (2011 12.9, 2012 2.4); Brazil asset charges and allowances for doubtful accounts (2010 4.4, 2011 6.2, 2012 3.6); other (2010 2.4, 2011 -0.4, 2012 3.2); the components sum to 34.7. Pre-tax income revised FY2011 -18.7 (5.8% of FY2011 pre-tax as originally reported), FY2012 -9.2 (2.0%); net income FY2011 -12.0, FY2012 -4.5. FY2012 balance sheet: total assets 23,286.0 to 23,264.3; equity 2,507.3 to 2,486.2; cash +12.3; restricted cash -20.0; receivables -7.0; fleet cost -42.3. Cash flow: FY2012 operating -8.1, investing +20.4; FY2011 operating -22.4, investing +22.4. Revised quarters: every 2012 quarter and Q1 to Q3 2013. The release states a different total: "These out of period errors totaling $47.9 million" (1.6 more than the 10-K). Schedule II opening 2013 allowance 29.3 against 25.1 closing FY2012 as originally reported. No Item 4.02 filing | revision | FY2010 (cumulative, via opening deficit), FY2011, FY2012, Q1 2012 to Q3 2013; Q4 2013 derived | Revenue, direct operating, fleet depreciation, SG&A, other expense, income tax, net income, cash, restricted cash, receivables, prepaid, fleet assets, intangibles, goodwill, payables, accruals, taxes, deferred taxes, equity, allowance, operating and investing cash flow | [P68, pp. 83 to 89; P84, p. 149; P86, p. 158; P295, pp. 2, 9; P299; calc, C3, C4, C5, C11] |
| E25 | 2014-03-19; 2014-03-20 | FY2013 10-K filed 78 days after year end (FY2011: 58; FY2012: 63); Q4 2013 earnings release 77 days after year end (prior three years: 53 to 56). FY2013 10-K/A filed 20 March 2014 to correct the auditor's consent (Exhibit 23.1), per the manifest. Whether a Form 12b-25 was filed cannot be checked (not in events.txt scope) | other (filing timing) | FY2013 | None directly | [P0, file table and "Known limits"; P299, header; calc, C10] |
| E26 | 2014-03 | "In March 2014, the Company announced that its Board of Directors has approved plans to separate the Hertz car and equipment rental businesses into two independent, publicly traded companies." New USD 1 billion share repurchase program | other (planned separation; subsequent) | After the pack period | None in pack periods; future segment and disposal break | [P85, p. 150] |

## 5. Auditor record

FY2009 and FY2010 audit reports are not in the pack [P0, "Known limits"].

| | FY2011 | FY2012 | FY2013 |
|---|---|---|---|
| Firm | PricewaterhouseCoopers LLP, Florham Park, New Jersey [P8, p. 85] | PricewaterhouseCoopers LLP, Florham Park, New Jersey [P36] | PricewaterhouseCoopers LLP, Florham Park, New Jersey [P65] |
| Report date | 27 February 2012 [P8, p. 85] | 4 March 2013 [P36] | 19 March 2014 [P65] |
| Tenure | Not stated [not found: P8, P297, P298 searched for "since", "served as", "PricewaterhouseCoopers"] | Not stated [not found: P36, same terms] | Not stated [not found: P65, same terms] |
| Opinion, financial statements | Unqualified: "present fairly, in all material respects" [P8, p. 84] | Unqualified, same words [P36, p. 71] | Unqualified, same words [P65, p. 74] |
| Opinion, internal control | Effective as of 31 Dec 2011 [P8, p. 84] | Effective as of 31 Dec 2012 [P36, p. 71] | Effective as of 31 Dec 2013, COSO 1992 framework [P65, p. 74] |
| Emphasis, explanatory or going-concern paragraph | None [P8: 0 hits for "emphasi", "explanatory", "as discussed in note", "going concern"] | None [P36: same] | None; the report does not mention the revision of prior periods [P65: 0 hits for "revis", "error" and the terms above] |
| Other paragraph | Donlen excluded from the internal-control audit (about 8% of assets, 2% of revenue) [P8, p. 85] | Dollar Thrifty excluded from the internal-control audit (about 21% of assets, 2% of revenue) [P36] | None |
| Critical audit matter titles | None: reports predate critical audit matters [P0, header table] | None [P0] | None [P0] |
| Changes | No Item 4.01 report 1 Jan 2011 to 31 Mar 2014 [P299] | Same [P299] | Same; 10-K/A of 20 Mar 2014 corrected the auditor's consent exhibit only [P0, "Known limits"] |

## 6. Comparability map

Each cell compares the period with the same period one year earlier. "Clean" means no event from steps 3 to 7 breaks that comparison. Event IDs refer to section 4. P1 holds no 2010 quarters and no FY2008 [P1, IS_Q, IS_A]. "Gross margin" has no line in these statements [P0, "Known limits"]; the cell covers the cost lines F2 would use in its place (direct operating and fleet depreciation).

**Annual**

| Line group | FY2009 | FY2010 | FY2011 | FY2012 | FY2013 |
|---|---|---|---|---|---|
| Revenue | No FY2008 in P1 | Clean | E2, E3, E24 | E6, E9, E10, E24; line split E18 | E9, E10, E15, E16, E24; line split E17, E18 |
| Gross margin (cost lines) | No FY2008 in P1; E4, E22 | E4, E22 | E2, E22, E24 | E9, E10, E22, E24 | E9, E22, E24 |
| Receivables and contract assets | No FY2008 in P1 | Clean | E2, E24 | E9, E24 | E15, E24 |
| Inventory | No FY2008 in P1 | Clean | Clean | E9 | E15 (effect not disclosed) |
| Payables and accruals | No FY2008 in P1; E4 | E4 | E2, E4 (opening), E5, E24 | E9, E21, E24 | E9, E21, E24 |
| PP&E and intangibles | No FY2008 in P1; E4, E22 | E4, E22 | E2, E4 (opening), E22, E24 | E6, E9, E21, E22, E24 | E15, E21, E22, E24 |
| Reserves and provisions | No FY2008 in P1 | Clean | E24 (Brazil allowances) | E9, E10, E24 | E10, E24 |
| Operating cash flow | No FY2008 in P1 | E4 (change in payables +1.1) | E2, E24 | E9, E24 | E9, E24; tie-out W1 |
| Non-GAAP measures | No FY2008 in P1; E4 | E4 | E2, E24 | E8, E9, E10, E24 | E13, E14, E18, E24 |

**Quarterly, 2011** (no 2010 quarters in P1; events listed are those inside the quarter)

| Line group | Q1 2011 | Q2 2011 | Q3 2011 | Q4 2011 |
|---|---|---|---|---|
| Revenue | No Q1 2010 in P1; E24 | No Q2 2010 in P1; E24 | No Q3 2010 in P1; E2, E24 | No Q4 2010 in P1; E2, E24 |
| Gross margin (cost lines) | No Q1 2010; E22, E24 | No Q2 2010; E22, E24 | No Q3 2010; E2, E22, E24 | No Q4 2010; E2, E22, E24 |
| Receivables and contract assets | No Q1 2010; E24 | No Q2 2010; E24 | No Q3 2010; E2, E24 | No Q4 2010; E2, E24 |
| Inventory | No Q1 2010 in P1 | No Q2 2010 in P1 | No Q3 2010 in P1 | No Q4 2010 in P1 |
| Payables and accruals | No Q1 2010; E24 | No Q2 2010; E24 | No Q3 2010; E2, E24 | No Q4 2010; E2, E5, E24 |
| PP&E and intangibles | No Q1 2010; E22, E24 | No Q2 2010; E22, E24 | No Q3 2010; E2, E22, E24 | No Q4 2010; E2, E22, E24 |
| Reserves and provisions | No Q1 2010; E24 | No Q2 2010; E24 | No Q3 2010; E24 | No Q4 2010; E24 |
| Operating cash flow | No Q1 2010; E24 | No Q2 2010; E24 | No Q3 2010; E2, E24 | No Q4 2010; E2, E24 |
| Non-GAAP measures | No Q1 2010; E24 | No Q2 2010; E24 | No Q3 2010; E2, E24 | No Q4 2010; E2, E24 |

The 2011 quarters as revised by E24 are not disclosed; only FY2011 as revised is [not found: P84, P68 searched for 2011 quarterly columns].

**Quarterly, 2012** (compared with the same 2011 quarter)

| Line group | Q1 2012 | Q2 2012 | Q3 2012 | Q4 2012 |
|---|---|---|---|---|
| Revenue | E2, E6, E24 | E2, E6, E24; line split E17 | E2, E6, E24 | E9, E10, E24 |
| Gross margin (cost lines) | E2, E22, E24 | E2, E22, E24 | E2, E22, E24 | E9, E10, E22, E24 |
| Receivables and contract assets | E2, E24 | E2, E24 | E24 | E9, E24 |
| Inventory | Clean | Clean | Clean | E9 |
| Payables and accruals | E2, E24 | E2, E24 | E24 | E9, E24 |
| PP&E and intangibles | E2, E6, E22, E24 | E2, E6, E22, E24 | E6, E22, E24 | E9, E22, E24 |
| Reserves and provisions | E24 | E24 | E24 | E9, E10, E24 |
| Operating cash flow | E2, E24 | E2, E24 | E2, E24 | E9, E24 |
| Non-GAAP measures | E2, E8, E24 | E2, E8, E24 | E2, E8, E24 | E8, E9, E10, E24 |

**Quarterly, 2013** (compared with the same 2012 quarter; Q4 2013 derived on mixed bases, see "Read first" item 2)

| Line group | Q1 2013 | Q2 2013 | Q3 2013 | Q4 2013 |
|---|---|---|---|---|
| Revenue | E9, E10, E24 | E9, E10, E15, E24; line split E17 | E9, E10, E15, E24; line split E18 | E9, E10, E15, E24 (Q4 absorbs 9M corrections); line split E18 |
| Gross margin (cost lines) | E9, E22, E24 | E9, E15, E22, E24 | E9, E15, E22, E24 | E9, E15, E22, E24 (Q4 absorbs 9M corrections) |
| Receivables and contract assets | E9, E24 | E9, E15, E24 | E9, E15, E24 | E15, E24 |
| Inventory | E9 | E9, E15 | E9, E15 | E15 |
| Payables and accruals | E9, E24 | E9, E15, E24 | E9, E15, E24 | E15, E21, E24 |
| PP&E and intangibles | E9, E22, E24 | E9, E15, E22, E24 | E9, E15, E22, E24 | E15, E21, E22, E24 |
| Reserves and provisions | E9, E10, E24 | E9, E10, E24 | E9, E10, E24 | E10, E24 |
| Operating cash flow | E9, E24 | E9, E24 | E9, E24 | E9, E24; tie-out W1 |
| Non-GAAP measures | E9, E13, E14, E24 | E9, E13, E14, E24 | E9, E13, E14, E18, E24 | E13, E14, E18, E24 |

## 7. Items for the ledger

ID assignment is an assumption: the checklist that defines C15, C16 and E4 is not in the pack, so F1-C15 is used for restatements and revisions, F1-C16 for auditor matters and F1-E4 for internal-control and covenant conditions [inf: F1 prompt header and output section 7]. No non-reliance conclusion, auditor change, auditor disagreement, reportable event, material weakness or going-concern language was found [P299; search results in "Looked for and not found"], so no row is P1.

| ID | Item | Period | Evidence | Locator | Benign reading | Adverse reading | Context | Resolving disclosure | Priority | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| F1-C15-1 | Revision of FY2011, FY2012, 2012 quarters and Q1 to Q3 2013 for out-of-period errors | FY2010 to Q3 2013 | "During the fourth quarter of 2013, we identified certain out of period errors totaling $46.3 million, of which $34.7 million ($21.0 million, net of tax) related to our previously issued consolidated financial statements for the years ended December 31, 2012, 2011 and prior." Pre-tax income revised FY2011 -18.7 (5.8% of FY2011 pre-tax as originally reported) [calc, C5]; FY2012 -9.2 (2.0%) [calc, C5]. Release total 47.9 against 10-K total 46.3 [calc, C5] | P68, pp. 83 to 89; P84, p. 149; P295, p. 9 | The company found and corrected classification and estimate errors (vendor incentives booked against marketing expense rather than fleet cost; Brazil asset charges and bad-debt allowances; small other items), judged them immaterial to each prior period, and disclosed the corrections with period-by-period tables [P68, pp. 83 to 89] | Errors in several areas spanning 2010 to 2013 were identified in a single quarter; the vendor-incentive item moved cost between SG&A and fleet depreciation, so line-level trends in P1 for 2011 to 2013 are on a different basis from the revised filings; the release and the 10-K give different totals [inf: P68, P295, P1] | E24; no Item 4.02 filing [P299]; internal control concluded effective [P87; P65]; auditor report silent on the revision [P65] | Explanation of the 1.6 difference between 47.9 and 46.3; revised 2011 quarters; revised 2013 interim cash flows; how control deficiencies behind the errors were evaluated [not found: P68, P87, P295, P296] | P3 | |
| F1-C15-2 | Revision of FY2008 to FY2010 identified in Q3 2011 | FY2008 to FY2010 (P1 FY2009, FY2010) | "During the third quarter of 2011, we identified certain errors in our previously issued consolidated financial statements." FY2010 equity 2,131.3 to 2,118.5; FY2009 net loss attributable -3.5 [calc, C6]. Cumulative effect described as USD (26.9)m to 31 Dec 2007 retained earnings in the 10-Q and USD (8.7)m to 31 Dec 2008 accumulated deficit in the 10-K; 2009 direct operating adjustment 6,300 against 2,634 (thousands) | P131, pp. 7 to 8; P11, p. 92 | Mostly multi-year deferred-tax corrections with small income-statement effects, disclosed in the quarter found and carried into the 10-K [P131; P11] | A second revision within three years; the 10-Q and 10-K describe the 2009 and pre-2009 effects differently [inf: P131, P11] | E4; P1 FY2009 is pre-revision and not in RESTATED [P1] | Reconciliation of the two descriptions of the 2009 and cumulative effects [not found: P9, P11, P131] | P3 | |
| F1-C15-3 | Cash flow classification revisions (three) | Q1 2010; FY2010 to FY2012 | (a) Q1 2010 lease-payment gross-up between operating and investing; (b) parent-only return of capital 23.0 per year moved to investing for 2010 and 2011; (c) revolver borrowings and repayments presented gross, "This revision had no impact on the Company's total operating, investing or financing cash flows." | P91, p. 7; P37, p. 138; P229, p. 8; P68, p. 83 | Presentation corrections that leave total cash flows unchanged (a is within the consolidated statement; b is parent-only; c is within financing) [P91; P37; P229] | Classification of fleet-related cash between operating and investing has been corrected more than once, which bears on operating cash flow trends [inf: P91, P68] | E1, E12, E17 | Amounts for (a) [not found: P91, P131] | P3 | |
| F1-C15-4 | FY2012 cash flow line differences not itemised by the company | FY2012 | Capital expenditures -312.8 to -297.1 (+15.7) and proceeds from disposal of property and equipment 137.7 to 122.0 (-15.7); changes in receivables +8.5, payables -15.9, accrued liabilities -7.0; the note gives only section totals [calc, C2] | P1, RESTATED; P66, p. 80; P68, p. 84 | Offsetting reclassifications inside investing and operating that belong to the E24 corrections [inf: P68] | Line-level reclassification between capital spending and disposal proceeds is not explained anywhere in the text [inf: P68, P66] | E24 | Line-level reconciliation [not found: P66, P68] | P3 | |
| F1-C16-1 | Auditor consent exhibit corrected by 10-K/A; no auditor change | FY2013 | 10-K/A filed 20 March 2014 "to correct an error in Exhibit 23.1"; the original consent also listed two Form S-3 file numbers (manifest summary). No Item 4.01 report in the window | P0, "Known limits"; P299 | Clerical correction of the registration statements listed in the consent [P0] | None beyond a filing error on the auditor's consent [inf: P0] | E25; same firm all three years [P8, P36, P65] | 10-K/A text itself (not a pack text file) [P0] | P3 | |
| F1-E4-1 | HVF II Series 2013-B requirement not met at year end; amortization events; waivers | Q4 2013 | "As of December 31, 2013, a requirement under the HVF II Series 2013-B Notes was unknowingly not met, resulting in the occurrence of an amortization event..." Waivers from 100% of required noteholders in January 2014 | P71, p. 108; P85, p. 150 | A technical requirement on a new financing platform, cured by waiver within weeks [P71; P85] | The company did not know of the lapse at year end, and borrowing under the affected notes was restricted at 31 Dec 2013 [P71] | E23; ICFR concluded effective [P87] | Nature of the requirement and whether it was evaluated as a control deficiency [not found: P71, P85, P87] | P3 | |
| F1-E4-2 | Internal control concluded effective in the year of the E24 revision, the E23 lapse, an ERP implementation and a CFO change | FY2013 | ICFR effective as of 31 Dec 2013 by management and auditor; no material weakness or significant deficiency disclosed; Oracle modules implemented in Q3 2013; CFO resigned effective 1 Oct 2013 | P87; P65, p. 74; P299 | Errors were judged immaterial individually and in aggregate, which is consistent with no material weakness [P68, p. 83] | Several errors across years and areas surfaced in one quarter alongside a system change and finance leadership change, with no disclosure of how deficiencies were evaluated [inf: P68, P87, P299] | E19, E20, E23, E24 | Management's evaluation of deficiencies [not found: P87, P62] | P3 | |

```csv
ID,Item,Period,Evidence,Locator,Benign reading,Adverse reading,Context,Resolving disclosure,Priority,Verdict
F1-C15-1,"Revision of FY2011, FY2012, 2012 quarters and Q1 to Q3 2013 for out-of-period errors","FY2010 to Q3 2013","Out of period errors totaling $46.3m, of which $34.7m ($21.0m net of tax) related to FY2012, FY2011 and prior. Pre-tax income revised FY2011 -18.7 (5.8% of FY2011 pre-tax as originally reported) [calc]; FY2012 -9.2 (2.0%) [calc]. Release total 47.9 vs 10-K 46.3 [calc]","P68 pp.83-89; P84 p.149; P295 p.9","Company found and corrected classification and estimate errors (vendor incentives, Brazil allowances, other), judged immaterial, disclosed with period tables","Errors in several areas spanning 2010-2013 identified in one quarter; vendor-incentive item moved cost between SG&A and fleet depreciation; P1 2011-2013 lines on pre-revision basis; release and 10-K totals differ","E24; no Item 4.02 (P299); ICFR effective (P87, P65); auditor report silent (P65)","Explanation of 1.6 difference; revised 2011 quarters; revised 2013 interim cash flows; evaluation of control deficiencies [not found]",P3,
F1-C15-2,"Revision of FY2008 to FY2010 identified in Q3 2011","FY2008 to FY2010","Errors identified Q3 2011; FY2010 equity 2,131.3 to 2,118.5; FY2009 net loss attributable -3.5 [calc]; cumulative effect (26.9) to Dec 2007 RE in 10-Q vs (8.7) to Dec 2008 deficit in 10-K; 2009 direct operating adj 6,300 vs 2,634 (thousands)","P131 pp.7-8; P11 p.92","Mostly multi-year deferred-tax corrections with small income-statement effects, disclosed when found","Second revision within three years; 10-Q and 10-K describe 2009 and cumulative effects differently","E4; P1 FY2009 pre-revision and not in RESTATED","Reconciliation of the two descriptions [not found]",P3,
F1-C15-3,"Cash flow classification revisions (three)","Q1 2010; FY2010 to FY2012","(a) Q1 2010 lease-payment gross-up operating/investing; (b) parent-only return of capital 23.0 per year to investing 2010-2011; (c) revolver borrowings presented gross, no impact on section totals","P91 p.7; P37 p.138; P229 p.8; P68 p.83","Presentation corrections leaving total cash flows unchanged","Fleet-related cash classification between operating and investing corrected more than once","E1, E12, E17","Amounts for (a) [not found]",P3,
F1-C15-4,"FY2012 cash flow line differences not itemised by the company","FY2012","Capex -312.8 to -297.1 (+15.7); proceeds from disposal of P&E 137.7 to 122.0 (-15.7); receivables +8.5, payables -15.9, accrued -7.0; note gives section totals only [calc]","P1 RESTATED; P66 p.80; P68 p.84","Offsetting reclassifications belonging to the E24 corrections","Capex vs disposal-proceeds reclassification not explained in the text","E24","Line-level reconciliation [not found]",P3,
F1-C16-1,"Auditor consent exhibit corrected by 10-K/A; no auditor change","FY2013","10-K/A filed 2014-03-20 to correct Exhibit 23.1 (manifest summary); no Item 4.01 report in window","P0 Known limits; P299","Clerical correction of registration statements listed in the consent","Filing error on the auditor's consent only","E25; same firm FY2011-FY2013 (P8, P36, P65)","10-K/A text (not a pack text file)",P3,
F1-E4-1,"HVF II Series 2013-B requirement not met at year end; amortization events; waivers","Q4 2013","Requirement unknowingly not met at 31 Dec 2013, amortization events triggered; waivers from 100% of required noteholders January 2014","P71 p.108; P85 p.150","Technical requirement on new platform, cured by waiver within weeks","Company unaware at year end; borrowing restricted at 31 Dec 2013","E23; ICFR effective (P87)","Nature of requirement; control evaluation [not found]",P3,
F1-E4-2,"ICFR concluded effective in year of E24 revision, E23 lapse, ERP implementation and CFO change","FY2013","ICFR effective at 31 Dec 2013 (management and auditor); no material weakness or significant deficiency disclosed; Oracle modules Q3 2013; CFO resigned effective 1 Oct 2013","P87; P65 p.74; P299","Errors judged immaterial individually and in aggregate","Several errors surfaced in one quarter alongside system and finance leadership change; no disclosure of deficiency evaluation","E19, E20, E23, E24","Management's evaluation of deficiencies [not found]",P3,
```

## 8. Looked for and not found

| Disclosure | Files searched | Terms | Result |
|---|---|---|---|
| Change of fiscal year end, extra week | P2 to P299 | "change in fiscal year", "53-week", "53 week", "fifty-three", "extra week", "transition period" | 0 hits except 2 unrelated "transition period" hits (P294, P297) |
| Discontinued operations, held for sale | P2 to P299 | "discontinued", "held for sale" | 0 hits; Advantage kept in continuing operations [P70, p. 101] |
| Consideration for Cinelease, Arpielle, China Auto Rental | P41, P70, P166, P225, P227 notes-05, P247 notes-05, P279, P62, P66, P81, releases | "Cinelease", "Arpielle", "China Auto Rental", "China Auto" | Not disclosed in any file searched |
| Non-reliance conclusion (Item 4.02) | P299 | Item 4.02; "non-reliance" | None filed 1 Jan 2011 to 31 Mar 2014 [P299] |
| Change of auditor (Item 4.01), former auditor's letter | P299 | Item 4.01 | None [P299] |
| Auditor tenure statement | P8, P36, P65, P297, P298 | "since", "served as", "PricewaterhouseCoopers" | Not stated; proxies hold compensation only |
| Emphasis, explanatory or going-concern paragraph; mention of the revision in the FY2013 report | P8, P36, P65 | "emphasi", "explanatory", "as discussed in note", "going concern", "revis", "error" | 0 hits |
| Material weakness, significant deficiency, not effective | P2 to P299 | "material weakness", "significant deficiency", "not effective" | Only the audit-report sentence "assessing the risk that a material weakness exists" (P8, P9, P36, P37, P65, P66) |
| Going concern, substantial doubt | P2 to P299 | "going concern", "substantial doubt" | 0 hits |
| Late filing notice | P2 to P299 | "late filing", "NT 10-K", "12b-25" | 0 hits; events.txt does not cover Form 12b-25 [P299, header] |
| Remediation of control issues | P2 to P299 | "remediation" | 173 hits, sampled hits are environmental remediation in the contingencies notes (for example P79, p. 139) |
| Covenant breach or waiver other than E23 | P13, P42, P71, P85, releases | "in compliance", "waiver", "covenant default", "breach" | Only E23; "waiver" hits elsewhere are loss damage waiver product text (for example P295) |
| Change in accounting policy or estimate as a phrase | P2 to P299 | "change in accounting policy", "change in accounting estimate", "new accounting standard" | 0 hits; estimate changes found through the depreciation notes (E22) |
| Prior-period recast wording | P2 to P299 | "recast", "conformed to current" | "recast" hits are the word "forecast(s)" (sampled P107, P266); "conformed to current" 0 hits |
| "Correction of an error" phrase | P2 to P299 | "correction of an error" | 0 hits; the FY2013 note uses the heading "Correction of Errors" [P68, p. 83] |
| ASC 606, ASC 842, ASC 326, ASU 2022-04, ASU 2025-06 | P2 to P299 | "Topic 606", "Topic 842", "Topic 326", "2022-04", "2025-06", "2014-09", "2016-02" | 0 hits; none falls inside FY2009 to FY2013 [inf: P0 periods] |
| 2011 quarters as revised by E24 | P66, P68, P84 | 2011 quarterly columns | Not disclosed; FY2011 annual only |
| Revised 2013 interim cash flows | P68, P84, P295, P296 | quarterly cash flow revision | Not disclosed |
| Reason for Q2 2013 revenue-line reclassification | P229, P246 | "reclassif" | Only the general sentence "Certain prior period amounts have been reclassified to conform with current period presentation." [P229, p. 8] |
| Confirmation of 2013 adoption of ASU 2011-11, 2012-02, 2013-02 | P66, P68, P208, P229, P249 | "adopted", "adoption" | Only the forward-looking statements in P39 and P208 |
| 10-Q disclosure controls conclusions (Part I Item 4) | pack | n/a | Not extracted [P0, "Known limits"] |

## 9. Could not run

1. Income statement tie-out, revenue minus COGS equals gross profit, all 17 periods: no COGS or gross-profit line exists [P0, "Known limits"]. Substitute arithmetic checks were run instead.
2. Cash flow net change against balance-sheet cash for FY2009: no FY2008 balance sheet in P1.
3. Quarters-to-years for diluted shares and diluted EPS: Q4 not derived by design [P0].
4. Year-over-year comparability for FY2009 and for every 2011 quarter: P1 has no FY2008 or 2010 quarters.
5. IFRS-specific items (function or nature, revaluation model, IFRS 15/16/9/18, IAS 8, IAS 7 supplier finance): framework is US GAAP.
6. Canadian items (NI 52-107, NI 51-102 s. 11.5 and s. 4.11, NI 52-109, key audit matters): not a Canadian issuer.
7. Critical audit matter titles: the reports predate critical audit matters [P0].
8. Former auditor's letter and reportable events: no auditor change.
9. Auditor tenure: not printed in these reports.
10. FY2009 and FY2010 auditor reports and controls sections: FY2009 and FY2010 10-Ks are not text files [P0, "Known limits"].
11. Quarterly internal-control and disclosure-control conclusions: 10-Q Part I Item 4 not extracted [P0].
12. Form 12b-25 check: outside events.txt scope [P299].

## 10. Code

Scripts in the order they were first run. All read only the pack files. Python 3 with openpyxl.

**tieout.py**

```python
# Tie-out tests on P1 statements.xlsx (USD millions). Tolerance = 1 unit of reported scale (USD 1m) per method step 2.
import openpyxl
PACK = r"C:/Users/aaron/OneDrive/Desktop/Master/WireSift Research/Events/CFA Vancouver Forensic/tests/hertz-fy2013/pack/"
wb = openpyxl.load_workbook(PACK + "statements.xlsx", data_only=True)
TOL = 1.0

def sheet(name):
    ws = wb[name]
    rows = list(ws.iter_rows(values_only=True))
    hdr = rows[0][1:]
    return hdr, {r[0]: dict(zip(hdr, r[1:])) for r in rows[1:] if r[0]}

def extra():
    ws = wb["EXTRA"]
    rows = list(ws.iter_rows(values_only=True))
    hdr = rows[0][3:]
    out = {}
    for r in rows[1:]:
        if r[0]:
            out[(r[0], r[1], r[2])] = dict(zip(hdr, r[3:]))
    return out

fails = []
def check(test, sheet_, line, period, lhs, rhs):
    if lhs is None or rhs is None:
        print(f"  SKIP {test} {sheet_} {period}: missing input")
        return None
    d = round(lhs - rhs, 4)
    ok = abs(d) <= TOL
    print(f"  {'PASS' if ok else 'FAIL'} {test:<34} {sheet_:<5} {period:<10} lhs={lhs:>10.1f} rhs={rhs:>10.1f} diff={d:>8.1f}")
    if not ok:
        fails.append((test, sheet_, line, period, lhs, rhs, d))
    return ok

X = extra()
tle = {k[2]: v for k, v in X.items() if k[0] == "BS" and k[2] == "us-gaap:LiabilitiesAndStockholdersEquity"}
tle = list(tle.values())[0]

for sfx in ["Q", "A"]:
    print(f"== Balance sheet, BS_{sfx}: total assets = total liabilities + total equity")
    hdr, bs = sheet(f"BS_{sfx}")
    for p in hdr:
        ta, tl, te = bs["Total assets"][p], bs["Total liabilities"][p], bs["Total equity"][p]
        check("BS: TA = TL + TE", f"BS_{sfx}", "Total assets", p, ta, (tl or 0) + (te or 0) if tl is not None and te is not None else None)
        check("BS: TL+TE (EXTRA) = TA", f"BS_{sfx}", "Total liabilities and equity", p, ta, tle.get(p))

for sfx in ["Q", "A"]:
    print(f"== Cash flow, CF_{sfx}: CFO + CFI + CFF + FX = net change in cash")
    hdr, cf = sheet(f"CF_{sfx}")
    _, bs = sheet(f"BS_{sfx}")
    for p in hdr:
        parts = [cf[l][p] for l in ["Cash from operations", "Cash from investing", "Cash from financing", "Effect of exchange rates"]]
        s = sum(parts) if all(v is not None for v in parts) else None
        check("CF: sections sum = net change", f"CF_{sfx}", "Net change in cash", p, s, cf["Net change in cash"][p])
    print(f"== Cash flow, CF_{sfx}: net change = change in BS cash")
    bhdr, _ = sheet(f"BS_{sfx}")
    for i, p in enumerate(hdr):
        if i == 0:
            if sfx == "Q":
                prior = sheet("BS_A")[1]["Cash and equivalents"]["FY2010"]  # opening cash for Q1 FY2011 = FY2010 year end
            else:
                print("  SKIP CF: net change = dBS cash CF_A FY2009: no FY2008 balance sheet in P1")
                continue
        else:
            prior = bs["Cash and equivalents"][hdr[i - 1]]
        check("CF: net change = dBS cash", f"CF_{sfx}", "Net change in cash", p, cf["Net change in cash"][p], bs["Cash and equivalents"][p] - prior)

for sfx in ["Q", "A"]:
    print(f"== Income statement, IS_{sfx}: revenue - COGS = gross profit")
    hdr, is_ = sheet(f"IS_{sfx}")
    for p in hdr:
        if is_["Cost of goods sold"][p] is None or is_["Gross profit"][p] is None:
            print(f"  NOT RUNNABLE IS_{sfx} {p}: COGS and gross profit lines blank (no such lines on the face of the statement)")
        else:
            check("IS: Rev - COGS = GP", f"IS_{sfx}", "Gross profit", p, is_["Revenue"][p] - is_["Cost of goods sold"][p], is_["Gross profit"][p])

# Substitute arithmetic check on the IS face (not required by the method; recorded as supplementary):
print("== Income statement supplementary: pre-tax - tax = net income; revenue - total expenses = pre-tax (annual, EXTRA)")
for sfx in ["Q", "A"]:
    hdr, is_ = sheet(f"IS_{sfx}")
    for p in hdr:
        check("IS: PBT - tax = NI", f"IS_{sfx}", "Net income", p, is_["Pre-tax income"][p] - is_["Income tax expense"][p], is_["Net income"][p])
texp = [v for k, v in X.items() if k[2] == "htz:CostAndExpensesIncludingInterestExpense"][0]
hdr, isa = sheet("IS_A")
for p in hdr:
    check("IS: Rev - total expenses = PBT", "IS_A", "Pre-tax income", p, isa["Revenue"][p] - texp[p], isa["Pre-tax income"][p])

print("== Quarters to years: sum of Q1..Q4 = FY for every flow line")
for st in ["IS", "CF"]:
    qh, q = sheet(f"{st}_Q")
    ah, a = sheet(f"{st}_A")
    for line in q:
        for fy in ["FY2011", "FY2012", "FY2013"]:
            qs = [q[line][f"Q{i} {fy}"] for i in range(1, 5)]
            av = a.get(line, {}).get(fy)
            if all(v is None for v in qs) and av is None:
                continue
            if any(v is None for v in qs) or av is None:
                if line in ("Diluted shares", "Diluted EPS"):
                    print(f"  NOT RUN {st} {line} {fy}: Q4 not derived by design (P0) (quarters={qs}, annual={av})")
                else:
                    print(f"  FAIL {st} {line} {fy}: quarters blank where annual exists (quarters={qs}, annual={av})")
                    fails.append((f"Q->Y {line}", f"{st}_Q", line, fy, None, av, None))
                continue
            check(f"Q->Y {line[:24]}", f"{st}_Q", line, fy, sum(qs), av)

print("\nFAILURES:", len(fails))
for f in fails:
    print(" ", f)
```

**search.py**

```python
# Keyword search across every text file listed in the P0 manifest (P2..P299), per method steps 1 and 3 to 7.
import re, os, sys, json
PACK = r"C:/Users/aaron/OneDrive/Desktop/Master/WireSift Research/Events/CFA Vancouver Forensic/tests/hertz-fy2013/pack/"
ids = {}
for l in open(PACK + "manifest.md", encoding="utf-8"):
    m = re.match(r"\| (P\d+) \| ([^|]+?) \|", l)
    if m and m.group(2).endswith(".txt"):
        ids[m.group(2)] = m.group(1)
TERMS = {
 "step1": ["fiscal year end", "change in fiscal year", "53-week", "53 week", "fifty-three", "extra week", "transition period"],
 "step3": ["acquisition", "acquired", "business combination", "purchase price", "divest", "disposal", "sold", "discontinued", "held for sale"],
 "step4": ["adopted", "adoption", "new accounting standard", "recently issued", "change in accounting policy", "change in accounting estimate", "useful life", "reclassif", "recast", "conformed to current", "conform to the current", "segment"],
 "step5": ["restate", "restatement", "revision", "revised", "previously issued", "immaterial error", "correction of an error", "non-reliance", "prior period", "out of period", "out-of-period"],
 "step7": ["material weakness", "significant deficiency", "remediation", "not effective", "going concern", "substantial doubt", "covenant", "waiver", "late filing", "NT 10-K", "12b-25"],
}
def page_of(text, pos):
    ms = list(re.finditer(r"\[p\. (\d+)\]", text[:pos]))
    return ms[-1].group(1) if ms else "pre-p1"
def run(step, files=None):
    out = {}
    for fn, pid in ids.items():
        if files and not re.search(files, fn): continue
        t = open(PACK + fn, encoding="utf-8").read()
        for term in TERMS[step]:
            n = len(re.findall(re.escape(term), t, re.I))
            if n: out.setdefault(term, []).append((pid, n))
    return out
if __name__ == "__main__":
    step = sys.argv[1]
    res = run(step, sys.argv[2] if len(sys.argv) > 2 else None)
    for term in TERMS[step]:
        hits = res.get(term, [])
        print(f"{term!r}: {sum(n for _, n in hits)} hits in {len(hits)} files" + (": " + ", ".join(f"{p}({n})" for p, n in hits[:60]) if hits else ""))
```

**ctx.py**

```python
# Print each hit of a regex in a pack file with its page marker and surrounding text.
import re, sys
from search import PACK, ids, page_of
rev = {v: k for k, v in ids.items()}
pid, pat = sys.argv[1], sys.argv[2]
w = int(sys.argv[3]) if len(sys.argv) > 3 else 400
t = open(PACK + rev[pid], encoding="utf-8").read()
last = -10**9
for m in re.finditer(pat, t, re.I):
    if m.start() - last < w: continue
    last = m.start()
    print(f"--- {pid} {rev[pid]} p.{page_of(t, m.start())} @{m.start()}")
    print(t[max(0, m.start() - w): m.end() + w].replace("\n", " / "))
```

**calc.py**

```python
# F1 calculations. Workbook values are read from P1; text values are copied with their locator in the comment.
import openpyxl, statistics
from datetime import date
PACK = r"C:/Users/aaron/OneDrive/Desktop/Master/WireSift Research/Events/CFA Vancouver Forensic/tests/hertz-fy2013/pack/"
wb = openpyxl.load_workbook(PACK + "statements.xlsx", data_only=True)
def sheet(name):
    rows = list(wb[name].iter_rows(values_only=True)); hdr = rows[0][1:]
    return {r[0]: dict(zip(hdr, r[1:])) for r in rows[1:] if r[0]}
IS_A, IS_Q, BS_A, CF_A, CF_Q = sheet("IS_A"), sheet("IS_Q"), sheet("BS_A"), sheet("CF_A"), sheet("CF_Q")
r = lambda x: round(x, 1)

print("C1 Cash tie-out failure FY2013 / Q4 FY2013 explained by revised FY2012 cash")
rest = [row for row in wb["RESTATED"].iter_rows(min_row=2, values_only=True)]
cash12_rev = [x for x in rest if x[0] == "BS" and x[1] == "Cash and equivalents" and x[2] == "FY2012"][0][4]
print("  FY2012 cash as reprinted in FY2013 10-K:", cash12_rev)
print("  BS change using reprinted opening:", r(BS_A["Cash and equivalents"]["FY2013"] - cash12_rev), "vs CF net change", CF_A["Net change in cash"]["FY2013"])
q13 = sum(CF_Q["Net change in cash"][f"Q{i} FY2013"] for i in (1, 2, 3))
print("  Q1-Q3 FY2013 net change (from original 533.3 opening) sum:", r(q13), "; Q3 FY2013 closing 548.7 minus 533.3 =", r(548.7 - 533.3))

print("C2 RESTATED sheet: lines differing by more than 1 (USD m)")
big = [(x[0], x[1], x[2], x[3], x[4], r(x[4] - x[3])) for x in rest if abs(x[4] - x[3]) > 1.0]
for b in big: print("  ", b)
print("  count >1:", len(big), "| by year:", {y: sum(1 for b in big if b[2] == y) for y in ["FY2010", "FY2011", "FY2012"]})
small = [(x[1], x[2], r(x[4] - x[3])) for x in rest if 0 < abs(x[4] - x[3]) <= 1.0]
print("  nonzero but <=1:", small)

print("C3 FY2011 as reprinted in the FY2013 10-K (P66 p.76) vs as originally reported (P1 IS_A)")
fy11_rev = {"Revenue": 8299.3, "Selling, general and administrative": 767.7, "Pre-tax income": 305.6, "Net income": 183.8}  # P66, p.76
for k, v in fy11_rev.items(): print("  ", k, IS_A[k]["FY2011"], "->", v, "diff", r(v - IS_A[k]["FY2011"]))
print("   Direct operating 4566.4 -> 4573.1 diff", r(4573.1 - 4566.4), "| Dep of REE and lease charges 1905.7 -> 1896.2 diff", r(1896.2 - 1905.7))  # P66 p.76; P1 EXTRA orig

print("C4 Quarterly revenue and pre-tax: workbook (as originally reported) vs as revised in FY2013 10-K (P68 pp.85-89; P84 p.149)")
rev_q = {"Q1 FY2012": (1961.7, -36.7), "Q2 FY2012": (2226.2, 148.0), "Q3 FY2012": (2517.2, 373.1), "Q4 FY2012": (2319.7, -43.1),
         "Q1 FY2013": (2436.9, 73.7), "Q2 FY2013": (2709.2, 205.9), "Q3 FY2013": (3069.4, 321.3), "Q4 FY2013": (2556.4, 62.3)}
for q, (rv, pt) in rev_q.items():
    print(f"   {q}: revenue {IS_Q['Revenue'][q]} vs {rv} diff {r(rv - IS_Q['Revenue'][q])}; pre-tax {IS_Q['Pre-tax income'][q]} vs {pt} diff {r(pt - IS_Q['Pre-tax income'][q])}")
q4d_rev = IS_A["Revenue"]["FY2013"] - sum(IS_Q["Revenue"][f"Q{i} FY2013"] for i in (1, 2, 3))
q4d_pt = IS_A["Pre-tax income"]["FY2013"] - sum(IS_Q["Pre-tax income"][f"Q{i} FY2013"] for i in (1, 2, 3))
print("   Q4 FY2013 derived (FY2013 minus Q1-Q3 as originally reported): revenue", r(q4d_rev), "pre-tax", r(q4d_pt))
print("   derived Q4 minus revised Q4 (P84):", r(q4d_rev - 2556.4), r(q4d_pt - 62.3), "| 9M 2013 adjustments per P68 p.87: revenue -5.0, pre-tax -11.6")

print("C5 Revision components (P68 p.83): prior-period pre-tax effect")
comp = {"vendor 2011": 12.9, "vendor 2012": 2.4, "Brazil 2010": 4.4, "Brazil 2011": 6.2, "Brazil 2012": 3.6, "other 2010": 2.4, "other 2012": 3.2, "other 2011": -0.4}
print("   sum of components:", r(sum(comp.values())), "| stated prior-period amount 34.7")
print("   by year 2010/2011/2012:", r(4.4 + 2.4), r(12.9 + 6.2 - 0.4), r(2.4 + 3.6 + 3.2))
print("   total errors 46.3 minus prior-period 34.7 =", r(46.3 - 34.7), "| ER-Q4-FY2013 total 47.9 minus 10-K total 46.3 =", r(47.9 - 46.3))
print("   FY2011 NI revision -12.0 as % of FY2011 NI as originally reported:", r(-12.0 / IS_A['Net income']['FY2011'] * 100), "%")
print("   FY2012 NI revision -4.5 as % of FY2012 NI as originally reported:", r(-4.5 / IS_A['Net income']['FY2012'] * 100), "%")
print("   FY2011 pre-tax revision -18.7 as % of FY2011 pre-tax as originally reported:", r(-18.7 / IS_A['Pre-tax income']['FY2011'] * 100), "%")
print("   FY2012 pre-tax revision -9.2 as % of FY2012 pre-tax as originally reported:", r(-9.2 / IS_A['Pre-tax income']['FY2012'] * 100), "%")

print("C6 Q3 2011 revision of FY2009/FY2010 (P131 p.7; P11 p.92)")
print("   FY2010 NI attributable -48.0 -> -48.7: diff", r(-48.680 - -48.044))
print("   FY2009 NI attributable -126.0 -> -129.5: diff", r(-129.528 - -126.022))
print("   FY2009 BS revised (P131): TA 16002.4->16015.1", r(16015.1 - 16002.4), "TL 13905.0->13929.9", r(13929.9 - 13905.0), "TE 2097.4->2087.2", r(2087.2 - 2097.4))
print("   FY2009 BS in P1 BS_A: TA", BS_A["Total assets"]["FY2009"], "TE", BS_A["Total equity"]["FY2009"])
print("   2009 direct operating adjustment: Q3 2011 10-Q 6,300k vs FY2011 10-K 2,634k; diff (USD m):", r((6300 - 2634) / 1000))

print("C7 Revenue by business line: FY2012 as originally reported (P1 EXTRA) vs as recast in FY2013 10-K (P66 p.76)")
hdrx = [c.value for c in wb["EXTRA"][1]][3:]
ex = {row[2]: dict(zip(hdrx, row[3:])) for row in wb["EXTRA"].iter_rows(min_row=2, values_only=True) if row[0] == "IS"}
orig = {"car": ex["htz:RevenueCarRental"]["FY2012"], "equip": ex["htz:RevenueEquipmentRental"]["FY2012"], "other": ex["us-gaap:OtherSalesRevenueNet"]["FY2012"]}
recast = {"car": 7161.7, "equip": 1385.4, "other": 477.8}
for k in orig: print("  ", k, orig[k], "->", recast[k], "diff", r(recast[k] - orig[k]))
print("   total diff", r(sum(recast.values()) - sum(orig.values())))
print("   Quarterly 'Other' revenue FY2013 (P1 EXTRA):", [ex["us-gaap:OtherSalesRevenueNet"][f"Q{i} FY2013"] for i in (1, 2, 3, 4)])
print("   Q2 2012 as reprinted in Q2 2013 10-Q (P227 p.3): car 1889.6 vs orig", ex["htz:RevenueCarRental"]["Q2 FY2012"], "diff", r(1889.6 - ex["htz:RevenueCarRental"]["Q2 FY2012"]),
      "; other 0.5 vs orig", ex["us-gaap:OtherSalesRevenueNet"]["Q2 FY2012"], "diff", r(0.5 - ex["us-gaap:OtherSalesRevenueNet"]["Q2 FY2012"]))

print("C8 Depreciation-rate changes (P74 p.126 vs P45 p.113, P16 p.125)")
print("   2012: US -139.4 + intl 8.8 =", r(-139.4 + 8.8), "vs FY2012 10-K car rental net -130.6")
print("   2011: US -26.7 + intl 12.9 =", r(-26.7 + 12.9), "vs FY2011 10-K car rental net -13.8")
print("   2013 car rental net: US -44.2 + intl 5.0 =", r(-44.2 + 5.0))
print("   2012 car rental rate change as % of FY2012 pre-tax as originally reported:", r(-130.6 / IS_A['Pre-tax income']['FY2012'] * 100), "%")

print("C9 Acquisitions")
print("   Dollar Thrifty days owned in FY2012 (2012-11-19 to 2012-12-31, inclusive):", (date(2012, 12, 31) - date(2012, 11, 19)).days + 1)
print("   DT revenue 170.6 as % of FY2012 revenue as originally reported:", r(170.6 / IS_A['Revenue']['FY2012'] * 100), "%")
print("   DT PPA preliminary (P41 p.88) -> final (P70 p.98): goodwill", r(889 - 885.0), "intangibles", r(1545 - 1546.0), "accrued liab", r(-298 - -277.0), "deferred tax", r(-846 - -864.0))
print("   Donlen days owned in FY2011 (2011-09-01 to 2011-12-31, inclusive):", (date(2011, 12, 31) - date(2011, 9, 1)).days + 1)
print("   Donlen revenue 142.7 as % of FY2011 revenue:", r(142.7 / IS_A['Revenue']['FY2011'] * 100), "%")
print("   Goodwill FY2011->FY2012 (P1 BS_A):", r(BS_A["Goodwill"]["FY2012"] - BS_A["Goodwill"]["FY2011"]), "| intangibles:", r(BS_A["Intangible assets, net"]["FY2012"] - BS_A["Intangible assets, net"]["FY2011"]))
print("   Total assets FY2011->FY2012 change:", r(BS_A["Total assets"]["FY2012"] - BS_A["Total assets"]["FY2011"]))

print("C10 Filing timing (dates from P0 manifest)")
for fy, d in [(2011, date(2012, 2, 27)), (2012, date(2013, 3, 4)), (2013, date(2014, 3, 19))]:
    print(f"   FY{fy} 10-K filed {d}: days after year end", (d - date(fy, 12, 31)).days)
for fy, d in [(2010, date(2011, 2, 23)), (2011, date(2012, 2, 22)), (2012, date(2013, 2, 25)), (2013, date(2014, 3, 18))]:
    print(f"   Q4 FY{fy} earnings release 8-K filed {d}: days after year end", (d - date(fy, 12, 31)).days)

print("C11 Allowance: Schedule II opening vs prior closing as originally reported (P1 NOTES)")
N = sheet("NOTES")
for a, b in [("FY2013", "FY2012"), ("FY2012", "FY2011"), ("FY2011", "FY2010")]:
    print(f"   opening {a}", N["Allowance: opening"][a], f"closing {b}", N["Allowance: closing"][b], "diff", r(N["Allowance: opening"][a] - N["Allowance: closing"][b]))

print("C12 Scale scan: any nonzero cell more than 300x above or below the median absolute value of its row (P1)")
for name in ["IS_Q", "IS_A", "BS_Q", "BS_A", "CF_Q", "CF_A", "EXTRA"]:
    ws = wb[name]; rows = list(ws.iter_rows(values_only=True)); hdr = rows[0]
    off = 3 if name == "EXTRA" else 1
    for row in rows[1:]:
        vals = [(hdr[i], v) for i, v in enumerate(row) if i >= off and isinstance(v, (int, float)) and v != 0]
        if len(vals) < 3: continue
        med = statistics.median(abs(v) for _, v in vals)
        for h, v in vals:
            if med and (abs(v) / med > 300 or abs(v) / med < 1 / 300):
                print(f"   {name} | {row[1] if name == 'EXTRA' else row[0]} | {h} | {v} (row median {med})")

print("C13 Stock repurchased: annual vs quarters (P1 CF_A, CF_Q)")
print("   FY2013 annual", CF_A["Stock repurchased"]["FY2013"], "| Q4 derived", CF_Q["Stock repurchased"]["Q4 FY2013"],
      "| implied Q1-Q3 total =", r(CF_A["Stock repurchased"]["FY2013"] - CF_Q["Stock repurchased"]["Q4 FY2013"]))

print("C14 FY2011 cash flow as reprinted in the FY2013 10-K (P66 pp.80-81) vs as originally reported (P1 CF_A)")
fy11_cf = {"Cash from operations": 2211.1, "Cash from investing": -2170.6}  # P66 p.80
for k, v in fy11_cf.items(): print("  ", k, CF_A[k]["FY2011"], "->", v, "diff", r(v - CF_A[k]["FY2011"]))
print("   FY2012 restricted cash change: orig (P1 EXTRA)", -261.6, "-> reprinted (P66 p.80)", -241.6, "diff", r(-241.6 - -261.6))

print("C15 Sign check: revolver proceeds FY2013, P1 EXTRA vs P66 p.81")
hdrx = [c.value for c in wb["EXTRA"][1]][3:]
exc = {row[2]: dict(zip(hdrx, row[3:])) for row in wb["EXTRA"].iter_rows(min_row=2, values_only=True) if row[0] == "CF"}
v = exc["us-gaap:ProceedsFromLinesOfCredit"]["FY2013"]
print("   P1 EXTRA:", v, "| P66 text: 9511.6 | sum with P1 EXTRA", r(v + 9511.6))
print("   Purchase of treasury shares row (P1 EXTRA) Q1/Q2 FY2013:", exc["us-gaap:TreasuryStockValueAcquiredParValueMethod"]["Q1 FY2013"], exc["us-gaap:TreasuryStockValueAcquiredParValueMethod"]["Q2 FY2013"])
```

**inventory.py**

```python
# Pack inventory: every file listed in P0, opened and checked for content.
import re, os, openpyxl
PACK = r"C:/Users/aaron/OneDrive/Desktop/Master/WireSift Research/Events/CFA Vancouver Forensic/tests/hertz-fy2013/pack/"
rows = []
for l in open(PACK + "manifest.md", encoding="utf-8"):
    m = re.match(r"\| (P\d+) \| ([^|]+?) \| ([^|]*?) \| ([^|]*?) \|", l)
    if m: rows.append(m.groups())
status = {}
for pid, fn, what, per in rows:
    p = PACK + fn
    try:
        if fn.endswith(".xlsx"):
            wb = openpyxl.load_workbook(p, data_only=True); ok = f"opened ({len(wb.sheetnames)} sheets: {', '.join(wb.sheetnames)})"
        else:
            t = open(p, encoding="utf-8").read(); ok = "opened" if len(t) > 0 else "EMPTY"
    except Exception as e:
        ok = f"FAILED: {e}"
    status[pid] = ok
print("files listed in manifest:", len(rows), "| opened:", sum(1 for v in status.values() if v.startswith("opened")))
# group by source filing prefix
groups = {}
for pid, fn, what, per in rows:
    key = fn.split("_")[0] if "_" in fn else fn
    groups.setdefault(key, []).append((pid, fn))
for k, v in groups.items():
    print(f"| {k} | {v[0][0]} to {v[-1][0]} | {len(v)} | " + "; ".join(f"{p} {f.split('_',1)[-1] if '_' in f else f}" for p, f in v) + " | " + ("all opened" if all(status[p].startswith("opened") for p, _ in v) else "SEE STATUS") + " |")
print(status["P1"])
```

**assemble.py**

```python
# Assemble F1-output.md: insert code, count figures by mark, write context sheet and ledger CSV.
import re, os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = r"C:/Users/aaron/OneDrive/Desktop/Master/WireSift Research/Events/CFA Vancouver Forensic/tests/hertz-fy2013/runs/v0.2-claude-code/"
os.makedirs(OUT, exist_ok=True)
draft = open(os.path.join(HERE, "draft.md"), encoding="utf-8").read()

# Figure count (heuristic): numeric tokens with a decimal point, a thousands comma or a percent sign,
# outside code blocks and the CSV. Each token is attributed to the next mark on its line (or the last mark
# if none follows): a mark that is only [calc ...] counts as calculated; any mark naming a pack file counts
# as copied. [unverified] marks are counted separately.
body = re.sub(r"```.*?```", "", draft, flags=re.S)
tok = re.compile(r"(?<![\w.])\(?-?\d{1,3}(?:,\d{3})+(?:\.\d+)?%?\)?|(?<![\w.])\(?-?\d+\.\d+%?\)?|(?<![\w.])\d+%")
copied = calc = 0
mark = re.compile(r"\[[^\]]*\]")
for line in body.splitlines():
    # numbers before a mark belong to that mark; a mark naming a pack file (P0..P299) counts as copied,
    # a mark that is only [calc ...] counts as calculated; numbers after the last mark take the last mark's type
    pos, last = 0, None
    segs = []
    for m in mark.finditer(line):
        segs.append((line[pos:m.start()], m.group(0))); pos = m.end(); last = m.group(0)
    segs.append((line[pos:], last))
    for text, mk in segs:
        n = len(tok.findall(text))
        if mk and mk.startswith("[calc") and not re.search(r"P\d", mk):
            calc += n
        else:
            copied += n
unver = body.count("[unverified")
print("figures copied:", copied, "calculated:", calc, "unverified:", unver)

scripts = ["tieout.py", "search.py", "ctx.py", "calc.py", "inventory.py", "assemble.py"]
code = ["Scripts in the order they were first run. All read only the pack files. Python 3 with openpyxl.\n"]
for s in scripts:
    code.append(f"**{s}**\n\n```python\n" + open(os.path.join(HERE, s), encoding="utf-8").read().rstrip() + "\n```\n")
code.append("""**Read-only inspection commands** (run between the scripts to read pack text; they print text and compute no figures). Representative forms:

```bash
python ctx.py P68 "immaterial error|out of period|revision|previously issued" 1500   # FY2013 Note 2 correction text
python ctx.py P11 "revised|previously issued|reclassif|adopt" 700                      # FY2011 Note 2 revision
python ctx.py P295 "immaterial error|out of period|revis|delay|postpone|restat" 600    # Q4 2013 release
python ctx.py P71 / P85 (HVF II amortization event, subsequent events); P8, P36, P65 (auditor reports); P28, P57, P87 (Item 9A)
python -c "...read AR-FY2013_notes-04..., AR-FY2012_notes-04..., Q1/Q2/Q3-FY2013_notes-05... business combinations"
python -c "...print STATEMENTS OF OPERATIONS revenue lines from Q1/Q2/Q3-FY2013 and Q3-FY2012 financial-statements files"
grep -h -i "repurchase|treasury" Q2-FY2013_financial-statements.txt Q3-FY2013_financial-statements.txt
grep -c -i "revis|error|emphasi|explanatory|going concern|served as|since [0-9]" AR-FY20xx_auditor-report.txt
python -c "...openpyxl: print IS_A, BS_A, CF_A, NOTES, EXTRA, RESTATED, LOCATORS rows"
```
""")
code.append("**Output of inventory.py** (every manifest file, grouped by source filing):\n\n```\n" + open(os.path.join(HERE, "inventory.out"), encoding="utf-8").read().rstrip() + "\n```\n")
code.append("**Output of calc.py**\n\n```\n" + open(os.path.join(HERE, "calc.out"), encoding="utf-8").read().rstrip() + "\n```\n")
code.append("**Output of search.py** (hit counts per term, all text files P2 to P299)\n\n```\n" + "\n".join(l[:160] for l in open(os.path.join(HERE, "search.out"), encoding="utf-8").read().splitlines()) + "\n```\n")

items_run = 8
ledger = re.findall(r"^\| F1-[CE]\d+-\d+ \|.*\| (P\d) \| \|$", draft, flags=re.M)
could_not = len(re.findall(r"^\d+\. ", draft.split("## 9. Could not run")[1].split("## 10.")[0], flags=re.M))
pc = {p: ledger.count(p) for p in ["P1", "P2", "P3", "P4"]}
verify = (f"`Verification: {items_run} items run, {len(ledger)} ledger rows (P1 {pc['P1']}, P2 {pc['P2']}, P3 {pc['P3']}, P4 {pc['P4']}), "
          f"{could_not} could not run. Figures: {copied} copied, {calc} calculated, {unver} unverified. Units: USD, millions (P1; text files in their own units). "
          f"Framework: US GAAP. Context sheet: produced by this step (F1 is its source, not a consumer).`\n\n"
          "Items run = the eight method steps. Figure counts are a script count of numeric tokens by the mark on their line (see assemble.py), so they are approximate.")
final = draft.replace("{{VERIFY}}", verify).replace("{{CODE}}", "\n".join(code))
open(OUT + "F1-output.md", "w", encoding="utf-8").write(final)

# Context sheet = everything before section 8
ctx = final.split("## 8. Looked for and not found")[0].rstrip() + "\n"
open(OUT + "context-sheet.md", "w", encoding="utf-8").write(ctx)
csv = re.search(r"```csv\n(.*?)```", final, flags=re.S).group(1)
open(OUT + "ledger-F1.csv", "w", encoding="utf-8", newline="").write(csv)
print("ledger rows:", len(ledger), pc, "could not run:", could_not)
print("chars:", len(final), "words:", len(final.split()), "context-sheet words:", len(ctx.split()))
```

**Read-only inspection commands** (run between the scripts to read pack text; they print text and compute no figures). Representative forms:

```bash
python ctx.py P68 "immaterial error|out of period|revision|previously issued" 1500   # FY2013 Note 2 correction text
python ctx.py P11 "revised|previously issued|reclassif|adopt" 700                      # FY2011 Note 2 revision
python ctx.py P295 "immaterial error|out of period|revis|delay|postpone|restat" 600    # Q4 2013 release
python ctx.py P71 / P85 (HVF II amortization event, subsequent events); P8, P36, P65 (auditor reports); P28, P57, P87 (Item 9A)
python -c "...read AR-FY2013_notes-04..., AR-FY2012_notes-04..., Q1/Q2/Q3-FY2013_notes-05... business combinations"
python -c "...print STATEMENTS OF OPERATIONS revenue lines from Q1/Q2/Q3-FY2013 and Q3-FY2012 financial-statements files"
grep -h -i "repurchase|treasury" Q2-FY2013_financial-statements.txt Q3-FY2013_financial-statements.txt
grep -c -i "revis|error|emphasi|explanatory|going concern|served as|since [0-9]" AR-FY20xx_auditor-report.txt
python -c "...openpyxl: print IS_A, BS_A, CF_A, NOTES, EXTRA, RESTATED, LOCATORS rows"
```

**Output of inventory.py** (every manifest file, grouped by source filing):

```
files listed in manifest: 299 | opened: 299
| statements.xlsx | P1 to P1 | 1 | P1 statements.xlsx | all opened |
| AR-FY2011 | P2 to P29 | 28 | P2 business.txt; P3 risk-factors.txt; P4 legal.txt; P5 mdna.txt; P6 critical-estimates.txt; P7 market-risk.txt; P8 auditor-report.txt; P9 financial-statements.txt; P10 notes-01-background.txt; P11 notes-02-summary-of-significant-accounting-policies.txt; P12 notes-03-goodwill-and-other-intangible-assets.txt; P13 notes-04-debt.txt; P14 notes-05-employee-retirement-benefits.txt; P15 notes-06-stock-based-compensation.txt; P16 notes-07-depreciation-of-revenue-earning-equipment-and.txt; P17 notes-08-taxes-on-income.txt; P18 notes-09-lease-and-concession-agreements.txt; P19 notes-10-segment-information.txt; P20 notes-11-contingencies-and-off-balance-sheet-commitments.txt; P21 notes-12-restructuring.txt; P22 notes-13-financial-instruments.txt; P23 notes-14-related-party-transactions.txt; P24 notes-15-earnings-loss-per-share.txt; P25 notes-16-quarterly-financial-information-unaudited.txt; P26 notes-17-subsequent-events.txt; P27 schedule-ii.txt; P28 controls.txt; P29 related-parties.txt | all opened |
| AR-FY2012 | P30 to P58 | 29 | P30 business.txt; P31 risk-factors.txt; P32 legal.txt; P33 mdna.txt; P34 critical-estimates.txt; P35 market-risk.txt; P36 auditor-report.txt; P37 financial-statements.txt; P38 notes-01-background.txt; P39 notes-02-summary-of-significant-accounting-policies.txt; P40 notes-03-goodwill-and-other-intangible-assets.txt; P41 notes-04-business-combinations-and-divestitures.txt; P42 notes-05-debt.txt; P43 notes-06-employee-retirement-benefits.txt; P44 notes-07-stock-based-compensation.txt; P45 notes-08-depreciation-of-revenue-earning-equipment-and.txt; P46 notes-09-taxes-on-income.txt; P47 notes-10-lease-and-concession-agreements.txt; P48 notes-11-segment-information.txt; P49 notes-12-contingencies-and-off-balance-sheet-commitments.txt; P50 notes-13-restructuring.txt; P51 notes-14-financial-instruments.txt; P52 notes-15-related-party-transactions.txt; P53 notes-16-earnings-per-share.txt; P54 notes-17-quarterly-financial-information-unaudited.txt; P55 notes-18-subsequent-events.txt; P56 schedule-ii.txt; P57 controls.txt; P58 related-parties.txt | all opened |
| AR-FY2013 | P59 to P88 | 30 | P59 business.txt; P60 risk-factors.txt; P61 legal.txt; P62 mdna.txt; P63 critical-estimates.txt; P64 market-risk.txt; P65 auditor-report.txt; P66 financial-statements.txt; P67 notes-01-background.txt; P68 notes-02-summary-of-significant-accounting-policies.txt; P69 notes-03-goodwill-and-other-intangible-assets.txt; P70 notes-04-business-combinations-and-divestitures.txt; P71 notes-05-debt.txt; P72 notes-06-employee-retirement-benefits.txt; P73 notes-07-stock-based-compensation.txt; P74 notes-08-depreciation-of-revenue-earning-equipment-and.txt; P75 notes-09-taxes-on-income.txt; P76 notes-10-lease-and-concession-agreements.txt; P77 notes-11-segment-information.txt; P78 notes-12-accumulated-other-comprehensive-income-loss.txt; P79 notes-13-contingencies-and-off-balance-sheet-commitments.txt; P80 notes-14-restructuring.txt; P81 notes-15-financial-instruments-and-fair-value.txt; P82 notes-16-related-party-transactions.txt; P83 notes-17-earnings-per-share.txt; P84 notes-18-quarterly-financial-information-unaudited.txt; P85 notes-19-subsequent-events.txt; P86 schedule-ii.txt; P87 controls.txt; P88 related-parties.txt | all opened |
| Q1-FY2011 | P89 to P108 | 20 | P89 financial-statements.txt; P90 notes-01-background.txt; P91 notes-02-basis-of-presentation.txt; P92 notes-03-cash-and-cash-equivalents-and-restricted-cash.txt; P93 notes-04-goodwill-and-other-intangible-assets.txt; P94 notes-05-taxes-on-income.txt; P95 notes-06-depreciation-of-revenue-earning-equipment-and.txt; P96 notes-07-debt.txt; P97 notes-08-employee-retirement-benefits.txt; P98 notes-09-stock-based-compensation.txt; P99 notes-10-segment-information.txt; P100 notes-11-total-equity.txt; P101 notes-12-restructuring.txt; P102 notes-13-financial-instruments.txt; P103 notes-14-related-party-transactions.txt; P104 notes-15-contingencies-and-off-balance-sheet-commitments.txt; P105 notes-16-earnings-loss-per-share.txt; P106 notes-17-subsequent-events.txt; P107 mdna.txt; P108 risk-factors.txt | all opened |
| Q2-FY2011 | P109 to P128 | 20 | P109 financial-statements.txt; P110 notes-01-background.txt; P111 notes-02-basis-of-presentation.txt; P112 notes-03-cash-and-cash-equivalents-and-restricted-cash.txt; P113 notes-04-goodwill-and-other-intangible-assets.txt; P114 notes-05-taxes-on-income.txt; P115 notes-06-depreciation-of-revenue-earning-equipment-and.txt; P116 notes-07-debt.txt; P117 notes-08-employee-retirement-benefits.txt; P118 notes-09-stock-based-compensation.txt; P119 notes-10-segment-information.txt; P120 notes-11-total-equity.txt; P121 notes-12-restructuring.txt; P122 notes-13-financial-instruments.txt; P123 notes-14-related-party-transactions.txt; P124 notes-15-contingencies-and-off-balance-sheet-commitments.txt; P125 notes-16-earnings-loss-per-share.txt; P126 notes-17-subsequent-events.txt; P127 mdna.txt; P128 risk-factors.txt | all opened |
| Q3-FY2011 | P129 to P147 | 19 | P129 financial-statements.txt; P130 notes-01-background.txt; P131 notes-02-basis-of-presentation-and-recently-issued.txt; P132 notes-03-cash-and-cash-equivalents-and-restricted-cash.txt; P133 notes-04-goodwill-and-other-intangible-assets.txt; P134 notes-05-taxes-on-income.txt; P135 notes-06-depreciation-of-revenue-earning-equipment-and.txt; P136 notes-07-debt.txt; P137 notes-08-employee-retirement-benefits.txt; P138 notes-09-stock-based-compensation.txt; P139 notes-10-segment-information.txt; P140 notes-11-total-equity.txt; P141 notes-12-restructuring.txt; P142 notes-13-financial-instruments.txt; P143 notes-14-related-party-transactions.txt; P144 notes-15-contingencies-and-off-balance-sheet-commitments.txt; P145 notes-16-earnings-loss-per-share.txt; P146 mdna.txt; P147 risk-factors.txt | all opened |
| Q1-FY2012 | P148 to P166 | 19 | P148 financial-statements.txt; P149 notes-01-background.txt; P150 notes-02-basis-of-presentation-and-recently-issued.txt; P151 notes-03-cash-and-cash-equivalents-and-restricted-cash.txt; P152 notes-04-goodwill-and-other-intangible-assets.txt; P153 notes-05-taxes-on-income.txt; P154 notes-06-depreciation-of-revenue-earning-equipment-and.txt; P155 notes-07-debt.txt; P156 notes-08-employee-retirement-benefits.txt; P157 notes-09-stock-based-compensation.txt; P158 notes-10-segment-information.txt; P159 notes-11-total-equity.txt; P160 notes-12-restructuring.txt; P161 notes-13-financial-instruments.txt; P162 notes-14-related-party-transactions.txt; P163 notes-15-contingencies-and-off-balance-sheet-commitments.txt; P164 notes-16-earnings-loss-per-share.txt; P165 notes-17-subsequent-events.txt; P166 mdna.txt | all opened |
| Q2-FY2012 | P167 to P185 | 19 | P167 financial-statements.txt; P168 notes-01-background.txt; P169 notes-02-basis-of-presentation-and-recently-issued.txt; P170 notes-03-cash-and-cash-equivalents-and-restricted-cash.txt; P171 notes-04-goodwill-and-other-intangible-assets.txt; P172 notes-05-taxes-on-income.txt; P173 notes-06-depreciation-of-revenue-earning-equipment-and.txt; P174 notes-07-debt.txt; P175 notes-08-employee-retirement-benefits.txt; P176 notes-09-stock-based-compensation.txt; P177 notes-10-segment-information.txt; P178 notes-11-total-equity.txt; P179 notes-12-restructuring.txt; P180 notes-13-financial-instruments.txt; P181 notes-14-related-party-transactions.txt; P182 notes-15-contingencies-and-off-balance-sheet-commitments.txt; P183 notes-16-earnings-loss-per-share.txt; P184 notes-17-subsequent-events.txt; P185 mdna.txt | all opened |
| Q3-FY2012 | P186 to P205 | 20 | P186 financial-statements.txt; P187 notes-01-background.txt; P188 notes-02-basis-of-presentation-and-recently-issued.txt; P189 notes-03-cash-and-cash-equivalents-and-restricted-cash.txt; P190 notes-04-goodwill-and-other-intangible-assets.txt; P191 notes-05-taxes-on-income.txt; P192 notes-06-depreciation-of-revenue-earning-equipment-and.txt; P193 notes-07-debt.txt; P194 notes-08-employee-retirement-benefits.txt; P195 notes-09-stock-based-compensation.txt; P196 notes-10-segment-information.txt; P197 notes-11-total-equity.txt; P198 notes-12-restructuring.txt; P199 notes-13-financial-instruments.txt; P200 notes-14-related-party-transactions.txt; P201 notes-15-contingencies-and-off-balance-sheet-commitments.txt; P202 notes-16-earnings-per-share.txt; P203 notes-17-subsequent-events.txt; P204 mdna.txt; P205 risk-factors.txt | all opened |
| Q1-FY2013 | P206 to P226 | 21 | P206 financial-statements.txt; P207 notes-01-background.txt; P208 notes-02-basis-of-presentation-and-recently-issued.txt; P209 notes-03-cash-and-cash-equivalents-and-restricted-cash.txt; P210 notes-04-goodwill-and-other-intangible-assets.txt; P211 notes-05-business-combinations-and-divestitures.txt; P212 notes-06-taxes-on-income.txt; P213 notes-07-depreciation-of-revenue-earning-equipment-and.txt; P214 notes-08-debt.txt; P215 notes-09-employee-retirement-benefits.txt; P216 notes-10-stock-based-compensation.txt; P217 notes-11-segment-information.txt; P218 notes-12-other-comprehensive-income-loss.txt; P219 notes-13-restructuring.txt; P220 notes-14-financial-instruments.txt; P221 notes-15-related-party-transactions.txt; P222 notes-16-contingencies-and-off-balance-sheet-commitments.txt; P223 notes-17-earnings-loss-per-share.txt; P224 notes-18-subsequent-events.txt; P225 mdna.txt; P226 risk-factors.txt | all opened |
| Q2-FY2013 | P227 to P246 | 20 | P227 financial-statements.txt; P228 notes-01-background.txt; P229 notes-02-basis-of-presentation-and-recently-issued.txt; P230 notes-03-cash-and-cash-equivalents-and-restricted-cash.txt; P231 notes-04-goodwill-and-other-intangible-assets.txt; P232 notes-05-business-combinations-and-divestitures.txt; P233 notes-06-taxes-on-income.txt; P234 notes-07-depreciation-of-revenue-earning-equipment-and.txt; P235 notes-08-debt.txt; P236 notes-09-employee-retirement-benefits.txt; P237 notes-10-stock-based-compensation.txt; P238 notes-11-segment-information.txt; P239 notes-12-accumulated-other-comprehensive-loss.txt; P240 notes-13-restructuring.txt; P241 notes-14-financial-instruments.txt; P242 notes-15-related-party-transactions.txt; P243 notes-16-contingencies-and-off-balance-sheet-commitments.txt; P244 notes-17-earnings-per-share.txt; P245 notes-18-subsequent-events.txt; P246 mdna.txt | all opened |
| Q3-FY2013 | P247 to P267 | 21 | P247 financial-statements.txt; P248 notes-01-background.txt; P249 notes-02-basis-of-presentation-and-recently-issued.txt; P250 notes-03-cash-and-cash-equivalents-and-restricted-cash.txt; P251 notes-04-goodwill-and-other-intangible-assets.txt; P252 notes-05-business-combinations-and-divestitures.txt; P253 notes-06-taxes-on-income.txt; P254 notes-07-depreciation-of-revenue-earning-equipment-and.txt; P255 notes-08-debt.txt; P256 notes-09-employee-retirement-benefits.txt; P257 notes-10-stock-based-compensation.txt; P258 notes-11-segment-information.txt; P259 notes-12-accumulated-other-comprehensive-loss.txt; P260 notes-13-restructuring.txt; P261 notes-14-financial-instruments-and-fair-value.txt; P262 notes-15-related-party-transactions.txt; P263 notes-16-contingencies-and-off-balance-sheet-commitments.txt; P264 notes-17-earnings-per-share.txt; P265 notes-18-subsequent-events.txt; P266 mdna.txt; P267 risk-factors.txt | all opened |
| releases/OTHER-2011-01-25.txt | P268 to P268 | 1 | P268 releases/OTHER-2011-01-25.txt | all opened |
| releases/ER-Q4-FY2010.txt | P269 to P269 | 1 | P269 releases/ER-Q4-FY2010.txt | all opened |
| releases/OTHER-2011-02-25.txt | P270 to P270 | 1 | P270 releases/OTHER-2011-02-25.txt | all opened |
| releases/ER-Q1-FY2011.txt | P271 to P271 | 1 | P271 releases/ER-Q1-FY2011.txt | all opened |
| releases/OTHER-2011-05-02.txt | P272 to P272 | 1 | P272 releases/OTHER-2011-05-02.txt | all opened |
| releases/ER-Q2-FY2011.txt | P273 to P273 | 1 | P273 releases/ER-Q2-FY2011.txt | all opened |
| releases/OTHER-2011-08-08.txt | P274 to P274 | 1 | P274 releases/OTHER-2011-08-08.txt | all opened |
| releases/ER-Q3-FY2011.txt | P275 to P275 | 1 | P275 releases/ER-Q3-FY2011.txt | all opened |
| releases/OTHER-2011-11-07.txt | P276 to P276 | 1 | P276 releases/OTHER-2011-11-07.txt | all opened |
| releases/ER-Q4-FY2011.txt | P277 to P277 | 1 | P277 releases/ER-Q4-FY2011.txt | all opened |
| releases/OTHER-2012-02-27.txt | P278 to P278 | 1 | P278 releases/OTHER-2012-02-27.txt | all opened |
| releases/ER-Q1-FY2012.txt | P279 to P279 | 1 | P279 releases/ER-Q1-FY2012.txt | all opened |
| releases/OTHER-2012-05-07.txt | P280 to P280 | 1 | P280 releases/OTHER-2012-05-07.txt | all opened |
| releases/ER-Q2-FY2012.txt | P281 to P281 | 1 | P281 releases/ER-Q2-FY2012.txt | all opened |
| releases/OTHER-2012-08-01.txt | P282 to P282 | 1 | P282 releases/OTHER-2012-08-01.txt | all opened |
| releases/ER-Q3-FY2012.txt | P283 to P283 | 1 | P283 releases/ER-Q3-FY2012.txt | all opened |
| releases/OTHER-2012-11-06.txt | P284 to P284 | 1 | P284 releases/OTHER-2012-11-06.txt | all opened |
| releases/ER-Q4-FY2012.txt | P285 to P285 | 1 | P285 releases/ER-Q4-FY2012.txt | all opened |
| releases/OTHER-2013-02-28.txt | P286 to P286 | 1 | P286 releases/OTHER-2013-02-28.txt | all opened |
| releases/ER-Q1-FY2013.txt | P287 to P287 | 1 | P287 releases/ER-Q1-FY2013.txt | all opened |
| releases/OTHER-2013-05-03.txt | P288 to P288 | 1 | P288 releases/OTHER-2013-05-03.txt | all opened |
| releases/ER-Q2-FY2013.txt | P289 to P289 | 1 | P289 releases/ER-Q2-FY2013.txt | all opened |
| releases/OTHER-2013-07-30.txt | P290 to P290 | 1 | P290 releases/OTHER-2013-07-30.txt | all opened |
| releases/OTHER-2013-08-01-a.txt | P291 to P291 | 1 | P291 releases/OTHER-2013-08-01-a.txt | all opened |
| releases/OTHER-2013-08-01-b.txt | P292 to P292 | 1 | P292 releases/OTHER-2013-08-01-b.txt | all opened |
| releases/ER-Q3-FY2013.txt | P293 to P293 | 1 | P293 releases/ER-Q3-FY2013.txt | all opened |
| releases/OTHER-2013-11-06.txt | P294 to P294 | 1 | P294 releases/OTHER-2013-11-06.txt | all opened |
| releases/ER-Q4-FY2013.txt | P295 to P295 | 1 | P295 releases/ER-Q4-FY2013.txt | all opened |
| releases/OTHER-2014-03-20.txt | P296 to P296 | 1 | P296 releases/OTHER-2014-03-20.txt | all opened |
| proxy/PROXY-2012.txt | P297 to P297 | 1 | P297 proxy/PROXY-2012.txt | all opened |
| proxy/PROXY-2013.txt | P298 to P298 | 1 | P298 proxy/PROXY-2013.txt | all opened |
| events.txt | P299 to P299 | 1 | P299 events.txt | all opened |
opened (11 sheets: IS_Q, IS_A, BS_Q, BS_A, CF_Q, CF_A, EXTRA, NOTES, NONGAAP, RESTATED, LOCATORS)
```

**Output of calc.py**

```
C1 Cash tie-out failure FY2013 / Q4 FY2013 explained by revised FY2012 cash
  FY2012 cash as reprinted in FY2013 10-K: 545.5
  BS change using reprinted opening: -122.3 vs CF net change -122.3
  Q1-Q3 FY2013 net change (from original 533.3 opening) sum: 15.4 ; Q3 FY2013 closing 548.7 minus 533.3 = 15.4
C2 RESTATED sheet: lines differing by more than 1 (USD m)
   ('IS', 'Revenue', 'FY2012', 9020.8, 9024.9, 4.1)
   ('IS', 'Selling, general and administrative', 'FY2012', 945.8, 968.1, 22.3)
   ('IS', 'Pre-tax income', 'FY2012', 450.5, 441.4, -9.1)
   ('IS', 'Income from continuing operations', 'FY2012', 243.1, 238.6, -4.5)
   ('IS', 'Net income', 'FY2012', 243.1, 238.6, -4.5)
   ('BS', 'Cash and equivalents', 'FY2012', 533.3, 545.5, 12.2)
   ('BS', 'Trade receivables, net', 'FY2012', 1886.6, 1879.7, -6.9)
   ('BS', 'Equipment held for rental or lease, gross', 'FY2012', 15831.2, 15788.9, -42.3)
   ('BS', 'Accumulated depreciation, equipment held for rental or lease', 'FY2010', -2251.8, -2267.4, -15.6)
   ('BS', 'Accumulated depreciation, equipment held for rental or lease', 'FY2012', -2922.9, -2892.3, 30.6)
   ('BS', 'Equipment held for rental or lease, net', 'FY2010', 8939.4, 8923.8, -15.6)
   ('BS', 'Equipment held for rental or lease, net', 'FY2012', 12908.3, 12896.6, -11.7)
   ('BS', 'Goodwill', 'FY2010', 300.2, 328.6, 28.4)
   ('BS', 'Goodwill', 'FY2012', 1341.9, 1329.3, -12.6)
   ('BS', 'Intangible assets, net', 'FY2012', 4032.1, 4030.2, -1.9)
   ('BS', 'Total assets', 'FY2010', 17332.2, 17345, 12.8)
   ('BS', 'Total assets', 'FY2012', 23286, 23264.3, -21.7)
   ('BS', 'Trade payables', 'FY2010', 945, 954.3, 9.3)
   ('BS', 'Trade payables', 'FY2012', 999.1, 1003.2, 4.1)
   ('BS', 'Accrued liabilities', 'FY2012', 1180.5, 1163.1, -17.4)
   ('BS', 'Income taxes payable', 'FY2012', 118.6, 144.6, 26.0)
   ('BS', 'Total liabilities', 'FY2010', 15200.9, 15226.5, 25.6)
   ('BS', 'Common equity', 'FY2010', 2114.8, 2101.9, -12.9)
   ('BS', 'Common equity', 'FY2012', 2507.3, 2486.2, -21.1)
   ('BS', 'Total equity', 'FY2010', 2131.3, 2118.5, -12.8)
   ('BS', 'Total equity', 'FY2012', 2507.3, 2486.2, -21.1)
   ('CF', 'Net income', 'FY2012', 243.1, 238.6, -4.5)
   ('CF', 'Depreciation and amortization', 'FY2012', 2325.1, 2305.5, -19.6)
   ('CF', 'Change in receivables', 'FY2012', -157.7, -149.2, 8.5)
   ('CF', 'Change in payables', 'FY2010', 118, 119.1, 1.1)
   ('CF', 'Change in payables', 'FY2012', 49.9, 34, -15.9)
   ('CF', 'Change in accrued liabilities', 'FY2012', -22.6, -29.6, -7.0)
   ('CF', 'Cash from operations', 'FY2012', 2718, 2709.7, -8.3)
   ('CF', 'Capital expenditures (PP&E)', 'FY2012', -312.8, -297.1, 15.7)
   ('CF', 'Proceeds from disposals', 'FY2012', 137.7, 122, -15.7)
   ('CF', 'Cash from investing', 'FY2012', -4746.8, -4726.3, 20.5)
   ('CF', 'Net change in cash', 'FY2012', -398.5, -386.3, 12.2)
  count >1: 37 | by year: {'FY2010': 9, 'FY2011': 0, 'FY2012': 28}
  nonzero but <=1: [('Pre-tax income', 'FY2010', -1.0), ('Income from continuing operations', 'FY2010', -0.6), ('Net income', 'FY2010', -0.6), ('Total liabilities', 'FY2012', -0.6), ('Net income', 'FY2010', -0.6), ('Purchases of equipment held for rental or lease', 'FY2012', 0.4), ('Cash from financing', 'FY2012', 0.1)]
C3 FY2011 as reprinted in the FY2013 10-K (P66 p.76) vs as originally reported (P1 IS_A)
   Revenue 8298.4 -> 8299.3 diff 0.9
   Selling, general and administrative 745.3 -> 767.7 diff 22.4
   Pre-tax income 324.3 -> 305.6 diff -18.7
   Net income 195.7 -> 183.8 diff -11.9
   Direct operating 4566.4 -> 4573.1 diff 6.7 | Dep of REE and lease charges 1905.7 -> 1896.2 diff -9.5
C4 Quarterly revenue and pre-tax: workbook (as originally reported) vs as revised in FY2013 10-K (P68 pp.85-89; P84 p.149)
   Q1 FY2012: revenue 1960.9 vs 1961.7 diff 0.8; pre-tax -36.8 vs -36.7 diff 0.1
   Q2 FY2012: revenue 2225.1 vs 2226.2 diff 1.1; pre-tax 158.7 vs 148.0 diff -10.7
   Q3 FY2012: revenue 2516.2 vs 2517.2 diff 1.0; pre-tax 368.9 vs 373.1 diff 4.2
   Q4 FY2012: revenue 2318.5 vs 2319.7 diff 1.2; pre-tax -40.3 vs -43.1 diff -2.8
   Q1 FY2013: revenue 2436.5 vs 2436.9 diff 0.4; pre-tax 72.2 vs 73.7 diff 1.5
   Q2 FY2013: revenue 2714.6 vs 2709.2 diff -5.4; pre-tax 211.9 vs 205.9 diff -6.0
   Q3 FY2013: revenue 3069.4 vs 3069.4 diff 0.0; pre-tax 328.3 vs 321.3 diff -7.0
   Q4 FY2013: revenue 2551.3 vs 2556.4 diff 5.1; pre-tax 50.7 vs 62.3 diff 11.6
   Q4 FY2013 derived (FY2013 minus Q1-Q3 as originally reported): revenue 2551.4 pre-tax 50.7
   derived Q4 minus revised Q4 (P84): -5.0 -11.6 | 9M 2013 adjustments per P68 p.87: revenue -5.0, pre-tax -11.6
C5 Revision components (P68 p.83): prior-period pre-tax effect
   sum of components: 34.7 | stated prior-period amount 34.7
   by year 2010/2011/2012: 6.8 18.7 9.2
   total errors 46.3 minus prior-period 34.7 = 11.6 | ER-Q4-FY2013 total 47.9 minus 10-K total 46.3 = 1.6
   FY2011 NI revision -12.0 as % of FY2011 NI as originally reported: -6.1 %
   FY2012 NI revision -4.5 as % of FY2012 NI as originally reported: -1.9 %
   FY2011 pre-tax revision -18.7 as % of FY2011 pre-tax as originally reported: -5.8 %
   FY2012 pre-tax revision -9.2 as % of FY2012 pre-tax as originally reported: -2.0 %
C6 Q3 2011 revision of FY2009/FY2010 (P131 p.7; P11 p.92)
   FY2010 NI attributable -48.0 -> -48.7: diff -0.6
   FY2009 NI attributable -126.0 -> -129.5: diff -3.5
   FY2009 BS revised (P131): TA 16002.4->16015.1 12.7 TL 13905.0->13929.9 24.9 TE 2097.4->2087.2 -10.2
   FY2009 BS in P1 BS_A: TA 16002.4 TE 2097.4
   2009 direct operating adjustment: Q3 2011 10-Q 6,300k vs FY2011 10-K 2,634k; diff (USD m): 3.7
C7 Revenue by business line: FY2012 as originally reported (P1 EXTRA) vs as recast in FY2013 10-K (P66 p.76)
   car 7456.1 -> 7161.7 diff -294.4
   equip 1383.2 -> 1385.4 diff 2.2
   other 181.5 -> 477.8 diff 296.3
   total diff 4.1
   Quarterly 'Other' revenue FY2013 (P1 EXTRA): [79.2, 0.8, 133.5, 129.8]
   Q2 2012 as reprinted in Q2 2013 10-Q (P227 p.3): car 1889.6 vs orig 1849.3 diff 40.3 ; other 0.5 vs orig 41.6 diff -41.1
C8 Depreciation-rate changes (P74 p.126 vs P45 p.113, P16 p.125)
   2012: US -139.4 + intl 8.8 = -130.6 vs FY2012 10-K car rental net -130.6
   2011: US -26.7 + intl 12.9 = -13.8 vs FY2011 10-K car rental net -13.8
   2013 car rental net: US -44.2 + intl 5.0 = -39.2
   2012 car rental rate change as % of FY2012 pre-tax as originally reported: -29.0 %
C9 Acquisitions
   Dollar Thrifty days owned in FY2012 (2012-11-19 to 2012-12-31, inclusive): 43
   DT revenue 170.6 as % of FY2012 revenue as originally reported: 1.9 %
   DT PPA preliminary (P41 p.88) -> final (P70 p.98): goodwill 4.0 intangibles -1.0 accrued liab -21.0 deferred tax 18.0
   Donlen days owned in FY2011 (2011-09-01 to 2011-12-31, inclusive): 122
   Donlen revenue 142.7 as % of FY2011 revenue: 1.7 %
   Goodwill FY2011->FY2012 (P1 BS_A): 949.8 | intangibles: 1469.9
   Total assets FY2011->FY2012 change: 5612.5
C10 Filing timing (dates from P0 manifest)
   FY2011 10-K filed 2012-02-27: days after year end 58
   FY2012 10-K filed 2013-03-04: days after year end 63
   FY2013 10-K filed 2014-03-19: days after year end 78
   Q4 FY2010 earnings release 8-K filed 2011-02-23: days after year end 54
   Q4 FY2011 earnings release 8-K filed 2012-02-22: days after year end 53
   Q4 FY2012 earnings release 8-K filed 2013-02-25: days after year end 56
   Q4 FY2013 earnings release 8-K filed 2014-03-18: days after year end 77
C11 Allowance: Schedule II opening vs prior closing as originally reported (P1 NOTES)
   opening FY2013 29.3 closing FY2012 25.1 diff 4.2
   opening FY2012 20.3 closing FY2011 20.3 diff 0.0
   opening FY2011 19.7 closing FY2010 19.7 diff 0.0
C12 Scale scan: any nonzero cell more than 300x above or below the median absolute value of its row (P1)
   EXTRA | Common Stock, $0.01 par value, 2,000,000,000 shares authorized, 413,462,889 and 410,245,225 shares issued and outstanding | Q1 FY2011 | 4.1 (row median 4167)
   EXTRA | Common Stock, $0.01 par value, 2,000,000,000 shares authorized, 413,462,889 and 410,245,225 shares issued and outstanding | Q2 FY2013 | 4.2 (row median 4167)
   EXTRA | Common Stock, $0.01 par value, 2,000,000,000 shares authorized, 413,462,889 and 410,245,225 shares issued and outstanding | Q3 FY2013 | 4.5 (row median 4167)
   EXTRA | Common Stock, $0.01 par value, 2,000,000,000 shares authorized, 413,462,889 and 410,245,225 shares issued and outstanding | Q4 FY2013 | 4.5 (row median 4167)
   EXTRA | Common Stock, $0.01 par value, 2,000,000,000 shares authorized, 413,462,889 and 410,245,225 shares issued and outstanding | FY2009 | 4.1 (row median 4167)
   EXTRA | Common Stock, $0.01 par value, 2,000,000,000 shares authorized, 413,462,889 and 410,245,225 shares issued and outstanding | FY2010 | 4.1 (row median 4167)
   EXTRA | Common Stock, $0.01 par value, 2,000,000,000 shares authorized, 413,462,889 and 410,245,225 shares issued and outstanding | FY2013 | 4.5 (row median 4167)
   EXTRA | Treasury Stock, at cost, 23,200,000 shares and 0 shares | Q1 FY2013 | -467248 (row median 277.35)
   EXTRA | Basic (in shares) | Q4 FY2011 | 0.3 (row median 415.9)
   EXTRA | Basic (in shares) | Q4 FY2012 | 0.4 (row median 415.9)
C13 Stock repurchased: annual vs quarters (P1 CF_A, CF_Q)
   FY2013 annual -554.7 | Q4 derived -87.5 | implied Q1-Q3 total = -467.2
C14 FY2011 cash flow as reprinted in the FY2013 10-K (P66 pp.80-81) vs as originally reported (P1 CF_A)
   Cash from operations 2233.3 -> 2211.1 diff -22.2
   Cash from investing -2192.9 -> -2170.6 diff 22.3
   FY2012 restricted cash change: orig (P1 EXTRA) -261.6 -> reprinted (P66 p.80) -241.6 diff 20.0
C15 Sign check: revolver proceeds FY2013, P1 EXTRA vs P66 p.81
   P1 EXTRA: -9511.6 | P66 text: 9511.6 | sum with P1 EXTRA 0.0
   Purchase of treasury shares row (P1 EXTRA) Q1/Q2 FY2013: -467248 466780.8
```

**Output of search.py** (hit counts per term, all text files P2 to P299)

```
#### step1
'fiscal year end': 132 hits in 122 files: P2(1), P3(1), P4(1), P5(1), P6(1), P7(1), P8(1), P9(1), P10(1), P11(1), P12(1), P13(1), P14(1), P15(1), P16(1), P17(1)
'change in fiscal year': 0 hits in 0 files
'53-week': 0 hits in 0 files
'53 week': 0 hits in 0 files
'fifty-three': 0 hits in 0 files
'extra week': 0 hits in 0 files
'transition period': 2 hits in 2 files: P294(1), P297(1)
#### step3
'acquisition': 1687 hits in 132 files: P2(11), P3(8), P5(13), P8(2), P9(37), P10(4), P12(17), P13(4), P17(1), P19(3), P22(1), P23(1), P29(1), P30(13), P31(30), 
'acquired': 614 hits in 101 files: P2(14), P3(2), P5(7), P6(2), P8(1), P9(18), P10(4), P11(1), P12(9), P17(1), P22(1), P28(1), P30(6), P31(2), P33(13), P34(5), 
'business combination': 81 hits in 38 files: P4(3), P9(2), P20(2), P32(2), P33(1), P34(1), P37(7), P38(3), P39(2), P41(2), P49(1), P61(1), P62(1), P63(1), P66(8
'purchase price': 196 hits in 66 files: P2(1), P3(1), P5(1), P9(6), P12(5), P15(1), P30(1), P31(1), P33(3), P34(2), P37(15), P39(2), P40(2), P41(9), P44(1), P55
'divest': 300 hits in 57 files: P30(3), P31(2), P33(4), P37(15), P38(3), P41(11), P48(2), P59(4), P60(2), P62(12), P66(18), P67(3), P70(11), P77(2), P81(2), P12
'disposal': 747 hits in 116 files: P2(2), P3(2), P4(1), P5(23), P6(5), P9(17), P11(5), P13(1), P16(5), P19(3), P20(1), P30(2), P31(2), P32(1), P33(22), P34(5), 
'sold': 214 hits in 82 files: P2(2), P3(4), P5(1), P9(8), P10(1), P13(2), P16(2), P22(2), P23(1), P29(1), P30(3), P31(4), P33(2), P37(6), P38(1), P42(2), P45(1)
'discontinued': 0 hits in 0 files
'held for sale': 0 hits in 0 files
#### step4
'adopted': 59 hits in 23 files: P5(2), P9(4), P14(2), P15(2), P33(2), P37(5), P43(3), P44(2), P62(2), P66(5), P72(3), P73(2), P107(2), P127(2), P146(2), P166(2)
'adoption': 39 hits in 31 files: P66(2), P68(2), P107(1), P127(1), P146(1), P166(2), P185(1), P204(1), P206(1), P208(1), P225(1), P227(2), P229(2), P246(1), P24
'new accounting standard': 0 hits in 0 files
'recently issued': 45 hits in 24 files: P37(1), P39(1), P66(1), P68(1), P129(2), P131(3), P148(2), P150(3), P166(1), P167(2), P169(3), P185(1), P186(2), P188(3)
'change in accounting policy': 0 hits in 0 files
'change in accounting estimate': 0 hits in 0 files
'useful life': 12 hits in 11 files: P9(1), P12(1), P37(1), P41(1), P66(2), P70(1), P81(1), P129(1), P133(1), P247(1), P261(1)
'reclassif': 178 hits in 42 files: P9(7), P11(5), P22(2), P37(8), P39(4), P41(4), P66(19), P68(7), P70(4), P78(8), P89(3), P91(1), P102(2), P109(5), P111(2), P1
'recast': 123 hits in 35 files: P107(1), P127(1), P146(1), P166(1), P185(1), P204(1), P225(1), P246(1), P266(1), P268(5), P269(8), P270(1), P271(6), P272(5), P2
'conformed to current': 0 hits in 0 files
'conform to the current': 8 hits in 2 files: P66(4), P68(4)
'segment': 1633 hits in 102 files: P2(9), P5(70), P6(4), P9(12), P12(2), P19(8), P21(3), P30(10), P33(75), P34(3), P37(14), P39(1), P40(1), P41(2), P48(8), P50(
#### step5
'restate': 48 hits in 23 files: P3(1), P9(2), P15(1), P23(1), P29(1), P31(1), P37(3), P44(1), P52(2), P58(2), P66(4), P71(1), P73(1), P82(2), P88(2), P226(1), P
'restatement': 12 hits in 2 files: P297(6), P298(6)
'revision': 30 hits in 17 files: P37(2), P66(7), P68(2), P70(1), P81(1), P84(1), P86(1), P206(1), P211(1), P227(2), P229(1), P232(1), P247(4), P249(2), P252(1),
'revised': 193 hits in 54 files: P5(2), P6(1), P9(7), P11(7), P33(1), P34(1), P37(1), P59(1), P62(2), P63(1), P66(25), P68(19), P70(2), P77(1), P86(1), P89(1), 
'previously issued': 27 hits in 11 files: P9(2), P11(2), P66(4), P68(2), P71(2), P129(2), P131(2), P275(2), P295(6), P296(2), P299(1)
'immaterial error': 4 hits in 4 files: P66(1), P68(1), P295(1), P296(1)
'correction of an error': 0 hits in 0 files
'non-reliance': 1 hits in 1 files: P299(1)
'prior period': 72 hits in 47 files: P5(1), P9(2), P11(1), P17(1), P31(1), P37(2), P39(1), P46(1), P59(1), P60(1), P62(1), P66(11), P68(3), P70(2), P75(1), P77(
'out of period': 6 hits in 4 files: P66(1), P68(1), P295(3), P296(1)
'out-of-period': 0 hits in 0 files
#### step7
'material weakness': 6 hits in 6 files: P8(1), P9(1), P36(1), P37(1), P65(1), P66(1)
'significant deficiency': 0 hits in 0 files
'remediation': 173 hits in 45 files: P2(4), P3(1), P4(4), P5(4), P9(4), P20(4), P30(4), P31(2), P32(4), P33(4), P37(4), P49(4), P59(4), P60(2), P61(4), P62(4), 
'not effective': 0 hits in 0 files
'going concern': 0 hits in 0 files
'substantial doubt': 0 hits in 0 files
'covenant': 273 hits in 73 files: P3(7), P5(4), P9(11), P13(11), P31(8), P33(4), P37(11), P42(11), P60(7), P62(4), P66(10), P71(10), P89(4), P96(4), P107(8), P1
'waiver': 123 hits in 62 files: P2(7), P4(4), P5(3), P9(2), P20(2), P30(7), P32(4), P33(3), P37(2), P49(2), P59(7), P61(2), P62(4), P66(4), P71(1), P79(2), P85(
'late filing': 0 hits in 0 files
'NT 10-K': 0 hits in 0 files
'12b-25': 0 hits in 0 files
```


## 11. Verification

`Verification: 8 items run, 7 ledger rows (P1 0, P2 0, P3 7, P4 0), 12 could not run. Figures: 183 copied, 61 calculated, 0 unverified. Units: USD, millions (P1; text files in their own units). Framework: US GAAP. Context sheet: produced by this step (F1 is its source, not a consumer).`

Items run = the eight method steps. Figure counts are a script count of numeric tokens by the mark on their line (see assemble.py), so they are approximate.

**Candidates for review, not findings.**
