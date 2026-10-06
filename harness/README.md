# Harness

Grades any adapter's output the same way. Two scripts so far, both built 6 October 2026.

## run.py: run the five prompts and record everything

```
python harness/run.py --company home-depot-fy2025 --prompts v2.22 --adapter claude-code --repeat 2
python harness/run.py --company hertz-fy2013 --prompts v2.22 --adapter manual
python harness/run.py --check runs/hertz-fy2013/v2.22/manual/001
```

Each run gets a folder `runs/<company>/<version>/<adapter>/<nnn>/`:

| File | What |
|---|---|
| `workspace/` | The allow-listed files from the pack's `config.json` (`--files default`, `full` or `chat`), and nothing else. This is all the model sees. The runner refuses anything that looks like an answer key, a score, a README or a config, whatever the allow-list says. Not committed |
| `prompt-1.md` to `prompt-5.md` | The prompt text as sent: the body of each file in `tools/prompts/`, without its header; prompt 5 with the two numbers-track replies pasted in |
| `numbers-1.md`, `numbers-2.md`, `text-3.md`, `text-4.md`, `report-5.md` | The replies |
| `check-*.md` and `.json` | The citation checker's report on each reply |
| `run.json` | The record: company, prompt version and a hash of each prompt, repo commit, adapter, model, file set, cutoff, per-step status, session, cost, turns and seconds, and each check's summary |

Adapters:

- **claude-code**: a fresh headless Claude Code conversation per track (`claude -p`, JSON output), with Read, Bash, Write, Glob and Grep and no web tools, working in the run's workspace. Prompt 2 resumes prompt 1's conversation; prompts 4 and 5 resume prompt 3's. An appended system note tells the model the files in the directory are the user's attachments and the only documents available. Pass `--model` and `--max-budget` as needed. The CLI must be logged in (`claude`, then `/login`); a revoked token shows up as a 401 recorded in `run.json` and the run stops.
- **manual**: no model call. Writes the prompts, the workspace and a README for a person to run the prompts in a chat platform. Drop the replies into the folder (markdown, text or PDF) and `--check` grades them. This is how the October 2026 chat runs are checked.

`--repeat n` makes n runs with the same settings. Repeat runs establish the noise floor before a moved number is attributed to a prompt edit.

## check_citations.py: check one reply against its pack

```
python harness/check_citations.py <reply.md|.txt|.pdf> --pack test-data/<company> [--out report.md] [--json report.json]
```

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

The scorer: an agent that reads a run against the company's answer key the way `tests/hertz-fy2013/score.md` was done and writes one scorecard. Partial passes need a reader, so this stays an agent, not a script.

The test record for every version so far is `tools/TESTS.md`.
