# Turn 1 (prompt 3: read the footnotes). Calculations and quotation checks.
# Run from the company folder:  python runs/v2.5/text-code-3.py [reply.md citations.json]
import re, sys, json, openpyxl
sys.stdout.reconfigure(encoding="utf-8")
F26 = "annual-report-FY2026-02-01-key-sections.txt"
F25 = "annual-report-FY2025-02-02-key-sections.txt"
T = {F26: open(F26, encoding="utf-8").read(), F25: open(F25, encoding="utf-8").read()}

wb = openpyxl.load_workbook("statements.xlsx", data_only=True)
def sheet(name):
    rows = list(wb[name].iter_rows(values_only=True)); hdr = rows[0]
    return {r[0]: dict(zip(hdr[1:], r[1:])) for r in rows[1:] if r[0]}
IS, BS, CF, BSQ = sheet("IS annual"), sheet("BS annual"), sheet("CF annual"), sheet("BS quarterly")
Y25, Y24, Y23 = "FY (ended 2026-02-01)", "FY (ended 2025-02-02)", "FY (ended 2024-01-28)"  # fiscal 2025, 2024, 2023
EQ = [k for k in BS if k.startswith("Total stockholders")][0]
def pct(a, b): return (a / b - 1) * 100

print("== Net sales: whole company vs Primary segment vs Other (segment figures from Note 2, p. 55)")
ns25, ns24 = IS["Net sales"][Y25], IS["Net sales"][Y24]
prim25, prim24, oth25, oth24 = 151966, 153108, 12717, 6406
assert prim25 + oth25 == ns25 and prim24 + oth24 == ns24
print("consolidated", ns25 - ns24, round(pct(ns25, ns24), 2))
print("primary", prim25 - prim24, round(pct(prim25, prim24), 2))
print("other incremental", oth25 - oth24)
wk53 = 2500  # 'approximately $2.5 billion' (Item 7, p. 33)
print("primary ex 53rd week %", round(pct(prim25, prim24 - wk53), 2))
pop25, pop24, oop25, oop24 = 20574, 21313, 316, 213
assert pop25 + oop25 == IS["Operating income"][Y25] and pop24 + oop24 == IS["Operating income"][Y24]
print("primary op income chg", pop25 - pop24, round(pct(pop25, pop24), 2), "margin", round(pop25 / prim25 * 100, 2), round(pop24 / prim24 * 100, 2))
print("consolidated op income chg %", round(pct(IS["Operating income"][Y25], IS["Operating income"][Y24]), 2))
pc25, pc24 = 99717, 101194
print("primary gross margin", round((prim25 - pc25) / prim25 * 100, 2), round((prim24 - pc24) / prim24 * 100, 2))
print("primary SG&A % sales", round(28885 / prim25 * 100, 2), round(27822 / prim24 * 100, 2), "SG&A growth", round(pct(28885, 27822), 2))
oc25, oc24 = IS["Cost of sales"][Y25] - pc25, IS["Cost of sales"][Y24] - pc24
print("other gross margin", round((oth25 - oc25) / oth25 * 100, 2), round((oth24 - oc24) / oth24 * 100, 2))
print("comp check (1.014*0.990-1) %", round((1.014 * 0.990 - 1) * 100, 2))
print("services revenue chg %", round(pct(5654, 5840), 1), "products", round(pct(159029, 153674), 1))

print("\n== Acquired businesses (Other): returns on what was paid")
print("other op margin", round(oop25 / oth25 * 100, 2), round(oop24 / oth24 * 100, 2))
am25, am24 = 398, 218
print("other op margin before intangible amortization", round((oop25 + am25) / oth25 * 100, 2), round((oop24 + am24) / oth24 * 100, 2))
paid = 18028 + 5081
print("purchase consideration SRS+GMS", paid, "| other op income / paid %", round(oop25 / paid * 100, 2), "| before amortization %", round((oop25 + am25) / paid * 100, 2))
gw_other = 13780
print("other goodwill", gw_other, "share of total goodwill %", round(gw_other / BS["Goodwill"][Y25] * 100, 1), "op income / other goodwill %", round(oop25 / gw_other * 100, 2))
gi = BS["Goodwill"][Y25] + BS["Intangible assets, net"][Y25]
print("goodwill+intangibles", gi, "% total assets", round(gi / BS["Total assets"][Y25] * 100, 1), "equity", BS[EQ][Y25], "multiple of equity", round(gi / BS[EQ][Y25], 2))
print("GMS: 4257+824+354 =", 4257 + 824 + 354, "; debt repaid", 824 + 354)
print("GMS net of cash", 5081 - 136, "other acquisitions cash", -CF["Payments for businesses acquired, net"][Y25] - (5081 - 136))
print("GMS sales % of net sales", round(2000 / ns25 * 100, 2))
ta_ex = BS["Total assets"][Y25] - gi
print("total assets ex goodwill/intangibles", ta_ex, "GMS assets ex gw/intangibles at acquisition", 7186 - 2610 - 1800, round((7186 - 2610 - 1800) / ta_ex * 100, 2), "%")
print("other cost+opex check", oth25 - oop25, oth24 - oop24)

print("\n== ROIC (Item 7, p. 35)")
ltd = {y: BS["Current installments of long-term debt"][y] + BS["Long-term debt, excluding current installments"][y] for y in (Y25, Y24, Y23)}
eq = {y: BS[EQ][y] for y in (Y25, Y24, Y23)}
cp = {y: (BS["Short-term debt"][y] or 0) for y in (Y25, Y24, Y23)}
def roic(y, yprev, with_cp=False):
    etr = IS["Provision for income taxes"][y] / IS["Earnings before provision for income taxes"][y]
    nopat = IS["Operating income"][y] * (1 - etr)
    cap = (ltd[y] + eq[y] + ltd[yprev] + eq[yprev]) / 2
    if with_cp: cap += (cp[y] + cp[yprev]) / 2
    return nopat, cap, nopat / cap * 100
for lab, y, yp in (("FY2025", Y25, Y24), ("FY2024", Y24, Y23)):
    n, c, r = roic(y, yp); n2, c2, r2 = roic(y, yp, True)
    print(lab, "NOPAT", round(n), "avg debt+equity", c, "ROIC", round(r, 2), "| with commercial paper: capital", c2, "ROIC", round(r2, 2))
print("avg equity change", (eq[Y25] + eq[Y24]) / 2 - (eq[Y24] + eq[Y23]) / 2, "avg LT debt change", (ltd[Y25] + ltd[Y24]) / 2 - (ltd[Y24] + ltd[Y23]) / 2)
print("LT debt change", ltd[Y25] - ltd[Y24], "commercial paper change", cp[Y25] - cp[Y24], "senior notes repaid", 500 + 500 + 1000 + 750 + 900 + 600)

print("\n== Inventory")
inv25, inv24, inv23 = (BS["Merchandise inventories"][y] for y in (Y25, Y24, Y23))
print("inventory growth %", round(pct(inv25, inv24), 2), "cost of sales growth %", round(pct(IS["Cost of sales"][Y25], IS["Cost of sales"][Y24]), 2), "GMS inventory acquired", 568)
print("2-point turnover", round(IS["Cost of sales"][Y25] / ((inv25 + inv24) / 2), 2), round(IS["Cost of sales"][Y24] / ((inv24 + inv23) / 2), 2))
q = BSQ["Merchandise inventories"]
q25 = [q[k] for k in ("Q4 (ended 2025-02-02)", "Q1 (ended 2025-05-04)", "Q2 (ended 2025-08-03)", "Q3 (ended 2025-11-02)", "Q4 (ended 2026-02-01)")]
q24 = [q[k] for k in ("Q4 (ended 2024-01-28)", "Q1 (ended 2024-04-28)", "Q2 (ended 2024-07-28)", "Q3 (ended 2024-10-27)", "Q4 (ended 2025-02-02)")]
print("5-point turnover", round(IS["Cost of sales"][Y25] / (sum(q25) / 5), 2), round(IS["Cost of sales"][Y24] / (sum(q24) / 5), 2))
print("shrink: implied base behind $79M per 10%:", 79 * 10, "| % of cost of sales", round(790 / IS["Cost of sales"][Y25] * 100, 2))

print("\n== Operating cash flow")
ocf25, ocf24 = CF["Net cash provided by operating activities"][Y25], CF["Net cash provided by operating activities"][Y24]
print("OCF change", ocf25 - ocf24, round(pct(ocf25, ocf24), 1), "%")
tot = 0
for k in ("Changes in accounts payable and accrued expenses", "Changes in merchandise inventories", "Changes in income taxes payable"):
    sw = CF[k][Y25] - CF[k][Y24]; tot += sw
    print(" ", k, CF[k][Y25], CF[k][Y24], "swing", sw)
print("  three swings together", tot)
print("income taxes paid (Note 6)", 4848, 3653, "change", 4848 - 3653, "federal change", 3590 - 2475)
print("deferred tax provision", 495, -39, "| deferred tax liability on property", 1514 - 854)
print("OCF / net earnings", round(ocf25 / IS["Net earnings"][Y25], 2), round(ocf24 / IS["Net earnings"][Y24], 2))

print("\n== Leases and commitments")
print("lease payments incl. not yet commenced", 11638 + 3591 + 675, "within 12 months", 1792 + 391)
print("operating lease cost growth %", round(pct(1846, 1661), 1), "| variable lease cost", 585, "| operating lease liability", 1418 + 8160)
print("\n== Supplier finance")
print("rollforward", 598 + 4394 - 4578, 514 + 5140 - 5056, "% of AP", round(414 / BS["Accounts payable"][Y25] * 100, 1), round(598 / BS["Accounts payable"][Y24] * 100, 1))
print("days payable (AP / cost of sales x days in year)", round(BS["Accounts payable"][Y25] / IS["Cost of sales"][Y25] * 364, 1), round(BS["Accounts payable"][Y24] / IS["Cost of sales"][Y24] * 371, 1))
print("\n== Receivables")
print("customer receivables growth %", round(pct(2588, 1896), 1), "increase", 2588 - 1896, "share of receivables %", round(2588 / 5597 * 100, 1), "GMS receivables acquired", 899)
print("\n== Tie-outs")
print("Note 3 depreciation + intangible amortization", 3452 + 607, "segment table", 4059, "cash flow", CF["Depreciation and amortization, excluding amortization of intangible assets"][Y25] + CF["Intangible asset amortization"][Y25])
print("intangibles: future amortization total", 683 + 674 + 654 + 615 + 578 + 6476, "net definite-lived", 8982 + 698)
print("self-insurance 1.6bn vs 1.5bn; deferred tax asset on it", 262, 271)
print("Revisions sheet: FY2023 D&A split", 3061 + 186, "= 3,247 as first reported")

# ---------- quotation check ----------
def page_of(t, pos):
    p = re.findall(r"\[p\. (\d+)\]", t[:pos]); return int(p[-1]) if p else None

if len(sys.argv) > 2:
    reply = open(sys.argv[1], encoding="utf-8").read()
    cites = json.load(open(sys.argv[2], encoding="utf-8"))   # [quote, "26" or "25", page]
    found = re.findall(r'"([^"]+)"', reply) + re.findall(r"“([^”]+)”", reply)
    print("\nquotations found in reply:", len(found))
    known = [c[0] for c in cites]
    missing = [x for x in found if x not in known]
    print("quotes without a citation record:", missing)
    allok = not missing
    for qt, f, pg in cites:
        t = T[F26 if f == "26" else F25]
        pages = sorted({page_of(t, m.start()) for m in re.finditer(re.escape(qt), t)})
        good = pg in pages and qt in reply
        allok &= good
        print("OK  " if good else "FAIL", "cited p.", pg, "found on", pages, "|", qt)
    print("ALL QUOTES OK" if allok else "QUOTE CHECK FAILED")
