# Turn 1: scan the numbers. All figures in USD millions.
import re, datetime as dt, json, os
import openpyxl

BASE = r"C:\Users\aaron\OneDrive\Desktop\Master\WireSift Research\Events\CFA Vancouver Forensic\test-data\home-depot-fy2025"
HERE = os.path.join(BASE, "runs", "v2.5")
wb = openpyxl.load_workbook(os.path.join(BASE, "statements.xlsx"), data_only=True)


def sheet(name):
    ws = wb[name]
    rows = list(ws.iter_rows(values_only=True))
    hdr = rows[0]
    cols = {}
    for j, h in enumerate(hdr[1:-1], start=1):
        m = re.search(r"ended (\d{4}-\d{2}-\d{2})", h)
        cols[m.group(1)] = j
    data = {}
    for r in rows[1:]:
        if r[0] is None:
            continue
        data.setdefault(r[0], {d: r[j] for d, j in cols.items()})
    return data, list(cols), hdr


ISa, isa_cols, _ = sheet("IS annual")
BSa, bsa_cols, _ = sheet("BS annual")
CFa, cfa_cols, _ = sheet("CF annual")
ISq, isq_cols, _ = sheet("IS quarterly")
BSq, bsq_cols, _ = sheet("BS quarterly")
CFq, cfq_cols, cfq_hdr = sheet("CF quarterly")
print("CF quarterly headings flagged mixed basis:", [h for h in cfq_hdr if h and "mixed" in h])

d = lambda s: dt.date.fromisoformat(s)
FY = isa_cols  # 2022-01-30 ... 2026-02-01
QL, QP = "2026-08-02", "2025-08-03"  # latest quarter in the workbook; same quarter a year earlier
QPP = "2024-07-28"
assert isq_cols[-1] == QL


# ---- figures taken from the annual report notes (property note) ----
def txt(fn):
    return open(os.path.join(BASE, fn), encoding="utf-8").read()


AR26 = txt("annual-report-FY2026-02-01-key-sections.txt")
AR25 = txt("annual-report-FY2025-02-02-key-sections.txt")


def nums(text, label, n):
    m = re.search(r"(?m)^" + re.escape(label) + r"((?: \| \$?[\d,]+){%d})$" % n, text)
    assert m, label
    return [int(x.replace(",", "").replace("$", "")) for x in m.group(1).split(" | ")[1:]]


gross, land, cip, dep = {}, {}, {}, {}
gross["2026-02-01"], gross["2025-02-02"] = nums(AR26, "Property and equipment, at cost", 2)
land["2026-02-01"], land["2025-02-02"] = nums(AR26, "Land", 2)
cip["2026-02-01"], cip["2025-02-02"] = nums(AR26, "Construction in progress", 2)
g25, gross["2024-01-28"] = nums(AR25, "Property and equipment, at cost", 2)
assert g25 == gross["2025-02-02"]
_, land["2024-01-28"] = nums(AR25, "Land", 2)
_, cip["2024-01-28"] = nums(AR25, "Construction in progress", 2)
dep["2026-02-01"], dep["2025-02-02"], dep["2024-01-28"] = nums(AR26, "Depreciation and finance lease amortization expense", 3)
d25, d24, dep["2023-01-29"] = nums(AR25, "Depreciation and finance lease amortization expense", 3)
assert (d25, d24) == (dep["2025-02-02"], dep["2024-01-28"])
depreciable = {k: gross[k] - land[k] - cip[k] for k in gross}
print("gross PP&E", gross, "\nland", land, "\nCIP", cip, "\ndepreciable", depreciable, "\ndepreciation", dep)

out = {}


def put(row, col, v):
    out.setdefault(row, {})[col] = v


pct = lambda a, b: (a / b - 1) * 100

# ---- annual ----
for i, fy in enumerate(FY):
    rev, cos = ISa["Net sales"][fy], ISa["Cost of sales"][fy]
    put("Gross margin %", fy, ISa["Gross profit"][fy] / rev * 100)
    put("Operating margin %", fy, ISa["Operating income"][fy] / rev * 100)
    put("SG&A % of sales", fy, ISa["Selling, general and administrative"][fy] / rev * 100)
    ni, cfo = CFa["Net earnings"][fy], CFa["Net cash provided by operating activities"][fy]
    capex = -CFa["Capital expenditures"][fy]
    put("FCF", fy, cfo - capex)
    put("FCF / net earnings", fy, (cfo - capex) / ni)
    put("Net earnings", fy, ni)
    put("CFO", fy, cfo)
    if fy in bsa_cols:
        days = (d(fy) - d(FY[i - 1])).days
        put("days in period", fy, days)
        put("DSO", fy, BSa["Receivables, net"][fy] / rev * days)
        put("Days inventory", fy, BSa["Merchandise inventories"][fy] / cos * days)
        put("Days payable", fy, BSa["Accounts payable"][fy] / cos * days)
        p = FY[i - 1]
        if p in bsa_cols:
            rg, cg = pct(rev, ISa["Net sales"][p]), pct(cos, ISa["Cost of sales"][p])
            put("Revenue growth %", fy, rg)
            put("Cost of sales growth %", fy, cg)
            put("Receivables growth %", fy, pct(BSa["Receivables, net"][fy], BSa["Receivables, net"][p]))
            put("Inventory growth %", fy, pct(BSa["Merchandise inventories"][fy], BSa["Merchandise inventories"][p]))
            put("Payables growth %", fy, pct(BSa["Accounts payable"][fy], BSa["Accounts payable"][p]))
            put("Receivables gap pp", fy, out["Receivables growth %"][fy] - rg)
            put("Inventory gap pp", fy, out["Inventory growth %"][fy] - cg)
            put("Payables gap pp", fy, out["Payables growth %"][fy] - cg)
            avgTA = (BSa["Total assets"][fy] + BSa["Total assets"][p]) / 2
            put("Accruals % avg assets", fy, (ni - cfo) / avgTA * 100)
            if fy in depreciable and p in depreciable:
                put("Depreciation rate %", fy, dep[fy] / ((depreciable[fy] + depreciable[p]) / 2) * 100)
            # Beneish M-score
            r = lambda line, y: BSa[line][y]
            DSRI = (r("Receivables, net", fy) / rev) / (r("Receivables, net", p) / ISa["Net sales"][p])
            GMI = (ISa["Gross profit"][p] / ISa["Net sales"][p]) / (ISa["Gross profit"][fy] / rev)
            aq = lambda y: 1 - (r("Total current assets", y) + r("Net property and equipment", y)) / r("Total assets", y)
            AQI = aq(fy) / aq(p)
            SGI = rev / ISa["Net sales"][p]
            dr = lambda y: dep[y] / (dep[y] + r("Net property and equipment", y))
            DEPI = dr(p) / dr(fy)
            sg = lambda y: ISa["Selling, general and administrative"][y] / ISa["Net sales"][y]
            SGAI = sg(fy) / sg(p)
            TATA = (ni - cfo) / r("Total assets", fy)
            lv = lambda y: (r("Long-term debt, excluding current installments", y) + r("Total current liabilities", y)) / r("Total assets", y)
            LVGI = lv(fy) / lv(p)
            M = -4.84 + 0.920 * DSRI + 0.528 * GMI + 0.404 * AQI + 0.892 * SGI + 0.115 * DEPI - 0.172 * SGAI + 4.679 * TATA - 0.327 * LVGI
            put("M-score", fy, M)
            put("M inputs", fy, dict(DSRI=DSRI, GMI=GMI, AQI=AQI, SGI=SGI, DEPI=DEPI, SGAI=SGAI, TATA=TATA, LVGI=LVGI))


# ---- quarters: latest (Q2 ended 2026-08-02) beside the same quarter a year earlier ----
def qprev(q):
    return bsq_cols[bsq_cols.index(q) - 1]


for q, yago in ((QP, QPP), (QL, QP)):
    rev, cos = ISq["Net sales"][q], ISq["Cost of sales"][q]
    days = (d(q) - d(qprev(q))).days
    put("days in period", q, days)
    put("Gross margin %", q, ISq["Gross profit"][q] / rev * 100)
    put("Operating margin %", q, ISq["Operating income"][q] / rev * 100)
    put("SG&A % of sales", q, ISq["Selling, general and administrative"][q] / rev * 100)
    put("DSO", q, BSq["Receivables, net"][q] / rev * days)
    put("Days inventory", q, BSq["Merchandise inventories"][q] / cos * days)
    put("Days payable", q, BSq["Accounts payable"][q] / cos * days)
    rg, cg = pct(rev, ISq["Net sales"][yago]), pct(cos, ISq["Cost of sales"][yago])
    put("Revenue growth %", q, rg)
    put("Cost of sales growth %", q, cg)
    put("Receivables growth %", q, pct(BSq["Receivables, net"][q], BSq["Receivables, net"][yago]))
    put("Inventory growth %", q, pct(BSq["Merchandise inventories"][q], BSq["Merchandise inventories"][yago]))
    put("Payables growth %", q, pct(BSq["Accounts payable"][q], BSq["Accounts payable"][yago]))
    put("Receivables gap pp", q, out["Receivables growth %"][q] - rg)
    put("Inventory gap pp", q, out["Inventory growth %"][q] - cg)
    put("Payables gap pp", q, out["Payables growth %"][q] - cg)
    ni, cfo = CFq["Net earnings"][q], CFq["Net cash provided by operating activities"][q]
    capex = -CFq["Capital expenditures"][q]
    avgTA = (BSq["Total assets"][q] + BSq["Total assets"][qprev(q)]) / 2
    put("Accruals % avg assets", q, (ni - cfo) / avgTA * 100)
    put("FCF", q, cfo - capex)
    put("FCF / net earnings", q, (cfo - capex) / ni)
    put("Net earnings", q, ni)
    put("CFO", q, cfo)

# ---- supporting figures for the flags ----
extra = {}
for fy in bsa_cols:
    ta = BSa["Total assets"][fy]
    gi = BSa["Goodwill"][fy] + (BSa["Intangible assets, net"][fy] or 0)
    extra[fy] = dict(
        receivables=BSa["Receivables, net"][fy],
        inventories=BSa["Merchandise inventories"][fy],
        payables=BSa["Accounts payable"][fy],
        goodwill_intang=gi,
        share_of_assets=gi / ta * 100,
        acq=CFa["Payments for businesses acquired, net"][fy],
        ap_change=CFa["Changes in accounts payable and accrued expenses"][fy],
        tax_change=CFa["Changes in income taxes payable"][fy],
        inv_change=CFa["Changes in merchandise inventories"][fy],
    )
extra["acq quarters"] = {q: CFq["Payments for businesses acquired, net"][q] for q in cfq_cols[-5:]}
cfo_ = CFa["Net cash provided by operating activities"]
extra["CFO change FY26 %"] = pct(cfo_["2026-02-01"], cfo_["2025-02-02"])
extra["CFO change FY26 $"] = cfo_["2026-02-01"] - cfo_["2025-02-02"]
extra["NI change FY26 %"] = pct(CFa["Net earnings"]["2026-02-01"], CFa["Net earnings"]["2025-02-02"])
extra["NI change FY26 $"] = CFa["Net earnings"]["2026-02-01"] - CFa["Net earnings"]["2025-02-02"]
for a, b in (("2022-01-30", "2026-02-01"),):
    extra["op margin change pp FY22->FY26"] = out["Operating margin %"][b] - out["Operating margin %"][a]
    extra["gross margin change pp FY22->FY26"] = out["Gross margin %"][b] - out["Gross margin %"][a]
    extra["sga pct change pp FY22->FY26"] = out["SG&A % of sales"][b] - out["SG&A % of sales"][a]
extra["D&A opex % of sales"] = {fy: ISa["Depreciation and amortization"][fy] / ISa["Net sales"][fy] * 100 for fy in FY}
extra["quarter balances"] = {q: dict(rec=BSq["Receivables, net"][q], inv=BSq["Merchandise inventories"][q], ap=BSq["Accounts payable"][q]) for q in (QPP, QP, QL)}

# ---- revisions ----
rev_rows = list(wb["Revisions"].iter_rows(values_only=True))
extra["revisions"] = [(r[0], r[1], r[3], r[4], r[6], r[8]) for r in rev_rows[1:]]

cols = FY + [QP, QL]
print("columns:", cols)
for row, vals in out.items():
    if row == "M inputs":
        for k, v in vals.items():
            print("M inputs", k, {a: round(b, 3) for a, b in v.items()})
        continue
    print(f"{row:26s}", " | ".join(f"{vals[c]:9.2f}" if c in vals else "        -" for c in cols))
print(json.dumps(extra, indent=1, default=str))
json.dump({"out": out, "extra": extra, "cols": cols}, open(os.path.join(HERE, "_numbers1.json"), "w"), default=str)

# ================= build the reply (every figure below is formatted from the values computed above) =================
lab = {"2022-01-30": "FY Jan-22", "2023-01-29": "FY Jan-23", "2024-01-28": "FY Jan-24", "2025-02-02": "FY Feb-25 (53 wk)",
       "2026-02-01": "FY Feb-26", "2025-08-03": "Q2 Aug-25", "2026-08-02": "Q2 Aug-26 (latest)"}
F22, F23, F24, F25, F26 = "2022-01-30", "2023-01-29", "2024-01-28", "2025-02-02", "2026-02-01"


def cell(row, c, fmt):
    v = out.get(row, {}).get(c)
    return "n/a" if v is None else fmt(v)


f1 = lambda v: f"{v:.1f}"
s1 = lambda v: f"{v:+.1f}"
f2 = lambda v: f"{v:.2f}"
m0 = lambda v: f"{v:,.0f}"
rows = [
    ("Days sales outstanding", "DSO", f1),
    ("Days inventory", "Days inventory", f1),
    ("Days payable", "Days payable", f1),
    ("Receivables growth less revenue growth, pts", "Receivables gap pp", s1),
    ("Inventory growth less cost-of-sales growth, pts", "Inventory gap pp", s1),
    ("Payables growth less cost-of-sales growth, pts", "Payables gap pp", s1),
    ("Gross margin, %", "Gross margin %", f1),
    ("Operating margin, %", "Operating margin %", f1),
    ("Accruals ÷ average assets, % (quarters not annualised)", "Accruals % avg assets", f1),
    ("Free cash flow, $m", "FCF", m0),
    ("Net earnings, $m", "Net earnings", m0),
    ("Depreciation rate, %", "Depreciation rate %", f1),
    ("M-score (against the prior year)", "M-score", f2),
]
L = []
L.append("| Measure | " + " | ".join(lab[c] for c in cols) + " |")
L.append("|---|" + "---:|" * len(cols))
for name, key, fmt in rows:
    L.append(f"| {name} | " + " | ".join(cell(key, c, fmt) for c in cols) + " |")
L.append("")
L.append("**Cost line:** Cost of sales, as reported. Substitutes: depreciation and gross property (less land and construction in progress) "
         "come from the annual reports' property note, and the M-score's accruals input is (net earnings less operating cash flow) ÷ year-end assets.")
L.append("")
o, e = out, extra
g = lambda row, c: o[row][c]
L.append("**Flags**")
L.append("")
L.append(f"1. **Receivables outgrew sales.** \"Receivables, net\" (BS annual, BS quarterly) rose {g('Receivables growth %',F25):.1f}% in FY Feb-25 against \"Net sales\" up {g('Revenue growth %',F25):.1f}%, "
         f"{g('Receivables growth %',F26):.1f}% against {g('Revenue growth %',F26):.1f}% in FY Feb-26 and {g('Receivables growth %',QL):.1f}% against {g('Revenue growth %',QL):.1f}% in Q2 Aug-26; "
         f"days sales outstanding went from {g('DSO',F24):.1f} to {g('DSO',F26):.1f}. "
         f"Acquisition payments of {-e[F25]['acq']:,} and {-e[F26]['acq']:,} in those two years could explain it.")
L.append(f"2. **Cash flow fell more than earnings in FY Feb-26.** \"Net cash provided by operating activities\" (CF annual) fell {-e['CFO change FY26 %']:.1f}%, from {g('CFO',F25):,} to {g('CFO',F26):,}, against net earnings down {-e['NI change FY26 %']:.1f}%; "
         f"\"Changes in accounts payable and accrued expenses\" swung from {e[F25]['ap_change']:,} to {e[F26]['ap_change']:,} and \"Changes in income taxes payable\" from {e[F25]['tax_change']:,} to {e[F26]['tax_change']:,}.")
L.append(f"3. **Goodwill and intangibles are almost a third of assets.** \"Goodwill\" plus \"Intangible assets, net\" (BS annual) went from {e[F24]['goodwill_intang']:,} ({e[F24]['share_of_assets']:.1f}% of total assets) at Jan-24 "
         f"to {e[F26]['goodwill_intang']:,} ({e[F26]['share_of_assets']:.1f}%) at Feb-26, which with receivables lifted the M-score to {g('M-score',F25):.2f} in FY Feb-25, still below -1.78. The acquisition payments could explain it.")
L.append(f"4. **Operating margin has fallen every year since FY Jan-23.** \"Operating income\" (IS annual) went from {g('Operating margin %',F23):.1f}% to {g('Operating margin %',F26):.1f}% of sales while gross margin moved only from {g('Gross margin %',F23):.1f}% to {g('Gross margin %',F26):.1f}%; "
         f"\"Selling, general and administrative\" rose from {g('SG&A % of sales',F23):.1f}% to {g('SG&A % of sales',F26):.1f}% of sales.")
L.append(f"5. **Inventory up, payables down in FY Feb-26.** \"Merchandise inventories\" (BS annual) rose {g('Inventory growth %',F26):.1f}% against cost of sales up {g('Cost of sales growth %',F26):.1f}% (days inventory {g('Days inventory',F25):.1f} to {g('Days inventory',F26):.1f}) "
         f"while \"Accounts payable\" fell {-g('Payables growth %',F26):.1f}% (days payable {g('Days payable',F25):.1f} to {g('Days payable',F26):.1f}). "
         f"The {-e[F26]['acq']:,} acquisition payment could explain part of the inventory rise.")
L.append("")
rv = e["revisions"]
assert len(rv) == 4
L.append(f"**Revised figures:** the Revisions sheet lists four changes, all re-labelling ({-rv[0][5]:,} of intangibles moved out of \"Other assets\" at 28 Jan 2024; "
         f"intangible amortization of {-rv[1][5]}, {-rv[2][5]} and {-rv[3][5]} moved out of the cash-flow depreciation line); none moved income or equity.")
L.append("")
L.append("**Not calculated:** the allowance for doubtful accounts (the annual reports give no figure, saying only that it was not material: FY Feb-26 report, p. 48); "
         "balance-sheet measures for FY Jan-22 and year-over-year measures for FY Jan-23 (the earliest balance sheet is 29 Jan 2023); "
         "the depreciation rate before FY Feb-25 and for the quarters (no gross property figures).")
reply = "\n".join(L) + "\n"

# ---- checks before saving ----
# every year in the op-margin flag really is lower than the one before
assert g("Operating margin %", F24) < g("Operating margin %", F23) and g("Operating margin %", F25) < g("Operating margin %", F24) and g("Operating margin %", F26) < g("Operating margin %", F25)
assert all(g("M-score", y) < -1.78 for y in (F24, F25, F26))


def page_of(text, pos):
    ms = [m for m in re.finditer(r"\[p\. (\d+)\]", text[:pos])]
    return int(ms[-1].group(1)) if ms else None


pos = AR26.find("The valuation allowance related to these receivables was not material")
assert pos > 0 and page_of(AR26, pos) == 48, page_of(AR26, pos)
print("page check: allowance sentence is on p.", page_of(AR26, pos), "of the FY Feb-26 report")
quotes = re.findall(r"“([^”]+)”", reply)
print("quotations from the filings in the reply:", quotes if quotes else "none (the quoted strings are spreadsheet line names)")
for name in re.findall(r'"([^"]+)"', reply):  # every spreadsheet line named in the reply exists in the workbook
    assert any(name in sh for sh in (ISa, BSa, CFa)), name
assert "—" not in reply
for w in ("fraud", "manipulat", "red flag"):
    assert w not in reply.lower()
print("word count:", len(reply.split()), "| words outside the table:", len("\n".join(l for l in L if not l.startswith("|")).split()))
open(os.path.join(HERE, "numbers-1.md"), "w", encoding="utf-8").write(reply)
import shutil
shutil.copyfile(os.path.abspath(__file__), os.path.join(HERE, "numbers-code-1.py"))
print(reply)
