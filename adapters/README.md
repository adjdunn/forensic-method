# Adapters

One thin runner per platform. Every adapter takes the same inputs (a prompt version, a company's allow-listed file set) and produces replies in the same shape (one markdown file per prompt, per track, plus a run record), so the harness grades them all alike.

| Adapter | Status |
|---|---|
| `claude-code`: a fresh headless Claude Code agent per track | first to build |
| `claude-api`: the Claude API with the code-execution tool | after adapter one is stable |
| `openai`: the OpenAI API with its code tool | later |
| `manual`: a person pasting the prompts into Claude or ChatGPT chat and saving the replies | in use since October 2026; the acceptance test for every settled version |

"Runs everywhere" is a table: same pack, same prompt version, every adapter, one scorecard each.
