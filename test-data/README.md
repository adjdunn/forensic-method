# Test data: five real companies

Ready-to-attach files for testing the five prompts (`../tools/prompts/`) in Claude or ChatGPT. Each folder holds what the user guide tells a new user to gather: the statements as a spreadsheet, two consecutive annual reports and the fourth-quarter results releases, cut off at a date so the files show only what an analyst could have read then.

Real company names stay in this folder and the test logs. They do not go in the presentation (see `../CLAUDE.md`).

## The companies

| Folder | Company | Framework | Filings to | Why it is here |
|---|---|---|---|---|
| [hertz-fy2013/](hertz-fy2013/README.md) | Hertz Global Holdings | US GAAP | 31 Mar 2014 | Resolved SEC case: holding periods, subrogation allowances. Has a full answer key from the first test |
| [under-armour-fy2016/](under-armour-fy2016/README.md) | Under Armour | US GAAP | 31 Mar 2017 | Resolved SEC case: pull-forwards of next-quarter orders (receivables and revenue timing) |
| [kraft-heinz-fy2017/](kraft-heinz-fy2017/README.md) | Kraft Heinz | US GAAP | 31 Dec 2018 | Resolved SEC case: supplier savings booked early (cost of sales, adjusted EBITDA). The 2015 merger sits in the comparatives |
| [home-depot-fy2025/](home-depot-fy2025/README.md) | Home Depot | US GAAP | today | No known case. Two large acquisitions (SRS, GMS). Tests whether the prompts explain acquisition jumps instead of flagging them |
| [cae-fy2026/](cae-fy2026/README.md) | CAE | IFRS (Canadian 40-F) | today | No known case. Canadian IFRS: statement of financial position, contract assets, a 2024 goodwill impairment, changed non-GAAP definitions |

Case details and sources: `../research/06-case-library.md` (cases 11, 16 and 17).

## What each folder holds

| File | Contents |
|---|---|
| `statements.xlsx` | Income statement, balance sheet and cash flow, annual (4 to 5 years) and quarterly (12 to 15 quarters; CAE annual only). The company's own line items and labels, in millions. **As originally reported**: each number comes from the first filing that reported it. The **Revisions** sheet lists every later change to a line and period, which is what prompt 4's prior-year check needs. **Sources** gives the filing and link behind each column. **Industry** gives the matching industry row from Aswath Damodaran's public tables (receivables, inventory and payables as shares of sales, margins, capital spending against depreciation), from the January update nearest the year end. Quarters derived by subtraction are shaded |
| `annual-report-<year end>.txt` | Full annual report as text. `[p. N]` marks the start of each printed page, so the prompts can cite pages |
| `annual-report-<year end>-key-sections.txt` | The parts the prompts read. For a 10-K: Items 1, 1A, 3, 7, 8 and 9A. For CAE's 40-F: the MD&A and the audited statements, without the annual information form |
| `annual-report-<year end>-chat.txt` | Hertz only so far. The key-sections file cut to what the prompts read, for a company whose two reports are too large to attach together: business pages on the company, fleet and risk management only; the prior year's own comparison out of the MD&A; debt, pension, stock compensation and financial instruments notes trimmed to their opening table or paragraphs; Schedule I out. Each cut is marked in square brackets so the model can say when something it needs is missing; page markers are the full report's. Built by `_build/chat_cut.py` |
| `earnings-release-Q4-<year end>.txt` | The fourth-quarter and full-year results release, with the adjusted-earnings reconciliations |
| `README.md` | Sizes, sources, and which file goes with which prompt |

## Will it fit in one conversation?

Rough token counts for the two key-sections files together, plus the two releases:

| Company | Key sections, both years | Releases | Fits a ~200k-token chat? |
|---|---|---|---|
| Under Armour | ~136k | ~12k | Yes |
| Home Depot | ~139k | ~10k | Yes |
| Kraft Heinz | ~189k | ~21k | No. Use a Claude Project or ChatGPT, which search large files instead of loading them whole |
| CAE | ~246k | ~35k | No. Same options as Kraft Heinz |
| Hertz | ~274k; ~180k with the `-chat` files | ~38k | Not as key sections. The `-chat` cut (6 October 2026) brings the two reports to ~180k, close to what Home Depot's chat run carried (two key-sections files, one full report and two releases, ~235k, which worked) |

Rebuilt 1 October 2026: the key-sections files now include Item 1 (the business description) and treat a heading repeated on every page ("ITEM 7 ... (Continued)") as one section. Before that fix the Hertz files held one page each of the management discussion and risk factors.

These are estimates (characters divided by four). How each platform handles files over its limit is untested; recording that is part of the test (see `../tools/TESTS.md`, "Open platform questions").

## Suggested order

1. **Under Armour.** Smallest, fits, and the receivables signal is prompt 1's core case.
2. **Home Depot.** The benign check. A good run explains the acquisition quarters rather than flagging them.
3. **Hertz.** Scores against the existing answer key (`../tests/hertz-fy2013/answer-key.md`).
4. **Kraft Heinz** and **CAE.** The size limits and the IFRS terms.

Log each run in `../tools/TESTS.md`.

## Known limits

- The workbook covers the face of the three statements only. Note detail (allowance rollforwards, inventory components, useful lives) is in the annual report text, which is where the prompts are told to look.
- A fourth quarter is worked out as the full year minus nine months. When that year's annual report changed earlier figures, the column heading is marked "[mixed basis]" and the About sheet says why; use the results release for the company's own quarter.
- Derived quarters can mix old and new presentation when a company reclassified lines mid-year. Hertz 2013 segment revenue is an example: segment quarters do not sum to the year, while total revenue does. The Revisions sheet shows each change.
- Home Depot's inline filings do not expose printed page numbers, so its page markers count pages from the start of the document.
- No Canadian filer that is on SEDAR+ only. SEDAR+ blocks automated download; to add one, save the PDFs by hand.
- Answer keys exist for Hertz only. For Under Armour and Kraft Heinz, the SEC orders in the case library say what happened; they are not yet written up as answer keys with page locators.

## Industry rows

Damodaran groups: Hertz, Transportation (the nearest bucket; there is no rental-and-leasing row); Under Armour, Apparel; Kraft Heinz, Food Processing; Home Depot, Retail (Building Supply); CAE, Aerospace/Defense. His archive files are numbered one year behind their date: `wcdata13.xls` is the January 2014 update and covers fiscal 2013. Peer sets built from FMP statements were tried and dropped, because the peers had to be hand-picked.

## Rebuilding

```bash
cd _build && python build.py
```

`python build.py <folder>` rebuilds one company. Downloads are cached in `_build/cache/` (about 60 MB, safe to delete). To add a company, add an entry to `COMPANIES` in `_build/build.py` with its SEC CIK and date window.
