# Cloud session brief: run the battery

For a Claude Code cloud session started on this repository. Everything here is one job: run the current prompts on the named companies through the harness, check and score the replies, and push the results. Nothing else.

## Steps

1. Confirm the environment: `python --version` (3.11 or newer), `pip install pypdf openpyxl` if missing. Confirm the Claude Code CLI is present and can answer: `echo "Reply with the single word ok." | claude -p --output-format json --tools ""`. If it answers, the `claude-code` adapter works here. If it does not, use the fallback in step 3.
2. For each company named in the task, run:
   `python harness/run.py --company <id> --prompts <version> --adapter claude-code --files <set> --repeat <n>`
   with the file set the task names (`default` is the key-sections reports; `full` is the full reports; `chat` is the cut copies). Each run writes `runs/<company>/<version>/claude-code/<nnn>/` with the replies, the checker reports and `run.json`.
3. Fallback when no nested CLI is available: run `python harness/run.py --company <id> --prompts <version> --adapter manual --files <set>`, which writes `prompt-1.md` to `prompt-5.md` and a `workspace/` into a run folder. Then act as the adapter yourself: for the numbers track, start one fresh subagent whose working directory is that `workspace/`, give it `prompt-1.md` with the system note from `harness/run.py` (`SYSTEM_NOTE`), save its reply as `numbers-1.md`, then send `prompt-2.md` to the same subagent and save `numbers-2.md`. For the text track, a second fresh subagent: `prompt-3.md`, `prompt-4.md`, then `prompt-5.md` with the two numbers replies pasted under its last line (the runner has already pasted them if the numbers replies exist when you build the folder; otherwise paste them yourself). The subagents may use only the files in `workspace/`, Python for calculations, and no web tools; they must never open `tests/`, `tools/TESTS.md` or any `scoring/` folder. Then `python harness/run.py --check <run folder>`. Record in `run.json` that the adapter was `cloud-self` and which model the subagents used.
4. Score each run: `python harness/score.py --run <run folder>` writes `scoring/brief.md`; then start a fresh subagent that reads that brief and does what it says, writing `scoring/scorecard.md`. The scorer is the only agent that may read `tests/<company>/answer-key.md`.
5. Commit everything under `runs/` (workspaces are ignored) and push to `main`. In the commit message, give each run's verdict line from its scorecard.
6. Append one row per run to the "Runs" table in `tools/TESTS.md` (same shape as the existing rows) and one row per scorecard to "Harness scorecards", then commit and push again.

## Rules

- Prompts are not edited in a cloud run. If a scorecard raises prompt defects, they go in the scorecard and the TESTS.md row, numbered on from the last PR number used.
- No em-dashes in anything written.
- Real company names stay in the repo; nothing from a run goes anywhere else.
- If a step fails, record the failure in `run.json` or the TESTS.md row and go on to the next company.
