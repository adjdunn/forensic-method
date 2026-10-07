# Cloud session brief: write an answer key from an SEC order

For a Claude Code cloud session started on this repository. One job: write `tests/<company>/answer-key.md` for a named company from the SEC's settled order alone, before any prompt run on that company is scored, in the same shape as `tests/hertz-fy2013/answer-key.md`. The key is scorer-only: it never reaches a runner.

## Protocol (from `tests/hertz-fy2013/README.md`, "Protocol")

1. **The order is the only source.** Download the SEC's settled administrative order (the PDF from sec.gov/litigation/admin, or the AAER) and read the whole document. Do not write any number, date, quotation or paragraph reference from a summary, a search snippet or memory. Where a fetch tool returns a summary instead of the document, discard it and download the file. Save the text you read as `tests/<company>/sources/<release>.txt` with the URL and the download date at the top.
2. **Key before any run.** If `runs/<company>/` already holds runs, do not open them. The key must be written blind to what the prompts found.
3. **Marks.** Every statement in the key carries one of the Hertz key's marks: `[order ¶N]` for a paragraph of the order, `[order §X]` for a section, `[inf]` for your inference with the reasoning written out, `[brief]` for a fact supplied here that the order does not state, `[conv]` for a scoring convention.
4. **Items.** For each thing the order says was visible in the company's filings at the time, one K item in the Hertz key's layout: the order's paragraph, the quotation from the order (quoting the filing where it does), the order's finding, the filing and period, the checklist reference, the expected catch, the PASS criterion, the benign reading a good row carries, and where the order is vague. Mark required items and bonus items. Then the traps: things the order says that were not visible in the filings, or that a run could only know from the order; a run that states one of them as fact has hit a trap. Then G1 (no fraud, manipulation, red flag in the run's own sentences) and G2 (nothing from after the pack's cutoff used as fact).
5. **Scope by file set.** The pack holds the two annual reports, the two fourth-quarter releases and the statements workbook (`test-data/<company>/config.json`). For each K item say which document it needs. An item that needs a 10-Q, an interim release, a call deck or a proxy is marked "needs: <document>" and the pass bar is stated for the five-file pack as well as for a fuller pack (the Hertz key's AK10 lesson).
6. **Priority mapping.** The v2 prompts rank by evidence level: 1 (a sentence contradicted by the company's own numbers or another sentence in the same report), 2 (two or more signals on one account), 3 (a single signal); "checked and explained" is P4. State each item's expected level in those terms.
7. **Cutoff.** The pack's cutoff date is in `config.json`. Everything the order describes after that date is outside the pack; list it under "what the pack cannot show", as the Hertz key's section 1 does.
8. **Pass bar.** State it at the end, per file set: which items are required at which level, the trap count allowed (zero), G1, G2.

## Companies

| Company | Pack | Order | Cutoff |
|---|---|---|---|
| Under Armour, Inc. | `test-data/under-armour-fy2016` | The SEC's settled order of May 2021 (pull-forwards of orders from later quarters, Q3 2015 to Q4 2016; the order makes no finding that GAAP was violated). Find the release numbers on the document itself | 2017-03-31 |
| The Kraft Heinz Company | `test-data/kraft-heinz-fy2017` | The SEC's settled order of September 2021 (supplier cost savings recognised early, lowering cost of sales and lifting Adjusted EBITDA, Q4 2015 to 2018). Find the release numbers on the document itself | 2018-12-31 |

The `README.md` in each pack folder states the case in one line; take the release numbers from the order, not from there.

## Also, for Hertz

Apply the corrections AK1 to AK12 to `tests/hertz-fy2013/answer-key.md`: AK1 to AK7 are in `tests/hertz-fy2013/score.md` section 11; AK8 to AK12 are in the scorecards under `runs/hertz-fy2013/v2.22/manual/001/scoring/`, `runs/hertz-fy2013/v2.22/claude-code/001/scoring/` and `runs/hertz-fy2013/v2.23/claude-code/001/scoring/`. Keep the original text in place under a dated "superseded" mark where the Hertz key's addendum convention does, so the pre-run version stays on record. Do not change any K item's substance beyond what a numbered correction says.

## Rules

- No em-dashes in anything written.
- Write only under `tests/<company>/` (the key, a README in the Hertz shape, a `sources/` folder with the order's text). Touch nothing in `tools/`, `test-data/`, `harness/` or `runs/`.
- Commit each company's key separately, push to `main`, and in the commit message give the order's release number and date as the document states them.
- If the order cannot be downloaded and read in full, stop and say so. A key written from anything less is worse than no key.
