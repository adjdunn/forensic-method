# Under Armour, Inc.: test data

US GAAP. Resolved SEC case (order May 2021): undisclosed pull-forwards of next-quarter orders, Q3 2015 to Q4 2016. The order makes no finding that GAAP was violated.

**Window:** SEC filings made from 2015-01-01 to 2017-03-31. Nothing filed after 2017-03-31 is included, so the documents show only what an analyst could have read on that date.

## Files

| File | What it is | Size |
|---|---|---|
| `statements.xlsx` | Income statement, balance sheet and cash flow as the company presents them, in USD millions. Annual: 5 fiscal years, 2012-12-31 to 2016-12-31. Quarterly: 12 quarters, 2014-03-31 to 2016-12-31. As originally reported; 48 later changes listed on the Revisions sheet. An Industry sheet gives Damodaran's industry averages for the matching year | small |
| `annual-report-FY2015-12-31.txt` | 10-K for the fiscal year ended 2015-12-31, full text (79 pages; page markers are the printed page numbers) | 306,199 characters, about 77k tokens |
| `annual-report-FY2015-12-31-key-sections.txt` | same 10-K, Items 1 (business), 1A (risk factors), 3 (legal), 7 (MD&A), 8 (statements and notes), 9A (controls) | 268,095 characters, about 67k tokens |
| `annual-report-FY2016-12-31.txt` | 10-K for the fiscal year ended 2016-12-31, full text (84 pages; page markers are the printed page numbers) | 310,384 characters, about 78k tokens |
| `annual-report-FY2016-12-31-key-sections.txt` | same 10-K, Items 1 (business), 1A (risk factors), 3 (legal), 7 (MD&A), 8 (statements and notes), 9A (controls) | 269,544 characters, about 67k tokens |
| `earnings-release-Q4-FY2015-12-31.txt` | results release furnished 2016-01-28 on 8-K | 23,823 characters, about 6k tokens |
| `earnings-release-Q4-FY2016-12-31.txt` | results release furnished 2017-01-31 on 8-K | 24,012 characters, about 6k tokens |

Token counts are estimates (characters divided by four). A chat conversation holds roughly 150k to 200k tokens on most plans. If the two full annual reports will not fit, attach the key-sections files instead.

## What to attach for each prompt

| Prompt | Attach |
|---|---|
| 1. Working capital | `statements.xlsx` |
| 2. Earnings quality | Nothing new. Add `earnings-release-Q4-FY2015-12-31.txt` and `earnings-release-Q4-FY2016-12-31.txt` for the adjusted-earnings check |
| 3. Footnote changes | `annual-report-FY2015-12-31-key-sections.txt` and `annual-report-FY2016-12-31-key-sections.txt` |
| 4. Consistency check | Nothing new, if prompts 1 to 3 ran in the same conversation |
| 5. Red-flag report | Nothing new |

## Amendments filed in the window

- None in the window.

## How this was built

`../_build/build.py under-armour-fy2016` downloads the filings from EDGAR, parses the rendered statement pages (the R files behind each filing's "Financial Report"), and converts the annual reports and releases from HTML to text. Rerunning it reproduces the folder.
