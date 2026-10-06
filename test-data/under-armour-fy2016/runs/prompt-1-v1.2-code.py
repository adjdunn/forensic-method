"""Working-capital measures for the attached statements.xlsx (prompt 1, v1.2).
Statement figures: statements.xlsx (USD millions, as originally reported).
Allowance and customer reserves: annual report notes (typed in below with page references)."""
import re
from datetime import date
import openpyxl

wb = openpyxl.load_workbook('statements.xlsx', data_only=True)

def sheet(name):
    ws = wb[name]
    rows = list(ws.iter_rows(values_only=True))
    hdr = rows[0]
    cols = {}
    for j, h in enumerate(hdr[1:-1], start=1):
        m = re.search(r'ended (\d{4})-(\d{2})-(\d{2})', h)
        cols[date(int(m.group(1)), int(m.group(2)), int(m.group(3)))] = j
    data = {}
    for r in rows[1:]:
        data.setdefault(r[0], r)  # first occurrence of a label
    return cols, data

def get(name, line):
    cols, data = sheet(name)
    return {d: data[line][j] for d, j in cols.items() if data[line][j] is not None}

rev_a = get('IS annual', 'Net revenues'); cogs_a = get('IS annual', 'Cost of goods sold')
ar_a = get('BS annual', 'Accounts receivable, net'); inv_a = get('BS annual', 'Inventories'); ap_a = get('BS annual', 'Accounts payable')
rev_q = get('IS quarterly', 'Net revenues'); cogs_q = get('IS quarterly', 'Cost of goods sold')
ar_q = get('BS quarterly', 'Accounts receivable, net'); inv_q = get('BS quarterly', 'Inventories'); ap_q = get('BS quarterly', 'Accounts payable')

def prior_year(d):
    return date(d.year - 1, d.month, d.day)

def days_year(d):
    return (d - prior_year(d)).days

def days_quarter(d):
    m = d.month - 3
    start = date(d.year - 1, 12, 31) if m == 0 else date(d.year, m, 30 if m in (6, 9) else 31)
    return (d - start).days

def g(series, d):
    p = prior_year(d)
    return series[d] / series[p] - 1 if d in series and p in series else None

def measures(d, rev, cogs, ar, inv, ap, ndays):
    out = {'days': ndays}
    out['DSO'] = ar[d] / rev[d] * ndays if d in ar else None
    out['DIO'] = inv[d] / cogs[d] * ndays if d in inv else None
    out['DPO'] = ap[d] / cogs[d] * ndays if d in ap else None
    gr, gc = g(rev, d), g(cogs, d)
    for k, s, base in (('AR gap', ar, gr), ('Inv gap', inv, gc), ('AP gap', ap, gc)):
        gs = g(s, d)
        out[k] = (gs - base) * 100 if gs is not None and base is not None else None
        out[k + ' (bal g)'] = gs * 100 if gs is not None else None
    out['rev g'] = gr * 100 if gr is not None else None
    out['cogs g'] = gc * 100 if gc is not None else None
    return out

def fmt(v):
    return '   n/a' if v is None else f'{v:6.1f}'

print('ANNUAL')
for d in sorted(ar_a):
    m = measures(d, rev_a, cogs_a, ar_a, inv_a, ap_a, days_year(d))
    print(d, {k: (round(v, 1) if v is not None else None) for k, v in m.items()})

print('QUARTERLY (latest four quarters, each beside the year-earlier quarter)')
latest4 = sorted(rev_q)[-4:]
for d in latest4:
    for dd in (prior_year(d), d):
        m = measures(dd, rev_q, cogs_q, ar_q, inv_q, ap_q, days_quarter(dd))
        print(dd, {k: (round(v, 1) if v is not None else None) for k, v in m.items()})

# Notes (USD millions). Allowance for doubtful accounts: FY2016 report p. 55 (2016, 2015); FY2015 report p. 50 (2015, 2014).
allow = {2014: 3.7, 2015: 5.9, 2016: 11.3}
# Reserves for customer returns, allowances, markdowns and discounts: FY2016 p. 57; FY2015 p. 52.
resv = {2014: 68.9, 2015: 94.5, 2016: 146.2}
print('ALLOWANCE AND RESERVES')
for y in (2014, 2015, 2016):
    d = date(y, 12, 31)
    net = ar_a[d]
    gross = net + allow[y]
    gross_all = net + allow[y] + resv[y]
    q4 = rev_q[d]
    print(y, 'allow % of (net+allow)', round(allow[y] / gross * 100, 2),
          '| allow % of (net+allow+reserves)', round(allow[y] / gross_all * 100, 2),
          '| reserves % of gross_all', round(resv[y] / gross_all * 100, 1),
          '| reserves % of annual revenue', round(resv[y] / rev_a[d] * 100, 2),
          '| reserves % of Q4 revenue', round(resv[y] / q4 * 100, 1),
          '| gross_all', round(gross_all, 1))
for y in (2015, 2016):
    print(y, 'reserve growth %', round((resv[y] / resv[y - 1] - 1) * 100, 1),
          'allowance growth %', round((allow[y] / allow[y - 1] - 1) * 100, 1))

# Supporting checks used in the flags
d16, d15 = date(2016, 12, 31), date(2015, 12, 31)
cf = get('CF annual', 'Accounts payable'); cfo = get('CF annual', 'Net cash provided by (used in) operating activities')
print('AP cash-flow line FY2016', cf[d16], 'CFO FY2016', cfo[d16], 'share %', round(cf[d16] / cfo[d16] * 100, 1))
print('AP FY2015 -> FY2016', ap_a[d15], ap_a[d16], 'growth %', round((ap_a[d16] / ap_a[d15] - 1) * 100, 1))
print('Sports Authority receivable 32.5 as % of FY2015 net AR', round(32.5 / ar_a[d15] * 100, 1))
# Revisions touching the lines used
ws = wb['Revisions']
hit = [r for r in ws.iter_rows(min_row=2, values_only=True)
       if r[1] and re.search(r'receivable|Inventor|Accounts payable|Net revenues|Cost of goods', r[1], re.I)
       and not re.search(r'Increase|cash flow', str(r[0]) , re.I)]
print('Revisions rows touching receivables, inventories, payables, revenue or cost of goods sold:', len(hit))
for r in ws.iter_rows(min_row=2, values_only=True):
    if r[1] and re.search(r'receivable|Inventor|payable|revenue|Cost of goods', r[1], re.I): print('  ', r[:5])
