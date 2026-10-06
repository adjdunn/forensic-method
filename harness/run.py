"""Run the five prompts on one company's pack through an adapter, check every reply, and write a run record.

    python harness/run.py --company home-depot-fy2025 --prompts v2.22 --adapter claude-code --repeat 2
    python harness/run.py --company hertz-fy2013 --prompts v2.22 --adapter manual        # writes the prompts and the file set for a person
    python harness/run.py --check runs/hertz-fy2013/v2.22/manual/001                     # checks replies that were added by hand

Each run gets its own folder, runs/<company>/<version>/<adapter>/<nnn>/, holding:
    workspace/        the allow-listed files, and nothing else: this is all the model sees
    prompt-1.md ...   the prompt text as sent (prompt 5 with the numbers-track replies pasted in)
    numbers-1.md, numbers-2.md, text-3.md, text-4.md, report-5.md   the replies
    check-*.md/json   the citation checker's report on each reply
    run.json          the record: file set, adapter, model, prompt hashes, repo commit, cost, timings

The adapters:
    claude-code   a fresh headless Claude Code conversation per track (claude -p), with Read, Bash, Write, Glob and Grep
                  and no web tools; prompt 2 resumes prompt 1's conversation, prompts 4 and 5 resume prompt 3's
    manual        no model call: the prompts and the workspace are written for a person to run in a chat platform,
                  and --check grades the replies they drop into the folder

What the runner does not do: it never reads or copies the answer key, score.md, README.md or config.json into the
workspace, whatever the allow-list says. The allow-list names files in the pack; anything else is refused.
"""
import argparse, datetime as dt, hashlib, json, os, re, shutil, subprocess, sys, uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROMPTS = ROOT / "tools" / "prompts"
PACKS = ROOT / "test-data"
RUNS = ROOT / "runs"
sys.path.insert(0, str(ROOT / "harness"))
import check_citations as cc  # noqa: E402

NEVER = re.compile(r"(answer-key|score\.md|README\.md|config\.json|\.\./|\\\.\.|^/|^[A-Za-z]:)", re.I)
STEPS = [  # (prompt number, track, reply file name)
    (1, "numbers", "numbers-1.md"), (2, "numbers", "numbers-2.md"),
    (3, "text", "text-3.md"), (4, "text", "text-4.md"), (5, "text", "report-5.md"),
]
SYSTEM_NOTE = (
    "You are a chat assistant. The user has attached these files, which are in the current working directory and are "
    "the only documents available: {files}. Use nothing else about this company. Python is available through Bash for "
    "calculations; do every calculation in code. Your final message is the reply to the user: write it in markdown, "
    "with no preamble about what you are going to do."
)


# ---------- prompts ----------

def load_prompt(n: int) -> tuple[str, str]:
    path = next(PROMPTS.glob(f"{n}-*.md"))
    text = path.read_text(encoding="utf-8")
    body = text.split("\n---\n", 1)[1].strip() if "\n---\n" in text else text
    if "—" in body:
        raise SystemExit(f"{path.name} contains an em-dash")
    return path.name, body


def prompt_hashes() -> dict:
    return {load_prompt(n)[0]: hashlib.sha256(load_prompt(n)[1].encode()).hexdigest()[:12] for n in range(1, 6)}


# ---------- workspace ----------

def build_workspace(pack: Path, cfg: dict, variant: str, run_dir: Path) -> list[str]:
    files = cfg["attach"].get(variant)
    if not files:
        raise SystemExit(f"config.json has no attach set '{variant}' (has {list(cfg['attach'])})")
    ws = run_dir / "workspace"
    ws.mkdir(parents=True, exist_ok=True)
    for f in files:
        if NEVER.search(f):
            raise SystemExit(f"refusing to attach {f}")
        src = pack / f
        if not src.is_file():
            raise SystemExit(f"missing from pack: {f}")
        shutil.copy2(src, ws / f)
    return files


# ---------- adapters ----------

def claude_bin() -> str:
    """The Claude Code binary: CLAUDE_BIN if set, else the desktop app's bundled CLI (CLAUDE_CODE_EXECPATH, newer than the
    winget install), else whatever `claude` is on the path. The model names the harness uses need CLI 2.1.280 or newer."""
    for var in ("CLAUDE_BIN", "CLAUDE_CODE_EXECPATH"):
        if os.environ.get(var) and Path(os.environ[var]).is_file():
            return os.environ[var]
    return "claude"


class ClaudeCode:
    name = "claude-code"

    def __init__(self, model: str | None, budget: float | None):
        self.model, self.budget = model, budget
        self.sessions: dict[str, str] = {}

    def ask(self, track: str, prompt: str, workdir: Path, files: list[str]) -> dict:
        cmd = [claude_bin(), "-p", "--output-format", "json", "--dangerously-skip-permissions",
               "--tools", "Read,Bash,Write,Glob,Grep", "--disallowedTools", "WebFetch,WebSearch,Agent",
               "--append-system-prompt", SYSTEM_NOTE.format(files=", ".join(files))]
        if self.model:
            cmd += ["--model", self.model]
        if self.budget:
            cmd += ["--max-budget-usd", str(self.budget)]
        if track in self.sessions:
            cmd += ["--resume", self.sessions[track]]
        else:
            self.sessions[track] = str(uuid.uuid4())
            cmd += ["--session-id", self.sessions[track]]
        t0 = dt.datetime.now()
        proc = subprocess.run(cmd, input=prompt, capture_output=True, text=True, encoding="utf-8", cwd=str(workdir), shell=(os.name == "nt"))
        raw = proc.stdout.strip()
        try:
            out = json.loads(raw[raw.index("{"):]) if "{" in raw else {}
        except json.JSONDecodeError:
            out = {}
        return {"reply": out.get("result", "") if not out.get("is_error") else "",
                "error": out.get("result") if out.get("is_error") or proc.returncode else (proc.stderr[-2000:] if not out else None),
                "session_id": out.get("session_id", self.sessions[track]), "cost_usd": out.get("total_cost_usd"),
                "usage": out.get("usage"), "models": list((out.get("modelUsage") or {}).keys()),
                "num_turns": out.get("num_turns"), "seconds": round((dt.datetime.now() - t0).total_seconds(), 1)}


class Manual:
    name = "manual"

    def ask(self, track, prompt, workdir, files):
        return {"reply": "", "error": None, "session_id": None, "note": "manual adapter: paste prompt into a chat, save the reply here"}


# ---------- the run ----------

def next_run_dir(company: str, version: str, adapter: str) -> Path:
    base = RUNS / company / version / adapter
    base.mkdir(parents=True, exist_ok=True)
    n = 1 + max([int(p.name) for p in base.iterdir() if p.is_dir() and p.name.isdigit()] or [0])
    d = base / f"{n:03d}"
    d.mkdir()
    return d


def git_commit() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True, cwd=str(ROOT)).stdout.strip()
    except Exception:
        return ""


def check_reply(run_dir: Path, pack: Path, reply_file: str) -> dict | None:
    path = run_dir / reply_file
    if not path.is_file() or path.stat().st_size == 0:
        return None
    base = reply_file.rsplit(".", 1)[0]
    argv = [str(path), "--pack", str(pack), "--out", str(run_dir / f"check-{base}.md"), "--json", str(run_dir / f"check-{base}.json")]
    old = sys.argv
    sys.argv = ["check_citations.py"] + argv
    try:
        import io, contextlib
        with contextlib.redirect_stdout(io.StringIO()):
            cc.main()
    finally:
        sys.argv = old
    return json.loads((run_dir / f"check-{base}.json").read_text(encoding="utf-8"))["summary"]


def do_run(a) -> Path:
    pack = PACKS / a.company
    cfg = json.loads((pack / "config.json").read_text(encoding="utf-8"))
    adapter = ClaudeCode(a.model, a.max_budget) if a.adapter == "claude-code" else Manual()
    run_dir = next_run_dir(a.company, a.prompts, a.adapter)
    files = build_workspace(pack, cfg, a.files, run_dir)
    record = {"company": a.company, "prompts_version": a.prompts, "prompt_hashes": prompt_hashes(), "repo_commit": git_commit(),
              "adapter": a.adapter, "model_requested": a.model, "file_set": a.files, "files": files,
              "cutoff": cfg.get("cutoff"), "started": dt.datetime.now().isoformat(timespec="seconds"), "dry_run": a.dry_run,
              "steps": []}
    replies: dict[str, str] = {}
    for n, track, out_name in STEPS:
        pname, body = load_prompt(n)
        if n == 5:
            pasted = "\n\n".join(f"### Numbers track, reply {k}\n\n{replies.get(k, '[reply missing]')}" for k in (1, 2))
            body = body.replace("[paste them here]", pasted)
        (run_dir / f"prompt-{n}.md").write_text(body, encoding="utf-8")
        step = {"prompt": n, "file": pname, "track": track, "reply_file": out_name}
        if a.dry_run or a.adapter == "manual":
            step["status"] = "not run"
        else:
            print(f"  prompt {n} ({track}) ...", flush=True)
            res = adapter.ask(track, body, run_dir / "workspace", files)
            step.update({k: v for k, v in res.items() if k != "reply"})
            if res["error"] or not res["reply"]:
                step["status"] = "error"
                record["steps"].append(step)
                print(f"  prompt {n} failed: {str(res['error'])[:300]}")
                break
            (run_dir / out_name).write_text(res["reply"], encoding="utf-8")
            replies[n] = res["reply"]
            step["status"] = "ok"
            step["check"] = check_reply(run_dir, pack, out_name)
            # the model may have written files into the workspace; keep its code, nothing else is read back
        record["steps"].append(step)
    record["finished"] = dt.datetime.now().isoformat(timespec="seconds")
    record["cost_usd"] = round(sum(s.get("cost_usd") or 0 for s in record["steps"]), 4)
    record["models"] = sorted({m for s in record["steps"] for m in (s.get("models") or [])})
    (run_dir / "run.json").write_text(json.dumps(record, indent=1), encoding="utf-8")
    if a.adapter == "manual" or a.dry_run:
        (run_dir / "README.md").write_text(
            f"# Manual run: {a.company}, prompts {a.prompts}\n\nAttach every file in `workspace/` to a new chat, paste `prompt-1.md`, "
            f"then `prompt-2.md` in the same chat. In a second chat with the same files, paste `prompt-3.md`, `prompt-4.md`, then `prompt-5.md` "
            f"with the two numbers-track replies pasted under its last line. Save the replies here as numbers-1.md, numbers-2.md, text-3.md, "
            f"text-4.md and report-5.md (text or PDF), then run:\n\n    python harness/run.py --check {run_dir.relative_to(ROOT).as_posix()}\n",
            encoding="utf-8")
    return run_dir


def do_check(run_path: str):
    run_dir = Path(run_path) if Path(run_path).is_absolute() else ROOT / run_path
    record = json.loads((run_dir / "run.json").read_text(encoding="utf-8"))
    pack = PACKS / record["company"]
    for step in record["steps"]:
        for ext in ("md", "txt", "pdf"):
            f = step["reply_file"].rsplit(".", 1)[0] + "." + ext
            if (run_dir / f).is_file():
                step["reply_file"] = f
                step["check"] = check_reply(run_dir, pack, f)
                step["status"] = "checked"
                print(f"  {f}: {step['check']['quotes']['exact_on_page']}/{step['check']['quotes']['total']} quotations exact on page, "
                      f"{step['check']['arithmetic']['mismatches']} arithmetic mismatches, {step['check']['words']} words")
                break
    (run_dir / "run.json").write_text(json.dumps(record, indent=1), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--company"); ap.add_argument("--prompts", default="current")
    ap.add_argument("--adapter", default="claude-code", choices=["claude-code", "manual"])
    ap.add_argument("--files", default="default", help="attach set from config.json: default, full or chat")
    ap.add_argument("--repeat", type=int, default=1)
    ap.add_argument("--model", default="claude-opus-5-5", help="model id passed to the CLI; the CLI's own default can be an older model")
    ap.add_argument("--max-budget", type=float)
    ap.add_argument("--dry-run", action="store_true", help="build the workspace and the prompts, call no model")
    ap.add_argument("--check", help="run the checker over the replies in an existing run folder")
    a = ap.parse_args()
    if a.check:
        do_check(a.check); return
    if not a.company:
        ap.error("--company is required")
    for i in range(a.repeat):
        print(f"run {i + 1} of {a.repeat}: {a.company}, prompts {a.prompts}, adapter {a.adapter}, files {a.files}")
        d = do_run(a)
        print(f"  -> {d.relative_to(ROOT).as_posix()}")


if __name__ == "__main__":
    main()
