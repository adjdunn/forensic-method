# Test T1: Hertz Global Holdings, as of 31 March 2014

The first real-company test of the forensic prompts (v0.2). Profile T1 in [tools/TESTS.md](../../tools/TESTS.md): a US GAAP filer with a resolved SEC enforcement history, tested on the filings an analyst could read before the company admitted anything.

## Why Hertz

The SEC's settled order (Securities Act Release 10601, December 2018) names specific sentences in the 2013 10-Qs and the FY2013 10-K that were visible at the time, which gives the test an answer key from a primary document. The company also has an unclassified balance sheet, no cost-of-sales line, a rental fleet outside PP&E and a large acquisition inside the window (Dollar Thrifty, November 2012), so it stresses the prompts in ways a tidy industrial company would not.

Caveat: two of F4's ten consistency checks were written from this case. A pass on those tests whether the tool finds a known signal, not whether it generalizes. The held-back company (T5) is the generalization test.

## Folders

| Path | What |
|---|---|
| `answer-key.md` | Written from the SEC order before any prompt ran. The runners never see it |
| `pack/` | What the prompts get: manifest, statements.xlsx, section text files, releases, proxies, events |
| `build/` | How the pack was built: EDGAR downloads, report parser, workbook builder, tie-out |
| `runs/v0.2-claude-code/` | Dry-run outputs, one file per prompt, plus the context sheet and ledgers |
| `score.md` | The scored comparison of the runs against the answer key |

## Protocol

1. **Pack frozen before any run.** Built from EDGAR only, as originally reported, cut off at 31 March 2014. The workbook ties out on every balance sheet, cash-flow total and quarter-to-year sum (`build/tieout.md`).
2. **Answer key written before any run**, from the SEC order alone.
3. **Prompts frozen at v0.2.** No prompt edits during the run. Changes found necessary go into TESTS.md as v0.3 items.
4. **Blind runners.** Each prompt is run by a fresh agent that may read only its prompt file, the pack, and the outputs of earlier steps it is told to attach. It may not open the answer key, the research files, the manual or this README's scoring section. It uses Python for arithmetic, standing in for a chat platform's code tool.
5. **Order.** F1 first. F2, F3 and F4 in parallel, each given the context sheet. F5 given the four ledgers. F6 is not run: it needs the analyst's verdicts.
6. **Scoring** by a separate agent against the answer key and TESTS.md's measures: the K items, the traps, 20 sampled numbers recomputed from the pack, 20 sampled locators opened, quotations checked, benign readings present, no banned words, nothing from after the cut-off.

## What this dry run does not test

The chat platforms. A Claude Code agent has more room than a chat message and a different file-handling path. The platform check (prompt length, workbook reading by sheet name, ledger handoff) is separate and is Aaron's.
