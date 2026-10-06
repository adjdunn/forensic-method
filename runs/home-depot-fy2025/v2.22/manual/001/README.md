# Manual run: home-depot-fy2025, prompts v2.22

Attach every file in `workspace/` to a new chat, paste `prompt-1.md`, then `prompt-2.md` in the same chat. In a second chat with the same files, paste `prompt-3.md`, `prompt-4.md`, then `prompt-5.md` with the two numbers-track replies pasted under its last line. Save the replies here as numbers-1.md, numbers-2.md, text-3.md, text-4.md and report-5.md (text or PDF), then run:

    python harness/run.py --check runs/home-depot-fy2025/v2.22/manual/001
