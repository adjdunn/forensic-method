# Turn 4: compare the two annual reports.
# (1) sentence-level comparison of the sections present in both files, to find wording
#     added, reworded or dropped;  (2) the numbers behind the side-by-side table;
# (3) the quotation check for reply-4.md.
import json, os, re, sys, difflib
import common
from common import *

A13, A12, R13, R12 = "FY2013 annual report", "FY2012 annual report", "FY2013 release", "FY2012 release"
def pct(a, b): return (a / b - 1) * 100

# ---------------------------------------------------------------- (1) sentence comparison
def section(doc, start, end):
    t = text(doc) + "\nzzzEND"; a = t.index(start); b = t.index(end, a + len(start))
    return t[a:b]
def sentences(seg):
    seg = re.sub(r"\[p\. [^\]]+\]\nHERTZ GLOBAL HOLDINGS, INC\. AND SUBSIDIARIES\n\nNOTES TO CONSOLIDATED FINANCIAL STATEMENTS \(Continued\)\n", " ", seg)
    seg = re.sub(r"\[p\. [^\]]+\]", " ", seg)
    seg = re.sub(r"\s*\n\s*", " ", seg)
    return [s.strip() for s in re.split(r"(?<=[\.\:])\s+(?=[A-Z“\"(•])", seg) if len(s.strip()) > 25]
def norm(s):
    s = s.replace("‑", "-").replace("’", "'").replace("‘", "'")
    s = re.sub(r"\$?\(?[\d,]+\.?\d*\)?%?", "#", s)
    s = re.sub(r"\b(January|February|March|April|May|June|July|August|September|October|November|December)\b", "MONTH", s)
    return re.sub(r"\s+", " ", s).lower()
SECTIONS = {
    "Note 2 policies": ("Note 2—Summary of Significant Accounting Policies", "Recently Issued Accounting Pronouncements") * 2,
    "Note 8 depreciation": ("Note 8—Depreciation of Revenue Earning Equipment and Lease Charges", "Note 9—Taxes on Income") * 2,
    "Contingencies": ("Note 12—Contingencies and Off-Balance Sheet Commitments", "Note 13—Restructuring", "Note 13—Contingencies and Off-Balance Sheet Commitments", "Note 14—Restructuring"),
    "Restructuring": ("Note 13—Restructuring", "Note 14—Financial Instruments", "Note 14—Restructuring", "Note 15—Financial Instruments"),
    "Related parties": ("Note 15—Related Party Transactions", "Note 16—Earnings Per Share", "Note 16—Related Party Transactions", "Note 17—Earnings Per Share"),
    "Segment note": ("Note 11—Segment Information", "Years ended December 31,") * 2,
    "Auditor's report": ("REPORT OF INDEPENDENT REGISTERED PUBLIC ACCOUNTING FIRM", "CONSOLIDATED BALANCE SHEETS") * 2,
    "Item 9A controls": ("ITEM 9A. Controls and Procedures", "zzzEND") * 2,
    "Note 9 taxes": ("Note 9—Taxes on Income", "Note 10—Lease and Concession Agreements") * 2,
    "Note 10 leases": ("Note 10—Lease and Concession Agreements", "Note 11—Segment Information") * 2,
    "Note 3 goodwill": ("Note 3—Goodwill and Other Intangible Assets", "Note 4—Business Combinations") * 2,
    "Note 5 debt": ("Note 5—Debt", "Note 6—Employee Retirement Benefits") * 2,
}
def compare(name, s12, e12, s13, e13, show=True):
    a = sentences(section(A12, s12, e12)); b = sentences(section(A13, s13, e13))
    na = {norm(x): x for x in a}; nb = {norm(x): x for x in b}
    only_a = [na[k] for k in na if k not in nb]; only_b = [nb[k] for k in nb if k not in na]
    res = dict(reworded=[], dropped=[], added=[]); used = set()
    for x in only_a:
        m = difflib.get_close_matches(norm(x), [norm(y) for y in only_b], n=1, cutoff=0.6)
        if m: y = nb[m[0]]; used.add(y); res["reworded"].append((x, y))
        else: res["dropped"].append(x)
    res["added"] = [y for y in only_b if y not in used]
    if show:
        print(f"{name}: FY2012 {len(a)} sentences, FY2013 {len(b)}; reworded {len(res['reworded'])}, dropped {len(res['dropped'])}, added {len(res['added'])}")
    return res
DIFF = {k: compare(k, *v) for k, v in SECTIONS.items()}
if "--diff" in sys.argv:            # full listing, long; tables (lines with " | ") left out
    for k, r in DIFF.items():
        print("\n" + "=" * 80 + "\n" + k)
        for x, y in r["reworded"]:
            if " | " not in x: print("  REWORDED\n    2012:", x[:600], "\n    2013:", y[:600])
        for x in r["dropped"]:
            if " | " not in x: print("  DROPPED 2012:", x[:600])
        for y in r["added"]:
            if " | " not in y: print("  ADDED 2013:", y[:600])

# ---------------------------------------------------------------- (2) numbers
out = {}
# balance sheet items (FY2012 report is in $ thousands)
cars13, cars12r = row(A13, "Cars", page=75); oth13, oth12r = row(A13, "Other equipment", page=75)
cars12, cars11 = [x / 1000 for x in row(A12, "Cars", page=72)]; oth12, oth11 = [x / 1000 for x in row(A12, "Other equipment", page=72)]
def unlabeled(doc, first_cell):          # a totals line with no label: "2,619.1 | 2,549.9"
    l = [x for x in text(doc).splitlines() if x.startswith(first_cell + " |")][0]
    return [float(c.replace(",", "")) for c in l.split(" | ")]
ppe13, ppe12 = unlabeled(A13, "2,619.1")              # total property and equipment at cost, FY2013 p. 75
ppe11 = unlabeled(A12, "2,549,882")[1] / 1000         # FY2012 p. 72, $ thousands
rev13, rev12r, rev11r = row(A13, "Total revenues", page=76)
pti13, pti12r, pti11r = row(A13, "Income before income taxes", page=76)
pti12_first = row(A12, "Income (loss) before income taxes", page=73)[0] / 1000

# purchases of revenue earning equipment by segment, year (FY2013 release Table 7)
buy = [-x for x in row(R13, "Revenue earning equipment expenditures", after="FLEET GROWTH", nth=1)]
proc = row(R13, "Proceeds from disposal of revenue earning equipment", after="FLEET GROWTH", nth=1)
car_buy13, car_buy12 = buy[0] + buy[1] + buy[3], buy[5] + buy[6] + buy[8]
eq_buy13, eq_buy12 = buy[2], buy[7]
avg_cars13, avg_cars12 = (cars13 + cars12r) / 2, (cars12r + cars11) / 2
avg_oth13, avg_oth12 = (oth13 + oth12r) / 2, (oth12r + oth11) / 2
seg13 = lambda lab, nth: row(A13, lab, page=131, nth=nth)
dep_us, dep_int, dep_eq, dep_oth = seg13("U.S. car rental", 2), seg13("International car rental", 2), seg13("Worldwide equipment rental", 2), seg13("All other operations", 2)
rents = row(A13, "Rents paid for vehicles leased", page=126)
car_dep13, car_dep12 = dep_us[0] + dep_int[0] + dep_oth[0] - rents[0], dep_us[1] + dep_int[1] + dep_oth[1] - rents[1]
us_gl, int_gl = (-48.2, 100.6, 114.9), (-15.2, -17.3, -16.0)          # gains (losses) on disposal, FY2013 p. 126
out["cars_holding"] = dict(
    implied_months=(avg_cars12 / car_buy12 * 12, avg_cars13 / car_buy13 * 12), change_months=avg_cars13 / car_buy13 * 12 - avg_cars12 / car_buy12 * 12,
    car_purchases=(car_buy12, car_buy13), avg_gross_cars=(avg_cars12, avg_cars13),
    car_dep_rate=(car_dep12 / avg_cars12 * 100, car_dep13 / avg_cars13 * 100),
    car_dep_rate_before_disposals=((car_dep12 + us_gl[1] + int_gl[1]) / avg_cars12 * 100, (car_dep13 + us_gl[0] + int_gl[0]) / avg_cars13 * 100),
)
out["equipment_holding"] = dict(
    dep_rate=(dep_eq[1] / avg_oth12 * 100, dep_eq[0] / avg_oth13 * 100),
    months_if_depreciated_to_zero=(avg_oth12 / dep_eq[1] * 12, avg_oth13 / dep_eq[0] * 12),
    implied_months_by_purchases=(avg_oth12 / eq_buy12 * 12, avg_oth13 / eq_buy13 * 12),
)
dpe = row(A13, "Depreciation of property and equipment", page=80)          # 205.3 172.6 158.0
out["property"] = dict(rate=(dpe[1] / ((ppe12 + ppe11) / 2) * 100, dpe[0] / ((ppe13 + ppe12) / 2) * 100),
                       implied_years=(((ppe12 + ppe11) / 2) / dpe[1], ((ppe13 + ppe12) / 2) / dpe[0]))
am = row(A13, "Amortization of other intangible assets", page=80)            # 121.5 83.9 70.0
ga13 = row(A13, "Total |", page=96, nth=0)[0]; ga12r = row(A13, "Total |", page=96, nth=2)[0]
ga12 = row(A12, "Total |", page=86, nth=0)[0]; ga11 = row(A12, "Total |", page=86, nth=2)[0]
out["intangibles"] = dict(gross=(ga11, ga12, ga12r, ga13), rate=(am[1] / ((ga12r + ga11) / 2) * 100, am[0] / ((ga13 + ga12r) / 2) * 100),
                          implied_years=(((ga12r + ga11) / 2) / am[1], ((ga13 + ga12r) / 2) / am[0]), donlen_lives=(16, 20))
disp = row(A13, "Adjustment of depreciation upon disposal", page=126)        # 37.2 (96.8) (112.2): + is a loss
proc13, proc12 = proc[4], proc[9]; us_proc13, us_proc12 = proc[0], proc[5]
out["residuals"] = dict(
    gain_pct_proceeds=(-disp[1] / proc12 * 100, -disp[0] / proc13 * 100),
    us_gain_pct_proceeds=(us_gl[1] / us_proc12 * 100, us_gl[0] / us_proc13 * 100),
    us_swing_pts=us_gl[0] / us_proc13 * 100 - us_gl[1] / us_proc12 * 100,
)
out["rate_changes"] = dict(net_2012=139.4 - 8.8, first_reported_2012=130.6, net_2011=26.7 - 12.9, first_reported_2011=13.8, net_2013=44.2 - 5.0,
                           pct_pretax=((139.4 - 8.8) / pti12_first * 100, (44.2 - 5.0) / pti13 * 100))
s13 = row(A13, "Year ended December 31, 2013", page=158); s12r = row(A13, "Year ended December 31, 2012(b)", page=158)
s12 = [x / 1000 for x in row(A12, "Year ended December 31, 2012", page=140)]
rec13, rec12r = row(A13, "Receivables, less allowance", page=75)[-2:]; rec12 = row(A12, "Receivables, less allowance", page=72)[-2] / 1000
out["allowance"] = dict(
    pct_gross=(s12[-1] / (s12[-1] + rec12) * 100, s12r[-1] / (s12r[-1] + rec12r) * 100, s13[-1] / (s13[-1] + rec13) * 100),
    restated_2012=(s12[-1], s12r[-1]), restated_pct=pct(s12r[-1], s12[-1]),
    writeoffs_pct_opening=(-s12r[2] / s12r[0] * 100, -s13[3] / s13[0] * 100), writeoffs=(-s12r[2], -s13[3]),
)
pl13, pl12 = row(A13, "Public liability and property damage", page=75)
proforma12 = row(A13, "2012 supplemental pro forma", page=99)[0]
out["public_liability"] = dict(pct_revenue=(pl12 / rev12r * 100, pl13 / rev13 * 100), pct_proforma_2012=pl12 / proforma12 * 100)
utb13 = row(A13, "Balance at December 31", page=129); utb12 = row(A12, "Balance at December 31", page=116)
utb_prior13 = row(A13, "Decrease attributable to tax positions taken during prior periods", page=129)
utb_prior12 = row(A12, "Increase (decrease) attributable to tax positions taken during prior periods", page=116)
settle13 = row(A13, "Decrease attributable to settlements with taxing authorities", page=129)
out["tax_positions"] = dict(
    dec2011=(utb12[1], utb13[2]), dec2011_change=utb13[2] - utb12[1], dec2012=(utb12[0], utb13[1]),
    prior_period_decrease_2012=(utb_prior12[0], utb_prior13[1]),
    expected_reversal_2013=6.8, actual_decreases_2013=-(utb_prior13[0] + settle13[0]),
)
out["vendor_incentives"] = dict(moved_out_of_marketing=(22.4, 25.9, 21.2), pct_of_fleet_purchases_2012=25.9 / -row(A13, "Revenue earning equipment expenditures", page=80)[1] * 100,
                                advertising_2012=(158.0, 183.9), advertising_pct_rev=(158.0 / (row(A12, "Total revenues", page=73)[0] / 1000) * 100, 183.9 / rev12r * 100, 213.1 / rev13 * 100))
mat12 = [6218.8, 1122.1, 1894.1, 267.1, 219.2, 5752.5]; mat13 = [2053.3, 5284.5, 1367.5, 366.0, 3643.5, 3587.8]
out["debt_due"] = dict(first_year=(mat12[0], mat13[0]), share=(mat12[0] / sum(mat12) * 100, mat13[0] / sum(mat13) * 100), totals=(sum(mat12), sum(mat13)),
                       short_term_other=(5718.7, 927.2))
excl12 = [109.6, 83.6, 38.0, 11.1, 0.9, 163.7, 44.0]; excl13 = [132.2, 68.4, 77.0, 21.8, 1.0, 18.5, 40.0, 7.8, 28.7, 44.0, 50.7]
new13 = [40.0, 7.8, 28.7, 44.0]
out["adjusted"] = dict(lines=(len(excl12), len(excl13)), totals=(sum(excl12), sum(excl13)), new_lines=sum(new13), new_share=sum(new13) / sum(excl13) * 100,
                       new_labels=40.0 + 7.8 + 44.0, new_labels_share=(40.0 + 7.8 + 44.0) / sum(excl13) * 100)
adj = lambda lab: row(A13, lab, page=131, nth=1)
r_us, r_int = seg13("U.S. car rental", 0), seg13("International car rental", 0)
a_us, a_int = adj("U.S. car rental"), adj("International car rental")
car12_adj = row(A12, "Car rental", page=118, nth=1)[0]; car12_rev = row(A12, "Car rental", page=118, nth=0)[0]
int_gaap13 = row(R13, "International Car Rental", after="Income (loss) before income taxes:")[2]
out["segments"] = dict(us_margin=(a_us[0] / r_us[0] * 100, a_us[1] / r_us[1] * 100), intl_margin=(a_int[0] / r_int[0] * 100, a_int[1] / r_int[1] * 100),
                       old_car_rental_margin_2012=car12_adj / car12_rev * 100, intl_gaap_pretax_2013=int_gaap13, intl_gaap_margin=int_gaap13 / r_int[0] * 100,
                       intl_disposal_losses=int_gl, intl_rate_increases=(5.0, 8.8, 12.9))
conc12_first = row(A12, "Total |", page=116)[0]; conc12_now = row(A13, "Total |", page=129)[1]
out["silent_changes"] = dict(concession_total_2012=(conc12_first, conc12_now), restructuring_cash_2012=(26.8, 36.8), pension_withdrawal=(23.2, 24.1))
out["legal"] = dict(judgment=40.0, pct_pretax=40.0 / pti13 * 100)
out["controls"] = dict(errors_total=46.3, years_touched="2010 to 2013")

def show(d, ind=0):
    for k, v in d.items():
        if isinstance(v, dict): print(" " * ind + k + ":"); show(v, ind + 2)
        elif isinstance(v, (list, tuple)): print(" " * ind + f"{k}: " + ", ".join(f"{x:,.2f}" if isinstance(x, float) else str(x) for x in v))
        else: print(" " * ind + (f"{k}: {v:,.2f}" if isinstance(v, float) else f"{k}: {v}"))
print(); show(out)

# ---------------------------------------------------------------- (3) quotation check
def check_reply4(fn="reply-4.md"):
    r = open(os.path.join(HERE, fn), encoding="utf-8").read()
    n = ok = 0; fails = []
    def test(q, doc, pages_allowed, where):
        nonlocal n, ok
        n += 1
        hits = [x.start() for x in re.finditer(re.escape(q), text(doc))]
        if not hits: fails.append(("not an exact substring", q, doc, where)); return
        pages = {page_at(doc, h) for h in hits}
        if not (set(pages_allowed) & pages): fails.append((f"page is {sorted(pages)} not {pages_allowed}", q, doc)); return
        ok += 1
    for line in r.split("\n"):
        if line.startswith("|") and not line.startswith("|---") and not line.startswith("| Statement"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            # pipes inside quotes were written as a broken bar; rebuild cells on the 5-column layout
            for ci, cell in enumerate(cells[:3]):
                for m in re.finditer(r'"([^"]+)"', cell):
                    q = m.group(1).replace("¦", "|")
                    if ci == 0:      # same words in both years: pages are in columns 2 and 3
                        test(q, A12, re.findall(r"p\. (\w+)", cells[1]), "table col1 FY2012")
                        test(q, A13, re.findall(r"p\. (\w+)", cells[2]), "table col1 FY2013")
                    else:
                        test(q, A12 if ci == 1 else A13, re.findall(r"p\. (\w+)", cell), f"table col{ci+1}")
        else:
            for m in re.finditer(r'"([^"\n]+)"\s*\(([^()]*?)\)', line):
                q, cite = m.group(1).replace("¦", "|"), m.group(2)
                doc = next((d for d in FILES if d in cite), None)
                pg = re.findall(r"p\. (\w+)", cite)
                if doc is None or not pg: n += 1; fails.append(("citation not understood", q, cite)); continue
                test(q, doc, pg, "block")
            cited = {m.group(1) for m in re.finditer(r'"([^"\n]+)"\s*\(([^()]*?)\)', line)}
            for q in re.findall(r'"([^"\n]+)"', line):
                if q not in cited and q not in ("dropped", "not present"): fails.append(("quoted string without a citation", q))
    print(f"{fn}: {n} quotation checks, {ok} pass, {len(fails)} fail")
    for f in fails: print("  FAIL:", f)
if os.path.exists(os.path.join(HERE, "reply-4.md")):
    print(); check_reply4(); print("words:", wc("reply-4.md"))
