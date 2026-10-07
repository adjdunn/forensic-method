"""Recompute the figures the v2.23 chat (manual) replies rest on, from the workspace files only.

Run from anywhere:  python recompute.py
Inputs: ../workspace/statements.xlsx and the four text files beside it.
Every figure typed in from the pack text is first asserted present on its cited page.
"""
import os
import re
import sys

import openpyxl

HERE = os.path.dirname(os.path.abspath(__file__))
WS = os.path.join(HERE, "..", "workspace")

# ---------------------------------------------------------------- pack text
def load(fn):
    out, page = [], None
    with open(os.path.join(WS, fn), encoding="utf-8") as fh:
        for i, line in enumerate(fh.read().split("\n"), 1):
            m = re.match(r"^\[p\. ([^\]]+)\]", line)
            if m:
                page = m.group(1)
            out.append((i, page, line))
    return out

FY13 = load("annual-report-FY2013-12-31.txt")
FY12 = load("annual-report-FY2012-12-31.txt")
ER13 = load("earnings-release-Q4-FY2013-12-31.txt")
ER12 = load("earnings-release-Q4-FY2012-12-31.txt")

def norm(s):
    return (s.replace("’", "'").replace("‘", "'").replace("“", '"')
             .replace("”", '"').replace("‑", "-").replace("–", "-")
             .replace("\u2014", "-").replace("\xa0", " "))

def on_page(doc, page, text):
    """True if `text` occurs on the given page marker of `doc`."""
    t = norm(text).lower()
    return any(pg == str(page) and t in norm(line).lower() for _, pg, line in doc)

def assert_on_page(doc, name, page, text):
    ok = on_page(doc, page, text)
    print(f"  [{'ok' if ok else 'NOT FOUND'}] {name} p.{page}: {text!r}")
    return ok

def hits(doc, term):
    """Count of `term` (case-insensitive) per page, and the total."""
    per = {}
    for _, pg, line in doc:
        k = len(re.findall(re.escape(term), line, flags=re.I))
        if k:
            per[pg] = per.get(pg, 0) + k
    return sum(per.values()), sorted(per, key=lambda p: int(p) if p and p.isdigit() else 0)

# ---------------------------------------------------------------- workbook
wb = openpyxl.load_workbook(os.path.join(WS, "statements.xlsx"), data_only=True)

def sheet(name):
    ws = wb[name]
    rows = list(ws.iter_rows(values_only=True))
    hdr = rows[0]
    data = {}
    for r in rows[1:]:
        if r[0] is not None and r[0] not in data:
            data[r[0]] = r
    return hdr, data

def col(hdr, label):
    for i, h in enumerate(hdr):
        if h and label in str(h):
            return i
    raise KeyError(label)

def get(sheetname, line, period):
    hdr, data = sheet(sheetname)
    for key, r in data.items():
        if key.startswith(line):
            return r[col(hdr, period)]
    raise KeyError(line)

results = []
def check(label, reported, computed, tol=None, note=""):
    """Compare at the reply's rounding: tol defaults to half a unit of the last printed digit."""
    if tol is None:
        s = str(reported)
        dec = len(s.split(".")[1]) if "." in s else 0
        tol = 0.5 * 10 ** (-dec) + 1e-9
    ok = abs(float(reported) - float(computed)) <= tol
    results.append((label, reported, computed, ok))
    print(f"  [{'match' if ok else 'MISMATCH'}] {label}: reported {reported}, recomputed {computed:.4f}{(' ; ' + note) if note else ''}")
    return ok

PTI13 = 663.1  # FY2013 pre-tax income, workbook IS annual and FY2013 10-K p. 76

# ================================================================ 1. rental depreciation rate
print("\n1. Rental equipment depreciation rate (numbers-1 flag 3: 16.2, 15.3, 14.2 first reported; numbers-2: 15.2 to 14.3 revised)")
assert_on_page(FY13, "FY13 Note 8", 126, "Depreciation of revenue earning equipment | $2,407.8 | $2,145.9 | $1,912.3")
assert_on_page(FY12, "FY12 Note 8", 113, "Depreciation of revenue earning equipment | $2,165.2 | $1,921.8 | $1,747.0")
assert_on_page(FY13, "FY13 BS revised 2012 cars", 75, "Cars | 14,456.6 | 12,548.8")
cars = {y: get("BS annual", "Cars", f"{y}-12-31") for y in (2010, 2011, 2012, 2013)}
oth = {y: get("BS annual", "Other equipment", f"{y}-12-31") for y in (2010, 2011, 2012, 2013)}
gross = {y: cars[y] + oth[y] for y in cars}
gross12_rev = 12548.8 + 3240.1
avg = lambda a, b: (a + b) / 2
dep = {2011: 1921.8, 2012: 2165.2, 2013: 2407.8}      # charge before the disposal adjustment, as first reported
r11 = dep[2011] / avg(gross[2010], gross[2011]) * 100
r12 = dep[2012] / avg(gross[2011], gross[2012]) * 100
r13 = dep[2013] / avg(gross[2012], gross[2013]) * 100
check("FY2011 rate % (numbers-1)", 16.2, r11)
check("FY2012 rate % first reported (numbers-1)", 15.3, r12)
check("FY2013 rate % first-reported base (numbers-1)", 14.2, r13)
check("Average gross rental equipment FY2013 $m (numbers-1)", 16900, avg(gross[2012], gross[2013]), tol=50)
short_fr = r12 / 100 * avg(gross[2012], gross[2013]) - dep[2013]
check("Charge not taken at FY12 rate $m first reported (numbers-1)", 175, short_fr, tol=0.5)
check("Share of pre-tax % (numbers-1)", 26, short_fr / PTI13 * 100, tol=0.5)
r12_rev = 2145.9 / avg(gross[2011], gross12_rev) * 100
r13_rev = 2407.8 / avg(gross12_rev, gross[2013]) * 100
check("FY2012 rate % revised (numbers-2, report-5)", 15.2, r12_rev)
check("FY2013 rate % revised base (numbers-2, report-5)", 14.3, r13_rev)
short_rev = r12_rev / 100 * avg(gross12_rev, gross[2013]) - 2407.8
check("Charge not taken $m revised (numbers-2, report-5)", 152, short_rev, tol=0.5)
check("Share of pre-tax % revised", 23, short_rev / PTI13 * 100, tol=0.5)
check("Net rate changes $39.6m as % of the shortfall (numbers-2)", 26, 39.6 / short_rev * 100, tol=0.5)
check("$39.6m as % of the charge (numbers-2; 2,525.5 total line)", 1.6, 39.6 / 2525.5 * 100)

# ================================================================ 2. stated rate changes and disposal results as shares
print("\n2. Stated rate changes and disposal results as shares of pre-tax income (text-3, text-4, numbers-2, report-5)")
assert_on_page(FY13, "FY13 Note 8", 126, "net decreases of $44.2 million, $139.4 million and $26.7 million")
assert_on_page(FY13, "FY13 Note 8", 126, "net losses of $48.2 million, and net gains of $100.6 million and $114.9 million")
assert_on_page(FY13, "FY13 Note 8 international", 126, "net increases of $5.0 million, $8.8 million and $12.9 million")
assert_on_page(FY13, "FY13 Note 8 equipment", 126, "decrease of $0.4 million, an increase of $0.5 million, and a decrease of $4.4 million")
assert_on_page(FY13, "FY13 revised pre-tax", 84, "Income before income taxes | 450.6 | (9.2) | 441.4 | 324.3 | (18.7) | 305.6")
check("$44.2m as % of pre-tax", 6.7, 44.2 / PTI13 * 100)
check("$48.2m as % of pre-tax", 7.3, 48.2 / PTI13 * 100)
net13 = 44.2 - 5.0 + 0.4
net12 = 139.4 - 8.8 - 0.5
net11 = 26.7 - 12.9 + 4.4
check("Net rate change FY2013 $m (numbers-2)", 39.6, net13)
check("Net rate change FY2012 $m (numbers-2)", 130.1, net12)
check("Net rate change FY2011 $m (numbers-2)", 18.2, net11)
check("Net FY2013 as % of revised pre-tax (numbers-2)", 6.0, net13 / 663.1 * 100)
check("Net FY2012 as % of revised pre-tax (numbers-2)", 29.5, net12 / 441.4 * 100)
check("Net FY2011 as % of revised pre-tax (numbers-2)", 6.0, net11 / 305.6 * 100)
check("$139.4m as % of 2012 revised pre-tax (text-4)", 31.6, 139.4 / 441.4 * 100)
check("U.S. disposal swing $m (text-4 Why it matters: 100.6 gain to 48.2 loss)", 148.8, 100.6 + 48.2)
check("International rate change $5.0m as % (text-4)", 0.8, 5.0 / PTI13 * 100)
check("2012 worldwide car figure ties: 139.4 - 8.8 (text-4)", 130.6, 139.4 - 8.8)
assert_on_page(FY12, "FY12 Note 8 130.6", 113, "net decreases of $130.6 million")

# ================================================================ 3. per-vehicle depreciation
print("\n3. U.S. depreciation per vehicle per month (numbers-2, text-3, text-4)")
assert_on_page(ER13, "ER13 Table 7 U.S. depreciation", "unnumbered", "Depreciation of revenue earning equipment | 1,269.7 | 451.1 | 298.8 | 425.4 | 2,445.0 | 939.9")
assert_on_page(ER13, "ER13 Table 4 average cars", "unnumbered", "Average number of cars (Company-operated) | 472,200 | 22.4% | 468,500 | 31.2%")
assert_on_page(FY13, "FY13 p.49 average cars", 49, "Average number of cars (Company-operated) | 468,500 | 358,000 | 321,700")
assert_on_page(FY13, "FY13 p.49 leased cars", 49, "Average number of cars (Leased) | 21,500 | 1,100")
assert_on_page(FY13, "FY13 p.131 segment depreciation", 131, "U.S. car rental | $1,269.3 | $940.6 | $971.7")
cars13, cars12 = 468500, 468500 / 1.312          # numbers-2 uses the release's 31.2% growth for the 2012 base
check("2013 per car per month $ (numbers-2, release line)", 226, 1269.7e6 / cars13 / 12, tol=0.5)
check("2012 per car per month $ (numbers-2)", 219, 939.9e6 / cars12 / 12, tol=0.5)
check("Change % (numbers-2)", 3.0, (1269.7 / cars13) / (939.9 / cars12) * 100 - 100, tol=0.15)
check("2013 before disposal results $ (numbers-2)", 217, (1269.7 - 48.2) * 1e6 / cars13 / 12, tol=0.5)
check("2012 before disposal results $ (numbers-2)", 243, (939.9 + 100.6) * 1e6 / cars12 / 12, tol=0.5)
check("Change before disposal results % (numbers-2)", -10.5, ((1269.7 - 48.2) / cars13) / ((939.9 + 100.6) / cars12) * 100 - 100, tol=0.1)
check("text-3: 2012 per company-operated car $ (10-K line)", 219, 940.6e6 / 358000 / 12, tol=0.5)
check("text-3: 2013 per company-operated car $ (10-K line)", 226, 1269.3e6 / 468500 / 12, tol=0.5)
check("text-3: 2012 incl. leased $", 218, 940.6e6 / (358000 + 1100) / 12, tol=0.5)
check("text-3: 2013 incl. leased $", 216, 1269.3e6 / (468500 + 21500) / 12, tol=0.5)

# ================================================================ 4. receivables
print("\n4. Receivables (numbers-1 flag 1, numbers-2, report-5 item 4)")
assert_on_page(FY13, "FY13 BS receivables", 75, "Receivables, less allowance for doubtful accounts of $30.8 and $29.3 | 1,512.6 | 1,879.7")
assert_on_page(FY13, "FY13 p.81 fleet-sale receivables", 81, "Sales of revenue earning equipment included in receivables | 357.3 | 618.6")
assert_on_page(FY13, "FY13 p.99 pro forma revenue", 99, "10,197.4")
rec12, rec13 = get("BS annual", "Receivables", "2012-12-31"), get("BS annual", "Receivables", "2013-12-31")
rev12, rev13 = get("IS annual", "Total revenues", "2012-12-31"), get("IS annual", "Total revenues", "2013-12-31")
check("Receivables change % first reported (numbers-1)", -19.8, (rec13 / rec12 - 1) * 100)
check("Revenue growth % (numbers-1)", 19.4, (rev13 / rev12 - 1) * 100)
dso12 = rec12 / rev12 * 366
dso13 = rec13 / rev13 * 365
check("DSO FY2012 first reported, 366-day year (numbers-1)", 76.5, dso12)
check("DSO FY2013 (numbers-1)", 51.3, dso13)
sh_fr = dso12 / 365 * rev13 - rec13
check("Receivables at FY12 days less balance $m (numbers-1)", 746, sh_fr, tol=0.5)
check("Share of pre-tax % (numbers-1)", 113, sh_fr / PTI13 * 100, tol=0.5)
rec12r, rev12r = 1879.7, 9024.9
dso12r = rec12r / rev12r * 366
check("DSO FY2012 revised (numbers-2)", 76.2, dso12r)
check("Receivables change % revised (numbers-2)", -19.5, (rec13 / rec12r - 1) * 100)
sh_rev = dso12r / 365 * rev13 - rec13
check("Shortfall revised $m (numbers-2, report-5)", 737, sh_rev, tol=0.5)
check("Share of pre-tax % revised (numbers-2; the checker's 64.7% used 1,153.2 as the base)", 111, sh_rev / PTI13 * 100, tol=0.5)
check("Fleet-sale receivables fall $m (numbers-2)", 261.3, 618.6 - 357.3)
fall = rec12r - rec13
check("Total fall $m (numbers-2)", 367.1, fall)
check("Fleet share of the fall % (numbers-2)", 71, 261.3 / fall * 100, tol=0.5)
check("Fleet fall as % of opening receivables (numbers-2)", 13.9, 261.3 / rec12r * 100)
other12 = rec12r - 618.6 - 0.9      # also net of property-sale receivables (p. 81: 0.9 then 16.6)
other13 = rec13 - 357.3 - 16.6
check("Other receivables fall $m (numbers-2: ex fleet-sale and property-sale receivables)", 121.5, other12 - other13)
check("Other receivables fall % (numbers-2)", 9.6, (other12 - other13) / other12 * 100)
check("Revenue growth vs pro forma 2012 % (numbers-2)", 5.6, (rev13 / 10197.4 - 1) * 100)
check("CF receivables line FY2013 (numbers-2: $34.7m use)", 34.7, -get("CF annual", "Receivables", "2013-12-31"))
unrec = fall - 261.3
check("Unreconciled remainder $m (numbers-2 'about 110'; fall less fleet-sale receivables)", 110, unrec, tol=5, note="105.8 exact; the reply's derivation is not shown")
check("report-5: 110 as % of pre-tax", 16.6, 110 / PTI13 * 100)

# ================================================================ 5. payables
print("\n5. Payables (numbers-1 flag 2, numbers-2, report-5 Also noted)")
assert_on_page(FY13, "FY13 BS payables", 75, "Accounts payable | $967.9 | $1,003.2")
assert_on_page(FY13, "FY13 p.98 Dollar Thrifty payables", 98, "Accounts payable | (43)")
assert_on_page(FY13, "FY13 p.81 unpaid purchases", 81, "Purchases of revenue earning equipment included in accounts payable and accrued liabilities | $289.1 | $247.0")
assert_on_page(FY13, "FY13 p.81 unpaid property", 81, "Purchases of property and equipment included in accounts payable | 55.6 | 35.0")
assert_on_page(FY13, "FY13 p.80 CF payables", 80, "Accounts payable | 23.2 | 34.0")
assert_on_page(FY13, "FY13 p.64 cash flow rise", 64, "$879.9 million more cash from operating activities")
ap12, ap13 = get("BS annual", "Accounts payable", "2012-12-31"), get("BS annual", "Accounts payable", "2013-12-31")
cost12 = get("IS annual", "Direct operating", "2012-12-31") + get("IS annual", "Depreciation of revenue earning equipment and lease charges", "2012-12-31")
cost13 = get("IS annual", "Direct operating", "2013-12-31") + get("IS annual", "Depreciation of revenue earning equipment and lease charges", "2013-12-31")
check("Payables change % first reported (numbers-1)", -3.1, (ap13 / ap12 - 1) * 100)
check("Cost growth % first reported (numbers-1)", 19.2, (cost13 / cost12 - 1) * 100)
dpo12 = ap12 / cost12 * 366
dpo13 = ap13 / cost13 * 365
check("Days payable FY2012 first reported (numbers-1)", 52.7, dpo12)
check("Days payable FY2013 (numbers-1)", 42.7, dpo13)
p_sh = dpo12 / 365 * cost13 - ap13
check("Payables at FY12 days less balance $m (numbers-1)", 226, p_sh, tol=0.5)
check("Share of pre-tax % (numbers-1)", 34, p_sh / PTI13 * 100, tol=0.5)
ap12r, cost12r = 1003.2, 4806.0 + 2128.9
dpo12r = ap12r / cost12r * 366
check("Payables change % revised (numbers-2)", -3.5, (ap13 / ap12r - 1) * 100)
check("Cost growth % revised (numbers-2)", 19.4, (cost13 / cost12r - 1) * 100)
check("Days payable FY2012 revised (numbers-2)", 52.9, dpo12r)
p_sh_r = dpo12r / 365 * cost13 - ap13
check("Shortfall at FY12 days revised $m (numbers-2)", 233, p_sh_r, tol=0.5)
check("Share of pre-tax % revised (numbers-2)", 35, p_sh_r / PTI13 * 100, tol=0.5)
pf = ap12r / 10197.4 * rev13 - ap13
check("Shortfall on pro forma 2012 revenue $m (numbers-2)", 92, pf, tol=0.5)
check("Share of pre-tax % (numbers-2 '14%'; the checker's 8.0% used 1,153.2 as the base)", 14, pf / PTI13 * 100, tol=0.5)
check("Acquisition base share of the shortfall % (numbers-2, report-5 '61%')", 61, (p_sh_r - pf) / p_sh_r * 100, tol=0.5)
wc13 = 23.2 + 25.2 + 24.5
wc12 = 34.0 - 29.6 + 28.8
check("Liability working-capital lines FY2013 $m (numbers-2)", 72.9, wc13)
check("Same, FY2012 revised $m (numbers-2)", 33.2, wc12)
check("Difference as % of the $879.9m rise (numbers-2)", 4.5, (wc13 - wc12) / 879.9 * 100)
check("Balance fall $m (numbers-2)", 35.3, ap12r - ap13)
check("Unpaid fleet and property purchases rise $m (numbers-2)", 62.7, (289.1 + 55.6) - (247.0 + 35.0))
gap = 23.2 + 62.7 + (ap12r - ap13)
check("Unaccounted gap $m (numbers-2 '$121m')", 121, gap, tol=0.5)
check("Gap as % of opening balance (numbers-2)", 12, gap / ap12r * 100, tol=0.5)
check("report-5: 121 as % of pre-tax", 18.2, 121 / PTI13 * 100)

# ================================================================ 6. allowance
print("\n6. Allowance for doubtful accounts (numbers-1 table, numbers-2, text-3, text-4, report-5)")
assert_on_page(FY13, "FY13 Schedule II 2013", 158, "Year ended December 31, 2013 | $29.3 | $41.9 | $(0.1) | $(40.3) | (a) | $30.8")
assert_on_page(FY13, "FY13 Schedule II 2012 revised", 158, "Year ended December 31, 2012(b) | 20.3 | 38.3")
assert_on_page(FY13, "FY13 CF provision", 80, "Provision for losses on doubtful accounts | 45.9 | 38.3 | 28.2")
assert_on_page(FY12, "FY12 BS allowance", 72, "allowance for doubtful accounts of $25,113 and $20,282")
assert_on_page(FY12, "FY12 Schedule II 2010", 140, "Year ended December 31, 2010 | 21,268 | 19,667 | (695) | (20,532) | (a) | 19,708")
rec10, rec11 = get("BS annual", "Receivables", "2010-12-31"), get("BS annual", "Receivables", "2011-12-31")
check("Allowance % of gross FY2010 (numbers-1 1.4)", 1.4, 19.708 / (rec10 + 19.708) * 100)
check("Allowance % of gross FY2011 (numbers-1 1.2)", 1.2, 20.282 / (rec11 + 20.282) * 100)
check("Allowance % of gross FY2012 first reported (numbers-1 1.3)", 1.3, 25.113 / (rec12 + 25.113) * 100)
check("Allowance % of gross FY2012 revised (numbers-2, text-4 1.5)", 1.5, 29.3 / (rec12r + 29.3) * 100)
check("Allowance % of gross FY2013 (all replies 2.0)", 2.0, 30.8 / (rec13 + 30.8) * 100)
check("Allowance over write-offs FY2013 (text-3, text-4 0.76)", 0.76, 30.8 / 40.3)
check("Allowance over write-offs FY2012 (text-4 1.00)", 1.00, 29.3 / 29.3)
check("Bad-debt charge as % of pre-tax (text-3 6.3)", 6.3, 41.9 / PTI13 * 100)
check("Provision tie-out gap $m (text-3, report-5 4.0)", 4.0, 45.9 - 41.9)

# ================================================================ 7. adjusted earnings
print("\n7. Adjusted earnings (numbers-2, text-3, text-4, report-5)")
assert_on_page(ER13, "ER13 Table 6 adjusted pre-tax", "unnumbered", "Income before income taxes | 663.1 | 490.1 | 1,153.2 | 441.4 | 450.9 | 892.3")
assert_on_page(ER13, "ER13 Table 6 adjusted net income", "unnumbered", "$346.2 | $403.4 | $749.6 | $238.6 | $350.3 | $588.9")
assert_on_page(ER13, "ER13 p.5 restructuring", 5, "Restructuring and related charges | 98.8 | 49.1")
assert_on_page(ER13, "ER13 p.5 acquisition", 5, "Acquisition related costs | 18.5 | 163.7")
assert_on_page(ER13, "ER13 p.5 purchase accounting", 5, "Purchase accounting | 132.2 | 109.6")
assert_on_page(ER13, "ER13 p.5 debt charges", 5, "Debt-related charges | 68.4 | 83.6")
assert_on_page(ER13, "ER13 Corporate EBITDA items 2013", 3, "Total extraordinary, unusual or non-recurring items | $79.1 | $75.4 | $8.9 | $0.7 | $119.3 | $283.4")
assert_on_page(ER13, "ER13 Corporate EBITDA items 2012", 3, "$78.1 | $239.3")
assert_on_page(FY13, "FY13 p.50 restructuring", 50, "Restructuring charges | (77.0) | (38.0) | (56.4)")
assert_on_page(FY13, "FY13 p.50 restructuring related", 50, "Restructuring related charges(4) | (21.8) | (11.1) | (9.8)")
assert_on_page(FY13, "FY13 p.50 integration", 50, "Integration expenses(7) | (40.0)")
assert_on_page(FY13, "FY13 p.50 relocation", 50, "Relocation costs | (7.8)")
assert_on_page(FY13, "FY13 p.50 impairment", 50, "Impairment charges and other(10) | (44.0)")
assert_on_page(FY13, "FY13 p.57 effective rate", 57, "The effective tax rate for the year ended December 31, 2013 was 47.8%")
assert_on_page(ER13, "ER13 normalized rate", "unnumbered", "normalized income tax rate (35% for 2013 and 34% for 2012)")
assert_on_page(FY13, "FY13 p.140 cumulative restructuring", 140, "$645.4 million")
assert_on_page(FY13, "FY13 p.141 accrual", 141, "$48.4")
assert_on_page(FY13, "FY13 p.44 relocation in restructuring", 44, "$21.9 million of costs related to the relocation")
check("Gap FY2013 $m", 490.1, 1153.2 - 663.1)
check("Gap as % of reported (numbers-2 74, text-3 73.9)", 73.9, 490.1 / PTI13 * 100)
check("Gap FY2012 $m (numbers-2)", 450.9, 892.3 - 441.4)
check("Gap FY2012 as % of revised reported (numbers-2 102)", 102, 450.9 / 441.4 * 100, tol=0.5)
check("Four recurring items FY2013 as % of the gap (numbers-2 65)", 65, (98.8 + 18.5 + 132.2 + 68.4) / 490.1 * 100, tol=0.5)
check("Four recurring items FY2012 as % of the gap (numbers-2 90)", 90, (49.1 + 163.7 + 109.6 + 83.6) / 450.9 * 100, tol=0.5)
check("Restructuring plus related as % of pre-tax (text-3, report-5 14.9)", 14.9, (77.0 + 21.8) / PTI13 * 100)
check("Restructuring plus related $m", 98.8, 77.0 + 21.8)
check("New 2013 exclusions $m (text-4 131.2: integration, relocation, impairment, note conversion loss)", 131.2, 40.0 + 7.8 + 44.0 + 39.4)
check("New exclusions as % of pre-tax (text-4 19.8)", 19.8, 131.2 / PTI13 * 100)
check("Tax at 35% vs 47.8% on adjusted pre-tax $m (text-3 147.6)", 147.6, (0.478 - 0.35) * 1153.2, tol=0.5)
check("Same as % of reported pre-tax (text-3 22.3)", 22.3, (0.478 - 0.35) * 1153.2 / PTI13 * 100, tol=0.1)
check("Effective rate from the workbook %", 47.8, get("IS annual", "Provision for taxes on income", "2013-12-31") / -PTI13 * 100)
found_39_4 = any("39.4" in line for _, pg, line in FY13 if pg == "50")
print(f"  text-4's 39.4 loss on note conversion: {'on' if found_39_4 else 'not on'} FY13 p.50 (the page text-4 cites for the table); "
      f"{'on' if on_page(ER13, 5, '$39.4 million in expenses related to the loss on conversion') else 'not on'} the FY2013 release p.5 footnote (g)")

# ================================================================ 8. error corrections
print("\n8. Error corrections and revisions (numbers-1, numbers-2, text-3, text-4, report-5)")
assert_on_page(FY13, "FY13 Note 2", 83, "out of period errors totaling $46.3 million, of which $34.7 million")
assert_on_page(FY13, "FY13 Note 2 nine months", 87, "Income before income taxes | 328.3 | (7.0) | 321.3 | 612.4 | (11.6) | 600.8")
assert_on_page(FY13, "FY13 Note 2 equity", 84, "total equity from $2,507.3 million to $2,486.2 million")
assert_on_page(ER13, "ER13 Q4 pre-tax", 2, "$62.3")
assert_on_page(ER13, "ER13 $47.9 million", "unnumbered", "out of period errors totaling $47.9 million")
pti11_fr, pti11_rev = 324.3, 305.6
check("FY2011 pre-tax cut $m (numbers-1 18.7)", 18.7, pti11_fr - pti11_rev)
check("FY2011 cut as % of first reported (text-3 5.8)", 5.8, 18.7 / 324.3 * 100)
check("FY2012 pre-tax cut $m from the workbook 450.5 (numbers-1 9.1; the 10-K's 450.6 gives 9.2, PK10)", 9.1, get("IS annual", "Income before income taxes", "2012-12-31") - 441.4)
check("$46.3m as % of pre-tax (text-3, text-4, report-5 7.0)", 7.0, 46.3 / PTI13 * 100)
check("34.7 + 11.6 ties to 46.3 (text-3)", 46.3, 34.7 + 11.6)
check("Nine-month 2013 effect $m (text-3 11.6)", 11.6, 612.4 - 600.8)
check("$34.7m as % of Q4 pre-tax 62.3 (text-3 56)", 56, 34.7 / 62.3 * 100, tol=0.5)
check("Equity cut $m (numbers-1 21.1)", 21.1, 2507.3 - 2486.2)
check("Net income cut FY2011 from the workbook (numbers-1 11.9)", 11.9, get("IS annual", "Net income", "2011-12-31") - 183.8)
check("Net income cut FY2012 (numbers-1 4.5)", 4.5, get("IS annual", "Net income", "2012-12-31") - 238.6)

# ================================================================ 9. Q4 gross margin and cash against earnings
print("\n9. Q4 gross margin (numbers-1 flag 5, numbers-2, report-5) and net income against free cash flow (numbers-1 flag 4, numbers-2)")
assert_on_page(ER13, "ER13 Q4 revenue", "unnumbered", "Total revenues | $2,556.3 | $2,319.7")
assert_on_page(ER13, "ER13 Q4 direct operating", "unnumbered", "Direct operating | 1,439.3 | 1,257.7")
assert_on_page(ER13, "ER13 Q4 depreciation line", "unnumbered", "Depreciation of revenue earning equipment and lease charges | 643.0 | 550.0")
assert_on_page(ER13, "ER13 Q4 U.S. depreciation", "unnumbered", "Depreciation of revenue earning equipment | 333.4 | 102.0 | 75.7 | 109.1 | 620.2 | 245.9")
assert_on_page(ER13, "ER13 U.S. fleet growth", "unnumbered", "472,200 | 22.4%")
assert_on_page(ER13, "ER13 transaction days", "unnumbered", "32,875 | 16.1%")
assert_on_page(ER13, "ER13 FCF table working capital", "unnumbered", "Changes in assets and liabilities, net of effects of acquisitions, and other | (14.5) | 51.6 | 157.3 | (48.5)")
assert_on_page(ER13, "ER13 FCF gain", 2, "an increase of $293.6 million")
assert_on_page(ER13, "ER13 fleet financing", "unnumbered", "Net financing activity related to car rental fleet | (84.3) | 147.2 | - | 71.0 | 133.9")
q4rev12, q4rev13 = 2319.7, 2556.3
gm12 = (q4rev12 - 1257.7 - 550.0) / q4rev12 * 100
gm13 = (q4rev13 - 1439.3 - 643.0) / q4rev13 * 100
check("Q4 2012 gross margin % (numbers-1)", 22.1, gm12)
check("Q4 2013 gross margin % (numbers-1)", 18.5, gm13)
q4size = (gm12 - gm13) / 100 * q4rev13
check("Fall times Q4 revenue $m (numbers-1 90)", 90, q4size, tol=0.5)
check("Share of pre-tax % (numbers-1, report-5 14)", 14, q4size / PTI13 * 100, tol=0.5)
check("Whole-company Q4 depreciation line rise $m (numbers-2 93.0)", 93.0, 643.0 - 550.0)
check("U.S. Q4 depreciation rise as % of it (numbers-2 94)", 94, (333.4 - 245.9) / 93.0 * 100, tol=0.5)
check("Depreciation part of the margin fall $m (numbers-2 37)", 37, 643.0 - 550.0 * q4rev13 / q4rev12, tol=0.5)
check("Direct operating part $m (numbers-2 53)", 53, 1439.3 - 1257.7 * q4rev13 / q4rev12, tol=0.5)
cfo13 = get("CF annual", "Net cash provided by (used in) operating activities", "2013-12-31")
ree13 = -get("CF annual", "Revenue earning equipment expenditures", "2013-12-31") - get("CF annual", "Proceeds from disposal of revenue earning equipment", "2013-12-31")
pe13 = -get("CF annual", "Property and equipment expenditures", "2013-12-31")
fcf13 = cfo13 - ree13 - pe13
check("FCF FY2013 $m (numbers-1 242: operating cash less net fleet spending less gross property spending)", 242, fcf13, tol=0.5)
check("Net income less FCF $m (numbers-2 104.7)", 104.7, get("IS annual", "Net income", "2013-12-31") - fcf13, tol=0.05)
check("Share of pre-tax % (numbers-1, numbers-2 16)", 16, (346.2 - fcf13) / PTI13 * 100, tol=0.5)
cfo12 = get("CF annual", "Net cash provided by (used in) operating activities", "2012-12-31")
ree12 = -get("CF annual", "Revenue earning equipment expenditures", "2012-12-31") - get("CF annual", "Proceeds from disposal of revenue earning equipment", "2012-12-31")
fcf12 = cfo12 - ree12 - (-get("CF annual", "Property and equipment expenditures", "2012-12-31"))
check("FCF FY2012 first reported $m (numbers-1 -83)", -83, fcf12, tol=0.5)
check("Net fleet spending FY2012 $m (numbers-1 2,488)", 2488, ree12, tol=0.5)
check("Net fleet spending FY2013 $m (numbers-1 3,034)", 3034, ree13, tol=0.5)
fcf12r = 2709.7 - (9612.8 - 7125.1) - 297.1        # FY2013 10-K p. 80, revised 2012 column
check("FY2012 gap revised $m (numbers-2 313.7)", 313.7, 238.6 - fcf12r, tol=0.1)
check("Working-capital line improvement $m (numbers-2 205.8)", 205.8, 157.3 + 48.5)
check("As % of the $293.6m FCF gain (numbers-2 70)", 70, 205.8 / 293.6 * 100, tol=0.5)

# ================================================================ 10. text-4 statement tests and text-3 balances
print("\n10. text-4 statements table and text-3 balances")
assert_on_page(FY13, "FY13 eighteen months", 11, "our approximate average holding period for a rental car was eighteen months in the United States and thirteen months")
assert_on_page(FY12, "FY12 eighteen months", 11, "our approximate average holding period for a rental car was eighteen months in the United States and fourteen months")
assert_on_page(FY13, "FY13 holding periods table", 91, "Holding periods are as follows:")
assert_on_page(FY13, "FY13 cars range", 91, "Cars | 4 to 36 months")
assert_on_page(FY12, "FY12 useful lives table", 81, "Useful lives are as follows:")
assert_on_page(FY12, "FY12 cars range", 81, "Cars | 4 to 28 months")
assert_on_page(FY13, "FY13 maintenance sentence", 53, "vehicle maintenance costs of $9.6 million due to the expansion of our off-airport and leisure businesses, longer holding periods and the impact of recalls")
assert_on_page(FY13, "FY13 driver sentence", 126, "optimization of fleet holding periods related to the integration of Dollar Thrifty")
assert_on_page(FY13, "FY13 driver sentence MD&A", 42, "optimization of fleet holding periods related to the integration of Dollar Thrifty")
assert_on_page(FY13, "FY13 also indicative", 126, "was also indicative of the residual values experienced in the U.S.")
assert_on_page(FY12, "FY12 strong residual", 113, "was indicative of the strong residual values experienced in the U.S.")
assert_on_page(FY12, "FY12 fairly stronger", 42, "We believe the residual values have remained fairly stronger")
assert_on_page(FY13, "FY13 strategy remains flexible", 42, "this strategy remains flexible")
assert_on_page(FY12, "FY12 expect to continue to decrease (text-4 gives no 2012 page)", 41, "we expect this percentage to continue to decrease")
assert_on_page(FY12, "FY12 non-program lower rates", 41, "Non-program cars typically have lower acquisition costs and lower depreciation rates")
assert_on_page(FY13, "FY13 two to fifteen", 93, "range from two to fifteen years")
assert_on_page(FY13, "FY13 Donlen customer relationships 16", 99, "Customer relationships | 16 | $65.0")
assert_on_page(FY13, "FY13 Donlen trademark 20", 99, "Trademark | 20 | 7.0")
assert_on_page(FY13, "FY13 other intangibles 3 to 10", 91, "Other intangible assets | 3 to 10 years")
assert_on_page(FY12, "FY12 other intangibles 3 to 20", 81, "Other intangible assets | 3 to 20 years")
assert_on_page(FY13, "FY13 allowance method (text-4 cites 2012 p. 80; it is p. 81)", 90, "based on our historical experience and our judgment")
assert_on_page(FY12, "FY12 allowance method, p. 81", 81, "based on our historical experience and our judgment")
print(f"  [{'ok' if not on_page(FY12, 80, 'historical experience and our judgment') else 'present'}] FY12 p.80 does not carry the allowance sentence (text-4's 2012 page is one off)")
assert_on_page(FY13, "FY13 non-program U.S. 91/95", 42, "Percentage of non-program cars in our U.S. car rental operations | 91% | 95% | 83%")
assert_on_page(FY13, "FY13 international cars sold", 43, "64,500, 54,500 and 54,800 non-program cars")
assert_on_page(FY13, "FY13 concessions nine years", 98, "$405 million of concession agreements")
assert_on_page(FY13, "FY13 indefinite-lived total", 96, "3,350.1")
assert_on_page(FY13, "FY13 self-insured reserve", 75, "Public liability and property damage | 347.7 | 332.2")
assert_on_page(FY13, "FY13 p.70 leases and concessions", 70, "Operating leases and concession agreements(3) | 2,727.7")
assert_on_page(FY13, "FY13 p.70 purchase obligations", 70, "Purchase obligations(5) | 4,757.6")
assert_on_page(FY13, "FY13 p.104 letters of credit", 104, "standby letters of credit totaling $644.9 million")
assert_on_page(FY13, "FY13 p.80 Simply Wheelz impairment", 80, "Impairment charges and other | 40.0")
assert_on_page(FY13, "FY13 p.56 44.0", 56, "impairment charges and other of $44.0 million")
assert_on_page(FY13, "FY13 p.52 SG&A table 54.1", 52, "Selling, general and administrative | 1,022.2 | 968.1 | 54.1")
assert_on_page(FY13, "FY13 p.55 SG&A text 52.6", 55, "increased $52.6 million")
assert_on_page(FY13, "FY13 p.84 accumulated deficit 1,123.2", 84, "$1,123.2 million")
assert_on_page(FY13, "FY13 p.78 accumulated deficit 1,123.3", 78, "$(1,123.3)")
assert_on_page(FY13, "FY13 p.150 covenant", 150, "unknowingly not being met")
assert_on_page(FY13, "FY13 p.159 Oracle", 159, "implemented Oracle general ledger, accounts payable and a portion of fixed assets")
assert_on_page(FY13, "FY13 p.137 Sobel", 137, "could potentially exceed $40.0 million")
assert_on_page(FY13, "FY13 p.138 reserves", 138, "none of those reserves are material")
assert_on_page(FY13, "FY13 p.45 minor adjustments", 45, "relatively minor adjustments")
assert_on_page(FY13, "FY13 p.94 no impairment", 94, "no impairment existed")
assert_on_page(FY13, "FY13 p.50 one-time", 50, "certain one-time charges")
assert_on_page(FY13, "FY13 p.44 initiatives", 44, "Additional efficiency and cost saving initiatives are being developed")
assert_on_page(FY13, "FY13 p.140 2007 through 2013", 140, "During 2007 through 2013")
assert_on_page(FY13, "FY13 p.133 fleet receivables", 133, "a decrease in fleet receivables within our U.S. car rental segment, primarily related to the timing of purchases and sales")
assert_on_page(FY13, "FY13 p.64 timing of payments", 64, "due to the timing of our payments")
assert_on_page(FY12, "FY12 p.60 timing of payments", 60, "due to the timing of our payments")
assert_on_page(ER13, "ER13 p.2 lower than expected pricing", 2, "lower than expected pricing and higher expenses related to carrying extra fleet")
assert_on_page(ER13, "ER13 p.2 earnings growth", 2, "earnings growth and improved working capital")
assert_on_page(ER12, "ER12 p.3 strong residual values", 3, "strong residual values")
assert_on_page(FY13, "FY13 p.83 four reportable segments", 83, "reportable segments")
assert_on_page(FY13, "FY13 p.83 gross basis", 83, "on a gross basis")
assert_on_page(FY12, "FY12 p.141 controls exclusion", 141, "We have excluded from our evaluation the internal controls over financial reporting of Dollar Thrifty")
assert_on_page(FY12, "FY12 p.141 21% and 2%", 141, "21% and 2%")
assert_on_page(FY12, "FY12 p.122 mediation", 122, "the parties will again be engaging in mediation")
assert_on_page(FY13, "FY13 p.138 Ramirez", 138, "Pedro Ramirez")
check("Top of car range rise % (text-4 29)", 29, (36 - 28) / 28 * 100, tol=0.5)
check("Top of car range rise months (text-4 8)", 8, 36 - 28)
check("Concessions 405 over nine years $m a year (text-4 45.0)", 45.0, 405 / 9)
found_44_5 = [pg for _, pg, line in FY13 if "44.5" in line]
print(f"  text-4 '44.5 booked in 2013' for concession amortization: '44.5' occurs in the FY2013 10-K on pages {found_44_5 or 'none'}")
check("Self-insured reserve % of 2012 pro forma revenue (text-4 3.3)", 3.3, 332.2 / 10197.4 * 100)
check("Self-insured reserve % of 2013 revenue (text-4 3.2)", 3.2, 347.7 / rev13 * 100)
check("Equipment rate 2013: segment charge plus disposal gain over average cost (text-4 9.6)", 9.6, (298.8 + 26.2) / 3401.2 * 100)
check("Equipment rate 2012 (text-4 9.3)", 9.3, (272.1 + 13.5) / 3069.0 * 100)
check("Goodwill plus indefinite-lived intangibles $m (text-3 4,697.6)", 4697.6, get("BS annual", "Goodwill", "2013-12-31") + 3350.1)
check("Vehicle impairment 40.0 as % of pre-tax (text-3 6.0)", 6.0, 40.0 / PTI13 * 100)
check("Sobel exposure 40.0 as % (text-3 6.0)", 6.0, 40.0 / PTI13 * 100)
check("Property depreciation rate FY2013 % (numbers-1 7.9: 205.3 over average property at cost)", 7.9, 205.3 / avg(get("BS annual", "Total property and equipment, at cost", "2012-12-31"), get("BS annual", "Total property and equipment, at cost", "2013-12-31")) * 100)
check("Capital spending over depreciation FY2013 (numbers-1 1.28)", 1.28, (ree13 + pe13) / (2407.8 + 205.3))
check("Accruals % of average assets FY2013 (numbers-1 -13.5)", -13.5, (346.2 - cfo13) / avg(get("BS annual", "Total assets", "2012-12-31"), get("BS annual", "Total assets", "2013-12-31")) * 100)

# ================================================================ hit table (text-4 Part 2) and trap scan
print("\nHit table in text-4 against the pack (count, pages):")
for term, rep12, rep13 in [("holding period", "10 on 11, 42, 44, 61, 81", "15 on 11, 42, 45, 53, 66, 91, 126"),
                           ("useful li", "16 on 46, 80, 81, 83, 85, 86, 88, 89", "16 on 46, 83, 90, 93, 94, 96, 98, 99, 146"),
                           ("residual", "43", "46"), ("salvage", "none", "none"), ("average", "61", "68")]:
    n12, p12 = hits(FY12, term)
    n13, p13 = hits(FY13, term)
    print(f"  {term!r}: FY2012 {n12} on {', '.join(p12)} (reply: {rep12}); FY2013 {n13} on {', '.join(p13)} (reply: {rep13})")

print("\nTrap scan of the five replies (terms that would mark a hit):")
terms = ["21 to", "25 months", "planned holding", "24 or 30", "disposed", "affirmative", "peer", "attorney", "rolling", "spreadsheet",
         "9.3", "4 percent", "11 percent", "post-close", "audit committee", "1.72", "1.66", "1.65", "budget", "235", "17 areas",
         "material weakness", "tone at the top", "June 2014", "May 2014", "November 2014", "Estero", "penalty", "fraud", "manipulat",
         "red flag", "misstat", "suspicious", "concerning"]
for fn in ["numbers-1.txt", "numbers-2.txt", "text-3.txt", "text-4.txt", "report-5.txt"]:
    txt = open(os.path.join(HERE, "..", fn), encoding="utf-8").read()
    found = [t for t in terms if t.lower() in txt.lower()]
    print(f"  {fn}: {found or 'none'}")

n_ok = sum(1 for r in results if r[3])
print(f"\n{n_ok} of {len(results)} sub-figures match at the reply's rounding.")
for label, rep, comp, ok in results:
    if not ok:
        print(f"  not matched: {label}: reported {rep}, recomputed {comp:.4f}")
