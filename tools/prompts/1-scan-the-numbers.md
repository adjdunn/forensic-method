# 1. Scan the numbers

**Numbers track, step 1.** In a new conversation, attach the company's financial statements spreadsheet, its last two annual reports and its last two fourth-quarter results releases. Then paste this prompt.

---

Scan the attached company's financial statements for movements worth a closer look. Use the spreadsheet for the figures. Don't explain the movements yet; that comes in the next step.

**Calculate, in code, for each fiscal year, and for the latest quarter that the attached reports or releases cover, beside the same quarter a year earlier:** (the spreadsheet may run further; stop at the last quarter a document explains)

*Working capital*
- Days sales outstanding, days inventory and days payable: the period-end balance ÷ the period's revenue (or cost of sales) × days in the period.
- Growth gaps, year over year: receivables growth minus revenue growth; inventory growth minus cost-of-sales growth; payables growth minus cost-of-sales growth.
- The allowance for doubtful accounts as a percentage of gross receivables. If the spreadsheet doesn't show it, take it from the balance sheet in the annual reports.

*Earnings and cash*
- Gross margin and operating margin.
- Accruals: (net income − operating cash flow) ÷ average total assets.
- Free cash flow (operating cash flow − capital expenditures) against net income.
- The depreciation rate: depreciation ÷ average gross depreciable assets. Take depreciation and gross assets (at cost, less land and construction in progress) from the property note in the annual reports, not from the spreadsheet's cash flow line, which can change basis between years. Use that one depreciation figure for every measure that needs one. For a rental or leasing company, do this separately for the rental equipment, and count purchases net of disposal proceeds as capital spending.
- The Beneish M-score for each pair of years:
  M = −4.84 + 0.920·DSRI + 0.528·GMI + 0.404·AQI + 0.892·SGI + 0.115·DEPI − 0.172·SGAI + 4.679·TATA − 0.327·LVGI.
  If an input can't be computed, use the closest measure available or set it to 1. A score above −1.78 is a reason to look, not evidence: the model raises more than 100 false alarms for every real case.

*Revised figures*
- From the spreadsheet's Revisions sheet: the later changes to figures the company had already reported that moved income or equity.

*Levels against the industry*
- If the spreadsheet has an Industry sheet, set the company's latest-year receivables, inventory and payables as shares of sales, its margins and its capital spending against depreciation beside the industry averages there. A level well away from the industry figure is a candidate flag even if it has not moved. The averages carry no range, so say how far away the company sits and leave the judgment to the reader.

**Watch for:**
- No cost-of-sales line: use the sum of the direct cost lines that sit above selling and administrative expenses (for a rental company, direct operating costs plus depreciation of rental equipment), and name them. Use that same sum for margins, days inventory, days payable and the M-score.
- No inventory: skip the inventory measures.
- Acquisitions: a large cash outflow for acquisitions means balances can jump before a full period of revenue arrives. Note it beside any flag it could explain.
- Quarterly figures are seasonal. Compare a quarter only with the same quarter a year earlier.
- A fourth quarter worked out by subtraction can mix original and revised figures. If its column heading is marked "mixed basis", take that quarter (and the same quarter a year earlier) from the results release instead, and say you did. If the heading says only some lines are mixed basis, use the spreadsheet for the quarter and leave the shaded lines out of any measure. The spreadsheet has quarterly cash flow; the releases usually do not.

**Then pick up to five flags:** the movements most out of line with the company's own history, and the levels most out of line with the industry. For each flag, calculate two more things, then list the flags largest size first:
- **Size:** what the movement is worth in money, as a share of the latest year's pre-tax income. Use these methods every time, so the figure is the same from one run to the next:
  - a balance that outgrew its driver: the balance less what it would be at the prior year's days (days sales outstanding, days inventory or days payable). Days allow for a 52- or 53-week year; a plain ratio does not;
  - a balance that fell behind its driver (payables falling while costs rise): what it would be at the prior year's days, less the balance;
  - a margin that fell: the fall in the margin times the revenue of the period the fall was measured over (the year for a yearly fall, the quarter for a same-quarter fall);
  - a depreciation rate that fell: the charge not taken at the prior rate;
  - cash flow against earnings: net income less free cash flow;
  - a level away from the industry figure, with no movement behind it: the balance less what it would be at the industry's share of sales.
  Say which amount you used.
- **Persistence:** how many consecutive years, or same-quarter comparisons, the measure has moved the same way.

**Rules:**
- Use only the attached documents. No outside knowledge of this company or of anything that happened later.
- Do every calculation in code. Don't show the code unless asked.
- These are things to check, not findings. Don't use words like fraud, manipulation or red flag.
- If something you need is not in the documents, say so. Don't estimate.

**Reply with no introduction. Aim for one page.**
1. **A table of the measures**, with periods across the top: the fiscal years, then the latest quarter beside the same quarter a year earlier, then, if there is an Industry sheet, one column for the industry average where there is one. Leave out any row or column that would be empty. The M-score takes one row.
2. **One line** under the table: the cost line used, and any measure built on a substitute. Name the substitute, not its derivation.
3. **Flags**, numbered, two short lines each. First line: what moved, by how much, over which periods, and the one thing that might explain it (an acquisition, a new standard) if the statements show one. Second line: size as a share of pre-tax income, with the amount used, and how many consecutive periods it has run. Keep the sheet and line names in the code, available on request. No thresholds: the reader judges.
4. **Revised figures:** one line.
5. **Not calculated:** one line.
