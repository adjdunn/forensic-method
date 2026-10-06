# F5: The ledger

## 0. Header

```
ID:        F5
Name:      The ledger
Question:  Across everything the earlier steps raised, which items share a cause, which deserve the analyst's reading time first, and what should the analyst read to settle each?
Runs:      After F1 to F4. Stops for the analyst's verdicts. F6 runs on the verdicted ledger.
Needs:     ledger-F1.csv to ledger-F4.csv (or the ledger tables pasted from each step); context-sheet.md; earnings releases; proxy or circular; consensus.csv if the analyst supplied one
Returns:   A reading plan, a thread table, and the merged ledger with an empty Verdict column. Save the CSV as ledger-merged.csv.
Checklist: E1 to E6, and the merge of all rows.
```

## 1. Purpose

The earlier steps each see one part of the accounts. The same underlying event often shows up in several of them: a receivables build in F2, a high DSRI in F3, and a new bill-and-hold sentence in F4 may be one story. This step joins them into threads, adds the context items that need the whole picture, ranks the threads by strength of evidence, and tells the analyst what to read first and where. It then stops. It does not decide what anything means.

{{RULES}}

## 3. Inputs

1. Read the context sheet and every ledger file attached. List each file and its row count. If a step's ledger is missing, say which checklist rows are therefore absent and continue.
2. Check each row has every column, a unique ID, a locator and both readings. List any malformed row under "Could not run" and exclude it.

## 4. Method

1. **Context rows (E1 to E6).** Where the inputs exist:
   - **E1, consensus:** from consensus.csv, for each quarter, reported revenue and EPS against consensus; the length of any run of meets or narrow beats (within 1 percent of consensus). Label every consensus figure Tier 5 with its source. If consensus.csv is absent, record E1 under "Could not run".
   - **E2, guidance:** from the releases, each guidance range against the one before it and against the result that followed. For a raised full-year range, subtract the year-to-date actual to get the implied remainder, and compare that with the remainder implied by the prior range.
   - **E3, compensation:** from the proxy or circular, the metrics that drive annual and long-term incentive pay, and whether any is an adjusted measure or a working-capital or cash metric the earlier steps flagged.
   - **E4, turnover and controls:** from the context sheet. For a Canadian company that is not an SEC issuer, a material weakness is management's disclosure in the MD&A, without an auditor's attestation; say so.
   - **E5, growth against the industry:** record under "Could not run", because the pack carries no peer data, unless the analyst supplied it.
   - **E6, differential disclosure:** for each fiscal year, compare the headline figures and descriptions in the fourth-quarter release with the annual filing. Record any figure or description that differs.

2. **Build threads.** Group rows that bear on the same account and the same period, or on the same underlying disclosure. Give each thread an ID (T1, T2 ...), a one-line name that describes the observation without characterizing it (for example "Q4 FY2025 receivables build with new early-shipment wording"), and the list of member row IDs. A row can belong to only one thread. A row that joins nothing is a thread of one.

3. **Localize each thread.** Name the account that carries it: revenue recognition and receivables; contract assets; inventory and cost of sales; capitalized costs and intangibles; useful lives and depreciation; reserves and provisions; payables and supplier finance; cash-flow classification; adjusted measures; disclosure only. Name the resolving disclosure: the specific note, table or rule that would settle it, and whether it is in the pack.

4. **Rank.** A thread takes the highest priority of its members. A thread whose members come from two or more different steps, and which the context sheet does not explain, rises to at least P2. Within a priority, rank the most recent period first.

5. **Write the reading plan.** For each thread in rank order: what to read, in which file, at which locator, and the question the reading should answer. The question is framed so either reading of the thread could be confirmed. Example: "Read the revenue note, P14, p. 62: is the early-shipment arrangement at the customer's request, with the goods segregated?"

6. **Stop.** Present the merged ledger with the Verdict column empty. Below it, give the analyst these verdict options: **Explained** (the benign reading holds), **Open** (needs more than the pack contains), **Of concern** (the adverse reading is supported by the evidence cited), **Dismissed** (the row is wrong, with the reason). Ask the analyst to add a verdict and a short note to every thread, then attach the verdicted ledger to F6.

## 5. Judgment notes

- A thread made of rows from different steps is stronger than a thread of the same kind of row repeated. Three ratios on one account are one signal seen three ways; a ratio, a text change and a failed consistency check are three.
- A thread explained by the context sheet stays in the ledger. The analyst needs to see that it was checked.
- The reading plan is the most useful thing this step produces. An analyst with a limited hour should be able to take the first five lines and know exactly which pages to open.
- Consensus and guidance comparisons describe expectations, not the company's accounts. Label them as such.

## 6. Output

**Title:** Ledger: [company], [first period] to [last period]

1. **Header line.** Company, framework, the ledgers merged and their row counts.
2. **Summary.** Threads by priority; rows merged; rows excluded as malformed; context rows run and not run.
3. **Reading plan.** Numbered, in rank order.
4. **Thread table.** Thread ID | Name | Account | Members | Priority | Resolving disclosure | In pack?
5. **Context rows.** The E1 to E6 results, with their computations.
6. **Merged ledger.** Every row, with a Thread column added after ID, Verdict empty, as a markdown table and as CSV.
7. **For the analyst.** The verdict options and the instruction in method step 6.

{{LEDGER}}

{{CLOSE}}

## 9. Self-check before returning

- [ ] Every input row appears in the merged ledger or in the malformed list.
- [ ] Every thread has an account and a resolving disclosure.
- [ ] Thread names describe observations and contain no characterization.
- [ ] Every reading-plan line names a file, a locator and a question.
- [ ] The Verdict column is empty.
- [ ] Every consensus figure is labelled Tier 5 with its source.
