# Test log: T1 Hertz, prompts v0.2, Claude Code dry run

Findings recorded as they arrive. Each is classed as a **pack defect** (fix in the pack builder), a **prompt defect** (candidate change for v0.3), or a **platform note**. The prompts and the pack were frozen for the run; nothing below was fixed mid-run.

## F1: context and comparability

**Run:** completed all eight steps. The response ran to about 16,000 words, roughly half of it code and script output. Seven ledger rows, all P3.

**What it found that matters** (not scored yet; see score.md):
- The FY2013 10-K revises FY2011, FY2012, each 2012 quarter and Q1 to Q3 2013 for errors identified in Q4 2013, totalling $46.3 million. The Q4 2013 earnings release gives $47.9 million. There was no non-reliance filing.
- An earlier revision, found in Q3 2011, changed FY2008 to FY2010, and the 10-Q and the 10-K describe its effect on 2009 differently.
- A breach of a fleet-financing requirement at year end, waived in January 2014.
- A later 10-K filing date than in prior years.
- Context events: Dollar Thrifty, Donlen, the Advantage divestiture and its buyer's bankruptcy, a segment recast, revenue-line reclassification, and fleet depreciation-rate changes.

### Pack defects

| # | Defect | Effect | Fix |
|---|---|---|---|
| PK1 | Derived Q4 FY2013 = revised full year minus unrevised nine months, so it mixes bases | The Q4 FY2013 figures in every derived line absorb the whole 2013 revision | In the builder, when a 10-K revises the interim quarters, derive Q4 from the revised nine months the 10-K discloses, or leave Q4 blank and say why. Flag in the manifest either way |
| PK2 | EXTRA: common stock and treasury stock left in thousands | Wrong scale on two EXTRA lines | Apply the unit scale to every EXTRA line, including captions the parser treats as shares |
| PK3 | EXTRA: sign flip on revolver proceeds | Wrong sign on one EXTRA line | Check the sign convention for lines whose label changes between "proceeds" and "payments" |
| PK4 | CF_Q: Q1 FY2013 share repurchase missing | One blank cell | Map the treasury-share purchase element used in that filing |
| PK5 | RESTATED compares each year only with the next year's 10-K | Misses FY2011 as revised in the FY2013 10-K, and FY2009 as revised in 2011 | Compare each year with every later annual report in the pack |
| PK6 | The builder's own tie-out does not check cash-flow net change against the balance-sheet change in cash | The FY2013 $12.2 million gap (revised opening cash) passed the builder and was caught only by F1 | Add the test to the builder |

### Prompt defects (v0.3 candidates)

| # | Prompt | Defect | Proposed change |
|---|---|---|---|
| PR1 | F1 | Asks for ledger rows "F1-C15, F1-C16 and F1-E4" without saying what those rows are; the checklist is not in the pack. The runner guessed C15 = restatements, C16 = auditor, the reverse of the checklist | Name each row in the prompt: C15 auditor change; C16 restatements and revisions; E4 management turnover and internal control |
| PR2 | All | Verification line: "Context sheet: used / not attached" does not fit F1, which produces the sheet | Give F1 its own verification line |
| PR3 | All | "Items run" undefined in the verification line | Define as checklist rows run |
| PR4 | F1 | Self-check requires every file in the inventory; with 300 files the table is unreadable | Allow the inventory grouped by filing, with the full ID list in an appendix |
| PR5 | F1 | The comparability map across 17 periods is too wide for one table | Specify annual and quarterly maps separately |
| PR6 | All | "Show all code" produced about 8,000 words of code and output in F1 | Show the code, not the printed output of every exploratory script; cap output echo |
| PR7 | F1 | Step 5 assumes the RESTATED sheet covers every reprint | Instruct: also compare any comparative figures quoted in the text with the original filings |

## F2: working capital

**Run:** every method step completed; 15 of 19 checklist rows run (A5, A6, A12, A15 could not run). 13 ledger rows: P1 0, P2 1, P3 6, P4 6. The P2 is accrued liabilities as a share of revenue, 10.26 percent in FY2013, the lowest in FY2009 to FY2013 and down four years running. About 20,400 words including 8,400 of code.

**Runner judgments worth keeping:** separated vehicle-sale receivables due from manufacturers (up to 48 percent of receivables, from the cash-flow supplemental disclosure) and recomputed DSO without them; added an "FY2012 as revised" column so FY2013 compares on one basis; used the restructuring rollforward from the note text when NOTES had no release column, which turned up a 10.0 difference between the FY2012 and FY2013 10-Ks' accounts of the same 2012 movements.

### Prompt defects (v0.3 candidates)

| # | Prompt | Defect | Proposed change |
|---|---|---|---|
| PR8 | F2, F3 | No rule for a US GAAP company with no cost-of-sales line; the only substitute given is the IFRS nature-of-expense one | Add: where no cost-of-sales line exists under either framework, name the closest cost line (direct operating costs, cost of services) as a substitute, label every affected ratio "substitute cost base", and cap those rows at P3 |
| PR9 | F2 | Receivables may include non-customer amounts (manufacturer receivables, tax refunds, insurance) that swamp DSO | Add a step: split trade receivables from other receivables where the notes or cash-flow supplement allow, and run DSO on the customer portion |
| PR10 | F2, F3, F4 | Checklist row numbers are named in the header but not attached to each measure inside the steps | Put the row number beside each measure |
| PR11 | Shared ledger block | Trigger (b) "three or more consecutive year-over-year comparisons" does not say the run must end in the latest period; "adverse direction" is undefined for some measures | Define both, and list the adverse direction for each measure |
| PR12 | Shared ledger block | "Items found by reading text always become rows" forced a P3 for search hits that turned out to be fleet debt, not receivable sales | Text hits become rows only when they bear on the checklist row after reading; irrelevant hits go in "Looked for and not found" with the reason |
| PR13 | F2 | Reserve releases point only to NOTES; most US GAAP reserve rollforwards are in the note text | Read rollforwards from the NOTES sheet where present, otherwise from the note text files |

## F4: disclosure deltas and consistency

**Run:** steps 1 to 7 completed. 188 section pairs measured, 20 unpaired. All ten consistency checks have a result: 3 inconsistent (useful lives, explanation of the fleet-depreciation movement, the non-recurring label), 2 consistent, 5 cannot test. 33 ledger rows: P1 7, P2 2, P3 19, P4 5. All 95 quotations verified in code against file and page. About 30,400 words; the narrative, consistency table and ledger are about 12,000.

**Partial:** step 3's classification of every changed sentence (about 35,000) was done by code for 8,467 roll-forwards and near-identical sentences; the priority sections were read in full; MD&A, Item 1, Item 8, releases and proxy by counts, the ten check searches and targeted reads.

### Prompt defects (v0.3 candidates)

| # | Prompt | Defect | Proposed change |
|---|---|---|---|
| PR14 | F4 | Step 3 asks for every changed sentence to be classified; a three-year pack has about 35,000. Not feasible on any platform | Scope step 3 to the first ten sections of the reading order; for the rest, report counts and read only sentences that hit the consistency-check search terms or the checklist rows' terms |
| PR15 | F4 | Section map of 210 rows dominates the output | Report the map only for sections with substantive changes; give totals for the rest |
| PR16 | F1, F4 | Checklist row IDs are inconsistent across prompts because the checklist is not attached (F1's runner used C15 for restatements; F4 used C16) | Attach a one-page row index to every prompt, or name each row in the prompt text (see PR1, PR10) |
| PR17 | F4 | C15 in scope but no method step for it | Either add an auditor-change step or drop C15 from F4's scope (F1 covers it) |
| PR18 | F4 | P2 rule "another step's evidence ... you can see it in the pack" is undefined when the step runs alone | Define: another step's ledger row attached to this run, or two independent signals within this step |
| PR19 | F4 | Check 2's condition "stated average or life unchanged" fits loosely where there is no stated average | Split check 2 into (a) stated life or average against disclosed ranges, and (b) depreciation rate against stated lives |
| PR20 | F4 | Check 7: the non-recurring label may appear only in releases, which Item 10(e)(1)(ii)(B) does not reach | State that the prohibition applies to filed documents; in furnished releases the test is Regulation G and C&DI 102.03, and say which applies to each hit |
| PR21 | Shared rules | Rule 12 (no em-dashes) conflicts with rule 6 (quote exactly) | Rule 12 applies to the assistant's own words; quotations keep the filing's punctuation |

## F3: earnings quality and accruals

**Run:** steps 1 to 8 completed; 11 items could not run (no capitalized software, contract costs or interest-capitalized disclosure; anything needing FY2008 or earlier). M-score below −1.78 in every pair on every mapping. F-score 1.77, 1.85 and 1.77 for FY2011 to FY2013 with the fleet outside PP&E; 0.57 to 0.62 with the fleet counted as PP&E. 18 ledger rows: P1 1, P2 3, P3 8, P4 6. About 25,800 words, 10,700 of them code.

**The P1:** the FY2013 depreciation note lowers US depreciation rates by $44.2 million as "indicative of the residual values experienced" while the same note reports $48.2 million of US vehicle disposal losses from "declining residual values". **The P2s:** the falling fleet depreciation rate; the car holding-period range widening from 4 to 26 months to 4 to 36; restructuring charges adjusted out in 16 of 16 quarters under a "non-recurring" or "one-time" label.

### Prompt defects (v0.3 candidates)

| # | Prompt | Defect | Proposed change |
|---|---|---|---|
| PR22 | F3 | No fallback for an unclassified balance sheet (no current totals, one debt line); Sloan accruals, RSST WC, AQI and LVGI cannot run as written | Add: if current totals are absent, compute the measures on a stated set of individual operating lines, label them "approximated", cap resulting rows at P3; report the cash-flow accrual form as primary |
| PR23 | F3 | No guidance for lessors: whether the rental fleet counts as PP&E decides whether the F-score clears 1.0 on Hertz | Require both mappings for any company with equipment held for rental or lease, with the fleet-in-PP&E version primary for AQI, DEPI and soft assets (the fleet is the operating PP&E of such a business), and state the swing |
| PR24 | F3 | Mixed bases after a revision are not addressed | When the context sheet records a revision, compare the latest year with the prior year as revised, and say which basis each figure is on |
| PR25 | F3 | Rule texts (Item 10(e), Item 2.02, ASC 835-20) and the 0.00345 figure are cited in the prompt but the runner cannot verify them from the pack, so it marked them unverified | Cite rules in the prompt as the prompt's instruction, not as a claim the output must source; tell the assistant not to mark prompt-supplied rules unverified |
| PR26 | F3 | "Adverse direction" for indices with negative coefficients (SGAI, LVGI) undefined | Define: the direction that raises M |
| PR27 | All | Ledger delivered twice (markdown and CSV) doubles the longest part of the output | Deliver the CSV only, or the markdown table only with a one-line conversion instruction; test which survives the platforms better |

## Score, F1 to F4 (full detail in score.md)

**Verdict against the suggested pass bar: fail on one condition.** K5 was caught only in part at P1: the holding-period range widening (4 to 26, 4 to 28, 4 to 36 months) was caught by F4-D3-01 (P1) and F3-C8-02 (P2), but the unchanged "eighteen months" average in Item 1 of the FY2012 and FY2013 10-Ks was not. Both steps' searches hit that sentence and neither read it. K6 missed for the same reason. Every other condition on the bar holds.

**Clean:** 30 of 30 recomputed numbers match; 27 of 27 locators open to the cited text; 21 of 21 quotations verbatim; all 71 ledger rows benign-first; all 17 P4 rows cite a context event; no trap hits; G1 and G2 hold.

**Legitimate catches the key did not expect:** F3's P1 (the FY2013 depreciation note's "indicative of the residual values experienced" against its own "declining residual values" losses, P74 p. 126) and F4's check-3 result (the Q2 2013 call slides in the pack say residuals were "softer than expected", P292 slide 11). The answer key's statement that the residual decline appeared in no filing is too broad for this pack.

**Answer-key errors found by the scorer (AK1 to AK7):** among them, the 10-Qs do give dollar effects ($14.8m, $15.5m, $18.0m); the 10-K says "longer" not "extended" holding periods; DEPI is below 1 on this pack, so K10's expectation cannot be met; the key omitted the 10-K sentence tying lower depreciation to "optimization of fleet holding periods related to the integration of Dollar Thrifty". The key is corrected in a dated addendum, not rewritten, so the pre-run version stays on record.

**Noise:** about 11 ledger rows unsupported by their evidence and 5 wrongly prioritized; the clearest is F4-D3-02 at P1 (two intangible-life statements with different scopes). **New defects** PR28 to PR35 and PK7 to PK8 are in score.md; PR28 (tabulate every life and holding-period statement year over year, in every section including Item 1) is the fix for the K5 and K6 misses.

## F5: the ledger (scored here, not in score.md)

**Run:** every method step completed except E1 (no consensus file) and E5 (no peer data), which the prompt says to skip. 71 input rows merged, none malformed, 8 context rows added; 79 rows in 25 threads: P1 3, P2 7, P3 12, P4 3. About 46,300 words, of which the merged ledger (twice) is 25,600 and code 12,400; the reading plan, thread table and context rows are about 7,500.

**Score on the F5 items:**

| Item | Result | Basis |
|---|---|---|
| K7 guidance (required) | Pass | Every range in date order with locators (Table E2-a); the 26 September 2013 range taken from the Q3 release that confirms it, and the missing document stated, not filled; labelled "expectations, not the accounts"; result against the lowered range computed: FY2013 below the low end on all five metrics |
| K11 depreciation with maintenance (bonus) | Pass | Thread T1 joins 14 rows from F2, F3, F4 and F5 on FY2013 fleet depreciation, holding periods and residual statements, localized to useful lives and depreciation, P1 |
| K15 incentive pay (bonus) | Pass, beyond the criterion | Metrics quoted with locators; payouts recomputed on the revised figures with the proxies' own rules (2011 API payout 189.1 percent as reported, 182.0 percent on revised API) |

**The reading plan is the most useful thing in the whole run.** Item 1 sends the analyst to Note 8 p. 126, MD&A pp. 42 to 43 and 54 and the Q4 slides, with a question either reading could answer. An analyst with an hour could start there.

### Prompt defects (v0.3 candidates)

| # | Prompt | Defect | Proposed change |
|---|---|---|---|
| PR36 | F5 | No citation form for the attached ledgers and context sheet (not pack files) | Add marks `[L:F3-C8-01]` for a ledger row and `[CS:event]` for a context-sheet event |
| PR37 | F1, F5 | Context-sheet event IDs (E1 to E26) collide with checklist rows E1 to E6 | Number context events `EV1`, `EV2` ... |
| PR38 | F5 | No tie-break within a priority beyond recency | Adopt the runner's: number of contributing steps, then P1 members, then member count |
| PR39 | F5 | E6 "headline figures" undefined | List them: revenue, pre-tax income, net income, diluted EPS, total assets, cash, operating cash flow, each adjusted measure headlined |
| PR40 | F5 | Output: the merged ledger twice is 25,600 words | Return the reading plan and thread table in the reply; the merged ledger as CSV only |

## Overall result of the T1 dry run

- **Accuracy is not the problem.** Every sampled number, locator and quotation checked out; no trap hits; no banned language; no hindsight.
- **Recall failed in one place, for a fixable reason.** The one required miss (the unchanged "eighteen months" average, K5 in part and K6) was found by both steps' searches and not read. PR28 fixes it.
- **The tools found things the answer key did not expect**, from filed text: the same-page contradiction in the FY2013 depreciation note, the "softer than expected" residuals on the Q2 slides, the FY2013 revision and its effect on incentive pay.
- **Noise is moderate:** about 11 of 71 rows unsupported and 5 misprioritized.
- **Length is the blocking defect for the platforms.** F1 to F5 ran 16,000 to 46,000 words each against a chat reply's limit. v0.3 has to cut this by roughly an order of magnitude before the platform test means anything.

## Platform notes

- A chat reply of 16,000 words will be cut off on both platforms. PR6 matters beyond tidiness: the output has to fit a chat response. Test on the platforms.
- The harness loaded the project CLAUDE.md into the runner's context. The runner says it used none of it. On a chat platform this cannot happen; for later dry runs, run from a folder without a CLAUDE.md.
