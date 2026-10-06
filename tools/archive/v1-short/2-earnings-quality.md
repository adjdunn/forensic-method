# 2. Earnings quality

Use the same conversation and attachments as prompt 1. Then paste this prompt.

---

Test how well the attached company's earnings are backed by cash, over the years provided.

**Calculate, in code, for each year:**
- Accruals: (net income − operating cash flow) ÷ average total assets.
- Free cash flow (operating cash flow − capital expenditures) against net income.
- Capital expenditures against depreciation. For a rental or leasing company, count purchases of rental equipment net of disposal proceeds as capital spending, and say so.
- The Beneish M-score, for each pair of consecutive years:
  M = −4.84 + 0.920·DSRI + 0.528·GMI + 0.404·AQI + 0.892·SGI + 0.115·DEPI − 0.172·SGAI + 4.679·TATA − 0.327·LVGI,
  with TATA = (net income − operating cash flow) ÷ total assets. Show each of the eight inputs. If an input can't be computed (for example, there are no current-asset totals), use the closest measure available or set it to 1, and say which.

**Adjusted earnings:** if the earnings releases give adjusted figures, show the gap between reported and adjusted earnings each year. List any item called "non-recurring" or "one-time" that appears in more than one year.

**Keep the M-score in proportion.** Scores above −1.78 are a screen, not evidence: in later testing the model raised more than 100 false alarms for every real case. Say which inputs drive the score. That tells the analyst which accounts to read.

**Then pick up to three flags.**

**Rules:**
- Use only the attached documents. No outside knowledge of this company.
- Do every calculation in code. Don't show the code unless asked.
- For every flag, give the innocent explanation first, then the concerning one.
- Quote the filing exactly, with the document and page.
- If the company revised earlier figures, say which figures are on which basis.
- These are things to check, not findings. Don't use words like fraud, manipulation or red flag.
- If something you need is not in the documents, say so. Don't estimate.

**Reply in about one page:**
1. A table of the measures by year.
2. The M-score by year, with the two or three inputs that drive it.
3. A flags table: Flag | Evidence | Where to look | Innocent reading | Concerning reading.
4. One line on anything you could not calculate, and why.
