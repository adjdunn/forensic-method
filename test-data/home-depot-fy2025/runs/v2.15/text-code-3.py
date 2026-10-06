# Step 3, read the footnotes: Home Depot, fiscal year ended 1 February 2026.
# Every number in the reply is computed here; every quotation is checked against the file and page.
import re, os, openpyxl
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
LATEST = os.path.join(BASE, 'annual-report-FY2026-02-01-key-sections.txt')
txt = open(LATEST, encoding='utf-8').read()
wb = openpyxl.load_workbook(os.path.join(BASE, 'statements.xlsx'), data_only=True)

def sheet(name):
    ws = wb[name]; rows = list(ws.iter_rows(values_only=True)); hdr = rows[0]
    return {r[0]: dict(zip(hdr[1:], r[1:])) for r in rows[1:] if r[0]}
IS, BS, CF = sheet('IS annual'), sheet('BS annual'), sheet('CF annual')
Y, P = 'FY (ended 2026-02-01)', 'FY (ended 2025-02-02)'
EQ = [k for k in BS if k.startswith('Total stockholders') and 'liabilities' not in k][0]
pretax = IS['Earnings before provision for income taxes'][Y]
sales, cogs = IS['Net sales'][Y], IS['Cost of sales'][Y]
pct = lambda a, b=pretax: 100 * a / b

# ---- figures taken from the notes of the latest report (page markers in comments)
gw_other = 13780                                                  # p.60
other_oi, other_sales, other_sales_py = 316, 12717, 6406          # p.55
other_amort = 398                                                 # p.56
consideration = 18028 + 5081                                      # p.75, p.74
cr_gross, cr_gross_py, cr_acc, cr_acc_py, cr_net = 10517, 8845, 1535, 1035, 8982   # p.60
fut_total, fut_after5 = 9680, 6476                                # p.61
nopat, nopat_py, avg_cap, avg_cap_py = 15897, 16424, 61914, 52431 # p.35
cp, cp_py, cp_py2 = BS['Short-term debt'][Y], BS['Short-term debt'][P], 0
dep_note = 3452                                                   # p.58
dep_cf = CF['Depreciation and amortization, excluding amortization of intangible assets'][Y]  # p.47
depr_base = ((21321 + 20289 + 2571 + 4133) + (20260 + 18474 + 2423 + 4045)) / 2   # p.58, cost excluding land and construction in progress
self_ins, sf_end = 1600, 414                                      # p.52, p.51
prim_sales, prim_sales_py, prim_sga, prim_sga_py = 151966, 153108, 28885, 27822   # p.55
gms_assets_ex = 7186 - 2610 - 1800                                # p.74
gms_sales = 2000                                                  # p.75

# ---- calculations
other_ret = pct(other_oi, consideration); other_ret_pre = pct(other_oi + other_amort, consideration)
cr_charge = cr_acc - cr_acc_py; cr_avg = (cr_gross + cr_gross_py) / 2
cr_life = cr_avg / cr_charge; cr_15 = cr_avg / 15 - cr_charge
roic = pct(nopat, avg_cap); roic_cp = pct(nopat, avg_cap + (cp + cp_py) / 2)
roic_py = pct(nopat_py, avg_cap_py); roic_py_cp = pct(nopat_py, avg_cap_py + (cp_py + cp_py2) / 2)
ltd = lambda c: BS['Current installments of long-term debt'][c] + BS['Long-term debt, excluding current installments'][c]
assert abs(((ltd(Y) + BS[EQ][Y]) + (ltd(P) + BS[EQ][P])) / 2 - avg_cap) < 1
ltd_chg = ltd(Y) - ltd(P)
dpo = BS['Accounts payable'][Y] / cogs * 365
dep_life = depr_base / dep_note
defrev = BS['Deferred revenue'][Y]
co_assets_ex = BS['Total assets'][Y] - BS['Goodwill'][Y] - BS['Intangible assets, net'][Y]

reply = f"""Pages are the [p. N] markers in the latest annual report. Pre-tax income was ${pretax:,} million.

**1. Policy profile**

| Area | What the report says | Where it sits | Why |
|---|---|---|---|
| Revenue recognition | "at the time the customer takes possession of merchandise" (p. 52) | Typical | Point of sale, net of returns; the $1.5bn and $1.1bn of deferred revenue tie to the ${defrev:,}m balance; the returns liability has no amount |
| Reserves and allowances | Receivables allowance "was not material" (p. 48); self-insurance at "expected ultimate cost for claims incurred (undiscounted)" (p. 52) | Can't tell | Self-insurance of $1.6bn ({pct(self_ins):.1f}% of pre-tax income) is undiscounted, which is cautious, but no reserve shows its movements |
| Capitalized costs and useful lives | Intangible lives "range up to approximately 20 years" (p. 51) | Leans aggressive | Customer lists run {cr_life:.1f} years straight-line; buildings and equipment imply {dep_life:.1f} years, which is ordinary |
| Impairment and goodwill | Acquired units' fair value "exceeded its respective carrying amount, including goodwill" (p. 60) | Leans aggressive | ${gw_other:,}m of goodwill with no room stated; rests on thin disclosure |
| Off the balance sheet | "no material off-balance sheet arrangements" (p. 37) | Typical | Leases are on the balance sheet; supplier finance is ${sf_end}m ({pct(sf_end, BS['Accounts payable'][Y]):.1f}% of payables) and {dpo:.0f} days payable sits inside the stated 30 to 60 days |
| Related parties | No note and no statement either way | Can't tell | Not in the documents |
| Contingencies and legal | "not expected to have a material adverse effect" (p. 73) | Typical | Standard wording with no accrual or range; rests on general practice |
| Auditor's report and controls | "present fairly, in all material respects" (p. 41); "Management excluded GMS" (p. 77) | Typical | Clean opinions, no material weakness; one critical audit matter, on inventory systems |
| Adjusted (non-GAAP) measures | ROIC on "long-term debt (including current installments) and equity" (p. 35) | Leans aggressive | The only such measure; its capital base leaves out ${cp:,}m of commercial paper |

**2. Full write-ups**

**Impairment and goodwill: the room on ${gw_other/1000:.1f}bn of acquired goodwill is not shown**
- **The report says:** the older retail units "substantially exceeded" carrying amount, but the acquired distribution units only "exceeded its respective carrying amount, including goodwill" (Note 4, p. 60).
- **Test:** no margin is given to test. The acquired businesses earned ${other_oi}m of operating income on ${consideration:,}m paid for them, {other_ret:.1f}% ({other_ret_pre:.1f}% before intangible amortization), with the second acquisition owned for five months. Size: ${gw_other:,}m, {pct(gw_other):.0f}% of pre-tax income, a balance-sheet amount.
- **Reading:** can't tell; the weaker wording and the low current return possibly mean thin room. A stated margin well above carrying amount would point to ordinary.
- **Read next:** the percentage excess per reporting unit and the discount and growth rates used; goodwill is not among the critical accounting estimates (p. 38).

**Useful lives: customer lists spread evenly over about 20 years**
- **The report says:** straight-line "as this approximates the pattern of expected economic benefit" (Note 1, p. 51), while the same assets are valued on "expected customer attrition rates" (p. 38).
- **Test:** the year's charge of ${cr_charge}m on average cost of ${cr_avg:,.0f}m implies {cr_life:.1f} years, so the 20-year claim holds; {pct(fut_after5, fut_total):.0f}% of remaining amortization falls after five years. At 15 years the charge would be ${cr_15:,.0f}m higher ({pct(cr_15):.1f}% of pre-tax income). Size: ${cr_net:,}m net, {pct(cr_net):.0f}% of pre-tax income, a balance-sheet amount.
- **Reading:** most likely the reporting stretched a little, since a list that loses customers each year gives more benefit early than late; this rests on general practice. Disclosed attrition low enough to fit an even 20-year pattern would point to ordinary.
- **Read next:** the attrition rates assumed in the valuations (Note 13, pp. 74 and 76).

**Non-GAAP: ROIC leaves out the commercial paper that replaced notes**
- **The report says:** ROIC uses "long-term debt (including current installments) and equity" (p. 35), and commercial paper funded "the repayment of senior note maturities" (p. 36).
- **Test:** the reported {roic:.1f}% is reproduced. Long-term debt fell ${-ltd_chg:,}m while commercial paper rose ${cp - cp_py:,}m; counting commercial paper gives {roic_cp:.1f}%, and the fall from last year becomes {roic_py_cp - roic_cp:.1f} points, not {roic_py - roic:.1f}. Size: ${cp:,}m, {pct(cp):.0f}% of pre-tax income, a balance-sheet amount.
- **Reading:** possibly the reporting stretched: moving borrowing into commercial paper shrinks the capital base of a measure that share awards pay on ("target average ROIC and operating profit", p. 71). A definition unchanged from earlier years would point to ordinary.
- **Read next:** last year's definition, and the proxy statement's ROIC targets.

**3. Also noted**
- Depreciation in the cash flow statement (${dep_cf:,}m, p. 47) is ${dep_cf - dep_note}m above the depreciation note (${dep_note:,}m, p. 58); the gap is unexplained.
- A "non-recurring legal-related benefit" in the prior year is given no amount (p. 34); retail-segment SG&A rose {pct(prim_sga - prim_sga_py, prim_sga_py):.1f}% while retail-segment sales fell {-pct(prim_sales - prim_sales_py, prim_sales_py):.1f}% against a 53-week year.
- The controls opinions leave out GMS, put at "approximately 3%" of assets excluding goodwill and intangibles (p. 77); its acquisition-date assets work out to {pct(gms_assets_ex, co_assets_ex):.1f}%.
- Store credit card receivables are owned by third parties that "should not be consolidated", with an option to buy them in 2028; no amount is given (p. 52).

**4. Not in the documents:** related-party disclosures, Schedule II and the proxy statement are not included, and the report carries no adjusted earnings measure.
"""

# ---- quotation check: every quoted string must sit on the cited page of the latest report
marks = [(m.start(), int(m.group(1))) for m in re.finditer(r'\[p\. (\d+)\]', txt)]
def page_of(i):
    pg = None
    for pos, n in marks:
        if pos <= i: pg = n
        else: break
    return pg
def pages_with(q):
    return sorted({page_of(m.start()) for m in re.finditer(re.escape(q), txt)})
quotes = [
 ("at the time the customer takes possession of merchandise", 52),
 ("was not material", 48),
 ("expected ultimate cost for claims incurred (undiscounted)", 52),
 ("range up to approximately 20 years", 51),
 ("exceeded its respective carrying amount, including goodwill", 60),
 ("no material off-balance sheet arrangements", 37),
 ("not expected to have a material adverse effect", 73),
 ("present fairly, in all material respects", 41),
 ("Management excluded GMS", 77),
 ("long-term debt (including current installments) and equity", 35),
 ("substantially exceeded", 60),
 ("as this approximates the pattern of expected economic benefit", 51),
 ("expected customer attrition rates", 38),
 ("the repayment of senior note maturities", 36),
 ("target average ROIC and operating profit", 71),
 ("non-recurring legal-related benefit", 34),
 ("approximately 3%", 77),
 ("should not be consolidated", 52),
]
fails = []
for q, pg in quotes:
    if pg not in pages_with(q): fails.append((q, pg, pages_with(q)))
    if not re.search(re.escape('"' + q + '"') + r'[^|\n]*?p\. ' + str(pg), reply): fails.append((q, pg, 'not quoted with that page in reply'))
extra = set(re.findall(r'"([^"]+)"', reply)) - {q for q, _ in quotes}
print('quotes checked:', len(quotes), '| failures:', fails, '| quoted strings in reply not on the list:', extra)
# figures taken from the notes must appear in the report text
for s in ['13,780', '8,982', '3,452', '$414', '9,680', '6,476', '15,897', '61,914', '18,028', '5,081', '28,885', '27,822', '7,186']:
    assert s in txt, s
assert round(roic, 1) == 25.7 and '—' not in reply and '>' not in reply
open(os.path.join(BASE, 'runs', 'v2.15', 'text-3.md'), 'w', encoding='utf-8').write(reply)
print('words:', len(reply.split()))
print(dict(cr_life=round(cr_life, 2), cr_15=round(cr_15), other_ret=round(other_ret, 2), other_ret_pre=round(other_ret_pre, 2),
           roic=round(roic, 2), roic_cp=round(roic_cp, 2), roic_py=round(roic_py, 2), roic_py_cp=round(roic_py_cp, 2),
           ltd_chg=ltd_chg, cp_chg=cp - cp_py, dpo=round(dpo, 1), dep_life=round(dep_life, 1),
           gms_assets=round(pct(gms_assets_ex, co_assets_ex), 2), gms_sales=round(pct(gms_sales, sales), 2),
           gw_pct=round(pct(gw_other), 1), cr_pct=round(pct(cr_net), 1), cp_pct=round(pct(cp), 1)))
