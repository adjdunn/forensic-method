# Harness

Grades any adapter's output the same way.

## check_citations.py (built 6 October 2026)

```
python harness/check_citations.py <reply.md|.txt|.pdf> --pack test-data/<company> [--out report.md] [--json report.json]
```

Reads one prompt reply and the company's pack (`test-data/<company>/`, with its `config.json`) and reports:

| Check | What it does |
|---|---|
| Quotations | Every `"quoted passage"` in the reply: exact in a pack document, and on the page the reply cites (the `[p. N]` markers). An elided quotation ("A... B") counts when every part is on the same page. The document is read from the citation's own words (a year, "release", "last year's report"); when the citation says nothing, every document is searched |
| Figures | Every money amount and every figure with a decimal or a thousands separator: printed in a pack document or in the statements workbook, or not. Not printed is not an error on its own (sums and shares are derived); the list is for a reader. Percentages are listed separately |
| Arithmetic | Where a sentence pairs an amount with its share of pre-tax income ("$746m, 113% of pre-tax income"; "113% of pre-tax income ($746m ...)"), the share is recomputed against the pre-tax income the reply states, or the workbook's latest year when the reply does not state it |
| Banned words | fraud, manipulation, red flag; em-dashes |
| Post-cutoff | Years later than the pack's cutoff mentioned in the reply, with context. A recommendation to read a later filing is fine; a fact from one is not |
| Length | Words and an estimate of pages |

Calibrated on the October 2026 Claude chat runs (Home Depot and Hertz, prompts 1 to 5), which had been checked by hand first: the script finds the same quotations exact and on the cited page, and its remaining "look at" lines are the genuine ambiguities (a one-word quotation that appears on many pages; a quotation whose sentence carries two citations). What it does not do: judge whether a derived figure is right, or whether a reading is fair. Those stay with the scorer and the reader.

## Planned

1. `run.py --company <id> --prompts <version> --adapter <name> --repeat <n>`: runs both tracks and the report through an adapter with the allow-listed file set from the company's `config.json`, saves replies under `runs/<company>/<version>/<adapter>/<n>/`, calls the checker, writes a run record (file set, adapter, model, date). Repeat runs establish the noise floor before a moved number is attributed to a prompt edit.
2. The scorer: an agent that reads a run against the company's answer key the way `tests/hertz-fy2013/score.md` was done and writes one scorecard. Partial passes need a reader, so this stays an agent, not a script.

The test record for every version so far is `tools/TESTS.md`.
