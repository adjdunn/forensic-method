# 1. Working capital

In a new conversation, attach the company's financial statements spreadsheet and its last two annual reports. Then paste this prompt.

---

Analyze the attached company's receivables, inventory and payables.

**Calculate, in code, for each fiscal year:**
- Days sales outstanding: year-end receivables ÷ revenue × days in the year.
- Days inventory: year-end inventory ÷ cost of sales × days in the year.
- Days payable: year-end payables ÷ cost of sales × days in the year.
- Growth gaps, year over year: receivables growth minus revenue growth; inventory growth minus cost-of-sales growth; payables growth minus cost-of-sales growth.
- Every reserve netted against receivables: the allowance for doubtful accounts, and any reserves for returns, markdowns, discounts or rebates. Show each as a percentage of gross receivables (net receivables plus these reserves) and of revenue.

**Quarters:** calculate the days and growth gaps for every quarter that has a year-earlier quarter in the documents. Use the quarter's own revenue or cost of sales and the days in the quarter. Quarterly days are seasonal: compare them with the same quarter a year earlier, never with the annual figures.

**Where the numbers come from:** take statement figures from the spreadsheet if one is attached, otherwise from the filings. Take the reserves, the make-up of receivables and any acquisitions from the notes in the annual reports.

**Watch for:**
- No cost-of-sales line: use the closest cost line and say which one.
- Receivables that are not from customers (amounts due from manufacturers, tax refunds, insurance): separate them if the notes allow, and compute days sales outstanding on customer receivables.
- Acquisitions: they raise balances before a full period of revenue arrives. Check the notes before treating a jump as unusual.

**Then pick the three flags that matter most:** the movements in receivables, inventory, payables or the reserves most out of line with the company's own history. For each, find what the company says about it in the annual reports and set that beside the numbers.

**Rules:**
- Use only the attached documents. No outside knowledge of this company.
- Do every calculation in code. Don't show the code unless asked.
- For every flag, give the innocent explanation first, then the concerning one.
- Where the evidence is text, quote the annual report exactly, with the document and page. Where it is a figure from the spreadsheet, name the sheet and the line.
- If the company revised earlier figures, say which figures are on which basis.
- These are things to check, not findings. Don't use words like fraud, manipulation or red flag.
- If something you need is not in the documents, say so. Don't estimate.

**Reply with no introduction. Aim for one page; go longer only when leaving something out would hide a movement that matters.**
1. **A chart**, drawn in code: three panels side by side, for receivables, inventory and payables. In each, plot by quarter the year-over-year growth of the balance against the year-over-year growth of revenue (for receivables) or cost of sales (for inventory and payables). Two labelled lines per panel, plain titles, no commentary on the chart. If there are no quarters, use fiscal years.
2. **A table of the measures**, with periods across the top: the fiscal years, then the latest quarter beside the same quarter a year earlier. Leave out any row or column that would be empty.
3. **Up to three short bullets on basis:** revised figures, acquisitions, how gross receivables was defined, or a substitute cost line. Skip any that don't apply.
4. **A flags table:** Flag | Evidence | Where to look | Innocent reading | Concerning reading. At most 40 words in a cell.
5. **Also out of line:** one line each for any other movement that did not make the top three, in these accounts or outside them.
6. **Not calculated:** one line on anything you could not calculate, and why.
