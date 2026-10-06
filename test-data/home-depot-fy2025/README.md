# The Home Depot, Inc.: test data

US GAAP. No known enforcement case. Two large acquisitions in the window: SRS (fiscal 2024) and GMS (fiscal 2025, through SRS), per the fiscal 2025 10-K. The benign test: balance-sheet jumps that an acquisition explains.

**Window:** SEC filings made from 2024-01-01 to 2026-09-26. Nothing filed after 2026-09-26 is included, so the documents show only what an analyst could have read on that date.

## Files

| File | What it is | Size |
|---|---|---|
| `statements.xlsx` | Income statement, balance sheet and cash flow as the company presents them, in USD millions. Annual: 5 fiscal years, 2022-01-30 to 2026-02-01. Quarterly: 14 quarters, 2023-04-30 to 2026-08-02. As originally reported; 4 later changes listed on the Revisions sheet. An Industry sheet gives Damodaran's industry averages for the matching year | small |
| `annual-report-FY2025-02-02.txt` | 10-K for the fiscal year ended 2025-02-02, full text (84 pages; page markers count pages from the start, because the filing's own page numbers could not be read) | 326,240 characters, about 82k tokens |
| `annual-report-FY2025-02-02-key-sections.txt` | same 10-K, Items 1 (business), 1A (risk factors), 3 (legal), 7 (MD&A), 8 (statements and notes), 9A (controls) | 272,277 characters, about 68k tokens |
| `annual-report-FY2026-02-01.txt` | 10-K for the fiscal year ended 2026-02-01, full text (85 pages; page markers count pages from the start, because the filing's own page numbers could not be read) | 331,610 characters, about 83k tokens |
| `annual-report-FY2026-02-01-key-sections.txt` | same 10-K, Items 1 (business), 1A (risk factors), 3 (legal), 7 (MD&A), 8 (statements and notes), 9A (controls) | 278,358 characters, about 70k tokens |
| `earnings-release-Q4-FY2025-02-02.txt` | results release furnished 2025-02-25 on 8-K | 20,065 characters, about 5k tokens |
| `earnings-release-Q4-FY2026-02-01.txt` | results release furnished 2026-02-24 on 8-K | 20,666 characters, about 5k tokens |

Token counts are estimates (characters divided by four). A chat conversation holds roughly 150k to 200k tokens on most plans. If the two full annual reports will not fit, attach the key-sections files instead.

## What to attach for each prompt

| Prompt | Attach |
|---|---|
| 1. Working capital | `statements.xlsx` |
| 2. Earnings quality | Nothing new. Add `earnings-release-Q4-FY2025-02-02.txt` and `earnings-release-Q4-FY2026-02-01.txt` for the adjusted-earnings check |
| 3. Footnote changes | `annual-report-FY2025-02-02-key-sections.txt` and `annual-report-FY2026-02-01-key-sections.txt` |
| 4. Consistency check | Nothing new, if prompts 1 to 3 ran in the same conversation |
| 5. Red-flag report | Nothing new |

## Amendments filed in the window

- None in the window.

## How this was built

`../_build/build.py home-depot-fy2025` downloads the filings from EDGAR, parses the rendered statement pages (the R files behind each filing's "Financial Report"), and converts the annual reports and releases from HTML to text. Rerunning it reproduces the folder.
