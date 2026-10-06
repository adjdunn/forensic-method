# Turn 2: follow the flags. Tests of the company's explanations, then a quotation check on reply-2.md.
import re, sys, io, os
import openpyxl

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
    """Every "quote" (document, p. N) in the reply must be an exact substring of that document
    with [p. N] as the nearest page marker above one of its occurrences."""
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
            where = [k for k, t in TXT.items() if q in t]
            print("UNCITED quoted string:", q[:80], "| found in:", where)
    print(f"{len(cited)} cited quotations, {ok} pass")
    return len(cited), ok


def has(text, s):
    assert s in text, s
    return True


wb = openpyxl.load_workbook(D + r"\statements.xlsx", data_only=True)
def row(sheet, label, nth=1):
    ws = wb[sheet]; rows = list(ws.iter_rows(values_only=True)); hdr = rows[0]; n = 0
    for r in rows[1:]:
        if r[0] == label:
            n += 1
            if n == nth:
                return {hdr[i]: r[i] for i in range(1, len(hdr) - 1)}
fy = lambda y: f"FY (ended {y}-12-31)"; q = lambda n, y: {3: f"Q3 (ended {y}-09-30)", 4: f"Q4 (ended {y}-12-31)"}[n]
g = lambda a, b: 100 * (a / b - 1)

if __name__ == "__main__":
    BSa_cars, BSa_oeq = row("BS annual", "Cars"), row("BS annual", "Other equipment")
    BSq_cars, BSq_oeq = row("BS quarterly", "Cars"), row("BS quarterly", "Other equipment")

    print("=== Flag: rental equipment depreciation ===")
    # Note 8, FY2013 annual report (2012 and 2011 as revised) and FY2012 annual report (as first reported)
    has(A13, "Depreciation of revenue earning equipment | $2,407.8 | $2,145.9 | $1,912.3")
    has(A13, "Adjustment of depreciation upon disposal of revenue earning equipment | 37.2 | (96.8) | (112.2)")
    has(A12, "Depreciation of revenue earning equipment | $2,165.2 | $1,921.8 | $1,747.0")
    dep = {2013: 2407.8, 2012: 2145.9, 2011: 1912.3}
    disp = {2013: 37.2, 2012: -96.8, 2011: -112.2}
    has(A13, "Cars | 14,456.6 | 12,548.8")
    gross = {2010: BSa_cars[fy(2010)] + BSa_oeq[fy(2010)], 2011: BSa_cars[fy(2011)] + BSa_oeq[fy(2011)],
             2012: 12548.8 + 3240.1, 2013: BSa_cars[fy(2013)] + BSa_oeq[fy(2013)]}   # 2012 as revised
    for y in (2011, 2012, 2013):
        print(y, f"depreciation before disposal results {dep[y]} / average gross equipment {(gross[y]+gross[y-1])/2:,.1f} = {100*dep[y]/((gross[y]+gross[y-1])/2):.1f}%")
    print(f"Disposal result: 2012 gain {-disp[2012]} to 2013 loss {disp[2013]}: swing {disp[2013]-disp[2012]:.1f}")
    has(A13, "net losses of $48.2 million, and net gains of $100.6 million and $114.9 million")
    print(f"U.S. car disposals: gain 100.6 (2012) to loss 48.2 (2013): swing {48.2+100.6:.1f}")
    has(A13, "net decreases of $44.2 million, $139.4 million and $26.7 million")
    has(A13, "net increases of $5.0 million, $8.8 million and $12.9 million")
    has(A13, "a decrease of $0.4 million, an increase of $0.5 million, and a decrease of $4.4 million")
    net13, net12, net11 = -44.2 + 5.0 - 0.4, -139.4 + 8.8 + 0.5, -26.7 + 12.9 - 4.4
    print(f"Net effect of rate changes on depreciation: 2013 {net13:.1f}, 2012 {net12:.1f}, 2011 {net11:.1f}")
    print(f"  as % of pre-tax income: 2013 {100*-net13/663.1:.1f}% of 663.1; 2012 {100*-net12/441.4:.1f}% of 441.4 (revised)")
    print(f"  U.S. rate cuts over 2011-2013: {44.2+139.4+26.7:.1f}")
    # per-vehicle test, U.S. and international (FY2013 annual report p. 49 and p. 54)
    has(A13, "Average number of cars (Company-operated) | 468,500 | 358,000 | 321,700")
    has(A13, "Average number of cars (Leased) | 21,500 | 1,100 | —")
    has(A13, "$1,269.3 million for 2013 increased $328.7 million, or 34.9% from $940.6 million for 2012")
    us13, us12 = 1269.3e6 / 468500 / 12, 940.6e6 / 358000 / 12
    us13l, us12l = 1269.3e6 / (468500 + 21500) / 12, 940.6e6 / (358000 + 1100) / 12
    print(f"U.S. depreciation and lease charges per company-operated car per month: 2013 ${us13:.0f} vs 2012 ${us12:.0f}: {g(us13,us12):+.1f}%")
    print(f"  including leased cars: ${us13l:.0f} vs ${us12l:.0f}: {g(us13l,us12l):+.1f}%")
    has(A13, "Average number of cars (Company-operated) | 159,700 | 153,700 | 156,900")
    i13, i12 = 532.0e6 / 159700 / 12, 528.2e6 / 153700 / 12
    print(f"International per car per month: ${i13:.0f} vs ${i12:.0f}: {g(i13,i12):+.1f}%")
    # Q4 on the release basis (FY2013 release, Table 7 and Table 5)
    has(R13, "Depreciation of revenue earning equipment | 333.4 | 102.0 | 75.7 | 109.1 | 620.2 | 245.9 | 111.9 | 73.9 | 102.1 | 533.8")
    a13 = (BSq_cars[q(4, 2013)] + BSq_oeq[q(4, 2013)] + BSq_cars[q(3, 2013)] + BSq_oeq[q(3, 2013)]) / 2
    a12 = (BSq_cars[q(4, 2012)] + BSq_oeq[q(4, 2012)] + BSq_cars[q(3, 2012)] + BSq_oeq[q(3, 2012)]) / 2
    print(f"Q4 depreciation of revenue earning equipment (release, revised basis) 620.2 vs 533.8: {g(620.2,533.8):+.1f}%; average gross equipment {g(a13,a12):+.1f}%")
    print(f"  Q4 rate annualised {100*4*620.2/a13:.1f}% vs {100*4*533.8/a12:.1f}% (turn 1, mixed basis: 13.0% vs 13.9%)")
    has(R13, "Average number of cars (Company-operated) | 472,200 | 22.4% | 468,500 | 31.2%")
    q4us13 = 333.4e6 / 472200 / 3; q4us12 = 246.0e6 / (472200 / 1.224) / 3
    print(f"Q4 U.S. depreciation and lease charges per company-operated car per month: ${q4us13:.0f} vs ${q4us12:.0f}: {g(q4us13,q4us12):+.1f}% (333.4 vs 246.0 is {g(333.4,246.0):+.1f}%, cars +22.4%)")

    print("\n=== Flag: receivables ===")
    has(A13, "Receivables, less allowance for doubtful accounts of $30.8 and $29.3 | 1,512.6 | 1,879.7")
    has(A13, "Sales of revenue earning equipment included in receivables | 357.3 | 618.6 | 620.7")
    rec13, rec12, fl13, fl12 = 1512.6, 1879.7, 357.3, 618.6     # revised basis for 2012
    print(f"Receivables fell {rec12-rec13:.1f} ({g(rec13,rec12):.1f}%); fleet sale receivables fell {fl12-fl13:.1f} ({g(fl13,fl12):.1f}%) = {100*(fl12-fl13)/(rec12-rec13):.0f}% of the fall")
    o13, o12 = rec13 - fl13, rec12 - fl12
    print(f"Other receivables {o12:.1f} -> {o13:.1f}: {g(o13,o12):.1f}% (fall {o12-o13:.1f}) against revenue {g(10771.9,9024.9):+.1f}%")
    print(f"  days of revenue in other receivables: 2013 {o13/10771.9*365:.0f}, 2012 {o12/9024.9*366:.0f}, 2011 {(1616.4-620.7)/8299.3*365:.0f}")
    has(A13, "Receivables | (34.7) | (149.2) | (73.6)")
    has(A13, "Sales of property and equipment included in receivables | 16.6 | 0.9 | 41.8")
    resid = (rec13 - rec12) - (34.7 - 45.9 - (fl12 - fl13) + (16.6 - 0.9))
    print(f"Cash flow statement: receivables rose 34.7 in operations; balance sheet fell {rec12-rec13:.1f}. After the provision (45.9), fleet (-{fl12-fl13:.1f}) and property (+{16.6-0.9:.1f}) sale receivables, unexplained change {resid:.1f}")
    has(R13, "Proceeds from disposal of revenue earning equipment | 839.3 | 587.9 | 37.6 | 130.1 | 1,594.9 | 1,316.7 | 770.8 | 50.0 | 148.7 | 2,286.2")
    print(f"Q4 disposal proceeds 1,594.9 vs 2,286.2: {g(1594.9,2286.2):.1f}%; fleet receivables / Q4 proceeds: 2013 {100*fl13/1594.9:.0f}%, 2012 {100*fl12/2286.2:.0f}%, 2011 {100*620.7/2918.0:.0f}%")
    has(A13, "Year ended December 31, 2013 | $29.3 | $41.9 | $(0.1) | $(40.3) | (a) | $30.8")
    has(A13, "Provision for losses on doubtful accounts | 45.9 | 38.3 | 28.2")
    print(f"Allowance: charged to expense 41.9 (Schedule II) vs 45.9 (cash flow statement), difference {45.9-41.9:.1f}; write-offs 40.3 vs 29.3: {g(40.3,29.3):+.1f}%")

    print("\n=== Flag: Q4 2013 fleet purchases ===")
    has(A13, "Fourth Quarter | 978.6 | (1,594.9) | (616.3) | 67.4 | (10.7) | 56.7")
    has(A13, "Fourth Quarter | 1,928.3 | (2,286.2) | (357.9) | 75.5 | (35.2) | 40.3")
    has(R13, "Revenue earning equipment expenditures | $(662.3) | $(19.2) | $(90.0) | $(207.1) | $(978.6) | $(1,183.9) | $(344.0) | $(156.4) | $(244.0) | $(1,928.3)")
    print(f"Q4 purchases 978.6 vs 1,928.3: {g(978.6,1928.3):.1f}% (fall {1928.3-978.6:.1f}); spreadsheet derived 957.4 vs 1,932.2")
    for nm, a, b in [("U.S.", 662.3, 1183.9), ("International", 19.2, 344.0), ("Equipment", 90.0, 156.4), ("All other", 207.1, 244.0)]:
        print(f"  {nm}: {a} vs {b}: {g(a,b):.1f}%, {100*(b-a)/(1928.3-978.6):.0f}% of the fall")
    print(f"  Q4 disposal proceeds: total {g(1594.9,2286.2):.1f}%, U.S. 839.3 vs 1,316.7 {g(839.3,1316.7):.1f}%, International 587.9 vs 770.8 {g(587.9,770.8):.1f}%")
    has(R13, "Transaction days (in thousands) (a) | 32,875 | 16.1% | 133,181 | 26.2%")
    has(R13, "Average number of cars (Company-operated) | 154,300 | 3.6% | 159,700 | 3.9%")
    print("  U.S. Q4: average cars +22.4% vs transaction days +16.1%: gap", round(22.4 - 16.1, 1), "pts; international cars +3.6%, days +5.5%")
    has(A13, "$4,457.5 million represent fleet purchases"); has(A12, "$5,236.1 million represent fleet purchases")
    print(f"  Fleet purchase commitments at year end: 4,457.5 vs 5,236.1: {g(4457.5,5236.1):.1f}%")
    has(R13, "Free cash flow | $428.2 | $442.5 | $448.7 | $155.1")
    print(f"  Company free cash flow 2013 448.7, of which Q4 428.2 ({100*428.2/448.7:.0f}%)")

    print("\n=== Other flags ===")
    has(R13, "Direct operating | 1,439.3 | 1,257.7 | 56.3% | 54.2%")
    has(R13, "Direct operating | 1,439.3 | (62.1 | )(a) | 1,377.2 | 1,257.7 | (42.7 | )(a) | 1,215.0")
    print(f"Q4 direct operating, revised basis: {100*1439.3/2556.3:.1f}% vs {100*1257.7/2319.7:.1f}%; after the company's adjustments {100*1377.2/2556.3:.1f}% vs {100*1215.0/2319.7:.1f}%")
    has(R13, "Total RPD (b) | $44.91 | (1.4)% | $47.00 | 1.5%")
    print(f"  $0.12 per share x 464.3m diluted shares = {0.12*464.3:.1f} after tax; adjusted pre-tax income fell {210.7-186.3:.1f} (210.7 to 186.3)")
    has(A13, "the fair value of debt securities was $151.0 million and $0.0 million")
    has(A13, "Prepaid expenses and other assets | 717.2 | 489.3")
    print(f"Prepaid and other assets rose {717.2-489.3:.1f} (revised basis); China Auto Rental notes 151.0 = {100*151.0/(717.2-489.3):.0f}% (purchases 130.0, unrealised gain 21.0)")

    print("\n=== Adjusted earnings ===")
    has(R13, "Adjusted pre-tax income | 1,153.2 | 1,153.2 | 892.3 | 892.3")
    has(R12, "Adjusted pre-tax income | 901.5 | 901.5 | 680.5 | 680.5")
    for lab, adj, rep in [("2013", 1153.2, 663.1), ("2012 as revised", 892.3, 441.4), ("2012 as first reported", 901.5, 450.6), ("2011 as first reported", 680.5, 324.3)]:
        print(f"{lab}: adjusted pre-tax {adj} vs reported {rep}: gap {adj-rep:.1f} = {100*(adj-rep)/rep:.0f}% of reported")
    print(f"Adjusted net income vs reported: 2013 749.6 vs 346.2 ({749.6/346.2:.2f}x); 2012 as revised 588.9 vs 238.6 ({588.9/238.6:.2f}x)")
    has(R13, "Total extraordinary, unusual or non-recurring items | $79.1 | $75.4 | $8.9 | $0.7 | $119.3 | $283.4 | $112.3 | $23.5 | $25.1 | $0.3 | $78.1 | $239.3")
    has(R12, "Total extraordinary, unusual or non-recurring items | $136.1 | $25.1 | $78.1 | $239.3 | $23.6 | $42.4 | $85.4 | $151.4")
    has(A13, "restructuring charges relating to various initiatives of $77.0 million, $38.0 million and $56.4 million")
    has(A12, "restructuring charges relating to various initiatives of $38.0 million, $56.4 million and $54.7 million")
    print("Items in both years' non-recurring table: restructuring 77.0 / 38.0 (56.4 in 2011, 54.7 in 2010); restructuring related 21.8 / 11.1; acquisition related 18.5 / 163.7; other 45.6 / 26.5. Total 283.4 / 239.3 / 151.4 (2011)")
    print(f"  restructuring plus related: 2013 {77.0+21.8:.1f}, 2012 {38.0+11.1:.1f}, 2011 {56.4+9.8:.1f}")

    print("\n=== Reserves ===")
    pl = {2010: 278.7, 2011: 281.5, 2012: 332.2, 2013: 347.7}
    print(f"Public liability and property damage reserve {pl[2012]} -> {pl[2013]}: {g(pl[2013],pl[2012]):+.1f}% vs revenue +19.4%, U.S. transaction days +26.2%")
    print("  reserve as % of revenue:", {y: round(100 * pl[y] / r, 2) for y, r in [(2010, 7562.5), (2011, 8298.4), (2012, 9020.8), (2013, 10771.9)]})
    has(A13, "self insurance expenses of $9.0 million")
    print("  no roll-forward of claims paid in the documents; no reserve reduction described as a change in estimate")

    if os.path.exists(OUT + r"\reply-2.md"):
        print("\n=== Quotation check, reply-2.md ===")
        check_quotes(OUT + r"\reply-2.md", labels=())
