# CAE Inc.: test data

IFRS, Canadian, files a 40-F with the SEC. No known enforcement case. The workbook is annual only: the build reads 10-Q and annual-report XBRL, and CAE files its quarterly reports on Form 6-K.

**Window:** SEC filings made from 2024-04-01 to 2026-09-26. Nothing filed after 2026-09-26 is included, so the documents show only what an analyst could have read on that date.

## Files

| File | What it is | Size |
|---|---|---|
| `statements.xlsx` | Income statement, balance sheet and cash flow as the company presents them, in CAD millions. Annual: 4 fiscal years, 2023-03-31 to 2026-03-31. Quarterly: none (annual only). As originally reported; 2 later changes listed on the Revisions sheet. An Industry sheet gives Damodaran's industry averages for the matching year | small |
| `annual-report-FY2025-03-31.txt` | 40-F exhibits for the year ended 2025-03-31: annual information form, MD&A, audited statements | 643,050 characters, about 161k tokens |
| `annual-report-FY2025-03-31-key-sections.txt` | same 40-F, MD&A and audited statements only | 490,470 characters, about 123k tokens |
| `annual-report-FY2026-03-31.txt` | 40-F exhibits for the year ended 2026-03-31: annual information form, MD&A, audited statements | 637,811 characters, about 159k tokens |
| `annual-report-FY2026-03-31-key-sections.txt` | same 40-F, MD&A and audited statements only | 477,556 characters, about 119k tokens |
| `earnings-release-Q4-FY2025-03-31.txt` | results release furnished 2025-05-13 on 6-K | 66,128 characters, about 17k tokens |
| `earnings-release-Q4-FY2026-03-31.txt` | results release furnished 2026-05-21 on 6-K | 74,056 characters, about 19k tokens |

Token counts are estimates (characters divided by four). A chat conversation holds roughly 150k to 200k tokens on most plans. If the two full annual reports will not fit, attach the key-sections files instead.

## What to attach for each prompt

| Prompt | Attach |
|---|---|
| 1. Working capital | `statements.xlsx` |
| 2. Earnings quality | Nothing new. Add `earnings-release-Q4-FY2025-03-31.txt` and `earnings-release-Q4-FY2026-03-31.txt` for the adjusted-earnings check |
| 3. Footnote changes | `annual-report-FY2025-03-31-key-sections.txt` and `annual-report-FY2026-03-31-key-sections.txt` |
| 4. Consistency check | Nothing new, if prompts 1 to 3 ran in the same conversation |
| 5. Red-flag report | Nothing new |

## Amendments filed in the window

- None in the window.

## How this was built

`../_build/build.py cae-fy2026` downloads the filings from EDGAR, parses the rendered statement pages (the R files behind each filing's "Financial Report"), and converts the annual reports and releases from HTML to text. Rerunning it reproduces the folder.
