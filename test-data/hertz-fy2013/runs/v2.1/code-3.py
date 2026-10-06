# Turn 3: read the footnotes. Tests of claims in the notes, then a quotation check on reply-3.md.
import re, sys, io, os, datetime

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
D = r"C:\Users\aaron\OneDrive\Desktop\Master\WireSift Research\Events\CFA Vancouver Forensic\test-data\hertz-fy2013"
OUT = D + r"\runs\v2.1"
DOCS = {
    "FY2013 annual report": "annual-report-FY2013-12-31-key-sections.txt",
    "FY2012 annual report": "annual-report-FY2012-12-31-key-sections.txt",
    "FY2013 release": "earnings-release-Q4-FY2013-12-31.txt",
    "FY2012 release": "earnings-release-Q4-FY2012-12-31.txt",
}
TXT = {k: open(os.path.join(D, v), encoding="utf-8").read() for k, v in DOCS.items()}
A13, A12, R13, R12 = (TXT[k] for k in DOCS)


def page_at(text, pos):
    m = re.findall(r"\[p\. (\w+)\]", text[:pos])
    return m[-1] if m else None


def check_quotes(reply_path, labels=()):
    reply = open(reply_path, encoding="utf-8").read()
    cited = re.findall(r'"([^"]+)" \(((?:FY2013|FY2012) (?:annual report|release))[^)]*?, p\. (\w+)\)', reply)
    allq = re.findall(r'"([^"]+)"', reply)
    ok = 0
    for q, doc, pg in cited:
        t = TXT[doc]
        pages = [page_at(t, m.start()) for m in re.finditer(re.escape(q), t)]
        good = pg in pages
        ok += good
        print(("PASS" if good else "FAIL"), f"| {doc} p. {pg} | found on pages {sorted(set(pages))} | {q[:70]}")
    citedset = {q for q, _, _ in cited}
    for q in allq:
        if q not in citedset and q not in labels:
            print("UNCITED quoted string:", q[:80], "| found in:", [k for k, t in TXT.items() if q in t])
    print(f"{len(cited)} cited quotations, {ok} pass")
    return len(cited), ok


def has(text, s):
    assert s in text, s


if __name__ == "__main__":
    print("=== Correction of errors (Note 2) ===")
    has(A13, "reduced pre-tax income by $12.9 million in 2011 and $2.4 million in 2012")
    has(A13, "reduced pre-tax income by $4.4 million in 2010, $6.2 million in 2011 and $3.6 million in 2012")
    has(A13, "decreased pre-tax income by $2.4 million in 2010 and $3.2 million in 2012, and increased pre-tax income by $0.4 million in 2011")
    vendor = {2011: 12.9, 2012: 2.4}; brazil = {2010: 4.4, 2011: 6.2, 2012: 3.6}; other = {2010: 2.4, 2012: 3.2, 2011: -0.4}
    by_year = {y: vendor.get(y, 0) + brazil.get(y, 0) + other.get(y, 0) for y in (2010, 2011, 2012)}
    prior = sum(by_year.values())
    print("By year, reduction of pre-tax income:", {y: round(v, 1) for y, v in by_year.items()}, "total", round(prior, 1), "(stated 34.7)")
    has(A13, "Income before income taxes | 450.6 | (9.2) | 441.4 | 324.3 | (18.7) | 305.6")
    has(A13, "Income before income taxes | 328.3 | (7.0) | 321.3 | 612.4 | (11.6) | 600.8")
    print(f"Remainder in 2013: 46.3 - 34.7 = {46.3-34.7:.1f} (nine-month table shows 11.6)")
    print(f"34.7 as % of Q4 2013 pre-tax income 62.3: {100*34.7/62.3:.0f}%; 46.3 as % of FY2013 pre-tax 663.1: {100*46.3/663.1:.1f}%")
    has(R13, "These out of period errors totaling $47.9 million"); has(A13, "out of period errors totaling $46.3 million")
    print(f"Release total 47.9 vs annual report 46.3: difference {47.9-46.3:.1f}")
    print(f"Vendor incentives moved out of SG&A: 2012 25.9, 2011 22.4, nine months 2013 21.2; into depreciation: 23.6, 9.5, 22.1; net {25.9-23.6:.1f}, {22.4-9.5:.1f}, {21.2-22.1:.1f}")
    has(A13, "concluded that our disclosure controls and procedures are effective")
    has(A13, "internal control over financial reporting was effective as of December 31, 2013")

    print("\n=== Adjusted net income tax rate ===")
    has(R13, "Assumed provision for income taxes at 35% in 2013 and 34% in 2012 | (403.6) | (303.4)")
    has(A13, "Effective Tax Rate | 47.8% | 45.9% | 39.9%")
    adj = 1153.2
    at35 = adj * (1 - 0.35); at478 = adj * (1 - 0.478)
    print(f"Adjusted pre-tax 1,153.2: at 35% {at35:.1f} (reported 749.6); at 47.8% {at478:.1f}; difference {at35-at478:.1f}")
    has(A13, "This adjustment for December 31, 2013, 2012 and 2011 was $7.7 million")
    print(f"Adjusted diluted EPS: ({749.6}+7.7)/463.9 = {(749.6+7.7)/463.9:.2f}; at 47.8%: {(at478+7.7)/463.9:.2f}")
    print(f"2012 (revised): 892.3 at 34% = {892.3*0.66:.1f} (reported 588.9); at 45.9% {892.3*(1-0.459):.1f}")
    has(A13, "Income taxes | 70.9 | 71.7 | 49.6")
    print(f"Cash taxes paid 70.9 = {100*70.9/663.1:.1f}% of pre-tax income 663.1; provision 316.9; deferred 245.2 = {100*245.2/316.9:.0f}% of provision")
    has(A13, "Federal | $(7.9) | $8.0 | $0.6"); has(A13, "Domestic | $551.2 | $349.9 | $173.9")
    has(A13, "Change in valuation allowance | 5.7 | 9.0 | 0.7"); has(A13, "Federal and foreign permanent differences | 4.9 | 2.7 | —")
    print(f"Valuation allowance and permanent differences add {5.7+4.9:.1f} points in 2013")
    has(A13, "Year ended December 31, 2013 | $226.4 | $37.9 | $15.1 | $— | $279.4")
    print(f"Valuation allowance 226.4 -> 279.4: +{279.4-226.4:.1f}; charged to expense 37.9 (2013) vs 39.8 (2012); 5.7% x 663.1 = {0.057*663.1:.1f}")

    print("\n=== Amortization event (Note 5, Note 19) ===")
    has(A13, "HVF II Series 2013-A(4) | 1.02% | Floating | 11/2015 | 2,380.0 | —"); has(A13, "HVF II Series 2013-B(4) | 1.02% | Floating | 11/2015 | 585.0 | —")
    print(f"HVF II notes outstanding {2380.0+585.0:.1f} = {100*(2380.0+585.0)/16309.4:.1f}% of total debt 16,309.4; Series 2013-B alone 585.0")
    has(A13, "HVF Series 2009-1(4) | 0.99% | Floating | 11/2015 | 60.0 | 2,350.0")
    print(f"All U.S. rental car variable funding notes: {2380.0+585.0+60.0:.1f} = {100*(2380.0+585.0+60.0)/16309.4:.1f}% of total debt")
    has(A13, "Total | $2,197.8 | $1,180.6"); has(A13, "2014 | $2,053.3 | (including $927.2 of other short-term borrowings*)")
    print(f"Cash 423.2 + availability 1,180.6 = {423.2+1180.6:.1f} against 2014 maturities 2,053.3 ({100*(423.2+1180.6)/2053.3:.0f}%)")
    has(A13, "Total Fleet Debt | 1,041.1 | 23.9"); has(A12, "Total Fleet Debt | 1,083.5 | 35.4")
    print("Fleet debt availability under borrowing base: 23.9 of 1,041.1 capacity (2013) vs 35.4 of 1,083.5 (2012)")
    print("Days from set-up of HVF II (25 Nov 2013) to year end:", (datetime.date(2013, 12, 31) - datetime.date(2013, 11, 25)).days)

    print("\n=== Also noted ===")
    has(A13, "Other intangible assets | 3 to 10 years"); has(A13, "which range from two to fifteen years")
    has(A13, "Customer relationships | 16 | $65.0"); has(A13, "Trademark | 20 | 7.0")
    print("Intangible lives: table 3 to 10 years; text two to fifteen years; Donlen customer relationships 16, trademark 20")
    has(A13, "A judgment - which could potentially exceed $40.0 million")
    print(f"Nevada judgment 40.0 = {100*40.0/663.1:.1f}% of pre-tax income")
    has(A13, "we recorded an impairment charge of $40.0 million"); has(A13, "Subleased Vehicles - Advantage | $279 million")
    print(f"Advantage subleased vehicles: 40.0 written off against fair value 279 -> {100*40/(279+40):.1f}% of carrying value before the charge")
    has(A13, "Minimum fixed obligations | 404.8 | 263.7 | 248.8"); has(A13, "Additional amounts, based on revenues | 294.6 | 316.2 | 311.6")
    print(f"Concession minimums expensed {100*(404.8/263.7-1):+.1f}%; revenue-based {100*(294.6/316.2-1):+.1f}%")
    rents = 141.3 + 116.9 + 88.9 + 66.8 + 46.5 + 195.7; conc = 407.9 + 310.3 + 249.1 + 188.9 + 152.0 + 685.6; eq = 52.6 + 16.0 + 8.0 + 1.2
    has(A13, "Operating leases and concession agreements(3) | 2,727.7"); has(A13, "Purchase obligations(5) | 4,757.6")
    print(f"Lease and concession minimums: rents {rents:.1f} + concessions {conc:.1f} + equipment {eq:.1f} = {rents+conc+eq:.1f} (table 2,727.7)")
    has(A13, "we incurred $645.4 million"); has(A13, "Balance as of December 31, 2013 | $20.1 | $— | $0.2 | $28.1 | $48.4")
    print(f"Restructuring: 645.4 over 2007-2013 = {645.4/7:.1f} a year; accrual 21.0 -> 48.4")
    has(A13, "was $3.1 million for the executive officers")
    has(A13, "outstanding standby letters of credit totaling $644.9 million")
    print(f"Trade name 3,330.0 + goodwill 1,347.5 = {3330.0+1347.5:.1f} vs equity 2,771.2 ({(3330.0+1347.5)/2771.2:.2f}x)")
    has(A13, "resulted in an adjustment to the numerator (net income) of our earnings per share computation")
    has(A13, "Adjustments to previously recorded purchase price allocation(a) | 13.2 | — | — | — | 13.2")
    has(A13, "This revision had no impact on the Company's total operating, investing or financing cash flows")
    has(A13, "Such revisions have no impact on our consolidated financial condition, results of operations or cash flows")

    if os.path.exists(OUT + r"\reply-3.md"):
        print("\n=== Quotation check, reply-3.md ===")
        check_quotes(OUT + r"\reply-3.md")
