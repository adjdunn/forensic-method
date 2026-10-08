"""Recompute ten measures used by the single-prompt Hertz reply (report-5.txt) from the
workspace files, assert the quotations the score rests on are on their cited pages,
recount the "Words searched" table, and scan the reply for trap and banned terms.

Run from anywhere:  python recompute.py
Reads only runs/hertz-fy2013/single-v1/manual/001/workspace/* and report-5.txt.
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
    s = s.replace("ﬀ", "ff").replace("ﬁ", "fi").replace("ﬂ", "fl")
    return re.sub(r"\s+", " ", s.replace("’", "'").replace("‘", "'")
                  .replace("“", '"').replace("”", '"').replace("‑", "-")
                  .replace(chr(0x2013), "-").replace(EM, "-"))

def on_page(doc, page, text):
    return norm(text) in norm(doc.get(page, ""))

# The reply's quotations, each with the page the reply gives (or the page the scorer settled it to).
QUOTES = [
    # statements table and item 1 (K5, K6, K9)
    (P13, "11", "approximate average holding period for a rental car was eighteen months in the United States"),
    (P12, "11", "approximate average holding period for a rental car was eighteen months in the United States"),
    (P12, "11", "fourteen months in our international operations"), (P13, "11", "thirteen months in our international operations"),
    (P12, "81", "Useful lives are as follows:"), (P12, "81", "Cars | 4 to 28 months"),
    (P13, "91", "Holding periods are as follows:"), (P13, "91", "Cars | 4 to 36 months"),
    (P13, "53", "longer holding periods and the impact of recalls"),
    (P13, "53", "vehicle maintenance costs of $9.6 million due to the expansion of our off-airport and leisure businesses, longer holding periods and the impact of recalls"),
    (P13, "126", "The cumulative effect of the reduction in rates was also indicative of the residual values experienced in the U.S."),
    (P13, "42", "The cumulative effect of the reduction in rates was also indicative of the residual values experienced in the U.S."),
    (P12, "113", "The cumulative effect of the reduction in rates was indicative of the strong residual values experienced in the U.S."),
    (P13, "126", "net decreases of $44.2 million, $139.4 million and $26.7 million"),
    (P13, "126", "net losses of $48.2 million, and net gains of $100.6 million"),
    (P13, "126", "net increases of $5.0 million, $8.8 million and $12.9 million"),
    (P13, "126", "a decrease of $0.4 million, an increase of $0.5 million, and a decrease of $4.4 million"),
    (P13, "126", "car sales channel diversification, acceleration of our retail sales expansion"),
    (P13, "126", "optimization of fleet holding periods related to the integration of Dollar Thrifty"),   # the words the reply omits
    (P13, "54", "a deterioration in the used vehicle residual values"),
    (P13, "146", "we recorded an impairment charge of $40.0 million"), (P13, "24", "subleased approximately 20,000 vehicles to Simply Wheelz"),
    (P12, "41", "With fewer program cars in our fleet, we have an increased risk that the market value of a car at the time of its disposition will be less than its estimated residual value"),
    (P13, "42", "monthly per vehicle depreciation costs decreased"), (P12, "42", "monthly per vehicle depreciation costs decreased"),
    (P12, "81", "Other intangible assets | 3 to 20 years"), (P13, "91", "Other intangible assets | 3 to 10 years"),
    (P12, "83", "range from two to fifteen years"), (P13, "93", "range from two to fifteen years"),
    (P12, "89", "Customer relationships | 16 | $65.0"), (P13, "99", "Trademark | 20 | 7.0"),
    (P12, "22", "We expect this percentage to continue to decrease"), (P12, "41", "we expect this percentage to continue to decrease"),
    (P13, "23", "For the years ended December 31, 2013 and 2012, 30% of the vehicles purchased"),
    (P13, "43", "accelerated rotation strategy"),
    (P12, "42", "the average holding period for non-program vehicles is longer than program vehicles"),
    (P13, "42", "the average holding period for non-program vehicles is longer than program vehicles"),
    (P13, "42", "Percentage of non-program cars in our U.S. car rental operations | 91% | 95% | 83%"),
    (P12, "81", "Other equipment | 24 to 108 months"), (P13, "91", "Other equipment | 24 to 108 months"),
    (P12, "81", "Buildings | 3 to 50 years"), (P13, "91", "Buildings | 5 to 50 years"),
    (P12, "81", "Capitalized internal use software | 1 to 15 years"), (P13, "91", "Capitalized internal use software | 1 to 10 years"),
    (P12, "81", "based on our historical experience and our judgment"), (P13, "90", "based on our historical experience and our judgment"),
    # item 2
    (P13, "50", "certain one-time charges and nonoperational items"), (P13, "50", "debt-related charges"),
    (P12, "50", "non-cash debt charges"), (P12, "50", "certain one-time charges and non-operational items"),
    (P12, "124", "From January 1, 2007 through December 31, 2012, we incurred $568.4 million"),
    (P13, "44", "restructuring charges relating to various initiatives of $77.0 million"),
    (R13, "5", "litigation accrual of $5.7 million"), (R13, "5", "litigation accrual of $14.0 million"),
    (P13, "50", "Impairment charges and other(10) | (44.0)"), (P13, "57", "The effective tax rate for the year ended December 31, 2013 was 47.8%"),
    (R13, "5", "Assumed provision for income taxes at 35% in 2013"),
    (R13U, None, "Free cash flow | $428.2 | $442.5 | $448.7 | $155.1"),
    (R13U, None, "net worldwide car rental fleet financing"),
    (R13U, None, "Net financing activity related to car rental fleet | (84.3) | 147.2 | " + EM + " | 71.0 | 133.9"),
    (R13, "5", "Restructuring and related charges | 98.8 | 49.1"), (R13, "5", "Adjusted pre-tax income | 1,153.2 | 1,153.2 | 892.3 | 892.3"),
    # item 3
    (P13, "83", "we identified certain out of period errors totaling $46.3 million, of which $34.7 million ($21.0 million, net of tax) related to"),
    (P13, "83", "charges related to certain assets and allowances for doubtful accounts in Brazil"),   # reply cites p.87; it is on p.83
    (P13, "83", "$4.4 million in 2010, $6.2 million in 2011 and $3.6 million in 2012"),
    (P13, "87", "under accruals"), (P13, "87", "certain reclassifications of $23.1 million"),
    (P13, "87", "Income before income taxes | 328.3 | (7.0) | 321.3 | 612.4 | (11.6) | 600.8"),
    (P13, "87", "$22.1 million adjustment related to vendor incentives"), (P13, "87", "$21.2 million adjustment related to vendor incentives"),
    (P13, "159", "effective as of December 31, 2013"), (P13, "74", "effective internal control over financial reporting as of December 31, 2013"),
    (P13, "159", "implemented Oracle general ledger"), (P13, "138", "February 25, 2013 through November 4, 2013"),
    # item 4
    (P13, "137", "granted, in part, the plaintiffs' motion for partial summary judgment with respect to restitution and granted the plaintiffs' motion for class certification"),
    (P13, "137", "A judgment - which could potentially exceed $40.0 million - has still not been issued"),
    (P13, "137", "We continue to believe the outcome of this case will not be material"),
    (P13, "137", "mediation of this case in March 2014"), (P12, "122", "mediation"),
    # item 5
    (P13, "75", "Accrued liabilities | 1,104.7 | 1,163.1"), (P13, "80", "Accrued liabilities | 25.2 | (29.6)"),
    (P13, "64", "timing of our payments"),
    # Also noted, Checked and explained, Not examined
    (P13, "81", "Sales of revenue earning equipment included in receivables | 357.3 | 618.6"),
    (P13, "81", "Purchases of revenue earning equipment included in accounts payable and accrued liabilities | $289.1"),
    (P13, "80", "Provision for losses on doubtful accounts | 45.9"), (P13, "158", "Year ended December 31, 2013 | $29.3 | $41.9 | $(0.1) | $(40.3) | (a) | $30.8"),
    (P12, "81", "gains from the dispositions of property and equipment of $6.3 million"), (P13, "91", "$8.3 million"),
    (R13U, None, "Net cash provided by operating activities | $753.5 | $600.5 | $3,589.7 | $2,709.8"),
    (P12, "25", "Several of our remaining multiemployer plans have underfunded liabilities"),
    (P13, "26", "Our multiemployer plans could have significant underfunded liabilities"),
    (P12, "22", "We are not a party to any long-term car supply arrangements with manufacturers"),
    (R13, "2", "$0.12 impact of lower than expected pricing and higher expenses related to carrying extra fleet"),
    (P13, "146", "Balance at the end of period | $151.0"), (P13, "100", "China Auto Rental"),
    (R13U, None, "Selling, general and administrative | 222.2 | (21.1 | )(c) | 201.1 | 331.1 | (126.4 | )(c) | 204.7"),
    (P13, "94", "did not exceed their estimated fair values"), (P13, "96", "did not exceed their estimated fair values"),
    (P13, "96", "Trade name | 3,330.0"),
    (P13, "75", "Prepaid expenses and other assets | 717.2 | 489.3"),
    (P13, "39", "Worldwide car rental(b) | $8,706.9 | $7,161.7"),
    (P13, "49", "Average number of cars (Company-operated) | 468,500 | 358,000"), (P13, "49", "Average number of cars (Leased) | 21,500 | 1,100"),
    (P13, "131", "U.S. car rental | $1,269.3 | $940.6"),
    (P13, "126", "Depreciation of revenue earning equipment | $2,407.8 | $2,145.9 | $1,912.3"),
    (P12, "113", "$2,165.2 | $1,921.8"),
    (P12, "140", "Year ended December 31, 2012 | $20,282 | $34,144 | $28 | $(29,341) | (a) | $25,113"),
    (P12, "140", "Year ended December 31, 2011 | 19,708 | 28,164 | 68 | (27,658) | (a) | 20,282"),
    (P13, "158", "Year ended December 31, 2012(b) | 20.3 | 38.3 | " + EM + " | (29.3) | (a) | 29.3"),
    (R13U, None, "Depreciation of revenue earning equipment | 333.4 | 102.0 | 75.7 | 109.1 | 620.2 | 245.9 | 111.9 | 73.9 | 102.1 | 533.8"),
    (R13U, None, "Direct operating | 1,439.3 | 1,257.7"), (R13U, None, "Depreciation of revenue earning equipment and lease charges | 643.0 | 550.0"),
    (R13U, None, "Revenue earning equipment expenditures | $(662.3) | $(19.2) | $(90.0) | $(207.1) | $(978.6)"),
    (R13U, None, "Net revenue earning equipment capital expenditures | 177.0 | 568.7 | (52.4) | (77.0) | 616.3 | 132.8 | 426.8 | (106.4) | (95.3) | 357.9"),
    (R13U, None, "Property and equipment expenditures, net of disposals | (56.6) | (40.3) | (240.7) | (175.1)"),
    (R13, "2", "$62.3 | $(0.6)"), (R13, "2", "$(43.1) | $(36.8)"),
    (R12, "4", "$1.82 - $1.92"), (R13, "4", "$1.63"),
]
bad = []
for doc, page, q in QUOTES:
    ok = (norm(q) in norm(doc)) if page is None else on_page(doc, page, q)
    if not ok:
        bad.append((page, q))
print(f"Quotations and figures asserted on their pages: {len(QUOTES) - len(bad)} of {len(QUOTES)}")
for page, q in bad:
    print("  NOT FOUND:", page, q)
print("  'long-term car supply' in FY2013 10-K:", any("long-term car supply" in t for t in P13.values()))
print("  'extended holding' in either 10-K:", any("extended holding" in t for t in P13.values()) or any("extended holding" in t for t in P12.values()))

# ---------------------------------------------------- words searched recount
print("\nWords searched (reply's page lists against the pack)")
def hits(doc, pat):
    return sorted({pg for pg, t in doc.items() if re.search(pat, t, re.I)}, key=lambda x: (len(x), x))
reply_words = {
    "holding period": (["11", "42", "44", "61", "81"], ["11", "42", "45", "53", "66", "91", "126"]),
    "useful life": (["89"], ["99", "146"]),
    "useful lives": (["46", "80", "81", "83", "85", "86", "88"], ["46", "83", "90", "93", "94", "96", "98"]),
    "residual": (["1", "11", "22", "23", "24", "40", "41", "42", "44", "53", "54", "55", "58", "59", "60", "63", "81", "113"],
                 ["1", "11", "23", "24", "25", "40", "41", "42", "43", "45", "54", "61", "62", "63", "64", "68", "91", "126"]),
    "salvage": ([], []),
}
for w, (r12, r13) in reply_words.items():
    h12, h13 = hits(P12, re.escape(w)), hits(P13, re.escape(w))
    print(f"  {w!r}: 2012 reply {r12} pack {h12} {'match' if r12 == h12 else 'DIFFER'}; 2013 reply {r13} pack {h13} {'match' if r13 == h13 else 'DIFFER'}")
a12, a13 = hits(P12, r"\baverage\b"), hits(P13, r"\baverage\b")
print(f"  'average': reply '30 pages' / '38 pages'; pack {len(a12)} / {len(a13)} pages; reply's named pages present: "
      f"{all(p in a12 for p in ['11','42','45','46','81'] + [str(i) for i in range(104,113)])} / "
      f"{all(p in a13 for p in ['11','42','43','46','92'] + [str(i) for i in range(117,125)])}")

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
    return out
IS = sheet("IS annual"); BS = sheet("BS annual"); CF = sheet("CF annual"); BSQ = sheet("BS quarterly"); ISQ = sheet("IS quarterly")
FY = {y: f"FY (ended {y}-12-31)" for y in (2009, 2010, 2011, 2012, 2013)}
def isv(line, y): return IS[line][FY[y]]
def bsv(line, y): return BS[line][FY[y]]
def cfv(line, y): return CF[line][FY[y]]
PTI = isv("Income before income taxes", 2013)   # 663.1
assert abs(PTI - 663.1) < 0.05
REC = "Receivables, less allowance for doubtful accounts of $30.8 and $29.3"
results = []
def rec(measure, label, reported, computed, tol, alt=False):
    """alt=True marks an alternative derivation tried for a figure; it is printed but not counted."""
    match = abs(computed - reported) <= tol
    if not alt:
        results.append((measure, label, reported, computed, match))
    print(f"  [{'alt' if alt else ('ok ' if match else 'NO ')}] {label}: reported {reported}, computed {computed:.4g}")

rev = {y: isv("Total revenues", y) for y in (2010, 2011, 2012, 2013)}
cost = {y: isv("Direct operating", y) + isv("Depreciation of revenue earning equipment and lease charges", y) for y in (2010, 2011, 2012, 2013)}
net = {y: bsv(REC, y) for y in (2010, 2011, 2012, 2013)}
ap = {y: bsv("Accounts payable", y) for y in (2010, 2011, 2012, 2013)}
inv = {y: bsv("Inventories, at lower of cost or market", y) for y in (2010, 2011, 2012, 2013)}
ta = {y: bsv("Total assets", y) for y in (2010, 2011, 2012, 2013)}
ni = {y: isv("Net income", y) for y in (2010, 2011, 2012, 2013)}
cfo = {y: cfv("Net cash provided by (used in) operating activities", y) for y in (2010, 2011, 2012, 2013)}
# Q4 figures from the FY2013 release (Q4 2012 on the release's revised basis)
q4rev = {2012: 2319.7, 2013: 2556.3}; q4cost = {2012: 1257.7 + 550.0, 2013: 1439.3 + 643.0}; q4sga = {2012: 331.1, 2013: 222.2}
q4pti = {2012: -43.1, 2013: 62.3}; q4ni = {2012: -36.8, 2013: -0.6}; q4cfo = {2012: 600.5, 2013: 753.5}
rec12 = 1879.7; ap12r = 1003.2; cars12r = 12548.8     # Revisions sheet / FY2013 p.75
Q = {"Q3-12": "Q3 (ended 2012-09-30)", "Q4-12": "Q4 (ended 2012-12-31)", "Q3-13": "Q3 (ended 2013-09-30)", "Q4-13": "Q4 (ended 2013-12-31)"}

# ---- M1 rental depreciation rate (K9): annual and Q4 same-quarter; cars and equipment split
print("\nM1 depreciation rate on rental equipment (K9)")
gross = {y: bsv("Cars", y) + bsv("Other equipment", y) for y in (2010, 2011, 2012, 2013)}
dep = {2011: 1921.8, 2012: 2165.2, 2013: 2407.8}       # FY2012 p.113; FY2013 p.126 (before the disposal adjustment)
rec("M1", "FY2011 rate % (16.2)", 16.2, dep[2011] / ((gross[2010] + gross[2011]) / 2) * 100, 0.05)
rec("M1", "FY2012 rate % (15.3)", 15.3, dep[2012] / ((gross[2011] + gross[2012]) / 2) * 100, 0.05)
rec("M1", "FY2013 rate % on the first-reported 2012 base (14.3)", 14.3, dep[2013] / ((gross[2012] + gross[2013]) / 2) * 100, 0.05, alt=True)
gross12r = cars12r + bsv("Other equipment", 2012)
rec("M1", "FY2013 rate % on the revised 2012 base (14.3)", 14.3, dep[2013] / ((gross12r + gross[2013]) / 2) * 100, 0.05)
def q(col): return BSQ["Cars"][col] + BSQ["Other equipment"][col]
q4_13 = 620.2 * 365 / 92 / ((q(Q["Q3-13"]) + q(Q["Q4-13"])) / 2)
q4_12 = 533.8 * 366 / 92 / ((q(Q["Q3-12"]) + q(Q["Q4-12"])) / 2)
rec("M1", "Q4 2012 rate, release line annualised by days % (13.7)", 13.7, q4_12 * 100, 0.06)
rec("M1", "Q4 2013 rate % (13.4)", 13.4, q4_13 * 100, 0.06)
car13 = 1269.3 + 532.0 + 425.4 - 80.5 - (48.2 + 15.2)      # p.131 segments less p.126 rents and disposal results
car12 = 940.6 + 528.2 + 388.0 - 79.8 - (-100.6 + 17.3)
eq13 = 298.8 + 26.2; eq12 = 272.1 + 13.5
rec("M1", "cars-only rate FY2012 % (16.7)", 16.7, car12 / ((bsv("Cars", 2011) + cars12r) / 2) * 100, 0.06)
rec("M1", "cars-only rate FY2013 % (15.4)", 15.4, car13 / ((cars12r + bsv("Cars", 2013)) / 2) * 100, 0.06)
rec("M1", "equipment rate FY2012 % (9.4)", 9.4, eq12 / ((bsv("Other equipment", 2011) + bsv("Other equipment", 2012)) / 2) * 100, 0.06)
rec("M1", "equipment rate FY2013 % (9.6)", 9.6, eq13 / ((bsv("Other equipment", 2012) + bsv("Other equipment", 2013)) / 2) * 100, 0.06)
pe_dep = {2011: 158.0, 2012: 172.6, 2013: 205.3}
pe_gross = {y: bsv("Total property and equipment, at cost", y) for y in (2010, 2011, 2012, 2013)}
for y, rep in ((2011, 7.6), (2012, 7.3), (2013, 7.9)):
    rec("M1", f"property and equipment rate FY{y} % ({rep})", rep, pe_dep[y] / ((pe_gross[y - 1] + pe_gross[y]) / 2) * 100, 0.06)

# ---- M2 item 1 sizes
print("\nM2 item 1 sizes: stated cut, charge not taken, exposure, cumulative cuts, per-car charges")
rec("M2", "$44.2m less $5.0m international increase, as the reply states it (39.2, reply says 39.6)", 39.2, 44.2 - 5.0, 0.01)
rec("M2", "net cuts 44.2 - 5.0 + 0.4 equipment (39.6; p.40 prints 39.6)", 39.6, 44.2 - 5.0 + 0.4, 0.01)
rec("M2", "$39.6m as % of pre-tax (6.0)", 6.0, 39.6 / PTI * 100, 0.05)
rec("M2", "$48.2m + $40.0m exposure as % (13.3)", 13.3, 88.2 / PTI * 100, 0.05)
rec("M2", "cumulative U.S. cuts 44.2 + 139.4 + 26.7 (210.3)", 210.3, 44.2 + 139.4 + 26.7, 0.01)
co13, co12, le13, le12 = 468500, 358000, 21500, 1100       # p.49
us13, us12 = 1269.3, 940.6                                  # p.131
pcm13_b = (us13 - 48.2) * 1e6 / (co13 * 12); pcm12_b = (us12 + 100.6) * 1e6 / (co12 * 12)   # before disposal results, company-operated cars
pcm13_a = us13 * 1e6 / (co13 * 12); pcm12_a = us12 * 1e6 / (co12 * 12)
rec("M2", "U.S. per car per month before disposal result FY2012 $ (242)", 242, pcm12_b, 0.5)
rec("M2", "same FY2013 $ (217)", 217, pcm13_b, 0.5)
rec("M2", "change % (-10)", -10, (pcm13_b / pcm12_b - 1) * 100, 0.6)
rec("M2", "after disposal result FY2012 $ (219)", 219, pcm12_a, 0.5)
rec("M2", "same FY2013 $ (226)", 226, pcm13_a, 0.5)
rec("M2", "change % (+3)", 3, (pcm13_a / pcm12_a - 1) * 100, 0.6)
short_co = (pcm12_b - pcm13_b) * co13 * 12 / 1e6
short_all = ((us12 + 100.6) / ((co12 + le12) * 12) - (us13 - 48.2) / ((co13 + le13) * 12)) * (co13 + le13) * 12
rec("M2", "U.S. charge not taken at the 2012 per-car rate, company-operated cars $m (reply 'about $139M')", 139, short_co, 3.0)
rec("M2", "same, company-operated plus leased cars $m (reply 'about $139M')", 139, short_all, 3.0, alt=True)
rec("M2", "same on the rounded $242 and $217 $m (reply 'about $139M')", 139, 25 * co13 * 12 / 1e6, 3.0, alt=True)
rec("M2", "$139m as % (21)", 21, 139 / PTI * 100, 0.06)
rec("M2", "fleet-wide charge not taken at the FY2012 rate $m (not in the reply; v2.26 174.5)", 174.5, dep[2012] / ((gross[2011] + gross[2012]) / 2) * (gross[2012] + gross[2013]) / 2 - dep[2013], 0.3, alt=True)

# ---- M3 allowance (K12)
print("\nM3 allowance for doubtful accounts (K12)")
allow = {2011: 20.3, 2012: 25.1, 2013: 30.8}
for y, rp in ((2011, 1.24), (2012, 1.31), (2013, 2.00)):
    rec("M3", f"allowance % of gross receivables {y} ({rp})", rp, allow[y] / (net[y] + allow[y]) * 100, 0.006)
rec("M3", "2012 revised % (1.53)", 1.53, 29.3 / (rec12 + 29.3) * 100, 0.006)
rec("M3", "allowance / write-offs FY2012 revised (1.00)", 1.00, 29.3 / 29.3, 0.006)
rec("M3", "allowance / write-offs FY2013 (0.76)", 0.76, 30.8 / 40.3, 0.006)
rec("M3", "provision 45.9 (cash flow) less 41.9 (Schedule II) (4.0)", 4.0, cfv("Provision for losses on doubtful accounts", 2013) - 41.9, 0.01)
rec("M3", "charge 41.9 against write-offs 40.3: ratio (reply 'roughly equal')", 1.04, 41.9 / 40.3, 0.006)
rec("M3", "Q4 2012 allowance % (1.53 on the revised base)", 1.53, 29.3 / (rec12 + 29.3) * 100, 0.006)

# ---- M4 adjusted measures (item 2)
print("\nM4 adjusted pre-tax income and exclusions (item 2)")
rec("M4", "gap 2013 1,153.2 - 663.1 (490.1)", 490.1, 1153.2 - PTI, 0.01)
rec("M4", "gap 2013 % (74)", 74, 490.1 / PTI * 100, 0.6)
rec("M4", "gap 2012 901.5 - 450.6 (450.9)", 450.9, 901.5 - 450.6, 0.01)
rec("M4", "gap 2012 % of revised 441.4 (102)", 102, 450.9 / 441.4 * 100, 0.6)
rec("M4", "restructuring plus related 98.8 % (14.9)", 14.9, 98.8 / PTI * 100, 0.05)
rec("M4", "restructuring 2007 to 2013: 568.4 + 77.0 (645.4, p.140)", 645.4, 568.4 + 77.0, 0.01)
rec("M4", "free cash flow 448.7 less fleet financing 133.9 (314.8)", 314.8, 448.7 - 133.9, 0.01)
rec("M4", "effective tax rate from the workbook % (47.8)", 47.8, -isv("Provision for taxes on income", 2013) / PTI * 100, 0.06)

# ---- M5 error corrections (K14, item 3)
print("\nM5 out-of-period errors (item 3)")
rec("M5", "34.7 as % of 2013 pre-tax (5.2)", 5.2, 34.7 / PTI * 100, 0.05)
rec("M5", "46.3 - 34.7 (11.6)", 11.6, 46.3 - 34.7, 0.01)
rec("M5", "release Q4 pre-tax 62.3 less workbook mixed-basis Q4 50.7 (11.6)", 11.6, 62.3 - ISQ["Income before income taxes"]["Q4 (ended 2013-12-31) [mixed basis]"], 0.01)
rec("M5", "Brazil allowance understatement 2012, 2011 ($3.6m, $6.2m; p.83)", 9.8, 3.6 + 6.2, 0.01)

# ---- M6 receivables (DSO, growth gap, the fall)
print("\nM6 receivables")
for y, rp in ((2011, 71.1), (2012, 76.3), (2013, 51.3)):
    rec("M6", f"DSO FY{y}, 365 days ({rp})", rp, net[y] / rev[y] * 365, 0.06)
rec("M6", "Q4 2012 DSO on 92 days (reply 74.5)", 74.5, net[2012] / q4rev[2012] * 92, 0.06)
rec("M6", "Q4 2012 DSO, Q4 revenue times four, 366 days (reply 74.5)", 74.5, net[2012] / (q4rev[2012] * 4) * 366, 0.06, alt=True)
rec("M6", "Q4 2013 DSO on 92 days (54.4)", 54.4, net[2013] / q4rev[2013] * 92, 0.06)
for y, rp in ((2011, 9.4), (2012, 8.0), (2013, -39.2)):
    rec("M6", f"receivables growth less revenue growth FY{y}, pts ({rp})", rp, ((net[y] / net[y - 1]) - (rev[y] / rev[y - 1])) * 100, 0.06)
rec("M6", "Q4 on Q4, first-reported 2012 base, pts (reply -29.5)", -29.5, ((net[2013] / net[2012]) - (q4rev[2013] / q4rev[2012])) * 100, 0.06, alt=True)
rec("M6", "Q4 on Q4, revised 2012 base, pts (reply -29.5)", -29.5, ((net[2013] / rec12) - (q4rev[2013] / q4rev[2012])) * 100, 0.06)
rec("M6", "fall in receivables, revised base 1,879.7 - 1,512.6 (367)", 367, rec12 - net[2013], 0.6)
rec("M6", "fleet-sale receivables 617.3 - 357.3 (260)", 260, 617.3 - 357.3, 0.6)
rec("M6", "operating receivables rose (cash flow line, 34.7)", 34.7, -cfv("Receivables", 2013), 0.01)
rec("M6", "reply's 'unexplained' 367.1 - 260.0 - 34.7 (72)", 72, 367.1 - 260.0 - 34.7, 0.6)
rec("M6", "unexplained if the 34.7 is a rise: 367.1 - 260.0 + 34.7 (142; not the reply's figure)", 142, 367.1 - 260.0 + 34.7, 0.6, alt=True)
rec("M6", "industry DSO 11.5% of sales times 365 (42)", 42, 0.115 * 365, 0.6)

# ---- M7 inventory and payables days, growth gaps, industry levels
print("\nM7 inventory, payables, industry levels")
for y, rp in ((2011, 4.7), (2012, 5.6), (2013, 4.1)):
    rec("M7", f"days inventory FY{y} ({rp})", rp, inv[y] / cost[y] * 365, 0.06)
rec("M7", "Q4 2012 days inventory (5.4)", 5.4, inv[2012] / q4cost[2012] * 92, 0.06)
rec("M7", "Q4 2013 days inventory (4.1)", 4.1, inv[2013] / q4cost[2013] * 92, 0.06)
for y, rp in ((2011, 50.6), (2012, 52.5), (2013, 42.7)):
    rec("M7", f"days payable FY{y}, 365 days ({rp})", rp, ap[y] / cost[y] * 365, 0.06)
rec("M7", "Q4 2012 days payable on 92 days, first-reported payables (reply 51.1)", 51.1, ap[2012] / q4cost[2012] * 92, 0.06, alt=True)
rec("M7", "Q4 2012 days payable, revised payables 1,003.2 (reply 51.1)", 51.1, ap12r / q4cost[2012] * 92, 0.06)
rec("M7", "Q4 2013 days payable (42.8)", 42.8, ap[2013] / q4cost[2013] * 92, 0.06)
for y, rp in ((2011, -9.1), (2012, 18.5), (2013, -31.9)):
    rec("M7", f"inventory growth less cost growth FY{y}, pts ({rp})", rp, ((inv[y] / inv[y - 1]) - (cost[y] / cost[y - 1])) * 100, 0.06)
rec("M7", "Q4 inventory gap, pts (-27.9)", -27.9, ((inv[2013] / inv[2012]) - (q4cost[2013] / q4cost[2012])) * 100, 0.06)
for y, rp in ((2011, -11.2), (2012, 4.0), (2013, -22.3)):
    rec("M7", f"payables growth less cost growth FY{y}, pts ({rp})", rp, ((ap[y] / ap[y - 1]) - (cost[y] / cost[y - 1])) * 100, 0.06)
rec("M7", "Q4 payables gap, revised 2012 payables, pts (-18.7)", -18.7, ((ap[2013] / ap12r) - (q4cost[2013] / q4cost[2012])) * 100, 0.06)
rec("M7", "inventory % of sales 2013 (0.9)", 0.9, inv[2013] / rev[2013] * 100, 0.06)
rec("M7", "payables % of sales 2013 (9.0)", 9.0, ap[2013] / rev[2013] * 100, 0.06)
gap = ap[2013] - 0.045 * rev[2013]
rec("M7", "payables above the industry 4.5% $m (483)", 483, gap, 0.6)
rec("M7", "that as % (73)", 73, gap / PTI * 100, 0.6)
rec("M7", "payables fell 10 days in 2013 (52.5 to 42.7)", 10, ap[2012] / cost[2012] * 365 - ap[2013] / cost[2013] * 365, 0.6)

# ---- M8 margins
print("\nM8 margins")
for y, gm, om, pm in ((2011, 22.0, 13.0, 3.9), (2012, 23.0, 12.5, 5.0), (2013, 23.2, 13.7, 6.2)):
    rec("M8", f"FY{y} gross margin % ({gm})", gm, (rev[y] - cost[y]) / rev[y] * 100, 0.06)
    rec("M8", f"FY{y} operating margin % ({om})", om, (rev[y] - cost[y] - isv("Selling, general and administrative", y)) / rev[y] * 100, 0.06)
    rec("M8", f"FY{y} pre-tax margin % ({pm})", pm, isv("Income before income taxes", y) / rev[y] * 100, 0.06)
for yq, gm, om, pm in ((2012, 22.1, 7.8, -1.9), (2013, 18.5, 9.9, 2.4)):
    rec("M8", f"Q4 {yq} gross margin % ({gm})", gm, (q4rev[yq] - q4cost[yq]) / q4rev[yq] * 100, 0.06)
    rec("M8", f"Q4 {yq} operating margin % ({om})", om, (q4rev[yq] - q4cost[yq] - q4sga[yq]) / q4rev[yq] * 100, 0.06)
    rec("M8", f"Q4 {yq} pre-tax margin % ({pm})", pm, q4pti[yq] / q4rev[yq] * 100, 0.06)
fall = (q4rev[2012] - q4cost[2012]) / q4rev[2012] - (q4rev[2013] - q4cost[2013]) / q4rev[2013]
rec("M8", "Q4 gross margin fall, pts (3.5)", 3.5, fall * 100, 0.06)
rec("M8", "fall times Q4 revenue $m (90)", 90, fall * q4rev[2013], 0.6)
rec("M8", "that as % (13.6)", 13.6, fall * q4rev[2013] / PTI * 100, 0.06)
rec("M8", "$0.12 x 463.9m shares / (1 - 0.35) $m pre-tax (about 86)", 86, 0.12 * 463.9 / 0.65, 0.6)
rec("M8", "Q4 2012 SG&A 331.1 carried 126.4 of acquisition costs (release)", 126.4, 126.4, 0.01)

# ---- M9 accruals, free cash flow, capital spending
print("\nM9 accruals, free cash flow, capital spending")
for y, rp in ((2011, -11.6), (2012, -12.1), (2013, -13.6)):
    rec("M9", f"accruals % of average assets FY{y} ({rp})", rp, (ni[y] - cfo[y]) / ((ta[y - 1] + ta[y]) / 2) * 100, 0.06)
avgq = {2012: (BSQ["Total assets"][Q["Q3-12"]] + BSQ["Total assets"][Q["Q4-12"]]) / 2, 2013: (BSQ["Total assets"][Q["Q3-13"]] + BSQ["Total assets"][Q["Q4-13"]]) / 2}
rec("M9", "Q4 2012 accruals annualised % (-11.8)", -11.8, (q4ni[2012] - q4cfo[2012]) * 366 / 92 / avgq[2012] * 100, 0.06)
rec("M9", "Q4 2013 accruals annualised % (-11.9)", -11.9, (q4ni[2013] - q4cfo[2013]) * 365 / 92 / avgq[2013] * 100, 0.06)
def fcf(y):
    return (cfo[y] + cfv("Revenue earning equipment expenditures", y) + cfv("Proceeds from disposal of revenue earning equipment", y)
            + cfv("Property and equipment expenditures", y) + cfv("Proceeds from disposal of property and equipment", y))
for y, rp in ((2011, 401.5), (2012, 54.8), (2013, 314.5)):
    rec("M9", f"free cash flow FY{y} $m ({rp})", rp, fcf(y), 0.3)
for y, rp in ((2011, -205.8), (2012, 188.3), (2013, 31.7)):
    rec("M9", f"net income less free cash flow FY{y} ({rp})", rp, ni[y] - fcf(y), 0.3)
q4fcf = {2012: 600.5 + 357.9 - 40.3, 2013: 753.5 + 616.3 - 56.6}     # release: operating cash flow, net fleet capex, net property capex
rec("M9", "Q4 2012 free cash flow $m (918.0)", 918.0, q4fcf[2012], 0.3)
rec("M9", "Q4 2013 free cash flow $m (1,313.2)", 1313.2, q4fcf[2013], 0.3)
rec("M9", "Q4 2012 net income less free cash flow (-954.8)", -954.8, q4ni[2012] - q4fcf[2012], 0.3)
rec("M9", "Q4 2013 net income less free cash flow (-1,313.8)", -1313.8, q4ni[2013] - q4fcf[2013], 0.3)
def capex(y):
    return -(cfv("Revenue earning equipment expenditures", y) + cfv("Proceeds from disposal of revenue earning equipment", y)
             + cfv("Property and equipment expenditures", y) + cfv("Proceeds from disposal of property and equipment", y))
for y, rp in ((2011, 0.93), (2012, 1.19), (2013, 1.24)):
    rec("M9", f"net capital spending / depreciation FY{y} ({rp})", rp, capex(y) / (cfv("Depreciation of revenue earning equipment", y) + cfv("Depreciation of property and equipment", y)), 0.006)
rec("M9", "Q4 2013 net capital spending / depreciation (reply 1.4): net spending is negative", 1.4, -(616.3 - 56.6) / (620.2 + 55.6), 0.06)
rec("M9", "nearest: Q4 2013 gross fleet purchases 978.6 / Q4 depreciation 675.8 (reply 1.4)", 1.4, 978.6 / (620.2 + 55.6), 0.06, alt=True)
nine12 = 492.0 + 666.4 + 971.5
rec("M9", "Q4 2012 operating cash flow implied by revised annual less first-reported nine months (reply 578.5)", 578.5, 2709.7 - nine12, 0.06)

# ---- M10 Beneish M-score with components (K10)
print("\nM10 Beneish M-score, 2013 on 2012 (K10)")
dso13 = net[2013] / rev[2013] * 365; dso12 = net[2012] / rev[2012] * 365
DSRI = dso13 / dso12
GMI = ((rev[2012] - cost[2012]) / rev[2012]) / ((rev[2013] - cost[2013]) / rev[2013])
def ca(y): return bsv("Cash and cash equivalents", y) + bsv("Restricted cash and cash equivalents", y) + net[y] + inv[y] + bsv("Prepaid expenses and other assets", y)
def ppe(y): return bsv("Total revenue earning equipment", y) + bsv("Total property and equipment", y)
AQI = (1 - (ca(2013) + ppe(2013)) / ta[2013]) / (1 - (ca(2012) + ppe(2012)) / ta[2012])
SGI = rev[2013] / rev[2012]
d = {y: cfv("Depreciation of revenue earning equipment", y) + cfv("Depreciation of property and equipment", y) for y in (2012, 2013)}
DEPI = (d[2012] / (d[2012] + ppe(2012))) / (d[2013] / (d[2013] + ppe(2013)))
SGAI = (isv("Selling, general and administrative", 2013) / rev[2013]) / (isv("Selling, general and administrative", 2012) / rev[2012])
LVGI = (bsv("Total liabilities", 2013) / ta[2013]) / (bsv("Total liabilities", 2012) / ta[2012])
TATA = (ni[2013] - cfo[2013]) / ta[2013]
M = -4.84 + 0.92 * DSRI + 0.528 * GMI + 0.404 * AQI + 0.892 * SGI + 0.115 * DEPI - 0.172 * SGAI + 4.679 * TATA - 0.327 * LVGI
for lab, rp, v in (("DSRI", 0.67, DSRI), ("GMI", 0.99, GMI), ("AQI", 0.93, AQI), ("SGI", 1.19, SGI), ("DEPI", 0.94, DEPI), ("SGAI", 0.91, SGAI), ("LVGI", 0.99, LVGI), ("TATA", -0.13, TATA)):
    rec("M10", f"{lab} ({rp})", rp, v, 0.006)
rec("M10", "M-score 2013 (-3.25)", -3.25, M, 0.006)
rec("M10", "DEPI contribution 0.115 x DEPI (not shown in the reply)", 0.115 * DEPI, 0.115 * DEPI, 0.001, alt=True)
# 2012 on 2011 pair
dso11 = net[2011] / rev[2011] * 365
DSRI2 = dso12 / dso11; GMI2 = ((rev[2011] - cost[2011]) / rev[2011]) / ((rev[2012] - cost[2012]) / rev[2012])
AQI2 = (1 - (ca(2012) + ppe(2012)) / ta[2012]) / (1 - (ca(2011) + ppe(2011)) / ta[2011]); SGI2 = rev[2012] / rev[2011]
d11 = cfv("Depreciation of revenue earning equipment", 2011) + cfv("Depreciation of property and equipment", 2011)
DEPI2 = (d11 / (d11 + ppe(2011))) / (d[2012] / (d[2012] + ppe(2012)))
SGAI2 = (isv("Selling, general and administrative", 2012) / rev[2012]) / (isv("Selling, general and administrative", 2011) / rev[2011])
LVGI2 = (bsv("Total liabilities", 2012) / ta[2012]) / (bsv("Total liabilities", 2011) / ta[2011]); TATA2 = (ni[2012] - cfo[2012]) / ta[2012]
M2 = -4.84 + 0.92 * DSRI2 + 0.528 * GMI2 + 0.404 * AQI2 + 0.892 * SGI2 + 0.115 * DEPI2 - 0.172 * SGAI2 + 4.679 * TATA2 - 0.327 * LVGI2
rec("M10", "M-score 2012 (-2.73)", -2.73, M2, 0.006)
# public liability reserve (Checked and explained)
pl = {2011: bsv("Public liability and property damage", 2011), 2012: bsv("Public liability and property damage", 2012), 2013: bsv("Public liability and property damage", 2013)}
car = {2011: isv("Worldwide car rental", 2011), 2012: 7161.7, 2013: isv("Worldwide car rental", 2013)}   # 2012 revised, FY2013 p.39
rec("M10", "public liability reserve growth % (4.7)", 4.7, (pl[2013] / pl[2012] - 1) * 100, 0.06)
rec("M10", "car rental revenue growth on the revised 2012 base % (21.6)", 21.6, (car[2013] / car[2012] - 1) * 100, 0.06)
rec("M10", "reserve % of car rental revenue 2013 (3.99)", 3.99, pl[2013] / car[2013] * 100, 0.006)
rec("M10", "same 2011 (4.06)", 4.06, pl[2011] / car[2011] * 100, 0.006)
rec("M10", "shortfall at the 2011 share $m (reply '$5M')", 5, pl[2011] / car[2011] * car[2013] - pl[2013], 0.6)
rec("M10", "prepaid and other assets rise, revised 2012 base 717.2 - 489.3 (228)", 228, 717.2 - 489.3, 0.6)
rec("M10", "accrued liabilities % of revenue 2012 revised (12.9)", 12.9, 1163.1 / 9024.9 * 100, 0.06)
rec("M10", "same 2013 (10.3)", 10.3, 1104.7 / rev[2013] * 100, 0.06)
rec("M10", "accrued liabilities at the 2012 share less actual $m (284)", 284, 1163.1 / 9024.9 * rev[2013] - 1104.7, 0.6)
rec("M10", "that as % (43)", 43, (1163.1 / 9024.9 * rev[2013] - 1104.7) / PTI * 100, 0.6)
rec("M10", "balance fall 58.4 against cash-flow source 25.2: gap (83.6)", 83.6, (1163.1 - 1104.7) + 25.2, 0.06)
rec("M10", "Sobel $40.0m as % (6.0)", 6.0, 40.0 / PTI * 100, 0.06)

n_ok = sum(1 for r in results if r[4]); print(f"\nSub-figures: {n_ok} of {len(results)} match at the reply's rounding")
for r in results:
    if not r[4]:
        print("  mismatch:", r[0], r[1], "reported", r[2], "computed", round(r[3], 3))

# ------------------------------------------------------------- reply scans
print("\nReply scan (report-5.txt)")
t = open(os.path.join(RUN, "report-5.txt"), encoding="utf-8").read()
banned = r"\bfraud|manipulat|red flag|misstat|suspicious|material weakness|aggressive"
traps = (r"planned holding|21 to|25 months|24 or 30|disposed cars|affirmative|attorney|rolling|spreadsheet error|"
         r"9\.3 million|tone at the top|\b235\b|June 2014|May 2014|November 2014|2015|1\.78|1\.68|1\.72|1\.66|1\.65|budget|"
         r"\b1\.82\b|\b1\.63\b|extended holding|subrogation|Manheim|restat")
print("  banned:", re.findall(banned, t, re.I))
print("  trap or key terms:", re.findall(traps, t, re.I))
for w in ("eighteen", "18 / 18", "longer holding", "p.53", "p.126", "optimization", "Dollar Thrifty", "maintenance", "2014", "late 2013", "Absorbed", "Level 1", "Level 2", "Level 3"):
    print(f"  {w!r}: {len(re.findall(re.escape(w), t))}")
print("  words:", len(t.split()), "; em-dashes:", t.count(EM))
