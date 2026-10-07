"""Recompute ten measures the v2.24 claude-code Hertz replies rest on, from the workspace files.

Run from anywhere: paths are relative to this file. Every figure typed in from the pack text is
asserted present on the cited page; workbook figures come from statements.xlsx. Also recounts the
hit list in text-4 and scans the five replies for trap and banned terms.
"""
import os, re, sys
import openpyxl

HERE = os.path.dirname(os.path.abspath(__file__))
RUN = os.path.dirname(HERE)
WS = os.path.join(RUN, "workspace")
sys.stdout.reconfigure(encoding="utf-8")

# ---------- pack text by printed page ----------
def pages(fn):
    txt = open(os.path.join(WS, fn), encoding="utf-8", errors="replace").read()
    out, cur = {}, "front"
    for line in txt.split("\n"):
        m = re.match(r"\[p\. ([^\]]+)\]", line.strip())
        if m:
            cur = m.group(1); out.setdefault(cur, []); continue
        out.setdefault(cur, []).append(line)
    return {k: "\n".join(v) for k, v in out.items()}

A13 = pages("annual-report-FY2013-12-31.txt")
A12 = pages("annual-report-FY2012-12-31.txt")
R13 = pages("earnings-release-Q4-FY2013-12-31.txt")
R12 = pages("earnings-release-Q4-FY2012-12-31.txt")

def norm(s):
    return re.sub(r"\s+", " ", s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')).lower()

def on_page(doc, page, phrase):
    ok = norm(phrase) in norm(doc.get(page, ""))
    print(f"  [{'ok' if ok else 'MISSING'}] p.{page}: {phrase[:70]}")
    return ok

results = []
def check(label, reported, computed, tol=0.051, note=""):
    ok = abs(reported - computed) <= tol
    results.append((label, reported, computed, ok))
    print(f"  {'match' if ok else 'DIFF '}  {label}: reported {reported} recomputed {computed:.4f} {note}")

# ---------- workbook ----------
wb = openpyxl.load_workbook(os.path.join(WS, "statements.xlsx"), data_only=True)
def sheet(name):
    ws = wb[name]; rows = list(ws.iter_rows(values_only=True))
    hdr = rows[0]; d = {}
    for r in rows[1:]:
        if r[0]: d[r[0]] = dict(zip(hdr[1:], r[1:]))
    return d
IS = sheet("IS annual"); BS = sheet("BS annual"); CF = sheet("CF annual")
ISQ = sheet("IS quarterly"); BSQ = sheet("BS quarterly")
FY = {y: f"FY (ended {y}-12-31)" for y in (2010, 2011, 2012, 2013)}
REV = IS["Total revenues"]; DO = IS["Direct operating"]; DEP = IS["Depreciation of revenue earning equipment and lease charges"]
SGA = IS["Selling, general and administrative"]; PTI = IS["Income before income taxes"]
AP = BS["Accounts payable"]; REC = BS["Receivables, less allowance for doubtful accounts of $30.8 and $29.3"]
CARS = BS["Cars"]; OTH = BS["Other equipment"]
pti13 = PTI[FY[2013]]; assert pti13 == 663.1
rev13 = REV[FY[2013]]; rev12 = REV[FY[2012]]

print("\n== Pack phrases the K items rest on ==")
on_page(A13, "11", "our approximate average holding period for a rental car was eighteen months in the United States and thirteen months in our international operations")
on_page(A12, "11", "our approximate average holding period for a rental car was eighteen months in the United States and fourteen months in our international operations")
on_page(A12, "81", "Useful lives are as follows:"); on_page(A12, "81", "Cars | 4 to 28 months")
on_page(A13, "91", "Holding periods are as follows:"); on_page(A13, "91", "Cars | 4 to 36 months")
on_page(A13, "53", "vehicle maintenance costs of $9.6 million due to the expansion of our off-airport and leisure businesses, longer holding periods and the impact of recalls")
on_page(A13, "126", "optimization of fleet holding periods related to the integration of Dollar Thrifty")
on_page(A13, "42", "optimization of fleet holding periods related to the integration of Dollar Thrifty")
on_page(A13, "126", "The cumulative effect of the reduction in rates was also indicative of the residual values experienced in the U.S.")
on_page(A12, "113", "indicative of the strong residual values experienced in the U.S.")
on_page(A13, "126", "net losses of $48.2 million, and net gains of $100.6 million and $114.9 million")
on_page(A13, "126", "declining residual values from falling demand for used vehicles")
on_page(A13, "126", "net decreases of $44.2 million, $139.4 million and $26.7 million")
on_page(A13, "126", "net increases of $5.0 million, $8.8 million and $12.9 million")
on_page(A13, "43", "a decrease of $0.4 million, an increase of $0.5 million")
on_page(A13, "54", "a deterioration in the used vehicle residual values")
on_page(A13, "42", "we have decreased the percentage of program cars"); on_page(A13, "42", "this strategy remains flexible")
on_page(A12, "41", "we expect this percentage to continue to decrease")
on_page(A13, "42", "Percentage of non-program cars in our U.S. car rental operations | 91% | 95% | 83%")
on_page(A13, "43", "Percentage of non-program cars in our international car rental operations | 76% | 79% | 75%")
on_page(A13, "42", "it is expected that the average age of our fleet will increase")
on_page(A12, "42", "We believe the residual values have remained fairly stronger")
on_page(A12, "42", "due to improved residual values in the U.S.")
on_page(A13, "64", "due to the timing of our payments"); on_page(A12, "60", "due to the timing of our payments")
on_page(A13, "50", "certain one-time charges and nonoperational items"); on_page(A13, "140", "$645.4 million")
on_page(A13, "140", "Additional efficiency and cost saving initiatives are being developed")
on_page(A13, "83", "out of period errors totaling $46.3 million"); on_page(A13, "83", "would have been material to the fourth quarter")
on_page(A13, "159", "Oracle general ledger, accounts payable"); on_page(A13, "150", "unknowingly not being met")
on_page(A13, "137", "could potentially exceed $40.0 million"); on_page(A13, "93", "two to fifteen years")
on_page(A13, "99", "Customer relationships | 16 | $65.0"); on_page(A13, "99", "Trademark | 20 | 7.0")
on_page(A12, "81", "Other intangible assets | 3 to 20 years"); on_page(A13, "91", "Other intangible assets | 3 to 10 years")
on_page(A13, "50", "Advantage sublease revenue | (65.0)"); on_page(A13, "24", "9,000")
on_page(R13, "2", "lower than expected pricing and higher expenses related to carrying extra fleet")
on_page(R12, "4", "$1.82 - $1.92"); on_page(R13, "4", "$1.63")
on_page(A13, "45", "industry residual value guidebooks"); on_page(A13, "45", "Depreciation rates are adjusted prospectively")
on_page(A13, "45", "relatively minor"); on_page(A13, "45", "based on rental volume and actuarial evaluations")
on_page(A13, "15", "average age of HERC's worldwide rental fleet was 43 months"); on_page(A13, "98", "nine years")
on_page(A13, "96", "Trade name | 3,330.0"); on_page(A13, "95", "$1,347.5"); on_page(A13, "70", "2,727.7"); on_page(A13, "70", "4,757.6")
on_page(A13, "98", "Accounts payable | (43)"); on_page(A13, "99", "10,197.4")
on_page(A13, "158", "Year ended December 31, 2013 | $29.3 | $41.9 | $(0.1) | $(40.3)")
on_page(A12, "140", "$25,113"); on_page(A13, "80", "Provision for losses on doubtful accounts | 45.9")
on_page(A13, "81", "Purchases of revenue earning equipment included in accounts payable and accrued liabilities | $289.1 | $247.0")
on_page(A13, "81", "Sales of revenue earning equipment included in receivables | 357.3 | 618.6")
on_page(A13, "81", "Purchases of property and equipment included in accounts payable | 55.6")
on_page(A13, "75", "Accounts payable | $967.9 | $1,003.2"); on_page(A13, "75", "1,512.6 | 1,879.7"); on_page(A13, "75", "Cars | 14,456.6 | 12,548.8")
on_page(A13, "76", "Direct operating | 5,752.0 | 4,806.0"); on_page(A13, "84", "Income before income taxes | 450.6 | (9.2) | 441.4 | 324.3 | (18.7) | 305.6")
on_page(A13, "87", "612.4 | (11.6) | 600.8"); on_page(A13, "57", "47.8%")
on_page(A13, "50", "Premiums paid on debt(9) | (28.7) |"); on_page(A13, "50", "Other(11) | (50.7) | (44.0)")
on_page(R13, "5", "$39.4 million in expenses related to the loss on conversion"); on_page(R13, "5", "Restructuring and related charges | 98.8 | 49.1")
on_page(R12, "4", "Restructuring and related charges | 49.1 | 66.2"); on_page(R12, "4", "Adjusted pre-tax income | 901.5 | 901.5 | 680.5")
on_page(R13, "4", "$1,153.2 million, an increase of 29.2% from prior year amount of $892.3 million")
on_page(R13, "unnumbered", "Total revenues | $2,556.3 | $2,319.7"); on_page(R13, "unnumbered", "Direct operating | 1,439.3 | 1,257.7")
on_page(R13, "unnumbered", "Depreciation of revenue earning equipment and lease charges | 643.0 | 550.0")
on_page(R13, "unnumbered", "Depreciation of revenue earning equipment | 333.4 | 102.0 | 75.7 | 109.1 | 620.2 | 245.9 | 111.9 | 73.9 | 102.1 | 533.8")
on_page(R13, "unnumbered", "Average number of cars (Company-operated) | 472,200 | 22.4%"); on_page(R13, "unnumbered", "Transaction days (in thousands) (a) | 32,875 | 16.1%")
on_page(R13, "unnumbered", "Total RPD (b) | $44.91 | (1.4)%"); on_page(R13, "1", "Fourth quarter GAAP pre-tax income of $62.3 million")
on_page(A13, "131", "U.S. car rental | $1,269.3 | $940.6"); on_page(A13, "131", "International car rental | 532.0 | 528.2")
on_page(A13, "49", "Average number of cars (Company-operated) | 468,500 | 358,000"); on_page(A13, "49", "Average number of cars (Leased) | 21,500 | 1,100")
on_page(A13, "49", "Average number of cars (Company-operated) | 159,700 | 153,700"); on_page(A13, "49", "Average number of cars (Leased) | 1,600 | 1,400")
on_page(A13, "42", "197,700, 136,400 and 121,800"); on_page(A13, "96", "Concession rights | 411.3 | (49.5)"); on_page(A13, "96", "Concession rights | 406.0 | (5.0)")
on_page(A13, "126", "Depreciation of revenue earning equipment | $2,407.8 | $2,145.9 | $1,912.3"); on_page(A12, "113", "Depreciation of revenue earning equipment | $2,165.2 | $1,921.8")
on_page(A13, "126", "Adjustment of depreciation upon disposal of revenue earning equipment | 37.2 | (96.8)")

# ---------- 1. rental depreciation rate (numbers-1, numbers-2, report-5) ----------
print("\n== 1. Rental equipment depreciation rate: Note 8 charge over average gross cars plus other equipment ==")
gross = {y: CARS[FY[y]] + OTH[FY[y]] for y in (2010, 2011, 2012, 2013)}
gross12_rev = 12548.8 + 3240.1           # p. 75 revised FY2012
note8 = {2011: 1921.8, 2012: 2165.2, 2013: 2407.8}   # FY2012 p. 113; FY2013 p. 126
note8_12_rev = 2145.9                     # FY2013 p. 126
avg = lambda a, b: (a + b) / 2
r11 = note8[2011] / avg(gross[2010], gross[2011]) * 100
r12 = note8[2012] / avg(gross[2011], gross[2012]) * 100
r13_first = note8[2013] / avg(gross[2012], gross[2013]) * 100
r12_rev = note8_12_rev / avg(gross[2011], gross12_rev) * 100
r13_rev = note8[2013] / avg(gross12_rev, gross[2013]) * 100
check("numbers-1 FY2011 rate 16.2", 16.2, r11)
check("numbers-1 FY2012 rate 15.3", 15.3, r12)
check("numbers-1 FY2013 rate 14.3 (first-reported base gives 14.2; revised base 14.3)", 14.3, r13_rev, note=f"first-reported base {r13_first:.2f}")
check("numbers-2 FY2012 revised 15.2", 15.2, r12_rev)
check("numbers-2 FY2013 revised 14.3", 14.3, r13_rev)
not_taken_first = (r12 - r13_first) / 100 * avg(gross[2012], gross[2013])
not_taken_rev = (r12_rev - r13_rev) / 100 * avg(gross12_rev, gross[2013])
check("numbers-1 charge not taken $174.5m", 174.5, not_taken_first, tol=0.3)
check("numbers-1 26% of pre-tax", 26, not_taken_first / pti13 * 100, tol=0.5)
check("numbers-2 / report-5 charge not taken $152.1m", 152.1, not_taken_rev, tol=0.3)
check("report-5 ranks on 22.9%", 22.9, not_taken_rev / pti13 * 100, tol=0.1)
check("numbers-2 $39.6m net rate changes = 26% of $152.1m", 26, 39.6 / not_taken_rev * 100, tol=0.5)
check("numbers-2 $39.6m = 1.6% of $2,407.8m", 1.6, 39.6 / 2407.8 * 100)
print("  Q4 same-quarter rate: NOT computed by the run. Scorer's figure from the release line 620.2 / 533.8 and quarterly gross fleet:")
q = lambda c: BSQ[c]
g = lambda col: BSQ["Cars"][col] + BSQ["Other equipment"][col]
q4_13 = 620.2 / avg(g("Q3 (ended 2013-09-30)"), g("Q4 (ended 2013-12-31)")) * 365 / 92 * 100
q4_12 = 533.8 / avg(g("Q3 (ended 2012-09-30)"), g("Q4 (ended 2012-12-31)")) * 366 / 92 * 100
print(f"    Q4 2012 {q4_12:.1f}%  Q4 2013 {q4_13:.1f}% (days-annualised), computable from the pack (AK12)")

# ---------- 2. stated rate changes, disposal swing, shares (text-3, text-4, numbers-2, report-5) ----------
print("\n== 2. Stated rate changes and disposal results as shares of pre-tax income ==")
check("$44.2m = 6.7%", 6.7, 44.2 / pti13 * 100)
check("$48.2m = 7.3%", 7.3, 48.2 / pti13 * 100)
check("net $39.6m = 44.2 - 5.0 + 0.4", 39.6, 44.2 - 5.0 + 0.4)
check("$39.6m = 6%", 6, 39.6 / pti13 * 100, tol=0.5)
check("2012 net $130.1m = 139.4 - 8.8 - 0.5", 130.1, 139.4 - 8.8 - 0.5)
check("2012 net as 29% of revised pre-tax 441.4", 29, 130.1 / 441.4 * 100, tol=0.6)
check("U.S. swing $148.8m", 148.8, 100.6 + 48.2)
check("swing 22.4% of pre-tax", 22.4, 148.8 / pti13 * 100)
check("text-4 international -$5.0m = 0.8%", 0.8, 5.0 / pti13 * 100)
check("text-4 equipment +$0.4m = 0.1%", 0.1, 0.4 / pti13 * 100)
check("text-4 top of car range +29%", 29, (36 - 28) / 28 * 100, tol=0.6)

# ---------- 3. per-vehicle depreciation and the holding-period proxies (text-4) ----------
print("\n== 3. text-4 statements-table arithmetic ==")
us13, us12 = 1269.3, 940.6; intl13, intl12 = 532.0, 528.2
check("U.S. per vehicle incl. leased 2012 $218.3", 218.3, us12 / (358.0 + 1.1) / 12 * 1000, tol=0.06)
check("U.S. per vehicle incl. leased 2013 $215.9", 215.9, us13 / (468.5 + 21.5) / 12 * 1000, tol=0.06)
check("change -1.1%", -1.1, (us13 / 490.0) / (us12 / 359.1) * 100 - 100)
check("company-operated 2012 $218.9", 218.9, us12 / 358.0 / 12 * 1000, tol=0.06)
check("company-operated 2013 $225.8", 225.8, us13 / 468.5 / 12 * 1000, tol=0.06)
check("company-operated +3.1%", 3.1, (us13 / 468.5) / (us12 / 358.0) * 100 - 100)
check("international per vehicle 2012 $283.8", 283.8, intl12 / (153.7 + 1.4) / 12 * 1000, tol=0.06)
check("international per vehicle 2013 $274.9", 274.9, intl13 / (159.7 + 1.6) / 12 * 1000, tol=0.06)
car_rate_12 = (us12 + intl12) / avg(CARS[FY[2011]], CARS[FY[2012]]) * 100
car_rate_13 = (us13 + intl13) / avg(12548.8, CARS[FY[2013]]) * 100
check("car depreciation incl. lease charges over avg gross cars 2012 13.2%", 13.2, car_rate_12)
check("same 2013 13.3%", 13.3, car_rate_13)
# implied U.S. non-program holding: average fleet x average non-program share / non-program cars sold x 12
hp12 = 358000 * (0.83 + 0.95) / 2 / 136400 * 12
hp13 = 468500 * (0.95 + 0.91) / 2 / 197700 * 12
check("implied U.S. non-program holding 2012 28.0 months (average of year-end shares)", 28.0, hp12)
check("implied 2013 26.4 months", 26.4, hp13)
print(f"    (on the year-end share alone: {358000*0.95/136400*12:.1f} and {468500*0.91/197700*12:.1f}; p. 42 attributes the 44.9% rise in cars sold to Dollar Thrifty)")
check("P&E depreciation over year-end gross 2012 6.8%", 6.8, CF["Depreciation of property and equipment"][FY[2012]] / BS["Total property and equipment, at cost"][FY[2012]] * 100)
check("same 2013 7.9%", 7.9, CF["Depreciation of property and equipment"][FY[2013]] / BS["Total property and equipment, at cost"][FY[2013]] * 100)
check("HERC accumulated depreciation over gross 2012 32.2%", 32.2, 1041.9 / 3240.1 * 100)
check("same 2013 31.2%", 31.2, 1095.8 / 3512.2 * 100)
check("concession implied life 9.2 years (411.3 / (49.5 - 5.0))", 9.2, 411.3 / (49.5 - 5.0))
check("accident reserve +4.7%", 4.7, (347.7 / 332.2 - 1) * 100)
check("reported revenue +19.4%", 19.4, (rev13 / 9024.9 - 1) * 100)
check("reserve 3.26% of pro forma 2012 revenue", 3.26, 332.2 / 10197.4 * 100, tol=0.006)
check("reserve 3.23% of 2013 revenue", 3.23, 347.7 / rev13 * 100, tol=0.006)

# ---------- 4. allowance (numbers-1, text-3, numbers-2) ----------
print("\n== 4. Allowance for doubtful accounts ==")
allow = {2010: 19.708, 2011: 20.282, 2012: 25.113, 2013: 30.8}   # FY2012 Schedule II (thousands) p. 140; FY2013 p. 158
for y, rep in ((2010, 1.4), (2011, 1.2), (2012, 1.3), (2013, 2.0)):
    check(f"allowance % of gross receivables FY{y} {rep}", rep, allow[y] / (REC[FY[y]] + allow[y]) * 100)
check("text-3 allowance covers 0.76 years of write-offs (30.8 / 40.3)", 0.76, 30.8 / 40.3, tol=0.006)
check("text-3 tie-out gap 45.9 - 41.9 = 4.0", 4.0, 45.9 - 41.9)
check("numbers-2 allowance rose 29.3 to 30.8 (revised 2012)", 1.5, 30.8 - 29.3)

# ---------- 5. adjusted measures (numbers-2, text-3, text-4, report-5) ----------
print("\n== 5. Adjusted pre-tax income ==")
check("FY2013 gap $490.1m = 74%", 74, 490.1 / pti13 * 100, tol=0.5)
check("73.9%", 73.9, 490.1 / pti13 * 100)
check("FY2012 gap $450.9m = 102% revised", 102, 450.9 / 441.4 * 100, tol=0.5)
check("FY2012 gap 100% first reported", 100, 450.9 / 450.6 * 100, tol=0.5)
check("FY2011 gap $356.2m", 356.2, 680.5 - 324.3)
check("FY2011 110%", 110, 356.2 / 324.3 * 100, tol=0.5)
check("restructuring plus related $98.8m = 14.9%", 14.9, 98.8 / pti13 * 100)
check("restructuring 2011 to 2013 from Note 14: 56.4 + 38.0 + 77.0", 171.4, 56.4 + 38.0 + 77.0)
check("seven-year average $92.2m", 92.2, 645.4 / 7)
new5 = 40.0 + 44.0 + 39.4 + 28.7 + 7.8
check("five new add-backs $159.9m", 159.9, new5)
check("24.1% (text-4, report-5 ranks on)", 24.1, new5 / pti13 * 100)
new4 = 40.0 + 44.0 + 28.7 + 7.8
print(f"    note: $39.4m sits inside 'Other' (p. 50: 50.7 in 2013, 44.0 in 2012; release p. 5 fn (g)); the four line items absent in 2012 total {new4:.1f} = {new4/pti13*100:.1f}%; premiums were taken in 2011 (62.4)")
check("text-3 restructuring + purchase accounting + debt charges = 45.2%", 45.2, (98.8 + 132.2 + 68.4) / pti13 * 100)
check("adjusted growth 29.2% on 892.3", 29.2, (1153.2 / 892.3 - 1) * 100)
check("27.9% on 901.5", 27.9, (1153.2 / 901.5 - 1) * 100)
check("1 point of tax on 1,153.2 = $11.5m", 11.5, 1153.2 * 0.01)
check("effective tax rate 47.8%", 47.8, 316.9 / pti13 * 100)
check("report-5 $44.0m Simply Wheelz = 6.6%", 6.6, 44.0 / pti13 * 100)

# ---------- 6. error corrections (numbers-1, text-3, text-4, report-5) ----------
print("\n== 6. Error corrections ==")
check("2011 pre-tax cut 18.7 = 5.8%", 5.8, 18.7 / 324.3 * 100)
check("2011 net income cut 12.0 = 6.1% (p. 84: 195.8 to 183.8)", 6.1, 12.0 / 195.8 * 100)
check("numbers-1 2011 net income fell 11.9 (workbook 195.7)", 11.9, IS["Net income"][FY[2011]] - 183.8)
check("2012 errors 2.0% (9.2 / 450.6)", 2.0, 9.2 / 450.6 * 100)
check("numbers-1 2012 cut 9.1 (workbook 450.5; PK10)", 9.1, PTI[FY[2012]] - 441.4)
check("$46.3m = 7.0%", 7.0, 46.3 / pti13 * 100)
check("2013 portion 11.6 = 612.4 - 600.8", 11.6, 612.4 - 600.8)
check("1.7% (11.6 / 663.1 = 1.749)", 1.7, 11.6 / pti13 * 100, tol=0.051)
check("prior-year 34.7 = 46.3 - 11.6", 34.7, 46.3 - 11.6)
check("34.7 = 56% of Q4 pre-tax 62.3", 56, 34.7 / 62.3 * 100, tol=0.5)
check("equity cut 21.1", 21.1, 2507.3 - 2486.2)
check("Q4 2012 pre-tax loss 40.3 to 43.1 (workbook derived; release)", -40.3, ISQ["Income before income taxes"]["Q4 (ended 2012-12-31)"])

# ---------- 7. payables (numbers-1, numbers-2, report-5) ----------
print("\n== 7. Payables ==")
cost13 = DO[FY[2013]] + DEP[FY[2013]]; cost12 = DO[FY[2012]] + DEP[FY[2012]]; cost12_rev = 4806.0 + 2128.9
dp13 = AP[FY[2013]] / cost13 * 365; dp12 = AP[FY[2012]] / cost12 * 366; dp12_rev = 1003.2 / cost12_rev * 366
check("days payable FY2013 42.7", 42.7, dp13); check("FY2012 52.7 (366-day year)", 52.7, dp12); check("FY2012 revised 52.9", 52.9, dp12_rev)
check("Q4 2013 42.8", 42.8, AP[FY[2013]] / (1439.3 + 643.0) * 92); check("Q4 2012 50.8", 50.8, 999.1 / (1257.7 + 550.0) * 92)
check("payables fell 3% first reported", -3.1, (AP[FY[2013]] / AP[FY[2012]] - 1) * 100); check("fell 3.5% revised", -3.5, (967.9 / 1003.2 - 1) * 100)
check("cost rose 19% first reported", 19.2, (cost13 / cost12 - 1) * 100); check("19.4% revised", 19.4, (cost13 / cost12_rev - 1) * 100)
check("size $226.3m at FY2012 days", 226.3, dp12 / 365 * cost13 - AP[FY[2013]], tol=0.3); check("34% of pre-tax", 34, 226.3 / pti13 * 100, tol=0.5)
check("revised size $232.8m", 232.8, dp12_rev / 365 * cost13 - 967.9, tol=0.3)
check("Dollar Thrifty $43m = 18% of 232.8", 18, 43 / 232.8 * 100, tol=0.6)
check("direct operating days 76.4 to 61.4 (revised 2012)", 76.4, 1003.2 / 4806.0 * 366); check("61.4", 61.4, 967.9 / DO[FY[2013]] * 365)
check("cash-flow gap 23.2 + 35.3 = 58.5", 58.5, 23.2 + (1003.2 - 967.9))
check("industry gap $483.2m", 483.2, AP[FY[2013]] - 0.045 * rev13, tol=0.2); check("73% of pre-tax", 73, 483.2 / pti13 * 100, tol=0.5)
check("property purchases 55.6 = 12% of gap", 12, 55.6 / 483.2 * 100, tol=0.5); check("plus fleet 289.1 = 71%", 71, (55.6 + 289.1) / 483.2 * 100, tol=0.5)
check("payables ex both = 5.8% of sales", 5.8, (AP[FY[2013]] - 55.6 - 289.1) / rev13 * 100)
check("payables 9.0% of sales", 9.0, AP[FY[2013]] / rev13 * 100)

# ---------- 8. receivables (numbers-1, numbers-2, report-5) ----------
print("\n== 8. Receivables ==")
check("DSO FY2013 51.3", 51.3, REC[FY[2013]] / rev13 * 365); check("DSO FY2012 76.5", 76.5, REC[FY[2012]] / rev12 * 366)
check("Q4 DSO 54.4", 54.4, REC[FY[2013]] / 2556.3 * 92); check("Q4 2012 74.8", 74.8, REC[FY[2012]] / 2319.7 * 92)
check("receivables 14.0% of sales", 14.0, REC[FY[2013]] / rev13 * 100); check("industry gap $273.8m", 273.8, REC[FY[2013]] - 0.115 * rev13, tol=0.2)
check("41% of pre-tax", 41, 273.8 / pti13 * 100, tol=0.5)
check("ex fleet sales 10.7% of sales", 10.7, (REC[FY[2013]] - 357.3) / rev13 * 100)
check("fleet-sale receivables fell $261.3m", 261.3, 618.6 - 357.3); check("total fall $367.1m (revised 2012)", 367.1, 1879.7 - REC[FY[2013]])
check("71%", 71, 261.3 / 367.1 * 100, tol=0.5)
check("receivables growth less revenue growth FY2013 -39.2pp", -39.2, (REC[FY[2013]] / REC[FY[2012]] - 1) * 100 - (rev13 / rev12 - 1) * 100)

# ---------- 9. Q4 gross margin (numbers-1, numbers-2, report-5) ----------
print("\n== 9. Q4 gross margin from the release ==")
gm13 = (2556.3 - 1439.3 - 643.0) / 2556.3 * 100; gm12 = (2319.7 - 1257.7 - 550.0) / 2319.7 * 100
check("Q4 2013 18.5%", 18.5, gm13); check("Q4 2012 22.1%", 22.1, gm12)
size = (gm12 - gm13) / 100 * 2556.3
check("size $90.2m", 90.2, size, tol=0.2); check("14% of pre-tax (13.6 rounded)", 14, size / pti13 * 100, tol=0.5)
dep_share = (643.0 / 2556.3 - 550.0 / 2319.7) * 2556.3; do_share = (1439.3 / 2556.3 - 1257.7 / 2319.7) * 2556.3
check("depreciation 41% of the fall", 41, dep_share / size * 100, tol=0.6); check("direct operating 59%", 59, do_share / size * 100, tol=0.6)
check("FY2013 gross margin 23.2%", 23.2, (rev13 - cost13) / rev13 * 100)
check("FY2013 operating margin 13.7%", 13.7, (rev13 - cost13 - SGA[FY[2013]]) / rev13 * 100)
check("capital spending over depreciation 1.25 (net fleet and property capex over Note 8 plus P&E depreciation)", 1.25,
      (10298.4 - 7264.1 + 313.8 - 73.0) / (2407.8 + 205.3))

# ---------- 10. balances and exposures (text-3, report-5) ----------
print("\n== 10. Balances and exposures ==")
check("goodwill plus trade name $4,677.5m", 4677.5, 1347.5 + 3330.0)
check("1.69x total equity 2,771.2", 1.69, 4677.5 / 2771.2, tol=0.006)
check("Nevada $40.0m = 6.0%", 6.0, 40.0 / pti13 * 100)
check("3.1 executive residences on p. 147 (text)", 3.1, 3.1)
check("purchase obligations 4,757.6 of which fleet 4,457.5 (p. 70)", 4757.6, 4757.6)
check("leases and concessions 2,727.7 (p. 70)", 2727.7, 2727.7)

# ---------- hit list recount (text-4 section 3) ----------
print("\n== text-4 hit list recount (pages by year) ==")
def hits(doc, term):
    out = {}
    for p, t in doc.items():
        n = len(re.findall(term, t, re.I))
        if n: out[p] = n
    return out
for term, rep12, rep13 in (("residual", 43, 46), ("holding period", 10, 15), ("useful li", 16, 16), ("average", 61, 69), ("salvage", 0, 0)):
    h12, h13 = hits(A12, term), hits(A13, term)
    print(f"  {term!r}: FY2012 {sum(h12.values())} (reply {rep12}) pages {sorted(h12, key=lambda x: int(x) if x.isdigit() else -1)}")
    print(f"  {term!r}: FY2013 {sum(h13.values())} (reply {rep13}) pages {sorted(h13, key=lambda x: int(x) if x.isdigit() else -1)}")

# ---------- trap and banned-word scan ----------
print("\n== Reply scan ==")
terms = ["fraud", "manipulat", "red flag", "misstat", "restat", "material weakness", "planned holding", "21 to", "25 months", "24 or 30",
         "affirmative", "attorney", "subrogat", "rolling", "spreadsheet", "9.3", "235", "tone at the top", "Estero", "penalty", "disposed",
         "improved residual", "1.82", "eighteen", "ranks on", "2014", "Oracle", "weakness"]
for fn in ("numbers-1.md", "numbers-2.md", "text-3.md", "text-4.md", "report-5.md"):
    txt = open(os.path.join(RUN, fn), encoding="utf-8").read()
    found = {t: len(re.findall(re.escape(t), txt, re.I)) for t in terms}
    found = {k: v for k, v in found.items() if v}
    print(f"  {fn}: {found}; em-dashes {txt.count(chr(8212))}")

n_ok = sum(1 for r in results if r[3]); print(f"\n== {n_ok} of {len(results)} sub-figures match ==")
for r in results:
    if not r[3]: print("  DIFF:", r)
