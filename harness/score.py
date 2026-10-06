"""Assemble the scoring bundle for one run, and optionally launch the scoring agent.

    python harness/score.py --run runs/hertz-fy2013/v2.22/manual/001            # writes scoring/brief.md, prints how to launch
    python harness/score.py --run runs/hertz-fy2013/v2.22/manual/001 --launch   # runs the scorer through headless Claude Code

The scorer is an agent, not a script: partial passes need a reader. This file only gathers what it needs into
scoring/brief.md inside the run folder (the brief, the paths, the checker summaries, the key's location) so that any
agent, local or cloud, can be pointed at one file. The answer key is read by the scorer and by nobody else in the harness.
"""
import argparse, json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def build_bundle(run_dir: Path) -> Path:
    record = json.loads((run_dir / "run.json").read_text(encoding="utf-8"))
    company = record["company"]
    key_dir = ROOT / "tests" / company
    key = key_dir / "answer-key.md"
    if not key.is_file():
        raise SystemExit(f"no answer key at {key}; the scorer needs one written before the run")
    score_prev = key_dir / "score.md"
    out = run_dir / "scoring"
    out.mkdir(exist_ok=True)
    brief = (ROOT / "harness" / "scorer-brief.md").read_text(encoding="utf-8")
    replies = []
    for s in record["steps"]:
        f = run_dir / s["reply_file"]
        if f.is_file():
            c = s.get("check") or {}
            q = c.get("quotes", {})
            replies.append(f"- `{f.relative_to(ROOT).as_posix()}`: {q.get('exact_on_page', '?')}/{q.get('total', '?')} quotations exact on page; "
                           f"{c.get('arithmetic', {}).get('mismatches', '?')} arithmetic mismatches; {c.get('words', '?')} words; "
                           f"checker report `{(run_dir / ('check-' + s['reply_file'].rsplit('.', 1)[0] + '.md')).relative_to(ROOT).as_posix()}`")
    workspace = run_dir / "workspace"
    pack_note = (f"`{workspace.relative_to(ROOT).as_posix()}/`" if workspace.is_dir()
                 else f"`test-data/{company}/` (the workspace is gone; use these files only: {', '.join(record['files'])})")
    this_run = "\n".join([
        f"- Company: {company}. Prompts: {record['prompts_version']} (repo commit {record.get('repo_commit', '?')}). "
        f"Adapter: {record['adapter']}. Model: {', '.join(record.get('models') or []) or 'not recorded'}. Cutoff: {record.get('cutoff')}.",
        f"- Run folder: `{run_dir.relative_to(ROOT).as_posix()}/`; record `run.json` there.",
        f"- Files the run saw ({record['file_set']} set): {', '.join(record['files'])}, in {pack_note}.",
        "- Replies and checker results:", *replies,
        f"- Answer key: `{key.relative_to(ROOT).as_posix()}`" + (f"; prior score with defect numbering: `{score_prev.relative_to(ROOT).as_posix()}`" if score_prev.is_file() else ""),
        "- Measures: `tools/TESTS.md`, section on measures.",
        f"- Write the scorecard to `{(out / 'scorecard.md').relative_to(ROOT).as_posix()}`.",
    ])
    (out / "brief.md").write_text(brief.rstrip() + "\n\n" + this_run + "\n", encoding="utf-8")
    return out / "brief.md"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True); ap.add_argument("--launch", action="store_true"); ap.add_argument("--model")
    a = ap.parse_args()
    run_dir = Path(a.run) if Path(a.run).is_absolute() else ROOT / a.run
    brief = build_bundle(run_dir)
    print(f"brief written: {brief.relative_to(ROOT).as_posix()}")
    prompt = f"Read {brief.relative_to(ROOT).as_posix()} and do what it says. Work from the repository root. Write only the files it allows."
    if a.launch:
        cmd = ["claude", "-p", "--output-format", "json", "--dangerously-skip-permissions",
               "--tools", "Read,Bash,Write,Glob,Grep", "--disallowedTools", "WebFetch,WebSearch"]
        if a.model:
            cmd += ["--model", a.model]
        proc = subprocess.run(cmd, input=prompt, capture_output=True, text=True, encoding="utf-8", cwd=str(ROOT), shell=(sys.platform == "win32"))
        print(proc.stdout[-3000:] or proc.stderr[-3000:])
    else:
        print("to score with a local agent:  claude  (from the repo root), then paste:\n  " + prompt)


if __name__ == "__main__":
    main()
