# Turn 2 (prompt 4: compare the footnotes). Alignment of the two reports, calculations, quotation checks.
# Run from the company folder:  python runs/v2.5/text-code-4.py [reply.md citations.json]
import re, sys, json, difflib, openpyxl
sys.stdout.reconfigure(encoding="utf-8")
F26 = "annual-report-FY2026-02-01-key-sections.txt"   # this year (fiscal 2025)
F25 = "annual-report-FY2025-02-02-key-sections.txt"   # last year (fiscal 2024)
T = {F26: open(F26, encoding="utf-8").read(), F25: open(F25, encoding="utf-8").read()}

# ---------- 1. alignment of the two years (paragraph level, then word level) ----------
def sections(t):
    heads = [(m.group(1), m.start()) for m in re.finditer(r"^=== (.*) ===$", t, flags=re.M)] + [("END", len(t))]
    return {n: t[s:e] for (n, s), (_, e) in zip(heads, heads[1:])}
def paras(sec):
    out, page = [], None
    for ln in sec.split("\n"):
        m = re.match(r"\[p\. (\d+)\]", ln)
        if m: page = int(m.group(1)); continue
        ln = ln.strip()
        if not ln or re.match(r"Fiscal 20\d\d Form 10-K \| \d+", ln): continue
        out.append((page, ln))
    return out
def wdiff(a, b):
    ta, tb = a.split(), b.split(); out = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, ta, tb, autojunk=False).get_opcodes():
        if tag == "equal": out.append(" ".join(ta[i1:i2]))
        else:
            if i2 > i1: out.append("[-" + " ".join(ta[i1:i2]) + "-]")
            if j2 > j1: out.append("{+" + " ".join(tb[j1:j2]) + "+}")
    return " ".join(out)
def merged(name):
    """Both years of one section in a single text: '=' same, '~' reworded (word-level marks), '-' only last year, '+' only this year."""
    a, b = paras(sections(T[F25])[name]), paras(sections(T[F26])[name]); lines = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, [x[1] for x in a], [x[1] for x in b], autojunk=False).get_opcodes():
        if tag == "equal":
            lines += [f"= [25 p.{p} / 26 p.{q}] {s}" for (p, s), (q, _) in zip(a[i1:i2], b[j1:j2])]
        elif tag == "replace":
            A, B = a[i1:i2], b[j1:j2]; used, jstart = set(), 0
            for p, s in A:
                best, bs = None, 0.55
                for k in range(jstart, len(B)):
                    if k in used: continue
                    r = difflib.SequenceMatcher(None, s.split(), B[k][1].split(), autojunk=False).ratio()
                    if r > bs: bs, best = r, k
                if best is None: lines.append(f"- [25 p.{p}] DROPPED: {s}"); continue
                for k in range(jstart, best):
                    if k not in used: lines.append(f"+ [26 p.{B[k][0]}] ADDED: {B[k][1]}"); used.add(k)
                used.add(best); jstart = best + 1
                lines.append(f"~ [25 p.{p} / 26 p.{B[best][0]}] {wdiff(s, B[best][1])}")
            lines += [f"+ [26 p.{B[k][0]}] ADDED: {B[k][1]}" for k in range(len(B)) if k not in used]
        elif tag == "delete": lines += [f"- [25 p.{p}] DROPPED: {s}" for p, s in a[i1:i2]]
        else: lines += [f"+ [26 p.{p}] ADDED: {s}" for p, s in b[j1:j2]]
    return "\n\n".join(lines)
if "--merged" in sys.argv:          # python text-code-4.py --merged "Item 1A"   prints the aligned text that was read
    print(merged(sys.argv[sys.argv.index("--merged") + 1])); sys.exit()

# ---------- 2. calculations ----------
wb = openpyxl.load_workbook("statements.xlsx", data_only=True)
def sheet(name):
    rows = list(wb[name].iter_rows(values_only=True)); hdr = rows[0]
    return {r[0]: dict(zip(hdr[1:], r[1:])) for r in rows[1:] if r[0]}
IS, BS, CF, BSQ = sheet("IS annual"), sheet("BS annual"), sheet("CF annual"), sheet("BS quarterly")
Y25, Y24, Y23 = "FY (ended 2026-02-01)", "FY (ended 2025-02-02)", "FY (ended 2024-01-28)"   # fiscal 2025, 2024, 2023
def pct(a, b): return (a / b - 1) * 100
cos25, cos24 = IS["Cost of sales"][Y25], IS["Cost of sales"][Y24]

print("== Critical audit matters: inventory and shrink")
inv = {y: BS["Merchandise inventories"][y] for y in (Y25, Y24, Y23)}
print("inventory", inv[Y25], "growth %", round(pct(inv[Y25], inv[Y24]), 1))
print("shrink: cost of a 10% higher rate", 95, 79, "change %", round(pct(79, 95), 1), "| implied base", 950, 790)
print("implied base % of Primary cost of sales", round(950 / 101194 * 100, 2), round(790 / 99717 * 100, 2), "| % of consolidated", round(950 / cos24 * 100, 2), round(790 / cos25 * 100, 2))
print("customer relationships valued: SRS 5,400 (matter last year), GMS 1,540 (no matter)")

print("\n== Sales per retail square foot (dropped): rebuilt from transactions x ticket / (stores x 104,000 sq ft)")
def spsf(trans_m, ticket, stores): return trans_m * ticket / (stores * 0.104)
e24, e23, e25 = spsf(1637.2, 89.31, 2347), spsf(1621.8, 90.07, 2347 - 12), spsf(1601.5, 90.56, 2359)
print("method check: fiscal 2024 est", round(e24, 2), "vs reported 599.92; fiscal 2023 est", round(e23, 2), "vs reported 604.55")
print("fiscal 2025 est", round(e25, 2), "| vs fiscal 2024 est %", round(pct(e25, e24), 2), "| vs reported 599.92 %", round(pct(e25, 599.92), 2))
wk = 2500 / 153108        # 53rd week share of Primary sales in fiscal 2024
print("fiscal 2024 est on 52 weeks", round(e24 * (1 - wk), 2), "| fiscal 2025 vs that %", round(pct(e25, e24 * (1 - wk)), 2))
print("reported history %", round(pct(599.92, 604.55), 1), round(pct(604.55, 627.17), 1))

print("\n== Commercial paper and total borrowings")
ltd = {y: BS["Current installments of long-term debt"][y] + BS["Long-term debt, excluding current installments"][y] for y in (Y25, Y24)}
cp = {y: BS["Short-term debt"][y] for y in (Y25, Y24)}
print("commercial paper", cp[Y24], cp[Y25], "x", round(cp[Y25] / cp[Y24], 1), "| long-term debt", ltd[Y24], ltd[Y25])
print("long-term debt + commercial paper", ltd[Y24] + cp[Y24], ltd[Y25] + cp[Y25], "change", ltd[Y25] + cp[Y25] - ltd[Y24] - cp[Y24])
q = BSQ["Short-term debt"]
q25 = [q[k] for k in ("Q4 (ended 2025-02-02)", "Q1 (ended 2025-05-04)", "Q2 (ended 2025-08-03)", "Q3 (ended 2025-11-02)", "Q4 (ended 2026-02-01)")]
q24 = [q[k] for k in ("Q4 (ended 2024-01-28)", "Q1 (ended 2024-04-28)", "Q2 (ended 2024-07-28)", "Q3 (ended 2024-10-27)", "Q4 (ended 2025-02-02)")]
print("quarter-end commercial paper", q24, q25, "| five-point averages", sum(q24) / 5, sum(q25) / 5, "| disclosed daily average fiscal 2024: 1,343")

print("\n== Other changes")
print("Other goodwill", 11025, 13780, "| GMS goodwill untested", 2610)
print("SG&A % of sales", round(IS["Selling, general and administrative"][Y24] / IS["Net sales"][Y24] * 100, 1), round(IS["Selling, general and administrative"][Y25] / IS["Net sales"][Y25] * 100, 1))
print("customer receivables", 924, 1896, 2588, "growth %", round(pct(1896, 924), 1), round(pct(2588, 1896), 1), "increase", 2588 - 1896, "| share of receivables %", round(924 / 3328 * 100, 1), round(1896 / 4903 * 100, 1), round(2588 / 5597 * 100, 1))
print("fiscal 2024 product lines as first shown vs now: Storage & Organization", 5636, 4898, 4898 - 5636, "| Kitchen & Blinds", 7238, 7889, 7889 - 7238, "| Hardlines", 48562, 47721, "| Decor", 51790, 52525, "| Building Materials", 52756, 52862, "| totals", 52756 + 51790 + 48562, 52862 + 52525 + 47721)
print("online sales check: 15.1% of fiscal 2024 sales grown 8.7% as % of fiscal 2025 sales", round(0.151 * IS["Net sales"][Y24] * 1.087 / IS["Net sales"][Y25] * 100, 2))
print("SRS goodwill 11,006 -> 11,003")

print("\n== What stayed the same: the numbers behind each unchanged statement")
# property lives: depreciation / average depreciable cost (cost less land and construction in progress)
dep = {Y25: 3452, Y24: 3283}
base = {Y25: 59467 - 9499 - 1654, Y24: 55783 - 9060 - 1521, Y23: 53257 - 9027 - 1192}
for y, yp in ((Y24, Y23), (Y25, Y24)):
    r = dep[y] / ((base[y] + base[yp]) / 2)
    print("property: depreciation rate %", round(r * 100, 2), "implied average life", round(1 / r, 1), "years", y)
print("finance leases: amortization / average cost -> years", round(1 / (328 / ((4087 + 4045) / 2)), 1), round(1 / (322 / ((4045 + 4133) / 2)), 1), "| stated weighted remaining term 12, 12")
# intangibles: next year's scheduled amortization against gross definite-lived cost
g24, g25 = 8845 + 610 + 11, 10517 + 889 + 1
print("intangibles: scheduled next-year amortization / gross definite-lived -> years", round(g24 / 553, 1), round(g25 / 683, 1), "| on the year's charge and average cost", round(((3425 + 227 + 12 + g24) / 2) / 425, 1), round(((g24 + g25) / 2) / 607, 1))
print("SRS and GMS stated lives imply a year's charge of", round(5400 / 20 + 380 / 5), "+ GMS", round(1540 / 19 + 260 / 7), "; Other amortization reported", 218, 398)
print("leases: weighted remaining term operating 10, 9, 8; finance 13, 12, 12 (stated range one to 20 years)")
print("supplier finance: average confirmed obligations / invoices confirmed x days", round((514 + 598) / 2 / 5140 * 371, 1), round((598 + 414) / 2 / 4394 * 364, 1), "| payables days", round(BS["Accounts payable"][Y24] / cos24 * 371, 1), round(BS["Accounts payable"][Y25] / cos25 * 364, 1), "(stated 30 to 60 days)")
print("receivables allowance: 1% of customer receivables", round(0.01 * 2588), "| % of pre-tax earnings", round(0.01 * 2588 / IS["Earnings before provision for income taxes"][Y25] * 100, 2))
print("self-insurance: liability 1.4, 1.5, 1.6 $B; deferred tax asset 258, 271, 262; ratio %", round(258 / 1400 * 100, 1), round(271 / 1500 * 100, 1), round(262 / 1600 * 100, 1), "| DTA change %", round(pct(262, 271), 1))
print("inventory days", round(inv[Y24] / cos24 * 371, 1), round(inv[Y25] / cos25 * 364, 1), "| company turnover 4.7, 4.4")
print("Primary operating income since the fiscal 2023 goodwill test", 21689, 21313, 20574, round(pct(20574, 21689), 1))

# ---------- 3. quotation check ----------
def page_of(t, pos):
    p = re.findall(r"\[p\. (\d+)\]", t[:pos]); return int(p[-1]) if p else None
if len(sys.argv) > 2:
    reply = open(sys.argv[1], encoding="utf-8").read()
    cites = json.load(open(sys.argv[2], encoding="utf-8"))   # [quote, "26" or "25", page]
    found = re.findall(r'"([^"]+)"', reply) + re.findall(r"“([^”]+)”", reply)
    known = [c[0] for c in cites]
    missing = [x for x in found if x not in known]
    print("\nquotations found in reply:", len(found), "| without a citation record:", missing)
    allok = not missing
    for qt, f, pg in cites:
        t = T[F26 if f == "26" else F25]
        pages = sorted({page_of(t, m.start()) for m in re.finditer(re.escape(qt), t)})
        good = pg in pages and qt in reply
        allok &= good
        print("OK  " if good else "FAIL", "FY20" + f, "cited p.", pg, "found on", pages, "|", qt)
    print("ALL QUOTES OK" if allok else "QUOTE CHECK FAILED")
