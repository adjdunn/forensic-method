## 7. Ledger format

Every candidate this step raises becomes one ledger row. Later steps read these rows, so the format is fixed.

**Columns, in this order:** ID | Item | Period | Evidence | Locator | Benign reading | Adverse reading | Context | Resolving disclosure | Priority | Verdict

- **ID:** step, checklist row, sequence. Example: `F2-A1-03`.
- **Item:** the checklist row and a short name. Example: `A1 DSO, ending`.
- **Period:** the fiscal quarter or year, as the company labels it.
- **Evidence:** the computed value with its comparison (`Q3 FY2025 ending DSO 71.2 days against 58.4 in Q3 FY2024 [calc]`), or the sentence as filed, quoted.
- **Locator:** pack file and location, so the analyst can open it in under a minute.
- **Benign reading:** the most plausible ordinary explanation. Written first.
- **Adverse reading:** what it would mean if the ordinary explanation does not hold. Written as a possibility, never as a finding.
- **Context:** the context-sheet event that bears on this item, or "none".
- **Resolving disclosure:** the note, table or rule that would settle it, and whether that disclosure is in the pack.
- **Priority:** reading priority, meaning how strong the evidence is that this item deserves the analyst's time. It is not a measure of how serious the item would be if the adverse reading were true.
  - **P1:** a stated contradiction, where a sentence in the filing is inconsistent with a number in the filing; or a disclosure the rules require is absent.
  - **P2:** two or more independent signals point at the same account and period, and the context sheet does not explain them.
  - **P3:** a single signal the context sheet does not explain.
  - **P4:** a signal the context sheet explains. Kept so the analyst can see it was checked.
- **Verdict:** always left blank. The analyst fills it.

**When a computed item becomes a row.** Every computed item appears in the computation tables. It also becomes a ledger row when any of these holds, and you say which one:

- (a) the latest value is the most adverse in the pack's own series;
- (b) the adverse direction has held for three or more consecutive year-over-year comparisons;
- (c) a growth gap between two lines, such as receivables growth minus revenue growth, exceeds 10 percentage points in the latest period.

These triggers are this kit's convention, chosen to limit noise. They are not thresholds from the literature, and the analyst may change them. Items found by reading text always become rows.

**Deliver the rows twice.** First as a markdown table. Then as CSV in a code block, with the same columns and a header row, for the analyst to save as `ledger-F#.csv` and attach to the next step.
