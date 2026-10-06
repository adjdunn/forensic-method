# F1: Context and comparability

## 0. Header

```
ID:        F1
Name:      Context and comparability
Question:  What is this company's reporting basis, and what in its recent history breaks a year-over-year comparison?
Runs:      First. Its output is attached to every later step.
Needs:     P0 manifest; P1 statements workbook; the annual and quarterly text files; earnings releases; events.txt
Returns:   A context sheet. Save it as context-sheet.md and attach it to F2, F3, F4 and F5.
Checklist: Supports every row. Also raises C15, C16 and E4 directly.
```

## 1. Purpose

Every benign reading in the later steps depends on knowing what changed around the numbers: a deal, a new standard, a restatement, a recast segment. This step records those events once, with locators, so the later steps can check each candidate against them. It also checks that the statement workbook ties out, because every later ratio inherits any error in it. It does not compute forensic ratios or read the notes for signals. That is F2 to F4.

{{RULES}}

## 3. Inputs

Read the manifest first. List every file in the pack with its ID and say whether you could open it. If the statements workbook is missing or unreadable, stop. If a text file is missing, carry on and record the gap under "Could not run".

## 4. Method

Work through these in order. Each step ends with a finding or an explicit "nothing found", with the search you ran.

1. **Basis.** From the manifest, the statements' own headers and the basis-of-preparation note, record: framework, currency, units, fiscal year end, and the periods covered. Take the framework from the basis-of-preparation note, not the listing: a Canadian company that is also an SEC issuer may report under US GAAP (NI 52-107 section 3.7). For an IFRS reporter, also record whether expenses are presented by function or by nature, and whether any class of PP&E or intangibles is carried under the revaluation model. Compare the manifest with the text files. Any mismatch, such as a different fiscal year end, units or framework, goes at the top of the context sheet. Search for a change of fiscal year end and an extra week in any fiscal year.

2. **Tie-out, in code.** For every period in the workbook, test:
   - balance sheet: total assets equals total liabilities plus total equity;
   - cash flow: operating plus investing plus financing plus the exchange-rate effect equals the net change in cash, and the net change equals the change in cash on the balance sheet;
   - income statement: revenue minus cost of goods sold equals gross profit;
   - quarters to years: the four quarters of each flow line sum to the annual figure, where both exist.

   Allow a difference of one unit of the reported scale for rounding. Report every failure with the sheet, line and period. A failure does not stop the pass, but every later item that uses that cell must inherit a warning.

3. **Acquisitions, disposals and discontinued operations.** Search the notes and MD&A for: acquisition, acquired, business combination, purchase price, divest, disposal, sold, discontinued, held for sale. For each event, record the date, the consideration, the revenue and income contributed where disclosed, and which periods and lines it affects. An acquisition closed late in a quarter affects the balance sheet before the income statement catches up, so record the closing date exactly.

4. **Accounting changes.** Search for: adopted, adoption, new accounting standard, recently issued, change in accounting policy, change in accounting estimate, useful life, reclassif, recast, conformed to current presentation, segment. Record each standard adopted with its date and transition method, each voluntary policy change, each change in estimate the company discloses, each reclassification of prior periods, and each segment recast.
   - US GAAP: note in particular ASC 606 (revenue), ASC 842 (leases), ASC 326 (credit losses), ASU 2022-04 (supplier finance) and ASU 2025-06 (internal-use software) where the periods cover their adoption.
   - IFRS: note in particular IFRS 15, IFRS 16, IFRS 9, the 2023 supplier-finance amendments to IAS 7 and IFRS 7, and IFRS 18 where the periods cover their adoption. IFRS 18 applies to annual periods beginning on or after 1 January 2027 and changes the cash flow statement: non-financial companies must classify interest paid as financing and interest and dividends received as investing. It is applied retrospectively, so the first IFRS 18 report restates one comparative year, and older years in the pack stay on the old basis. Record which years sit on each side.
   - IFRS 16 and ASC 842 both took effect for periods beginning in 2019. Any comparison spanning 2018 and 2019 carries a lease-accounting break.
   - A company that says an adoption was immaterial has still broken the series. Record it anyway.

5. **Restatements and revisions.** Search for: restate, restatement, revision, revised, previously issued, immaterial error, correction of an error, non-reliance, prior period. Record each with the periods affected, the lines affected, the amounts, and whether it was a full restatement with a non-reliance filing or a revision corrected in the comparatives.
   - US GAAP: a non-reliance conclusion is a Form 8-K Item 4.02 in events.txt. A revision appears only in a note.
   - IFRS: IAS 8 corrects a material prior-period error in the comparatives of the next statements, and the disclosure need not be repeated later, so it appears in one year's notes only. Search for "prior period error", "correction of an error" and "restated".
   - Canada: there is no non-reliance form. A decision to re-file or restate with a materially different result requires a news release under NI 51-102 section 11.5; search events.txt for re-file, restate and 11.5.
   - In code: if the workbook has a `RESTATED` sheet, compare each comparative year as reprinted with the same year as originally reported in the `_A` sheets. Report every line that differs by more than one unit of scale, whether or not the company labelled it. An unlabelled difference is a finding.

6. **The auditor.** For each year: the audit firm, the tenure statement if there is one, the type of opinion, any emphasis or going-concern paragraph, and the titles of the critical audit matters (PCAOB audits) or key audit matters (Canadian and international audits). Record any change of auditor from events.txt, with the reasons given, any reportable event, and whether the former auditor's letter agrees with the company's account. Do not analyse the audit matters here. F4 reads them.
   - US: Form 8-K Item 4.01 and Regulation S-K Item 304. Reportable events concern internal control, reliance on management's representations, audit scope, and information affecting reliability.
   - Canada: NI 51-102 section 4.11. The reporting package carries letters from both the former and the new auditor and is reproduced in the next information circular. Reportable events are a disagreement, a consultation with the new auditor, or an unresolved issue.
   - Key audit matters in Canada start with periods ending on or after 15 December 2020 for TSX-listed companies and 15 December 2022 for other listed companies. Earlier years have none. The international standard has no auditor-tenure statement, so a Canadian report may not state tenure; track the firm name year by year instead.

7. **Internal control and other conditions.** Search for: material weakness, significant deficiency, remediation, not effective, going concern, substantial doubt, covenant, waiver, late filing. Record each with its period and whether it was remediated. For a Canadian company that is not an SEC issuer, material weaknesses are disclosed in the MD&A under NI 52-109 and are not attested by the auditor; record that the source is management's.

8. **The comparability map.** Build a table with the periods across the columns and these line groups down the rows: Revenue; Gross margin; Receivables and contract assets; Inventory; Payables and accruals; PP&E and intangibles; Reserves and provisions; Operating cash flow; Non-GAAP measures. In each cell, write "clean" or the event from steps 3 to 7 that breaks the year-over-year comparison for that line in that period. This map is what F2 to F4 read first.

## 5. Judgment notes

- An acquisition moves receivables, inventory and payables in the quarter it closes, and revenue only for the days owned. Days-based ratios jump in that quarter for no forensic reason.
- Standard adoptions break a series even when the company calls the effect immaterial. The later steps need to know which periods sit either side of the break.
- A revision of prior-period figures has no press release and often no mention in MD&A. It is found only by reading the notes. Treat every revision as worth recording.
- In a PCAOB audit report, tenure is printed. A tenure that restarts is a change of auditor even if no one mentions it. In Canadian and international reports, compare firm names year by year.
- Canadian companies can report under IFRS or US GAAP. Getting the framework wrong sends every later step down the wrong branch, which is why it comes from the basis-of-preparation note.
- The tie-out catches pack errors, not company errors. A failure means the workbook needs fixing before the ratios mean anything.
- This step records events. It does not judge them. A restatement is an event here; whether it matters is for the analyst.

## 6. Output

**Title:** Context sheet: [company], [first period] to [last period]

1. **Basis.** Framework, currency, units, fiscal year end, periods, and any mismatch between the manifest and the filings.
2. **Pack inventory.** Every file with its ID and whether it opened.
3. **Tie-out.** One line per test and period group: passed, or the failures with sheet, line and period.
4. **Event log.** Table: Date | Event | Type (acquisition, disposal, adoption, policy change, estimate change, reclassification, segment recast, restatement, revision, auditor, control, other) | Periods affected | Lines affected | Locator.
5. **Auditor record.** Table with years across the columns: firm, tenure, opinion, emphasis paragraphs, audit matter titles, changes.
6. **Comparability map.** The table from method step 8.
7. **Items for the ledger.** Restatements, revisions, auditor changes, material weaknesses and going-concern language also become ledger rows, using the ledger columns below, with IDs F1-C15, F1-C16 and F1-E4.

## 7. Ledger rows from this step

Use these columns for the items in output section 7: ID | Item | Period | Evidence | Locator | Benign reading | Adverse reading | Context | Resolving disclosure | Priority | Verdict. Priority: P1 for a non-reliance conclusion, an auditor disagreement or reportable event, or an unremediated material weakness; P3 for other items. Leave Verdict blank. Give the rows as a markdown table and again as CSV in a code block.

{{CLOSE}}

## 9. Self-check before returning

- [ ] Every file in the manifest appears in the pack inventory with its status.
- [ ] Every tie-out test was run in code, and the code is shown.
- [ ] Every event has a date and a locator.
- [ ] Every search in steps 3 to 7 is either reported as a hit or listed under "Looked for and not found".
- [ ] The comparability map has a cell for every line group and period, with no blanks.
- [ ] Nothing in the output judges an event. It records it.
