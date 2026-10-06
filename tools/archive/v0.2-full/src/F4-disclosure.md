# F4: Disclosure deltas and consistency

## 0. Header

```
ID:        F4
Name:      Disclosure deltas and consistency
Question:  What did the company change in its disclosures from one year to the next, and do the sentences the rules attach to numbers agree with those numbers?
Runs:      After F1. Its ledger feeds F5.
Needs:     The section text files for at least two annual periods (and same-quarter interim periods where available); context-sheet.md; P1 statements workbook; earnings releases
Returns:   A section map, the substantive changes with before-and-after quotes, the consistency checks, and ledger rows. Save the CSV as ledger-F4.csv.
Checklist: D1 to D5, and the text rows A4, A8, C2, C6, C10 to C16.
```

## 1. Purpose

Two passes. The **delta pass** finds what the company changed in its filings from one year to the next, reading the sections in the order the evidence says matters most. The **consistency pass** tests sentences against numbers: a sentence the rules attach to a figure, checked against that figure. In the resolved SEC cases, the signals most clearly visible in the filings at the time were contradictions of this kind, not ratios. This step does not compute working-capital ratios (F2) or screens (F3), but it uses the workbook to test sentences.

{{RULES}}

## 3. Inputs

1. Attach and read `context-sheet.md` first. If it is not attached, say so, then run F1's method steps 1, 3 and 4 in brief before continuing, and mark the output "context sheet not attached, abbreviated check run".
2. List every section file by filing and section key. Pair each section with the same section in the prior year's filing. List every section that has no pair, because a section that appears or disappears is itself a change.
3. Work one section pair at a time. Load the two files, finish that section, then move on. Do not load all filings at once.

## 4. Method

### Part A: the delta pass (D1, D2, D4, D5)

1. **Measure each pair in code.** Split each file into sentences. For each section pair, count sentences added, removed, and changed (a changed sentence is one whose closest match in the other year is similar but not identical). Report the counts per section in the section map. Counts describe the size of a change. They do not grade it.

2. **Read the changes, in this order.** Risk factors; legal proceedings and the contingencies note; market risk; the auditor's report; critical accounting estimates; the revenue note; the receivables, inventory, payables and supplier-finance notes; the PP&E, intangibles and capitalized-cost notes; the provisions, reserves, warranty and restructuring notes; related parties, guarantees and unconsolidated entities; the definitions of non-GAAP measures in the releases; MD&A last. MD&A changes the most and has the weakest measured link to later outcomes, which is why it is read last.

3. **Classify every added, removed or changed sentence** as one of:
   - **mechanical:** explained by an event on the context sheet (cite it), a date roll-forward, or a renumbering;
   - **wording:** a change in words with no change in substance;
   - **substantive:** a change in what the company says.

   Only substantive changes go further. Quote each substantive change as before and after, with both locators.

4. **What to look for in each section.**
   - **Risk factors (D2):** new risks, removed risks, and risks whose wording hardened or softened ("may" to "has", "could adversely affect" to "adversely affected"). A removed risk can matter as much as an added one.
   - **Legal and contingencies (C10):** a matter that moves between "remote", "reasonably possible" and "probable"; an accrual that appears, grows or is reversed; a switch between "cannot estimate" and a stated range. Under IFRS, IAS 37 uses "probable" to mean more likely than not, a lower bar than US GAAP, and measures a range at its midpoint rather than its minimum; record the words the company uses. IFRS has two forms of withholding: a statement that an estimate is "not practicable" (IAS 37 paragraph 91), and omission because disclosure would "prejudice seriously" the company's position in a dispute (paragraph 92), which the standard calls extremely rare. A move into the paragraph 92 form is a stronger change than a move into paragraph 91.
   - **Auditor's report (C14):** critical audit matters (PCAOB audits) or key audit matters (Canadian and international audits) added or removed; any change in how an unchanged matter was addressed, especially a shift from testing management's assumptions to developing an independent estimate; any change of firm, opinion or emphasis paragraph. Canadian key audit matters begin with periods ending on or after 15 December 2020 (TSX) or 2022 (other listed companies); a year with none before those dates is not a change.
   - **Critical accounting estimates (C13):** US rules have required, since 2021, why each estimate is uncertain, how much it changed over a relevant period, and its sensitivity. A Canadian IFRS reporter has two places to diff: the MD&A's critical accounting estimates (Form 51-102F1 item 1.12, which asks for changes over the past two years with their quantitative effect; venture issuers are exempt) and the audited note on judgments and sources of estimation uncertainty (IAS 1 paragraphs 122 and 125). Record for each estimate whether a change amount and a sensitivity are given, and whether either was given last year and dropped this year. An item can leave the IAS 1 note for an ordinary reason: the note covers only risks of material adjustment within the next year.
   - **Revenue note (A8, C11, C12):** new or changed wording on principal or agent, when control transfers, bill-and-hold, variable consideration, practical expedients, or the disaggregation categories; any reclassification of payments to customers between revenue and expense lines.
   - **Working-capital notes (A4):** a change in the allowance method or segments; a supplier-finance or factoring programme appearing or disappearing; a change in inventory costing or reserve method.
   - **PP&E, intangibles, capitalized costs (C5, C7):** a change in stated useful lives, residual values or depreciation methods; a change in what is capitalized or when capitalization starts.
   - **Provisions and reserves (C6, C9):** new classes; releases or "adjustments" credited to income; a release described as a change in estimate; a release recorded through a different line from the original charge. IFRS: every class of provision has a rollforward with "unused amounts reversed" on its own line, and a provision may be used only for the expenditure it was created for (IAS 37 paragraph 61); amounts "used" beyond the plan's described scope are a question. Under IFRS a restructuring provision can be recognized when a detailed plan is announced, earlier than US GAAP allows.
   - **Related parties, guarantees, unconsolidated entities (D4):** a new related party, a new guarantee of another entity's obligations, a new unconsolidated entity, or an existing one described differently.
   - **Non-GAAP definitions (C2):** any change in how a measure is defined or which items it excludes, and whether prior periods were recast.
   - **Revisions (C16):** in the notes of annual and interim filings, search for revision, revised, immaterial error, previously reported, as adjusted, prior period error, correction of an error, restated. Record each hit. Under IFRS the correction disclosure appears in one year's notes only, so check every year.

5. **Same-quarter interim deltas.** Where the pack has the same fiscal quarter's interim filing for two years, repeat steps 1 to 4 for the notes only.

### Part B: the consistency pass (D3)

6. **Run every check in the table.** For each row: search for the sentence type using the search terms; if found, quote the sentence for each year; compute the number it should agree with, in code, from the workbook or the notes; then record one result: consistent, inconsistent, or cannot test (and name the missing number). Run every row even when the delta pass found no change in that sentence, because an unchanged sentence in a changed situation is exactly what this pass exists to catch.

| # | Sentence type | Search for | Check against | Inconsistent when | Where it comes from |
|---|---|---|---|---|---|
| 1 | No impairment indicators | no indicators of impairment; no events or changes in circumstances; triggering event; fair value substantially exceeds; headroom | Operating results of the segment or unit that carries goodwill, over the periods in the pack; any disclosed sale process, offer or strategic review for that unit | The sentence says no indicators while the unit's results decline over consecutive periods, or while a sale or review of the unit is disclosed elsewhere in the pack | SEC order against UPS, 2024 |
| 2 | Useful lives, holding periods, residual values | useful li; holding period; residual value; salvage; estimated life | Depreciation ÷ average gross PP&E over the same years; any ranges disclosed in each year | The stated average or life is unchanged while the disclosed range widens or depreciation per unit of gross PP&E falls; or a change is described as prospective with no disclosure of its effect | SEC order against Hertz, 2018; SEC complaint against Waste Management executives, 2002 |
| 3 | Explanations of a movement | due to; driven by; primarily as a result of; reflecting | The figure the explanation relies on, where the pack discloses it | The explanation points one way and a figure disclosed elsewhere in the pack points the other. The Hertz example: lower depreciation attributed to improved residual values in a quarter when residual values had declined | SEC order against Hertz, 2018 |
| 4 | Change orders, claims, unapproved variations | change order; unapproved; claims; under discussion; pending approval; variable consideration | The amount recognized for unapproved items, where the rules require it; the trend in contract assets | The sentence acknowledges unapproved items but gives no amount where one is required, or the amount grows while described as routine. US: ASC 910-20-50-1 and Regulation S-X Rule 5-02.3(c)(3) | SEC order against Fluor, 2023 |
| 5 | Scope of receivable sales or factoring | factor; sale of receivables; current receivables; securitiz; derecogni | Receivable maturities, amounts derecognized, and the effect on cash from operations, where disclosed | The description limits the programme (for example to current receivables) while other disclosures show longer-dated or larger transfers; or the programme is absent from the liquidity discussion while material to cash from operations | SEC order against General Electric, 2020 |
| 6 | Share of bill-and-hold or early-shipment sales | bill-and-hold; bill and hold; early buy; percent of revenue; held for customer | The quarter in which those sales fell; receivables and inventory movements in that quarter | A small annual share is disclosed for sales concentrated in one quarter, where they are a much larger share of that quarter | SEC order against Sunbeam, 2001 |
| 7 | Items labelled non-recurring, one-time or unusual | non-recurring; nonrecurring; one-time; unusual; infrequent | The same category's presence in the reconciliations of prior periods | The category appeared in two or more prior fiscal years, or in five or more of the last eight quarters. US: Item 10(e)(1)(ii)(B) of Regulation S-K prohibits smoothing such items in filings. Canada: NI 52-112 section 6(2) prohibits the label, not the adjustment, so the test is whether the recurring item is still called non-recurring, unusual or infrequent | SEC order against DXC Technology, 2023 |
| 8 | Reserve release described as a change in estimate | change in estimate; change in accounting estimate; reversal; release; favorable adjustment; unused amounts reversed | The reserve rollforward: payments against releases in the same period. IFRS: the IAS 37 paragraph 84 "unused amounts reversed" line | A release is described as a change in estimate without a matching fall in the underlying payments or claims experience | SEC order against W.R. Grace, 1999 |
| 9 | Customer or distributor concentration | largest customer; significant customer; percent of revenue; distributor; concentration of credit risk | Receivable and revenue shares by customer where disclosed | The receivables concentration differs materially from the revenue concentration for the same customer, or a large customer's terms are described differently in different notes | SEC complaint against MiMedx, 2019 |
| 10 | Liquidity sufficiency | sufficient; adequate liquidity; meet our obligations | Supplier-finance obligations, factoring and covenant disclosures elsewhere in the pack | The liquidity discussion omits a financing programme that another note shows is material to cash from operations | SEC order against General Electric, 2020; ASU 2022-04; IAS 7 amendments, 2023 |

7. **Assign priority.** An inconsistent result is P1. A rule-required amount that is absent is P1. A substantive change in the first five sections of step 2 that the context sheet does not explain is P3, or P2 if another step's evidence points at the same account in the same period and you can see it in the pack. A mechanical change is not a row.

## 5. Judgment notes

- The sentences that matter most are often the ones that did not change. A company copies a reassuring sentence forward by habit; the consistency pass exists to test it against this year's numbers.
- Most large changes in filings are bad news, but not all. In the research on filing changes, about one in seven large changes was positive and predicted positive returns. Read before you rank.
- Acquisitions, divestitures and new standards rewrite whole sections mechanically. Name the event from the context sheet before reading anything else in that section.
- Hedging words carry meaning in legal and contingency sections: "remote", "reasonably possible" and "probable" are defined terms. A move between them is a substantive change even if nothing else in the sentence changes.
- A dropped disclosure is as informative as an added one. A sensitivity given last year and absent this year needs an explanation.
- Quote exactly. The analyst must be able to find the sentence in the filing from your locator and see the same words.

## 6. Output

**Title:** Disclosure deltas and consistency: [company], [first period] to [last period]

1. **Header line.** Company, framework, filings compared.
2. **Summary.** Sections compared, substantive changes found, consistency checks run and their results, rows by priority. No conclusions.
3. **Section map.** Table: Section | Filing pair | Sentences added | Removed | Changed | Mechanical cause, if any.
4. **Substantive changes.** Grouped by section in the order of step 2. For each: before (quoted, locator), after (quoted, locator), and the checklist row it bears on.
5. **Consistency checks.** Table: # | Sentence type | Sentence as filed (per year, with locator) | Number it was checked against [calc] | Result | Reason.
6. **Ledger rows.**

{{LEDGER}}

{{CLOSE}}

## 9. Self-check before returning

- [ ] Every section in the pack appears in the section map, paired or listed as unpaired.
- [ ] Every one of the ten consistency checks has a result, including "cannot test" with the missing number named.
- [ ] Every substantive change is quoted before and after, with both locators.
- [ ] Every mechanical change cites the context-sheet event or the reason it is mechanical.
- [ ] Every number used in a consistency check was computed in code, and the code is shown.
- [ ] No quotation is paraphrased.
- [ ] No sentence concludes that a change or an inconsistency means anything beyond a candidate.
