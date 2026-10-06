# Scan the numbers: Home Depot, fiscal years ended Jan-2022 to Feb-2026, Q4 ended 2026-02-01 vs 2025-02-02
import openpyxl, re, datetime as dt, os, sys
D = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
wb = openpyxl.load_workbook(os.path.join(D, 'statements.xlsx'))

def sheet(name):
    ws = wb[name]
    heads = [c.value for c in ws[1]]
    out, fills = {}, {}
    for row in ws.iter_rows(min_row=2):
        line = row[0].value
        if line is None: continue
        for h, c in zip(heads[1:-1], row[1:-1]):
            end = re.search(r'ended (\d{4}-\d{2}-\d{2})', h).group(1)
            key = (h.split(' ')[0], end)
            out.setdefault(line, {})[key] = c.value
            fills.setdefault(line, {})[key] = c.fill.fgColor.rgb if c.fill.fill_type else None
    return out, fills, heads

ISa, _, _ = sheet('IS annual'); BSa, _, _ = sheet('BS annual'); CFa, _, _ = sheet('CF annual')
ISq, ISqf, ISqh = sheet('IS quarterly'); BSq, _, _ = sheet('BS quarterly'); CFq, CFqf, CFqh = sheet('CF quarterly')
print('IS quarterly headings marked mixed:', [h for h in ISqh if h and 'mixed' in h])
print('CF quarterly headings marked mixed:', [h for h in CFqh if h and 'mixed' in h])
ORANGE = '00F8D7B0'
for nm, F in (('CF', CFqf), ('IS', ISqf)):
    for line, dd in F.items():
        for k, f in dd.items():
            if f == ORANGE: print('orange cell (left out of measures):', nm, line, k)

FY = ['2022-01-30', '2023-01-29', '2024-01-28', '2025-02-02', '2026-02-01']
LAB = {'2022-01-30': 'FY2021', '2023-01-29': 'FY2022', '2024-01-28': 'FY2023', '2025-02-02': 'FY2024', '2026-02-01': 'FY2025'}
def d(s): return dt.date.fromisoformat(s)
days = {'2022-01-30': 364}
for a_, b_ in zip(FY, FY[1:]): days[b_] = (d(b_) - d(a_)).days
print('days', days)

def a(S, line, y): return S[line].get(('FY', y))
rev = {y: a(ISa, 'Net sales', y) for y in FY}
cos = {y: a(ISa, 'Cost of sales', y) for y in FY}
gp = {y: a(ISa, 'Gross profit', y) for y in FY}
sga = {y: a(ISa, 'Selling, general and administrative', y) for y in FY}
oi = {y: a(ISa, 'Operating income', y) for y in FY}
ni = {y: a(ISa, 'Net earnings', y) for y in FY}
pti = {y: a(ISa, 'Earnings before provision for income taxes', y) for y in FY}
cfo = {y: a(CFa, 'Net cash provided by operating activities', y) for y in FY}
capex = {y: -a(CFa, 'Capital expenditures', y) for y in FY}
acq = {y: -a(CFa, 'Payments for businesses acquired, net', y) for y in FY}
BY = FY[1:]
rec = {y: a(BSa, 'Receivables, net', y) for y in BY}
inv = {y: a(BSa, 'Merchandise inventories', y) for y in BY}
ap = {y: a(BSa, 'Accounts payable', y) for y in BY}
ta = {y: a(BSa, 'Total assets', y) for y in BY}
ca = {y: a(BSa, 'Total current assets', y) for y in BY}
ppe = {y: a(BSa, 'Net property and equipment', y) for y in BY}
cl = {y: a(BSa, 'Total current liabilities', y) for y in BY}
ltd = {y: a(BSa, 'Long-term debt, excluding current installments', y) for y in BY}

# ---- property note (annual reports) ----
def load(fn): return open(os.path.join(D, fn), encoding='utf-8', errors='replace').read()
ar25, ar26 = load('annual-report-FY2025-02-02-key-sections.txt'), load('annual-report-FY2026-02-01-key-sections.txt')
rl25, rl26 = load('earnings-release-Q4-FY2025-02-02.txt'), load('earnings-release-Q4-FY2026-02-01.txt')
def page_of(text, sub):
    i = text.index(sub)
    return re.findall(r'\[p\. (\d+)\]', text[:i])[-1]
def nums(text, label):
    m = re.search(r'^' + re.escape(label) + r' \| (.*)$', text, re.M)
    return [int(x.replace('$', '').replace(',', '')) for x in m.group(1).split(' | ')], page_of(text, m.group(0))
dep = {}
v, p = nums(ar25, 'Depreciation and finance lease amortization expense'); print('dep note AR25 p', p, v)
dep['2025-02-02'], dep['2024-01-28'], dep['2023-01-29'] = v
v, p = nums(ar26, 'Depreciation and finance lease amortization expense'); print('dep note AR26 p', p, v)
assert v[1] == dep['2025-02-02'] and v[2] == dep['2024-01-28']; dep['2026-02-01'] = v[0]
gross = {}
for text, ys in ((ar25, ('2025-02-02', '2024-01-28')), (ar26, ('2026-02-01', '2025-02-02'))):
    cost, p = nums(text, 'Property and equipment, at cost'); land, _ = nums(text, 'Land'); cip, _ = nums(text, 'Construction in progress')
    for i, y in enumerate(ys):
        g = cost[i] - land[i] - cip[i]
        assert gross.get(y, g) == g; gross[y] = g
    print('property note p', p, cost, land, cip)
print('gross depreciable', gross, 'dep', dep)
for text, qt in ((ar25, 'was not material to our consolidated financial statements at the end of fiscal 2024 or fiscal 2023'),
                 (ar26, 'was not material to our consolidated financial statements at the end of fiscal 2025 or fiscal 2024')):
    assert qt in text; print('allowance wording found on p', page_of(text, qt))

# ---- annual measures ----
M = {}
for i, y in enumerate(FY):
    r = {}
    py = FY[i - 1] if i else None
    r['GM'] = gp[y] / rev[y]; r['OM'] = oi[y] / rev[y]
    r['FCF'] = cfo[y] - capex[y]; r['FCF/NI'] = r['FCF'] / ni[y]; r['NI-FCF'] = ni[y] - r['FCF']
    if y in rec:
        r['DSO'] = rec[y] / rev[y] * days[y]; r['DIO'] = inv[y] / cos[y] * days[y]; r['DPO'] = ap[y] / cos[y] * days[y]
    if py in rec:
        r['gapRec'] = rec[y] / rec[py] - rev[y] / rev[py]
        r['gapInv'] = inv[y] / inv[py] - cos[y] / cos[py]
        r['gapAP'] = ap[y] / ap[py] - cos[y] / cos[py]
        r['accr'] = (ni[y] - cfo[y]) / ((ta[y] + ta[py]) / 2)
        if y in gross and py in gross: r['deprate'] = dep[y] / ((gross[y] + gross[py]) / 2)
        DSRI = (rec[y] / rev[y]) / (rec[py] / rev[py]); GMI = (gp[py] / rev[py]) / (gp[y] / rev[y])
        aq = lambda z: 1 - (ca[z] + ppe[z]) / ta[z]
        AQI = aq(y) / aq(py); SGI = rev[y] / rev[py]
        if py in dep:
            DEPI = (dep[py] / (dep[py] + ppe[py])) / (dep[y] / (dep[y] + ppe[y]))
        else:
            DEPI = 1.0
        SGAI = (sga[y] / rev[y]) / (sga[py] / rev[py]); TATA = (ni[y] - cfo[y]) / ta[y]
        LVGI = ((ltd[y] + cl[y]) / ta[y]) / ((ltd[py] + cl[py]) / ta[py])
        r['M'] = -4.84 + .920 * DSRI + .528 * GMI + .404 * AQI + .892 * SGI + .115 * DEPI - .172 * SGAI + 4.679 * TATA - .327 * LVGI
        r['Mparts'] = dict(DSRI=round(DSRI, 3), GMI=round(GMI, 3), AQI=round(AQI, 3), SGI=round(SGI, 3), DEPI=round(DEPI, 3), SGAI=round(SGAI, 3), TATA=round(TATA, 4), LVGI=round(LVGI, 3))
    M[y] = r
    print(LAB[y], {k: (round(v, 4) if isinstance(v, float) else v) for k, v in r.items()})
print('acquisition outflows', acq)

# ---- quarters: Q4 ended 2026-02-01 vs 2025-02-02 (and 2024-01-28 for growth and persistence) ----
Q = ['2024-01-28', '2025-02-02', '2026-02-01']; QP = {'2024-01-28': '2023-10-29', '2025-02-02': '2024-10-27', '2026-02-01': '2025-11-02'}
qdays = {y: (d(y) - d(QP[y])).days for y in Q}; print('quarter days', qdays)
def q(S, line, y, per='Q4'): return S[line].get((per, y))
QM = {}
for i, y in enumerate(Q):
    r = {}; R, C = q(ISq, 'Net sales', y), q(ISq, 'Cost of sales', y)
    r['GM'] = q(ISq, 'Gross profit', y) / R; r['OM'] = q(ISq, 'Operating income', y) / R
    r['DSO'] = q(BSq, 'Receivables, net', y) / R * qdays[y]; r['DIO'] = q(BSq, 'Merchandise inventories', y) / C * qdays[y]; r['DPO'] = q(BSq, 'Accounts payable', y) / C * qdays[y]
    n, o, cx = q(CFq, 'Net earnings', y), q(CFq, 'Net cash provided by operating activities', y), -q(CFq, 'Capital expenditures', y)
    r['FCF'] = o - cx; r['FCF/NI'] = (o - cx) / n; r['NI-FCF'] = n - (o - cx)
    ta0 = q(BSq, 'Total assets', QP[y], 'Q3')
    if ta0: r['accr'] = (n - o) / ((ta0 + q(BSq, 'Total assets', y)) / 2)
    if i:
        py = Q[i - 1]
        r['gapRec'] = q(BSq, 'Receivables, net', y) / q(BSq, 'Receivables, net', py) - R / q(ISq, 'Net sales', py)
        r['gapInv'] = q(BSq, 'Merchandise inventories', y) / q(BSq, 'Merchandise inventories', py) - C / q(ISq, 'Cost of sales', py)
        r['gapAP'] = q(BSq, 'Accounts payable', y) / q(BSq, 'Accounts payable', py) - C / q(ISq, 'Cost of sales', py)
    QM[y] = r
    print('Q4', y, {k: (round(v, 4) if isinstance(v, float) else v) for k, v in r.items()})
# check the derived Q4 income statement against the releases
for text, y, py in ((rl26, '2026-02-01', '2025-02-02'), (rl25, '2025-02-02', '2024-01-28')):
    for lab in ('Net sales', 'Cost of sales', 'Operating income', 'Net earnings'):
        m = re.search(r'^' + lab + r' \| \$? ?([\d,]+) \| \$? ?([\d,]+)', text, re.M)
        got = [int(x.replace(',', '')) for x in m.groups()] if m else None
        want = [q(ISq, lab, y), q(ISq, lab, py)]
        print('release check', y, lab, got, want, got == want)

# ---- industry ----
ws = wb['Industry']; ind = {r[0].value: r[1].value for r in ws.iter_rows() if r[1].value is not None}
L = FY[-1]
co = {'Acc Rec/ Sales': 100 * rec[L] / rev[L], 'Inventory/Sales': 100 * inv[L] / rev[L], 'Acc Pay/ Sales': 100 * ap[L] / rev[L],
      'Gross Margin': 100 * M[L]['GM'], 'Pre-tax Unadjusted Operating Margin': 100 * M[L]['OM'], 'Cap Ex/Deprecn': capex[L] / dep[L]}
for k in ind: print('industry', k, ind[k], 'company', round(co[k], 2), 'diff', round(co[k] - ind[k], 2))
print('shares of sales by year (rec, inv, ap, capex/dep)', {LAB[y]: (round(100 * rec[y] / rev[y], 2), round(100 * inv[y] / rev[y], 2), round(100 * ap[y] / rev[y], 2), round(capex[y] / dep[y], 2)) for y in BY})
print('industry payables gap in money', (ind['Acc Pay/ Sales'] / 100) * rev[L] - ap[L])

# ---- flag sizes (share of latest-year pre-tax income) ----
P = FY[-2]; PT = pti[L]; print('pre-tax income', PT)
def show(name, amt, how): print(f'FLAG {name}: {amt:.0f} = {100 * amt / PT:.1f}% of pre-tax | {how}')
show('cash vs earnings', M[L]['NI-FCF'], f'NI {ni[L]} - FCF ({cfo[L]} - {capex[L]})')
show('operating margin fall', (M[P]['OM'] - M[L]['OM']) * rev[L], f"({M[P]['OM']:.5f} - {M[L]['OM']:.5f}) x {rev[L]}")
show('gross margin fall', (M[P]['GM'] - M[L]['GM']) * rev[L], f"({M[P]['GM']:.5f} - {M[L]['GM']:.5f}) x {rev[L]}")
show('inventory', inv[L] - M[P]['DIO'] / days[L] * cos[L], f"{inv[L]} - {M[P]['DIO']:.3f}/{days[L]} x {cos[L]}")
show('payables', M[P]['DPO'] / days[L] * cos[L] - ap[L], f"{M[P]['DPO']:.3f}/{days[L]} x {cos[L]} - {ap[L]}")
show('receivables', rec[L] - M[P]['DSO'] / days[L] * rev[L], f"{rec[L]} - {M[P]['DSO']:.3f}/{days[L]} x {rev[L]}")
avg = (gross[L] + gross[P]) / 2
show('depreciation rate', (M[P]['deprate'] - M[L]['deprate']) * avg, f"({M[P]['deprate']:.5f} - {M[L]['deprate']:.5f}) x {avg}")
for k in ('DSO', 'DIO', 'DPO', 'GM', 'OM', 'FCF/NI', 'accr', 'deprate', 'M'):
    print('series', k, [(LAB[y], round(M[y][k], 4)) for y in FY if k in M[y]], '| Q4', [(y, round(QM[y][k], 4)) for y in Q if k in QM[y]])

# ---- revisions ----
ws = wb['Revisions']
for r in ws.iter_rows(min_row=2, values_only=True):
    if r[0]: print('rev', r[0], '|', r[1], '|', r[3], '|', r[4], '->', r[6], '|', r[8])

# ---- extras quoted in the flags ----
for y in FY: print('SG&A % sales', LAB[y], round(100 * sga[y] / rev[y], 2), '| D&A opex % sales', round(100 * a(ISa, 'Depreciation and amortization', y) / rev[y], 2))
print('growth FY2025: rec', round(100 * (rec[L] / rec[P] - 1), 1), 'rev', round(100 * (rev[L] / rev[P] - 1), 1), 'inv', round(100 * (inv[L] / inv[P] - 1), 1), 'cos', round(100 * (cos[L] / cos[P] - 1), 1), 'ap', round(100 * (ap[L] / ap[P] - 1), 1))
v, pg = nums(ar26, 'Customer receivables'); print('customer receivables AR26 p', pg, v)
v, pg = nums(ar25, 'Customer receivables'); print('customer receivables AR25 p', pg, v)
for k in ('Changes in merchandise inventories', 'Changes in accounts payable and accrued expenses', 'Changes in income taxes payable'):
    print(k, [a(CFa, k, y) for y in FY])
print('FCF', {LAB[y]: M[y]['FCF'] for y in FY}, 'NI', {LAB[y]: ni[y] for y in FY})
print('op margin fall pts', round(100 * (M[P]['OM'] - M[L]['OM']), 2), 'gross', round(100 * (M[P]['GM'] - M[L]['GM']), 2))

# ---- table rows as shown in the reply ----
def cell(v, f): return '' if v is None else f(v)
rows = [('Days sales outstanding', 'DSO', lambda v: f'{v:.1f}'), ('Days inventory', 'DIO', lambda v: f'{v:.1f}'), ('Days payable', 'DPO', lambda v: f'{v:.1f}'),
        ('Receivables growth less revenue growth, pts', 'gapRec', lambda v: f'{100*v:+.1f}'), ('Inventory growth less cost-of-sales growth, pts', 'gapInv', lambda v: f'{100*v:+.1f}'),
        ('Payables growth less cost-of-sales growth, pts', 'gapAP', lambda v: f'{100*v:+.1f}'), ('Gross margin, %', 'GM', lambda v: f'{100*v:.1f}'), ('Operating margin, %', 'OM', lambda v: f'{100*v:.1f}'),
        ('Accruals, % of average assets', 'accr', lambda v: f'{100*v:.1f}'), ('Free cash flow / net income', 'FCF/NI', lambda v: f'{v:.2f}'),
        ('Depreciation rate, %', 'deprate', lambda v: f'{100*v:.2f}'), ('M-score', 'M', lambda v: f'{v:.2f}')]
for name, k, f in rows:
    print('| ' + name + ' | ' + ' | '.join(cell(M[y].get(k), f) for y in FY) + ' | ' + ' | '.join(cell(QM[y].get(k), f) for y in Q[1:]) + ' |')
for name, B in (('Receivables, % of sales', rec), ('Inventory, % of sales', inv), ('Payables, % of sales', ap)):
    print('| ' + name + ' | ' + ' | '.join(f'{100*B[y]/rev[y]:.1f}' for y in BY))
print('| Capex / depreciation | ' + ' | '.join(f'{capex[y]/dep[y]:.2f}' for y in BY))
