# The Kraft Heinz Company: test data

US GAAP. Resolved SEC case (order September 2021): supplier cost savings recognized early, lowering cost of sales and lifting Adjusted EBITDA, Q4 2015 to 2018. Restated in 2019. The 2015 merger is in the comparatives.

**Window:** SEC filings made from 2016-01-01 to 2018-12-31. Nothing filed after 2018-12-31 is included, so the documents show only what an analyst could have read on that date.

## Files

| File | What it is | Size |
|---|---|---|
| `statements.xlsx` | Income statement, balance sheet and cash flow as the company presents them, in USD millions. Annual: 5 fiscal years, 2013-04-28 to 2017-12-30. Quarterly: 15 quarters, 2015-03-29 to 2018-09-29. As originally reported; 63 later changes listed on the Revisions sheet. An Industry sheet gives Damodaran's industry averages for the matching year | small |
| `annual-report-FY2016-12-31.txt` | 10-K for the fiscal year ended 2016-12-31, full text (122 pages; page markers are the printed page numbers) | 420,553 characters, about 105k tokens |
| `annual-report-FY2016-12-31-key-sections.txt` | same 10-K, Items 1 (business), 1A (risk factors), 3 (legal), 7 (MD&A), 8 (statements and notes), 9A (controls) | 370,535 characters, about 93k tokens |
| `annual-report-FY2017-12-30.txt` | 10-K for the fiscal year ended 2017-12-30, full text (122 pages; page markers are the printed page numbers) | 427,906 characters, about 107k tokens |
| `annual-report-FY2017-12-30-key-sections.txt` | same 10-K, Items 1 (business), 1A (risk factors), 3 (legal), 7 (MD&A), 8 (statements and notes), 9A (controls) | 375,764 characters, about 94k tokens |
| `earnings-release-Q4-FY2016-12-31.txt` | results release furnished 2017-02-15 on 8-K | 49,359 characters, about 12k tokens |
| `earnings-release-Q4-FY2017-12-30.txt` | results release furnished 2018-02-16 on 8-K | 32,554 characters, about 8k tokens |

Token counts are estimates (characters divided by four). A chat conversation holds roughly 150k to 200k tokens on most plans. If the two full annual reports will not fit, attach the key-sections files instead.

## What to attach for each prompt

| Prompt | Attach |
|---|---|
| 1. Working capital | `statements.xlsx` |
| 2. Earnings quality | Nothing new. Add `earnings-release-Q4-FY2016-12-31.txt` and `earnings-release-Q4-FY2017-12-30.txt` for the adjusted-earnings check |
| 3. Footnote changes | `annual-report-FY2016-12-31-key-sections.txt` and `annual-report-FY2017-12-30-key-sections.txt` |
| 4. Consistency check | Nothing new, if prompts 1 to 3 ran in the same conversation |
| 5. Red-flag report | Nothing new |

## Amendments filed in the window

- 10-Q/A filed 2017-11-07 for the period ended 2017-07-01
- 10-Q/A filed 2017-11-07 for the period ended 2017-04-01

## How this was built

`../_build/build.py kraft-heinz-fy2017` downloads the filings from EDGAR, parses the rendered statement pages (the R files behind each filing's "Financial Report"), and converts the annual reports and releases from HTML to text. Rerunning it reproduces the folder.
