# Turn 4: compare the two annual reports. Part A aligns the listed sections of both years with difflib
# and prints dropped, added and reworded sentences for reading. Part B tests the statements of lives,
# holding periods, residual values and reserve methods against the numbers. Part C checks quotations in reply-4.md.
import re, sys, io, os, difflib
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


def section(text, start_pat, end_pat):
    s = re.search(start_pat, text); e = re.search(end_pat, text[s.end():])
    return text[s.start(): s.end() + (e.start() if e else len(text))], s.start()


def clean(sec):
    """Join text broken across page markers, drop running headers."""
    sec = re.sub(r"\n\[p\. \w+\]\n", "\n", sec)
    sec = re.sub(r"\n(ITEM \d+A?\. [^\n]*\(Continued\)|HERTZ GLOBAL HOLDINGS, INC\. AND SUBSIDIARIES|NOTES TO CONSOLIDATED FINANCIAL STATEMENTS \(Continued\)|Operations \(Continued\)|ITEM 7\. Management's Discussion and Analysis of Financial Condition and Results of)\n", "\n", sec)
    return sec


def sentences(sec):
    out = []
    for para in clean(sec).split("\n"):
        para = para.strip()
        if not para:
            continue
        if " | " in para and not re.search(r"(months|years)", para):
            continue  # table rows are compared separately; keep rows that state lives or periods
        for s in re.split(r"(?<=[.!?])\s+(?=[A-Z“\"(])", para):
            if len(s) > 25:
                out.append(s)
    return out


def norm(s, digits=True):
    s = s.replace("‑", "-").replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = re.sub(r"\b(19|20)\d\d\b", "YEAR", s)
    if digits:
        s = re.sub(r"\$?\d[\d,\.]*", "#", s)
    return re.sub(r"\s+", " ", s).strip().lower()


def compare(name, s12, s13, numkw=None):
    a, b = sentences(s12), sentences(s13)
    na, nb = [norm(x) for x in a], [norm(x) for x in b]
    setb, seta = set(nb), set(na)
    print(f"\n################ {name}: {len(a)} sentences last year, {len(b)} this year")
    usedb = set()
    for i, x in enumerate(a):
        if na[i] in setb:
            j = nb.index(na[i])
            # same words; did a number that is not a date or amount of the year change?
            if numkw and re.search(numkw, x) and norm(x, False) != norm(b[j], False):
                print("NUMBER CHANGED\n   2012:", x[:600], "\n   2013:", b[j][:600])
            continue
        best = difflib.get_close_matches(na[i], nb, n=1, cutoff=0.6)
        if best:
            j = nb.index(best[0]); usedb.add(j)
            sm = difflib.SequenceMatcher(None, a[i].split(), b[j].split())
            dele = [" ".join(a[i].split()[i1:i2]) for tag, i1, i2, j1, j2 in sm.get_opcodes() if tag in ("delete", "replace")]
            ins = [" ".join(b[j].split()[j1:j2]) for tag, i1, i2, j1, j2 in sm.get_opcodes() if tag in ("insert", "replace")]
            print("REWORDED\n   2012:", a[i][:700], "\n   2013:", b[j][:700], "\n   out:", dele[:12], "\n   in :", ins[:12])
        else:
            print("DROPPED\n   2012:", x[:700])
    for j, y in enumerate(b):
        if nb[j] not in seta and j not in usedb:
            if not difflib.get_close_matches(nb[j], na, n=1, cutoff=0.6):
                print("ADDED\n   2013:", y[:700])


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"
    if mode in ("diff", "all"):
        pairs = [
            ("1 Risk factors", (A12, r"=== Item 1A ===", r"=== Item 3 ==="), (A13, r"=== Item 1A ===", r"=== Item 3 ===")),
            ("2 Legal proceedings and contingencies", (A12, r"Note 12—Contingencies and Off-Balance Sheet Commitments", r"Note 13—Restructuring"), (A13, r"Note 13—Contingencies and Off-Balance Sheet Commitments", r"Note 14—Restructuring")),
            ("3a Auditor's report", (A12, r"REPORT OF INDEPENDENT REGISTERED PUBLIC ACCOUNTING FIRM", r"CONSOLIDATED BALANCE SHEETS"), (A13, r"REPORT OF INDEPENDENT REGISTERED PUBLIC ACCOUNTING FIRM", r"CONSOLIDATED BALANCE SHEETS")),
            ("3b Controls", (A12, r"=== Item 9A ===", r"\Z"), (A13, r"=== Item 9A ===", r"\Z")),
            ("4 Item 7 overview and critical accounting estimates", (A12, r"=== Item 7 ===", r"\nRESULTS OF OPERATIONS\n"), (A13, r"=== Item 7 ===", r"\nRESULTS OF OPERATIONS\n")),
            ("5-7 Note 1 and Note 2 policies", (A12, r"Note 1—Background", r"Note 3—Goodwill"), (A13, r"Note 1—Background", r"Note 3—Goodwill")),
            ("6 Restructuring note", (A12, r"Note 13—Restructuring", r"Note 14—Financial Instruments"), (A13, r"Note 14—Restructuring", r"Note 15—Financial Instruments")),
            ("7 Note 8 depreciation", (A12, r"Note 8—Depreciation of Revenue Earning Equipment", r"Note 9—Taxes"), (A13, r"Note 8—Depreciation of Revenue Earning Equipment", r"Note 9—Taxes")),
            ("7 Note 3 intangibles", (A12, r"Note 3—Goodwill", r"Note 4—Business"), (A13, r"Note 3—Goodwill", r"Note 4—Business")),
            ("8 Related parties", (A12, r"Note 15—Related Party Transactions", r"Note 16—Earnings"), (A13, r"Note 16—Related Party Transactions", r"Note 17—Earnings")),
            ("9 Non-GAAP definitions and results tables (Item 7)", (A12, r"\nRESULTS OF OPERATIONS\n", r"\nYear Ended December 31, 2012 Compared"), (A13, r"\nRESULTS OF OPERATIONS\n", r"\nYear Ended December 31, 2013 Compared")),
            ("Item 1 business (for lives, holding periods, reserves)", (A12, r"=== Item 1 ===", r"=== Item 1A ==="), (A13, r"=== Item 1 ===", r"=== Item 1A ===")),
            ("Liquidity (Item 7)", (A12, r"\nLIQUIDITY AND CAPITAL RESOURCES\n", r"=== Item 8 ==="), (A13, r"\nLIQUIDITY AND CAPITAL RESOURCES\n", r"=== Item 8 ===")),
            ("Releases: Exhibit 1 definitions", (R12, r"Non-GAAP Measures: Definitions and Use/Importance", r"\Z"), (R13, r"Non-GAAP Measures: Definitions and Use/Importance", r"\Z")),
        ]
        kw = r"months|years|per occurrence|%|percent|average|age "
        for name, (t12, s12, e12), (t13, s13, e13) in pairs:
            x12, _ = section(t12, s12, e12); x13, _ = section(t13, s13, e13)
            compare(name, x12, x13, numkw=kw)

    # ---------------- Part B: numbers behind the changes and the unchanged statements ----------------
    if mode in ("calc", "all"):
        g = lambda a, b: 100 * (a / b - 1)
        print("\n=== Program cars ===")
        has(A13, "Percentage of non-program cars in our U.S. car rental operations | 91% | 95% | 83%")
        has(A13, "U.S. | 18% | 19% | 45% | 54% | 48%"); has(A12, "U.S. | 19% | 45% | 54% | 48% | 55%")
        has(A13, "net losses of $48.2 million, and net gains of $100.6 million and $114.9 million")
        print("U.S. non-program share of fleet: 83% (2011), 95% (2012), 91% (2013); program share of U.S. purchases 45%, 19%, 18%")
        assert "Non-program cars typically have lower acquisition costs" not in A13 and "continue to decrease in the future" not in A13
        assert "primarily related to Dollar Thrifty" not in A12[A12.find("Note 12—Contingencies"):A12.find("Note 13—Restructuring")]
        assert "beyond the control of management" not in A13
        print("U.S. disposal result: 114.9 gain (2011), 100.6 gain (2012), 48.2 loss (2013)")

        print("\n=== Pricing measure ===")
        has(A12, "Non-rental rate revenue | (1,676.6) | (1,256.7) | (1,041.7)"); has(A12, "Car rental segment revenues | $7,633.0 | $7,083.5 | $6,486.2")
        print(f"Items left out of the old measure in 2012: 1,676.6 = {100*1676.6/7633.0:.1f}% of car rental segment revenue 7,633.0 (2011: {100*1256.7/7083.5:.1f}%)")
        has(A12, "Domestic (Hertz, Dollar and Thrifty) | $39.07 | $40.30 | $42.16"); has(A13, "Total RPD(b) | $47.00 | $46.33 | $47.67")
        print(f"U.S. old measure 2012: 39.07 vs 40.30 = {g(39.07,40.30):.1f}%; new measure 2012: 46.33 vs 47.67 = {g(46.33,47.67):.1f}%; 2013: 47.00 vs 46.33 = {g(47.00,46.33):+.1f}%")
        print(f"New measure exceeds old for 2012 by {g(46.33,39.07):.1f}%")

        print("\n=== Public liability reserve ===")
        days = {2011: 137301, 2012: 148787, 2013: 133181 + 45019}
        has(A12, "Worldwide transaction days (in thousands)(a) | 148,787 | 137,301 | 127,159")
        has(A13, "Transaction days (in thousands)(a) | 133,181 | 105,539 | 93,741"); has(A13, "Transaction days (in thousands)(a) | 45,019 | 43,248 | 43,560")
        res = {2010: 278.7, 2011: 281.5, 2012: 332.2, 2013: 347.7}
        for y in (2011, 2012, 2013):
            print(y, f"reserve {res[y]} / {days[y]:,} thousand rental days = ${1000*res[y]/days[y]:.2f} per rental day")
        print(f"2013: reserve {g(res[2013],res[2012]):+.1f}% (+{res[2013]-res[2012]:.1f}) vs rental days {g(days[2013],days[2012]):+.1f}%; per day {g(res[2013]/days[2013],res[2012]/days[2012]):.1f}%")
        print(f"2012: reserve {g(res[2012],res[2011]):+.1f}% (+{res[2012]-res[2011]:.1f}); two years: reserve {g(res[2013],res[2011]):+.1f}% vs days {g(days[2013],days[2011]):+.1f}%; per day {g(res[2013]/days[2013],res[2011]/days[2011]):.1f}%")

        print("\n=== Prior-year figures shown differently ===")
        has(A12, "were $158.0 million, $145.8 million and $133.8 million"); has(A13, "were $213.1 million, $183.9 million and $168.2 million")
        print(f"Advertising 2012: 158.0 -> 183.9 (+{183.9-158.0:.1f}); 2011: 145.8 -> 168.2 (+{168.2-145.8:.1f}); vendor incentive adjustments to SG&A 25.9 and 22.4; {100*25.9/158.0:.1f}% of 2012 advertising as first reported")
        has(A12, "gains from the dispositions of property and equipment of $6.3 million and $43.1 million"); has(A13, "gains from the dispositions of property and equipment of $3.9 million and $8.3 million")
        print("Property disposal gains 2012: 6.3 (FY2012) vs 8.3 (FY2013); the words in \"Direct operating\" dropped")

        print("\n=== Useful lives table ===")
        has(A13, "Concession rights | 411.3 | (49.5) | 361.8"); has(A13, "Concession rights | 406.0 | (5.0) | 401.0")
        print(f"Amortisation outside concession rights: 2013 {121.5-(49.5-5.0):.1f}, 2012 {83.9-5.0:.1f}")
        has(A13, "Customer-related | $693.1 | $(502.2) | $190.9"); has(A12, "Customer-related | $672.6 | $(365.5) | $307.1")
        print(f"Customer-related intangibles: 2013 amortisation {502.2-433.8:.1f} on 693.1 = {693.1/(502.2-433.8):.1f} years; 2012 {434.0-365.5:.1f} on {(672.6+694.7)/2:.1f} = {((672.6+694.7)/2)/(434.0-365.5):.1f} years")
        ppe = {2011: 158.0 / ((1972.3 + 2197.0) / 2), 2012: 172.6 / ((2197.0 + 2549.9) / 2), 2013: 205.3 / ((2549.9 + 2619.1) / 2)}
        print("Property depreciation / average cost:", {y: f"{100*v:.1f}% ({1/v:.1f} years)" for y, v in ppe.items()})

        print("\n=== Tax reassurance dropped ===")
        has(A12, "carry forwards of $3,697.9 million"); has(A13, "carry forwards of $4,170.2 million")
        assert "likelihood of making material cash tax payments" not in A13
        print(f"Federal loss carry-forwards 3,697.9 -> 4,170.2 ({g(4170.2,3697.9):+.1f}%)")

        print("\n=== Stated holding periods against the numbers ===")
        has(A12, "eighteen months in the United States and fourteen months in our international operations")
        has(A13, "eighteen months in the United States and thirteen months in our international operations")
        wb = openpyxl.load_workbook(D + r"\statements.xlsx", data_only=True)
        rows = {r[0]: r for r in wb["BS annual"].iter_rows(values_only=True)}
        cars = dict(zip([2010, 2011, 2012, 2013], rows["Cars"][1:5])); cars[2012] = 12548.8  # 2012 as revised
        has(A13, "Total | $10,298.4 | $9,612.8 | $9,431.9 | $685.6 | 7.1% | $180.9 | 1.9%")
        has(A13, "Worldwide equipment rental | 671.5 | 762.9 | 588.7 | (91.4) | (12.0)% | 174.2 | 29.6%")
        buy = {2013: 10298.4 - 671.5, 2012: 9612.8 - 762.9, 2011: 9431.9 - 588.7}
        for y in (2011, 2012, 2013):
            avg = (cars[y] + cars[y - 1]) / 2
            print(y, f"average cars at cost {avg:,.1f} / car purchases {buy[y]:,.1f} = {12*avg/buy[y]:.1f} months")
        has(A13, "our U.S. car rental operations sold approximately 197,700, 136,400 and 121,800 non-program cars")
        for y, avgc, sold in [(2013, 468500, 197700), (2012, 358000, 136400), (2011, 321700, 121800)]:
            print(y, f"U.S. average cars {avgc:,} / non-program cars sold {sold:,} = {12*avgc/sold:.1f} months (ignores program car returns)")
        has(A13, "longer holding periods and the impact of recalls"); has(A13, "vehicle maintenance costs of $9.6 million")
        has(A12, "does not necessarily equate to higher costs"); has(A13, "does not necessarily equate to higher costs")
        has(A12, "Reserve requirements are based on rental volume and actuarial evaluations"); has(A13, "Reserve requirements are based on rental volume and actuarial evaluations")
        has(A12, "which range from two to fifteen years"); has(A13, "which range from two to fifteen years")
        has(A12, "Customer relationships | 16 | $65.0"); has(A13, "Customer relationships | 16 | $65.0")
        print("\n-- statements tested that still fit (left out of the table) --")
        has(A12, "the average age of HERC's worldwide rental fleet was 43 months"); has(A13, "the average age of HERC's worldwide rental fleet was 43 months")
        eq = {2013: (298.8 + 26.2) / 3401.2, 2012: (272.1 + 13.5) / 3069.0}
        acc = {2013: 1095.8 / 3512.2, 2012: 1041.9 / 3240.1}
        for y in (2012, 2013):
            print(y, f"equipment depreciation before disposal gains {100*eq[y]:.1f}% of average acquisition cost; x 43 months = {100*eq[y]*43/12:.0f}% vs accumulated depreciation {100*acc[y]:.0f}% of cost")
        print(f"Concession rights 405 over nine years = {405/9:.1f} a year; amortised in 2013 {49.5-5.0:.1f}")
        wo = {2013: (30.8, 40.3), 2012: (29.3, 29.3), 2011: (20.3, 27.7)}
        print("Allowance / year's write-offs:", {y: f"{100*a/w:.0f}%" for y, (a, w) in wo.items()})

    # ---------------- Part C: quotation check ----------------
    if mode in ("check", "all") and os.path.exists(OUT + r"\reply-4.md"):
        print("\n=== Quotation check, reply-4.md ===")
        TABLE = [  # statements in the 'stayed the same' table: (quote, last year's page, this year's page)
            ("eighteen months in the United States", "11", "11"),
            ("does not necessarily equate to higher costs", "42", "42"),
            ("based on rental volume", "45", "45"),
            ("two to fifteen years", "83", "93"),
        ]
        n, ok = check_quotes(OUT + r"\reply-4.md", labels=[q for q, _, _ in TABLE])
        reply = open(OUT + r"\reply-4.md", encoding="utf-8").read()
        for q, p12, p13 in TABLE:
            if f'"{q}"' not in reply:
                continue
            for doc, t, pg in (("FY2012 annual report", A12, p12), ("FY2013 annual report", A13, p13)):
                pages = [page_at(t, m.start()) for m in re.finditer(re.escape(q), t)]
                good = pg in pages; n += 1; ok += good
                print(("PASS" if good else "FAIL"), f"| {doc} p. {pg} | found on pages {sorted(set(pages))} | {q}")
        print(f"TOTAL {n} quotations, {ok} pass")
