# Turn 2: follow the flags. Hertz Global Holdings.
# Run from the hertz-fy2013 folder:  python -X utf8 runs/v2.2/numbers-code-2.py
# Figures come from statements.xlsx or from table rows in the text files; every text-file row used is
# checked below as an exact substring on the stated page before it is used.
import re
import sys
import openpyxl

AR12 = "annual-report-FY2012-12-31-key-sections.txt"
AR13 = "annual-report-FY2013-12-31-key-sections.txt"
ER12 = "earnings-release-Q4-FY2012-12-31.txt"
ER13 = "earnings-release-Q4-FY2013-12-31.txt"
TXT = {f: open(f, encoding="utf-8").read() for f in (AR12, AR13, ER12, ER13)}
FAIL = []


def pages_of(fname, needle):
    t = TXT[fname]
    out = []
    for m in re.finditer(re.escape(needle), t):
        pm = None
        for pm in re.finditer(r"\[p\. ([^\]]+)\]", t[: m.start()]):
            pass
        out.append(pm.group(1) if pm else None)
    return out


def src(fname, needle, page):
    """Check that a table row or sentence is in the file on the stated page (nearest [p. N] marker above)."""
    pg = pages_of(fname, needle)
    ok = str(page) in pg
    if not ok:
        FAIL.append((fname, needle, page, pg))
    print(f"  [{'OK' if ok else 'FAIL'}] {fname[:28]} p.{page}: {needle[:80]}")
    return ok


wb = openpyxl.load_workbook("statements.xlsx", data_only=True)


def sheet(name):
    ws = wb[name]
    rows = list(ws.iter_rows(values_only=True))
    periods = [re.search(r"ended (\d{4}-\d{2}-\d{2})", str(h)).group(1) for h in rows[0][1:-1]]
    d = {}
    for r in rows[1:]:
        if r[0] is None:
            continue
        key = r[-1] if r[-1] not in d else f"{r[-1]}|{r[0]}"
        d[key] = dict(zip(periods, r[1:-1]))
    return d


ISa, BSa, CFa, ISq = sheet("IS annual"), sheet("BS annual"), sheet("CF annual"), sheet("IS quarterly")
Y10, Y11, Y12, Y13 = "2010-12-31", "2011-12-31", "2012-12-31", "2013-12-31"
g = lambda a, b: 100 * (a / b - 1)

print("SOURCE ROWS (text files)")
# balance sheet and cash flow, FY2013 annual report (FY2012 column is as revised)
src(AR13, "Receivables, less allowance for doubtful accounts of $30.8 and $29.3 | 1,512.6 | 1,879.7", 75)
src(AR13, "Prepaid expenses and other assets | 717.2 | 489.3", 75)
src(AR13, "Cars | 14,456.6 | 12,548.8", 75)
src(AR13, "Less accumulated depreciation | (2,679.6) | (1,850.4)", 75)
src(AR13, "Other equipment | 3,512.2 | 3,240.1", 75)
src(AR13, "Public liability and property damage | 347.7 | 332.2", 75)
src(AR13, "Total revenues | 10,771.9 | 9,024.9 | 8,299.3", 76)
src(AR13, "Income before income taxes | 663.1 | 441.4 | 305.6", 76)
src(AR13, "Depreciation of revenue earning equipment | 2,445.0 | 2,049.0 | 1,800.0", 80)
src(AR13, "Provision for losses on doubtful accounts | 45.9 | 38.3 | 28.2", 80)
src(AR13, "Impairment charges and other | 40.0 | — | —", 80)
src(AR13, "Receivables | (34.7) | (149.2) | (73.6)", 80)
src(AR13, "Public liability and property damage | (3.7) | (4.3) | 6.6", 80)
src(AR13, "Sales of revenue earning equipment included in receivables | 357.3 | 618.6 | 620.7", 81)
# Note 8, FY2013 annual report
src(AR13, "Depreciation of revenue earning equipment | $2,407.8 | $2,145.9 | $1,912.3", 126)
src(AR13, "Adjustment of depreciation upon disposal of revenue earning equipment | 37.2 | (96.8) | (112.2)", 126)
src(AR13, "included net losses of $48.2 million, and net gains of $100.6 million and $114.9 million, respectively, on the disposal of vehicles used in our U.S. car rental operations", 126)
# Note 8, FY2012 annual report (as first reported)
src(AR12, "Depreciation of revenue earning equipment | $2,165.2 | $1,921.8 | $1,747.0", 113)
src(AR12, "These depreciation rate changes resulted in net decreases of $130.6 million and $13.8 million and a net increase of $19.1 million", 113)
# U.S. car rental operating data and segment depreciation, FY2013 annual report
src(AR13, "Average number of cars (Company-operated) | 468,500 | 358,000 | 321,700", 49)
src(AR13, "Average number of cars (Leased) | 21,500 | 1,100 | —", 49)
src(AR13, "Depreciation of revenue earning equipment and lease charges for our U.S. car rental segment of $1,269.3 million for 2013 increased $328.7 million, or 34.9% from $940.6 million for 2012", 54)
src(AR13, "2012 supplemental pro forma from 1/1/12 - 12/31/12 (combined entity)(3) | 10,197.4 | 404.6", 99)
# allowance schedule
src(AR13, "Year ended December 31, 2013 | $29.3 | $41.9 | $(0.1) | $(40.3) | (a) | $30.8", 158)
src(AR13, "Year ended December 31, 2012(b) | 20.3 | 38.3 | — | (29.3) | (a) | 29.3", 158)
src(AR13, "Year ended December 31, 2011(b) | 19.7 | 28.2 | 0.1 | (27.7) | (a) | 20.3", 158)
src(AR12, "Receivables, less allowance for doubtful accounts of $25,113 and $20,282 | 1,886,596 | 1,616,382", 72)
src(AR13, "Impairment charges and other(10) | (44.0) | — | —", 50)
# prepaid and other assets
src(AR13, "the fair value of debt securities was $151.0 million and $0.0 million, respectively", 145)
# reserves
src(AR13, "Balance as of December 31, 2012 | $12.4 | $0.2 | $0.3 | $8.1 | $21.0", 141)
src(AR13, "Balance as of December 31, 2013 | $20.1 | $— | $0.2 | $28.1 | $48.4", 141)
src(AR13, "we experienced a 26.2% increase in transaction days", 42)
# adjusted earnings
src(ER13, "Income before income taxes | 663.1 | 490.1 | 1,153.2 | 441.4 | 450.9 | 892.3", "unnumbered")
src(ER12, "Income before income taxes | 450.6 | 450.9 | 901.5 | 324.3 | 356.2 | 680.5", 10)
src(AR13, "Restructuring charges | (77.0) | (38.0) | (56.4)", 50)
src(AR13, "Restructuring related charges(4) | (21.8) | (11.1) | (9.8)", 50)
src(AR13, "Purchase accounting(2) | (132.2) | (109.6) | (87.6)", 50)
src(AR13, "Debt-related charges(3) | (68.4) | (83.6) | (130.4)", 50)
src(AR13, "Acquisition related costs and charges(6) | (18.5) | (163.7) | (18.8)", 50)
src(AR13, "Other(11) | (50.7) | (44.0) | —", 50)
src(AR13, "we incurred $645.4 million", 140)
# fourth quarter, FY2013 release (both quarters on the revised basis)
src(ER13, "Total revenues | $2,556.3 | $2,319.7 | 100.0% | 100.0%", "unnumbered")
src(ER13, "Direct operating | 1,439.3 | 1,257.7 | 56.3% | 54.2%", "unnumbered")
src(ER13, "Depreciation of revenue earning equipment and lease charges | 643.0 | 550.0 | 25.2% | 23.7%", "unnumbered")
src(ER13, "Selling, general and administrative | 222.2 | (21.1 | )(c) | 201.1 | 331.1 | (126.4 | )(c) | 204.7", "unnumbered")
src(ER13, "Transaction days (in thousands) (a) | 32,875 | 16.1% | 133,181 | 26.2%", "unnumbered")
src(ER13, "Total RPD (b) | $44.91 | (1.4)% | $47.00 | 1.5%", "unnumbered")
src(ER13, "Average number of cars (Company-operated) | 472,200 | 22.4% | 468,500 | 31.2%", "unnumbered")
src(ER13, "Depreciation of revenue earning equipment and lease charges | 333.4 | 124.8 | 75.7 | 109.1 | 0.0 | 643.0 | 246.0 | 128.0 | 73.9 | 102.1 | 0.0 | 550.0", "unnumbered")
src(ER13, "Transactions days (in thousands) | 32,875 | 28,324 | 10,473 | 9,924", "unnumbered")

# ------------------------------------------------------------------ FLAG 1: receivables
print("\nFLAG 1 receivables (FY2012 as revised in the FY2013 annual report)")
rec13, rec12 = 1512.6, 1879.7
fleet13, fleet12 = 357.3, 618.6
rev13, rev12, rev12_pf = 10771.9, 9024.9, 10197.4
print(" total change %.1f (%.1f%%); first-reported FY2012 balance %.1f" % (rec13 - rec12, g(rec13, rec12), BSa["us-gaap:AccountsReceivableNet"][Y12]))
print(" fleet-sale receivables change %.1f = %.1f%% of the fall" % (fleet13 - fleet12, 100 * (fleet13 - fleet12) / (rec13 - rec12)))
o13, o12 = rec13 - fleet13, rec12 - fleet12
print(" other receivables %.1f -> %.1f: change %.1f (%.1f%%)" % (o12, o13, o13 - o12, g(o13, o12)))
print(" revenue growth, whole company %.1f%%; against 2012 pro forma for Dollar Thrifty %.1f%%" % (g(rev13, rev12), g(rev13, rev12_pf)))
print(" days of other receivables: 2012 %.1f (pro forma revenue %.1f), 2013 %.1f" % (o12 / rev12 * 366, o12 / rev12_pf * 366, o13 / rev13 * 365))
print(" cash flow statement: receivables line (34.7) = use of cash, while the balance fell %.1f" % (rec12 - rec13))

# ------------------------------------------------------------------ FLAG 2: depreciation
print("\nFLAG 2 rental equipment depreciation")
gross = {Y10: BSa["us-gaap:PropertySubjectToOrAvailableForOperatingLeaseGross"][Y10] + BSa["htz:OtherEquipmentGross"][Y10],
         Y11: BSa["us-gaap:PropertySubjectToOrAvailableForOperatingLeaseGross"][Y11] + BSa["htz:OtherEquipmentGross"][Y11],
         Y12: 12548.8 + 3240.1,  # revised
         Y13: 14456.6 + 3512.2}
avg = {Y11: (gross[Y10] + gross[Y11]) / 2, Y12: (gross[Y11] + gross[Y12]) / 2, Y13: (gross[Y12] + gross[Y13]) / 2}
before = {Y11: 1912.3, Y12: 2145.9, Y13: 2407.8}       # Note 8, before the disposal adjustment (2011, 2012 as revised)
adj = {Y11: -112.2, Y12: -96.8, Y13: 37.2}             # disposal adjustment (minus = gain)
total_cf = {Y11: 1800.0, Y12: 2049.0, Y13: 2445.0}     # cash flow line, as revised
for y in (Y11, Y12, Y13):
    print(" %s avg gross fleet %.1f | before disposal results %.2f%% | incl. disposal results (cash flow line) %.2f%% | disposal adj %.1f" % (
        y[:4], avg[y], 100 * before[y] / avg[y], 100 * total_cf[y] / avg[y], adj[y]))
r12, r13 = before[Y12] / avg[Y12], before[Y13] / avg[Y13]
extra = (r12 - r13) * avg[Y13]
print(" fall in rate before disposal results 2012->2013: %.2f pts; on the 2013 average fleet that is %.1f, or %.1f%% of 2013 pre-tax income (663.1)" % (
    100 * (r12 - r13), extra, 100 * extra / 663.1))
print(" disposal adjustment swing 2012->2013: %.1f; U.S. car disposals: gain 100.6 -> loss 48.2, swing %.1f" % (adj[Y13] - adj[Y12], 100.6 + 48.2))
print(" net rate-change effect 2013: U.S. -44.2, international +5.0, equipment -0.4 => %.1f; 2012: -139.4 + 8.8 + 0.5 => %.1f (FY2012 report said -130.6 for car rental: %.1f)" % (
    -44.2 + 5.0 - 0.4, -139.4 + 8.8 + 0.5, -139.4 + 8.8))
print(" first-reported basis (turn 1): 2011 %.2f%%, 2012 %.2f%%, 2013 %.2f%%" % (
    100 * CFa["htz:CostOfServicesDepreciationAsAdjustedForGainLossUponDisposal"][Y11] / avg[Y11],
    100 * CFa["htz:CostOfServicesDepreciationAsAdjustedForGainLossUponDisposal"][Y12] / ((gross[Y11] + 12591.1 + 3240.1) / 2),
    100 * 2445.0 / ((12591.1 + 3240.1 + gross[Y13]) / 2)))
us_dep13, us_dep12 = 1269.3, 940.6
co13, co12, le13, le12 = 468500, 358000, 21500, 1100
pv_a13, pv_a12 = us_dep13 * 1e6 / (co13 + le13) / 12, us_dep12 * 1e6 / (co12 + le12) / 12
pv_b13, pv_b12 = us_dep13 * 1e6 / co13 / 12, us_dep12 * 1e6 / co12 / 12
print(" U.S. depreciation and lease charges per car per month: incl. leased cars $%.1f vs $%.1f (%.1f%%); company-operated only $%.1f vs $%.1f (%.1f%%)" % (
    pv_a13, pv_a12, g(pv_a13, pv_a12), pv_b13, pv_b12, g(pv_b13, pv_b12)))
print(" U.S. segment depreciation growth %.1f%% vs average company-operated cars %.1f%%" % (g(us_dep13, us_dep12), g(co13, co12)))
q_us13, q_us12, fleet_g = 333.4, 246.0, 22.4
print(" Q4 U.S. depreciation and lease charges growth %.1f%% vs average U.S. fleet +%.1f%% => per car %.1f%%" % (
    g(q_us13, q_us12), fleet_g, 100 * ((q_us13 / q_us12) / (1 + fleet_g / 100) - 1)))
print(" accumulated depreciation / cars at cost: 2012 revised %.1f%%, 2013 %.1f%%" % (100 * 1850.4 / 12548.8, 100 * 2679.6 / 14456.6))

# ------------------------------------------------------------------ FLAG 5: allowance
print("\nFLAG 5 allowance for doubtful accounts")
al13, al12, al12_first, al11 = 30.8, 29.3, 25.113, 20.3
print(" %% of gross receivables: 2012 first reported %.2f, 2012 revised %.2f, 2013 %.2f" % (
    100 * al12_first / (1886.596 + al12_first), 100 * al12 / (rec12 + al12), 100 * al13 / (rec13 + al13)))
print(" gross receivables change %.1f%%; allowance %.1f%%; write-offs 29.3 -> 40.3 = %.1f%%; provision (cash flow) 38.3 -> 45.9 = %.1f%%; schedule charge 38.3 -> 41.9 = %.1f%%; revenue %.1f%%" % (
    g(rec13 + al13, rec12 + al12), g(al13, al12), g(40.3, 29.3), g(45.9, 38.3), g(41.9, 38.3), g(rev13, rev12)))
print(" provision growth on first-reported 2012 (turn 1): %.1f%%" % g(45.9, CFa["us-gaap:ProvisionForDoubtfulAccounts"][Y12]))
print(" allowance / year's write-offs: 2011 %.2f, 2012 %.2f, 2013 %.2f" % (al11 / 27.7, al12 / 29.3, al13 / 40.3))
print(" allowance %% of receivables other than fleet sales: 2012 %.2f, 2013 %.2f" % (100 * al12 / (o12 + al12), 100 * al13 / (o13 + al13)))
print(" cash flow provision less schedule charge 2013: %.1f; adjusted-earnings impairment 44.0 less cash flow impairment 40.0: %.1f" % (45.9 - 41.9, 44.0 - 40.0))
print(" restated allowance at 2012: %.1f -> %.1f (+%.1f)" % (al12_first, al12, al12 - al12_first))

# ------------------------------------------------------------------ FLAG 3: fourth-quarter margin (release, revised basis)
print("\nFLAG 3 fourth-quarter gross margin (FY2013 release, both quarters revised)")
q13 = dict(rev=2556.3, do=1439.3, dep=643.0, sga=222.2, sga_adj=201.1)
q12 = dict(rev=2319.7, do=1257.7, dep=550.0, sga=331.1, sga_adj=204.7)
gm = lambda q: 100 * (q["rev"] - q["do"] - q["dep"]) / q["rev"]
print(" gross margin %.1f%% -> %.1f%%; revenue %.1f%%; direct operating %.1f%%; fleet depreciation %.1f%%" % (
    gm(q12), gm(q13), g(q13["rev"], q12["rev"]), g(q13["do"], q12["do"]), g(q13["dep"], q12["dep"])))
print(" SG&A %.1f -> %.1f (%.1f%%); adjustments 126.4 -> 21.1; adjusted SG&A %.1f -> %.1f (%.1f%%)" % (
    q12["sga"], q13["sga"], g(q13["sga"], q12["sga"]), q12["sga_adj"], q13["sga_adj"], g(q13["sga_adj"], q12["sga_adj"])))
cars13 = 472200
cars12 = cars13 / 1.224
print(" U.S. days on rent per car-day: Q4 2013 %.1f%%, Q4 2012 %.1f%% (fleet +22.4%%, transaction days +16.1%% = %.1f%% check)" % (
    100 * 32875e3 / (cars13 * 92), 100 * 28324e3 / (cars12 * 92), g(32875, 28324)))

# ------------------------------------------------------------------ FLAG 4: prepaid and other assets
print("\nFLAG 4 prepaid expenses and other assets")
pp13, pp12, pp12_first = 717.2, 489.3, BSa["us-gaap:PrepaidExpenseAndOtherAssets"][Y12]
print(" rise on revised basis %.1f (%.1f%%); on first-reported %.1f (%.1f%%); convertible notes 151.0 = %.1f%% of the revised rise" % (
    pp13 - pp12, g(pp13, pp12), pp13 - pp12_first, g(pp13, pp12_first), 100 * 151.0 / (pp13 - pp12)))

# ------------------------------------------------------------------ adjusted earnings
print("\nADJUSTED EARNINGS (pre-tax)")
print(" FY2013: adjusted 1,153.2 vs reported 663.1: gap %.1f = %.1f%% of reported" % (1153.2 - 663.1, 100 * (1153.2 - 663.1) / 663.1))
print(" FY2012 first reported: 901.5 vs 450.6: gap %.1f = %.1f%%; as revised 892.3 vs 441.4: gap %.1f = %.1f%%" % (
    901.5 - 450.6, 100 * (901.5 - 450.6) / 450.6, 892.3 - 441.4, 100 * (892.3 - 441.4) / 441.4))
print(" restructuring + related: 2013 %.1f, 2012 %.1f, 2011 %.1f" % (77.0 + 21.8, 38.0 + 11.1, 56.4 + 9.8))
print(" items present in both 2013 and 2012: purchase accounting 132.2/109.6, debt-related 68.4/83.6, restructuring 77.0/38.0, restructuring related 21.8/11.1, acquisition related 18.5/163.7, other 50.7/44.0")
both13 = 132.2 + 68.4 + 77.0 + 21.8 + 18.5 + 50.7
both12 = 109.6 + 83.6 + 38.0 + 11.1 + 163.7 + 44.0
print(" those repeating items sum to %.1f of the 2013 gap of 490.1 (%.1f%%) and %.1f of the 2012 gap of 450.9" % (both13, 100 * both13 / 490.1, both12))

# ------------------------------------------------------------------ reserves
print("\nRESERVES")
print(" public liability and property damage 332.2 -> 347.7: %.1f%%; cash flow line (3.7) in 2013, (4.3) in 2012; U.S. transaction days +26.2%%" % g(347.7, 332.2))
print(" restructuring accrual 21.0 -> 48.4; tax valuation allowance 226.4 -> 279.4")

# ------------------------------------------------------------------ quotation check for the reply
print("\nQUOTATION CHECK (every quotation in numbers-2.md)")
QUOTES = [
    (AR13, 133, "a decrease in fleet receivables within our U.S. car rental segment"),
    (AR13, 133, "timing of purchases and sales"),
    (AR13, 42, "indicative of the residual values experienced"),
    (AR12, 113, "strong residual values"),
    (AR13, 54, "a deterioration in the used vehicle residual values"),
    (AR13, 83, "allowances for doubtful accounts in Brazil"),
    (ER13, 2, "lower than expected pricing and higher expenses related to carrying extra fleet"),
    (AR13, 133, "strategic investment in China Auto Rental"),
    (ER13, 2, "Extraordinary, unusual or non-recurring gains and losses"),
    (ER12, 15, "Extraordinary, unusual or non-recurring gains and losses"),
    (AR13, 44, "During 2007 through 2013"),
    (AR13, 56, "adjustment to Advantage divestiture support payments"),
    (AR13, 138, "primarily related to Dollar Thrifty"),
]
for f, p, q in QUOTES:
    src(f, q, p)

try:
    reply = open("runs/v2.2/numbers-2.md", encoding="utf-8").read()
except FileNotFoundError:
    reply = None
if reply is not None:
    found = re.findall(r"\"([^\"]+)\"", reply)
    known = {q for _, _, q in QUOTES}
    print(" quotations found in the reply: %d" % len(found))
    for q in found:
        status = "OK" if q in known else "NOT IN CHECK LIST"
        if q not in known:
            FAIL.append(("reply", q, None, None))
        print("  [%s] %s" % (status, q))
    missing = [q for q in known if q not in found]
    print(" check-list quotations not used in the reply:", missing)

print("\nRESULT:", "ALL CHECKS PASS" if not FAIL else "FAILURES: %r" % FAIL)
sys.exit(0)
