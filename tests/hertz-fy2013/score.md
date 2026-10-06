# Score: T1 Hertz, prompts v0.2, Claude Code dry run (F1 to F4)

Scorer: independent, blind to the runs until they finished. Scope: F1-output.md, context-sheet.md, F2-output.md, F3-output.md, F4-output.md and ledger-F1.csv to ledger-F4.csv in `runs/v0.2-claude-code/`. F5 is scored separately, so K7, K11 and K15 (F5 items) are marked out of scope here. All recomputation, locator and quotation checks were run in Python over `pack/` (scripts: `score_lib.py`, `recompute.py`, `quotes.py` in the scorer's scratchpad). Pack locators below use the manifest IDs (P-numbers) and printed page markers.

## Verdict

**FAIL against the suggested pass bar, on one condition: K5 is not caught at P1.** The run caught half of K5 (the car holding-period range widening from 4 to 28 to 4 to 36 months, at P1 in F4-D3-01 and P2 in F3-C8-02) and missed the other half (the unchanged "eighteen months" average), although F4's own search regex matched the sentence. Every other condition of the bar is met: five of K1 to K6 pass or partially pass, there are zero trap hits, and G1 and G2 hold.

The bar is failed narrowly and for a real reason: the "eighteen months" sentence is in the pack (P59 p.11; P30 p.11) and no step read it. At the same time the run found, from pack evidence alone, the residual-value half of the order's depreciation case (order ¶23), which the answer key assumed was invisible. Several answer-key items are wrong on the pack (section 11), and they should be fixed before the next run is scored.

| Condition | Required | Result | Met |
|---|---|---|---|
| K5 at P1 | P1 row: 2013 "eighteen months" and "4 to 36" against 2012 "18" and "4 to 28" | Range half at P1 (F4-D3-01); average half missed | **No** |
| Five of K1 to K7 at expected priority or partial | 5 | K1 partial, K2 pass, K3 partial, K4 pass, K5 partial, K6 miss, K7 out of scope (F5) | Yes (5) |
| Zero trap hits | 0 | 0 (T1 checked in detail: pack-supported, not a hit) | Yes |
| G1 no characterization | holds | Banned words appear only in F3's self-check code | Yes |
| G2 nothing after 31 March 2014 | holds | No post-cut-off fact; no reliance on the SEC order | Yes |

### Scoring table

| ID | Req./bonus | Caught by (row) | Priority | Score | One-line reason |
|---|---|---|---|---|---|
| K1 | Req. | F4-D3-04 (Q2 rate-change amount quoted); F4 section 4.13 | P1 | Partial | Right filing and disclosure at P1, but the row challenges the residual-value basis, not the omitted holding-period change |
| K2 | Req. | F4-D3-04 (check 3) | P1 | Pass (different route) | "Inconsistent" on pack evidence: same filing's disposal losses and the Q2 call slide "Auction/dealer residuals softer than expected" |
| K3 | Req. | F4-D3-05; F4 section 4.13 | P1 | Partial | As K1, for Q3 |
| K4 | Req. | F4-D3-05 (check 3) | P1 | Pass (different route) | "Inconsistent" on the same 10-Q's own statement that a loss on vehicle sales raised depreciation; no claim that Q3 residuals fell |
| K5 | Req. | F4-D3-01 (P1), F3-C8-02 (P2): range only | P1 / P2 | Partial | "Eighteen months" never quoted; bar condition failed |
| K6 | Req. | none | none | Miss | The FY2013 MD&A "longer holding periods" maintenance sentence (P62 p.53) is not quoted anywhere |
| K7 | Req. (F5) | out of scope | n/a | n/a | F5 item |
| K8 | Bonus | F4-D3-03 | P1 | Pass (over-prioritized) | Q1 sentence quoted with locator; pack evidence exists, but P1 is too high for a $3.3m quarter |
| K9 | Bonus | F3-C5-01 (annual), F4-D3-01 (annual and same-quarter) | P2 / P1 | Pass | Computed in code on the fleet base, direction stated; recomputed |
| K10 | Bonus | F3 Table 2 | n/a | Pass on computation; key wrong | DEPI is 0.8985 (0.9359 fleet-in); a longer-held fleet lowers net PP&E, so net-basis DEPI falls, not rises |
| K11 | Bonus (F5) | out of scope | n/a | n/a | F5 item |
| K12 | Bonus | F2 section 3.1, F2-A3-01, F2-A3-02, F2-A4-01 | P3 / P4 | Pass | Allowance rate and write-off coverage FY2009 to FY2013 in code; no subrogation mechanism claimed |
| K13 | Bonus | context sheet E9; F2, F3 P4 rows | P4 | Pass, with two precision notes | Event dated and located; P4 rows cite it; Dollar Thrifty appears in the benign readings of F3-C8-02 and F4-D3-01 |
| K14 | Bonus | F1-C15-1 | P3 | Pass | FY2013 10-K revision language quoted with locators; $235m never cited |
| K15 | Bonus (F5) | out of scope | n/a | n/a | F5 item |
| G1 | Global | all | n/a | Holds | See section 3 |
| G2 | Global | all | n/a | Holds | See section 3 |

Measurement results: 30 of 30 recomputed numbers match; 27 of 27 locators open to the cited text (one gives the right line but not the page); 21 of 21 quotations are verbatim; 71 of 71 ledger rows carry a benign reading before the adverse one; 17 of 17 P4 rows cite a context-sheet event; all ten F4 consistency checks have a result.

## 1. K items

Scorer's own pack locators for the target sentences (confirmed in code):

- Q2 2013 10-Q, rate adjustment with amount: "These depreciation rate changes resulted in net decreases of $14.8 million and $15.5 million in depreciation expense for the three-month and six-month periods ended June 30, 2013" [P246 p.38; P234 p.14]. Next sentence: "Prospective changes include the impact of car sales channel diversification and acceleration of our retail sales expansion."
- Q3 2013 10-Q: U.S. rate changes "resulted in net decreases of $18.0 million and $35.3 million" [P266 p.42; P254 p.14], with the same two-driver "Prospective changes" sentence.
- FY2013 10-K note 8: "The favorable adjustments reflect changes from the impact of car sales channel diversification, acceleration of our retail sales expansion and the optimization of fleet holding periods related to the integration of Dollar Thrifty." [P74 p.126]. The FY2013 MD&A gives "optimization of fleet holding periods related to the integration of Dollar Thrifty" as a reason for lower U.S. monthly per-vehicle depreciation [P62 p.42].
- Average holding period: FY2011 "fourteen months in the United States" [P2 p.13]; FY2012 "eighteen months" [P30 p.11]; FY2013 "eighteen months" [P59 p.11].
- Range: "Cars | 4 to 26 months" [P11 p.94], "4 to 28" [P39 p.81], "4 to 36" [P68 p.91].
- Maintenance: "vehicle maintenance costs of $9.6 million due to the expansion of our off-airport and leisure businesses, longer holding periods and the impact of recalls" [P62 p.53]. The order's words "extended holding periods" appear in the pack only in the Q4 2013 call slides: "Higher maintenance costs from extended holding periods" [P296 slide 11].

**K1. Partial.** No row quotes the Q2 "adjusted on certain vehicles ... to reflect changes in the estimated residual values" sentence. F4-D3-04 (P1, check 3) quotes the Q2 MD&A per-vehicle sentence and the note's "$14.8 million" rate change [P246 p.38; P234 p.13-14] and challenges the residual-value basis of the cut. F4 section 4.13 separately records that the Q2 and Q3 notes add the two-driver "Prospective changes include ..." sentence, and section 4.8 item 20 records that the FY2013 note names a third driver, holding-period optimization. The pack supports a clean K1 row here: the interim filings list two drivers for the 2013 rate cuts, and the annual filing lists three for the same cuts. The tool had both sentences and did not join them. The key's pass criterion ("the filing gives no dollar effect") is wrong on the pack (see AK1); a row asserting that would have been false.

**K2. Pass (different route).** F4-D3-04, P1, check 3 "inconsistent". It quotes "due to improved residual values in the U.S." and "residuals have remained relatively strong during the period" [P246 p.38, verified]. It sets these against the same 10-Q's disposal result, "net losses of $17.5 million and net gains of $38.3 million" [P234 p.13, verified], and the Q2 call slide "Auction/dealer residuals softer than expected" [P292 slide 11, verified]. It records the $14.8m Q2 figure; the order's "$15 million" is the $15.5m six-month rate-change effect (AK2). This is none of the key's three outcomes. It is a pack-grounded version of the order's first limb (the residual-value attribution was inaccurate [order ¶23]), which the key assumed could not be reached. The row misses the order's second limb (the holding-period effect), and its benign column does not list the company's own other reasons (non-program mix, mix optimization, procurement), which the key asks for.

**K3. Partial.** F4-D3-05 (P1) quotes the Q3 MD&A "due to residual values that remained strong in the U.S." [P266 p.41] and the "$18.0 million" U.S. rate change [P254 p.14]. As with K1, the omission of holding periods from the Q3 driver list is not stated as a finding.

**K4. Pass (different route).** F4-D3-05 sets the "remained strong" sentence against the same 10-Q MD&A: "a loss realized on vehicle sales in the third quarter of 2013, compared to gains realized on vehicle sales in the third quarter of 2012" [P266 p.50, verified]. It also cites U.S. disposal losses of $11.1m against gains of $15.2m [P254 p.14, verified]. The row does not assert that Q3 residual values fell; it records a tension between two statements in one filing. The key's rule that "a P1 claiming Q3 residual values fell is a trap hit" does not apply, and should be narrowed (AK4).

**K5. Partial; bar condition failed.** F4-D3-01 (P1, check 2 "inconsistent") and F3-C8-02 (P2) quote the range for all three years with correct locators [P11 p.94; P39 p.81; P68 p.91, verified]. Neither quotes the "eighteen months" average. F4's "Looked for and not found" lists "average holding period" as searched only in P74, P63, P62 and P77, not in Item 1. Its check-2 regex (`holding period`, s3_search.py) runs over every text file and therefore matched P30 and P59. F3 reports 48 "holding period" hits and still writes "average holding period by year: not found in Notes 2 and 8 or MD&A". Both runs had the hit and did not read it (PR28). The FY2011 figure of fourteen months, rising to eighteen in FY2012, was also missed.

**K6. Miss.** The P62 p.53 maintenance sentence is not in any output, and neither are the P296 slide words. Both contain "holding period" and match F4's check-2 regex.

**K7.** F5 scope. For the F5 scorer: the 26 September 2013 revision document is not in the pack (see PK7), but the Q3 release says "The Company confirms its revised guidance which it issued on September 26, 2013" [P293 p.5].

**K8. Pass (bonus), over-prioritized.** F4-D3-03 quotes the Q1 MD&A "driven primarily by an increase in residual values and corresponding lower depreciation rates" [P225 p.42] and "residuals remained fairly strong" [P225 p.35]. This is a different Q1 sentence from the one the order tracks (P225, line 138), with the same substance. The contrary evidence is real (Q1 net loss of $3.3m against a $34.9m gain [P213 p.13]), but a $3.3m loss and a $0.7m rate change do not carry P1. P3 fits.

**K9. Pass (bonus).** F3-C5-01 computes fleet depreciation over average gross fleet as 0.1629, 0.1527, 0.1460 and 0.1447 (FY2010 to FY2013), on P1's "Equipment held for rental or lease, gross", which includes the fleet. The scorer recomputed FY2010 and FY2013 (N14, N15). F4-D3-01 gives the note-based provision rate (16.22%, 15.28%, 14.25%) and same-quarter changes for Q1 to Q4 2013 of -2.17, -1.33, -1.07 and -1.33 pp. The scorer recomputed Q2 as 13.62% against 14.95%, a change of -1.33, and FY2011 from 1,921.8 [P16 p.125]. Precision note: F4-D3-01's benign reading includes "Dollar Thrifty cars entered at fair value (E9)". That is a mix argument and a fair one, but K13's rule asks that the acquisition not be offered as the explanation.

**K10. Pass on computation; the key's expectation is wrong.** DEPI for FY2013/FY2012 is 0.8985 on the workbook mapping and 0.9359 with the fleet in PP&E (N22, N23, both recomputed). Both are below 1. DEPI uses depreciation / (depreciation + net PP&E). Longer holding periods raise accumulated depreciation, so the net base shrinks and the rate on net rises. The key's inference that DEPI would exceed 1 does not hold on a net-basis index (AK5). The pair is labelled non-comparable and the contribution is shown (+0.1033).

**K12. Pass (bonus).** F2 section 3.1 computes, in code, the allowance rate (1.58%, 1.43%, 1.24%, 1.31%, 2.00%) and write-off coverage (0.90, 1.04, 0.98, 0.86, 0.96) for FY2009 to FY2013 from NOTES (Schedule II) and BS_A, plus an FY2012-as-revised column. FY2013 is the least adverse value, so no row is required. F2 quotes the only subrogation reference in the pack, "Receivables include customer receivables, subro receivables, warranty, and other misc." [P270 slide 37, verified], and makes no mechanism claim. It does not say outright that subrogation cannot be isolated; it should. Scorer's computation for the key: the order's $9.3m of year-old subrogation receivables would be 0.60% of FY2013 gross receivables but 30.2% of the FY2013 allowance. The consolidated rate could hide it, but only if it had been reserved at a low rate. F2-A3-02 (a $4.0m FY2013 gap between the cash-flow provision and Schedule II, recomputed as N10) is a legitimate small lead in the same area.

**K13. Pass (bonus), with precision notes.** Context sheet E9 gives the date (2012-11-19), the allocation and its locators. The rows that cite E9 sit at P4 (F2-A1-01, F2-A13-01, F3-B4-02, F3-B4-03, F3-B5-01, F3-B6-01, F3-C17-02). The M-score pairs are labelled non-comparable (F3 Table 2). F2-A16-01 is correctly kept above P4, with the stated reason that E9 does not explain a fall below the pre-acquisition level. Precision failures under the key's rule: F3-C8-02's benign reading, "The ranges describe the fleet and assets in place (Dollar Thrifty vehicles ...)", and F4-D3-01's "Dollar Thrifty cars entered at fair value". Against that, the company itself ties holding periods to Dollar Thrifty [P74 p.126; P62 p.42], so citing that sentence as the company's explanation is legitimate. The key's rule needs revising (AK6).

**K14. Pass (bonus).** F1-C15-1 (P3) quotes "During the fourth quarter of 2013, we identified certain out of period errors totaling $46.3 million ..." [P68 p.83, verified] and the release's "$47.9 million" [P295 p.9, verified]. The $235m is not cited anywhere.

## 2. Traps

No output claims any of T1 to T16 without a pack quotation. Detail on each trap:

- **T1 (Q2 2013 residual values declined).** Not a hit. F4-D3-04's adverse reading ("management's own slides describe softer auction residuals") rests on the Q2 call slides, furnished on Form 8-K on 1 August 2013 and in the pack. They read "Residuals coming off historic peak Manheim down 4.4% YoY Q2:13; Moody's forecasted down 2.2% Auction/dealer residuals softer than expected" [P292 slide 11, verified]. The same 10-Q's disposal losses are also cited [P234 p.13]. The key's claim that the decline was "not stated in any filing" is too broad for this pack (AK3).
- **F3-C8-01 (P1).** Legitimate catch. Both sentences are verbatim in one note: "The cumulative effect of the reduction in rates was also indicative of the residual values experienced in the U.S. for the years ended December 31, 2013, 2012 and 2011." and "The loss on vehicle sales ... was primarily due to a combination of declining residual values from falling demand for used vehicles and timing of sales" [P74 p.126, both verified]. The MD&A adds "a deterioration in the used vehicle residual values" [P62 p.54, verified]. This is a stated tension inside one filed note about the same year, which is the P1 definition. One weakness: the benign column says losses "arose on cars sold after residuals weakened late in the year", but the row's own path shows a U.S. loss in H1 already (-9.4), so "late in the year" overstates it.
- **F4 check 3 result ("inconsistent", four periods).** Legitimate on the pack text for Q2, Q3 and FY2013 (locators above and N29, N30). Q1 is legitimate but over-prioritized (K8).
- **T2 to T4, T6.** No hits: "planned holding", "21 to", "25 months" and "24 or 30" do not occur, and "eighteen" never appears. F3-C8-02 and F4-D3-01 both say the holding-period effect is not quantified, which is correct.
- **T5.** No "affirmative decision" and no peer comparison. Near-miss: F4-D3-06's benign column paraphrases P74's "optimization of fleet holding periods" as "longer holding periods" [P74 p.126]. Other pack text supports the direction (P62 p.53; the range widening), but the row cites only P74 (PR34).
- **T7 to T11, T13.** No hits: no occurrences of attorney, rolling average, spreadsheet, 9.3 million, 4 or 11 percent, post-close or audit committee.
- **T12.** No hits: no internal estimates and no budget pressure. "1.78" occurs only as the M-score cutoff.
- **T14.** No hits: no $235m, no count of areas or material weaknesses, no "tone at the top". "Oracle" appears only as the pack's own control text, "the Company implemented Oracle general ledger ..." [P87 p.159], in E19 and F1-E4-2, with no claim of a weakness.
- **T15.** No post-cut-off events. "Estero, Florida" appears only in pack quotations [P60 p.26; P62 p.65]. "June 2014" appears only in the convertible-notes title inside a quotation [P295].
- **T16.** Not a hit. Vendor incentives and Brazil allowances are named from the FY2013 10-K's own "Correction of Errors" note [P68 p.83], which is in the pack.

Trap count: **0**.

## 3. G1 and G2

**G1 holds.** The banned words (fraud, manipulation, aggressive, red flag, suspicious, concerning) occur only in F3's self-check code (F3-output.md line 1607). "Misstatements" occurs once, in F4-C10-02, where it paraphrases the Ramirez complaint's allegation ("alleging misstatements"), with a quotation of the class period [P61 p.138]. It is attributed to the plaintiffs, not asserted by the tool. Adverse readings are hedged ("may", "can reflect"). F4's summary closes "These are candidates for review, not findings."

**G2 holds.** No fact is dated after 31 March 2014. The latest pack items used are the FY2013 10-K (19 March 2014), the 10-K subsequent-events note on the planned separation [P85 p.150] and the 20 March 2014 slides [P296]. No output cites the SEC order, the restatement or any 2014 announcement. F3's reference to Beneish and Vorst (2022) is screen-calibration literature supplied by the prompt, not a fact about Hertz. The log records that the runner had a project CLAUDE.md in context. Nothing in the outputs suggests knowledge of the order, and the K5 and K6 misses argue against leakage.

## 4. Computed numbers (30 sampled: 13 from F2, 17 from F3)

Recomputed in Python from statements.xlsx (P1) and the cited text inputs. Text inputs were verified first: 33.9 [P21], -130.6 and +0.5 [P45], -35.3, -18.0 and -20.5 [P254 p.14], -44.2 and -48.2 [P74 p.126]. Tolerance: the output's rounding.

| # | Row | Measure | Reported | Recomputed | Result |
|---|---|---|---|---|---|
| N1 | F2-A16-01 | Accrued / revenue FY2013 (%) | 10.26 | 10.2554 | match |
| N2 | F2-A16-01 | Accrued / revenue FY2009 (%) | 14.43 | 14.4308 | match |
| N3 | F2-A16-01 | FY2013 accruals at FY2012-revised intensity | 1,388.2 | 1,388.25 | match |
| N4 | F2-A16-01 | Payables + accruals ex fleet / revenue FY2013 (%) | 16.56 | 16.557 | match |
| N5 | F2-A16-02 | PL&PD reserve / revenue FY2013 (%) | 3.23 | 3.2278 | match |
| N6 | F2-A2-01 | Gross receivables growth FY2011 (%) | 18.9 | 18.92 | match |
| N7 | F2-A1-01 | Q4 FY2012 ending DSO | 74.9 | 74.86 | match |
| N8 | F2-A1-01 | Q4 FY2011 average DSO | 82.5 | 82.52 | match |
| N9 | F2-A1-01 | FY2011 ending DSO ex fleet receivables, change | 2.7 | 2.65 | match |
| N10 | F2-A3-02 | CF provision minus Schedule II FY2013 | 4.0 | 4.0 | match |
| N11 | F2-A13-01 | Margin proxy change FY2012 (pp) | 1.0 | 1.01 | match |
| N12 | F2-A16-03 | Restructuring "other" / pre-tax FY2011 (%) | 10.45 | 10.453 | match |
| N13 | F2-A14-01 | Q4 FY2013 DPO change vs Q4 FY2012 | -12.9 | -12.90 | match |
| N14 | F3-C5-01 | Fleet dep / avg gross fleet FY2013 | 0.1447 | 0.1447 | match |
| N15 | F3-C5-01 | Same, FY2010 | 0.1629 | 0.1629 | match |
| N16 | F3-C5-01 | Net fleet capex / fleet dep FY2013 | 1.241 | 1.2410 | match |
| N17 | F3-C5-01 | Rate-change effect / pre-tax FY2012 | -0.2888 | -0.2888 | match |
| N18 | F3-C17-01 | CFO / income FY2013 | 10.37 | 10.369 | match |
| N19 | F3-C17-01 | FCF after net fleet capex FY2012 | -82.9 | -82.9 | match |
| N20 | F3-B4-02 | SGI FY2013 | 1.1941 | 1.1941 | match |
| N21 | F3-B4-03 | SGAI FY2013 | 0.9051 | 0.9051 | match |
| N22 | F3 Table 2 | DEPI FY2013, workbook mapping | 0.8985 | 0.8985 | match |
| N23 | F3 Table 2 | DEPI FY2013, fleet in PP&E | 0.9359 | 0.9359 | match |
| N24 | F3-B5-01 | Soft assets FY2013 | 0.9212 | 0.9212 | match |
| N25 | F3-B6-01 | Change in cash sales FY2013 | 0.2737 | 0.2737 | match |
| N26 | F3 Table 1a | CF accruals / avg TA FY2013 | -0.1355 | -0.1355 | match |
| N27 | F3-B4-01 | GMI FY2013 | 0.9942 | 0.9942 | match |
| N28 | F3-B1-01 | FY2013 receivables difference not traced | 102.8 | 102.8 | match |
| N29 | F3-C8-01 | U.S. rate change H1 2013 (9M less Q3) | -17.3 | -17.3 | match |
| N30 | F3-C8-01 | U.S. disposal result Q4 2013 derived | -27.7 | -27.7 | match |

30 of 30 match. The scorer also spot-checked F4 (not in the sample): FY2011 provision rate 16.22% and Q2 2013 same-quarter change -1.33 pp both reproduce, and so do the per-car disposal figures (-250 against +857; -275 against +578).

## 5. Locators (27 sampled across F1 to F4)

| # | Row | Locator | Found | Result |
|---|---|---|---|---|
| L1 | F1 E23, F1-E4-1 | P71 p.108 | p.108 | ok |
| L2 | F1-C15-1 | P295 p.9 ($47.9m) | p.9 | ok |
| L3 | F1-C15-1 | P68 p.83 ($46.3m) | p.83 | ok |
| L4 | F1 E26 | P85 p.150 | p.150 | ok |
| L5 | F1 E19 | P87 | p.159 | ok |
| L6 | F1-C15-2 | P131 p.7 | p.7 | ok |
| L7 | F2-A14-01 | P62 p.64 | p.64 | ok |
| L8 | F2-A3-02 | P66 p.101 | p.101 | ok |
| L9 | F2-A4-01 | P68 p.90 | p.90 | ok |
| L10 | F2-A11-01 | P66 p.75 | p.75 | ok |
| L11 | F2-A16-02 | P34 p.45 | p.45 | ok |
| L12 | F2-A7-01 | P71 p.112 | p.112 | ok |
| L13 | F3-C8-01 | P62 p.54 | p.54 | ok |
| L14 | F3-C2-01 | P62 p.50 | p.50 | ok |
| L15 | F3-C3-01 | P285 p.10 | p.10 | ok |
| L16 | F3-C17-02 | P295 "p. 2 and Table 7, line 599" | FCF sentence p.2; footnote at line 599, on p.9 | ok (footnote page not stated) |
| L17 | F3-C8-02 | P11 p.94 | p.94 | ok |
| L18 | F4-D3-03 | P225 p.42 | p.42 | ok |
| L19 | F4-D3-04 | P292 p.11 | slide 11 | ok |
| L20 | F4-D3-05 | P266 p.41 | p.41 | ok |
| L21 | F4-D2-04 | P60 p.26 | p.26 | ok |
| L22 | F4-C10-01 | P61 p.137 | p.137 | ok |
| L23 | F4-C6-02 | P265 p.37 | p.37 | ok |
| L24 | F4-D4-01 | P82 p.147 | p.147 | ok |
| L25 | F4-D3-02 | P68 p.93 | p.93 | ok |
| L26 | F4 4.12, D3-06 | P62 p.42 | p.42 | ok |
| L27 | F4-D3-05 | P266 p.50 (loss on vehicle sales) | p.50 | ok |

27 of 27 open to the cited text.

## 6. Quotations (21 checked, 8 from F3 and 13 from F4)

All 21 are verbatim after normalizing curly quotes and whitespace. F3: the P74 "indicative of the residual values experienced" sentence (p.126); "declining residual values from falling demand for used vehicles" (P74 p.126); the P62 "deterioration" sentence (p.54); the Corporate EBITDA footnote (P295 p.3); the 10-K adjusted pre-tax definition (P62 p.50); "Represents incremental costs ..." (P77 p.135); the $40m to $45m relocation sentence (P62 p.65); the Donlen residual guarantee (P68 p.91). F4: the Q2 per-vehicle sentence and "residuals have remained relatively strong" (P246 p.38); the fleet-cost risk heading (P60 p.23); the car supply sentence (P31 p.22); the multiemployer sentence (P60 p.26); the franchisee gains sentence (P39 p.84); the Q1 2012 "positive trending" sentence (P154 p.12); the P74 "favorable adjustments" sentence (p.126); "1% change to residuals = $83M adjusted pre-tax income" (P296 slide 21); the Sobel judgment sentence (P61 p.137); "slight strengthening of used vehicle residual values" (P62 p.43); the FY2012 "strong residual values" sentence (P45 p.113); the guidebooks sentence (P63 p.45). F4 reports verifying all 95 of its quotations in code, which is consistent with this sample.

## 7. Benign-first

All 71 ledger rows (F1 7, F2 13, F3 18, F4 33) have a non-empty benign reading, and in every CSV the Benign column precedes the Adverse column. Three F4 rows have no real adverse reading ("None beyond ..."): F4-C10-04, F4-C14-01 and F4-A4-02. F1-C16-1 has only a trivial one. These should not be rows (section 9).

## 8. Context-sheet use

- All 17 P4 rows cite at least one context-sheet event (F2 6, F3 6, F4 5).
- Rows above P4 that an event plainly explains:
  - F1-C15-3 (P3): presentation-only cash-flow revisions E1, E12, E17. F3-C19-01 carries the same item at P4.
  - F4-D2-06 (P3): its own benign reading names E9.
  - F3-C3-03 (P3): its benign reading says each new category matches E9, E10 or E13. This one is borderline, because the undefined-labels point is not explained by the events.
- Context-sheet gaps found through later steps:
  - The headquarters relocation (announced May 2013 [P228 p.8]; $21.9m in restructuring [P62 p.44]) is not an event. F3 says so ("restructuring and relocation are not on the context sheet"), and F4-D2-04 and F4-D4-01 rely on it.
  - The 26 September 2013 guidance revision, confirmed in the Q3 release [P293 p.5], is not an event.

## 9. Rows that should not exist, or are wrongly prioritized

**Noise (not supported as a signal by the evidence cited):**

- F1-C16-1: clerical 10-K/A exhibit correction; no adverse reading.
- F2-A7-01: search artefact; already recorded as PR12.
- F2-A11-01: inventory is 0.38% of assets.
- F3-C3-02: one mislabelled row in a furnished table, with no effect on the total.
- F3-C7-01: standard "net of amounts capitalized" caption; nothing suggests material capitalization.
- F4-C10-04: SEC investigation closed with no action.
- F4-C14-01: duplicates F1; adverse "None beyond".
- F4-A4-02: duplicates E24 and F2-A4-01; adverse "None beyond".
- F4-D2-02: speculative reading of a deleted sentence.
- F4-C13-02: volatility method change with a stated reason, in 2012.
- F4-D2-04: describes a known event.

**Wrongly prioritized:**

- **F4-D3-02 (P1, should be P3 or dropped).** "Other intangible assets | 3 to 10 years" is a line in the property-and-equipment lives table [P68 p.91]. "Two to fifteen years" covers all finite-lived intangibles, including concessions and customer relationships [P68 p.93]. The two statements have different scopes, so this is not a stated contradiction. The row's own benign reading says so.
- **F4-D3-03 (P1, should be P3).** Q1 2013: a $3.3m disposal loss and a $0.7m rate change.
- **F4-D3-07 (P1) against F3-C2-01 (P2), same item.** The non-recurring label is the credit-agreement definition in furnished releases. The filed use is "one-time" in a segment measure. Whether Item 10(e) reaches either is unsettled (PR20). P2 fits, and the two steps disagree.
- **F2-A16-01 (P2, arguably P3).** The second "independent signal" is a balance-sheet line consolidation, which is presentation.
- **F1-C15-3 (P3, should be P4).** See section 8.

Count of section 5 benign items rated P1 or P2 with no other signal: **0**.

## 10. Overall judgment

**What the prompts do well on this pack.**

- **Arithmetic and sourcing are clean.** Every sampled number, locator and quotation checks out.
- **Discipline holds.** Benign readings come first on every row, P4 rows cite their events, the vocabulary stays neutral, and nothing leaks past the cut-off.
- **The fleet-depreciation cluster was found from inside the pack.** F3 and F4 converged independently on the right account and period, and all four readings are legitimate:
  - the FY2013 note's internal tension (F3-C8-01);
  - the Q2 and Q3 explanations against same-filing disposal losses and the company's own Q2 slides (F4-D3-04, F4-D3-05);
  - depreciation per unit of gross fleet falling in every 2013 quarter (F4-D3-01);
  - the range widening (F3-C8-02, F4-D3-01).
- **The residual-value limb of the order was reached from the pack.** This is the part the key assumed required inside knowledge (order ¶23: "a fact discussed within Hertz"). The pack's own furnished slides say it.

**What they do badly.**

- **Search hits are not read across all sections.** The holding-period sentences in Item 1 ("eighteen months") and in the MD&A cost discussion ("longer holding periods") were matched by F4's regex and never read. That is the whole of K5's average half and all of K6, and it is the difference between pass and fail.
- **Related readings are not joined into one row.** F4 quoted the interim two-driver sentence and the annual three-driver sentence and left them in separate sections, so the cleanest pack route to K1 and K3 went unused.
- **Rows are over-produced.** F4 has 33 rows, 19 of them P3, and about a third of all rows across the four steps are noise.
- **P1 is inflated in F4.** Two of its seven P1s do not meet the definition.
- **Priorities disagree across steps** for the same item.

## 11. Answer-key defects (fix before the next scoring)

| # | Item | Defect | Evidence | Fix |
|---|---|---|---|---|
| AK1 | K1, K3 | Pass criterion "the filing gives no dollar effect" is false on the pack | Q2: "net decreases of $14.8 million and $15.5 million" [P246 p.38; P234 p.14]; Q3: "$18.0 million and $35.3 million" [P266 p.42; P254 p.14] | Criterion: the row states that the interim filings attribute the rate cuts to residual values, channel diversification and retail expansion, and do not name holding periods, which the FY2013 note later names for the same year [P74 p.126] |
| AK2 | K2, K4 | "Scope of the $15m / $18m unknown" is resolved by the pack | The $15m is the H1 rate-change effect ($15.5m), with $14.8m in Q2; the $18m is the Q3 U.S. rate change | Replace the vagueness note with these locators |
| AK3 | T1 | "Not stated in any filing" is too broad | Q2 call slides, furnished 1 August 2013: "Residuals coming off historic peak Manheim down 4.4% YoY Q2:13 ... Auction/dealer residuals softer than expected" [P292 slide 11] | Narrow T1 to Hertz's internal residual data. A market-level decline is pack-visible, and a K2 "inconsistent" resting on P292 is a pass |
| AK4 | K4 | "A P1 claiming Q3 residual values fell is a trap hit" ignores pack text | Q3 10-Q: "a loss realized on vehicle sales in the third quarter of 2013" [P266 p.50]; U.S. disposal loss $11.1m [P254 p.14] | Trap hit only without a pack locator |
| AK5 | K10 | Expected direction is wrong for a net-basis DEPI | DEPI 0.8985 (0.9359 fleet-in); an older fleet has a lower net base | Drop K10, or restate it as "DEPI not expected above 1; note why" |
| AK6 | K6 | The quoted phrase is not the 10-K's wording | 10-K MD&A: "longer holding periods" [P62 p.53]; "extended holding periods" only in the Q4 slides [P296 slide 11] | Quote the pack's sentence and accept either locator |
| AK7 | K5, K6, K13 | The key omits the pack's strongest holding-period sentences | "optimization of fleet holding periods related to the integration of Dollar Thrifty" [P74 p.126; P62 p.42]; FY2011 average "fourteen months" [P2 p.13] | Add them to K5 and K6. Revise K13: quoting the company's own Dollar Thrifty attribution is allowed; offering the acquisition by itself as the benign reading is not |

## 12. New defects

### Prompt defects

| # | Prompt | Defect | Proposed change |
|---|---|---|---|
| PR28 | F4 (check 2), F3 (step 6) | Check-2 search hits outside the notes are not read: "holding period" matched Item 1 and MD&A sentences (P30, P59, P62 p.53), but the "average" search was run only on P74, P63, P62 and P77, and F3 reported 48 hits yet "not found" | For check 2, tabulate every hit that states a life, holding period or average with a number (normalize number words: "eighteen" to 18), in every section including Item 1 and the slides, year over year |
| PR29 | F4 (step 3) | The mechanical filter (numbers-only changes, 6,462 sentences) can bury estimate changes such as 14 to 18 months | Sentences that match any consistency-check term are never classed as mechanical |
| PR30 | F3, F4 | No step compares the drivers an interim filing gives for an estimate change with the drivers the annual filing gives for the same year | Add to check 3: list the stated drivers per filing for each quantified estimate change, and flag any driver that first appears in a later filing |
| PR31 | F1 to F4 | Same item, different priorities across steps (non-recurring label P2 in F3, P1 in F4; cash-flow revisions P3 in F1, P4 in F3) | A shared rule: a later step citing an earlier row's item takes that row's priority unless it adds a new signal, and says so |
| PR32 | Shared ledger block | Rows allowed with no adverse reading ("None beyond ...") | A row needs an adverse reading; otherwise record the item in "Looked for" or the context sheet |
| PR33 | F2 to F4, P1 definition | "Stated contradiction" fired on statements of different scope (F4-D3-02) and on immaterial amounts (F4-D3-03) | P1 requires the same subject, period and measure in both statements, plus a size note; otherwise P3 with the scope difference stated |
| PR34 | Shared rules | A paraphrase went beyond its source ("longer holding periods" for P74's "optimization of fleet holding periods") | When a row paraphrases a filing, keep the filing's operative word or quote it |
| PR35 | F1 | The event search missed the headquarters relocation programme and the 26 September 2013 guidance revision | Add programme announcements (restructuring, relocation) and guidance changes confirmed in releases to the event log search |

### Pack defects

| # | Defect | Effect | Fix |
|---|---|---|---|
| PK7 | Guidance and investor-presentation 8-Ks under Items 7.01 and 8.01 outside earnings dates are not in the pack; events.txt covers only Items 2.01, 4.01, 4.02 and 5.02. The 26 September 2013 revision and conference deck are absent | K7 (F5) can only be scored against the 4 November confirmation [P293 p.5] | Include every 8-K furnishing guidance or investor materials in the window, or list them in events.txt with dates so the tool can name what is missing |
| PK8 | The manifest does not state that the furnished call slides (OTHER files) carry management commentary on residual values and sensitivities that the 10-Qs lack | Scorers and key writers treat them as immaterial; the key's T1 was written without them | Add a manifest note on the content types in OTHER files (slides with KPIs, residual commentary, sensitivities) |
