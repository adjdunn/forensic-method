# Step 3 (read the footnotes): calculations, quotation check and reply writer.
# Run from the company folder (home-depot-fy2025):  python runs/v2.16/text-code-3.py --write
import re, sys, openpyxl
sys.stdout.reconfigure(encoding='utf-8')
LATEST = 'annual-report-FY2026-02-01-key-sections.txt'
txt = open(LATEST, encoding='utf-8').read()
wb = openpyxl.load_workbook('statements.xlsx', data_only=True)


def sheet(name):
    ws = wb[name]
    rows = list(ws.iter_rows(values_only=True))
    hdr = rows[0]
    return {r[0]: dict(zip(hdr[1:], r[1:])) for r in rows[1:] if r[0]}, hdr


IS, _ = sheet('IS annual')
BS, _ = sheet('BS annual')
CF, _ = sheet('CF annual')
BSQ, bsq_hdr = sheet('BS quarterly')
Y, P, PP = 'FY (ended 2026-02-01)', 'FY (ended 2025-02-02)', 'FY (ended 2024-01-28)'
EQ = [k for k in BS if k.startswith('Total stockholders')][0]

pti = IS['Earnings before provision for income taxes'][Y]
sales, sales_p = IS['Net sales'][Y], IS['Net sales'][P]
cogs = IS['Cost of sales'][Y]
opinc = IS['Operating income'][Y]


def pct(x):
    return 100 * x / pti


N = {'pti': pti}

# figures read from the latest report's notes (pages are given in the reply)
other_sales, other_sales_p = 12717, 6406          # Note 2
prim_sales, prim_sales_p = 151966, 153108
prim_cogs, prim_cogs_p = 99717, 101194
other_opinc = 316
gw_total, gw_other = 22344, 13780                 # Note 4
cust_rel_net, cust_acc, cust_acc_p = 8982, 1535, 1035
intang_amort = 607
dep_note3 = 3452                                  # Note 3
seg_da_total = 4059
gross_depr = 21321 + 20289 + 2571 + 4133          # buildings, FF&E, leasehold improvements, finance leases
gross_depr_p = 20260 + 18474 + 2423 + 4045
gms_consid, srs_consid = 5081, 18028              # Note 13
gms_sales = 2000
gms_assets_ex = 7186 - 2610 - 1800
cust_rec, cust_rec_p = 2588, 1896                 # Note 1
self_ins = 1600
supplier_fin = 414
lcs = 738
purch_obl = 1900
lease_not_commenced = 675
lease_pay_op, lease_pay_fin = 11638, 3591
cp, cp_p = BS['Short-term debt'][Y], BS['Short-term debt'][P]
CUR, LT = 'Current installments of long-term debt', 'Long-term debt, excluding current installments'
ltd, ltd_p, ltd_pp = (BS[CUR][k] + BS[LT][k] for k in (Y, P, PP))
eq, eq_p, eq_pp = (BS[EQ][k] for k in (Y, P, PP))

# 1 acquisitions "not material"
N['other_inc'] = other_sales - other_sales_p
N['sales_inc'] = sales - sales_p
N['other_share_of_inc'] = 100 * N['other_inc'] / N['sales_inc']
N['other_pct_sales'] = 100 * other_sales / sales
N['prim_growth'] = 100 * (prim_sales / prim_sales_p - 1)
N['sales_growth'] = 100 * (sales / sales_p - 1)
N['consid'] = gms_consid + srs_consid
N['consid_pct'] = pct(N['consid'])
N['other_opinc_pct'] = pct(other_opinc)
N['other_opinc_share'] = 100 * other_opinc / opinc
N['other_margin'] = 100 * other_opinc / other_sales
N['other_return'] = 100 * other_opinc / N['consid']
N['gw_pct'] = pct(gw_total)
N['gw_other_pct'] = pct(gw_other)
N['gms_sales_pct'] = 100 * gms_sales / sales
N['gms_assets_pct'] = 100 * gms_assets_ex / BS['Total assets'][Y]

# 2 return on invested capital
tax_rate = IS['Provision for income taxes'][Y] / pti
nopat = opinc - round(opinc * tax_rate)
avg_cap = ((ltd + eq) + (ltd_p + eq_p)) / 2
avg_cap_p = ((ltd_p + eq_p) + (ltd_pp + eq_pp)) / 2
N['nopat'] = nopat
N['avg_cap'] = avg_cap
N['avg_cap_p'] = avg_cap_p
N['roic'] = 100 * nopat / avg_cap
N['roic_cp'] = 100 * nopat / (avg_cap + (cp + cp_p) / 2)
N['roic_diff'] = N['roic'] - N['roic_cp']
N['cp_pct'] = pct(cp)
N['ltd_change'] = ltd - ltd_p
N['cp_change'] = cp - cp_p
N['avg_eq_change'] = (eq + eq_p) / 2 - (eq_p + eq_pp) / 2
N['avg_ltd_change'] = (ltd + ltd_p) / 2 - (ltd_p + ltd_pp) / 2

# 3 customer lists and property lives
N['cust_sl'] = 5400 / 20 + 1540 / 19
N['cust_sl_pct'] = pct(N['cust_sl'])
N['cust_charge'] = cust_acc - cust_acc_p
N['cust_charge_pct'] = pct(N['cust_charge'])
N['cust_net_pct'] = pct(cust_rel_net)
N['amort_pct'] = pct(intang_amort)
N['dep_rate'] = 100 * dep_note3 / ((gross_depr + gross_depr_p) / 2)
N['dep_life'] = 100 / N['dep_rate']
N['capex_dep'] = -CF['Capital expenditures'][Y] / dep_note3

# other tests
cf_da = CF['Depreciation and amortization, excluding amortization of intangible assets'][Y]
N['da_gap'] = cf_da - dep_note3
N['da_gap_pct'] = pct(N['da_gap'])
N['seg_da_check'] = dep_note3 + intang_amort - seg_da_total
inv, inv_p = BS['Merchandise inventories'][Y], BS['Merchandise inventories'][P]
N['turn_yearend'] = cogs / ((inv + inv_p) / 2)
qcols = [h for h in bsq_hdr[1:] if h and any(d in h for d in ('2025-02-02', '2025-05-04', '2025-08-03', '2025-11-02', '2026-02-01'))]
qinv = [BSQ['Merchandise inventories'][h] for h in qcols]
N['qcols'] = qcols
N['qinv'] = qinv
N['turn_5pt'] = cogs / (sum(qinv) / len(qinv))
N['prim_gm'] = 100 * (prim_sales - prim_cogs) / prim_sales
N['prim_gm_p'] = 100 * (prim_sales_p - prim_cogs_p) / prim_sales_p
N['cust_rec_growth'] = 100 * (cust_rec / cust_rec_p - 1)
N['cust_rec_pct'] = pct(cust_rec)
N['self_ins_pct'] = pct(self_ins)
N['def_rev_pct'] = pct(BS['Deferred revenue'][Y])
N['supplier_pct'] = pct(supplier_fin)
N['supplier_ap'] = 100 * supplier_fin / BS['Accounts payable'][Y]
N['lcs_pct'] = pct(lcs)
N['purch_pct'] = pct(purch_obl)
N['lease_total'] = lease_pay_op + lease_pay_fin + lease_not_commenced
N['inv_pct'] = pct(inv)
for k, v in N.items():
    print(k, v)


def f(k, d=1):
    return format(N[k], f',.{d}f')


reply = f"""All quotations and pages are from the latest annual report (year ended 1 February 2026). Sizes are shares of its pre-tax income (${pti:,} million).

**1. Policy profile**

| Area | What the report says | Where it sits | Why, in a few words | Size |
|---|---|---|---|---|
| 1. Revenue recognition | "at the time the customer takes possession of merchandise or when a service is performed" (p. 52) | Typical | Point-of-sale retail, net of expected returns; rests on general practice | Deferred revenue {f('def_rev_pct')}%; returns not quantified |
| 2. Reserves and allowances | "valuation allowance related to these receivables was not material" (p. 48) | Can't tell: not enough disclosed | No amounts for the allowance or returns, no movements, no Schedule II | Self-insurance {f('self_ins_pct')}%; customer receivables {f('cust_rec_pct')}% |
| 3. Capitalized costs and useful lives | "straight-line basis over their estimated useful lives, which range up to approximately 20 years" (p. 51) | Leans aggressive for acquired customer lists; property typical | Lists valued on "customer attrition rates" (p. 74) but charged evenly over 19 to 20 years; property charge implies about a {f('dep_life')}-year life | Intangible amortization {f('amort_pct')}% |
| 4. Impairment and goodwill | "exceeded its respective carrying amount, including goodwill" (p. 60) | Can't tell: not enough disclosed | No headroom given for the acquired units; the newest acquisition was not tested | Goodwill {f('gw_pct')}%; acquired units {f('gw_other_pct')}% |
| 5. Off the balance sheet | "We have no material off-balance sheet arrangements" (p. 37) | Typical | Leases are on the balance sheet and tie to the note; supplier finance is disclosed | Purchase obligations {f('purch_pct')}%; supplier finance {f('supplier_pct')}% |
| 6. Related parties | No related-party note in the sections provided | Can't tell: not in the documents | Nothing to judge | Not quantified |
| 7. Contingencies and legal | "not expected to have a material adverse effect" (p. 73) | Can't tell: not enough disclosed | No accrual or range; last year's "non-recurring legal-related benefit" (p. 34) has no amount | Not quantified |
| 8. Auditor and controls | "Sufficiency of audit evidence over certain merchandise inventories" (p. 41) | Typical | Clean opinions, one critical audit matter, no material weakness | Inventories {f('inv_pct')}% |
| 9. Adjusted measures | "long-term debt (including current installments) and equity" (p. 35) | Leans aggressive | The one adjusted measure, return on invested capital, leaves commercial paper out of capital; rests on general practice | Commercial paper {f('cp_pct')}% |

**2. Full write-ups**

**Acquisitions: called not material, yet they carry the sales growth**
- **The report says:** "the effect of the acquisition was not material to our financial results" (Note 13, p. 75 and p. 77), yet the sales increase was "primarily driven by SRS" and GMS (management discussion, p. 33).
- **Test:** the acquired businesses added ${N['other_inc']:,} million of sales (Note 2, p. 55), which is {f('other_share_of_inc', 0)}% of the whole-company increase of ${N['sales_inc']:,} million; whole-company sales grew {f('sales_growth')}% and Primary segment sales changed {f('prim_growth')}% (52 weeks against 53). The claim holds for earnings, not for sales or assets. Size: their operating income, ${other_opinc} million, is {f('other_opinc_pct')}% (an annual profit); the price paid, ${N['consid']:,} million, is {f('consid_pct', 0)}% (a one-time outlay).
- **Reading:** most likely ordinary: materiality was possibly judged on earnings, but the result is that no full-year figures are given for businesses earning {f('other_return')}% on their price before interest (GMS counted for five months). Full-year profit staying this low would point to goodwill (row 4) instead.
- **Read next:** the headroom by unit in the goodwill test, and the acquired companies' own last annual reports.

**Return on invested capital: commercial paper is left out of capital**
- **The report says:** "it measures how effectively we deploy our capital base" (management discussion, p. 35), and commercial paper funded "the repayment of senior note maturities" (p. 36).
- **Test:** the reported {f('roic')}% recomputes, so the arithmetic holds. But long-term debt fell ${-N['ltd_change']:,} million while commercial paper rose ${N['cp_change']:,} million, and the profit figure is before all interest. With average commercial paper counted, the figure is {f('roic_cp')}%. Size: commercial paper of ${cp:,} million is {f('cp_pct')}% (a year-end balance).
- **Reading:** possibly stretched, by about {f('roic_diff')} point, because borrowing moved to a line the definition does not count; share awards pay on "target average ROIC and operating profit" (p. 71). Repayment of the paper from cash flow within a year would make it ordinary.
- **Read next:** commercial paper in the next two quarterly reports, and the award definition in the proxy statement.

**Acquired customer lists: valued on attrition, charged evenly**
- **The report says:** straight-line "as this approximates the pattern of expected economic benefit" (Note 1, p. 51), but the lists were valued using "customer attrition rates" (Note 13, p. 74).
- **Test:** nothing to test on the pattern itself. Customer lists were charged ${N['cust_charge']} million in the year. Size: {f('cust_charge_pct')}% (an annual charge), on a carrying amount of {f('cust_net_pct')}% (a balance).
- **Reading:** possibly stretched a little: lists that lose customers most likely give more benefit early, so an even charge over about 20 years defers cost; this rests on general practice. Low, steady attrition would make the even charge fair.
- **Read next:** the attrition rates used, and the final GMS allocation, still "preliminary" (p. 74).

**3. Also noted**
- Depreciation "excluding amortization of intangible assets" is ${cf_da:,} million in the cash flow statement (p. 47) and ${dep_note3:,} million in Note 3 (p. 58); the ${N['da_gap']} million gap ({f('da_gap_pct')}%) is not explained.
- Customer receivables rose {f('cust_rec_growth')}% to ${cust_rec:,} million with the allowance "not material" (p. 48), while the risk factors say "we may face greater default risk" (p. 24).
- Inventory turnover of "4.4 times" (p. 32) holds on five quarter-end balances ({f('turn_5pt', 2)}); year-end balances give {f('turn_yearend', 2)}. No formula is stated.
- GMS is outside the controls assessment, and the company is "upgrading and migrating certain accounting and finance systems" (p. 77).

**4. Not in the documents:** Schedule II, the related-party item (Item 13) and the proxy statement; no warranty or restructuring reserve is mentioned.
"""

# quotation check: each quoted string must sit on the page cited next after it on the same line
marks = [(m.start(), int(m.group(1))) for m in re.finditer(r'\[p\. (\d+)\]', txt)]


def page_text(p):
    out = ''
    for i, (pos, pg) in enumerate(marks):
        if pg == p:
            end = marks[i + 1][0] if i + 1 < len(marks) else len(txt)
            out += txt[pos:end]
    return out


fails, n = [], 0
for line in reply.split('\n'):
    for m in re.finditer(r'"([^"]+)"', line):
        q = m.group(1)
        n += 1
        par = re.search(r'\(([^()]*p\. \d+[^()]*)\)', line[m.end():])
        pages = [int(x) for x in re.findall(r'p\. (\d+)', par.group(1))] if par else []
        bad = [p for p in pages if q not in page_text(p)]
        if not pages or bad:
            fails.append((q, pages, bad))
        else:
            print('OK', pages, q)
print('quotes checked', n, 'fails', fails)
print('words', len(re.findall(r'\S+', reply)))
if '--write' in sys.argv and not fails:
    open('runs/v2.16/text-3.md', 'w', encoding='utf-8').write(reply)
    print('saved')
