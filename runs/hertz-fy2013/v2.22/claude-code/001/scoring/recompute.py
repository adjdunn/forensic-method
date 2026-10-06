"""Recompute ten measures the hertz-fy2013 v2.22 claude-code/001 replies rest on.

Inputs: the workspace files the run saw (statements.xlsx and the four text
files with [p. N] page markers). Figures typed in from the pack text are
labelled with their page and asserted present on that page before use.
Run from anywhere; paths are absolute. No em-dashes.
"""
import re
import openpyxl

WS = r"C:\Users\aaron\Dev\forensic-method\runs\hertz-fy2013\v2.22\claude-code\001\workspace"


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
        out[key] = out.get(key, "") + parts[i + 1]
    return out


K13 = "annual-report-FY2013-12-31.txt"
K12 = "annual-report-FY2012-12-31.txt"
R13 = "earnings-release-Q4-FY2013-12-31.txt"
R12 = "earnings-release-Q4-FY2012-12-31.txt"
P = {n: pages(n) for n in (K13, K12, R13, R12)}


def on_page(name, page, needle):
    return needle in P[name][str(page)]


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
CF = sheet("CF annual")
FY = {y: f"FY (ended {y}-12-31)" for y in (2009, 2010, 2011, 2012, 2013)}
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
#    numbers-1 (first reported): 16.2, 15.3, 14.2.  numbers-2 (revised): 15.2, 14.3.
assert on_page(K13, 126, "$2,407.8 | $2,145.9 | $1,912.3")
assert on_page(K12, 113, "$2,165.2 | $1,921.8 | $1,747.0")
assert on_page(K13, 75, "14,456.6 | 12,548.8") and on_page(K13, 75, "3,512.2 | 3,240.1")
dep13, dep12r, dep12f, dep11f = 2407.8, 2145.9, 2165.2, 1921.8
g = {y: BS["Cars"][FY[y]] + BS["Other equipment"][FY[y]] for y in (2010, 2011, 2012, 2013)}
g12r = 12548.8 + 3240.1
avg13f, avg12f, avg11f = (g[2013] + g[2012]) / 2, (g[2012] + g[2011]) / 2, (g[2011] + g[2010]) / 2
avg13r, avg12r = (g[2013] + g12r) / 2, (g12r + g[2011]) / 2
r13f, r12f, r11f = dep13 / avg13f, dep12f / avg12f, dep11f / avg11f
r13r, r12r = dep13 / avg13r, dep12r / avg12r
rec("1a", "Rate FY2013 first reported, % (numbers-1: 14.2)", 14.2, round(r13f * 100, 1), "p. 126; workbook BS")
rec("1b", "Rate FY2012 first reported, % (numbers-1: 15.3)", 15.3, round(r12f * 100, 1), "FY2012 p. 113; workbook BS")
rec("1c", "Rate FY2011 first reported, % (numbers-1: 16.2)", 16.2, round(r11f * 100, 1), "FY2012 p. 113; workbook BS")
rec("1d", "Rate FY2013 revised base, % (numbers-2: 14.3)", 14.3, round(r13r * 100, 1), "p. 126; p. 75")
rec("1e", "Rate FY2012 revised, % (numbers-2: 15.2)", 15.2, round(r12r * 100, 1), "p. 126; p. 75")

# 2. Charge not taken at the FY2012 rate (numbers-1: $174.5m, 26.3%; numbers-2: $152.1m revised, 29% is $44.2m).
nt_f = r12f * avg13f - dep13
nt_r = r12r * avg13r - dep13
rec("2a", "Charge not taken at FY2012 rate, first reported, $m (numbers-1: 174.5)", 174.5, round(nt_f, 1), "derived from 1a, 1b")
rec("2b", "Same, % of pre-tax (numbers-1, report-5: 26.3)", 26.3, round(nt_f / PRETAX * 100, 1), "derived")
rec("2c", "Charge not taken, revised, $m (numbers-2, report-5: 152.1)", 152.1, round(nt_r, 1), "derived from 1d, 1e")
rec("2d", "Same, % of pre-tax (report-5: 22.9)", 22.9, round(nt_r / PRETAX * 100, 1), "derived")
assert on_page(K13, 126, "net decreases of $44.2 million")
rec("2e", "$44.2m as % of the revised charge not taken (numbers-2: 29)", 29, round(44.2 / nt_r * 100), "p. 126", tol=0.5)

# 3. Rate with the disposal adjustment added back, flat (numbers-2: 14.48 to 14.49).
assert on_page(K13, 126, "37.2 | (96.8) | (112.2)")
rec("3a", "Rate incl. disposal adjustment FY2013, % (numbers-2: 14.49)", 14.49, round((dep13 + 37.2) / avg13r * 100, 2), "p. 126; p. 75", tol=0.0051)
rec("3b", "Rate incl. disposal adjustment FY2012 revised, % (numbers-2: 14.48)", 14.48, round((dep12r - 96.8) / avg12r * 100, 2), "p. 126; p. 75", tol=0.0051)

# 4. U.S. depreciation per car per month. numbers-2 ex-disposal: $241.6 to $207.7, down 14.1%;
#    text-3 on the reported line: $218 to $216. Cars: company-operated plus leased, p. 49.
assert on_page(K13, 131, "U.S. car rental | $1,269.3 | $940.6")
assert on_page(K13, 126, "net losses of $48.2 million, and net gains of $100.6 million")
assert on_page(K13, 49, "468,500 | 358,000 | 321,700") and on_page(K13, 49, "21,500 | 1,100 |")
cars13, cars12 = 468500 + 21500, 358000 + 1100
pc13 = (1269.3 - 48.2) * 1e6 / cars13 / 12
pc12 = (940.6 + 100.6) * 1e6 / cars12 / 12
rec("4a", "U.S. dep per car per month ex disposal FY2013, $ (numbers-2: 207.7)", 207.7, round(pc13, 1), "p. 131; p. 126; p. 49")
rec("4b", "Same FY2012, $ (numbers-2: 241.6)", 241.6, round(pc12, 1), "p. 131; p. 126; p. 49")
rec("4c", "Fall, % (numbers-2: 14.1)", 14.1, round((1 - pc13 / pc12) * 100, 1), "derived")
rec("4d", "U.S. dep per car per month, reported line FY2013, $ (text-3: 216)", 216, round(1269.3e6 / cars13 / 12), "p. 131; p. 49", tol=0.5)
rec("4e", "Same FY2012, $ (text-3: 218)", 218, round(940.6e6 / cars12 / 12), "p. 131; p. 49", tol=0.5)

# 5. Disposal swing and the stated rate effects as shares of pre-tax (text-3, text-4, numbers-2, report-5).
assert on_page(K13, 126, "net losses of $15.2 million, $17.3 million")
assert on_page(K13, 43, "net increases of $5.0 million") and on_page(K13, 43, "decrease of $0.4 million")
rec("5a", "U.S. disposal swing, $m (text-3, text-4: 148.8)", 148.8, round(100.6 + 48.2, 1), "p. 126")
rec("5b", "$44.2m rate cut / pre-tax, % (text-3, text-4, report-5: 6.7)", 6.7, round(44.2 / PRETAX * 100, 1), "p. 126 / p. 76")
rec("5c", "$48.2m disposal loss / pre-tax, % (text-3: 7.3)", 7.3, round(48.2 / PRETAX * 100, 1), "p. 126 / p. 76")
rec("5d", "Net rate effect 44.2 - 5.0 + 0.4 = 39.6, % of pre-tax (numbers-2, text-4, report-5: 6.0)", 6.0, round((44.2 - 5.0 + 0.4) / PRETAX * 100, 1), "pp. 43, 126")
rec("5e", "Net car disposal loss FY2013, $m (text-4: 63.4)", 63.4, round(48.2 + 15.2, 1), "p. 126")
assert on_page(K12, 113, "net gains of $83.2 million")
rec("5f", "Net car disposal gain FY2012 on the FY2012 basis, $m (text-4: 83.2; printed; the FY2013 basis 100.6 - 17.3 gives 83.3)", 83.2, 83.2, "FY2012 p. 113")

# 6. Adjusted pre-tax income (numbers-2, text-3, text-4, report-5).
assert on_page(R13, 9, "663.1 | 490.1 | 1,153.2")
assert on_page(K13, 50, "(77.0) | (38.0) | (56.4)") and on_page(K13, 50, "(21.8) | (11.1) | (9.8)")
assert on_page(K13, 50, "Premiums paid on debt(9) | (28.7)") and on_page(K13, 50, "Other(11) | (50.7) | (44.0)")
assert on_page(K13, 50, "Integration expenses(7) | (40.0)") and on_page(K13, 50, "Relocation costs | (7.8)")
assert on_page(K13, 140, "we incurred $645.4 million")
rec("6a", "All add-backs $490.1m / pre-tax, % (text-3, report-5: 73.9)", 73.9, round(490.1 / PRETAX * 100, 1), "release p. 9 / p. 76")
rec("6b", "2012 gap $450.9m / revised pre-tax $441.4m, % (numbers-2: 102)", 102, round(450.9 / 441.4 * 100), "release p. 9; p. 84", tol=0.5)
rec("6c", "2012 gap = 901.5 - 450.6, $m (numbers-2: 450.9)", 450.9, round(901.5 - 450.6, 1), "release p. 9; p. 84")
rec("6d", "Restructuring plus related 77.0 + 21.8 = 98.8, % of pre-tax (text-3, report-5: 14.9)", 14.9, round((77.0 + 21.8) / PRETAX * 100, 1), "p. 50")
rec("6e", "Restructuring 2007 to 2013 per year, $m (text-3: 92.2)", 92.2, round(645.4 / 7, 1), "p. 140")
new = 40.0 + 7.8 + 44.0 + 28.7 + 50.7
rec("6f", "Add-back categories new in 2013, $m (text-4, report-5: 171.2)", 171.2, round(new, 1), "p. 50")
rec("6g", "Same, % of pre-tax (text-4, report-5: 25.8)", 25.8, round(new / PRETAX * 100, 1), "p. 50 / p. 76")
rec("6h", "Restructuring plus related 2012 (38.0 + 11.1) and 2011 (56.4 + 9.8), $m (numbers-2: 49.1, 66.2)", 49.1 + 66.2, round(38.0 + 11.1 + 56.4 + 9.8, 1), "p. 50")

# 7. Allowance for doubtful accounts (numbers-1 table, text-3, text-4, report-5).
assert on_page(K13, 158, "$29.3 | $41.9 | $(0.1) | $(40.3)") and on_page(K13, 158, "20.3 | 38.3 |")
rec("7a", "Allowance / write-offs FY2013 (text-3, text-4, report-5: 0.76)", 0.76, round(30.8 / 40.3, 2), "Sch. II p. 158", tol=0.0051)
rec("7b", "Allowance / write-offs FY2012 revised (text-4: 1.00)", 1.00, round(29.3 / 29.3, 2), "p. 158", tol=0.0051)
rec("7c", "Allowance at 1.0x write-offs less actual, $m (text-4: 9.5)", 9.5, round(40.3 - 30.8, 1), "p. 158")
rec("7d", "Same, % of pre-tax (text-4, report-5: 1.4)", 1.4, round((40.3 - 30.8) / PRETAX * 100, 1), "derived")
rec("7e", "Write-offs growth, % (text-4 says 37; exact 37.5, truncated not rounded)", 37, round((40.3 / 29.3 - 1) * 100, 1), "p. 158", tol=0.6)
rec("7f", "Allowance % of gross receivables FY2013 (numbers-1, text-3: 2.00)", 2.00, round(30.8 / (BS[REC][FY[2013]] + 30.8) * 100, 2), "p. 75; p. 158", tol=0.0051)
# FY2012 as first reported: allowance 25.1 (FY2012 10-K Schedule II p. 140); numbers-1: 1.31.
assert on_page(K12, 140, "$(29,341) | (a) | $25,113") and on_page(K12, 140, "(27,658) | (a) | 20,282") and on_page(K12, 140, "(20,532) | (a) | 19,708")
rec("7g", "Allowance % of gross receivables FY2012 first reported (numbers-1: 1.31)", 1.31, round(25.113 / (BS[REC][FY[2012]] + 25.113) * 100, 2), "FY2012 p. 140 (thousands); workbook BS", tol=0.0051)
rec("7h", "Same FY2011 (numbers-1: 1.24)", 1.24, round(20.282 / (BS[REC][FY[2011]] + 20.282) * 100, 2), "FY2012 p. 140; workbook BS", tol=0.0051)
rec("7i", "Same FY2010 (numbers-1: 1.43)", 1.43, round(19.708 / (BS[REC][FY[2010]] + 19.708) * 100, 2), "FY2012 p. 140; workbook BS", tol=0.0051)

# 8. Payables (numbers-1 flag 2 first reported; numbers-2 revised).
cost13 = IS["Direct operating"][FY[2013]] + IS["Depreciation of revenue earning equipment and lease charges"][FY[2013]]
cost12f = IS["Direct operating"][FY[2012]] + IS["Depreciation of revenue earning equipment and lease charges"][FY[2012]]
ap13, ap12f = BS["Accounts payable"][FY[2013]], BS["Accounts payable"][FY[2012]]
assert on_page(K13, 75, "Accounts payable | $967.9 | $1,003.2")
assert on_page(K13, 76, "Direct operating | 5,752.0 | 4,806.0") and on_page(K13, 76, "2,525.5 | 2,128.9")
ap12r, cost12r = 1003.2, 4806.0 + 2128.9
rec("8a", "Days payable FY2013 (numbers-1: 42.7)", 42.7, round(ap13 / cost13 * 365, 1), "workbook")
rec("8b", "Days payable FY2012 first reported, 366-day year (numbers-1: 52.7)", 52.7, round(ap12f / cost12f * 366, 1), "workbook")
rec("8c", "Days payable FY2012 revised, 366-day year (numbers-2: 52.9)", 52.9, round(ap12r / cost12r * 366, 1), "p. 75; p. 76")
rec("8d", "Payables change first reported, % (numbers-1: -3.1)", -3.1, round((ap13 / ap12f - 1) * 100, 1), "workbook")
rec("8e", "Payables change revised, % (numbers-2: -3.5)", -3.5, round((ap13 / ap12r - 1) * 100, 1), "p. 75")
rec("8f", "Cost growth first reported, % (numbers-1: 19.2)", 19.2, round((cost13 / cost12f - 1) * 100, 1), "workbook")
rec("8g", "Cost growth revised, % (numbers-2: 19.4)", 19.4, round((cost13 / cost12r - 1) * 100, 1), "p. 76")
size8 = ap12f / cost12f * 366 / 365 * cost13 - ap13
rec("8h", "Payables at prior-year days less actual, $m (numbers-1: 226.3)", 226.3, round(size8, 1), "derived")
rec("8i", "Same, % of pre-tax (numbers-1, report-5: 34.1)", 34.1, round(size8 / PRETAX * 100, 1), "derived")
assert on_page(K13, 81, "$289.1 | $247.0 | $153.6") and on_page(K13, 81, "| 55.6 | 35.0 | 53.3")
fp13, fp12 = 289.1 + 55.6, 247.0 + 35.0
rec("8j", "Fleet and property purchases in payables, rise, $m (numbers-2: 62.7)", 62.7, round(fp13 - fp12, 1), "p. 81")
rec("8k", "Payables ex fleet purchases FY2012 revised, $m (numbers-2: 721.2)", 721.2, round(ap12r - fp12, 1), "pp. 75, 81")
rec("8l", "Same FY2013, $m (numbers-2: 623.2)", 623.2, round(ap13 - fp13, 1), "pp. 75, 81")
rec("8m", "Fall in payables ex fleet purchases, % (numbers-2: 13.6)", 13.6, round((1 - (ap13 - fp13) / (ap12r - fp12)) * 100, 1), "derived")
assert on_page(K13, 80, "Accounts payable | 23.2 | 34.0") and on_page(K13, 80, "Accrued liabilities | 25.2 | (29.6)") and on_page(K13, 80, "Accrued taxes | 24.5 | 28.8")
assert on_page(K13, 64, "we generated $879.9 million more cash from operating activities")
wc = (23.2 + 25.2 + 24.5) - (34.0 - 29.6 + 28.8)
rec("8n", "Payables, accruals and taxes: 2013 lines less 2012 lines, $m (numbers-2: 39.7)", 39.7, round(wc, 1), "p. 80")
rec("8o", "Same, % of the $879.9m rise (numbers-2: 4.5)", 4.5, round(wc / 879.9 * 100, 1), "pp. 64, 80")
rec("8p", "Balance-sheet payables change, $m (numbers-2: -35.3)", -35.3, round(ap13 - ap12r, 1), "p. 75")

# 9. Q4 gross margin (numbers-1 flag 4, numbers-2, report-5), release Table 1 (p. 9) and Tables 4 and 5 (unnumbered).
assert on_page(R13, 9, "$2,556.3 | $2,319.7") and on_page(R13, 9, "1,439.3 | 1,257.7") and on_page(R13, 9, "643.0 | 550.0")
rev13q, rev12q, do13q, do12q, dp13q, dp12q = 2556.3, 2319.7, 1439.3, 1257.7, 643.0, 550.0
gm13 = (rev13q - do13q - dp13q) / rev13q
gm12 = (rev12q - do12q - dp12q) / rev12q
rec("9a", "Q4 2013 gross margin, % (numbers-1: 18.5)", 18.5, round(gm13 * 100, 1), "release p. 9")
rec("9b", "Q4 2012 gross margin, % (numbers-1: 22.1)", 22.1, round(gm12 * 100, 1), "release p. 9")
rec("9c", "Fall times Q4 revenue, $m (numbers-1, report-5: 90.2)", 90.2, round((gm12 - gm13) * rev13q, 1), "derived")
rec("9d", "Same, % of pre-tax (numbers-1, report-5: 13.6)", 13.6, round((gm12 - gm13) * rev13q / PRETAX * 100, 1), "derived")
rec("9e", "Fall times full-year revenue, $m (numbers-1: 380.2)", 380.2, round((gm12 - gm13) * IS["Total revenues"][FY[2013]], 1), "derived")
rec("9f", "Same, % of pre-tax (numbers-1: 57.3)", 57.3, round((gm12 - gm13) * IS["Total revenues"][FY[2013]] / PRETAX * 100, 1), "derived")
rec("9g", "Direct operating growth Q4, % (numbers-1: 14.4)", 14.4, round((do13q / do12q - 1) * 100, 1), "release p. 9")
rec("9h", "Fleet depreciation growth Q4, % (numbers-1: 16.9)", 16.9, round((dp13q / dp12q - 1) * 100, 1), "release p. 9")
rec("9i", "Revenue growth Q4, % (numbers-1: 10.2)", 10.2, round((rev13q / rev12q - 1) * 100, 1), "release p. 9")
U = P[R13]["9"]  # Tables 1 to 8 follow the p. 9 marker on unnumbered pages
assert "Transaction days (in thousands) (a) | 32,875 | 16.1%" in U and "Average number of cars (Company-operated) | 472,200 | 22.4%" in U
assert "Total RPD (b) | $44.91 | (1.4)%" in U
assert "Depreciation of revenue earning equipment and lease charges | 333.4 | 124.8 | 75.7 | 109.1 | 0.0 | 643.0 | 246.0" in U
days13q, cars13q = 32875e3, 472200
days12q, cars12q = days13q / 1.161, cars13q / 1.224
rec("9j", "U.S. Q4 utilisation 2013, % (numbers-2: 75.7)", 75.7, round(days13q / (cars13q * 92) * 100, 1), "release Table 4")
rec("9k", "U.S. Q4 utilisation 2012, % (numbers-2: 79.8)", 79.8, round(days12q / (cars12q * 92) * 100, 1), "release Table 4, derived from the % changes", tol=0.11)
rec("9l", "U.S. Q4 fleet depreciation growth, % (numbers-2: 35.5)", 35.5, round((333.4 / 246.0 - 1) * 100, 1), "release Table 5")
rec("9m", "Fleet depreciation above 16.1% day growth, $m (numbers-2: 47.8)", 47.8, round(333.4 - 246.0 * 1.161, 1), "release Tables 4 and 5")
rec("9n", "RPD fall 1.4% on Q4 days at $44.91, $m (numbers-2: 21.0)", 21.0, round((44.91 / 0.986 - 44.91) * days13q / 1e6, 1), "release Table 4", tol=0.11)
rec("9o", "Coverage 47.8 + 21.0 as % of the 90.2 fall (numbers-2: 76)", 76, round((47.8 + 21.0) / 90.2 * 100), "derived", tol=0.5)
assert on_page(R13, 9, "Diluted | 464.3 | 421.1")
rec("9p", "$0.12 per diluted Q4 share, pre-tax at 35%, $m (numbers-2: about 85.7)", 85.7, round(0.12 * 464.3 / 0.65, 1), "release pp. 2, 9", tol=0.3)

# 10. Reserve per rental day, receivables, free cash flow, text-4's car depreciation (rough).
assert on_page(K13, 49, "133,181 | 105,539 | 93,741") and on_page(K13, 49, "45,019 | 43,248 | 43,560")
d13, d12, d11 = 133181 + 45019, 105539 + 43248, 93741 + 43560
res13, res12, res11 = BS["Public liability and property damage"][FY[2013]], 332.2, 281.5
rec("10a", "Reserve per 1,000 rental days FY2013, $k (text-4: 1.95)", 1.95, round(res13 / d13 * 1000, 2), "p. 49; p. 75", tol=0.0051)
rec("10b", "Same FY2012 (text-4: 2.23)", 2.23, round(res12 / d12 * 1000, 2), "p. 49; p. 75", tol=0.0051)
rec("10c", "Same FY2011 (text-4: 2.05)", 2.05, round(res11 / d11 * 1000, 2), "p. 49; workbook BS", tol=0.0051)
rec("10d", "Rental days growth, % (text-4, report-5: 19.8)", 19.8, round((d13 / d12 - 1) * 100, 1), "p. 49")
rec("10e", "Reserve growth, % (text-4, report-5: 4.7)", 4.7, round((res13 / res12 - 1) * 100, 1), "p. 75")
rec("10f", "Reserve at the 2011 ratio less actual, $m (text-4: 17.7)", 17.7, round(res11 / d11 * d13 - res13, 1), "derived", tol=0.11)
rec("10g", "Reserve at the 2012 ratio less actual, $m (text-4: 50.2)", 50.2, round(res12 / d12 * d13 - res13, 1), "derived", tol=0.11)
# Receivables (numbers-1 flag 1; numbers-2 other flags).
rev13 = IS["Total revenues"][FY[2013]]
rec13 = BS[REC][FY[2013]]
rec("10h", "Receivables less balance at the industry 11.5% of sales, $m (numbers-1: 273.8)", 273.8, round(rec13 - 0.115 * rev13, 1), "workbook; Industry sheet")
rec("10i", "Same, % of pre-tax (numbers-1: 41.3)", 41.3, round((rec13 - 0.115 * rev13) / PRETAX * 100, 1), "derived")
assert on_page(K13, 75, "| 1,512.6 | 1,879.7") and on_page(K13, 81, "357.3 | 618.6 | 620.7")
rec("10j", "Vehicle-sale receivables fall, $m (numbers-2: 261.3)", 261.3, round(618.6 - 357.3, 1), "p. 81")
rec("10k", "As % of the revised receivables decline 367.1 (numbers-2: 71)", 71, round((618.6 - 357.3) / (1879.7 - 1512.6) * 100), "pp. 75, 81", tol=0.5)
rec("10l", "DSO ex vehicle-sale receivables FY2013 (numbers-2: 39.1)", 39.1, round((rec13 - 357.3) / rev13 * 365, 1), "pp. 75, 81; workbook IS")
# Free cash flow (numbers-1): CFO plus fleet and property capex net of proceeds.
fcf = {}
for y in (2010, 2012, 2013):
    fcf[y] = (CF["Net cash provided by (used in) operating activities"][FY[y]]
              + CF["Revenue earning equipment expenditures"][FY[y]] + CF["Proceeds from disposal of revenue earning equipment"][FY[y]]
              + CF["Property and equipment expenditures"][FY[y]] + CF["Proceeds from disposal of property and equipment"][FY[y]])
rec("10m", "Free cash flow FY2013, $m (numbers-1: 314.5)", 314.5, round(fcf[2013], 1), "workbook CF")
rec("10n", "Free cash flow FY2012, $m (numbers-1: 54.8)", 54.8, round(fcf[2012], 1), "workbook CF")
rec("10o", "Free cash flow FY2010, $m (numbers-1: 1,145.9)", 1145.9, round(fcf[2010], 1), "workbook CF")
rec("10p", "Net income less FCF FY2013, % of pre-tax (numbers-1: 4.8)", 4.8, round((IS["Net income"][FY[2013]] - fcf[2013]) / PRETAX * 100, 1), "derived")
# text-4's rough car depreciation rate (16.9 to 15.4) and fleet age in depreciation-months (12.0 to 15.4):
# "treats all depreciation outside equipment rental as cars and includes Donlen". Method not stated;
# the nearest reproducible reading is the Note 8 charge less the equipment rental segment line (p. 131).
assert on_page(K13, 131, "Worldwide equipment rental | 298.8 | 272.1")
car13, car12 = dep13 - 298.8, dep12r - 272.1
avgcars13 = (BS["Cars"][FY[2013]] + 12548.8) / 2
avgcars12 = (12548.8 + BS["Cars"][FY[2011]]) / 2
rec("10q", "Car depreciation / average gross cars FY2012, % (text-4: 16.9)", 16.9, round(car12 / avgcars12 * 100, 1), "pp. 126, 131, 75; workbook BS")
rec("10r", "Fleet age, accumulated / monthly car depreciation FY2012, months (text-4: 12.0)", 12.0, round(1881.0 / (car12 / 12), 1), "p. 75 (acc. dep. 1,881.0 first reported); derived")
assert on_page(K13, 75, "2,679.6")  # accumulated depreciation on cars, FY2013
acc13 = 2679.6
rec("10s", "Car depreciation / average gross cars FY2013, % (text-4: 15.4)", 15.4, round(car13 / avgcars13 * 100, 1), "same method as 10q")
rec("10t", "Fleet age FY2013, months (text-4: 15.4)", 15.4, round(acc13 / (car13 / 12), 1), "same method as 10r")
# The FY2013 figures reproduce only if the equipment segment line is grossed up for its own disposal
# gain ($26.2m, p. 126) before subtraction; the same gross-up ($13.5m) breaks the FY2012 figures.
assert on_page(K13, 126, "net gains of $26.2 million, $13.5 million")
car13b, car12b = dep13 - (298.8 + 26.2), dep12r - (272.1 + 13.5)
rec("10u", "FY2013 rate with the equipment line grossed up for its $26.2m gain, % (text-4: 15.4)", 15.4, round(car13b / avgcars13 * 100, 1), "alternative method")
rec("10v", "FY2013 age on the same basis, months (text-4: 15.4)", 15.4, round(acc13 / (car13b / 12), 1), "alternative method")
rec("10w", "FY2012 rate on that alternative method, % (text-4: 16.9)", 16.9, round(car12b / avgcars12 * 100, 1), "alternative method")
rec("10x", "FY2012 age on that alternative method, months (text-4: 12.0)", 12.0, round(1881.0 / (car12b / 12), 1), "alternative method")

print(f"{'#':<5} {'reported':>9} {'recomputed':>11}  result    measure")
for n, label, reported, value, where, res in results:
    print(f"{str(n):<5} {reported:>9} {value:>11}  {res:<9} {label} [{where}]")
print()
print(sum(1 for r in results if r[-1] == "match"), "of", len(results), "sub-figures match")
