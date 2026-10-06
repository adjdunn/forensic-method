# Hertz Global Holdings, Inc.: test data

US GAAP. Resolved SEC case (order December 2018): subrogation allowances, undisclosed extension of fleet holding periods, reaffirmed guidance. Restated in 2015. EDGAR now lists this filer as Herc Holdings (the old Hertz Global Holdings renamed after the 2016 spin-off); the filings are Hertz's.

**Answer key:** [../../tests/hertz-fy2013/answer-key.md](../../tests/hertz-fy2013/answer-key.md)

**Window:** SEC filings made from 2012-01-01 to 2014-03-31. Nothing filed after 2014-03-31 is included, so the documents show only what an analyst could have read on that date.

## Files

| File | What it is | Size |
|---|---|---|
| `statements.xlsx` | Income statement, balance sheet and cash flow as the company presents them, in USD millions. Annual: 5 fiscal years, 2009-12-31 to 2013-12-31. Quarterly: 12 quarters, 2011-03-31 to 2013-12-31. As originally reported; 111 later changes listed on the Revisions sheet. An Industry sheet gives Damodaran's industry averages for the matching year | small |
| `annual-report-FY2012-12-31.txt` | 10-K for the fiscal year ended 2012-12-31, full text (159 pages; page markers are the printed page numbers) | 619,176 characters, about 155k tokens |
| `annual-report-FY2012-12-31-key-sections.txt` | same 10-K, Items 1 (business), 1A (risk factors), 3 (legal), 7 (MD&A), 8 (statements and notes), 9A (controls) | 518,899 characters, about 130k tokens |
| `annual-report-FY2013-12-31.txt` | 10-K for the fiscal year ended 2013-12-31, full text (177 pages; page markers are the printed page numbers) | 671,051 characters, about 168k tokens |
| `annual-report-FY2013-12-31-key-sections.txt` | same 10-K, Items 1 (business), 1A (risk factors), 3 (legal), 7 (MD&A), 8 (statements and notes), 9A (controls) | 563,000 characters, about 141k tokens |
| `annual-report-FY2012-12-31-chat.txt` | **Attach this one to a chat.** The key-sections file cut to what the prompts read: business pages on the company, segments, fleet and risk management only; the 2011-with-2010 comparison out of the MD&A; the debt, pension, stock compensation and financial instruments notes trimmed to their opening table or paragraphs; Schedule I out, Schedule II kept. Every cut is marked in square brackets; page markers unchanged. Built by `../_build/chat_cut.py` | 345,466 characters, about 86k tokens |
| `annual-report-FY2013-12-31-chat.txt` | Same cut of the FY2013 10-K | 373,955 characters, about 93k tokens |
| `earnings-release-Q4-FY2012-12-31.txt` | results release furnished 2013-02-25 on 8-K | 71,721 characters, about 18k tokens |
| `earnings-release-Q4-FY2013-12-31.txt` | results release furnished 2014-03-18 on 8-K | 79,366 characters, about 20k tokens |

Token counts are estimates (characters divided by four). A chat conversation holds roughly 150k to 200k tokens on most plans. If the two full annual reports will not fit, attach the key-sections files instead.

## What to attach for each prompt

| Prompt | Attach |
|---|---|
| 1. Working capital | `statements.xlsx` |
| 2. Earnings quality | Nothing new. Add `earnings-release-Q4-FY2012-12-31.txt` and `earnings-release-Q4-FY2013-12-31.txt` for the adjusted-earnings check |
| 3. Footnote changes | `annual-report-FY2012-12-31-key-sections.txt` and `annual-report-FY2013-12-31-key-sections.txt` |
| 4. Consistency check | Nothing new, if prompts 1 to 3 ran in the same conversation |
| 5. Red-flag report | Nothing new |

## Amendments filed in the window

- 10-K/A filed 2014-03-20 for the period ended 2013-12-31

## How this was built

`../_build/build.py hertz-fy2013` downloads the filings from EDGAR, parses the rendered statement pages (the R files behind each filing's "Financial Report"), and converts the annual reports and releases from HTML to text. Rerunning it reproduces the folder.
