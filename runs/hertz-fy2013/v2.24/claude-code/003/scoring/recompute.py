"""Recompute the figures the v2.24 run 003 replies rest on, from the pack the run saw.

Run from the repository root:  python3 -I runs/hertz-fy2013/v2.24/claude-code/003/scoring/recompute.py

Sources: the workbook (statements.xlsx, first-reported figures) and the four text files in the
run's workspace. Every figure typed in from a text file is asserted present on its cited page
before it is used, so a wrong locator fails the script. Ten measures, each with sub-figures;
the last block prints a match count against the values the replies give.
"""
import re
import sys
import openpyxl

WS = "runs/hertz-fy2013/v2.24/claude-code/003/workspace/"
FILES = {
    "AR12": "annual-report-FY2012-12-31.txt",
    "AR13": "annual-report-FY2013-12-31.txt",
    "ER12": "earnings-release-Q4-FY2012-12-31.txt",
    "ER13": "earnings-release-Q4-FY2013-12-31.txt",
}

# ---------------------------------------------------------------- pack text by page
PAGES = {}
for key, name in FILES.items():
    txt = open(WS + name, encoding="utf-8", errors="replace").read()
    parts = re.split(r"\[p\. ([^\]]+)\]", txt)
    PAGES[key] = [(parts[i], re.sub(r"\s+", " ", parts[i + 1])) for i in range(1, len(parts), 2)]


def onpage(doc, page, text):
    """Assert that `text` sits on the cited page of `doc`; return True."""
    hits = [t for lab, t in PAGES[doc] if lab == str(page) and text in t]
    assert hits, f"{text!r} not on {doc} p.{page}"
    return True


def num(doc, page, label, col=0, unnumbered_ok=False):
    """Pull the col-th number from the first table line on `page` that starts with `label`."""
    for lab, t in PAGES[doc]:
        if lab != str(page):
            continue
        m = re.search(re.escape(label) + r"\s*\|([^\n]*)", t)
        if m:
            cells = [c.strip() for c in m.group(1).split("|")]
            vals = []
            for c in cells:
                c2 = c.replace("$", "").replace(",", "").replace("(", "-").replace(")", "")
                try:
                    vals.append(float(c2))
                except ValueError:
                    pass
            return vals[col]
    raise AssertionError(f"{label!r} not found on {doc} p.{page}")


# ---------------------------------------------------------------- workbook
wb = openpyxl.load_workbook(WS + "statements.xlsx", data_only=True)


def sheet_rows(name):
    ws = wb[name]
    rows = {}
    for row in ws.iter_rows(values_only=True):
        if row and isinstance(row[0], str):
            rows[row[0].strip()] = list(row[1:])
    return rows


IS = sheet_rows("IS annual")      # cols: FY2009, FY2010, FY2011, FY2012, FY2013
BS = sheet_rows("BS annual")      # cols: FY2010, FY2011, FY2012, FY2013
CF = sheet_rows("CF annual")      # cols: FY2009 .. FY2013
BSQ = sheet_rows("BS quarterly")  # cols: Q4 2011, Q1 2012 .. Q4 2013
IND = {r[0]: r[1] for r in wb["Industry"].iter_rows(values_only=True) if r and isinstance(r[1], (int, float))}

rev = {y: IS["Total revenues"][i] for i, y in enumerate([2009, 2010, 2011, 2012, 2013])}
do = {y: IS["Direct operating"][i] for i, y in enumerate([2009, 2010, 2011, 2012, 2013])}
dep_lc = {y: IS["Depreciation of revenue earning equipment and lease charges"][i] for i, y in enumerate([2009, 2010, 2011, 2012, 2013])}
sga = {y: IS["Selling, general and administrative"][i] for i, y in enumerate([2009, 2010, 2011, 2012, 2013])}
pti = {y: IS["Income before income taxes"][i] for i, y in enumerate([2009, 2010, 2011, 2012, 2013])}
int_exp = IS["Interest expense"][4]
int_inc = IS["Interest income"][4]
cos = {y: do[y] + dep_lc[y] for y in do}

recv = {y: BS["Receivables, less allowance for doubtful accounts of $30.8 and $29.3"][i] for i, y in enumerate([2010, 2011, 2012, 2013])}
ap = {y: BS["Accounts payable"][i] for i, y in enumerate([2010, 2011, 2012, 2013])}
cars = {y: BS["Cars"][i] for i, y in enumerate([2010, 2011, 2012, 2013])}
cars_ad = {y: -BS["Less accumulated depreciation"][i] for i, y in enumerate([2010, 2011, 2012, 2013])}
oeq = {y: BS["Other equipment"][i] for i, y in enumerate([2010, 2011, 2012, 2013])}
ppe_gross = {y: BS["Total property and equipment, at cost"][i] for i, y in enumerate([2010, 2011, 2012, 2013])}
equity = {y: BS["Total equity"][i] for i, y in enumerate([2010, 2011, 2012, 2013])}
goodwill13 = BS["Goodwill"][3]
dep_ppe = {y: CF["Depreciation of property and equipment"][i] for i, y in enumerate([2009, 2010, 2011, 2012, 2013])}
prov_cf = {y: CF["Provision for losses on doubtful accounts"][i] for i, y in enumerate([2009, 2010, 2011, 2012, 2013])}
ap_cf13 = CF["Accounts payable"][4]

PTI13 = pti[2013]
assert PTI13 == 663.1

results = []  # (measure, label, reported, recomputed, match)


def rec(measure, label, reported, value, tol=0.05):
    match = abs(reported - value) <= tol
    results.append((measure, label, reported, value, match))
    flag = "match" if match else "DIFF"
    print(f"  [{flag}] {label}: reported {reported}, recomputed {value:.3f}")


# ================================================================ 1. Rental equipment depreciation rate
print("1. Rental equipment depreciation rate (Note 8 charge before disposal adjustment over average gross fleet)")
onpage("AR12", 113, "Depreciation of revenue earning equipment | $2,165.2 | $1,921.8 | $1,747.0")
onpage("AR13", 126, "Depreciation of revenue earning equipment | $2,407.8 | $2,145.9 | $1,912.3")
onpage("AR13", 75, "Cars | 14,456.6 | 12,548.8")
dep_first = {2011: 1921.8, 2012: 2165.2, 2013: 2407.8}
dep_rev = {2011: 1912.3, 2012: 2145.9, 2013: 2407.8}
gross_first = {y: cars[y] + oeq[y] for y in cars}             # workbook, first reported
gross_rev = dict(gross_first)
gross_rev[2012] = 12548.8 + oeq[2012]                          # revised 2012 cars (AR13 p.75)
avg = lambda d, y: (d[y] + d[y - 1]) / 2
rate_first = {y: 100 * dep_first[y] / avg(gross_first, y) for y in (2011, 2012, 2013)}
rate_rev = {y: 100 * dep_rev[y] / avg(gross_rev, y) for y in (2011, 2012, 2013)}
rec(1, "FY2011 rate, first reported (numbers-1)", 16.2, rate_first[2011])
rec(1, "FY2012 rate, first reported (numbers-1)", 15.3, rate_first[2012])
rec(1, "FY2013 rate (numbers-1)", 14.3, rate_first[2013])
rec(1, "FY2011 rate, revised (numbers-2)", 16.1, rate_rev[2011])
rec(1, "FY2012 rate, revised (numbers-2)", 15.2, rate_rev[2012])
rec(1, "FY2013 rate, revised base (numbers-2)", 14.3, rate_rev[2013])

# ================================================================ 2. Charge not taken at the FY2012 rate; all-in rate
print("2. Charge not taken at the FY2012 rate; disclosed rate changes; all-in rate")
onpage("AR13", 126, "net decreases of $44.2 million, $139.4 million and $26.7 million")
onpage("AR13", 126, "net increases of $5.0 million, $8.8 million and $12.9 million")
onpage("AR13", 126, "a decrease of $0.4 million, an increase of $0.5 million, and a decrease of $4.4 million")
onpage("AR13", 126, "Adjustment of depreciation upon disposal of revenue earning equipment | 37.2 | (96.8) | (112.2)")
not_taken_first = rate_first[2012] / 100 * avg(gross_first, 2013) - dep_first[2013]
not_taken_rev = rate_rev[2012] / 100 * avg(gross_rev, 2013) - dep_rev[2013]
rec(2, "Charge not taken, first reported $m (numbers-1)", 174.5, not_taken_first, 0.5)
rec(2, "Share of pre-tax, first reported % (numbers-1)", 26, 100 * not_taken_first / PTI13, 0.5)
rec(2, "Charge not taken, revised $m (numbers-2)", 152.1, not_taken_rev, 0.5)
rec(2, "Share of pre-tax, revised % (numbers-2)", 23, 100 * not_taken_rev / PTI13, 0.5)
net_changes = 44.2 - 5.0 + 0.4
rec(2, "Disclosed net rate changes $m (numbers-2)", 39.6, net_changes, 0.05)
rec(2, "Net changes as share of revised shortfall % (numbers-2)", 26, 100 * net_changes / not_taken_rev, 0.5)
rec(2, "Net changes as share of total depreciation % (numbers-2)", 1.6, 100 * net_changes / 2407.8, 0.05)
allin13 = 100 * (2407.8 + 37.2) / avg(gross_rev, 2013)
allin12 = 100 * (2145.9 - 96.8) / avg(gross_rev, 2012)
rec(2, "All-in rate FY2013 % (numbers-2, report-5)", 14.5, allin13, 0.05)
rec(2, "All-in rate FY2012 % (numbers-2, report-5)", 14.5, allin12, 0.05)

# ================================================================ 3. Car-only depreciation rate (text-4) and the 26.7% the report ranks on
print("3. Car depreciation over average gross car cost (text-4 write-up 1; report-5 ranks item 1 on 26.7%)")
# Equipment-segment depreciation of revenue earning equipment from the FY2013 release (Table 7 segment lines,
# unnumbered page), net of equipment disposal gains; the gains are added back from Note 8.
eq_seg = {2013: 298.8, 2012: 272.1}
assert any("Depreciation of revenue earning equipment | 1,269.7 | 451.1 | 298.8 | 425.4 | 2,445.0" in t for lab, t in PAGES["ER13"])
assert any("939.9 | 449.1 | 272.1 | 388.0 | 2,049.1" in t for lab, t in PAGES["ER13"])
onpage("AR13", 126, "net gains of $26.2 million, $13.5 million and $13.3 million")
eq_gains = {2013: 26.2, 2012: 13.5}
car_dep = {y: dep_rev[y] - (eq_seg[y] + eq_gains[y]) for y in (2012, 2013)}
cars_rev = dict(cars)
cars_rev[2012] = 12548.8
car_rate = {y: 100 * car_dep[y] / avg(cars_rev, y) for y in (2012, 2013)}
rec(3, "Car rate FY2012 % (text-4)", 16.7, car_rate[2012], 0.05)
rec(3, "Car rate FY2013 % (text-4)", 15.4, car_rate[2013], 0.05)
car_not_taken = car_rate[2012] / 100 * avg(cars_rev, 2013) - car_dep[2013]
rec(3, "Car charge not taken at FY2012 rate $m (text-4 'about $177m')", 177, car_not_taken, 1.0)
rec(3, "Share of pre-tax % (report-5 'ranks on 26.7%')", 26.7, 100 * car_not_taken / PTI13, 0.1)

# ================================================================ 4. Stated effects and swings as shares of pre-tax income
print("4. Stated rate-cut effect, U.S. disposal loss, swing, legal exposure, goodwill plus trade name")
onpage("AR13", 126, "net losses of $48.2 million, and net gains of $100.6 million")
onpage("AR13", 137, "could potentially exceed $40.0 million")
onpage("AR13", 96, "3,330.0")
rec(4, "$44.2m as share of pre-tax % (text-3, text-4, report-5)", 6.7, 100 * 44.2 / PTI13, 0.05)
rec(4, "$48.2m as share of pre-tax % (text-3, report-5)", 7.3, 100 * 48.2 / PTI13, 0.05)
rec(4, "U.S. disposal swing $m (text-4)", 148.8, 100.6 + 48.2, 0.05)
rec(4, "Swing as share of pre-tax % (text-4)", 22.4, 100 * 148.8 / PTI13, 0.05)
rec(4, "Nevada exposure $40.0m as share % (text-3, text-4, report-5)", 6.0, 100 * 40.0 / PTI13, 0.05)
gw_tn = goodwill13 + 3330.0
rec(4, "Goodwill plus trade name $m (text-3, report-5)", 4677.5, gw_tn, 0.05)
rec(4, "As share of total equity % (text-3, report-5)", 169, 100 * gw_tn / equity[2013], 0.5)

# ================================================================ 5. Holding-period and life statements (text-4 Part 2 table)
print("5. Holding-period range, implied holding periods, per-vehicle depreciation, reserve, property rate")
onpage("AR12", 81, "Cars | 4 to 28 months")
onpage("AR13", 91, "Cars | 4 to 36 months")
onpage("AR12", 11, "eighteen months in the United States and fourteen months")
onpage("AR13", 11, "eighteen months in the United States and thirteen months")
onpage("AR13", 53, "longer holding periods")
onpage("AR13", 42, "Percentage of non-program cars in our U.S. car rental operations | 91% | 95% | 83%")
onpage("AR13", 42, "197,700, 136,400 and 121,800 non-program cars")
onpage("AR13", 43, "Percentage of non-program cars in our international car rental operations | 76% | 79% | 75%")
onpage("AR13", 43, "64,500, 54,500 and 54,800 non-program cars")
onpage("AR13", 49, "Average number of cars (Company-operated) | 468,500 | 358,000 | 321,700")
onpage("AR13", 49, "Average number of cars (Leased) | 21,500 | 1,100")
onpage("AR13", 49, "Average number of cars (Company-operated) | 159,700 | 153,700 | 156,900")
onpage("AR13", 54, "$1,269.3 million for 2013 increased $328.7 million, or 34.9% from $940.6 million")
onpage("AR13", 138, "$347.7 million and $332.2 million")
onpage("AR13", 42, "26.2% increase in transaction days")
rec(5, "Top of car range, rise % (text-4 '29%')", 29, 100 * (36 - 28) / 28, 0.5)
# Implied holding period: average company-operated cars x average non-program share over the year, over non-program cars sold, x 12
us_share = {2013: (0.95 + 0.91) / 2, 2012: (0.83 + 0.95) / 2}
us_cars = {2013: 468500, 2012: 358000}
us_sold = {2013: 197700, 2012: 136400}
us_months = {y: 12 * us_cars[y] * us_share[y] / us_sold[y] for y in us_cars}
rec(5, "Implied U.S. months 2012 (text-4 'about 28')", 28, us_months[2012], 0.5)
rec(5, "Implied U.S. months 2013 (text-4 'about 26')", 26, us_months[2013], 0.5)
int_share = {2013: (0.79 + 0.76) / 2, 2012: (0.75 + 0.79) / 2}
int_cars = {2013: 159700, 2012: 153700}
int_sold = {2013: 64500, 2012: 54500}
int_months = {y: 12 * int_cars[y] * int_share[y] / int_sold[y] for y in int_cars}
rec(5, "Implied international months 2012 (text-4 'about 26')", 26, int_months[2012], 0.5)
rec(5, "Implied international months 2013 (text-4 'about 23')", 23, int_months[2013], 0.5)
# U.S. per-vehicle depreciation per month: segment depreciation and lease charges over average cars
pv_all = {2013: 1269.3e6 / (468500 + 21500) / 12, 2012: 940.6e6 / (358000 + 1100) / 12}
pv_co = {2013: 1269.3e6 / 468500 / 12, 2012: 940.6e6 / 358000 / 12}
rec(5, "U.S. per-vehicle change incl. leased % (text-3, text-4)", -1.1, 100 * (pv_all[2013] / pv_all[2012] - 1), 0.05)
rec(5, "U.S. per-vehicle change company-operated % (text-3, text-4)", 3.1, 100 * (pv_co[2013] / pv_co[2012] - 1), 0.05)
rec(5, "PL&PD reserve rise % (text-4)", 4.7, 100 * (347.7 / 332.2 - 1), 0.05)
ppe_rate = {y: 100 * dep_ppe[y] / avg(ppe_gross, y) for y in (2012, 2013)}
rec(5, "Property and equipment rate FY2012 % (text-4)", 7.3, ppe_rate[2012], 0.05)
rec(5, "Property and equipment rate FY2013 % (text-4)", 7.9, ppe_rate[2013], 0.05)
eq_ad = {2013: 1095.8, 2012: 1041.9}
rec(5, "Other equipment accumulated over gross FY2012 % (text-4)", 32.2, 100 * eq_ad[2012] / oeq[2012], 0.05)
rec(5, "Other equipment accumulated over gross FY2013 % (text-4)", 31.2, 100 * eq_ad[2013] / oeq[2013], 0.05)
eq_rate = {y: 100 * (eq_seg[y] + eq_gains[y]) / avg(oeq, y) for y in (2012, 2013)}
rec(5, "Equipment rate FY2012 % (text-4 '9.3')", 9.3, eq_rate[2012], 0.05)
rec(5, "Equipment rate FY2013 % (text-4 '9.6')", 9.6, eq_rate[2013], 0.05)

# ================================================================ 6. Allowance for doubtful accounts
print("6. Allowance for doubtful accounts (Schedule II, balance sheet, cash flow)")
onpage("AR13", 158, "Year ended December 31, 2013 | $29.3 | $41.9 | $(0.1) | $(40.3)")
onpage("AR12", 140, "Year ended December 31, 2012 | $20,282 | $34,144 | $28 | $(29,341) | (a) | $25,113")
onpage("AR13", 80, "Provision for losses on doubtful accounts | 45.9 | 38.3 | 28.2")
allow = {2010: 19.708, 2011: 20.282, 2012: 25.113, 2013: 30.8}   # first reported; 2013 from AR13
rec(6, "Allowance share of gross receivables FY2011 % (numbers-1)", 1.24, 100 * allow[2011] / (recv[2011] + allow[2011]), 0.005)
rec(6, "Allowance share FY2012, first reported % (numbers-1)", 1.31, 100 * allow[2012] / (recv[2012] + allow[2012]), 0.005)
rec(6, "Allowance share FY2013 % (numbers-1, text-3)", 2.00, 100 * allow[2013] / (recv[2013] + allow[2013]), 0.005)
rec(6, "Allowance over write-offs FY2012 first reported (text-4 '0.86')", 0.86, 25.113 / 29.341, 0.005)
rec(6, "Allowance over write-offs FY2012 revised (text-4 '1.00')", 1.00, 29.3 / 29.3, 0.005)
rec(6, "Allowance over write-offs FY2013 (text-4, report-5 '0.76')", 0.76, 30.8 / 40.3, 0.005)
rec(6, "Months of write-offs covered (text-3 'about 9')", 9, 12 * 30.8 / 40.3, 0.5)
rec(6, "Schedule II vs cash-flow provision gap $m (text-3, report-5)", 4.0, prov_cf[2013] - 41.9, 0.05)
rec(6, "Gap as share of pre-tax % (report-5)", 0.6, 100 * 4.0 / PTI13, 0.05)

# ================================================================ 7. Adjusted pre-tax income
print("7. Adjusted pre-tax income: add-backs and their shares (FY2013 release reconciliation; Note 12 p.140)")
assert any("Income before income taxes | 663.1 | 490.1 | 1,153.2 | 441.4 | 450.9 | 892.3" in t for lab, t in PAGES["ER13"])
assert any("Income before income taxes | 450.6 | 450.9 | 901.5 | 324.3 | 356.2 | 680.5" in t for lab, t in PAGES["ER12"])
assert any("Restructuring and related charges | 98.8 | 49.1" in t for lab, t in PAGES["ER13"])
assert any("Integration expenses | 40.0" in t for lab, t in PAGES["ER13"])
assert any("Relocation costs | 7.8" in t for lab, t in PAGES["ER13"])
assert any("Impairment charges and other(f) | 44.0" in t for lab, t in PAGES["ER13"])
onpage("AR13", 140, "we incurred $645.4 million")
rec(7, "All add-backs $m (numbers-2, text-3, report-5)", 490.1, 1153.2 - 663.1, 0.05)
rec(7, "All add-backs share % (text-3, report-5 '73.9')", 73.9, 100 * 490.1 / PTI13, 0.05)
rec(7, "Restructuring plus related share % (text-3, report-5 '14.9')", 14.9, 100 * 98.8 / PTI13, 0.05)
new_cats = 40.0 + 7.8 + 44.0
rec(7, "New 2013 add-backs $m (text-4, report-5 '91.8')", 91.8, new_cats, 0.05)
rec(7, "New 2013 add-backs share % (text-4, report-5 '13.8')", 13.8, 100 * new_cats / PTI13, 0.05)
rec(7, "Restructuring plus integration and relocation share % (text-3 '22.1')", 22.1, 100 * (98.8 + 40.0 + 7.8) / PTI13, 0.05)
rec(7, "Seven-year restructuring average $m (text-3 'about $92m')", 92, 645.4 / 7, 0.5)
rec(7, "FY2011 gap as share of reported % (numbers-2 '110')", 110, 100 * 356.2 / 324.3, 0.5)
rec(7, "FY2012 gap as share of revised % (numbers-2 '102')", 102, 100 * 450.9 / 441.4, 0.5)
rec(7, "FY2013 gap as share of reported % (numbers-2 '74')", 74, 100 * 490.1 / 663.1, 0.5)
rec(7, "Adjusted pre-tax growth on revised 2012 % (text-4 '29.2')", 29.2, 100 * (1153.2 / 892.3 - 1), 0.05)
rec(7, "Adjusted pre-tax growth on first-reported 2012 % (text-4 '27.9')", 27.9, 100 * (1153.2 / 901.5 - 1), 0.05)

# ================================================================ 8. Error corrections (Note 2)
print("8. Out-of-period error corrections (Note 2, pp. 83 to 87; release p.1)")
onpage("AR13", 83, "out of period errors totaling $46.3 million, of which $34.7 million")
onpage("AR13", 84, "Income before income taxes | 450.6 | (9.2) | 441.4 | 324.3 | (18.7) | 305.6")
nine_prev = num("AR13", 87, "Income before income taxes", 0)
nine_rev = num("AR13", 87, "Income before income taxes", 2) if False else None
# the p.87 table carries three-month and nine-month columns; take the nine-month pair explicitly
line87 = [t for lab, t in PAGES["AR13"] if lab == "87"][0]
m87 = re.search(r"Income before income taxes \|([^\n]*?)(?:\(Provision\)|Provision)", line87)
vals87 = [float(c.replace("(", "-").replace(")", "").replace(",", "").replace("$", "").strip()) for c in m87.group(1).split("|") if re.search(r"\d", c)]
nine_prev, nine_rev = vals87[-3], vals87[-1]
assert any("$62.3 million" in t for lab, t in PAGES["ER13"])
rec(8, "FY2011 pre-tax cut $m (numbers-1 '18.7')", 18.7, 324.3 - 305.6, 0.05)
rec(8, "FY2011 cut as share of first-reported pre-tax % (text-3 '5.8')", 5.8, 100 * 18.7 / 324.3, 0.05)
rec(8, "FY2012 pre-tax cut, 10-K basis $m (text-4 '9.2')", 9.2, 450.6 - 441.4, 0.05)
rec(8, "FY2012 pre-tax cut, workbook basis $m (numbers-1 '9.1'; PK10)", 9.1, pti[2012] - 441.4, 0.05)
rec(8, "Prior-year portion as share of pre-tax % (report-5 '5.2')", 5.2, 100 * 34.7 / PTI13, 0.05)
rec(8, "2013 nine-month portion $m (text-4 '11.6')", 11.6, nine_prev - nine_rev, 0.05)
rec(8, "2013 portion as share of pre-tax % (report-5 '1.7')", 1.7, 100 * 11.6 / PTI13, 0.05)
rec(8, "Prior-year errors against Q4 pre-tax $62.3m % (text-3 '56')", 56, 100 * 34.7 / 62.3, 0.5)
rec(8, "Equity cut at 31 Dec 2012 $m (numbers-1 '21.1')", 21.1, equity[2012] - 2486.2, 0.05)

# ================================================================ 9. Payables
print("9. Payables: days, size, the Dollar Thrifty base effect, payables less unpaid purchases")
onpage("AR13", 84, "Direct operating | 4,795.8 | (a) | 10.2 | 4,806.0")
onpage("AR13", 84, "Depreciation of revenue earning equipment and lease charges | 2,148.2 | (b) | (19.3) | 2,128.9")
onpage("AR13", 75, "Accounts payable | $967.9 | $1,003.2")
onpage("AR13", 98, "Accounts payable | (43)")
onpage("AR13", 81, "Purchases of revenue earning equipment included in accounts payable and accrued liabilities | $289.1 | $247.0")
onpage("AR13", 81, "Purchases of property and equipment included in accounts payable | 55.6 | 35.0")
onpage("AR13", 80, "Accounts payable | 23.2 | 34.0")
days = lambda bal, flow, d: bal / flow * d
dp = {2010: days(ap[2010], cos[2010], 365), 2011: days(ap[2011], cos[2011], 365), 2012: days(ap[2012], cos[2012], 366), 2013: days(ap[2013], cos[2013], 365)}
cos12_rev = 4806.0 + 2128.9
dp12_rev = days(1003.2, cos12_rev, 366)
rec(9, "Days payable FY2010 (numbers-1)", 56.6, dp[2010], 0.05)
rec(9, "Days payable FY2011 (numbers-1)", 50.6, dp[2011], 0.05)
rec(9, "Days payable FY2012 first reported (numbers-1)", 52.7, dp[2012], 0.05)
rec(9, "Days payable FY2012 revised (numbers-2)", 52.9, dp12_rev, 0.05)
rec(9, "Days payable FY2013 (numbers-1)", 42.7, dp[2013], 0.05)
size_first = cos[2013] * dp[2012] / 365 - ap[2013]
size_rev = cos[2013] * dp12_rev / 365 - ap[2013]
rec(9, "Size at FY2012 days, first reported $m (numbers-1 '226.3')", 226.3, size_first, 0.1)
rec(9, "Share of pre-tax, first reported % (numbers-1 '34')", 34, 100 * size_first / PTI13, 0.5)
rec(9, "Size at FY2012 days, revised $m (numbers-2 '232.8')", 232.8, size_rev, 0.1)
rec(9, "Share of pre-tax, revised % (numbers-2 '35')", 35, 100 * size_rev / PTI13, 0.5)
dp12_exdt = days(1003.2 - 43, cos12_rev, 366)
size_exdt = cos[2013] * dp12_exdt / 365 - ap[2013]
rec(9, "Dollar Thrifty base effect $m (numbers-2 '51.5')", 51.5, size_rev - size_exdt, 0.15)
rec(9, "Dollar Thrifty share of the size % (numbers-2 '22')", 22, 100 * (size_rev - size_exdt) / size_rev, 0.5)
ex12 = 1003.2 - 247.0 - 35.0
ex13 = 967.9 - 289.1 - 55.6
rec(9, "Payables less unpaid purchases FY2012 $m (numbers-2 '721.2')", 721.2, ex12, 0.05)
rec(9, "Payables less unpaid purchases FY2013 $m (numbers-2 '623.2')", 623.2, ex13, 0.05)
rec(9, "Change % (numbers-2 '-13.6')", -13.6, 100 * (ex13 / ex12 - 1), 0.05)
rec(9, "Direct operating plus SG&A growth, revised 2012 base % (numbers-2 '17.3')", 17.3, 100 * ((do[2013] + sga[2013]) / (4806.0 + 968.1) - 1), 0.05)
rec(9, "Balance sheet fall in payables $m (numbers-2 '35.3')", 35.3, 1003.2 - 967.9, 0.05)
rec(9, "Cash-flow rise in payables $m (numbers-2 '23.2')", 23.2, ap_cf13, 0.05)
ind_ap = IND["Acc Pay/ Sales"] / 100
excess_ap = ap[2013] - ind_ap * rev[2013]
rec(9, "Payables above industry share $m (numbers-1 '483.2')", 483.2, excess_ap, 0.1)
rec(9, "Unpaid purchases cover of the excess % (numbers-2 '71')", 71, 100 * (289.1 + 55.6) / excess_ap, 0.5)
rec(9, "Payables ex purchases as share of sales % (numbers-2 '5.8')", 5.8, 100 * (ap[2013] - 289.1 - 55.6) / rev[2013], 0.05)
# Q4 days payable from the releases (first-reported Q4 2012 and the FY2013 release's Q4 figures)
assert any("Direct operating | 1,439.3 | 1,257.7" in t for lab, t in PAGES["ER13"])
assert any("Depreciation of revenue earning equipment and lease charges | 643.0 | 550.0" in t for lab, t in PAGES["ER13"])
assert any("Direct operating | 1,250.6 | 1,057.8" in t for lab, t in PAGES["ER12"])
rec(9, "Q4 2011 days payable (numbers-1 '52.1')", 52.1, days(ap[2011], 1057.8 + 526.7, 92), 0.05)
rec(9, "Q4 2012 days payable on the FY2013 release's revised Q4 2012 costs (numbers-1 '50.9')", 50.9, days(ap[2012], 1257.7 + 550.0, 92), 0.05)
rec(9, "Q4 2012 days payable on the FY2012 release's first-reported costs (numbers-1 '50.9')", 50.9, days(ap[2012], 1250.6 + 553.8, 92), 0.05)
rec(9, "Q4 2013 days payable (numbers-1 '42.8')", 42.8, days(ap[2013], 1439.3 + 643.0, 92), 0.05)

# ================================================================ 10. Receivables and margins
print("10. Receivables, operating margin against the industry, Q4 gross margin")
onpage("AR13", 81, "Sales of revenue earning equipment included in receivables | 357.3 | 618.6")
onpage("AR13", 81, "Sales of property and equipment included in receivables | 16.6 | 0.9")
onpage("AR13", 75, "Receivables, less allowance for doubtful accounts of $30.8 and $29.3 | 1,512.6 | 1,879.7")
assert any("Total revenues | $2,556.3 | $2,319.7" in t for lab, t in PAGES["ER13"])
rec(10, "DSO FY2012 first reported (numbers-1 '76.5')", 76.5, days(recv[2012], rev[2012], 366), 0.05)
rec(10, "DSO FY2013 (numbers-1 '51.3')", 51.3, days(recv[2013], rev[2013], 365), 0.05)
rec(10, "DSO Q4 2012 (numbers-1 '74.8')", 74.8, days(recv[2012], 2319.7, 92), 0.05)
rec(10, "DSO Q4 2013 (numbers-1 '54.4')", 54.4, days(recv[2013], 2556.3, 92), 0.05)
ind_ar = IND["Acc Rec/ Sales"] / 100
excess_ar = recv[2013] - ind_ar * rev[2013]
rec(10, "Receivables above industry share $m (numbers-1 '273.8')", 273.8, excess_ar, 0.1)
rec(10, "Share of pre-tax % (numbers-1 '41')", 41, 100 * excess_ar / PTI13, 0.5)
rec(10, "Sale proceeds in receivables as cover of the excess % (numbers-2 '137')", 137, 100 * (357.3 + 16.6) / excess_ar, 0.5)
rec(10, "Receivables ex sale proceeds as share of sales % (numbers-2 '10.6')", 10.6, 100 * (recv[2013] - 357.3 - 16.6) / rev[2013], 0.05)
rec(10, "Vehicle-sale receivables fall $m (numbers-2 '261.3')", 261.3, 618.6 - 357.3, 0.05)
rec(10, "Total receivables fall, revised 2012 $m (numbers-2 '367.1')", 367.1, 1879.7 - 1512.6, 0.05)
rec(10, "Vehicle-sale share of the fall % (numbers-2 '71')", 71, 100 * 261.3 / 367.1, 0.5)
rec(10, "Vehicle-sale fall as share of 2012 receivables % (numbers-2 '13.9')", 13.9, 100 * 261.3 / 1879.7, 0.05)
op_inc = rev[2013] - do[2013] - dep_lc[2013] - sga[2013]
op_m = 100 * op_inc / rev[2013]
rec(10, "Operating margin FY2013 % (numbers-1 '13.7')", 13.7, op_m, 0.05)
rec(10, "Gap to industry x revenue $m (numbers-1 '836.7')", 836.7, (op_m - IND["Pre-tax Unadjusted Operating Margin"]) / 100 * rev[2013], 0.1)
rec(10, "Gap as share of pre-tax % (numbers-1 '126')", 126, 100 * 836.7 / PTI13, 0.5)
net_int = int_exp + int_inc
rec(10, "Net interest $m (numbers-2 '704.4')", 704.4, net_int, 0.05)
m_after = 100 * (op_inc - net_int) / rev[2013]
rec(10, "Margin after net interest % (numbers-2 '7.1')", 7.1, m_after, 0.05)
rec(10, "Gap after net interest $m (numbers-2 '$132m')", 132, (m_after - 5.9) / 100 * rev[2013], 0.5)
rec(10, "Q4 2012 gross margin % (numbers-1 '22.1')", 22.1, 100 * (2319.7 - 1257.7 - 550.0) / 2319.7, 0.05)
rec(10, "Q4 2013 gross margin % (numbers-1 '18.5')", 18.5, 100 * (2556.3 - 1439.3 - 643.0) / 2556.3, 0.05)
rec(10, "Gross margin FY2013 % (numbers-1 '23.2')", 23.2, 100 * (rev[2013] - cos[2013]) / rev[2013], 0.05)

# ================================================================ summary
print()
n = len(results)
ok = sum(1 for r in results if r[4])
print(f"Sub-figures recomputed: {n}; matched: {ok}; differ: {n - ok}")
for m, label, rep, val, match in results:
    if not match:
        print(f"  DIFF measure {m}: {label}: reported {rep}, recomputed {val:.3f}")
by_measure = {}
for m, label, rep, val, match in results:
    by_measure.setdefault(m, []).append(match)
print("Measures with every sub-figure matching:", sum(1 for m in by_measure if all(by_measure[m])), "of", len(by_measure))
