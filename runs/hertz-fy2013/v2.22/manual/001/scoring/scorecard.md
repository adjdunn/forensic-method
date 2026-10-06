# Scorecard: hertz-fy2013, prompts v2.22, adapter manual, run 001

Scorer: Claude Code scoring agent (Fable 5.1), 6 October 2026. Inputs: `run.json`; the five replies as PDFs (`numbers-1.pdf`, `numbers-2.pdf`, `text-3.pdf`, `text-4.pdf`, `report-5.pdf`, text extracted with pypdf); the checker reports `check-numbers-1.md` to `check-report-5.md`; the workspace files; `tests/hertz-fy2013/answer-key.md` with its addendum (AK1 to AK7 applied); `tests/hertz-fy2013/score.md` for defect numbering; `tools/TESTS.md`, "What every run is scored on". Recomputation code: `scoring/recompute.py` (42 sub-figures under ten measures, all from the workspace files). Files the run saw: `statements.xlsx`, `annual-report-FY2012-12-31.txt`, `annual-report-FY2013-12-31.txt`, `earnings-release-Q4-FY2012-12-31.txt`, `earnings-release-Q4-FY2013-12-31.txt`. Per `run.json`, the replies are Aaron's Claude chat runs of 6 October 2026 with prompts 1 and 2 at v2.14 to v2.17 wording, 3 at v2.18, 4 at v2.19 and 5 at v2.20; the v2.21 and v2.22 ranking clauses in the saved `prompt-5.md` post-date the reply.

## Verdict

**Fail against the key's bar as written, narrowly, on one condition: K5 is partial, not at level 1 in full.** Of the key's seven required items only K5 and K6 are reachable from the five files the run saw (K1 to K4 need the 2013 10-Qs, K7 the Q3 2013 release). K6 passes by the addendum's route: the FY2013 10-K's "optimization of fleet holding periods related to the integration of Dollar Thrifty" is quoted with locators (pp. 42 and 126), tied to the widened holding-period range and the falling depreciation rate, and carried into the report's level-1 item. K5 is caught in both halves but not at the level the key asks: the range widening ("4 to 28" at FY2012 p. 81 to "4 to 36" at FY2013 p. 91) is a full write-up in text-4 and part of report item 1 at level 1, and the unchanged "eighteen months in the United States" is quoted for both years (p. 11 and p. 11) and set against the range top in text-4's stayed-the-same table, but that row ends "Can't tell; rough test" (the test used, fleet over cars sold, cannot test an average) and the average is dropped from the report, which prompt 5's own merge rule says should not happen. Everything else is clean: zero trap hits, 42 of 42 recomputed figures match, every quotation is exact and every locator opens, readings are hedged, nothing from after the cutoff is used. The gap between this run and a pass is one verdict word in a table and one merge step in the report. The T1-m entry in `tools/TESTS.md` reads K5 as "caught in full"; this scorecard reads it as partial because the key requires the result "inconsistent" at level 1, and the report never shows the average.

| Condition | Required | Result | Met |
|---|---|---|---|
| K5 at level 1 | Row quoting 2013 "eighteen months" and "4 to 36" against 2012 "18" and "4 to 28", with locators, result "inconsistent" | Range half: text-4 write-up 1 and report item 1, level 1. Average half: text-4 table row, both years quoted with pages, set against the range top, result "Can't tell; rough test"; absent from the report | Partly |
| Five of K1 to K7 at expected level or partial | 5 | Only K5 and K6 in pack: K5 partial, K6 pass. The condition cannot be applied to this file set (AK10) | Not applicable; 2 of 2 reachable items at least partial |
| Zero trap hits | 0 | 0 | Yes |
| G1: no characterization | holds | No banned words; "misstatement" occurs once, inside a quoted 10-K sentence | Yes |
| G2: nothing after 31 March 2014 | holds | No post-cutoff fact; "2014" appears only in read-next lines and in a quoted 10-K sentence dated 1 February 2014 | Yes |

## K items

Scorer's own pack locators, confirmed in code against the workspace files: "eighteen months in the United States" (FY2012 p. 11; FY2013 p. 11); "Cars | 4 to 28 months" under "Useful lives" (FY2012 p. 81) and "Cars | 4 to 36 months" under "Holding periods" (FY2013 p. 91); "longer holding periods" in the maintenance-cost sentence (FY2013 p. 53); "optimization of fleet holding periods related to the integration of Dollar Thrifty" (FY2013 pp. 42 and 126); "net decreases of $44.2 million, $139.4 million and $26.7 million" (pp. 42 and 126); "net losses of $48.2 million, and net gains of $100.6 million and $114.9 million" (p. 126); Schedule II allowance roll-forward (p. 158); "out of period errors totaling $46.3 million" (p. 83); the February 2013 guidance table (Q4 FY2012 release pp. 4 to 5).

| ID | Req./bonus | In pack? | Caught by (reply, item) | Level expected / got | Score | Reason |
|---|---|---|---|---|---|---|
| K1 | Req. | No: Q2 2013 10-Q | n/a | 1 / n/a | Not in pack | Needed the Q2 2013 10-Q MD&A or Note. The annual counterpart of the sentence, the FY2013 10-K's driver list for the same rate cuts, which does name holding periods (pp. 42, 126), was quoted and tested in numbers-2 and text-4 |
| K2 | Req. | No: Q2 2013 10-Q | n/a | 3 or 1 / n/a | Not in pack | Needed the Q2 2013 10-Q MD&A. The FY2013 10-K's version of the per-vehicle sentence (p. 42) was tested in numbers-2: "can't be tested as stated", nearest number the U.S. charge per company-operated car ($226 against $219 a month; $217 against $242 before disposal results), with the company's own reasons given first |
| K3 | Req. | No: Q3 2013 10-Q | n/a | 1 / n/a | Not in pack | Needed the Q3 2013 10-Q MD&A or Note |
| K4 | Req. | No: Q3 2013 10-Q | n/a | 3 or 1 / n/a | Not in pack | Needed the Q3 2013 10-Q MD&A |
| K5 | Req. | Yes | text-4 write-up 1 (range: FY2012 p. 81, FY2013 p. 91); text-4 stayed-the-same table, row 2 ("eighteen months in the United States", p. 11 and p. 11, against "Top of stated range 28 then 36 months"); report-5 item 1 (range only, level 1) | 1 / range 1; average no level (table row, "Can't tell; rough test") | Partial | Both sentences quoted with locators for both years. The range change is written up as not disclosed as a change in estimate, tied to the $44.2M rate cut and the holding-period explanation, and reaches the report at level 1. The unchanged average is set against the widened range in a table row but with a "can't tell" verdict on a test that cannot settle it (U.S. fleet over non-program cars sold, 31.6 then 29.7 months, recomputed), and it does not reach the report at all |
| K6 | Req. | Yes | numbers-2 depreciation write-up (p. 42); text-4 write-ups 1 and 2 (p. 126); report-5 item 1 | 1 or 2 / 1 | Pass (addendum route, AK6 and AK7) | "optimization of fleet holding periods related to the integration of Dollar Thrifty" quoted with locators, set against the widened range (K5) and the fall in the rental depreciation rate from 15.2% to 14.3% (K9), and carried into the report's level-1 item with the holding-period reading stated both ways. The p. 53 "longer holding periods" maintenance sentence is quoted nowhere, so the maintenance side of the link is missing (second run to miss it; PR38) |
| K7 | Req. | No: Q3 2013 release (4 November 2013) and the 26 September 2013 release | n/a | 3 / n/a | Not in pack | The required element, the reaffirmation, is absent. The pack does hold the February 2013 range (Q4 FY2012 release pp. 4 to 5: adjusted diluted EPS $1.82 to $1.92) and the FY2013 outturn (Q4 FY2013 release p. 5: $1.63); no reply sets one against the other, but the v2 prompts have no guidance step. The key's February figure differs from the pack's (AK8) |
| K8 | Bonus | No: Q1 2013 10-Q | n/a | 3 / n/a | Not in pack | Needed the Q1 2013 10-Q MD&A |
| K9 | Bonus | Yes | numbers-1 flag 4 (16.1%, 15.2%, 14.3% for FY2011 to FY2013); numbers-2 depreciation write-up; report-5 item 1 | 3, or 1 to 2 joined / 1 | Pass | Rate computed on Note 8's charge before the disposal adjustment over average gross cars plus other equipment (fleet in), annual, direction stated, two years of persistence, $152m (23% of pre-tax) not taken at the FY2012 rate; recomputed (rows 1 to 2b). Same-quarter rates not computed, with the reason stated (the note is annual; the releases carry no quarterly Note 8). Dollar Thrifty enters only through the company's own p. 126 attribution, which AK7 allows |
| K10 | Bonus | Yes | numbers-1 table: M-score totals only (-2.93, -2.72, -3.24) | localization / none | Not scored | DEPI is not shown separately at this prompt version, and the key item is defective (AK5: DEPI is below 1 on this pack) |
| K11 | Bonus | Partly: FY2013 10-K | report-5 item 1 | 1 thread / 1 | Partial | One thread at level 1 merges the Note 8 tension, the range widening, the dropped "strong", the rate fall and both tracks' readings. The maintenance-cost side (p. 53) is absent, so the thread has one of its two ends |
| K12 | Bonus | Yes: Schedule II p. 158 | numbers-1 table (allowance 1.4%, 1.2%, 1.3%, 2.0% of gross receivables); numbers-2 read-next (write-offs $29.3m to $40.3m, allowance 1.5% to 2.0%); text-4 table (allowance over write-offs 1.00 then 0.76, "Strained; rough test"); report-5 Also noted (write-offs up 37.5% against 5.1%; $4.0M provision tie-out gap) | 3 / Also noted | Pass | Ratios in code from Schedule II and the balance sheet, FY2010 to FY2013; Dollar Thrifty cited for the 2012 receivables level; no mechanism claim. It does not say "subrogation cannot be isolated", though neither 10-K mentions subrogation. Recomputed (rows 6 to 6e) |
| K13 | Bonus | Yes | numbers-1 flags 1 and 3 (acquired November 2012; $1,904.6m outflow); numbers-2 receivables and payables write-ups ($170m receivables, $43m payables, p. 98); text-4 write-up 3 (controls exclusion dropped); report-5 "Checked and explained" | 4 / explained | Pass | Dated, located and quantified; the receivables flag it explains ends in "Checked and explained"; the payables flag is kept open because the acquisition covers only 18% of the gap. Not offered on its own as the benign reading for the depreciation items; only the company's p. 126 attribution is used (AK7) |
| K14 | Bonus | Yes | text-3 write-up 3 and Also noted; text-4 write-up 3 and Part 3 table; report-5 item 4 | 3 / 2 | Pass | "out of period errors totaling $46.3 million" (p. 83) and the release's $47.9M quoted with locators; $235M never cited. Level 2 rests on two pack signals (the revision and the covenant "unknowingly not being met", p. 150) |
| K15 | Bonus | No: proxies | n/a | 3 or 4 / n/a | Not in pack | report-5 "Not examined" says no proxy statement |
| G1 | Global | | | | Holds | See below |
| G2 | Global | | | | Holds | See below |

## Traps

| Trap | Hit? | Sentence or "none" |
|---|---|---|
| T1 | No | The run cites "declining residual values" (FY2013 10-K p. 126) and "a deterioration in the used vehicle residual values" (p. 54), both pack quotations with locators, about FY2013 as a whole; nothing about Q2 2013 |
| T2 | No | none |
| T3 | No | none; "21" and "25 months" do not occur |
| T4 | No | none; text-4 calls its average test "rough" and does not say how the average is computed |
| T5 | No | none; no "decision" language and no peer comparison |
| T6 | No | none; text-4: "the holding-period share of the $44.2M is not split out" |
| T7 | No | none |
| T8 | No | none |
| T9 | No | none; "spreadsheet" occurs only for the statements workbook |
| T10 | No | none |
| T11 | No | none |
| T12 | No | none |
| T13 | No | none |
| T14 | No | none; "implemented Oracle general ledger, accounts payable" is quoted from p. 159 as a timing fact for the payables flag, not as a control weakness; no $235m, no count of areas or weaknesses |
| T15 | No | none; "2014" appears only in read-next lines ("2014 quarterly filings", "Q1 2014 results") and in the p. 24 Simply Wheelz sentence dated 1 February 2014, which is in the FY2013 10-K |
| T16 | No | Vendor incentives and Brazil are named from the 10-K's own Note 2 (pp. 83, 85) |

Trap count: **0**.

## G1 and G2

**G1 holds.** No banned word in any reply (checker: none in all five; scorer's own scan for fraud, manipulation, red flag, aggressive, suspicious, concerning, misstatement). "Leans aggressive" is prompt 3's own vocabulary; "misstatement" occurs once, inside the quoted Note 2 sentence "did not ... result in a material misstatement" (p. 83). Every reading is worded "most likely", "possibly" or "can't tell", and each write-up states what would change it; the report closes "Items to investigate, not conclusions."

**G2 holds.** No fact from after 31 March 2014. The latest pack text used is the FY2013 10-K's subsequent-events note (January and February 2014, p. 150) and the Q4 FY2013 release. "2014" otherwise appears only as what to read next. No reference to the SEC order, the restatement or any 2014 announcement; the K6 maintenance-sentence miss and the K5 "can't tell" argue against any leakage.

## Measurements

Checker summary per reply: numbers-1, 0 of 0 quotations (a table and five flags, no quotations), 3 shares recomputed with 0 mismatches, 753 words; numbers-2, 12 of 15 exact on the cited page, 0 mismatches, 1,145 words; text-3, 15 of 20, 0 mismatches, 1,135 words; text-4, 28 of 30, 0 mismatches, 1,129 words; report-5, 7 of 10, 0 mismatches, 878 words. No quotation was "not found" or found only in another document.

The checker's "page differs" and "no page cited" cases, settled in the pack: numbers-2 "timing" is quoted from p. 133 (cited in the same write-up); the p. 65 locator the checker attached to it belongs to the 30% fall in Q4 disposal proceeds, which is on p. 65 (fourth-quarter proceeds $1,594.9m against $2,286.2m). numbers-2 "Other unusual/non-recurring" and "litigation accrual" are on the Q4 FY2013 release pp. 9 and 2 and 5, cited as "the FY2013 release" without a page. text-3 "net decreases of $44.2 million", "net losses of $48.2 million" (p. 126), "could potentially exceed $40.0 million" and "will not be material" (p. 137) carry their pages at the end of the same table cell; "declining residual values" is on p. 126, and the write-up names Note 8 p. 126 one sentence earlier, though the sentence that quotes it cites only pp. 54 and 42. text-4 "optimization of fleet holding periods" carries p. 126 in the same sentence; "with fewer program cars in our fleet" carries pp. 22 and 23 in the table. report-5 "indicative of the residual values experienced" carries FY2013 p. 126 in the sentence; "strong" dropped and "fewer program cars" have no page in the report itself (text-4 gives FY2012 p. 113 and FY2013 p. 126, and pp. 22 and 23). Result: every quotation is exact and every locator opens; two phrases in the report rely on text-4 for their page.

TESTS.md measures: numbers tie (42 of 42 sub-figures below); locators open (all settled above); quotations exact (all); benign reading present and first (every write-up in numbers-2, text-3, text-4 and report-5 gives the company's explanation or an ordinary reading before the adverse one, and each reading names what would change it); context used (no context sheet at v2; Dollar Thrifty dated, located and quantified in numbers-1 and numbers-2); consistency checks and code shown do not apply at this version (prompts say not to show code); no characterization (holds); platform parity (not tested here).

Ten recomputed measures (`scoring/recompute.py`; 42 sub-figures, 42 match):

| # | Figure (reply) | Reported | Recomputed | Where in the pack | Match |
|---|---|---|---|---|---|
| 1 | Rental depreciation rate FY2013, FY2012, FY2011 (numbers-1 flag 4) | 14.3%, 15.2%, 16.1% | 14.3, 15.2, 16.1 | Note 8 charge before disposal adjustment (p. 126) over average gross cars plus other equipment (p. 75, FY2012 as revised; earlier years from the workbook); average FY2013 base 16,878.85 | Yes |
| 2 | Charge not taken at the FY2012 rate; share of pre-tax (numbers-1, report-5 item 1) | $152m, 23% | 152, 23 | Derived from row 1 and pre-tax 663.1 (p. 76) | Yes |
| 3 | U.S. rate cut $44.2m, U.S. disposal loss $48.2m, net rate cut $39.6m as shares of pre-tax (text-3, text-4, numbers-2, report-5) | 6.7%, 7.3%, 6.0% | 6.7, 7.3, 6.0 | pp. 126, 40, 76 | Yes |
| 4 | U.S. disposal swing gain to loss; share of pre-tax (text-3, text-4) | $148.8M, 22.4% | 148.8, 22.4 | p. 126 (100.6 gain, 48.2 loss) | Yes |
| 5 | Restructuring plus related; all exclusions; new exclusions (text-3, text-4, report-5) | 14.9%, 73.9%, 13.8% | 14.9, 73.9, 13.8 | p. 50 (77.0 + 21.8; 40.0 + 7.8 + 44.0); release p. 9 (490.1) | Yes |
| 6 | Allowance over write-offs FY2013 and FY2012; write-off and allowance growth; allowance share of gross receivables (text-4, report-5, numbers-1) | 0.76, 1.00; 37.5%, 5.1%; 2.0% | 0.76, 1.00; 37.5, 5.1; 2.0 | Schedule II p. 158; p. 75 | Yes |
| 7 | Receivables change, revenue growth, DSO FY2012 and FY2013, receivables at FY2012 days less the balance (numbers-1 flag 1) | -19.8%, +19.4%, 76.5 to 51.3, $746m | -19.8, 19.4, 76.5, 51.3, 746 | Workbook BS and IS, as first reported; FY2012 reproduces only with a 366-day year, which the reply does not say | Yes |
| 8 | Days payable FY2012 and FY2013; payables change; cost growth (numbers-1 flag 3) | 52.7 to 42.7; -3.1%; +19.2% | 52.7, 42.7, -3.1, 19.2 | Workbook; cost line direct operating plus REE depreciation and lease charges; 366-day 2012 | Yes |
| 9 | Q4 gross margin 2012 and 2013; fall times Q4 revenue; share of pre-tax (numbers-1 flag 5, report-5 item 3) | 22.1% to 18.5%; $90m; 14% | 22.1, 18.5, 90, 14 | Q4 FY2013 release p. 9 | Yes |
| 10 | Pre-tax growth on as-reported and revised FY2012; $34.7M and $46.3M as shares; cars sold restated; U.S. fleet over non-program cars sold; U.S. depreciation per car per month (text-4, text-3, report-5, numbers-2) | 47.2%, 50.2%; 5.2%, 7.0%; 7.1%; 31.6 then 29.7 months; $226 vs $219 | 47.2, 50.2; 5.2, 7.0; 7.1; 31.6, 29.7; 226, 219 | p. 84 (450.6, 441.4); p. 83; FY2013 pp. 42 to 43 and FY2012 p. 42 (190,900 vs 178,300); p. 49 and release p. 9 (358,000 + 1,100 and 468,500 + 21,500 cars); p. 131 | Yes |

Observation: the workbook's as-first-reported FY2012 pre-tax income is 450.5 (FY2012 10-K p. 113) while the FY2013 10-K's "as previously reported" column says 450.6 (p. 84); numbers-1 uses the first and text-4 the second; growth rounds to 47.2% either way (PK10).

## Ranking

The report's order follows the v2.22 rule if the scan's 23% (the charge not taken at the FY2012 rate, an income measure) governs item 1: level 1 items first (depreciation, then adjusted measures at 14.9%), then level 2 income effects by size (Q4 margin 14%, controls 5.2%), then the level 2 balance (payables, $233M, 35%, labelled and placed last with the reason stated). The report gives item 1 three sizes (6.7%, 6.0%, 23%) and does not say which one ranks it, so on the 6.7% it would sit below item 2; the reply pre-dates the v2.22 sentence that settles this (PR39). No item on the list is an explained item or a tie-out gap: the receivables flag, the industry payables share and the 2012 rate cut are in "Checked and explained", and the $4.0M provision gap is in "Also noted". Item 4 (controls effective beside errors) sits at level 2 where the key expected at most P3 for a controls item without a disclosed weakness; the run rests it on two pack signals (the revision note and the covenant notice on p. 150), which is defensible; observed once. One item belongs on the list and is not there: the unchanged "eighteen months" average (text-4 table, "can't tell") should have merged into item 1 under prompt 5's own rule that a statement left the same belongs with the estimate it describes; it appears nowhere in the report, not even in "Also noted" (PR37). The intangible-lives row ("No, both years; small") is also dropped; minor.

## Defects

### Answer key

| # | Item | Defect | Evidence | Fix |
|---|---|---|---|---|
| AK8 | K7 | The February 2013 range in the key ($1.78 to $1.88, from the order) is not what the pack's February document states, and the measure is not named | Q4 FY2012 release pp. 4 to 5: "Adjusted Diluted Earnings Per Share ... $1.82 - $1.92"; FY2013 outturn $1.63 (Q4 FY2013 release p. 5) | Record the pack's range and its label (adjusted diluted EPS); say the order's $1.78 to $1.88 is either a later interim revision not in this pack or a different measure; score "ranges in date order" against the pack's figures |
| AK9 | K5 | The pass criterion requires the result "inconsistent", but the key's own benign reading (an average measured on disposed cars lags a change in plans for cars still held) cannot be ruled out from the pack, so "cannot be reconciled without knowing how the average is computed" is the honest verdict and the key does not say how to score it | text-4 table row: both sentences, both years, both pages, "Can't tell; rough test" | State that a row quoting both sentences for both years and setting them against each other passes when it is carried to the report at level 1, whatever the verdict word, and is partial when it stays in a table |
| AK10 | Pass bar | "Five of K1 to K7" cannot be applied to a pack without the 10-Qs and the Q3 release; only K5 and K6 are reachable | This run's file set | State the bar per file set: for the five-file pack, K5 at level 1, K6 at least partial, zero traps, G1 and G2 |

### Prompts

| # | Prompt | Defect | Proposed change |
|---|---|---|---|
| PR36 | Prompt 4, Part 2 | The "still fits" test for a stated average inside a disclosed range was run as U.S. fleet over cars sold (a ceiling), which cannot test an average holding period, and ended "can't tell", so the unchanged average beside a widened range never registered as a statement that no longer fits. Observed once at this wording (v0.2 never read the sentence, PR28) | When a stated average sits inside a disclosed range, the number to compare is the range itself: an unchanged average while the top of the range moves is "no longer fits as stated" unless the report says how the average is computed; any arithmetic test is secondary and named as such |
| PR37 | Prompt 5, gather and merge | Rows of prompt 4's stayed-the-same table marked "Can't tell" or "No" were not gathered: the eighteen-month row and the intangible-lives row reach neither an item nor "Also noted", although the prompt says to collect "rows in tables" and "every item with a reading other than ordinary, including can't tell". Observed once | Add to the gather step "every row of the stayed-the-same table whose Still fits? is not yes", and have each merged item list the evidence lines it absorbed, so a dropped row is visible |
| PR38 | Prompt 4, section list and Part 2 | The maintenance-cost sentence "longer holding periods" (FY2013 p. 53) sits in the MD&A expense discussion, which the nine-section list does not reach, and Part 2's "wherever it appears" covers statements of lives and holding periods, not sentences that give a direction. Missed in v0.2 (PR28) and again here | In Part 2, also list every sentence in either report that gives a direction to a holding period, useful life or residual value (longer, shorter, extended, lower), with its page, and set each beside the depreciation items |
| PR39 | Prompt 5, sizes | Item 1 carries three sizes and the Shown line does not say which governs its rank above a larger single income effect; v2.22 added the rule after this reply, but not the display. Observed once | On the Shown line, mark the governing size ("ranks on 23%") |

### Pack

| # | Defect | Effect | Fix |
|---|---|---|---|
| PK9 | The manual pack labelled "full" holds five files (two 10-Ks, two Q4 releases, the workbook); the key's K1 to K4, K7, K8 and K15 rest on the 2013 10-Qs, the Q3 2013 release and the proxies, which the test-data pack does not hold | Seven of fifteen K items unreachable, five of them required; the key's pass bar cannot be applied as written | Add the 2013 10-Qs and the Q3 2013 release to the manual pack, or record in the key which K items each file set can reach |
| PK10 | Workbook FY2012 pre-tax income is 450.5 (FY2012 10-K p. 113) while the FY2013 10-K's "as previously reported" column gives 450.6 (p. 84); the replies use both | A 0.1 difference; growth rounds to 47.2% either way; cosmetic | None needed; a note on the Revisions sheet if it recurs |
