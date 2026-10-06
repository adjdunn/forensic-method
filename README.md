# Forensic method (working name)

Five short prompts that run a forensic accounting pass on a public company's filings in a chat assistant, and the harness that tests them. Built for an hour on AI-assisted forensic accounting for CFA Society Vancouver; meant to outlive it as an open-source method.

Private until v1. v1 means: the harness passes on five companies, the platform-parity table exists, and the method has a name.

## Three layers

| Layer | Where | What |
|---|---|---|
| **Method** | `tools/prompts/`, `tools/README.md` | The five prompts and the rules they share. Plain text, platform-neutral. Two tracks: numbers (prompts 1 and 2) and text (prompts 3 and 4), each in its own conversation; prompt 5 merges and ranks |
| **Adapters** | `adapters/` | One thin runner per platform, all producing replies in the same shape. First: headless Claude Code. Then the Claude API with code execution, then OpenAI. Manual chat runs are the fourth adapter, with a person as the runner |
| **Harness** | `harness/`, `test-data/`, `tests/` | Test packs (one folder per real company, built from EDGAR), answer keys written from the SEC orders before any run, the citation checker, the scorer, and the test record |

The manual and the research behind the method stay in the WireSift arena for now (`WireSift Research/Events/CFA Vancouver Forensic/manual/` and `research/`); this repo links to them.

## Where things are

| Thing | Location |
|---|---|
| Prompts, current version | `tools/prompts/1-scan-the-numbers.md` to `5-report.md` (version in `tools/TESTS.md`) |
| How to run them, the rules, where they came from | `tools/README.md` |
| Test record and changelog, every version since v0.2 | `tools/TESTS.md` |
| Five company packs | `test-data/<company>/`: Hertz FY2013, Under Armour FY2016, Kraft Heinz FY2017, Home Depot FY2025, CAE FY2026. Read `test-data/README.md` first |
| Pack builder, chat cut, HTML to text, industry sheet | `test-data/_build/` |
| Hertz answer key, score, scoring protocol, the original 25-file pack build | `tests/hertz-fy2013/` |
| PDF renderer for replies | `tools/render-pdf.py` |
| Long v0.2 prompt set (future agent material) | `tools/archive/v0.2-full/` |

Raw EDGAR downloads (`test-data/_build/cache/`, `tests/*/build/raw/`) are not committed; the build scripts fetch them again.

## Rules that bind every file here

- **Answer keys are scorer-only.** `tests/*/answer-key.md`, `score.md`, the research files and the manual never reach a runner agent. A runner's attachment list is an allow-list, never a folder.
- **The held-back company and its key never go public.** It lives in a folder excluded from the public repo for good, so the out-of-sample claim survives.
- **A prompt version is promoted only after one manual chat run.** The runner tests the prompts; the chat run tests the platform. Both are required.
- **No new numbers in prompt 5** beyond a share of pre-tax income. **No em-dashes** anywhere.
- **Real company names stay in the repo and the test logs.** They do not go in the presentation.
- Research integrity as in the WireSift standards: every number traced to a source with a locator, nothing fabricated, nothing estimated that is not in the documents.
