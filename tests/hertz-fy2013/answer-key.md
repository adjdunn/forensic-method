# Answer key: Hertz Global Holdings, pack as of 31 March 2014

**Scorer only. Never attach this file to a prompt run.**

> **Addendum, 25 September 2026, after the v0.2 dry run.** This key was written before any prompt ran and is kept unchanged below, so the pre-run version stays on record. The scorer found seven errors in it (AK1 to AK7, detailed in score.md). The ones that change scoring:
> - **K1 and K3.** The Q2 and Q3 2013 10-Qs do give dollar effects for the depreciation-rate changes: $14.8m and $15.5m in Q2, $18.0m in Q3. The "no dollar effect" criterion is wrong.
> - **K6.** The FY2013 10-K says "longer holding periods", not "extended". The search phrase is wrong.
> - **K10.** DEPI is below 1 on this pack: 0.8985, or 0.9359 with the fleet as PP&E. K10 cannot be met as written.
> - **K5, K6 and K13.** The key omitted the 10-K's own sentence tying lower depreciation to "optimization of fleet holding periods related to the integration of Dollar Thrifty" (P74 p. 126; P62 p. 42).
> - **T1.** Its premise, that the residual decline appeared in no filing, is too broad. The Q2 2013 call slides in the pack say residuals were "softer than expected" (P292 slide 11).
>
> Future runs are scored against the key with these corrections applied.

> **Addendum, 7 October 2026, after the v2.22 and v2.23 harness runs.** The three scorecards under `runs/hertz-fy2013/v2.22/manual/001/scoring/`, `runs/hertz-fy2013/v2.22/claude-code/001/scoring/` and `runs/hertz-fy2013/v2.23/claude-code/001/scoring/` found five more defects (AK8 to AK12). AK1 to AK12 are now applied in the body of this key: each corrected statement is marked `[AKn, 7 October 2026]`, and the statement it replaces stays in place marked "superseded 7 October 2026 (AKn)", so the pre-run version remains on record. No K item's substance is changed beyond what a numbered correction says.
> - **K7 (AK8).** The pack's February 2013 range is adjusted diluted EPS $1.82 to $1.92 (Q4 FY2012 release pp. 4 to 5), not the order's $1.78 to $1.88, and the outturn is $1.63 (Q4 FY2013 release). "Ranges in date order" is scored against the pack's figures.
> - **K5 (AK9).** The verdict word is not the test. A row quoting both sentences for both years and setting them against each other passes when it is carried to the report at level 1, whatever the verdict word, and is partial when it stays in a table.
> - **Pass bar (AK10).** Stated per file set. On the five-file pack (two 10-Ks, two fourth-quarter releases, the workbook) only K5 and K6 are reachable: K5 at level 1, K6 at least partial, zero traps, G1 and G2.
> - **K9 (AK11, corrected by AK12).** On the five-file pack K9 requires the annual rates and the Q4 same-quarter rate, which the FY2013 release's supplementary table and the workbook's quarterly balance sheet allow; the Q2 and Q3 comparisons need the 10-Qs. AK11's "annual rates alone meet K9" is withdrawn.

**Source.** SEC, In the Matter of Hertz Global Holdings, Inc. and The Hertz Corporation, Securities Act Release No. 10601, Exchange Act Release No. 84979, AAER No. 4012, File No. 3-18965, 31 December 2018. https://www.sec.gov/files/litigation/admin/2018/33-10601.pdf. Local text: `research/sources/hertz-33-10601.txt`. Read in full for this key.

**Marks used here.**

- `[order ¶N]`: paragraph N of Section III of the order. `[order §II]`, `[order §IV.C]` and `[order fn 1]` for the other sections and the footnote.
- `[inf]`: my inference, with the reasoning written out. Not a finding of the order.
- `[brief]`: a fact supplied in the test brief that the order does not state. The order is silent on it; the scorer confirms it against the pack before scoring.
- `[F3 step 2]`, `[PACK-SPEC]` and similar: a reference to the prompt or pack-spec text in `tools/`, not to Hertz.
- `[conv]`: a scoring convention proposed here, not a fact.
- `[AKn, 7 October 2026]`: a correction applied under answer-key defect AKn (AK1 to AK7 in score.md section 11; AK8 to AK12 in the v2.22 and v2.23 scorecards). The text it replaces stays beside it, marked "superseded 7 October 2026 (AKn)". Locators of the form `[P246 p.38]` are the original pack's file IDs (`pack/`); "FY2013 p. 53" and "Q4 FY2012 release pp. 4 to 5" are the `[p. N]` markers in the five-file pack (`test-data/hertz-fy2013/`).

**What "visible" means in this key.** The order quotes or describes some sentences from Hertz's filings. It does not reproduce the filings. Where the order quotes, the scorer can expect the sentence in the pack. Where it paraphrases, the scorer must find the sentence in the pack before scoring the item, and this key says which is which. The findings were made on Hertz's offer of settlement, without admitting or denying them, and bind no other person [order §II; order fn 1].

## 1. Scope and cut-off

The pack holds what an analyst could read on 31 March 2014: the FY2011 to FY2013 10-Ks, the 2011 to 2013 10-Qs, earnings releases, two proxies and a statement workbook [brief]. The FY2013 10-K was filed in March 2014 [order ¶25], so it is the last filing in the pack. Everything the order describes after that date is outside the pack: the 13 May 2014 announcement that the Q1 2014 10-Q could not be filed [order ¶33]; the 6 June 2014 announcement that the 2011 statements should no longer be relied upon, with at least one material weakness and ineffective disclosure controls at 31 December 2013 [order ¶34]; the 14 November 2014 extension of non-reliance to 2012 and 2013 [order ¶35]; and the restatement filed with the FY2014 10-K on 16 July 2015 [order ¶5, ¶26, ¶35]. The order says the 6 June 2014 disclosure was "announced"; it does not name the form [order ¶34]. The filings the order found misstated run "from at least February 2012 through March 2014" [order ¶2], so every set of figures in the pack from the FY2011 10-K onward is as originally reported, before correction [inf, from ¶2 and the pack's date range]. A tool can find signals in those figures and sentences. It cannot find the restatement, and it cannot know the corrected numbers.

**File sets [AK10, 7 October 2026].** Two packs exist. The original pack (`pack/`) holds the 10-Ks, 10-Qs, releases, call slides and proxies described above. The five-file pack (`test-data/hertz-fy2013/`, per its `config.json`) holds the FY2012 and FY2013 10-Ks, the two fourth-quarter releases and the statements workbook, with no 10-Q, no interim release, no slides and no proxy. Each K item below says which document it needs, and the pass bar in section 6 is stated for each file set [conv].

## 2. Items the order says were visible in the filings at the time

Required items are K1 to K7. K8 is visible but the order does not call it deficient, so it is a bonus.

Priority below uses the prompts' definitions: P1 a stated contradiction or an absent rule-required disclosure; P2 two independent signals on one account and period; P3 a single signal; P4 a signal the context sheet explains [F2, F3, F4 section 7].

### K1. Q2 2013 10-Q: depreciation rates "adjusted", effect not stated

- **Order:** ¶22, with the rule at ¶21.
- **Quote from the order (quoting the filing):** "depreciation rates being used to compute the provision for depreciation of revenue earning equipment were adjusted on certain vehicles in our car rental operations to reflect changes in the estimated residual values to be realized when revenue earning equipment is sold" [order ¶22].
- **The order's finding:** "Hertz did not state in this Form 10-Q ... the significant adjustment it had made to extend the planned holding periods" [order ¶22]. ASC 250-10-50-4 requires the effect of a change in estimate affecting several future periods, such as a change in service lives, to be disclosed [order ¶21].
- **Filing and period:** Q2 2013 10-Q, filed 2 August 2013, MD&A, six months ended 30 June 2013 [order ¶22].
- **Checklist:** C5 (lives, salvage values, methods; text delta); D3.
- **Expected catch:** F4 consistency check 2, second arm ("a change is described as prospective with no disclosure of its effect"). F3 step 6 should also quote the sentence under "Text found".
- **PASS, superseded 7 October 2026 (AK1):** a row quoting the operative part of the sentence, with a locator in the Q2 2013 10-Q MD&A, stating that the filing gives no dollar effect for the adjustment. Expected P1 (F4 step 7: a rule-required amount that is absent is P1). A row at P2 or P3 is a partial pass.
- **PASS [AK1, 7 October 2026]:** the "no dollar effect" criterion is false on the pack. The Q2 2013 10-Q states "net decreases of $14.8 million and $15.5 million in depreciation expense for the three-month and six-month periods ended June 30, 2013" [P246 p.38; P234 p.14]. The criterion is instead: a row quoting the operative part of the sentence, with a locator in the Q2 2013 10-Q MD&A or note, stating that the interim filing attributes the rate cuts to residual values, car sales channel diversification and retail sales expansion, and does not name holding periods, which the FY2013 note later names for the same year ("optimization of fleet holding periods related to the integration of Dollar Thrifty" [P74 p.126]). Expected P1; a row at P2 or P3 is a partial pass. Needs: the Q2 2013 10-Q; not in the five-file pack.
- **Benign reading a good row carries:** rates are "reviewed on a quarterly basis" as a matter of routine [order ¶22], and ordinary-course estimate revisions are often not quantified [inf].
- **Where the order is vague:** it quotes only the MD&A. It finds that the Q2 and Q3 10-Qs also failed Regulation S-X [order ¶38.b], which concerns the financial statements and notes, but it does not quote any note [order ¶38.b]. Accept a locator in the MD&A or in a note if the sentence in the pack matches.

### K2. Q2 2013 10-Q: lower depreciation attributed to "improved residual values"

- **Order:** ¶23.
- **Quote from the order (quoting the filing):** "our monthly per vehicle depreciation costs decreased as compared to the prior year period due to improved residual values in the U.S., a continued move towards a greater proportion of non-program vehicles, mix optimization and improved procurement and remarketing efforts" [order ¶23].
- **The order's finding:** the disclosure "was inaccurate, because residual values had declined in the second quarter of 2013, a fact discussed within Hertz," and it did not address that "extensions of holding periods had reduced depreciation expense" [order ¶23].
- **Filing and period:** Q2 2013 10-Q MD&A. The sentence explains a $15 million decline in depreciation expense in the first half of 2013, "concentrated almost entirely in the second quarter" [order ¶23].
- **Checklist:** D3; C5.
- **Expected catch:** F4 consistency check 3 (explanations of a movement).
- **PASS:** a row quoting the sentence, with a locator in the Q2 2013 10-Q MD&A, recording the $15 million decline, and giving a check 3 result. Three outcomes are possible, and they score differently:
  1. **"Cannot test", P3,** naming the missing figure (residual values, or disposal proceeds per vehicle). PASS. The order says the contrary fact was "discussed within Hertz" [order ¶23]; it does not say any filing disclosed it.
  2. **"Inconsistent", P1, citing pack evidence that holding periods were extended:** the FY2013 10-K's "extended holding periods" phrase (K6; the 10-K's own words are "longer holding periods", see AK6) or the widened holding-period range (K5), as a cause the Q2 explanation omits. FULL PASS. This is the only route to a P1 that the order supports from inside the pack [inf], and it reads a March 2014 document back against an August 2013 one, which the row should say.
  3. **"Inconsistent", P1, asserting that residual values declined in Q2 2013 with no pack locator for that fact:** FAIL on this item, and a trap hit (T1 in section 4).
  4. **[AK3, 7 October 2026] "Inconsistent", P1, resting on a pack locator for a market-level residual decline:** PASS. The Q2 2013 call slides, furnished 1 August 2013, say "Residuals coming off historic peak Manheim down 4.4% YoY Q2:13 ... Auction/dealer residuals softer than expected" [P292 slide 11], and the same 10-Q reports disposal results ("net losses of $17.5 million and net gains of $38.3 million" [P234 p.13]). A row that sets the "improved residual values" sentence against either of these has a pack-grounded contradiction, not a trap hit. T1 is narrowed accordingly (section 4). The slides are not in the five-file pack.
- **Benign reading a good row carries:** the company's own list, non-program mix, "mix optimization" and procurement and remarketing [order ¶23]. The order does not find those reasons false; it finds the residual-value attribution inaccurate and the holding-period effect omitted [order ¶23].
- **Where the order is vague, superseded 7 October 2026 (AK2):** it does not say whether the $15 million is consolidated, the car rental segment, or U.S. only, and it does not give the Q2 amount on its own [order ¶23]. Dollar Thrifty's fleet joined in November 2012 [brief], so a consolidated year-over-year fall in fleet depreciation would be unexpected [inf]; the figure may be a narrower measure. The scorer should find the $15 million in the 10-Q before scoring any computed check that uses it.
- **Scope of the $15 million [AK2, 7 October 2026]:** resolved by the pack. The $15 million is the six-month effect of the 2013 rate changes, $15.5 million, of which $14.8 million fell in Q2 ("net decreases of $14.8 million and $15.5 million" [P246 p.38; P234 p.14]). Score the amount against those locators.

### K3. Q3 2013 10-Q: depreciation-rate disclosure again omits holding periods

- **Order:** ¶24.
- **Quote from the order:** the Q3 MD&A "contained similar disclosures relating to typical adjustments in depreciation rates that omitted the adjustment in planned holding periods" [order ¶24].
- **Filing and period:** Q3 2013 10-Q, MD&A. The order does not give the filing date; the Q3 financial statements were issued on 4 November 2013 [order ¶30].
- **Checklist:** C5; D3.
- **Expected catch:** F4 consistency check 2, as K1; F3 step 6.
- **PASS, superseded 7 October 2026 (AK1):** as K1, for the Q3 2013 10-Q. Expected P1; P2 or P3 partial.
- **PASS [AK1, 7 October 2026]:** as the corrected K1, for the Q3 2013 10-Q. The Q3 filing also gives the effect: the U.S. rate changes "resulted in net decreases of $18.0 million and $35.3 million" [P266 p.42; P254 p.14], with the same two-driver "Prospective changes" sentence. The criterion is that the row states the interim drivers and the absence of holding periods from them, against the FY2013 note [P74 p.126]. Expected P1; P2 or P3 partial. Needs: the Q3 2013 10-Q; not in the five-file pack.
- **Where the order is vague:** it paraphrases this sentence and does not quote it [order ¶24]. The scorer must find the Q3 sentence in the pack first; if the pack's Q3 wording differs materially from Q2's, score on what the pack says.

### K4. Q3 2013 10-Q: lower depreciation attributed to residual values that "remained strong"

- **Order:** ¶24.
- **Quote from the order (quoting the filing):** "monthly per vehicle depreciation costs decreased as compared to the prior year period due to residual values that remained strong in the U.S., a continued move towards a greater proportion of non-program vehicles, mix optimization and improved procurement and remarketing efforts" [order ¶24].
- **The order's finding:** the disclosure "once again did not adequately disclose the impact of longer planned holding periods" [order ¶24]. The order says nothing about Q3 residual values themselves [order ¶24].
- **Filing and period:** Q3 2013 10-Q MD&A, explaining an $18 million decline in depreciation expense in the third quarter of 2013 [order ¶24].
- **Checklist:** D3; C5.
- **Expected catch:** F4 consistency check 3.
- **PASS, superseded 7 October 2026 (AK4):** as K2 outcomes 1 and 2, for Q3. P3 "cannot test" passes; P1 citing K5 or K6 as the omitted cause is a full pass. A P1 claiming Q3 residual values fell is a trap hit, since the order does not say so even internally.
- **PASS [AK4, 7 October 2026]:** as K2 outcomes 1, 2 and 4, for Q3. P3 "cannot test" passes; P1 citing K5 or K6 as the omitted cause is a full pass. A P1 claiming Q3 residual values fell is a trap hit only when it carries no pack locator. The Q3 10-Q itself reports "a loss realized on vehicle sales in the third quarter of 2013, compared to gains realized on vehicle sales in the third quarter of 2012" [P266 p.50] and a U.S. disposal loss of $11.1 million against a gain of $15.2 million [P254 p.14]; a row setting the "remained strong" sentence against those is a tension between two statements in one filing, and passes. Needs: the Q3 2013 10-Q; not in the five-file pack.
- **Where the order is vague, superseded 7 October 2026 (AK2):** same as K2 on the scope of the $18 million.
- **Scope of the $18 million [AK2, 7 October 2026]:** resolved by the pack. It is the Q3 effect of the U.S. rate change, "$18.0 million" for the quarter and "$35.3 million" for the nine months [P266 p.42; P254 p.14].

### K5. FY2013 10-K: average holding period unchanged at 18 months while the disclosed range widened

- **Order:** ¶25.
- **Quotes from the order:** the FY2013 10-K "recited that 'our approximate average holding period for a rental car was eighteen months in the United States'" and this "was the same 18-month average holding period reported in the Form 10-K for 2012" [order ¶25]. The FY2013 10-K "disclosed that the 'holding periods' for its cars ranged from 4 to 36 months, a broader range than the 4 to 28 months disclosed in its Form 10-K for 2012" [order ¶25].
- **The order's finding:** the 18-month figure did not explain that it was calculated from cars already disposed of, and the range disclosure did not address "either the scale of the shift to longer planned holding periods or that the cause was the result of an affirmative business decision" [order ¶25].
- **Filing and period:** FY2013 10-K, filed March 2014, against the FY2012 10-K [order ¶25]. The order does not say which section of either 10-K holds the sentences [order ¶25]; the business section and the depreciation policy note are the likely places [inf]. Accept any locator that opens to the sentence.
- **Checklist:** D3; C5; D1.
- **Expected catch:** F4 consistency check 2, first arm ("the stated average or life is unchanged while the disclosed range widens"). This is the check's own example. Also F4's delta pass on the PP&E or policy note, and F3 step 6 under "Text found".
- **PASS, superseded 7 October 2026 (AK9):** a P1 row quoting the 2013 "eighteen months" sentence and the 2013 "4 to 36" range, each with a locator, set against the 2012 "18" and "4 to 28", with the result "inconsistent". **Required at P1.** A row at P2 or P3 is a partial pass.
- **PASS [AK9, 7 October 2026]:** a row quoting the 2013 "eighteen months" sentence (FY2013 p. 11; P59 p.11) and the 2013 "4 to 36" range (FY2013 p. 91; P68 p.91), each with a locator, set against the 2012 "eighteen months" (FY2012 p. 11; P30 p.11) and "4 to 28" (FY2012 p. 81; P39 p.81), both years quoted. The verdict word is not the test: the benign reading below cannot be ruled out from the pack, so "cannot be reconciled without knowing how the average is computed" is as honest a verdict as "inconsistent". The row **passes when it is carried to the report at level 1, whatever the verdict word**, and is partial when it stays in a table or stops short of the report. **Required at level 1.** Needs: the two 10-Ks; in the five-file pack.
- **Pack sentences the key omitted [AK7, 7 October 2026]:** the FY2013 10-K ties the lower depreciation to holding periods in its own words: "The favorable adjustments reflect changes from the impact of car sales channel diversification, acceleration of our retail sales expansion and the optimization of fleet holding periods related to the integration of Dollar Thrifty" (Note 8, FY2013 p. 126; P74 p.126), with the same phrase in the MD&A as a reason for lower U.S. monthly per-vehicle depreciation (FY2013 p. 42; P62 p.42). A row that sets this sentence against the unchanged 18-month average is on the K5 point. The FY2011 10-K gave the average as "fourteen months in the United States" [P2 p.13], so the series is 14, 18, 18 months for FY2011 to FY2013 against a range top of 28 then 36.
- **Benign reading a good row carries:** an average measured on vehicles already sold lags any change in plans for vehicles still in the fleet [inf]. The filing did not say how the average was computed [order ¶25], so the tool cannot confirm this reading from the pack and should say so.

### K6. FY2013 10-K MD&A: "longer holding periods" named as a cause of higher maintenance costs

- **Heading, superseded 7 October 2026 (AK6):** the item was headed "extended holding periods", the order's words. The 10-K's words are "longer holding periods" (below).
- **Order:** ¶25.
- **Quote from the order:** the MD&A "did not address the extension of planned holding periods, other than to list generally 'extended holding periods' as one of several factors causing an increase in maintenance costs" [order ¶25].
- **The pack's sentence [AK6, 7 October 2026]:** the FY2013 10-K MD&A reads "vehicle maintenance costs of $9.6 million due to the expansion of our off-airport and leisure businesses, longer holding periods and the impact of recalls" (FY2013 p. 53; P62 p.53). The order's phrase "extended holding periods" appears in the pack only in the Q4 2013 call slides: "Higher maintenance costs from extended holding periods" [P296 slide 11]. A search for the order's phrase misses the 10-K. Accept either locator; on the five-file pack only the p. 53 sentence is available.
- **Second route [AK7, 7 October 2026]:** the FY2013 10-K's "optimization of fleet holding periods related to the integration of Dollar Thrifty" (Note 8, FY2013 p. 126; MD&A p. 42; P74 p.126; P62 p.42) names holding periods as a cause of lower depreciation in the same filing. A row quoting that sentence with its locator and linking it to K5 or K9 meets K6 on the depreciation side; the maintenance sentence at p. 53 meets it on the maintenance side. The two together are the full link (K11).
- **Filing and period:** FY2013 10-K, MD&A [order ¶25].
- **Checklist:** D3; C5; D1.
- **Expected catch:** F4 consistency check 2 or 3 (the "holding period" search term finds it), or F4's delta pass on the MD&A.
- **PASS, superseded 7 October 2026 (AK6, AK7):** a row quoting the phrase with its locator and setting it against at least one of: the unchanged 18-month average (K5); the lower depreciation explained without reference to holding periods (K2, K4); the fall in depreciation per unit of fleet (K9). Expected P1 or P2; P3 is a partial pass. A row that quotes the phrase only as a maintenance-cost driver, with no link to depreciation or the holding-period sentences, is a partial pass.
- **PASS [AK6, AK7, 7 October 2026]:** a row quoting either pack sentence ("longer holding periods", FY2013 p. 53, or "optimization of fleet holding periods related to the integration of Dollar Thrifty", FY2013 pp. 42 and 126) with its locator, and setting it against at least one of: the unchanged 18-month average (K5); the lower depreciation explained without reference to holding periods (K2, K4); the fall in depreciation per unit of fleet (K9). Expected P1 or P2; P3 is a partial pass. A row that quotes the p. 53 phrase only as a maintenance-cost driver, with no link to depreciation or the holding-period sentences, is a partial pass. A row that paraphrases p. 126 as "longer holding periods" without quoting the operative words is noted under PR34 but not failed. Needs: the FY2013 10-K; in the five-file pack.
- **Where the order is vague:** it quotes two words and paraphrases the rest [order ¶25]. The scorer should find the full sentence in the pack (done above under AK6).

### K7. Guidance cut in September 2013 and reaffirmed with Q3 results on 4 November 2013

- **Order:** ¶27, ¶30 (and ¶4).
- **Quotes from the order:** "The new guidance reduced projected 2013 net income from a range of $1.78-1.88 per share to a new range of $1.68-1.78 per share" [order ¶27]. "Hertz reaffirmed its $1.68-1.78 guidance range when it issued its third quarter 2013 financial statements on November 4, 2013" [order ¶30].
- **Filings and periods:** guidance first issued in February 2013, document not named [order ¶27]; the revision on 26 September 2013 in a press release issued the same day Hertz filed an investor-conference slide deck [order ¶27]; the reaffirmation with the Q3 2013 results on 4 November 2013 [order ¶30].
- **Checklist:** E2.
- **Expected catch:** F5 method step 1, E2 (guidance against prior guidance and against results).
- **PASS:** an F5 context row listing, with locators, each range the pack contains in date order, and setting the FY2013 result against the reaffirmed range if the Q4 2013 release is in the pack. Expected P3, labelled as expectations and not accounts [F5 judgment notes]. **Required for the 4 November 2013 reaffirmation.** The 26 September press release is not an earnings release, so it may not be in the pack [inf]; if it is absent, the tool must say the revision document is missing and must not supply the ranges from memory.
- **The pack's figures [AK8, 7 October 2026]:** the February 2013 range in the pack is "Adjusted Diluted Earnings Per Share ... $1.82 - $1.92" (Q4 FY2012 release pp. 4 to 5), labelled adjusted diluted EPS. It is not the order's $1.78 to $1.88 [order ¶27]: the order's figure is either a later interim revision not in this pack or a different measure, and the key does not know which. The FY2013 outturn is adjusted diluted EPS of $1.63 (Q4 FY2013 release p. 5; the headless scorecards cite the same figure at p. 9, where the release's tables sit). "Ranges in date order" is scored against the pack's figures, not the order's. On the five-file pack the reaffirmation of 4 November 2013 and the 26 September 2013 revision are absent, so the required element is "not in pack"; the reachable fragment is the February range set against the outturn, which the v2 prompts have no step for. Needs: the Q3 2013 release (4 November 2013) and the 26 September 2013 release; neither is in the five-file pack.
- **Where the order is vague:** it calls the measure "net income ... per share" and does not say whether it is GAAP or adjusted [order ¶27]. Score on the release's own label (adjusted diluted EPS in the pack, per AK8).
- **Not visible:** that internal estimates had already fallen below the range when it was reaffirmed [order ¶4, ¶28 to ¶29]. See T12.

### K8 (bonus). Q1 2013 10-Q: the same residual-value explanation, first appearance

- **Order:** ¶23.
- **Quote from the order:** the Q2 disclosure "tracked the language from Hertz's disclosure in its Form 10-Q for the first quarter of 2013" [order ¶23].
- **Filing and period:** Q1 2013 10-Q MD&A [order ¶23].
- **Checklist:** D3; C5.
- **Expected catch:** F4 check 3, or the delta pass noting a sentence carried forward.
- **PASS:** a row quoting the Q1 sentence with its locator, P3 or "cannot test". The order does not find the Q1 disclosure inaccurate [order ¶23]; a row that calls it inconsistent with no pack evidence is over-reach, though not a trap hit.

## 3. Items the mechanism implies would leave a trace, but the order does not say were visible

**Every item in this section is inference. A pass here is a bonus, not required.** The order describes the mechanism; whether the pack's numbers moved enough to register is unverified until the scorer computes them.

### K9. Fleet depreciation per unit of fleet cost falling in 2013 while holding periods lengthened

- **Reasoning:** extending holding periods "spread out over more months the depreciation expense Hertz had to incur on its cars, lowering such expense overall for current quarters" [order ¶20]. The weighted average of planned holding periods across the U.S. fleet rose during 2013 from 21 to almost 25 months [order ¶25], across the second to fourth quarters [order ¶19]. So depreciation of revenue earning equipment divided by average gross revenue earning equipment should be lower in 2013 than in 2012, and lower in Q2 to Q4 2013 than in the same quarters of 2012 [inf]. The Q2 residual-value decline [order ¶23] pushes the other way and the non-program mix shift [order ¶23] could push either way [inf], so the size of the net movement is unknown.
- **Checklist:** C5; D3 (F4 check 2, second arm: "depreciation per unit of gross PP&E falls").
- **Expected catch:** F3 step 6 (depreciation ÷ average gross PP&E); F4 check 2.
- **Expected signal:** a lower ratio in 2013; a P3 row, or P1 or P2 when joined to K5 or K6 [inf].
- **Pack caveat for the scorer:** Hertz's fleet is "revenue earning equipment" [order ¶22], a line distinct from ordinary property [inf]. The pack template has one "PP&E, gross" line [PACK-SPEC]. If the pack left the fleet out of that line, F3's formula runs on non-fleet property and misses the signal. Check which base the tool used before scoring. The MD&A discusses "monthly per vehicle depreciation costs" [order ¶23], so the filings may give a per-vehicle figure the tool can use directly [inf].
- **PASS (bonus), superseded 7 October 2026 (AK11, AK12):** the ratio computed in code on a base that includes the fleet, 2011 to 2013 annual and same-quarter 2012 to 2013, with the direction stated; Dollar Thrifty recorded as a comparability break, and not offered as the explanation for a lower rate. An acquired fleet adds depreciation and gross cost together, so it moves the rate only through mix [inf].
- **PASS (bonus) [AK12, 7 October 2026; corrects AK11]:** per file set. On the five-file pack: the ratio computed in code on a base that includes the fleet, annual for 2011 to 2013 (Note 8's charge before the disposal adjustment over average gross revenue earning equipment) and the Q4 same-quarter rate for 2012 to 2013, which the pack allows: the FY2013 release's supplementary table gives "Depreciation of revenue earning equipment" for Q4 2013 and Q4 2012 (620.2 and 533.8, Q4 FY2013 release p. 9) and the workbook's quarterly balance sheet gives the fleet at each quarter end. The Q2 and Q3 same-quarter comparisons are required only when the 10-Qs are in the pack. AK11's "annual rates alone meet K9" is withdrawn. On the full pack: annual and same-quarter Q2 to Q4, as the superseded criterion says. Direction stated in both cases; Dollar Thrifty recorded as a comparability break and not offered on its own as the explanation for a lower rate. Quoting the company's own attribution ("optimization of fleet holding periods related to the integration of Dollar Thrifty", FY2013 p. 126) as the company's explanation is allowed [AK7] (see K13).

### K10. M-score DEPI for the 2012 to 2013 pair: not expected above 1 on this pack

- **Heading, superseded 7 October 2026 (AK5):** the item was headed "M-score DEPI above 1 for the 2012 to 2013 pair". The expected direction was wrong for a net-basis DEPI.
- **Reasoning, superseded 7 October 2026 (AK5):** DEPI rises when the depreciation rate falls [F3 step 2 formula], which K9's mechanism implies for 2013 [inf].
- **Reasoning [AK5, 7 October 2026]:** on this pack DEPI is below 1: 0.8985 as computed from the workbook, or 0.9359 with the fleet treated as PP&E. The index is depreciation over depreciation plus net PP&E, and an older fleet carries a lower net base, so a fleet that is held longer lowers the net-basis ratio in the later year and pushes DEPI below 1 even as the gross-basis rate (K9) falls. DEPI is not expected above 1; the item is whether the tool notes why.
- **Checklist:** B4; B7.
- **Expected catch:** F3 steps 2 and 4.
- **Expected signal:** DEPI above 1 and localized to C5; small contribution, since the coefficient is 0.115 [F3 step 2]. The pair straddles the Dollar Thrifty acquisition [brief], so F3 should label it non-comparable [F3 step 2].
- **PASS (bonus), superseded 7 October 2026 (AK5):** DEPI shown with its contribution, localized to useful lives, pair labelled non-comparable. Same base caveat as K9.
- **PASS (bonus) [AK5, 7 October 2026]:** DEPI shown with its contribution, pair labelled non-comparable, and the reason it sits below 1 noted (net base; fleet ageing). A DEPI above 1 is not expected and its absence is not a miss. Where a prompt version shows M-score totals only, the item is not scored. Same base caveat as K9.

### K11. Lower depreciation paired with higher maintenance cost in the same year

- **Reasoning:** the two sides of one decision. Longer holding periods lower depreciation now and carry the risk that "older cars were likely to require more costly maintenance" [order ¶20]; the FY2013 10-K itself names "extended holding periods" among the causes of higher maintenance [order ¶25]. A tool that finds both in 2013 has one thread seen from two steps [inf].
- **Checklist:** C5; D3.
- **Expected catch:** F5 step 2, threading K1 to K6 and K9 into one thread localized to "useful lives and depreciation".
- **Expected signal:** one thread at P1, drawing rows from F3 and F4.
- **PASS (bonus):** the thread exists, carries the depreciation and holding-period rows together, and its reading-plan question could be answered either way.

### K12. Subrogation receivables allowance (A3, A4)

- **What the order says about the method:** the allowance was "based on a rolling 12-month average, not of collections experience, but of write-offs, divided by monthly billed receivables" [order ¶11]. From August 2012, claims over $5,000 still uncollected after about 120 days went to attorneys and were no longer written off at that point, and the 100 percent allowance on claims over 360 days gave way, for attorney-held claims, to the overall rolling write-off rate of about 11 to 16 percent [order ¶12]. Attorney net collections for August to December 2012 were about 2 percent [order ¶13]. In May 2013 a spreadsheet error was found that had recorded no allowance at all on receivables over 360 days; the fix used an 11 percent rate instead of 100 percent, so expenses rose by less than $1 million instead of $7 million [order ¶15]. About $9.3 million of subrogation receivables over a year old were on the books at the start of October 2013 [order ¶16]. In the fall of 2013 some categories were reserved at about 4 percent [order ¶17]. Each 2013 change "had a favorable impact on the company's financial statements" [order ¶14]. The cumulative pre-tax misstatement across the subrogation accounts was $48 million [order ¶9].
- **Reasoning about the trace:** holding claims instead of writing them off lowers write-offs from August 2012 [inf, from ¶12]. Because the rate is a rolling average of write-offs [order ¶11], lower write-offs then lower the rate applied to all billed receivables for the next twelve months, so the effect compounds [inf]. Gross receivables in the class rise as aged claims are held [inf, from ¶13 and ¶16]. In the subrogation class, then, allowance ÷ gross receivables and write-offs ÷ provision should both fall through late 2012 and 2013 [inf].
- **Why the trace is likely faint:** the amounts the order gives are small ($9.3 million aged [order ¶16]; single corrections of about $1 million and $7 million [order ¶15, ¶18]; $48 million cumulative across several years [order ¶9]). Unless the receivables note or Schedule II breaks out subrogation, the consolidated allowance rate may not move visibly [inf]. The scorer should compute $9.3 million as a share of the pack's gross receivables and allowance before judging a miss. The order does not say whether the receivables note or Schedule II disclosed subrogation separately, or described the allowance method at all.
- **Dollar Thrifty overlap:** the acquisition adds receivables and allowance in Q4 2012 [brief], so a 2012 movement in the consolidated allowance has an event to explain it [inf].
- **Checklist:** A3 (allowance rate; write-off coverage); A4 (method changed).
- **Expected catch:** F2 step 1.
- **Expected signal:** A3: a falling allowance rate or write-off coverage in 2013, P3, if visible at all. A4: most likely "no change in the described method found", because the order does not say any change was disclosed [inf].
- **PASS (bonus):** allowance rate and write-off coverage computed in code from Schedule II or the receivables note for 2011 to 2013, with the benign reading first, Dollar Thrifty cited for 2012, and a P3 row if 2013 is the most adverse value in the series. "Subrogation not separately disclosed; cannot isolate" also passes. Any claim about attorney referrals, the 360-day rule or the 11 or 4 percent rates without a pack quotation is a trap hit (T7 to T10).

### K13. Dollar Thrifty acquisition (November 2012) as a context event that yields P4, not flags

- **Reasoning:** the order does not mention the acquisition. The brief dates it to November 2012 [brief]. A late-year acquisition moves balance sheet lines at close and income lines only for the days owned [F1 judgment notes], so 2012 and 2013 comparisons on receivables, revenue, fleet, goodwill and intangibles, debt and accruals break [inf].
- **Checklist:** E5 context; A2; B2; B4; B5; the F1 comparability map.
- **Expected catch:** F1 step 3 records it with the closing date and a locator; F2 and F3 cite it.
- **Expected signal:** P4 rows citing the event for: receivables growth ahead of revenue growth in Q4 2012 to Q3 2013 against the prior year (A2); the gap between balance-sheet and cash-flow accruals in 2012 (B2); the 2011 to 2012 and 2012 to 2013 M-score pairs, labelled non-comparable (B4); the F-score issuance term (B5); goodwill and intangibles growth (AQI) [inf for all].
- **PASS (bonus), superseded 7 October 2026 (AK7):** the event is on the context sheet with its date, and every row it explains sits at P4 citing it. **It must not be used as the benign reading for K1 to K6 or K9**, because it does not explain a lower depreciation rate, an unchanged 18-month average or a widened range [inf]. Using it that way is a precision failure on the affected K item.
- **PASS (bonus) [AK7, 7 October 2026]:** the event is on the context sheet with its date, and every row it explains sits at P4 citing it. **The acquisition by itself must not be offered as the benign reading for K1 to K6 or K9**, because it does not explain a lower depreciation rate, an unchanged 18-month average or a widened range [inf]; offering it that way is a precision failure on the affected K item. **Quoting the company's own attribution is allowed:** the FY2013 10-K says the favorable depreciation adjustments reflect "the optimization of fleet holding periods related to the integration of Dollar Thrifty" (FY2013 pp. 42 and 126; P62 p.42; P74 p.126), and a row that quotes that sentence with its locator as the company's explanation is citing the filing, not the acquisition. The reading should keep the filing's operative words (PR34).

### K14. Revisions made in early 2014

- **What the order says:** "Including revisions made in early 2014, the company reduced its previously reported GAAP pretax income by a total of $235 million" [order ¶5]. The order does not say where those revisions were made, or whether the FY2013 10-K filed in March 2014 carried any of them.
- **Reasoning:** if the FY2013 10-K revised prior-period comparatives, that is a "little r" revision visible only in its notes [inf].
- **Checklist:** C16.
- **Expected catch:** F1 step 5 (revisions; the RESTATED sheet comparison, if the pack has one); F4 C16 search.
- **PASS (bonus):** if the pack's FY2013 10-K contains revision language, a P3 F1-C16 row quoting it. If the pack contains none, "none found" is correct and there is nothing to score. Citing the $235 million is a trap hit (T14).

### K15. Incentive pay in the proxies

- **What the order says:** the subrogation methodologies operated in "a pressured corporate environment where, in certain instances, there was an inappropriate emphasis on meeting internal budgets, business plans, and earnings estimates" [order ¶2], and staff worked "under persistent pressure to meet budgets" [order ¶13]. The order says nothing about how executives were paid.
- **Reasoning:** if the proxies tie annual incentives to an earnings or EBITDA target, E3 records it as an incentive factor [inf].
- **Checklist:** E3.
- **Expected catch:** F5 step 1, E3.
- **PASS (bonus):** the metrics driving annual and long-term incentive pay, quoted from the proxies with locators, P3 or P4, descriptive only. Any mention of internal budget pressure is a trap hit (T12).

## 4. Items that were NOT visible in the filings: traps

A tool that "finds" any of these from the pack is using memory, later documents or invention. The only defence is a quotation from a pack file that says the same thing; if a tool offers one, the scorer checks it against the pack before scoring a trap hit. The order does not say any of these was disclosed at the time.

| # | Trap | What the order says | Locator |
|---|---|---|---|
| T1 | Residual values declined in Q2 2013 (superseded 7 October 2026, AK3: narrowed to Hertz's internal residual-value data) | Discussed within Hertz; not stated in any filing (superseded 7 October 2026, AK3). [AK3, 7 October 2026]: the internal data is not in any filing, but a market-level decline is pack-visible: the Q2 2013 call slides say "Residuals coming off historic peak Manheim down 4.4% YoY Q2:13 ... Auction/dealer residuals softer than expected" [P292 slide 11], and the Q2 10-Q reports disposal losses [P234 p.13]. A row resting on either locator is not a hit; a row asserting the decline with no pack locator is | [order ¶23] |
| T2 | Top models' planned holding periods went from 20 to 24 or 30 months | Internal fleet decision in Q2 to Q4 2013 | [order ¶19] |
| T3 | Weighted-average planned holding period rose from 21 to almost 25 months | The 10-K said 18 months | [order ¶25] |
| T4 | The 18-month average was computed from disposed cars | The filing did not explain this | [order ¶25] |
| T5 | The extension was an affirmative business decision; Hertz's planned periods were longer than other major rental companies' | Not disclosed; peer comparison needs data outside the pack (E5 must be "could not run") | [order ¶20, ¶25] |
| T6 | The amount by which longer holding periods reduced 2013 depreciation | First disclosed in the FY2014 10-K filed 16 July 2015 | [order ¶26] |
| T7 | Subrogation allowance computed as a rolling 12-month average of write-offs over billed receivables | The order does not say the method was disclosed | [order ¶11] |
| T8 | Attorney referrals from August 2012 ($5,000, about 120 days); write-offs stopped; attorney net collections of about 2 and 3 percent | Internal practice and data | [order ¶12, ¶13, ¶15] |
| T9 | The May 2013 spreadsheet error; $7 million correction reduced to under $1 million | Internal Audit finding | [order ¶15] |
| T10 | $9.3 million of year-old subrogation receivables; the 4 percent effective rate | Internal | [order ¶16, ¶17] |
| T11 | Post-close adjustments of about $1 million in May 2012, April 2013 ($1.2 million) and May 2013; the September 2013 controls deficiency | Internal; "No formal documentation of a rationale ... has been identified" | [order ¶18] |
| T12 | Internal EPS estimates of $1.72, $1.66 and $1.65; the "gap-closing" effort; the marketing-credit error in the September revision; budget pressure | Internal analysis | [order ¶4, ¶16, ¶27 to ¶29] |
| T13 | Audit committee told in mid-November 2013 there were no significant deficiencies; pervasive journal-entry and reconciliation problems found shortly after | Internal | [order ¶32] |
| T14 | $235 million restatement; 17 areas; 11 material weaknesses; "inconsistent and sometimes inappropriate tone at the top"; $48 million subrogation total; problems with the Oracle system implementation as a control weakness | All from the July 2015 restatement | [order ¶5, ¶9, ¶31] |
| T15 | Any event after 31 March 2014: the 13 May, 6 June and 14 November 2014 announcements; the lead director's and CEO's departures in August and September 2014; the late-2014 fleet-plan change; the $182 million rise in 2014 fleet expenses; the 2016 successor structure; the Estero, Florida headquarters as described in the order; the $16 million penalty | Post cut-off | [order ¶7, ¶26, ¶33 to ¶35; order §IV.C] |
| T16 | Naming any of the 17 restatement areas beyond subrogation and depreciation | The order does not describe the other areas, so a tool naming them is drawing on something outside both the pack and this key | [order ¶5] |

## 5. Things that should be benign

A section 5 item rated P1 or P2 with no other signal behind it is a false positive. Count them per run.

| Event | Source | Expected handling |
|---|---|---|
| Donlen acquisition, 2011 | [brief]; the order is silent | F1 event log with date and locator; P4 for 2010 to 2011 and 2011 to 2012 comparisons on receivables, fleet, goodwill and intangibles [inf] |
| Dollar Thrifty acquisition, November 2012 | [brief]; the order is silent | As K13. P4 for acquisition-driven movements; never the benign reading for the depreciation and holding-period items (superseded 7 October 2026, AK7: the acquisition by itself is never the benign reading; the company's own attribution at FY2013 pp. 42 and 126 may be quoted as the company's explanation) |
| The Hertz Corporation became a separate reporting company for FY2013, after Form S-4 registration statements went effective in February and October 2013 | [order ¶8, ¶36] | F1 records it as a reporting-structure event. Any section or format change in the 2013 filings traceable to it is mechanical in F4's delta pass [inf] |
| Form S-8 filed 16 August 2013 for employee plans | [order ¶36] | Ordinary; no row expected |
| Routine quarterly review of depreciation rates, and routine estimation of holding periods | [order ¶3, ¶22] | The review's existence is not a signal. K1 and K3 arise from the missing effect disclosure, not from the review |
| Non-program vehicle mix, "mix optimization", procurement and remarketing | [order ¶23, ¶24] | The company's own reasons; they belong in the benign-reading column of K2 and K4, written first. The order does not find them false [order ¶23, ¶24] |
| Subrogation as a business process: recoveries from renters and third parties recorded as income and a receivable, with an allowance | [order ¶10] | The existence of damage-recovery receivables is ordinary; no row for that alone |
| The September 2013 guidance cut, attributed to "a series of business and financial setbacks" | [order ¶27] | A downward revision is ordinary disclosure. P3 at most under E2 (K7) |
| Controls conclusions in the FY2013 10-K | The order does not say what the 10-K stated. The ineffective-controls conclusion at 31 December 2013 was announced on 6 June 2014 [order ¶34] | [inf] The 10-K as filed probably did not report a material weakness. F1 records whatever the pack says. No E4 row above P3 is expected unless the pack contains a weakness |

## 6. Scoring table

Priority is the expected reading priority under the prompts' definitions. "Partial" means the row exists with a correct quotation and locator but at a lower priority than expected.

The table below is the pre-run version, kept on record. Rows K1, K2, K3, K4, K5, K6, K7, K9, K10 and K13 are superseded 7 October 2026 by the corrected rows in section 6a, which apply AK1 to AK12; the other rows stand.

| ID | Item | Req. or bonus | Expected step | Expected priority | Pass criterion |
|---|---|---|---|---|---|
| K1 | Q2 2013 10-Q: depreciation rates "adjusted" for residual values, no effect stated | Required | F4 check 2; F3 step 6 | P1 | Row quoting the sentence, locator in Q2 2013 10-Q MD&A (or a matching note), noting no dollar effect. P2 or P3 partial |
| K2 | Q2 2013 10-Q: $15M lower depreciation attributed to "improved residual values" | Required | F4 check 3 | P3 (cannot test) or P1 (via K5 or K6) | Row quoting the sentence with locator and the $15M decline; result either "cannot test" naming the missing figure, or "inconsistent" citing the 10-K holding-period evidence. P1 resting on residual values declining, with no pack locator, fails and scores T1 |
| K3 | Q3 2013 10-Q: rate-adjustment disclosure again omits holding periods | Required | F4 check 2; F3 step 6 | P1 | As K1, for Q3 2013. Scorer finds the sentence in the pack first, since the order paraphrases it |
| K4 | Q3 2013 10-Q: $18M lower depreciation attributed to residual values that "remained strong" | Required | F4 check 3 | P3 or P1 (via K5 or K6) | As K2, for Q3 2013 |
| K5 | FY2013 10-K: average holding period "eighteen months", unchanged from 2012, while range widened from 4 to 28 to 4 to 36 months | Required | F4 check 2 (first arm); F4 delta pass; F3 step 6 | P1 | P1 row quoting the 2013 sentence and range with locators against the 2012 counterparts, result "inconsistent". P2 or P3 partial |
| K6 | FY2013 10-K MD&A: "extended holding periods" as a cause of higher maintenance | Required | F4 check 2 or 3; F4 delta pass | P1 or P2 | Row quoting the phrase with locator, linked to K5, K2/K4 or K9. Unlinked row is partial |
| K7 | Guidance: February 2013 range, cut 26 September 2013, reaffirmed 4 November 2013 | Required (4 Nov reaffirmation) | F5 step 1, E2 | P3 | Ranges in date order with locators; result against reaffirmed range if Q4 release in pack; labelled expectations. Missing documents stated, not filled from memory |
| K8 | Q1 2013 10-Q: same residual-value explanation, carried into Q2 | Bonus | F4 check 3 or delta pass | P3 | Row quoting the Q1 sentence with locator |
| K9 | Fleet depreciation ÷ average gross fleet cost lower in 2013 | Bonus | F3 step 6; F4 check 2 | P3, or P1/P2 joined to K5/K6 | Ratio in code on a base including revenue earning equipment, annual and same-quarter, direction stated; Dollar Thrifty not used as the explanation |
| K10 | M-score DEPI above 1 for 2012 to 2013 | Bonus | F3 steps 2 and 4 | Localization, no separate row needed | DEPI and contribution shown, localized to C5, pair labelled non-comparable |
| K11 | Lower depreciation paired with higher maintenance in 2013 | Bonus | F5 step 2 | P1 thread | One thread holding the depreciation and holding-period rows from F3 and F4, localized to useful lives and depreciation |
| K12 | Subrogation allowance: allowance rate and write-off coverage 2011 to 2013; method text | Bonus | F2 step 1 (A3, A4) | P3 if visible; else none | Ratios in code from Schedule II or the receivables note, benign reading first, Dollar Thrifty cited for 2012; or "cannot isolate subrogation". No mechanism claims without a pack quote |
| K13 | Dollar Thrifty as context | Bonus | F1 step 3; F2; F3 | P4 | Event with date and locator; the rows it explains at P4 citing it; not used for K1 to K6 or K9 |
| K14 | Early-2014 revisions in the FY2013 10-K, if any | Bonus | F1 step 5; F4 C16 | P3 | Revision language quoted if present in the pack; "none found" if absent; $235M never cited |
| K15 | Incentive-pay metrics in the proxies | Bonus | F5 step 1, E3 | P3 or P4 | Metrics quoted with locators, descriptive only |
| G1 | No row asserts fraud or misstatement | Global | All steps | n/a | No ledger row or summary states or implies that Hertz's accounts were misstated or fraudulent; banned words absent except inside a filing quotation |
| G2 | No row relies on information from after 31 March 2014 | Global | All steps | n/a | Every fact traces to a pack file dated on or before 31 March 2014; zero hits on T15 and T14 |

**Trap count.** Report the number of section 4 traps hit per run, with the row ID. Any trap hit fails G2 when the source is post cut-off (T6, T14, T15), and is a hallucination finding otherwise.

### 6a. Corrected rows [AK1 to AK12, 7 October 2026]

"Needs" names the document the item rests on; "five-file" is the pack in `test-data/hertz-fy2013/` (two 10-Ks, two fourth-quarter releases, workbook). Expected priority is given in the v2 prompts' terms: level 1, 2, 3, or explained (P4).

| ID | Item | Req. or bonus | Needs | Expected level | Pass criterion (corrected) |
|---|---|---|---|---|---|
| K1 | Q2 2013 10-Q: depreciation rates "adjusted" for residual values; interim drivers omit holding periods | Required | Q2 2013 10-Q (not five-file) | 1 | Row quoting the sentence with a locator in the Q2 2013 10-Q, stating that the interim filing attributes the rate cuts to residual values, channel diversification and retail expansion and does not name holding periods, which the FY2013 note names for the same year [P74 p.126]. The filing does give the effect ($14.8M and $15.5M [P246 p.38; P234 p.14]); "no dollar effect" is false (AK1). Level 2 or 3 partial |
| K2 | Q2 2013 10-Q: lower depreciation attributed to "improved residual values" | Required | Q2 2013 10-Q (not five-file) | 3 (cannot test) or 1 | Row quoting the sentence with locator and the $14.8M Q2 and $15.5M six-month amounts (AK2); result "cannot test" naming the missing figure, "inconsistent" citing the 10-K holding-period evidence (K5, K6), or "inconsistent" citing the Q2 call slides [P292 slide 11] or the 10-Q's disposal losses [P234 p.13] (AK3). Level 1 resting on a residual decline with no pack locator fails and scores T1 |
| K3 | Q3 2013 10-Q: rate-adjustment disclosure again omits holding periods | Required | Q3 2013 10-Q (not five-file) | 1 | As the corrected K1, for Q3 2013; the Q3 effect is $18.0M and $35.3M [P266 p.42; P254 p.14] (AK1). Scorer finds the sentence in the pack first |
| K4 | Q3 2013 10-Q: lower depreciation attributed to residual values that "remained strong" | Required | Q3 2013 10-Q (not five-file) | 3 or 1 | As the corrected K2, for Q3 2013, with the $18.0M Q3 U.S. rate change (AK2). A level-1 row that residual values fell is a trap hit only without a pack locator; the Q3 10-Q's own "loss realized on vehicle sales in the third quarter of 2013" [P266 p.50] and the $11.1M U.S. disposal loss [P254 p.14] are locators (AK4) |
| K5 | FY2013 10-K: average holding period "eighteen months", unchanged from 2012, while range widened from 4 to 28 to 4 to 36 months | Required | FY2012 and FY2013 10-Ks (five-file) | 1 | Row quoting the 2013 sentence (p. 11) and range (p. 91) with locators against the 2012 counterparts (pp. 11, 81), both years quoted, set against each other; passes when carried to the report at level 1 whatever the verdict word, partial when it stays in a table (AK9). The 10-K's "optimization of fleet holding periods related to the integration of Dollar Thrifty" (pp. 42, 126) and the FY2011 "fourteen months" [P2 p.13] are on the point (AK7) |
| K6 | FY2013 10-K MD&A: "longer holding periods" as a cause of higher maintenance; or "optimization of fleet holding periods" as a cause of lower depreciation | Required | FY2013 10-K (five-file) | 1 or 2 | Row quoting the p. 53 maintenance sentence ("longer holding periods", not the order's "extended"; AK6) or the pp. 42 and 126 depreciation sentence (AK7) with locator, linked to K5, K2/K4 or K9. Unlinked row partial. "Extended holding periods" is only in the Q4 call slides [P296 slide 11], accepted as a locator on the full pack |
| K7 | Guidance: February 2013 range, cut 26 September 2013, reaffirmed 4 November 2013 | Required (4 Nov reaffirmation) | Q3 2013 release and 26 September 2013 release (not five-file) | 3 | Ranges in date order with locators, scored against the pack's figures: adjusted diluted EPS $1.82 to $1.92 (Q4 FY2012 release pp. 4 to 5) and the $1.63 outturn (Q4 FY2013 release), not the order's $1.78 to $1.88 (AK8); labelled expectations. Missing documents stated, not filled from memory |
| K9 | Fleet depreciation ÷ average gross fleet cost lower in 2013 | Bonus | Annual: the 10-Ks and workbook; Q4: the FY2013 release's supplementary table (five-file). Q2, Q3: the 10-Qs | 3, or 1/2 joined to K5/K6 | Ratio in code on a base including revenue earning equipment, annual 2011 to 2013 and the Q4 same-quarter rate (620.2 and 533.8, Q4 FY2013 release p. 9, over the workbook's quarter-end fleet); Q2 and Q3 only when the 10-Qs are in the pack (AK12, withdrawing AK11). Direction stated; Dollar Thrifty not offered on its own as the explanation; the company's p. 126 attribution may be quoted (AK7) |
| K10 | M-score DEPI for 2012 to 2013: below 1 on this pack (0.8985; 0.9359 fleet-in) | Bonus | Workbook (five-file) | Localization, no separate row needed | DEPI and contribution shown, pair labelled non-comparable, reason for a value below 1 noted (net base; fleet ageing). Not expected above 1 (AK5). Not scored where a prompt version shows totals only |
| K13 | Dollar Thrifty as context | Bonus | FY2012 and FY2013 10-Ks (five-file) | Explained (P4) | Event with date and locator; the rows it explains at P4 citing it. The acquisition by itself is never the benign reading for K1 to K6 or K9; the company's own attribution (FY2013 pp. 42, 126) may be quoted as the company's explanation (AK7) |

**Suggested pass bar, for the analyst to adjust before scoring, superseded 7 October 2026 (AK10)** [conv]: K5 at P1; at least five of K1 to K7 at their expected priority or partial; zero trap hits; G1 and G2 hold.

**Pass bar, per file set [AK10, AK12, 7 October 2026]** [conv]:

| File set | Required | Traps | Global | Bonus note |
|---|---|---|---|---|
| Five-file pack (`test-data/hertz-fy2013/`: FY2012 and FY2013 10-Ks, two Q4 releases, workbook) | K5 at level 1, by the AK9 route; K6 at least partial. K1 to K4 and K7 are "not in pack", not misses: K1 to K4 need the 2013 10-Qs, K7 the Q3 2013 release and the 26 September 2013 release | Zero trap hits | G1 and G2 hold | K9 requires the annual rates and the Q4 same-quarter rate (AK12); K10 not expected above 1 (AK5) |
| Full pack (`pack/`: 10-Ks, 10-Qs, releases, call slides, proxies) | K5 at level 1, by the AK9 route; at least five of K1 to K7 at their expected level or partial | Zero trap hits | G1 and G2 hold | K9 requires annual and same-quarter Q2 to Q4 |
