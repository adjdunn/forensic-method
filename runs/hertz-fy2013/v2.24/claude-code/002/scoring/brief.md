# Scorer brief

You are scoring one run of the forensic prompts against the company's answer key. You are independent of the run: you did not write the prompts or the replies, and you take nothing on trust from them. The product is one scorecard, written to `scoring/scorecard.md` in the run folder, in the format at the end of this brief.

## Inputs (the paths are filled in at the end of this brief)

1. `run.json`: what was run, with which files, by which adapter and model, and the citation checker's summary for each reply.
2. The replies: `numbers-1`, `numbers-2`, `text-3`, `text-4`, `report-5` (markdown, text or PDF).
3. The checker reports, `check-*.md`: quotations exact and on the cited page, figures printed or derived, shares recomputed, banned words, post-cutoff mentions. Use them; do not redo what they did. Where the checker marks a quotation "page differs" or "not found", open the pack and settle it yourself.
4. The pack the run saw: the files listed in `run.json` under `files`, in `workspace/` (or the pack folder if the workspace is gone). Page markers `[p. N]` are the printed page numbers.
5. The answer key, `answer-key.md`, with its addendum of corrections. Score against the key with the corrections applied. The key was written from the enforcement order before any run; where it is wrong on the pack, say so under answer-key defects rather than bending the score.
6. `tools/TESTS.md`, the "measures" section, for what a pass means at this version.

## Rules

- **Scope first.** List which K items the run could have caught given the files it saw. An item whose evidence sits only in a document the run did not have (a 10-Q, a call deck, an interim release) is "not in pack", not a miss. Say which document it needed.
- **Pass, partial, miss, at the level the key expects.** The key states an expected priority (P1 to P4). The v2 prompts rank by evidence level instead: level 1 (a sentence contradicted by the company's own numbers or another sentence), level 2 (two or more signals on one account), level 3 (a single signal); "checked and explained" is P4. Map P1 to level 1, P2 to level 2, P3 to level 3. A catch at a lower level than expected is a partial; say the level it got.
- **A catch means the sentence is quoted or its operative words are used, with a locator that opens to it, and the point the key makes is made.** A row that quotes the right sentence for a different point is a partial; say what point it made instead.
- **Traps.** For each trap in the key, say whether the run fell into it, with the sentence that would be the hit. A claim with a pack locator is not a trap hit even if it reads like one; a claim with no locator is.
- **G1, G2.** Banned words (fraud, manipulation, red flag) in the run's own sentences; anything from after the cutoff used as a fact. The checker counts; you judge the context.
- **Recompute ten figures** the replies use for their sizes or tests, from the pack, in code, and say which matched. Pick the ones the key's items rest on first.
- **Ranking.** Does the report's order follow its own rule (evidence level first, then income effects by size, then balances)? Is any item on the list one that should not be there (an explained item, a tie-out gap dressed as a finding, a claim tested against a number of the wrong scope)? Is anything in "Also noted" or "Checked and explained" that belongs on the list?
- **Defects.** Continue the numbering in `tests/<company>/score.md` if one exists (AK for answer-key defects, PR for prompt defects, PK for pack defects); otherwise start at 1. A prompt defect is a wording that caused a miss or a wrong row, with the change that would fix it. One run is not enough to call a rule wrong; say "observed once" where that is the case.
- **Never** edit the replies, the prompts, the key or the pack. Write only `scoring/scorecard.md` and, if you compute, `scoring/recompute.py`.
- No em-dashes. Real company names are fine here; this file stays in the repo.

## Scorecard format

```
# Scorecard: <company>, prompts <version>, adapter <adapter>, run <nnn>

Scorer: <agent and model>, <date>. Inputs: <list>. Files the run saw: <list>.

## Verdict
One paragraph: pass or fail against the key's bar, and the one or two things that decided it.

| Condition | Required | Result | Met |
|---|---|---|---|

## K items
| ID | Req./bonus | In pack? | Caught by (reply, item) | Level expected / got | Score | Reason |
|---|---|---|---|---|---|---|

## Traps
| Trap | Hit? | Sentence or "none" |
|---|---|---|

## G1 and G2
Two lines.

## Measurements
Checker summary per reply (quotations exact on page / total; arithmetic mismatches; words). Then the ten recomputed figures: value, where in the pack, match or not.

## Ranking
Short paragraph: order followed its rule or not; items that should not be on the list; items that should.

## Defects
### Answer key
| # | Item | Defect | Evidence | Fix |
### Prompts
| # | Prompt | Defect | Proposed change |
### Pack
| # | Defect | Effect | Fix |
```

## This run

- Company: hertz-fy2013. Prompts: v2.24 (repo commit 601c414). Adapter: claude-code. Model: claude-opus-5-5. Cutoff: 2014-03-31.
- Run folder: `runs/hertz-fy2013/v2.24/claude-code/002/`; record `run.json` there.
- Files the run saw (full set): statements.xlsx, annual-report-FY2012-12-31.txt, annual-report-FY2013-12-31.txt, earnings-release-Q4-FY2012-12-31.txt, earnings-release-Q4-FY2013-12-31.txt, in `runs/hertz-fy2013/v2.24/claude-code/002/workspace/`.
- Replies and checker results:
- `runs/hertz-fy2013/v2.24/claude-code/002/numbers-1.md`: 0/1 quotations exact on page; 0 arithmetic mismatches; 854 words; checker report `runs/hertz-fy2013/v2.24/claude-code/002/check-numbers-1.md`
- `runs/hertz-fy2013/v2.24/claude-code/002/numbers-2.md`: 0/17 quotations exact on page; 2 arithmetic mismatches; 1109 words; checker report `runs/hertz-fy2013/v2.24/claude-code/002/check-numbers-2.md`
- `runs/hertz-fy2013/v2.24/claude-code/002/text-3.md`: 15/20 quotations exact on page; 1 arithmetic mismatches; 1292 words; checker report `runs/hertz-fy2013/v2.24/claude-code/002/check-text-3.md`
- `runs/hertz-fy2013/v2.24/claude-code/002/text-4.md`: 29/49 quotations exact on page; 1 arithmetic mismatches; 1630 words; checker report `runs/hertz-fy2013/v2.24/claude-code/002/check-text-4.md`
- `runs/hertz-fy2013/v2.24/claude-code/002/report-5.md`: 10/16 quotations exact on page; 0 arithmetic mismatches; 1058 words; checker report `runs/hertz-fy2013/v2.24/claude-code/002/check-report-5.md`
- Answer key: `tests/hertz-fy2013/answer-key.md`; prior score with defect numbering: `tests/hertz-fy2013/score.md`
- Measures: `tools/TESTS.md`, section on measures.
- Write the scorecard to `runs/hertz-fy2013/v2.24/claude-code/002/scoring/scorecard.md`.
