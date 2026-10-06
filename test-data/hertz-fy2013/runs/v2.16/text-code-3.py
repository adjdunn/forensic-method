# Step 3 (read the footnotes), Hertz FY2013. Every number in the reply is computed here.
import re, os, openpyxl

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
R13 = os.path.join(BASE, "annual-report-FY2013-12-31-key-sections.txt")
XLS = os.path.join(BASE, "statements.xlsx")
OUT = os.path.join(BASE, "runs", "v2.16", "text-3.md")

text = open(R13, encoding="utf-8").read()

# ---- page index: text of each printed page (a page number can appear more than once) ----
pages = {}
marks = list(re.finditer(r"\[p\. (\d+)\]", text))
for i, m in enumerate(marks):
    end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
    pages.setdefault(int(m.group(1)), "")
    pages[int(m.group(1))] += text[m.end():end]


def on_page(s, p):
    return s in pages.get(p, "")


def fig(s, p):
    """Assert a figure string is printed on the cited page; return it as a float."""
    assert on_page(s, p), f"figure {s!r} not on p. {p}"
    return float(s.replace(",", "").replace("$", "").replace("(", "").replace(")", ""))


# ---- workbook figures ----
wb = openpyxl.load_workbook(XLS, data_only=True)


def row(sheet, label, col):
    ws = wb[sheet]
    hdr = [c.value for c in ws[1]]
    j = next(i for i, h in enumerate(hdr) if h and col in str(h))
    for r in ws.iter_rows(min_row=2, values_only=True):
        if r[0] and str(r[0]).startswith(label):
            return float(r[j])
    raise KeyError(label)


PTI = row("IS annual", "Income before income taxes", "2013-12-31")
cars13 = row("BS annual", "Cars", "2013-12-31")
oth13 = row("BS annual", "Other equipment", "2013-12-31")
goodwill = row("BS annual", "Goodwill", "2013-12-31")
plpd = row("BS annual", "Public liability and property damage", "2013-12-31")
cf_prov = row("CF annual", "Provision for losses on doubtful accounts", "2013-12-31")
# 2012 balances as shown in the FY2013 report (Revisions sheet, "as shown later")
rev = {}
for r in wb["Revisions"].iter_rows(min_row=2, values_only=True):
    if r[0] == "Balance sheet" and r[3] == "as at 2012-12-31" and isinstance(r[6], (int, float)):
        rev[r[1]] = float(r[6])
cars12 = rev["Cars"]
oth12 = fig("3,240.1", 75)


def pct(x):
    return 100 * x / PTI


# ---- area 3: depreciation rates and disposal results (Note 8, p. 126) ----
assert on_page("net decreases of $44.2 million", 126)
rate_cut = 44.2
us_loss = fig("$48.2", 126)
intl_loss = fig("$15.2", 126)
dep = fig("2,407.8", 126)
avg_cost = (cars13 + oth13 + cars12 + oth12) / 2
dep_rate = 100 * dep / avg_cost

# ---- area 2: reserves (Schedule II, p. 158) ----
allow = fig("$30.8", 158)
writeoff = fig("(40.3)", 158)
sched_exp = fig("$41.9", 158)
prov_gap = cf_prov - sched_exp
allow_cover = allow / writeoff
impair_cf = fig("40.0", 80)
impair_adj = fig("(44.0)", 50)

# ---- area 4: goodwill and indefinite-lived intangibles ----
indef = fig("3,350.1", 96)
gw_total = goodwill + indef

# ---- area 5: off balance sheet (Note 10, p. 130; table p. 70) ----
rents = [fig(s, 130) for s in ["$141.3", "116.9", "88.9", "66.8", "46.5", "195.7"]]
conc = [fig(s, 130) for s in ["$407.9", "310.3", "249.1", "188.9", "152.0", "685.6"]]
equip = [fig(s, 130) for s in ["$52.6", "$16.0", "$8.0", "$1.2"]]
lease_total = sum(rents) + sum(conc) + sum(equip)
assert abs(lease_total - fig("2,727.7", 70)) < 0.05

# ---- area 6: related parties ----
buyback_sponsor = fig("$467.2", 106)
assert on_page("$3.1 million for the executive officers", 147)
reloc_exec = 3.1

# ---- area 7: contingencies ----
sobel = fig("$40.0", 137)

# ---- area 8: errors (Note 2, p. 83) and controls ----
vendor = [fig("$12.9", 83), fig("$2.4", 83)]
brazil = [fig("$4.4", 83), fig("$6.2", 83), fig("$3.6", 83)]
other = [fig("$2.4", 83), fig("$3.2", 83), -fig("$0.4", 83)]
prior = sum(vendor) + sum(brazil) + sum(other)
assert abs(prior - fig("$34.7", 83)) < 0.05
ytd13 = fig("(11.6)", 87)
err_total = prior + ytd13
assert abs(err_total - fig("$46.3", 83)) < 0.05
q4_pti = fig("62.3", 149)
qsum = fig("73.7", 149) + fig("205.9", 149) + fig("321.3", 149) + q4_pti
assert abs(qsum - PTI) < 0.15

# ---- area 9: adjusted pre-tax income (p. 50) ----
adj = {k: fig(s, 50) for k, s in {
    "purchase": "(132.2)", "debt": "(68.4)", "restr": "(77.0)", "restr_rel": "(21.8)", "deriv": "(1.0)",
    "acq": "(18.5)", "integ": "(40.0)", "reloc": "(7.8)", "premium": "(28.7)", "impair": "(44.0)",
    "other": "(50.7)"}.items()}
seg_adj = fig("1,581.7", 50)
corp = fig("(428.5)", 50)
adj_total = sum(adj.values())
assert abs(seg_adj - corp - adj_total - PTI) < 0.15
adj_corp = seg_adj - corp
restr_both = adj["restr"] + adj["restr_rel"]
restr_7y = fig("$645.4", 140)
restr_avg = restr_7y / 7
assert on_page("$77.0 million, $38.0 million and $56.4 million", 44)
r3 = (77.0, 38.0, 56.4)

# ---- other tie-outs ----
assert on_page("increased $52.6 million", 55)
sga_table = fig("1,022.2", 52) - fig("968.1", 52)
assert on_page("2012 totaled $47.6 million", 56)
assert on_page("2012 totaled $47.8 million", 63)
intl12_a, intl12_b = 47.6, 47.8

reply = f"""**1. Policy profile** (latest annual report, year ended 31 December 2013; sizes are shares of 2013 pre-tax income of ${PTI:,.1f}m)

| Area | What the report says | Where it sits | Why, in a few words | Size |
|---|---|---|---|---|
| 1. Revenue recognition | "recognized over the period the revenue earning equipment is rented or leased" (p. 90) | Typical | General practice for rental; no policy given for loyalty points | Not quantified |
| 2. Reserves and allowances | "relatively minor adjustments to our recorded liability" (p. 45) | Can't tell: not enough disclosed | No roll-forward for the ${plpd:,.1f}m self-insurance reserve; ${allow:.1f}m allowance against ${writeoff:.1f}m written off | {pct(plpd):.0f}%; {pct(allow):.1f}% |
| 3. Capitalized costs and useful lives | U.S. rate changes gave "net decreases of $44.2 million" in depreciation (p. 126) | Leans aggressive | U.S. cars sold at "net losses of $48.2 million" (p. 126) the same year; depreciation was {dep_rate:.1f}% of average cost | {pct(rate_cut):.1f}% |
| 4. Impairment and goodwill | "no impairment existed" (p. 94) | Can't tell: not enough disclosed | No headroom or assumptions for ${gw_total:,.1f}m of goodwill and indefinite-lived intangibles | {pct(gw_total):.0f}% (carrying amount) |
| 5. Off the balance sheet | "a percentage of revenue with a guaranteed minimum" (p. 129) | Typical | ${lease_total:,.1f}m of lease and concession minimums disclosed by year; general practice | {pct(lease_total):.0f}% |
| 6. Related parties | "none of our outstanding debt at December 31, 2013 was with related parties" (p. 148) | Typical | Sponsors sold out in 2013; the company bought 23.2 million of their shares | {pct(buyback_sponsor):.0f}% (buy-back) |
| 7. Contingencies | a judgment "could potentially exceed $40.0 million" (p. 137) | Leans aggressive | Called not material after a ruling for the plaintiffs; above the usual 5% yardstick (general practice); accrual not given | {pct(sobel):.1f}% |
| 8. Auditor's report and controls | controls "effective" (p. 159); errors "would have been material to the fourth quarter" (p. 83) | Leans aggressive | No weakness reported beside ${err_total:.1f}m of corrected errors | {pct(err_total):.1f}% |
| 9. Adjusted measures | adds back "certain one-time charges" (p. 50) | Leans aggressive | Restructuring added back in all three years shown | {pct(adj_total):.0f}% (all add-backs) |

**2. Full write-ups**

**Useful lives and residual values: depreciation was cut while cars sold at a loss**
- **The report says:** the U.S. rate cuts were "indicative of the residual values experienced in the U.S.", yet U.S. car disposals show "net losses of $48.2 million" from "declining residual values" (Note 8, p. 126).
- **Test:** the claim does not hold for 2013: a car sold below book value was depreciated too slowly. Size: {pct(rate_cut):.1f}% of pre-tax income (${rate_cut:.1f}m of depreciation saved by the cuts); the disposal loss is {pct(us_loss):.1f}%.
- **Reading:** most likely the reporting stretched: residual values built into depreciation possibly ran ahead of the used-car market. It would be ordinary if the cuts applied only to cars moved to longer holding periods and the losses fell on other cars.
- **Read next:** rate changes and disposal results by quarter, and the first disposal results of 2014.

**Adjusted pre-tax income: "one-time" charges that arrive every year**
- **The report says:** the measure adds back "certain one-time charges" (Item 7, p. 50), while restructuring ran "During 2007 through 2013" (Item 7, p. 44).
- **Test:** the claim does not hold: restructuring was ${r3[0]:.1f}m, ${r3[1]:.1f}m and ${r3[2]:.1f}m in 2013, 2012 and 2011, and ${restr_7y:.1f}m over seven years. Size: {pct(restr_both):.1f}% of pre-tax income (${restr_both:.1f}m of restructuring and related expense added back); all add-backs are {pct(adj_total):.1f}%.
- **Reading:** most likely the reporting stretched: adjusted pre-tax income after corporate costs is {adj_corp / PTI:.2f} times the reported figure, and part of the gap recurs. It would be ordinary if the charges stop once the integration and the headquarters move finish.
- **Read next:** the restructuring note by initiative, and whether the $40 million to $45 million of further move costs (p. 65) is added back.

**Controls: errors corrected, controls still called effective**
- **The report says:** the errors "would have been material to the fourth quarter" (Note 2, p. 83), yet control over financial reporting "was effective as of December 31, 2013" (Item 9A, p. 159).
- **Test:** the figures tie: the listed items sum to ${prior:.1f}m for 2012 and earlier, and ${ytd13:.1f}m for nine months of 2013 makes ${err_total:.1f}m, or {100 * err_total / q4_pti:.0f}% of fourth-quarter pre-tax income of ${q4_pti:.1f}m. Size: {pct(err_total):.1f}% of 2013 pre-tax income, cumulative pre-tax errors.
- **Reading:** can't tell. The profile judges the choice to report no weakness; the standards allow it when each year's error is immaterial, so weak controls are not shown. Errors in three unrelated places and a debt requirement "unknowingly not met" (p. 108) possibly point the other way.
- **Read next:** how the errors were found, and whether later filings revise these periods again.

**3. Also noted**
- The cash flow statement shows a ${cf_prov:.1f}m provision for doubtful accounts (p. 80); Schedule II shows ${sched_exp:.1f}m (p. 158). The ${prov_gap:.1f}m gap possibly matches the "other" in impairment charges: ${impair_adj:.1f}m (p. 50) against ${impair_cf:.1f}m (p. 80).
- Intangible lives are given as "3 to 10 years" (p. 91) and "two to fifteen years" (p. 93), but two Donlen intangibles run 16 and 20 years (p. 99).
- Selling and administrative expense "increased $52.6 million" in the discussion (p. 55); the expense table shows ${sga_table:.1f}m (p. 52).
- Vendor incentives had been booked "as a reduction of marketing expenses" (p. 83) and not against the cost of cars; this is the largest corrected error.

**4. Not in the documents:** critical audit matters (the auditor's report has none), amounts earned but not yet billed, receivables sold or factored, supplier finance, and the proxy statement's related-party detail.
"""

# ---- verify every quotation is an exact substring of the report on the cited page ----
checks = {
    "recognized over the period the revenue earning equipment is rented or leased": 90,
    "relatively minor adjustments to our recorded liability": 45,
    "net decreases of $44.2 million": 126,
    "net losses of $48.2 million": 126,
    "no impairment existed": 94,
    "a percentage of revenue with a guaranteed minimum": 129,
    "none of our outstanding debt at December 31, 2013 was with related parties": 148,
    "could potentially exceed $40.0 million": 137,
    "effective": 159,
    "would have been material to the fourth quarter": 83,
    "certain one-time charges": 50,
    "indicative of the residual values experienced in the U.S.": 126,
    "declining residual values": 126,
    "one-time": 50,
    "During 2007 through 2013": 44,
    "was effective as of December 31, 2013": 159,
    "unknowingly not met": 108,
    "other": 50,
    "3 to 10 years": 91,
    "two to fifteen years": 93,
    "increased $52.6 million": 55,
    "as a reduction of marketing expenses": 83,
}
quoted = re.findall(r'"([^"]+)"', reply)
missing = [q for q in quoted if q not in checks]
fails = [(q, p) for q, p in checks.items() if not on_page(q, p)]
# facts cited by page without quotation marks
assert on_page("$40 million to $45 million", 65)
assert on_page("16 | $65.0", 99) and on_page("20 | 7.0", 99)
assert on_page("45.9", 80)

if __name__ == "__main__":
    print("quotations in reply:", len(quoted), "| distinct:", len(set(quoted)),
          "| not in check list:", missing, "| failed:", fails)
    print("words:", len(re.findall(r"\S+", reply)))
    for k in ["PTI", "dep_rate", "avg_cost", "allow_cover", "prov_gap", "gw_total", "lease_total", "prior",
              "err_total", "qsum", "adj_total", "adj_corp", "restr_both", "restr_avg", "sga_table"]:
        print(k, round(globals()[k], 3))
    if not fails and not missing:
        with open(OUT, "w", encoding="utf-8") as f:
            f.write(reply)
        print("saved", OUT)
