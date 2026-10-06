# The forensic prompts

Five short prompts that run a forensic pass on a company's filings in one Claude or ChatGPT conversation. Built to demonstrate the method and to be usable as-is. The depth (the full checklist, the rules behind each test, the case library) lives in the manual, not in the prompts.

## The idea

Extracting numbers and calculating ratios is the easy part: a data terminal, a spreadsheet or a script does it. The prompts put the model to work where it adds something those cannot: picking the movements that matter, following each one into the footnotes and releases for the company's explanation, and reading the notes themselves, including what changed from last year.

The pass is not only about fraud. Most of what it finds is a business weakening or earnings of poor quality, which is far more common and matters just as much to an investor or lender.

## How to run

The prompts run as two tracks, each in its own conversation, so each track shows its own best findings in full.

1. **Numbers track.** In a new conversation, attach the statements spreadsheet, the last two annual reports and the last two fourth-quarter results releases. Paste prompt 1, then prompt 2.
2. **Text track.** In a second new conversation, attach the same files. Paste prompt 3, then prompt 4.
3. **Report.** In the text-track conversation, paste prompt 5 with the two numbers-track replies pasted under it. It turns all four replies into a one-page review.

One reply at a time. Either track can be run without the other.

| # | Prompt | Track | What it does | Reads |
|---|---|---|---|---|
| 1 | [Scan the numbers](prompts/1-scan-the-numbers.md) | Numbers first | Working-capital, margin, accrual, cash and depreciation measures, the M-score, revised figures. Picks up to five flags, without explaining them | Spreadsheet |
| 2 | [Follow the flags](prompts/2-follow-the-flags.md) | Numbers first | For each flag: the company's explanation, quoted; whether it gave the same one last year; what the note adds; a test of the explanation against the numbers; three readings. Plus adjusted earnings and reserve releases | Annual reports, releases |
| 3 | [Read the footnotes](prompts/3-read-the-footnotes.md) | Text first | One year's notes read for what no ratio shows: revenue terms, estimates and reserves, changes in estimates, off-balance-sheet items, related parties, contingencies, the auditor's report, adjusted measures | Latest annual report, and the latest release for the adjusted measures |
| 4 | [Compare the footnotes](prompts/4-compare-the-footnotes.md) | Text first | Sentences added, reworded or dropped between two years, and a side-by-side table of statements that stayed the same, each tested against its number | Both annual reports |
| 5 | [Report](prompts/5-report.md) | | One page: top five items ranked by strength of evidence, what was checked and explained, what was not examined | Nothing new |

Prompt 3 judges the latest annual report on its own and uses last year's only for a figure a calculation needs. Prompt 4 needs both. Both tracks get the same five files, so the two conversations compare like with like.

**Size.** Two 10-Ks and two releases run from about 150k to 330k tokens. Claude chat took the largest pair in testing (Hertz, full reports) without trouble. For a company whose reports are too large for the platform, `test-data/_build/chat_cut.py` makes a `-chat` copy of each key-sections file with the bulk of the debt, pension and stock-compensation notes and the prior year's own comparison cut out, every cut marked in the text and the page markers unchanged.

## The rules every prompt carries

Use only the attached documents, and nothing that happened later. Calculate in code. Quote exactly, with the document and page; name the sheet and line for spreadsheet figures. Where a sentence makes a claim a number can test, test it. Give each item one reading, worded as a likelihood and never as a fact: most likely ordinary, the business weakening, the reporting stretched, or can't tell; and say what would point elsewhere. Say which figures are on which basis after a revision. Don't estimate what isn't there. Call results things to check, not findings.

## Where these came from

- **v0.2, six long prompts.** Built to the whole checklist and tested blind on Hertz Global Holdings as of March 2014, a real SEC enforcement case. Accurate, and far too long for a chat reply (16,000 to 46,000 words per step). In [archive/v0.2-full/](archive/v0.2-full/).
- **v1, five short prompts by topic** (working capital, earnings quality, footnote changes, consistency check, report). Replies of about a page. Tuning prompt 1 on Under Armour showed that the ratios were the least valuable part and the notes behind them the most. In [archive/v1-short/](archive/v1-short/).
- **v2, the current set.** Reorganized into a numbers-first track and a text-first track. The consistency check is no longer a separate prompt: testing a sentence against its number is a rule in prompts 2, 3 and 4. Prompt 3 is an absolute assessment of one year's accounting (where each policy sits: leans conservative, typical, leans aggressive, can't tell); prompt 4 is the comparison. Every item carries a size on one base, the effect on pre-tax income, with balances labelled, so prompt 5 can rank across the tracks. Run end to end in Claude chat on both a benign company and an enforcement case in October 2026, every output checked against the source files (v2.14 to v2.22 in [TESTS.md](TESTS.md)).

The test record and changelog are in [TESTS.md](TESTS.md). Test files for five real companies are in [../test-data/](../test-data/README.md).

## Upgrading later

The short prompts are the entry point. More powerful setups can be layered on later: a project instruction holding the rules, the long prompts' ledger and priority system, an agent that fetches filings itself. The v0.2 archive is the starting point for that.
