"""Recompute ten measures used by the v2.26 Hertz replies from the workspace files,
assert the quotations the score rests on are on their cited pages, and scan the
replies for trap, banned and holding-period terms.

Run from anywhere:  python recompute.py
Reads only runs/hertz-fy2013/v2.26/claude-code/001/workspace/* and the five replies.
Writes nothing.
"""
import os, re, sys
import openpyxl

HERE = os.path.dirname(os.path.abspath(__file__))
RUN = os.path.dirname(HERE)
WS = os.path.join(RUN, "workspace")
sys.stdout.reconfigure(encoding="utf-8")

# ---------------------------------------------------------------- pack text
def pages(fn):
    txt = open(os.path.join(WS, fn), encoding="utf-8", errors="replace").read()
    parts = re.split(r"\[p\. ([^\]]+)\]", txt)
    d = {}
    for i in range(1, len(parts), 2):
        d[parts[i]] = d.get(parts[i], "") + parts[i + 1]
    return d

P13 = pages("annual-report-FY2013-12-31.txt")
P12 = pages("annual-report-FY2012-12-31.txt")
R13 = pages("earnings-release-Q4-FY2013-12-31.txt")
R12 = pages("earnings-release-Q4-FY2012-12-31.txt")
R13U = R13["unnumbered"]
EM = chr(0x2014)

def norm(s):
    return re.sub(r"\s+", " ", s.replace("’", "'").replace("‘", "'")
                  .replace("“", '"').replace("”", '"').replace("‑", "-")
                  .replace(chr(0x2013), "-").replace(EM, "-"))

def on_page(doc, page, text):
    return norm(text) in norm(doc.get(page, ""))

QUOTES = [
    # K5 and K6 locators (scorer's own)
    (P13, "11", "our approximate average holding period for a rental car was eighteen months in the United States and thirteen months in our international operations"),
    (P12, "11", "our approximate average holding period for a rental car was eighteen months in the United States and fourteen months in our international operations"),
    (P12, "81", "Useful lives are as follows:"), (P12, "81", "Cars | 4 to 28 months"),
    (P13, "91", "Holding periods are as follows:"), (P13, "91", "Cars | 4 to 36 months"),
    (P13, "53", "vehicle maintenance costs of $9.6 million due to the expansion of our off-airport and leisure businesses, longer holding periods and the impact of recalls"),
    (P13, "42", "the longer holding period does not necessarily equate to higher costs"),
    (P12, "42", "the longer holding period does not necessarily equate to higher costs"),
    (P13, "126", "optimization of fleet holding periods related to the integration of Dollar Thrifty"),
    (P13, "42", "optimization of fleet holding periods related to the integration of Dollar Thrifty"),
    (P13, "126", "The cumulative effect of the reduction in rates was also indicative of the residual values experienced in the U.S."),
    (P13, "42", "The cumulative effect of the reduction in rates was also indicative of the residual values experienced in the U.S."),
    (P12, "113", "indicative of the strong residual values experienced in the U.S."),
    (P12, "42", "We believe the residual values have remained fairly stronger"),
    (P13, "126", "net losses of $48.2 million, and net gains of $100.6 million"),
    (P13, "126", "net gains of $26.2 million, $13.5 million and $13.3 million"),
    (P13, "126", "declining residual values from falling demand for used vehicles"),
    (P13, "126", "net decreases of $44.2 million, $139.4 million and $26.7 million"),
    (P13, "126", "$2,407.8 | $2,145.9 | $1,912.3"), (P13, "126", "Rents paid for vehicles leased | 80.5 | 79.8 | 96.1"),
    (P12, "113", "$2,165.2 | $1,921.8"), (P12, "113", "net decreases of $130.6 million"),
    (P13, "40", "decreased by $39.6 million, $130.1 million and $18.2 million"),
    (P13, "54", "a deterioration in the used vehicle residual values"),
    (P12, "42", "due to improved residual values in the U.S."),
    (P13, "42", "due to mix optimization, improved procurement and remarketing efforts"),
    (P13, "43", "slight strengthening of used vehicle residual values"),
    (P13, "45", "industry residual value guidebooks"), (P13, "45", "Depreciation rates are adjusted prospectively"),
    (P13, "45", "relatively minor adjustments"), (P13, "45", "based on rental volume and actuarial evaluations"),
    (P12, "45", "based on rental volume and actuarial evaluations"),
    (P13, "42", "the average age of our fleet will increase"),
    # other quotations the replies rest on
    (P13, "93", "range from two to fifteen years"), (P12, "83", "range from two to fifteen years"),
    (P13, "91", "Other intangible assets | 3 to 10 years"), (P12, "81", "Other intangible assets | 3 to 20 years"),
    (P13, "91", "Other equipment | 24 to 108 months"), (P12, "81", "Other equipment | 24 to 108 months"),
    (P13, "91", "Buildings | 5 to 50 years"), (P12, "81", "Buildings | 3 to 50 years"),
    (P13, "91", "Capitalized internal use software | 1 to 10 years"), (P12, "81", "Capitalized internal use software | 1 to 15 years"),
    (P13, "91", "contracted residual value guaranteed to us by the lessee, such that we do not experience any gains or losses"),
    (P12, "81", "contracted residual value guaranteed to us by the lessee, such that we do not experience any gains or losses"),
    (P13, "99", "Customer relationships | 16 | $65.0"), (P13, "99", "Trademark | 20 | 7.0"), (P12, "89", "Customer relationships | 16 | $65.0"),
    (P13, "98", "amortized over their expected useful lives of nine years"), (P12, "88", "amortized over their expected useful lives of nine years"),
    (P13, "93", "one level below our operating segments"), (P12, "83", "one level below our operating segments"),
    (P13, "46", "five reporting units: U.S. Car Rental, Europe Car Rental, Other International Car Rental, Donlen and Worldwide Equipment Rental"),
    (P12, "46", "five reporting units: U.S. Car Rental, Europe Car Rental, Other International Car Rental, Donlen and Worldwide Equipment Rental"),
    (P13, "94", "no impairment existed"), (P13, "90", "based on our historical experience"), (P12, "81", "based on our historical experience"),
    (P13, "131", "certain one-time charges and non-operational items"), (P13, "50", "certain one-time charges and nonoperational items"),
    (P13, "140", "$645.4 million"), (P13, "140", "Additional efficiency and cost saving initiatives are being developed"),
    (P13, "140", "$21.9 million of costs related to the relocation of our corporate headquarters"),
    (R13U, None, "Integration expenses (d) | 18.1 | " + EM + " | " + EM + " | " + EM + " | 21.9 | 40.0"),
    (P13, "50", "Other(11) | (50.7) | (44.0)"), (P13, "50", "Debt-related charges"), (P12, "50", "Non-cash debt charges"),
    (P13, "134", "Impairment charges and other(10) | (44.0)"), (P13, "80", "Impairment charges and other | 40.0"),
    (P13, "146", "we recorded an impairment charge of $40.0 million"),
    (R13U, None, "Other unusual/non-recurring (c)"),
    # the FY2013 release's Table 7 pages carry a second "[p. 2]" and "[p. 3]" after the unnumbered tables (PK11)
    (R13, "3", "Total extraordinary, unusual or non-recurring items | $79.1 | $75.4 | $8.9 | $0.7 | $119.3 | $283.4 | $112.3 | $23.5 | $25.1 | $0.3 | $78.1 | $239.3"),
    (R13, "2", "Extraordinary, unusual or non-recurring gains and losses (c) | 79.1 | 75.4 | 8.9 | 0.7 | 119.3 | 283.4 | 112.3 | 23.5 | 25.1 | 0.3 | 78.1 | 239.3"),
    (R13, "2", "Car rental fleet interest | (185.3) | (102.4) | " + EM + " | (14.2) | " + EM + " | (301.9)"),
    (R13U, None, "Proceeds from disposal of revenue earning equipment | 4,328.2 | 2,242.1 | 138.3 | 555.5 | 7,264.1"),
    (P13, "131", "We historically aggregated our U.S., Europe, Other International and Donlen car rental operating segments"),
    (P13, "108", "Upon discovery in January 2014 of such requirement not being met"),
    (R13, "5", "Restructuring and related charges | 98.8 | 49.1"), (R12, "4", "Restructuring and related charges | 49.1 | 66.2"),
    (R12, "4", "Acquisition related costs and charges | 163.7 | 18.8"), (R13U, None, "Acquisition related costs (d) | " + EM + " | " + EM + " | " + EM + " | " + EM + " | 18.5 | 18.5 | 96.4"),
    (R13U, None, "Free cash flow | $428.2 | $442.5 | $448.7 | $155.1"), (R13U, None, "excludes certain DTG acquisition related items of approximately $129.6 million"),
    (R12, "16", "Levered after-tax cash flow before fleet growth | (1,005.4)"), (R12, "16", "Corporate cash flow | $(2,183.4)"),
    (R13U, None, "Revenue earning equipment expenditures | $(662.3) | $(19.2) | $(90.0) | $(207.1) | $(978.6) | $(1,183.9) | $(344.0) | $(156.4) | $(244.0) | $(1,928.3)"),
    (P13, "83", "out of period errors totaling $46.3 million"), (P13, "83", "management has revised in this filing"),
    (P13, "83", "vendor incentives (reduced pre-tax income by $12.9 million in 2011 and $2.4 million in 2012)"),
    (P13, "84", "Income before income taxes | 450.6 | (9.2) | 441.4 | 324.3 | (18.7) | 305.6"),
    (P13, "158", "Year ended December 31, 2013 | $29.3 | $41.9 | $(0.1) | $(40.3) | (a) | $30.8"),
    (P13, "158", "Year ended December 31, 2012(b) | 20.3 | 38.3 | " + EM + " | (29.3) | (a) | 29.3"),
    (P12, "140", "Year ended December 31, 2012 | $20,282 | $34,144 | $28 | $(29,341) | (a) | $25,113"),
    (P13, "80", "Provision for losses on doubtful accounts | 45.9 | 38.3 | 28.2"),
    (P13, "137", "A judgment - which could potentially exceed $40.0 million"), (P13, "137", "We continue to believe the outcome of this case will not be material"),
    (P12, "122", "the parties will again be engaging in mediation"),
    (P13, "159", "implemented Oracle general ledger, accounts payable and a portion of fixed assets"),
    (P13, "108", "unknowingly not met"),
    (P12, "25", "Several of our remaining multiemployer plans have underfunded liabilities"),
    (P13, "26", "Our multiemployer plans could have significant underfunded liabilities"),
    (P13, "98", "Accounts payable | (43"), (P13, "99", "10,197.4"),
    (P13, "70", "2,727.7"), (P13, "70", "Purchase obligations(5) | 4,757.6"), (P13, "104", "letters of credit totaling $644.9 million"),
    (P13, "64", "due to the timing of our payments"), (P12, "60", "due to the timing of our payments"),
    (P13, "81", "Purchases of revenue earning equipment included in accounts payable and accrued liabilities | $289.1 | $247.0"),
    (P13, "81", "Sales of revenue earning equipment included in receivables | 357.3 | 618.6"),
    (P13, "81", "Purchases of property and equipment included in accounts payable | 55.6 | 35.0"),
    (P13, "81", "Sales of property and equipment included in receivables | 16.6 | 0.9"),
    (P13, "80", "Net cash provided by operating activities | 3,589.6 | 2,709.7"),
    (P13, "80", "Accounts payable | 23.2 | 34.0"), (P13, "80", "Accrued liabilities | 25.2 | (29.6)"), (P13, "80", "Accrued taxes | 24.5 | 28.8"),
    (P13, "80", "Public liability and property damage | (3.7) | (4.3)"),
    (P13, "42", "Percentage of non-program cars in our U.S. car rental operations | 91% | 95% | 83%"),
    (P13, "42", "197,700, 136,400 and 121,800 non-program cars"),
    (P13, "49", "Average number of cars (Company-operated) | 468,500 | 358,000"), (P13, "49", "Average number of cars (Leased) | 21,500 | 1,100"),
    (P13, "49", "Transaction days (in thousands)(a) | 133,181 | 105,539"), (P13, "49", "Transaction days (in thousands)(a) | 45,019 | 43,248"),
    (P12, "49", "Worldwide transaction days (in thousands)(a) | 148,787"),
    (P13, "131", "U.S. car rental | $1,269.3 | $940.6"), (P13, "131", "International car rental | 532.0 | 528.2"),
    (P13, "131", "Worldwide equipment rental | 298.8 | 272.1"), (P13, "131", "All other operations | 425.4 | 388.0"),
    (P13, "96", "Concession rights | 411.3 | (49.5) | 361.8"), (P13, "96", "Concession rights | 406.0 | (5.0) | 401.0"),
    (P13, "96", "Total | 3,350.1 | " + EM + " | 3,350.1"), (P13, "96", "Total | 1,167.2 | (589.3) | 577.9"),
    (P13, "121", "Teamsters Central States | 36-6044243 | Critical | Critical"), (P12, "108", "Teamsters Central States | 36-6044243 | Critical | Critical"),
    (R12, "4", "$1.82 - $1.92"), (R13, "4", "$1.63"),
    (R12, "10", "Income before income taxes | 450.6 | 450.9 | 901.5 | 324.3 | 356.2 | 680.5"),
    (R13, "5", "Adjusted pre-tax income | 1,153.2 | 1,153.2 | 892.3 | 892.3"),
    (R13U, None, "Depreciation of revenue earning equipment | 333.4 | 102.0 | 75.7 | 109.1 | 620.2 | 245.9 | 111.9 | 73.9 | 102.1 | 533.8"),
    (R13U, None, "Depreciation of revenue earning equipment and lease charges | 643.0 | 550.0"),
    (R13U, None, "Direct operating | 1,439.3 | 1,257.7"), (R13U, None, "Selling, general and administrative | 222.2 | 331.1"),
    (R13U, None, "Transaction days (in thousands) (a) | 32,875 | 16.1%"),
]
bad = []
for doc, page, q in QUOTES:
    ok = (norm(q) in norm(doc)) if page is None else on_page(doc, page, q)
    if not ok:
        bad.append((page, q))
print(f"Quotations asserted on their pages: {len(QUOTES) - len(bad)} of {len(QUOTES)}")
for page, q in bad:
    print("  NOT FOUND:", page, q)
# count of "Critical" plans in the multiemployer tables
for lab, doc, pg in (("FY2013 p.121", P13, "121"), ("FY2012 p.108", P12, "108")):
    rows = [l for l in doc[pg].splitlines() if "| Critical | Critical |" in l]
    print(f"  {lab}: plans marked Critical in both status columns: {len(rows)}")

# ------------------------------------------------------------- workbook
wb = openpyxl.load_workbook(os.path.join(WS, "statements.xlsx"), data_only=True)
def sheet(name):
    ws = wb[name]
    rows = list(ws.iter_rows(values_only=True))
    hdr = rows[0]
    out = {}
    for r in rows[1:]:
        if r[0] is None:
            continue
        out[r[0]] = dict(zip(hdr[1:], r[1:]))
    return out, hdr
IS, ish = sheet("IS annual"); BS, bsh = sheet("BS annual"); CF, cfh = sheet("CF annual")
BSQ, bsqh = sheet("BS quarterly")
FY = {y: f"FY (ended {y}-12-31)" for y in (2009, 2010, 2011, 2012, 2013)}
def isv(line, y): return IS[line][FY[y]]
def bsv(line, y): return BS[line][FY[y]]
def cfv(line, y): return CF[line][FY[y]]
PTI = isv("Income before income taxes", 2013)   # 663.1
assert abs(PTI - 663.1) < 0.05
results = []
def rec(measure, label, reported, computed, tol):
    match = abs(computed - reported) <= tol
    results.append((measure, label, reported, computed, match))
    print(f"  [{'ok ' if match else 'NO '}] {label}: reported {reported}, computed {computed:.4g}")

# ---- M1 rental depreciation rate (Note 8 charge before disposal adjustment over average gross fleet)
print("\nM1 depreciation rate on rental equipment, annual and Q4 same-quarter")
gross = {y: bsv("Cars", y) + bsv("Other equipment", y) for y in (2010, 2011, 2012, 2013)}
cars12_rev = 12548.8                                     # Revisions sheet
gross12_rev = cars12_rev + bsv("Other equipment", 2012)
dep = {2011: 1921.8, 2012: 2165.2, 2013: 2407.8}       # FY2012 p.113; FY2013 p.126
dep12_rev = 2145.9                                     # FY2013 p.126
rate11 = dep[2011] / ((gross[2010] + gross[2011]) / 2)
rate12 = dep[2012] / ((gross[2011] + gross[2012]) / 2)
rate13 = dep[2013] / ((gross[2012] + gross[2013]) / 2)
rate12r = dep12_rev / ((gross[2011] + gross12_rev) / 2)
rate13r = dep[2013] / ((gross12_rev + gross[2013]) / 2)
rec("M1", "FY2011 rate % (numbers-1 16.2)", 16.2, rate11 * 100, 0.05)
rec("M1", "FY2012 rate % first reported (numbers-1 15.3; numbers-2 15.28)", 15.28, rate12 * 100, 0.01)
rec("M1", "FY2013 rate % on first-reported base (numbers-1 14.2; numbers-2 14.25)", 14.25, rate13 * 100, 0.01)
rec("M1", "FY2012 rate % revised (numbers-2 15.17)", 15.17, rate12r * 100, 0.01)
rec("M1", "FY2013 rate % on revised base (numbers-2 14.27)", 14.27, rate13r * 100, 0.01)
short_fr = rate12 * (gross[2012] + gross[2013]) / 2 - dep[2013]
short_rev = rate12r * (gross12_rev + gross[2013]) / 2 - dep[2013]
rec("M1", "charge not taken at FY2012 rate, first reported $m (174.5)", 174.5, short_fr, 0.3)
rec("M1", "same, revised $m (152.1)", 152.1, short_rev, 0.3)
rec("M1", "share of pre-tax % (26.3)", 26.3, short_fr / PTI * 100, 0.1)
rec("M1", "share of pre-tax % revised, report ranks on (22.9)", 22.9, short_rev / PTI * 100, 0.1)
rec("M1", "average gross fleet FY2013 $m (numbers-1 'about 16,900')", 16900, (gross[2012] + gross[2013]) / 2, 60)
rec("M1", "$39.6m net rate changes as % of revised shortfall (26)", 26, 39.6 / short_rev * 100, 0.6)
# car-only and equipment-only rates (numbers-2): segment charge less rents and disposal results, over average gross cost
car13 = 1269.3 + 532.0 + 425.4 - 80.5 - (48.2 + 15.2)      # p.131 segments; p.126 rents and disposal losses
car12 = 940.6 + 528.2 + 388.0 - 79.8 - (-100.6 + 17.3)
eq13 = 298.8 + 26.2; eq12 = 272.1 + 13.5                   # equipment disposal gains added back
rec("M1", "car rate FY2012 % (numbers-2 16.74)", 16.74, car12 / ((bsv("Cars", 2011) + cars12_rev) / 2) * 100, 0.05)
rec("M1", "car rate FY2013 % (numbers-2 15.43)", 15.43, car13 / ((cars12_rev + bsv("Cars", 2013)) / 2) * 100, 0.05)
rec("M1", "equipment rate FY2012 % (numbers-2 9.41)", 9.41, eq12 / ((bsv("Other equipment", 2011) + bsv("Other equipment", 2012)) / 2) * 100, 0.05)
rec("M1", "equipment rate FY2013 % (numbers-2 9.63)", 9.63, eq13 / ((bsv("Other equipment", 2012) + bsv("Other equipment", 2013)) / 2) * 100, 0.05)
car_short = car12 / ((bsv("Cars", 2011) + cars12_rev) / 2) * ((cars12_rev + bsv("Cars", 2013)) / 2) - car13
rec("M1", "car-only charge not taken at FY2012 car rate $m (numbers-2 177.4)", 177.4, car_short, 0.6)
rec("M1", "$39.6m as % of the car-only size (22)", 22, 39.6 / car_short * 100, 0.6)
# Q4 same-quarter rate (PR46, new at v2.26): the release's cash-flow-basis line, annualised by days, over the average of the quarter's opening and closing fleet
def q(col):
    return BSQ["Cars"][col] + BSQ["Other equipment"][col]
q4_13 = 620.2 * 365 / 92 / ((q("Q3 (ended 2013-09-30)") + q("Q4 (ended 2013-12-31)")) / 2)
q4_12 = 533.8 * 366 / 92 / ((q("Q3 (ended 2012-09-30)") + q("Q4 (ended 2012-12-31)")) / 2)
rec("M1", "Q4 2012 same-quarter rate, annualised % (numbers-1 13.7)", 13.7, q4_12 * 100, 0.06)
rec("M1", "Q4 2013 same-quarter rate, annualised % (numbers-1 13.4)", 13.4, q4_13 * 100, 0.06)

# ---- M2 stated rate changes and disposal results as shares
print("\nM2 stated rate changes, disposal results, range")
rec("M2", "$44.2m as % of pre-tax (6.7)", 6.7, 44.2 / PTI * 100, 0.05)
rec("M2", "$48.2m as % (7.3)", 7.3, 48.2 / PTI * 100, 0.05)
rec("M2", "net cuts 44.2 - 5.0 + 0.4 (39.6)", 39.6, 44.2 - 5.0 + 0.4, 0.01)
rec("M2", "$39.6m as % (6.0)", 6.0, 39.6 / PTI * 100, 0.05)
rec("M2", "2012 net cuts 139.4 - 8.8 - 0.5 (130.1)", 130.1, 139.4 - 8.8 - 0.5, 0.01)
rec("M2", "U.S. disposal swing 100.6 + 48.2 (148.8)", 148.8, 100.6 + 48.2, 0.01)
rec("M2", "swing as % (22.4)", 22.4, 148.8 / PTI * 100, 0.05)
rec("M2", "range top 28 to 36 months, rise % (29)", 29, (36 / 28 - 1) * 100, 0.6)
rec("M2", "$48.2m loss as % of U.S. disposal proceeds 4,328.2 (text-3 1.1)", 1.1, 48.2 / 4328.2 * 100, 0.06)
rec("M2", "Donlen disposal result by difference FY2013 (0): 37.2 loss = 48.2 + 15.2 - 26.2", 0, 48.2 + 15.2 - 26.2 - 37.2, 0.05)
rec("M2", "Donlen disposal result by difference FY2012 (0): 96.8 gain = 100.6 - 17.3 + 13.5", 0, 100.6 - 17.3 + 13.5 - 96.8, 0.05)

# ---- M3 per-vehicle and turnover tests in text-4 and numbers-2
print("\nM3 per-vehicle charges and holding proxies (numbers-2, text-4)")
us13, us12 = 1269.3, 940.6                                  # p.131 U.S. segment depreciation and lease charges
co13, co12, le13, le12 = 468500, 358000, 21500, 1100       # p.49
pcm13 = (us13 - 48.2) * 1e6 / ((co13 + le13) * 12)          # before disposal results: loss removed
pcm12 = (us12 + 100.6) * 1e6 / ((co12 + le12) * 12)         # gain added back
rec("M3", "U.S. charge per car-month before disposal results FY2012 $ (241.6)", 241.6, pcm12, 0.1)
rec("M3", "same FY2013 $ (207.7)", 207.7, pcm13, 0.1)
rec("M3", "change % (-14.1)", -14.1, (pcm13 / pcm12 - 1) * 100, 0.1)
proxy12 = co12 * (0.83 + 0.95) / 2 / 136400 * 12; proxy13 = co13 * (0.95 + 0.91) / 2 / 197700 * 12
rec("M3", "implied non-program holding FY2012 months (text-4 28.0)", 28.0, proxy12, 0.1)
rec("M3", "implied non-program holding FY2013 months (text-4 26.4)", 26.4, proxy13, 0.1)
m = re.search(r"([\d,]+), ([\d,]+) and ([\d,]+) non-program cars", P13.get("43", ""))
if m:
    s13, s12 = (int(m.group(1).replace(",", "")), int(m.group(2).replace(",", "")))
    ip13 = 159700 * (0.79 + 0.76) / 2 / s13 * 12; ip12 = 153700 * (0.75 + 0.79) / 2 / s12 * 12
    rec("M3", "international implied holding FY2012 months (text-4 26.1)", 26.1, ip12, 0.1)
    rec("M3", "international implied holding FY2013 months (text-4 23.0)", 23.0, ip13, 0.1)
else:
    print("  international cars-sold figure not found on p. 43; text-4's 26.1 / 23.0 not recomputed")
pe_dep = {2012: 172.6, 2013: 205.3}
pe_gross = {y: bsv("Total property and equipment, at cost", y) for y in (2011, 2012, 2013)}
rec("M3", "property and equipment rate FY2012 % (text-4 7.3)", 7.3, pe_dep[2012] / ((pe_gross[2011] + pe_gross[2012]) / 2) * 100, 0.06)
rec("M3", "same FY2013 % (7.9)", 7.9, pe_dep[2013] / ((pe_gross[2012] + pe_gross[2013]) / 2) * 100, 0.06)
conc = (49.5 - 5.0) / 411.3
rec("M3", "concession amortization as % of cost (text-4 10.8)", 10.8, conc * 100, 0.06)
rec("M3", "implied life, years (text-4 9.2)", 9.2, 1 / conc, 0.06)

# ---- M4 allowance
print("\nM4 allowance for doubtful accounts")
net = {y: bsv("Receivables, less allowance for doubtful accounts of $30.8 and $29.3", y) for y in (2010, 2011, 2012, 2013)}
allow = {2010: 19.7, 2011: 20.3, 2012: 25.1, 2013: 30.8}   # Schedule II first reported (FY2012 p.140 in thousands; FY2013 p.158)
for y, rep in ((2010, 1.4), (2011, 1.2), (2012, 1.3), (2013, 2.0)):
    rec("M4", f"allowance % of gross receivables {y} (numbers-1 {rep})", rep, allow[y] / (net[y] + allow[y]) * 100, 0.06)
rec("M4", "allowance / write-offs FY2013 (0.76)", 0.76, 30.8 / 40.3, 0.006)
rec("M4", "charge / write-offs FY2013 (1.04)", 1.04, 41.9 / 40.3, 0.006)
rec("M4", "2012 revised allowance % of gross receivables (text-4 1.5)", 1.5, 29.3 / (1879.7 + 29.3) * 100, 0.06)
rec("M4", "2012 revised allowance / write-offs (text-4 1.00)", 1.00, 29.3 / 29.3, 0.006)
rec("M4", "cash-flow provision less Schedule II charge $m (4.0)", 4.0, cfv("Provision for losses on doubtful accounts", 2013) - 41.9, 0.01)
rec("M4", "2012 allowance revised 25.1 to 29.3: rise $m (4.2)", 4.2, 29.3 - 25.113, 0.05)
rec("M4", "2012 charge revised 34.1 to 38.3: rise $m (4.2)", 4.2, 38.3 - 34.144, 0.05)

# ---- M5 adjusted measures
print("\nM5 adjusted pre-tax income and add-backs")
adj = {2011: 680.5, 2012: 892.3, 2013: 1153.2}
rec("M5", "gap 2013 $m (490.1)", 490.1, adj[2013] - PTI, 0.01)
rec("M5", "gap 2013 % of pre-tax (73.9)", 73.9, (adj[2013] - PTI) / PTI * 100, 0.05)
rec("M5", "gap 2012 revised $m (450.9)", 450.9, adj[2012] - 441.4, 0.01)
rec("M5", "gap 2012 first reported 901.5 - 450.6 (450.9)", 450.9, 901.5 - 450.6, 0.01)
rec("M5", "gap 2011 $m (356.2)", 356.2, adj[2011] - 324.3, 0.01)
rec("M5", "restructuring plus related $98.8m as % (14.9)", 14.9, 98.8 / PTI * 100, 0.05)
rec("M5", "restructuring since 2007, average per year (text-3 'about 92')", 92, 645.4 / 7, 0.6)
rec("M5", "new exclusions 40.0 + 7.8 + 44.0 $m (91.8)", 91.8, 40.0 + 7.8 + 44.0, 0.01)
rec("M5", "that as % (13.8)", 13.8, 91.8 / PTI * 100, 0.05)
rec("M5", "Note 14 restructuring 56.4 + 38.0 + 77.0 + 2007-2010 = 645.4? (residual 2007-2010)", 645.4 - 56.4 - 38.0 - 77.0, 645.4 - (56.4 + 38.0 + 77.0), 0.01)
rec("M5", "2012 adjusted pre-tax 901.5 to 892.3, change (9.2)", 9.2, 901.5 - 892.3, 0.01)
rec("M5", "integration 21.9 (release Q4 column) equals relocation 21.9 (p.140)", 0, 21.9 - 21.9, 0.01)

# ---- M6 error corrections
print("\nM6 out-of-period errors and revisions")
rec("M6", "46.3 as % of pre-tax (7.0)", 7.0, 46.3 / PTI * 100, 0.05)
rec("M6", "2013 part 46.3 - 34.7 (11.6)", 11.6, 46.3 - 34.7, 0.01)
rec("M6", "11.6 as % (1.7)", 1.7, 11.6 / PTI * 100, 0.05)
rec("M6", "prior-year parts 6.8 + 18.7 + 9.2 (34.7)", 34.7, 6.8 + 18.7 + 9.2, 0.01)
rec("M6", "2011 correction as % of 2011 as-reported pre-tax (5.8)", 5.8, 18.7 / 324.3 * 100, 0.06)
rec("M6", "2012 pre-tax 450.6 to 441.4, change % (-2.0)", -2.0, (441.4 / 450.6 - 1) * 100, 0.06)
rec("M6", "workbook 2012 pre-tax (450.5; PK10)", 450.5, isv("Income before income taxes", 2012), 0.01)
rec("M6", "2011 pre-tax 324.3 to 305.6 (18.7)", 18.7, 324.3 - 305.6, 0.01)
rec("M6", "end-2012 equity 2,507.3 to 2,486.2 (21.1)", 21.1, 2507.3 - 2486.2, 0.01)

# ---- M7 payables
print("\nM7 payables")
cost = {y: isv("Direct operating", y) + isv("Depreciation of revenue earning equipment and lease charges", y) for y in (2012, 2013)}
cost12_rev = 4806.0 + 2128.9
ap = {2012: bsv("Accounts payable", 2012), 2013: bsv("Accounts payable", 2013)}; ap12_rev = 1003.2
rev = {y: isv("Total revenues", y) for y in (2012, 2013)}
dpo12 = ap[2012] / cost[2012] * 366; dpo12r = ap12_rev / cost12_rev * 366; dpo13 = ap[2013] / cost[2013] * 365
rec("M7", "days payable FY2012 first reported (52.7)", 52.7, dpo12, 0.06)
rec("M7", "days payable FY2012 revised (52.9)", 52.9, dpo12r, 0.06)
rec("M7", "days payable FY2013 (42.7)", 42.7, dpo13, 0.06)
q4cost13 = 1439.3 + 643.0; q4cost12 = 1257.7 + 550.0        # release Table 1
rec("M7", "Q4 2012 days payable (50.8)", 50.8, ap[2012] / q4cost12 * 92, 0.06)
rec("M7", "Q4 2013 days payable (42.8)", 42.8, ap[2013] / q4cost13 * 92, 0.06)
rec("M7", "payables fell % first reported (-3.1)", -3.1, (ap[2013] / ap[2012] - 1) * 100, 0.06)
rec("M7", "payables fell % revised (-3.5)", -3.5, (ap[2013] / ap12_rev - 1) * 100, 0.06)
rec("M7", "cost of sales rose % first reported (19.2)", 19.2, (cost[2013] / cost[2012] - 1) * 100, 0.06)
rec("M7", "cost of sales rose % revised (19.4)", 19.4, (cost[2013] / cost12_rev - 1) * 100, 0.06)
rec("M7", "payables growth less cost growth, pts (-22.3)", -22.3, ((ap[2013] / ap[2012]) - (cost[2013] / cost[2012])) * 100, 0.06)
size_fr = cost[2013] * dpo12 / 365 - ap[2013]; size_rev = cost[2013] * dpo12r / 365 - ap[2013]
rec("M7", "size at FY2012 days, first reported $m (226.3)", 226.3, size_fr, 0.3)
rec("M7", "size as % (34.1)", 34.1, size_fr / PTI * 100, 0.06)
rec("M7", "size revised $m (232.8)", 232.8, size_rev, 0.3)
rec("M7", "size revised as % (35.1)", 35.1, size_rev / PTI * 100, 0.06)
ocf_rise = 3589.6 - 2709.7
rec("M7", "operating cash flow rise, revised 2012 $m (879.9)", 879.9, ocf_rise, 0.01)
liab13 = 23.2 + 25.2 + 24.5 - 3.7; liab12 = 34.0 - 29.6 + 28.8 - 4.3
rec("M7", "liability lines of operating cash flow, 2013 less 2012 $m (40.3)", 40.3, liab13 - liab12, 0.05)
rec("M7", "that as % of the rise (4.6)", 4.6, (liab13 - liab12) / ocf_rise * 100, 0.06)
rec("M7", "balance fall 1003.2 - 967.9 (35.3)", 35.3, ap12_rev - ap[2013], 0.01)
d_sales12 = ap12_rev / 9024.9 * 366; d_sales13 = ap[2013] / rev[2013] * 365; d_pf = ap12_rev / 10197.4 * 366
rec("M7", "payables days on sales FY2012 revised (40.7)", 40.7, d_sales12, 0.06)
rec("M7", "same FY2013 (32.8)", 32.8, d_sales13, 0.06)
rec("M7", "pro forma share of the fall % (59)", 59, (d_sales12 - d_pf) / (d_sales12 - d_sales13) * 100, 0.6)
ind_gap = ap[2013] - 0.045 * rev[2013]
rec("M7", "payables % of sales 2013 (9.0)", 9.0, ap[2013] / rev[2013] * 100, 0.06)
rec("M7", "excess over industry 4.5% of sales $m (483.2)", 483.2, ind_gap, 0.3)
rec("M7", "that as % (72.9)", 72.9, ind_gap / PTI * 100, 0.06)
rec("M7", "fleet and capex purchases cover at most % of the gap (71)", 71, (289.1 + 55.6) / ind_gap * 100, 0.6)
rec("M7", "payables ex fleet and capex purchases, % of sales 2013 (5.8)", 5.8, (ap[2013] - 289.1 - 55.6) / rev[2013] * 100, 0.06)
rec("M7", "Q4 fleet spending 978.6 against 1,928.3 (release Table 7; p.60 table)", 1928.3 - 978.6, 1928.3 - 978.6, 0.01)

# ---- M8 receivables
print("\nM8 receivables")
rec("M8", "DSO FY2012 (76.5)", 76.5, net[2012] / rev[2012] * 366, 0.06)
rec("M8", "DSO FY2013 (51.3)", 51.3, net[2013] / rev[2013] * 365, 0.06)
rec("M8", "Q4 2012 DSO (74.8)", 74.8, net[2012] / 2319.7 * 92, 0.06)
rec("M8", "Q4 2013 DSO (54.4)", 54.4, net[2013] / 2556.3 * 92, 0.06)
rec("M8", "receivables % of sales 2013 (14.0)", 14.0, net[2013] / rev[2013] * 100, 0.06)
rgap = net[2013] - 0.115 * rev[2013]
rec("M8", "excess over industry 11.5% $m (273.8)", 273.8, rgap, 0.3)
rec("M8", "that as % (41.3)", 41.3, rgap / PTI * 100, 0.06)
rec("M8", "ex fleet-sale and property-sale receivables % of sales (10.6)", 10.6, (net[2013] - 357.3 - 16.6) / rev[2013] * 100, 0.06)
rec("M8", "disclosed items cover % of the gap (137)", 137, (357.3 + 16.6) / rgap * 100, 0.6)
rec("M8", "fall in receivables, revised basis 1879.7 - 1512.6 (367.1)", 367.1, 1879.7 - net[2013], 0.01)
rec("M8", "vehicle-sale receivables' share of the fall % (67)", 67, ((618.6 + 0.9) - (357.3 + 16.6)) / 367.1 * 100, 0.6)
rec("M8", "the rest fell % (-9.6)", -9.6, ((net[2013] - 357.3 - 16.6) / (1879.7 - 618.6 - 0.9) - 1) * 100, 0.06)
rec("M8", "receivables growth less revenue growth, pts (-39.2)", -39.2, ((net[2013] / net[2012]) - (rev[2013] / rev[2012])) * 100, 0.06)
rec("M8", "Q4 receivables growth less Q4 revenue growth, pts (-30.0)", -30.0, ((net[2013] / net[2012]) - (2556.3 / 2319.7)) * 100, 0.06)

# ---- M9 margins, accruals, cash flow
print("\nM9 margins, accruals, free cash flow")
gm13q = (2556.3 - 1439.3 - 643.0) / 2556.3; gm12q = (2319.7 - 1257.7 - 550.0) / 2319.7
rec("M9", "Q4 2012 gross margin % (22.1)", 22.1, gm12q * 100, 0.06)
rec("M9", "Q4 2013 gross margin % (18.5)", 18.5, gm13q * 100, 0.06)
rec("M9", "Q4 2012 operating margin % (7.8)", 7.8, (2319.7 - 1257.7 - 550.0 - 331.1) / 2319.7 * 100, 0.06)
rec("M9", "Q4 2013 operating margin % (9.9)", 9.9, (2556.3 - 1439.3 - 643.0 - 222.2) / 2556.3 * 100, 0.06)
for y, gm, om in ((2010, 18.7, 9.9), (2011, 22.0, 13.0), (2012, 23.0, 12.5), (2013, 23.2, 13.7)):
    c = isv("Direct operating", y) + isv("Depreciation of revenue earning equipment and lease charges", y); r = isv("Total revenues", y)
    rec("M9", f"FY{y} gross margin % ({gm})", gm, (r - c) / r * 100, 0.06)
    rec("M9", f"FY{y} operating margin % ({om})", om, (r - c - isv("Selling, general and administrative", y)) / r * 100, 0.06)
op13 = rev[2013] - cost[2013] - isv("Selling, general and administrative", 2013)
rec("M9", "margin gap times revenue $m (836.7)", 836.7, (op13 / rev[2013] - 0.059) * rev[2013], 0.6)
rec("M9", "that as % (126)", 126, (op13 / rev[2013] - 0.059) * rev[2013] / PTI * 100, 0.6)
rec("M9", "operating margin after fleet interest 301.9 % (10.9)", 10.9, (op13 - 301.9) / rev[2013] * 100, 0.06)
rec("M9", "pre-tax margin % (6.2)", 6.2, PTI / rev[2013] * 100, 0.06)
ta = {y: bsv("Total assets", y) for y in (2012, 2013)}
rec("M9", "accruals % of average assets FY2013 (-13.6)", -13.6, (isv("Net income", 2013) - cfv("Net cash provided by (used in) operating activities", 2013)) / ((ta[2012] + ta[2013]) / 2) * 100, 0.06)
def fcf(y):
    return (cfv("Net cash provided by (used in) operating activities", y)
            + cfv("Revenue earning equipment expenditures", y) + cfv("Proceeds from disposal of revenue earning equipment", y)
            + cfv("Property and equipment expenditures", y) + cfv("Proceeds from disposal of property and equipment", y))
for y, rep in ((2010, 1145.9), (2011, 401.5), (2012, 54.8), (2013, 314.5)):
    rec("M9", f"free cash flow FY{y} $m ({rep})", rep, fcf(y), 0.3)
capex13 = -(cfv("Revenue earning equipment expenditures", 2013) + cfv("Proceeds from disposal of revenue earning equipment", 2013)
            + cfv("Property and equipment expenditures", 2013) + cfv("Proceeds from disposal of property and equipment", 2013))
rec("M9", "net capital spending / depreciation FY2013 (1.25)", 1.25, capex13 / (2407.8 + 205.3), 0.006)

# ---- M10 balances and exposures
print("\nM10 balances, exposures, small items")
rec("M10", "Sobel $40.0m as % (6.0)", 6.0, 40.0 / PTI * 100, 0.06)
rec("M10", "goodwill 1,347.5 (workbook)", 1347.5, bsv("Goodwill", 2013), 0.01)
gi = 1347.5 + 3350.1
rec("M10", "goodwill plus indefinite-lived intangibles $m (4,697.6)", 4697.6, gi, 0.01)
rec("M10", "times total equity (1.7)", 1.7, gi / bsv("Total equity", 2013), 0.06)
rec("M10", "public liability reserve 347.7 (workbook)", 347.7, bsv("Public liability and property damage", 2013), 0.01)
rec("M10", "reserve per 1,000 transaction days 2012 $ (text-4 2.23)", 2.23, 332.2 / 148787 * 1000, 0.006)
rec("M10", "same 2013 $ (text-4 1.95)", 1.95, 347.7 / (133181 + 45019) * 1000, 0.006)
rec("M10", "lease and concession commitments 2,727.7 tie (p.70)", 2727.7, 601.9 + 789.1 + 455.4 + 881.3, 0.1)
rec("M10", "restructuring accrual roll-forward end balance (text-3 48.4)", 48.4, 48.4, 0.01)  # p.141 end balance, asserted below
assert on_page(P13, "141", "48.4"), "p.141 restructuring accrual 48.4 not found"

n_ok = sum(1 for r in results if r[4]); print(f"\nSub-figures: {n_ok} of {len(results)} match at the reply's rounding")
for r in results:
    if not r[4]:
        print("  mismatch:", r[0], r[1], "reported", r[2], "computed", round(r[3], 3))

# ------------------------------------------------------------- reply scans
print("\nReply scans")
replies = {n: open(os.path.join(RUN, n), encoding="utf-8").read() for n in
           ("numbers-1.md", "numbers-2.md", "text-3.md", "text-4.md", "report-5.md")}
banned = r"\bfraud|manipulat|red flag|misstat|suspicious|material weakness|aggressive"
traps = (r"planned holding|21 to|25 months|24 or 30|disposed cars|affirmative|attorney|rolling|spreadsheet error|"
         r"9\.3 million|tone at the top|\b235\b|June 2014|May 2014|November 2014|2015|1\.78|1\.68|1\.72|1\.66|1\.65|budget|"
         r"\b1\.82\b|extended holding|subrogation")
for n, t in replies.items():
    b = re.findall(banned, t, re.I); tr = re.findall(traps, t, re.I)
    print(f"  {n}: banned {b}; trap or key terms {tr}; 'longer holding' {len(re.findall('longer holding', t))}; "
          f"'p.53' {len(re.findall(r'p\.53|p\. 53', t))}; 'eighteen' {len(re.findall('eighteen', t))}; '18 months' {len(re.findall('18 months', t))}; "
          f"'optimization of fleet' {len(re.findall('optimization of fleet', t))}; 'maintenance' {len(re.findall('maintenance', t))}; "
          f"'2014' {len(re.findall('2014', t))}; em-dashes {t.count(EM)}")
t4 = replies["text-4.md"]
print("  text-4 'Words searched' section present:", "## 3. Words searched" in t4)
print("  report-5 'Absorbs' lines:", len(re.findall(r"Absorbs:", replies["report-5.md"])))
print("  FY2013 'longer holding' pages in the pack:", [p for p, t in P13.items() if "longer holding" in t],
      "FY2012:", [p for p, t in P12.items() if "longer holding" in t])
print("  FY2013 'holding period' pages:", [p for p, t in P13.items() if "holding period" in t],
      "FY2012:", [p for p, t in P12.items() if "holding period" in t])
print("  FY2013 'salvage' pages:", [p for p, t in P13.items() if "salvage" in t.lower()],
      "FY2012:", [p for p, t in P12.items() if "salvage" in t.lower()])
