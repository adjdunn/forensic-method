# Turn 2: follow the flags. All figures in USD millions unless stated.
import re, os, json, shutil, datetime as dt
import openpyxl

BASE = r"C:\Users\aaron\OneDrive\Desktop\Master\WireSift Research\Events\CFA Vancouver Forensic\test-data\home-depot-fy2025"
HERE = os.path.join(BASE, "runs", "v2.5")
wb = openpyxl.load_workbook(os.path.join(BASE, "statements.xlsx"), data_only=True)


def sheet(name):
    rows = list(wb[name].iter_rows(values_only=True))
    cols = {re.search(r"ended (\d{4}-\d{2}-\d{2})", h).group(1): j for j, h in enumerate(rows[0][1:-1], start=1)}
    data = {}
    for r in rows[1:]:
        if r[0] is not None:
            data.setdefault(r[0], {d: r[j] for d, j in cols.items()})
    return data, list(cols)


ISa, _ = sheet("IS annual")
BSa, _ = sheet("BS annual")
CFa, _ = sheet("CF annual")
ISq, _ = sheet("IS quarterly")
BSq, bsq_cols = sheet("BS quarterly")
CFq, _ = sheet("CF quarterly")
F23, F24, F25, F26 = "2023-01-29", "2024-01-28", "2025-02-02", "2026-02-01"

DOC = {
    "AR26": "annual-report-FY2026-02-01-key-sections.txt",
    "AR25": "annual-report-FY2025-02-02-key-sections.txt",
    "ER26": "earnings-release-Q4-FY2026-02-01.txt",
    "ER25": "earnings-release-Q4-FY2025-02-02.txt",
}
T = {k: open(os.path.join(BASE, v), encoding="utf-8").read() for k, v in DOC.items()}


def page_of(text, pos):
    ms = list(re.finditer(r"\[p\. (\d+)\]", text[:pos]))
    return int(ms[-1].group(1)) if ms else None


def pages_of(doc, s):
    """every page on which the exact string s occurs in the document"""
    t = T[doc]
    return sorted({page_of(t, m.start()) for m in re.finditer(re.escape(s), t)})


def row(doc, label, n, after=None, occurrence=0):
    """numbers on the first table row that starts with label (optionally after a marker string)"""
    t = T[doc]
    start = t.index(after) if after else 0
    ms = list(re.finditer(r"(?m)^" + re.escape(label) + r"((?: \| [^|\n]+){%d})$" % n, t[start:]))
    assert ms, (doc, label)
    cells = ms[occurrence].group(1).split(" | ")[1:]
    out = []
    for c in cells:
        c = c.strip().replace("$", "").replace(",", "").replace("%", "")
        neg = c.startswith("(") and c.endswith(")")
        c = c.strip("()")
        out.append(None if c in ("—", "") else (-float(c) if neg else float(c)))
    return out, page_of(t, start + ms[occurrence].start())


pct = lambda a, b: (a / b - 1) * 100
R = {}  # results
P = {}  # pages found for the figures taken from the reports

# ---------- Flag: operating margin / SG&A ----------
seg = "The following table presents net sales, significant expenses, and operating income for our Primary segment:"
(ps26, ps25, ps24), P["primary"] = row("AR26", "Net sales", 3, after=seg)
(pc26, pc25, pc24), _ = row("AR26", "Cost of sales", 3, after=seg)
(pg26, pg25, pg24), _ = row("AR26", "Selling, general and administrative", 3, after=seg)
(po26, po25, po24), _ = row("AR26", "Operating income", 3, after=seg)
# cross-check the earlier report's Primary table for the two overlapping years
(a25, a24, a23), _ = row("AR25", "Net sales", 3, after=seg)
assert (a25, a24) == (ps25, ps24)
R["primary_sga_growth_26"] = pct(pg26, pg25)
R["primary_sga_growth_25"] = pct(pg25, pg24)
R["primary_sga_growth_2y"] = pct(pg26, pg24)
R["primary_sales_growth_26"] = pct(ps26, ps25)
R["primary_sales_growth_2y"] = pct(ps26, ps24)
R["primary_opm"] = [po24 / ps24 * 100, po25 / ps25 * 100, po26 / ps26 * 100]
R["primary_gm"] = [(ps24 - pc24) / ps24 * 100, (ps25 - pc25) / ps25 * 100, (ps26 - pc26) / ps26 * 100]
R["primary_sga_pct"] = [pg24 / ps24 * 100, pg25 / ps25 * 100, pg26 / ps26 * 100]
R["primary_sga"] = [pg24, pg25, pg26]
R["co_opm"] = [ISa["Operating income"][y] / ISa["Net sales"][y] * 100 for y in (F24, F25, F26)]
R["co_sga_change_26"] = ISa["Selling, general and administrative"][F26] - ISa["Selling, general and administrative"][F25]
R["primary_sga_change_26"] = pg26 - pg25
rec = "The following table presents a reconciliation of certain segment information to our consolidated totals:"
(_, os26, _, _, os25, _), P["other"] = row("AR26", "Net sales", 6, after=rec)
(_, oo26, _, _, oo25, _), _ = row("AR26", "Operating income", 6, after=rec)
assert ps26 + os26 == ISa["Net sales"][F26] and ps25 + os25 == ISa["Net sales"][F25]
R["other_sales"] = [os25, os26]
R["other_oi"] = [oo25, oo26]
R["other_opm"] = [oo25 / os25 * 100, oo26 / os26 * 100]

# ---------- Flag: inventory and payables ----------
inv = BSa["Merchandise inventories"]
ap = BSa["Accounts payable"]
gms = "The following table summarizes our preliminary purchase price allocation, including resulting goodwill:"
(gms_inv,), P["gms"] = row("AR26", "Merchandise inventories", 1, after=gms)
(gms_rec,), _ = row("AR26", "Receivables", 1, after=gms)
(gms_ap,), _ = row("AR26", "Accounts payable", 1, after=gms)
(gms_gw,), _ = row("AR26", "Goodwill", 1, after=gms)
srs = "The following table summarizes our purchase price allocation, including resulting goodwill:"
(srs_rec,), P["srs26"] = row("AR26", "Receivables", 1, after=srs)
(srs_gw,), _ = row("AR26", "Goodwill", 1, after=srs)
(srs_rec25,), P["srs25"] = row("AR25", "Receivables", 1, after=gms)
(srs_gw25,), _ = row("AR25", "Goodwill", 1, after=gms)
assert srs_rec == srs_rec25
R["inv_rise"] = inv[F26] - inv[F25]
R["inv_built_cf"] = -CFa["Changes in merchandise inventories"][F26]
R["gms_inv"] = gms_inv
R["inv_built_share"] = R["inv_built_cf"] / R["inv_rise"] * 100
R["ap_fall"] = ap[F25] - ap[F26]
R["gms_ap"] = gms_ap


def turnover5(fy):  # cost of sales over the average of the five quarter-end inventories of the year
    i = bsq_cols.index(fy)
    qs = bsq_cols[i - 4 : i + 1]
    avg = sum(BSq["Merchandise inventories"][q] for q in qs) / 5
    return ISa["Cost of sales"][fy] / avg


def turnover2(fy, prev):
    return ISa["Cost of sales"][fy] / ((inv[fy] + inv[prev]) / 2)


R["turnover5"] = [turnover5(F25), turnover5(F26)]
R["turnover2"] = [turnover2(F25, F24), turnover2(F26, F25)]
days = lambda fy, prev: (dt.date.fromisoformat(fy) - dt.date.fromisoformat(prev)).days
R["days_inv"] = {fy: inv[fy] / ISa["Cost of sales"][fy] * days(fy, prev) for fy, prev in ((F23, "2022-01-30"), (F24, F23), (F25, F24), (F26, F25))}
(sf_conf26, sf_conf25), P["supfin"] = row("AR26", "Invoices confirmed during the year", 2)
(sf_end26, sf_end25), _ = row("AR26", "Confirmed obligations outstanding at the end of the year", 2)
R["supfin_confirmed_change"] = pct(sf_conf26, sf_conf25)
R["supfin_confirmed"] = [sf_conf25, sf_conf26]
R["supfin_outstanding"] = [sf_end25, sf_end26]
R["short_term_debt"] = [BSa["Short-term debt"][F25], BSa["Short-term debt"][F26]]
R["inv_growth_26"] = pct(inv[F26], inv[F25])
R["ap_growth_26"] = pct(ap[F26], ap[F25])

# ---------- Flag: receivables ----------
rcv = BSa["Receivables, net"]
(cr26, cr25), P["rec26"] = row("AR26", "Customer receivables", 2)
(cr25b, cr24), P["rec25"] = row("AR25", "Customer receivables", 2)
assert cr25 == cr25b
R["cust_rec"] = [cr24, cr25, cr26]
R["cust_rec_growth_26"] = pct(cr26, cr25)
R["rec_rise"] = [rcv[F25] - rcv[F24], rcv[F26] - rcv[F25]]
R["rec_growth"] = [pct(rcv[F25], rcv[F24]), pct(rcv[F26], rcv[F25])]
R["sales_growth"] = [pct(ISa["Net sales"][F25], ISa["Net sales"][F24]), pct(ISa["Net sales"][F26], ISa["Net sales"][F25])]
R["acq_rec"] = [srs_rec, gms_rec]
R["cf_rec_change"] = [CFa["Changes in receivables, net"][F25], CFa["Changes in receivables, net"][F26]]
R["h1_acq"] = -(CFq["Payments for businesses acquired, net"]["2026-05-03"] + CFq["Payments for businesses acquired, net"]["2026-08-02"])

# ---------- Flag: cash flow ----------
cfo = CFa["Net cash provided by operating activities"]
lines = ["Changes in accounts payable and accrued expenses", "Changes in merchandise inventories", "Changes in income taxes payable"]
R["cf_swings"] = {l: CFa[l][F26] - CFa[l][F25] for l in lines}
R["cf_three_swing"] = sum(R["cf_swings"].values())
wc = ["Changes in receivables, net", "Changes in merchandise inventories", "Changes in other current assets",
      "Changes in accounts payable and accrued expenses", "Changes in deferred revenue", "Changes in income taxes payable"]
R["wc"] = [sum(CFa[l][F25] for l in wc), sum(CFa[l][F26] for l in wc)]
(er_wc26, er_wc25), _ = row("ER26", "Changes in working capital", 2)
assert [er_wc25, er_wc26] == R["wc"], (er_wc25, er_wc26, R["wc"])
R["cfo_fall"] = cfo[F25] - cfo[F26]
(tp26, tp25, tp24), P["taxpaid"] = row("AR26", "Total income taxes paid", 3)
R["tax_paid"] = [tp25, tp26]

# ---------- Flag: goodwill ----------
gw = BSa["Goodwill"]
(_, _, acq25), P["gw"] = row("AR26", "Acquisitions (1)", 3, occurrence=0)
(_, _, acq26), _ = row("AR26", "Acquisitions (1)", 3, occurrence=1)
R["gw_rise_2y"] = gw[F26] - gw[F24]
R["gw_acq_2y"] = acq25 + acq26
R["srs_gw"] = [srs_gw25, srs_gw]  # as first reported, as finalised
R["gms_gw"] = gms_gw
(_, gw_other, _), _ = row("AR26", "Goodwill, balance at February 1, 2026", 3)
R["gw_other"] = gw_other

# ---------- Adjusted earnings (results releases) ----------
adj = "RECONCILIATION OF ADJUSTED DILUTED EARNINGS PER SHARE"
g26, _ = row("ER26", "Diluted earnings per share (GAAP)", 6, after=adj)
a26, P["adj26"] = row("ER26", "Adjusted diluted earnings per share (Non-GAAP)", 6, after=adj)
g25, _ = row("ER25", "Diluted earnings per share (GAAP)", 6, after=adj)
a25_, P["adj25"] = row("ER25", "Adjusted diluted earnings per share (Non-GAAP)", 6, after=adj)
# columns: Q4 this yr, Q4 last yr, % change, FY this yr, FY last yr, % change
R["eps"] = {"FY Feb-26": (g26[3], a26[3]), "FY Feb-25": (g25[3], a25_[3]), "FY Jan-24": (g25[4], a25_[4])}
assert g26[4] == g25[3] and a26[4] == a25_[3]
R["eps_gap"] = {k: (round(a - g, 2), (a - g) / g * 100) for k, (g, a) in R["eps"].items()}
op = "RECONCILIATION OF ADJUSTED OPERATING INCOME AND ADJUSTED OPERATING MARGIN"
am26, _ = row("ER26", "Acquired intangible asset amortization (4)", 4, after=op)
am25, _ = row("ER25", "Acquired intangible asset amortization (4)", 4, after=op)
R["intang_amort"] = {"FY Feb-26": am26[2], "FY Feb-25": am25[2], "FY Jan-24": am25[3]}
wk53 = 0.30  # per the releases: the extra week added approximately $0.30 to FY Feb-25 reported and adjusted EPS
for doc in ("ER25", "ER26"):
    assert "approximately $0.30 to adjusted diluted earnings per share" in T[doc]
R["adj_eps_change"] = pct(a26[3], a26[4])
R["adj_eps_change_52wk"] = pct(a26[3], a26[4] - wk53)
R["gaap_eps_change"] = pct(g26[3], g26[4])
R["gaap_eps_change_52wk"] = pct(g26[3], g26[4] - wk53)
R["releases_use_nonrecurring_words"] = {doc: bool(re.search(r"non-?recurring|one-time|unusual", T[doc], re.I)) for doc in ("ER25", "ER26")}
(next_amort,), P["next_amort"] = row("AR26", "Fiscal 2026", 1, after="The following table presents the estimated future amortization expense")
R["next_year_amort"] = next_amort

# ---------- Reserves ----------
R["change_in_estimate_phrase"] = {doc: bool(re.search(r"changes? in (accounting )?estimate", T[doc], re.I)) for doc in T}
(va25, va24), P["va25"] = row("AR25", "Valuation allowance", 2)
(va26, va25b), P["va26"] = row("AR26", "Valuation allowance", 2)
assert va25 == va25b
R["valuation_allowance"] = [-va24, -va25, -va26]
R["va_release_pts_of_tax_rate"] = (-va24 + va25) / ISa["Earnings before provision for income taxes"][F25] * 100
R["etr"] = {y: ISa["Provision for income taxes"][y] / ISa["Earnings before provision for income taxes"][y] * 100 for y in (F24, F25, F26)}
m25 = re.search(r"increased cost of sales by approximately \$(\d+) million for fiscal 2024", T["AR25"])
m26 = re.search(r"increased cost of sales by approximately \$(\d+) million for fiscal 2025", T["AR26"])
R["shrink_sens"] = [int(m25.group(1)), int(m26.group(1))]
P["shrink"] = [page_of(T["AR25"], m25.start()), page_of(T["AR26"], m26.start())]
R["shrink_sens_change"] = pct(R["shrink_sens"][1], R["shrink_sens"][0])
(u26, u25, u24), P["utb"] = row("AR26", "Unrecognized tax benefits balance at end of fiscal year", 3)
R["utb"] = [u24, u25, u26]
si25 = re.search(r"were \$([\d.]+) billion at February 2, 2025, and \$([\d.]+) billion at January 28, 2024", T["AR25"])
si26 = re.search(r"were \$([\d.]+) billion at February 1, 2026, and \$([\d.]+) billion at February 2, 2025", T["AR26"])
R["self_insurance_bn"] = [float(si25.group(2)), float(si25.group(1)), float(si26.group(1))]

print(json.dumps(R, indent=1, default=str))
print("pages:", P)

# ================= build the reply =================
f1 = lambda v: f"{v:.1f}"
n0 = lambda v: f"{v:,.0f}"
L = []
# --- 1. operating margin
L.append(f"**Operating margin down again, {f1(R['co_opm'][1])}% to {f1(R['co_opm'][2])}% (whole company)**")
L.append("- **The company says:** SG&A rose on \"higher payroll and related costs\" and a \"non-recurring legal-related benefit\" the year before (FY Feb-26 report, p. 34). "
         "Last year: different in part; payroll, plus \"lower legal-related benefits\" (FY Feb-25 report, p. 34).")
L.append(f"- **Test:** Primary segment SG&A (stores and online, before SRS and GMS) rose {f1(R['primary_sga_growth_26'])}% to {n0(pg26)} while its sales fell {f1(-R['primary_sales_growth_26'])}% (52 weeks against 53); "
         "neither report sizes payroll or the legal benefit, so the explanation partly holds.")
L.append(f"- **Reading:** most likely the business weakening: Primary SG&A is up {f1(R['primary_sga_growth_2y'])}% in two years on flat sales, taking its operating margin from {f1(R['primary_opm'][0])}% to {f1(R['primary_opm'][2])}%. "
         "A large legal benefit in FY Feb-25 would mean that year was flattered instead; both reports cite one.")
L.append(f"- **Read next:** Note 2, Primary segment table (FY Feb-26 report, p. {P['primary']}); Note 12 (p. 73) gives no legal amounts.")
L.append("")
# --- 2. inventory and payables
L.append(f"**Inventory up {f1(R['inv_growth_26'])}%, payables down {f1(-R['ap_growth_26'])}% in FY Feb-26 (whole company)**")
L.append("- **The company says:** turnover fell on \"higher average inventory levels\" (FY Feb-26 report, p. 32) and cash flow on \"the timing of vendor payments\" (p. 37), with no cause for either. "
         "Last year: \"lower average inventory levels\" (FY Feb-25 report, p. 32); the same vendor-payments phrase (p. 38).")
L.append(f"- **Test:** inventories rose {n0(R['inv_rise'])}, of which GMS brought {n0(gms_inv)} (FY Feb-26 report, p. {P['gms']}) and {n0(R['inv_built_cf'])} was built; payables fell {n0(R['ap_fall'])} although GMS brought {n0(gms_ap)}. "
         f"The turnover figures reproduce ({R['turnover5'][1]:.2f} and {R['turnover5'][0]:.2f} times on quarter-end averages), so the explanation partly holds: it describes the movement without explaining it.")
L.append(f"- **Reading:** can't tell from these documents; possibly ordinary, as days inventory ({f1(R['days_inv'][F26])}) is below the Jan-23 level ({f1(R['days_inv'][F23])}) and tariffs raised costs (p. 32). "
         f"Markdowns, or a fall in Primary gross margin (it rose from {f1(R['primary_gm'][1])}% to {f1(R['primary_gm'][2])}%), would point to the business weakening.")
L.append(f"- **Read next:** Note 1, supplier finance table (p. {P['supfin']}), where invoices confirmed fell {f1(-R['supfin_confirmed_change'])}%; the critical audit matter on merchandise inventories (pp. 41-42).")
L.append("")
# --- 3. receivables
L.append(f"**Receivables up {f1(R['rec_growth'][0])}%, then {f1(R['rec_growth'][1])}% (whole company)**")
L.append(f"- **The company says:** nothing in the FY Feb-26 report on why customer receivables rose from {n0(cr25)} to {n0(cr26)} (p. {P['rec26']}). "
         f"Last year: \"primarily as a result of the SRS acquisition\" (FY Feb-25 report, p. {P['rec25']}).")
assert P["srs25"] == P["gms"] == 74
L.append(f"- **Test:** receivables rose {n0(R['rec_rise'][0])} in FY Feb-25 against {n0(srs_rec)} acquired with SRS, and {n0(R['rec_rise'][1])} in FY Feb-26 against {n0(gms_rec)} acquired with GMS (p. 74 of each report), "
         "so the acquisition explanation holds for both years. Q2 Aug-26 can't be tested from these documents.")
L.append("- **Reading:** most likely ordinary: the acquired distributors brought more receivables than the whole increase. "
         "An allowance that stops being \"not material\" (FY Feb-26 report, p. 48), with customers said to \"increasingly use trade credit\" (p. 24), would point to the business weakening.")
L.append("- **Read next:** Note 1, receivables table (p. 48), and the 2026 quarterly reports, which are not attached.")
L.append("")
# --- other flags
L.append("**Other flags**")
L.append(f"- **Cash flow fell more than earnings (FY Feb-26):** \"timing of vendor payments and increased inventories\", plus a tax payment deferred from the year before (FY Feb-26 report, p. 37). "
         f"Held: those three cash flow lines swung by {n0(-R['cf_three_swing'])} against a {n0(R['cfo_fall'])} fall in operating cash flow, and income taxes paid rose from {n0(tp25)} to {n0(tp26)} (p. {P['taxpaid']}).")
L.append(f"- **Goodwill and intangibles:** \"preliminary determination of goodwill related to the GMS acquisition\", after SRS the year before (FY Feb-26 report, p. {P['gw']}). "
         f"Held: goodwill rose {n0(R['gw_rise_2y'])} in two years against {n0(R['gw_acq_2y'])} of acquisitions (SRS {n0(srs_gw)} as finalised, {n0(srs_gw25)} as first reported); "
         f"the acquired businesses earned {n0(oo26)} of operating income on {n0(os26)} of sales (p. {P['other']}).")
L.append("")
e = R["eps"]
gp = R["eps_gap"]
assert not any(R["releases_use_nonrecurring_words"].values())
L.append(f"**Adjusted earnings:** diluted EPS was {e['FY Feb-25'][0]:.2f} reported and {e['FY Feb-25'][1]:.2f} adjusted in FY Feb-25 (gap {gp['FY Feb-25'][0]:.2f}, {f1(gp['FY Feb-25'][1])}%), "
         f"then {e['FY Feb-26'][0]:.2f} and {e['FY Feb-26'][1]:.2f} in FY Feb-26 (gap {gp['FY Feb-26'][0]:.2f}, {f1(gp['FY Feb-26'][1])}%); "
         f"the only adjustment in both years is acquired intangible amortization ({n0(R['intang_amort']['FY Feb-25'])}, then {n0(R['intang_amort']['FY Feb-26'])}, before tax), which recurs every year.")
L.append(f"Neither release uses \"non-recurring\", \"one-time\" or \"unusual\". Left in both measures: the 53rd week (about $0.30 of FY Feb-25 EPS; without it adjusted EPS fell {f1(-R['adj_eps_change_52wk'])}%, not {f1(-R['adj_eps_change'])}%) "
         "and the legal benefit that the annual report, not the release, calls \"non-recurring\".")
L.append("")
assert not any(R["change_in_estimate_phrase"].values())
va = R["valuation_allowance"]
L.append("**Reserve releases:** neither report describes a reserve released through a change in estimate, and no claims or payments are disclosed to test one. "
         f"Two balances fell: the deferred tax valuation allowance, from {n0(va[0])} to {n0(va[1])} in FY Feb-25, called \"not material\" (FY Feb-25 report, p. {P['va25']}) though equal to {f1(R['va_release_pts_of_tax_rate'])} points of that year's tax rate if it went through income; "
         f"and the shrink reserve, whose 10% sensitivity fell from ${R['shrink_sens'][0]} million to ${R['shrink_sens'][1]} million (p. {P['shrink'][0]} of each report).")
reply = "\n".join(L) + "\n"

# ================= checks before saving =================
# 1. every quotation: exact substring of the cited file, and on the cited page
QUOTES = [
    ("higher payroll and related costs", "AR26", 34),
    ("non-recurring legal-related benefit", "AR26", 34),
    ("lower legal-related benefits", "AR25", 34),
    ("higher average inventory levels", "AR26", 32),
    ("the timing of vendor payments", "AR26", 37),
    ("lower average inventory levels", "AR25", 32),
    ("the timing of vendor payments", "AR25", 38),   # "the same phrase (p. 38)"
    ("primarily as a result of the SRS acquisition", "AR25", 48),
    ("not material", "AR26", 48),
    ("increasingly use trade credit", "AR26", 24),
    ("timing of vendor payments and increased inventories", "AR26", 37),
    ("preliminary determination of goodwill related to the GMS acquisition", "AR26", 60),
    ("non-recurring", "AR26", 34),
    ("not material", "AR25", 66),
]
ok = True
for q, doc, pg in QUOTES:
    exact = q in T[doc]
    pgs = pages_of(doc, q) if exact else []
    good = exact and pg in pgs
    ok &= good
    print(f"{'PASS' if good else 'FAIL'} | {doc} p.{pg} | exact={exact} | \"{q}\"")
assert ok
LABELS = {"non-recurring", "one-time", "unusual"}  # the prompt's own search words
for q in re.findall(r'"([^"]+)"', reply):
    assert any(q == x[0] for x in QUOTES) or q in LABELS, q
print("every quoted string in the reply is on the verified list:", True)
# 2. page checks for cited passages that are paraphrased, not quoted
def on_page(doc, s, pg):
    assert pg in pages_of(doc, s), (doc, s, pages_of(doc, s))
on_page("AR26", "we experienced increased costs as a result of tariffs in fiscal 2025", 32)
on_page("AR26", "12.COMMITMENTS AND CONTINGENCIES", 73)
on_page("AR26", "Sufficiency of audit evidence over certain merchandise inventories", 41)
on_page("AR26", "We identified the sufficiency of audit evidence over merchandise inventories", 42)
on_page("AR26", "deferral of our fourth quarter fiscal 2024 estimated federal tax payment", 37)
on_page("AR26", "Customer receivables relate to credit extended directly to certain customers", 48)
assert "Estimation of store shrink" in T["AR25"] and "Estimation of store shrink" not in T["AR26"]
assert P["primary"] == 55 and P["gms"] == 74 and P["supfin"] == 51 and P["rec26"] == 48 and P["rec25"] == 48 and P["taxpaid"] == 65
assert P["gw"] == 60 and P["other"] == 55 and P["va25"] == 66 and P["shrink"] == [39, 39], P
# 3. the FY Feb-26 receivables note really gives no reason
note26 = T["AR26"][T["AR26"].index("The following table presents components of receivables, net:"):T["AR26"].index("Merchandise Inventories\n")]
assert "acquisition" not in note26.lower() and "increase" not in note26.lower()
# 4. statements made in words
assert R["primary_gm"][2] > R["primary_gm"][1] and R["days_inv"][F26] < R["days_inv"][F23]
assert round(R["turnover5"][1], 1) == 4.4 and round(R["turnover5"][0], 1) == 4.7
assert srs_rec > R["rec_rise"][0] and gms_rec > R["rec_rise"][1]
assert all(v > 0 for v in R["cf_rec_change"])
assert "—" not in reply
for w in ("fraud", "manipulat", "red flag"):
    assert w not in reply.lower()
print("quotation check: all", len(QUOTES), "passed (exact text and page)")
print("word count:", len(reply.split()))
open(os.path.join(HERE, "numbers-2.md"), "w", encoding="utf-8").write(reply)
shutil.copyfile(os.path.abspath(__file__), os.path.join(HERE, "numbers-code-2.py"))
print(reply)
