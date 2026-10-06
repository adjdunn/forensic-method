# Harness

Grades any adapter's output the same way. Planned contents, in build order:

1. `check-citations.py`: input is a run's reply (markdown or PDF) and the company's pack; output is a report of quotations exact and on the cited page, figures present or derived, arithmetic recomputed, banned words, post-cutoff facts, reply length.
2. `run.py --company <id> --prompts <version> --adapter <name> --repeat <n>`: runs both tracks and the report through an adapter with an allow-listed file set from the company's config, saves replies under `runs/<company>/<version>/<adapter>/<n>/`, calls the checker, writes a run record (file set, adapter, model, date). Repeat runs establish the noise floor before a moved number is attributed to a prompt edit.
3. The scorer: an agent that reads a run against the company's answer key the way `tests/hertz-fy2013/score.md` was done and writes one scorecard. Partial passes need a reader, so this stays an agent, not a script.

The test record for every version so far is `tools/TESTS.md`.
