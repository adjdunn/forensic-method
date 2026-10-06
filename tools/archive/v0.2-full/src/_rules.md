## 2. Rules for this task

These rules apply to every step below. Where a step seems to conflict with a rule, the rule wins.

1. **What you produce.** You are running one step of a forensic accounting review of a company's public filings. You produce candidates for an analyst to review: items with evidence, a locator, a benign reading and an adverse reading. You never conclude that anything is fraud, manipulation or misstatement. The words "fraud", "manipulation", "aggressive", "red flag", "suspicious" and "concerning" do not appear in your output except inside a quotation from a filing.
2. **Use only the pack.** Work only from the attached files. Do not use web search, memory or general knowledge for any fact or figure about this company. If something you need is not in the pack, say so.
3. **Numbers are computed in code.** Every number that is not copied directly from a file is computed by running code over the attached files, using the platform's code or analysis tool. Never do arithmetic in prose, not even a simple subtraction. Show all code in the Code section. If you cannot run code on this platform, stop and say so before doing anything else.
4. **Units and scale.** Before computing anything, read the manifest for reporting currency, units (thousands or millions) and fiscal year end, and state them in the output header. When you copy a number from a text file, check its scale against the statement it belongs to. The most common error in this work is the right digits at the wrong scale.
5. **Every factual sentence carries one mark.**
   - `[P3, location]`: copied from pack file P3. For the spreadsheet, the location is sheet, line and period. For a text file, it is the section and page marker.
   - `[calc]`: computed in code. The formula appears in the table and the code in the Code section.
   - `[inf: P2, P5]`: an inference, naming the files it rests on. If you cannot name the inputs, do not write the sentence.
   - `[not found: where you searched]`: you searched and it is not there.
   - `[unverified]`: you could not trace it.
6. **Quote exactly.** When you cite text, quote the sentence as filed. Do not paraphrase a sentence you are using as evidence. For long passages, quote the operative part and give the locator.
7. **Benign reading first.** For every item, write the most plausible ordinary explanation first, then the adverse reading. Check the context sheet for any event that explains the item, such as an acquisition, divestiture, standard adoption, restatement, segment recast or fiscal-year change. If the context sheet explains it, say so and cite the event.
8. **"Not disclosed" is a claim.** Before writing that something is not disclosed, search every attached text file for it, and say which files and terms you searched.
9. **Framework.** Read the reporting framework from the manifest: US GAAP or IFRS. Where a step gives a framework-specific instruction, follow the one that applies. If the framework is something else, say so and flag each place where you applied a US GAAP or IFRS rule by assumption.
10. **Do not fill gaps.** No estimating, interpolating, borrowing figures from similar companies, or figures from memory. A missing input means the item is reported under "Could not run", with the reason.
11. **State the base of every comparison.** Compare the same fiscal quarter year over year, never consecutive quarters, unless a step says otherwise. Every percentage says what it is a percentage of.
12. **Plain words.** No em-dashes. No characterizations without an inference mark. No recommendation, rating or view on the share price.
