"""Recompute ten figures the hertz-fy2013 v2.22 manual/001 replies rest on.

Inputs: the workspace files the run saw (statements.xlsx and the four text
files with [p. N] page markers). Figures typed in from the pack text are
labelled with their page. Run from anywhere; paths are absolute.
"""
import re
import openpyxl

WS = r"C:\Users\aaron\Dev\forensic-method\runs\hertz-fy2013\v2.22\manual\001\workspace"


def pages(name):
    t = open(f"{WS}\\{name}", encoding="utf-8").read()
    parts = re.split(r"\[p\. (\d+)\]", t)
    out = {}
    for i in range(1, len(parts), 2):
        out[parts[i]] = out.get(parts[i], "") + parts[i + 1]
    return out


def on_page(name, page, needle):
    return needle in pages(name)[str(page)]


K13 = "annual-report-FY2013-12-31.txt"
K12 = "annual-report-FY2012-12-31.txt"
R13 = "earnings-release-Q4-FY2013-12-31.txt"
R12 = "earnings-release-Q4-FY2012-12-31.txt"

wb = openpyxl.load_workbook(f"{WS}\\statements.xlsx", data_only=True)


def sheet(name):
    ws = wb[name]
    rows = list(ws.iter_rows(values_only=True))
    hdr = rows[0]
    d = {}
    for r in rows[1:]:
        if r[0] is not None:
            d[r[0]] = dict(zip(hdr[1:], r[1:]))
    return d


IS = sheet("IS annual")
BS = sheet("BS annual")

FY = {y: f"FY (ended {y}-12-31)" for y in (2010, 2011, 2012, 2013)}
PRETAX = 663.1  # FY2013 10-K p. 76

results = []


def rec(n, label, reported, value, where, tol=None):
    if isinstance(reported, (int, float)):
        tol = tol if tol is not None else 0.05 * (1 if abs(reported) < 10 else 1) + 0.0
        ok = abs(value - reported) <= (tol if tol else 0.051)
    else:
        ok = reported == value
    results.append((n, label, reported, value, where, "match" if ok else "NO MATCH"))


# 1. Rental depreciation rate FY2013 (numbers-1 flag 4: 14.3%).
# Note 8 charge before disposal adjustment, FY2013 10-K p. 126; gross revenue
# earning equipment (cars + other equipment) FY2013 10-K p. 75, FY2012 as revised there.
dep13, dep12, dep11 = 2407.8, 2145.9, 1912.3          # p. 126
assert on_page(K13, 126, "$2,407.8 | $2,145.9 | $1,912.3")
gross13 = 14456.6 + 3512.2                             # p. 75
gross12r = 12548.8 + 3240.1                            # p. 75 (revised FY2012)
assert on_page(K13, 75, "14,456.6 | 12,548.8") and on_page(K13, 75, "3,512.2 | 3,240.1")
gross11 = BS["Cars"][FY[2011]] + BS["Other equipment"][FY[2011]]
gross10 = BS["Cars"][FY[2010]] + BS["Other equipment"][FY[2010]]
avg13 = (gross13 + gross12r) / 2
avg12 = (gross12r + gross11) / 2
avg11 = (gross11 + gross10) / 2
rate13, rate12, rate11 = dep13 / avg13, dep12 / avg12, dep11 / avg11
rec(1, "Rental depreciation rate FY2013, % (numbers-1 flag 4; also 15.2 and 16.1 for FY2012, FY2011)",
    14.3, round(rate13 * 100, 1), "Note 8 p. 126 over average gross REE p. 75 and workbook BS")
rec("1b", "Rental depreciation rate FY2012, %", 15.2, round(rate12 * 100, 1), "same")
rec("1c", "Rental depreciation rate FY2011, %", 16.1, round(rate11 * 100, 1), "same")
rec("1d", "Average gross rental equipment FY2013, $m (numbers-1 flag 4; exact 16,878.85, a half-cent rounding case)", 16878.9, round(avg13, 1), "p. 75", tol=0.101)

# 2. Charge not taken at the FY2012 rate (numbers-1 flag 4: $152m, 23% of pre-tax).
not_taken = rate12 * avg13 - dep13
rec(2, "Charge not taken at FY2012 rate, $m (numbers-1 flag 4)", 152, round(not_taken), "derived", tol=1)
rec("2b", "Same as % of pre-tax (numbers-1, report-5 item 1)", 23, round(not_taken / PRETAX * 100), "derived", tol=0.5)

# 3. Stated U.S. rate cut and disposal loss as shares of pre-tax (text-3, text-4, report-5).
assert on_page(K13, 126, "net decreases of $44.2 million") and on_page(K13, 126, "net losses of $48.2 million")
rec(3, "U.S. rate cut $44.2m / pre-tax, % (text-3, text-4, report-5)", 6.7, round(44.2 / PRETAX * 100, 1), "p. 126 / p. 76")
rec("3b", "U.S. disposal loss $48.2m / pre-tax, % (text-3)", 7.3, round(48.2 / PRETAX * 100, 1), "p. 126 / p. 76")
assert on_page(K13, 40, "decreased by $39.6 million")
rec("3c", "Net rate cut $39.6m / pre-tax, % (numbers-2, report-5)", 6.0, round(39.6 / PRETAX * 100, 1), "p. 40 / p. 76")

# 4. U.S. disposal swing (text-3, text-4: $148.8M, 22.4%).
assert on_page(K13, 126, "net gains of $100.6 million")
rec(4, "U.S. disposal swing gain to loss, $m (text-3, text-4)", 148.8, round(100.6 + 48.2, 1), "p. 126")
rec("4b", "Same as % of pre-tax (text-4)", 22.4, round(148.8 / PRETAX * 100, 1), "derived")

# 5. Adjusted-measure exclusions (text-3, report-5: 14.9% and 73.9%).
assert on_page(K13, 50, "(77.0) | (38.0) | (56.4)") and on_page(K13, 50, "(21.8) | (11.1) | (9.8)")
restr = 77.0 + 21.8
rec(5, "Restructuring plus related $98.8m / pre-tax, % (text-3, report-5)", 14.9, round(restr / PRETAX * 100, 1), "p. 50")
assert on_page(R13, 9, "663.1 | 490.1 | 1,153.2")
rec("5b", "All exclusions $490.1m / pre-tax, % (text-3, report-5)", 73.9, round(490.1 / PRETAX * 100, 1), "release p. 9")
assert on_page(K13, 50, "Integration expenses(7) | (40.0)") and on_page(K13, 50, "Relocation costs | (7.8)") and on_page(K13, 50, "Impairment charges and other(10) | (44.0)")
rec("5c", "New exclusions (integration 40.0, relocation 7.8, impairment 44.0) / pre-tax, % (text-4, report-5)", 13.8,
    round((40.0 + 7.8 + 44.0) / PRETAX * 100, 1), "p. 50")

# 6. Allowance against write-offs (text-4 table, report-5 Also noted).
assert on_page(K13, 158, "$29.3 | $41.9 | $(0.1) | $(40.3)") and on_page(K13, 158, "20.3 | 38.3 |")
rec(6, "Allowance / write-offs FY2013 (text-4)", 0.76, round(30.8 / 40.3, 2), "Schedule II p. 158", tol=0.005)
rec("6b", "Allowance / write-offs FY2012 (text-4)", 1.00, round(29.3 / 29.3, 2), "p. 158", tol=0.005)
rec("6c", "Write-offs growth FY2013, % (text-4, report-5)", 37.5, round((40.3 / 29.3 - 1) * 100, 1), "p. 158")
rec("6d", "Allowance growth FY2013, % (text-4, report-5)", 5.1, round((30.8 / 29.3 - 1) * 100, 1), "p. 158")
rec("6e", "Allowance % of gross receivables FY2013 (numbers-1, text-3)", 2.0, round(30.8 / (1512.6 + 30.8) * 100, 1), "p. 75, p. 158")

# 7. Receivables against revenue (numbers-1 flag 1; as first reported, workbook).
rec13 = BS["Receivables, less allowance for doubtful accounts of $30.8 and $29.3"][FY[2013]]
rec12 = BS["Receivables, less allowance for doubtful accounts of $30.8 and $29.3"][FY[2012]]
rev13 = IS["Total revenues"][FY[2013]]
rev12 = IS["Total revenues"][FY[2012]]
rec(7, "Receivables change FY2013, % (numbers-1 flag 1)", -19.8, round((rec13 / rec12 - 1) * 100, 1), "workbook BS")
rec("7b", "Revenue growth FY2013, % (numbers-1)", 19.4, round((rev13 / rev12 - 1) * 100, 1), "workbook IS")
rec("7c", "DSO FY2013 (numbers-1)", 51.3, round(rec13 / rev13 * 365, 1), "workbook")
rec("7d", "DSO FY2012, 366-day year (numbers-1)", 76.5, round(rec12 / rev12 * 366, 1), "workbook")
rec("7e", "Receivables at FY2012 days less FY2013 balance, $m (numbers-1: $746m, 113%)", 746,
    round(rec12 / rev12 * 366 / 365 * rev13 - rec13), "derived", tol=1)

# 8. Days payable (numbers-1 flag 3), cost line = direct operating + REE depreciation and lease charges.
cost13 = IS["Direct operating"][FY[2013]] + IS["Depreciation of revenue earning equipment and lease charges"][FY[2013]]
cost12 = IS["Direct operating"][FY[2012]] + IS["Depreciation of revenue earning equipment and lease charges"][FY[2012]]
ap13 = BS["Accounts payable"][FY[2013]]
ap12 = BS["Accounts payable"][FY[2012]]
rec(8, "Days payable FY2013 (numbers-1)", 42.7, round(ap13 / cost13 * 365, 1), "workbook")
rec("8b", "Days payable FY2012, 366-day year (numbers-1)", 52.7, round(ap12 / cost12 * 366, 1), "workbook")
rec("8c", "Payables change FY2013, % (numbers-1)", -3.1, round((ap13 / ap12 - 1) * 100, 1), "workbook")
rec("8d", "Cost growth FY2013, % (numbers-1)", 19.2, round((cost13 / cost12 - 1) * 100, 1), "workbook")

# 9. Q4 gross margin (numbers-1 flag 5, report-5 item 3), from the FY2013 release p. 9.
assert on_page(R13, 9, "$2,556.3 | $2,319.7") and on_page(R13, 9, "1,439.3 | 1,257.7") and on_page(R13, 9, "643.0 | 550.0")
gm13 = (2556.3 - 1439.3 - 643.0) / 2556.3
gm12 = (2319.7 - 1257.7 - 550.0) / 2319.7
rec(9, "Q4 2013 gross margin, % (numbers-1)", 18.5, round(gm13 * 100, 1), "release p. 9")
rec("9b", "Q4 2012 gross margin, % (numbers-1)", 22.1, round(gm12 * 100, 1), "release p. 9")
rec("9c", "Margin fall times Q4 revenue, $m (numbers-1: $90m, 14%)", 90, round((gm12 - gm13) * 2556.3), "derived", tol=1)
rec("9d", "Same as % of pre-tax", 14, round((gm12 - gm13) * 2556.3 / PRETAX * 100), "derived", tol=0.5)

# 10. Revision effects and the eighteen-month test (text-3, text-4, report-5).
assert on_page(K13, 84, "450.6 | (9.2) | 441.4")
rec(10, "Pre-tax growth on as-reported FY2012 450.6, % (text-4, report-5)", 47.2, round((PRETAX / 450.6 - 1) * 100, 1), "p. 84")
rec("10b", "Pre-tax growth on revised FY2012 441.4, %", 50.2, round((PRETAX / 441.4 - 1) * 100, 1), "p. 84, p. 57")
rec("10c", "Errors moved to prior years $34.7m / pre-tax, % (text-3, text-4, report-5)", 5.2, round(34.7 / PRETAX * 100, 1), "p. 83")
rec("10d", "Errors total $46.3m / pre-tax, %", 7.0, round(46.3 / PRETAX * 100, 1), "p. 83")
assert on_page(K13, 42, "197,700, 136,400 and 121,800") and on_page(K13, 43, "64,500, 54,500 and 54,800")
assert on_page(K12, 42, "178,300, 164,100 and 161,200")
rec("10e", "2012 cars sold restated, % higher (text-4: 190,900 vs 178,300)", 7.1, round((136400 + 54500) / 178300 * 100 - 100, 1), "FY2013 pp. 42-43; FY2012 p. 42")
# Eighteen-month rough test (text-4 table): U.S. fleet over non-program cars sold, months.
assert on_page(R13, 9, "468,500 | 31.2%") and on_page(R13, 9, "21,500 | N/M")
fleet13_total = 468500 + 21500          # company-operated plus leased, release p. 9
rec("10f", "U.S. fleet (company-operated + leased) / non-program cars sold FY2013, months (text-4: 29.7)", 29.7,
    round(fleet13_total / 197700 * 12, 1), "release p. 9; 10-K p. 42")
rec("10g", "Same on company-operated cars only (not what text-4 used)", 28.4, round(468500 / 197700 * 12, 1), "release p. 9")
# U.S. depreciation per company-operated car per month (numbers-2: $226 vs $219).
assert on_page(K13, 131, "U.S. car rental | $1,269.3 | $940.6")
rec("10h", "U.S. REE depreciation per company-operated car per month FY2013, $ (numbers-2)", 226,
    round(1269.3e6 / 468500 / 12), "p. 131; release p. 9", tol=1)
assert on_page(K13, 49, "468,500 | 358,000 | 321,700") and on_page(K13, 49, "21,500 | 1,100 |")
rec("10i", "Same FY2012 on 358,000 cars (numbers-2: $219)", 219, round(940.6e6 / 358000 / 12), "p. 131; p. 49", tol=1)
rec("10j", "U.S. fleet (358,000 + 1,100 leased) / non-program cars sold FY2012, months (text-4: 31.6)", 31.6,
    round((358000 + 1100) / 136400 * 12, 1), "p. 49; p. 42")

print(f"{'#':<4} {'reported':>10} {'recomputed':>11}  result   measure")
for n, label, reported, value, where, res in results:
    print(f"{str(n):<4} {reported:>10} {value:>11}  {res:<8} {label} [{where}]")
print()
print(sum(1 for r in results if r[-1] == "match"), "of", len(results), "match")
