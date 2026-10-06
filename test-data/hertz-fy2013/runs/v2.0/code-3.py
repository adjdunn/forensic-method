# Turn 3: read the footnotes (FY2013 annual report). Inputs pulled from named rows of the
# attached text files; arithmetic here; then the quotation check for reply-3.md.
import json, os, re
from common import *

A13, A12, R13, R12 = "FY2013 annual report", "FY2012 annual report", "FY2013 release", "FY2012 release"
def pct(a, b): return (a / b - 1) * 100
out = {}

pti13, pti12, pti11 = row(A13, "Income before income taxes", page=76)
ni13 = row(A13, "Net income", page=76)[0]
rev13, rev12, rev11 = row(A13, "Total revenues", page=76)
q4_pti13 = row(R13, "Income (loss) before income taxes", page="unnumbered")[0]

# 1. Advantage / Simply Wheelz
impair, fair_value = 40.0, 279.0                       # p. 146, p. 147
adj_line = -row(A13, "Impairment charges and other(10)", page=134)[0]      # 44.0
sublease = [-x for x in row(R13, "Advantage sublease revenue", nth=1)]     # twelve months: 65.0, 3.7
us_rev13 = row(A13, "U.S. car rental", page=131)[0]
loss_2012, locations_2012, sale_price, current_assets = 31.4, 24.1, 16.0, 3.6   # p. 101; FY2012 report p. 91
out["advantage"] = dict(
    carrying_before=fair_value + impair, writedown_pct=impair / (fair_value + impair) * 100,
    adjusted_line=adj_line, unexplained_other=adj_line - impair,
    sublease_revenue=sublease, sublease_pct_us_revenue=sublease[0] / us_rev13 * 100,
    charges_since_sale=loss_2012 + adj_line, with_location_divestitures=loss_2012 + adj_line + locations_2012,
    proceeds=sale_price + current_assets, impairment_pct_pretax=adj_line / pti13 * 100,
)

# 2. Financing requirement missed; borrowing room and maturities
mat = [2053.3, 5284.5, 1367.5, 366.0, 3643.5, 3587.8]                   # p. 104
tot_debt = row(A13, "Total Debt", page=103)[0]
hvf2 = row(A13, "HVF II Series 2013-A(4)", page=102)[1] + row(A13, "HVF II Series 2013-B(4)", page=102)[1]   # rate, Dec 2013 balance
hvf09 = row(A13, "HVF Series 2009-1(4)", page=102)[1]
avail13 = row(A13, "Total Fleet Debt", page=114)                         # 1,041.1 ; 23.9
avail12 = row(A12, "Total Fleet Debt", page=101)                         # 1,083.5 ; 35.4
avail_tot13 = row(A13, "Total |", page=114)
cash13 = row(A13, "Cash and cash equivalents", page=75)[0]
out["financing"] = dict(
    maturities_sum=sum(mat), due_2014_2015=mat[0] + mat[1], due_2014_2015_pct=(mat[0] + mat[1]) / sum(mat) * 100,
    affected_notes=hvf2 + hvf09, affected_pct_debt=(hvf2 + hvf09) / tot_debt * 100, hvf2=hvf2,
    fleet_capacity_2013=avail13, fleet_avail_pct_2013=avail13[1] / avail13[0] * 100,
    fleet_capacity_2012=avail12, fleet_avail_pct_2012=avail12[1] / avail12[0] * 100,
    total_availability=avail_tot13, availability_plus_cash=avail_tot13[1] + cash13, due_2014=mat[0],
)

# 3. Performance pay on Corporate EBITDA
ce_row = row(R13, "Corporate EBITDA |", after="FREE CASH FLOW, EBITDA, AND CORPORATE EBITDA", nth=1)
ce13, ce12 = ce_row[5], ce_row[11]
unusual = row(R13, "Extraordinary, unusual or non-recurring gains and losses (c)", nth=1)
guide_lo, guide_hi = 2210.0, 2270.0                                       # FY2012 release p. 4
apti_lo, apti13 = 1270.0, 1153.2
eps_lo, eps13 = 1.82, 1.63
sbc_q4 = [-x for x in row(R13, "Stock-based compensation charges")[:2]]   # 3.5, 8.0
out["pay"] = dict(
    corp_ebitda=(ce13, ce12), guidance=(guide_lo, guide_hi), shortfall_vs_low=guide_lo - ce13, shortfall_pct=(1 - ce13 / guide_lo) * 100,
    adj_pretax_shortfall_pct=(1 - apti13 / apti_lo) * 100, eps_shortfall_pct=(1 - eps13 / eps_lo) * 100,
    rate_cut_pct_of_corp_ebitda=(44.2 / ce13 * 100, 139.4 / ce12 * 100),
    unusual_addbacks=(unusual[5], unusual[11]), unusual_pct=(unusual[5] / ce13 * 100, unusual[11] / ce12 * 100),
    q4_stock_comp=sbc_q4, q4_stock_comp_change=pct(*sbc_q4),
)

# 4. Concession minimums
minfix = row(A13, "Minimum fixed obligations", page=129)
addl = row(A13, "Additional amounts, based on revenues", page=129)
rents = row(A13, "Rents |", page=129)
tot = row(A13, "Total |", page=129)
sched13 = [row(A13, y, page=130) for y in ("2014 |", "2015 |", "2016 |", "2017 |", "2018 |", "Years after 2018 |")]
sched12 = [row(A12, y, page=117) for y in ("2013 |", "2014 |", "2015 |", "2016 |", "2017 |", "Years after 2017 |")]
fut_r13, fut_c13 = sum(s[0] for s in sched13), sum(s[1] for s in sched13)
fut_r12, fut_c12 = sum(s[0] for s in sched12), sum(s[1] for s in sched12)
minfix12_first = row(A12, "Minimum fixed obligations", page=116)[0]
out["concessions"] = dict(
    min_fixed=minfix, min_fixed_growth=pct(minfix[0], minfix[1]), additional=addl, additional_growth=pct(addl[0], addl[1]),
    revenue_growth=pct(rev13, rev12), fixed_share=(minfix[0] / (minfix[0] + addl[0]) * 100, minfix[1] / (minfix[1] + addl[1]) * 100),
    total_expense=tot[:3], total_growth=pct(tot[0], tot[1]),
    future_minimums_2013=(fut_r13, fut_c13, fut_r13 + fut_c13), future_minimums_2012=(fut_r12, fut_c12, fut_r12 + fut_c12),
    future_growth=pct(fut_r13 + fut_c13, fut_r12 + fut_c12), future_concession_growth=pct(fut_c13, fut_c12),
    due_next_year=sched13[0][0] + sched13[0][1], min_fixed_2012_as_first_reported=minfix12_first,
    future_vs_equity=(fut_r13 + fut_c13) / row(A13, "Total Hertz Global Holdings, Inc. and Subsidiaries stockholders' equity", page=75)[0] * 100,
)

# 5. Legal
out["legal"] = dict(
    judgment_pct_pretax=40.0 / pti13 * 100, judgment_pct_q4_pretax=40.0 / q4_pti13 * 100,
    errors_called_material_to_q4=46.3, litigation_accruals=(5.7, 14.0), litigation_accruals_sum=5.7 + 14.0,
)

# 6. Sponsors' exit and the buyback
buy_mar = 23.2 * 20.14; buy_q4 = 3.877 * 22.54
repurch = -row(A13, "Purchase of treasury shares", page=81)[0]
out["buyback"] = dict(
    march=buy_mar, q4=buy_q4, total_computed=buy_mar + buy_q4, total_cash_flow=repurch,
    pct_net_income=repurch / ni13 * 100, march_pct_net_income=buy_mar / ni13 * 100, notes_replenish_pct=250.0 / 467.2 * 100,
    sponsor_shares_sold_2013=(60050777 + 49800405) / 1e6, bought_pct_of_march_sale=23200000 / 60050777 * 100,
    relocation_execs=3.1,
)

# goodwill and intangibles (for the closing line)
gw = row(A13, "Goodwill", page=75)[0]; intang = row(A13, "Other intangible assets, net", page=75)[0]
eq = row(A13, "Total Hertz Global Holdings, Inc. and Subsidiaries stockholders' equity", page=75)[0]
out["intangibles"] = dict(total=gw + intang, pct_equity=(gw + intang) / eq * 100, trade_name=3330.0)

def show(d, ind=0):
    for k, v in d.items():
        if isinstance(v, dict): print(" " * ind + k + ":"); show(v, ind + 2)
        elif isinstance(v, (list, tuple)): print(" " * ind + f"{k}: " + ", ".join(f"{x:,.2f}" if isinstance(x, float) else str(x) for x in v))
        else: print(" " * ind + (f"{k}: {v:,.2f}" if isinstance(v, float) else f"{k}: {v}"))
show(out)

# ---- quotation check. In this reply a quote with no citation after it takes the page in
# its block's header, e.g. **Title** (Note 15, p. 146), and the FY2013 annual report.
def check_reply3(fn="reply-3.md"):
    r = open(os.path.join(HERE, fn), encoding="utf-8").read()
    n = ok = 0; fails = []
    head_page = None
    for line in r.split("\n"):
        h = re.match(r"\*\*.+?\*\* \((.*?)\)\s*$", line)
        if h:
            pm = re.search(r"p\. (\w+)", h.group(1)); head_page = pm.group(1) if pm else None
        if line.startswith("|") or line.startswith("**2.") or line.startswith("**3."):
            head_doc_default = A13
        for m in re.finditer(r'"([^"\n]+)"(\s*\(([^()]*?)\))?', line):
            q, cite = m.group(1), m.group(3) or ""
            doc = next((d for d in FILES if d in cite), A13)
            pm = re.search(r"p\. (\w+)", cite)
            if line.startswith("|"):      # table row: pages are in the last cell
                allowed = set(re.findall(r"p\. (\w+)", line.split("|")[-2]))
            else:
                allowed = {pm.group(1) if pm else head_page}
            n += 1
            hits = [x.start() for x in re.finditer(re.escape(q), text(doc))]
            if not hits: fails.append(("not an exact substring", q, doc, allowed)); continue
            pages = {page_at(doc, h_) for h_ in hits}
            if not (allowed & pages): fails.append((f"page is {sorted(pages)} not {allowed}", q, doc)); continue
            ok += 1
    print(f"{fn}: {n} quotations, {ok} pass, {len(fails)} fail")
    for f in fails: print("  FAIL:", f)
if os.path.exists(os.path.join(HERE, "reply-3.md")):
    print(); check_reply3(); print("words:", wc("reply-3.md"))
