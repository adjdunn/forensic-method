"""Recompute ten measures the hertz-fy2013 v2.23 claude-code/001 replies rest on.

Inputs: the workspace files the run saw (statements.xlsx and the four text
files with [p. N] page markers). Figures typed in from the pack text are
labelled with their page and asserted present on that page before use.
Run from anywhere; paths are absolute. No em-dashes.
"""
import re
import openpyxl

WS = r"C:\Users\aaron\Dev\forensic-method\runs\hertz-fy2013\v2.23\claude-code\001\workspace"


def pages(name):
    t = open(f"{WS}\\{name}", encoding="utf-8").read()
    # "[p. unnumbered]" blocks (the release's tables) are folded into the last
    # numbered page, which is how the checker and the replies cite them (p. 9).
    parts = re.split(r"\[p\. (\d+|unnumbered)\]", t)
    out = {}
    key = "0"
    for i in range(1, len(parts), 2):
        if parts[i] != "unnumbered":
            key = parts[i]
        out[key] = out.get(key, "") + re.sub(r"\s+", " ", parts[i + 1])
    return out


K13 = "annual-report-FY2013-12-31.txt"
K12 = "annual-report-FY2012-12-31.txt"
R13 = "earnings-release-Q4-FY2013-12-31.txt"
R12 = "earnings-release-Q4-FY2012-12-31.txt"
P = {n: pages(n) for n in (K13, K12, R13, R12)}


def on_page(name, page, needle):
    return needle in P[name][str(page)]


def need(name, page, *needles):
    for s in needles:
        assert on_page(name, page, s), (name, page, s)


wb = openpyxl.load_workbook(f"{WS}\\statements.xlsx", data_only=True)


def sheet(name):
    rows = list(wb[name].iter_rows(values_only=True))
    hdr = rows[0]
    return {r[0]: dict(zip(hdr[1:], r[1:])) for r in rows[1:] if r[0] is not None}


IS = sheet("IS annual")
BS = sheet("BS annual")
BSQ = sheet("BS quarterly")
FY = {y: f"FY (ended {y}-12-31)" for y in (2009, 2010, 2011, 2012, 2013)}
Q = {"Q3 2012": "Q3 (ended 2012-09-30)", "Q4 2012": "Q4 (ended 2012-12-31)",
     "Q3 2013": "Q3 (ended 2013-09-30)", "Q4 2013": "Q4 (ended 2013-12-31)"}
REC = "Receivables, less allowance for doubtful accounts of $30.8 and $29.3"
PRETAX = IS["Income before income taxes"][FY[2013]]  # 663.1, FY2013 10-K p. 76
assert PRETAX == 663.1

results = []


def rec(n, label, reported, value, where, tol=0.051):
    ok = abs(value - reported) <= tol
    results.append((n, label, reported, value, where, "match" if ok else "NO MATCH"))


# ---------------------------------------------------------------------------
# 1. Rental equipment depreciation rate: Note 8 charge before the disposal
#    adjustment over average gross cars plus other equipment.
#    numbers-1: 16.2, 15.3, 14.3 (FY2011 to FY2013).  numbers-2: 15.2 to 14.3 revised.
need(K13, 126, "$2,407.8 | $2,145.9 | $1,912.3")
need(K12, 113, "$2,165.2 | $1,921.8 | $1,747.0")
need(K13, 75, "Cars | 14,456.6 | 12,548.8", "Other equipment | 3,512.2 | 3,240.1")
dep13, dep12r, dep12f, dep11f = 2407.8, 2145.9, 2165.2, 1921.8
g = {y: BS["Cars"][FY[y]] + BS["Other equipment"][FY[y]] for y in (2010, 2011, 2012, 2013)}
g12r = 12548.8 + 3240.1
avg13f, avg12f, avg11f = (g[2013] + g[2012]) / 2, (g[2012] + g[2011]) / 2, (g[2011] + g[2010]) / 2
avg13r, avg12r = (g[2013] + g12r) / 2, (g12r + g[2011]) / 2
r13f, r12f, r11f = dep13 / avg13f, dep12f / avg12f, dep11f / avg11f
r13r, r12r = dep13 / avg13r, dep12r / avg12r
rec("1a", "Rate FY2011 first reported, % (numbers-1: 16.2)", 16.2, round(r11f * 100, 1), "FY2012 p. 113; workbook BS")
rec("1b", "Rate FY2012 first reported, % (numbers-1: 15.3)", 15.3, round(r12f * 100, 1), "FY2012 p. 113; workbook BS")
rec("1c", "Rate FY2013 on the revised FY2012 base, % (numbers-1, numbers-2: 14.3)", 14.3, round(r13r * 100, 1), "p. 126; p. 75")
rec("1d", "Rate FY2013 on the first-reported FY2012 base, % (not stated; 14.2 in the v2.22 run)", 14.2, round(r13f * 100, 1), "p. 126; workbook BS")
rec("1e", "Rate FY2012 revised, % (numbers-2: 15.2)", 15.2, round(r12r * 100, 1), "p. 126; p. 75")

# 2. Charge not taken at the FY2012 rate (numbers-1: $175m, 26%; numbers-2 and report-5: $152m, 23%).
nt_f = r12f * avg13f - dep13
nt_r = r12r * avg13r - dep13
rec("2a", "Charge not taken, first reported, $m (numbers-1: 175)", 175, round(nt_f), "derived from 1b, 1d", tol=0.5)
rec("2b", "Same, % of pre-tax (numbers-1, report-5: 26)", 26, round(nt_f / PRETAX * 100), "derived", tol=0.5)
rec("2c", "Charge not taken, revised, $m (numbers-2: 152)", 152, round(nt_r), "derived from 1c, 1e", tol=0.5)
rec("2d", "Same, % of pre-tax (numbers-2, report-5: 23)", 23, round(nt_r / PRETAX * 100), "derived", tol=0.5)
need(K13, 126, "net decreases of $44.2 million")
need(K13, 43, "net increases of $5.0 million", "decrease of $0.4 million")
rec("2e", "Net rate changes 44.2 - 5.0 + 0.4 as % of the revised shortfall (numbers-2: 39.6, 26%)", 26,
    round((44.2 - 5.0 + 0.4) / nt_r * 100), "pp. 43, 126", tol=0.5)

# 3. Q4 rental depreciation rate, annualised (numbers-1: 13.7% Q4 2012, 13.4% Q4 2013).
#    Reproduces on the release's "Depreciation of revenue earning equipment" line (620.2; 533.8),
#    annualised by days in the year over the quarter's 92 days, over the average of the Q3 and Q4
#    gross cars plus other equipment from the workbook's quarterly balance sheet (first reported).
U = P[R13]["9"]
assert "Depreciation of revenue earning equipment | 333.4 | 102.0 | 75.7 | 109.1 | 620.2 | 245.9 | 111.9 | 73.9 | 102.1 | 533.8" in U
gq = {k: BSQ["Cars"][v] + BSQ["Other equipment"][v] for k, v in Q.items()}
q13 = 620.2 * 365 / 92 / ((gq["Q3 2013"] + gq["Q4 2013"]) / 2)
q12 = 533.8 * 366 / 92 / ((gq["Q3 2012"] + gq["Q4 2012"]) / 2)
rec("3a", "Q4 2013 annualised rate, % (numbers-1: 13.4)", 13.4, round(q13 * 100, 1), "release tables (after p. 9); workbook BS quarterly")
rec("3b", "Q4 2012 annualised rate, % (numbers-1: 13.7)", 13.7, round(q12 * 100, 1), "same")
# Simple x4 annualising gives 13.5 and 13.8: same direction.
rec("3c", "Q4 2013 on x4 annualising, % (check of method; same direction)", 13.5, round(620.2 * 4 / ((gq["Q3 2013"] + gq["Q4 2013"]) / 2) * 100, 1), "same")

# 4. Note 8 figures as shares of pre-tax (text-3, text-4, numbers-2, report-5).
need(K13, 126, "net losses of $48.2 million, and net gains of $100.6 million")
rec("4a", "$44.2m rate cut / pre-tax, % (text-3, text-4, report-5: 6.7)", 6.7, round(44.2 / PRETAX * 100, 1), "p. 126 / p. 76")
rec("4b", "$48.2m U.S. disposal loss / pre-tax, % (text-3, text-4, report-5: 7.3)", 7.3, round(48.2 / PRETAX * 100, 1), "p. 126")
rec("4c", "U.S. disposal swing, $m (text-3, text-4: 148.8)", 148.8, round(100.6 + 48.2, 1), "p. 126")
rec("4d", "Swing / pre-tax 663.1, % (text-4: 22.4; the checker's 16.7 used 892.3)", 22.4, round(148.8 / PRETAX * 100, 1), "p. 126 / p. 76")
need(K13, 126, "26.7 million")  # "net decreases of $44.2 million, $139.4 million and $26.7 million"
need(K13, 84, "441.4")
rec("4e", "2012 cut $139.4m / revised 2012 pre-tax 441.4, % (numbers-2: 31.6)", 31.6, round(139.4 / 441.4 * 100, 1), "p. 126; p. 84")
rec("4f", "2011 cut $26.7m / revised 2011 pre-tax 305.6, % (numbers-2: 8.7)", 8.7, round(26.7 / 305.6 * 100, 1), "p. 126; workbook Revisions")

# 5. Holding-period proxies and fleet age (text-4 table, report-5 item 1).
need(K13, 42, "197,700, 136,400 and 121,800 non-program cars", "| 91% | 95% | 83%")
need(K13, 43, "64,500, 54,500 and 54,800 non-program cars", "| 76% | 79% | 75%")
need(K13, 49, "Average number of cars (Company-operated) | 468,500 | 358,000 | 321,700",
     "Average number of cars (Company-operated) | 159,700 | 153,700 | 156,900")
rec("5a", "U.S. non-program fleet / non-program cars sold FY2013, months (text-4, report-5: 25.9)", 25.9, round(468500 * 0.91 / 197700 * 12, 1), "pp. 42, 49")
rec("5b", "Same FY2012, months (text-4, report-5: 29.9)", 29.9, round(358000 * 0.95 / 136400 * 12, 1), "pp. 42, 49")
rec("5c", "International same FY2013, months (text-4: 22.6)", 22.6, round(159700 * 0.76 / 64500 * 12, 1), "pp. 43, 49")
rec("5d", "International same FY2012, months (text-4: 26.7)", 26.7, round(153700 * 0.79 / 54500 * 12, 1), "pp. 43, 49")
need(K12, 81, "4 to 28 months")
need(K13, 91, "4 to 36 months")
rec("5e", "Top of the car range, rise %, 28 to 36 (text-4: 29)", 29, round((36 / 28 - 1) * 100), "FY2012 p. 81; FY2013 p. 91", tol=0.5)
need(K13, 75, "Less accumulated depreciation | (2,679.6) | (1,850.4)")
rec("5f", "Car accumulated depreciation / cost FY2012 revised, % (text-4: 14.7)", 14.7, round(1850.4 / 12548.8 * 100, 1), "p. 75", tol=0.06)
rec("5g", "Same FY2013, % (text-4: 18.5)", 18.5, round(2679.6 / 14456.6 * 100, 1), "p. 75")

# 6. Per-vehicle depreciation (text-3, text-4, numbers-2, report-5).
need(K13, 131, "U.S. car rental | $1,269.3 | $940.6")
need(K13, 49, "Average number of cars (Leased) | 21,500 | 1,100", "Average number of cars (Leased) | 1,600 | 1,400")
pv13, pv12 = 1269.3e6 / (468500 + 21500) / 12, 940.6e6 / (358000 + 1100) / 12
rec("6a", "U.S. dep per vehicle per month FY2013, $ (text-3, text-4: 215.9)", 215.9, round(pv13, 1), "p. 131; p. 49")
rec("6b", "Same FY2012, $ (text-3, text-4: 218.3)", 218.3, round(pv12, 1), "p. 131; p. 49")
rec("6c", "Change, % (text-3, report-5: -1.1)", -1.1, round((pv13 / pv12 - 1) * 100, 1), "derived")
co = (1269.3 / 468500) / (940.6 / 358000) - 1
rec("6d", "Company-operated cars only, change, % (text-3: +3.2)", 3.2, round(co * 100, 1), "p. 131; p. 49")
# 3.12 exact; 3.2 reproduces only from the dollars rounded first ($226 against $219).
rec("6d2", "Same from rounded dollars 226 / 219, % (text-3: +3.2)", 3.2, round((226 / 219 - 1) * 100, 1), "derived")
assert "Depreciation of revenue earning equipment and lease charges | 1,269.3 | 532.0 | 298.8 | 425.4 | 0.0 | 2,525.5 | 940.6 | 528.2 | 272.1" in U
rec("6e", "International dep per vehicle per month FY2013, $ (text-4: 274.9)", 274.9, round(532.0e6 / (159700 + 1600) / 12, 1), "release segment table; p. 49")
rec("6f", "Same FY2012, $ (text-4: 283.8)", 283.8, round(528.2e6 / (153700 + 1400) / 12, 1), "same")
assert "Average number of cars (Company-operated) | 472,200 | 22.4%" in U
assert "Depreciation of revenue earning equipment and lease charges | 333.4 | 124.8 | 75.7 | 109.1 | 0.0 | 643.0 | 246.0" in U
rec("6g", "U.S. Q4 depreciation per car, change, % (numbers-2, report-5: +10.7)", 10.7, round((333.4 / 246.0 / 1.224 - 1) * 100, 1), "release Tables 4, 5")
eq13 = 298.8 / ((3512.2 + 3240.1) / 2)
eq12 = 272.1 / ((3240.1 + BS["Other equipment"][FY[2011]]) / 2)
rec("6h", "Equipment depreciation / average equipment cost FY2013, % (text-4: 8.8; recomputes 8.85, truncated)", 8.8, round(eq13 * 100, 2), "p. 131; p. 75", tol=0.06)
rec("6i", "Same FY2012, % (text-4: 8.9; recomputes 8.96)", 8.9, round(eq12 * 100, 2), "p. 131; workbook BS", tol=0.07)

# 7. Allowance for doubtful accounts (numbers-1 table, text-3, text-4, report-5).
need(K13, 158, "$29.3 | $41.9 | $(0.1) | $(40.3)")
need(K12, 140, "$(29,341) | (a) | $25,113", "(27,658) | (a) | 20,282")
rec("7a", "Allowance % of gross receivables FY2013 (numbers-1, text-3: 2.00)", 2.00, round(30.8 / (BS[REC][FY[2013]] + 30.8) * 100, 2), "p. 75; p. 158", tol=0.0051)
rec("7b", "Same FY2012 first reported (numbers-1: 1.31)", 1.31, round(25.113 / (BS[REC][FY[2012]] + 25.113) * 100, 2), "FY2012 p. 140; workbook BS", tol=0.0051)
rec("7c", "Same FY2011 (numbers-1: 1.24)", 1.24, round(20.282 / (BS[REC][FY[2011]] + 20.282) * 100, 2), "FY2012 p. 140; workbook BS", tol=0.0051)
rec("7d", "Allowance / write-offs FY2013 (text-4, report-5: 0.76)", 0.76, round(30.8 / 40.3, 2), "p. 158", tol=0.0051)
rec("7e", "Allowance / write-offs FY2012 revised (text-4, report-5: 1.00)", 1.00, round(29.3 / 29.3, 2), "p. 158", tol=0.0051)
need(K13, 80, "Provision for losses on doubtful accounts | 45.9 | 38.3 | 28.2")
rec("7f", "Bad-debt expense, Schedule II against cash flow, gap $m (text-3, report-5: 41.9 vs 45.9)", 4.0, round(45.9 - 41.9, 1), "p. 158; p. 80")

# 8. Adjusted pre-tax income (numbers-2, text-3, text-4, report-5).
assert "663.1 | 490.1 | 1,153.2" in U
need(K13, 50, "(77.0) | (38.0) | (56.4)", "(21.8) | (11.1) | (9.8)", "Integration expenses(7) | (40.0)",
     "Relocation costs | (7.8)", "Premiums paid on debt(9) | (28.7)")
need(K13, 140, "we incurred $645.4 million")
rec("8a", "All add-backs $490.1m / pre-tax, % (numbers-2, text-3, report-5: 73.9 / 74)", 73.9, round(490.1 / PRETAX * 100, 1), "release p. 9")
rec("8b", "Restructuring plus related 77.0 + 21.8, % of pre-tax (text-3, report-5: 14.9)", 14.9, round(98.8 / PRETAX * 100, 1), "p. 50")
new = 40.0 + 7.8 + 44.0 + 28.7
rec("8c", "New 2013 categories, integration + relocation + impairment + debt premiums, $m (text-4: 120.5)", 120.5, round(new, 1), "p. 50")
rec("8d", "Same, % of pre-tax (text-4, report-5: 18.2)", 18.2, round(new / PRETAX * 100, 1), "p. 50")
rec("8e", "Restructuring 2007 to 2013 per year, $m (text-3: 92.2)", 92.2, round(645.4 / 7, 1), "p. 140")
need(R12, 10, "356.2")
rec("8f", "2011 gap $356.2m / first-reported 2011 pre-tax 324.3, % (numbers-2: 110)", 110, round(356.2 / 324.27 * 100), "FY2012 release p. 10; Revisions sheet", tol=0.5)
rec("8g", "2012 gap $450.9m / revised 441.4, % (numbers-2: 102)", 102, round(450.9 / 441.4 * 100), "release p. 9; p. 84", tol=0.5)
rec("8h", "Adjusted share: 490.1 / 1,153.2, % (numbers-2: 42)", 42, round(490.1 / 1153.2 * 100), "release p. 9", tol=0.5)

# 9. Error corrections (numbers-1, text-3, text-4, report-5).
need(K13, 83, "out of period errors totaling $46.3 million")
need(K13, 87, "612.4 | (11.6) | 600.8")
need(R13, 1, "Fourth quarter GAAP pre-tax income of $62.3 million")
rec("9a", "2011 pre-tax cut 324.27 - 305.6, $m (numbers-1: 18.7)", 18.7, round(324.27 - 305.6, 1), "Revisions sheet; p. 84")
rec("9b", "Same, % of first-reported 2011 (text-3, text-4, report-5: 5.8)", 5.8, round(18.67 / 324.27 * 100, 1), "derived")
rec("9c", "2012 pre-tax cut 450.545 - 441.4, $m (numbers-1: 9.1)", 9.1, round(450.545 - 441.4, 1), "Revisions sheet; p. 84")
rec("9d", "Same, % (text-3, text-4, report-5: 2.0)", 2.0, round(9.145 / 450.545 * 100, 1), "derived")
rec("9e", "$46.3m / pre-tax, % (text-3, text-4, report-5: 7.0)", 7.0, round(46.3 / PRETAX * 100, 1), "p. 83")
rec("9f", "2013 nine-month portion $11.6m / pre-tax, % (text-3, text-4, report-5: 1.7)", 1.7, round(11.6 / PRETAX * 100, 1), "p. 87")
rec("9g", "$46.3m / Q4 2013 pre-tax $62.3m, % (text-3: 74)", 74, round(46.3 / 62.3 * 100), "release p. 1", tol=0.5)
rec("9h", "Equity at 31 Dec 2012 cut, $m (numbers-1: 21.1)", 21.1, round(2507.286 - 2486.2, 1), "Revisions sheet; p. 75")

# 10. Receivables, payables and the Q4 margin (numbers-1, numbers-2, report-5).
rev13, rev12f = IS["Total revenues"][FY[2013]], IS["Total revenues"][FY[2012]]
rec13, rec12f = BS[REC][FY[2013]], BS[REC][FY[2012]]
need(K13, 75, "| 1,512.6 | 1,879.7")
need(K13, 81, "357.3 | 618.6 | 620.7", "Sales of property and equipment included in receivables | 16.6 | 0.9")
need(K13, 98, "Receivables | 170")
rec("10a", "DSO FY2012 first reported, 366 days (numbers-1: 76.5)", 76.5, round(rec12f / rev12f * 366, 1), "workbook")
rec("10b", "DSO FY2013 (numbers-1: 51.3)", 51.3, round(rec13 / rev13 * 365, 1), "workbook")
sz = rec12f / rev12f * 366 / 365 * rev13 - rec13
rec("10c", "Receivables at prior-year days less actual, $m (numbers-1: 746)", 746, round(sz), "derived", tol=0.5)
left = (1879.7 - 1512.6) - ((618.6 - 357.3) - (16.6 - 0.9))
rec("10d", "Receivables fall less net sale-receivables fall, $m (numbers-2: 121.5)", 121.5, round(left, 1), "pp. 75, 81")
rec("10e", "Left after the cash-flow line and provision (45.9 - 34.7), $m (numbers-2, report-5: about 110)", 110, round(left - (45.9 - 34.7)), "p. 80", tol=0.5)
cost13 = IS["Direct operating"][FY[2013]] + IS["Depreciation of revenue earning equipment and lease charges"][FY[2013]]
cost12f = IS["Direct operating"][FY[2012]] + IS["Depreciation of revenue earning equipment and lease charges"][FY[2012]]
ap13, ap12f = BS["Accounts payable"][FY[2013]], BS["Accounts payable"][FY[2012]]
rec("10f", "Days payable FY2012 first reported (numbers-1: 52.7)", 52.7, round(ap12f / cost12f * 366, 1), "workbook")
rec("10g", "Days payable FY2013 (numbers-1: 42.7)", 42.7, round(ap13 / cost13 * 365, 1), "workbook")
rec("10h", "Payables at prior-year days less actual, $m (numbers-1, report-5: 226)", 226, round(ap12f / cost12f * 366 / 365 * cost13 - ap13), "derived", tol=0.5)
need(K13, 80, "Accounts payable | 23.2 | 34.0", "Accrued liabilities | 25.2 | (29.6)", "Accrued taxes | 24.5 | 28.8",
     "Public liability and property damage | (3.7) | (4.3)")
wc13, wc12 = 23.2 + 25.2 + 24.5 - 3.7, 34.0 - 29.6 + 28.8 - 4.3
rec("10i", "Liability working-capital lines 2013 and 2012, $m (numbers-2: 69.2, 28.9)", 69.2 + 28.9, round(wc13 + wc12, 1), "p. 80")
need(K13, 64, "$879.9 million")
rec("10j", "Difference / $879.9m rise, % (numbers-2: 4.6)", 4.6, round((wc13 - wc12) / 879.9 * 100, 1), "pp. 64, 80")
need(K13, 81, "Purchases of property and equipment included in accounts payable | 55.6 | 35.0")
rec("10k", "Payables fall unaccounted, -35.3 - 23.2 - 20.6, $m (numbers-2, report-5: 79.1)", -79.1, round((967.9 - 1003.2) - 23.2 - (55.6 - 35.0), 1), "pp. 75, 80, 81")
need(R13, 9, "$2,556.3 | $2,319.7", "1,439.3 | 1,257.7", "643.0 | 550.0")
gm13 = (2556.3 - 1439.3 - 643.0) / 2556.3
gm12 = (2319.7 - 1257.7 - 550.0) / 2319.7
rec("10l", "Q4 gross margin 2013, % (numbers-1: 18.5)", 18.5, round(gm13 * 100, 1), "release p. 9")
rec("10m", "Q4 gross margin 2012, % (numbers-1: 22.1)", 22.1, round(gm12 * 100, 1), "release p. 9")
rec("10n", "Fall x Q4 revenue, $m (numbers-1: 90; v2.23 PR42 wording)", 90, round((gm12 - gm13) * 2556.3), "derived", tol=0.5)
rec("10o", "Same, % of pre-tax (numbers-1, report-5: 14)", 14, round((gm12 - gm13) * 2556.3 / PRETAX * 100), "derived", tol=0.5)

print(f"{'#':<5} {'reported':>9} {'recomputed':>11}  result    measure")
for n, label, reported, value, where, res in results:
    print(f"{str(n):<5} {reported:>9} {value:>11}  {res:<9} {label} [{where}]")
print()
print(sum(1 for r in results if r[-1] == "match"), "of", len(results), "sub-figures match")
