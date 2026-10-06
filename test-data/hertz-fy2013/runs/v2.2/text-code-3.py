# Turn 1 (prompt 3: read the footnotes). Calculations and quotation checks.
import re, os
import openpyxl

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FY13 = os.path.join(BASE, 'annual-report-FY2013-12-31-key-sections.txt')
XLSX = os.path.join(BASE, 'statements.xlsx')
REPLY = os.path.join(BASE, 'runs', 'v2.2', 'text-3.md')

t13 = open(FY13, encoding='utf-8').read()

# ---------- workbook figures ----------
wb = openpyxl.load_workbook(XLSX, data_only=True)


def sheet_rows(name):
    rows = list(wb[name].iter_rows(values_only=True))
    return rows[0], rows[1:]


def val(sheet, line, col_contains):
    hdr, rows = sheet_rows(sheet)
    ci = [i for i, h in enumerate(hdr) if h and col_contains in str(h)][0]
    for r in rows:
        if r[0] == line:
            return r[ci]
    raise KeyError(line)


def revised(statement, line, period_contains):
    hdr, rows = sheet_rows('Revisions')
    for r in rows:
        if r[0] == statement and r[1] == line and period_contains in str(r[3]):
            return r[4], r[6]
    raise KeyError((statement, line, period_contains))


pti13 = val('IS annual', 'Income before income taxes', '2013-12-31')
pti12_orig, pti12_rev = revised('Income statement', 'Income before income taxes', '12 months ended 2012-12-31')
pti11_orig, pti11_rev = revised('Income statement', 'Income before income taxes', '12 months ended 2011-12-31')
eps11_orig, eps11_rev = revised('Income statement', 'Diluted (in dollars per share)', '12 months ended 2011-12-31')
rev13 = val('IS annual', 'Total revenues', '2013-12-31')
rev12_orig, rev12_rev = revised('Income statement', 'Total revenues', '12 months ended 2012-12-31')
plpd13 = val('BS annual', 'Public liability and property damage', '2013-12-31')
plpd12 = val('BS annual', 'Public liability and property damage', '2012-12-31')
tax13 = -val('IS annual', 'Provision for taxes on income', '2013-12-31')
print('Workbook: pre-tax income FY2013', pti13, '| FY2012 orig/revised', round(pti12_orig, 1), pti12_rev,
      '| FY2011 orig/revised', round(pti11_orig, 1), pti11_rev)

# ---------- figures read from the FY2013 report (page in comment) ----------
us_rate_cut = {2013: 44.2, 2012: 139.4, 2011: 26.7}          # Note 8, p.126
us_disposal = {2013: -48.2, 2012: 100.6, 2011: 114.9}         # Note 8, p.126 (gain +, loss -)
intl_disposal = {2013: -15.2, 2012: -17.3, 2011: -16.0}
equip_disposal = {2013: 26.2, 2012: 13.5, 2011: 13.3}
adj_on_disposal = {2013: 37.2, 2012: -96.8, 2011: -112.2}     # table, p.126 (expense +)
us_dep = {2013: 1269.3, 2012: 940.6}                          # Note 11, p.131
us_cars_owned = {2013: 468500, 2012: 358000}                  # Item 7, p.49
us_cars_leased = {2013: 21500, 2012: 1100}

print('\n--- A. depreciation and residual values ---')
for y in (2013, 2012, 2011):
    s = -(us_disposal[y] + intl_disposal[y] + equip_disposal[y])
    print(y, 'disposal components sum to', round(s, 1), 'vs table', adj_on_disposal[y])
print('US rate cut 2013 as % of FY2013 pre-tax income:', round(100 * us_rate_cut[2013] / pti13, 1))
print('US rate cut 2012 as % of FY2012 pre-tax income (revised):', round(100 * us_rate_cut[2012] / pti12_rev, 1),
      '| (as first reported):', round(100 * us_rate_cut[2012] / pti12_orig, 1))
print('US rate cuts, three years:', round(sum(us_rate_cut.values()), 1))
print('US disposal swing 2012->2013:', round(us_disposal[2013] - us_disposal[2012], 1))
for y in (2013, 2012):
    a = us_dep[y] * 1e6 / us_cars_owned[y] / 12
    b = us_dep[y] * 1e6 / (us_cars_owned[y] + us_cars_leased[y]) / 12
    print(y, 'US depreciation and lease charges per car per month: owned only', round(a, 2), '| owned+leased', round(b, 2))
a13 = us_dep[2013] / us_cars_owned[2013]
a12 = us_dep[2012] / us_cars_owned[2012]
b13 = us_dep[2013] / (us_cars_owned[2013] + us_cars_leased[2013])
b12 = us_dep[2012] / (us_cars_owned[2012] + us_cars_leased[2012])
print('change owned only %:', round(100 * (a13 / a12 - 1), 1), '| owned+leased %:', round(100 * (b13 / b12 - 1), 1))

print('\n--- B. out-of-period errors ---')
vendor = {2011: 12.9, 2012: 2.4}
brazil = {2010: 4.4, 2011: 6.2, 2012: 3.6}
other = {2010: 2.4, 2012: 3.2, 2011: -0.4}
by_year = {y: round(vendor.get(y, 0) + brazil.get(y, 0) + other.get(y, 0), 1) for y in (2010, 2011, 2012)}
print('by year', by_year, 'total', round(sum(by_year.values()), 1), '(note: 34.7)')
print('total 46.3 less prior years 34.7 =', round(46.3 - 34.7, 1), '(nine months 2013 adjustment in note: 11.6)')
q4_pti = 62.3   # Note 18, p.149
print('46.3 as % of Q4 2013 pre-tax income 62.3:', round(100 * 46.3 / q4_pti, 1),
      '| Q4 pre-tax if all 46.3 had been booked in Q4:', round(q4_pti - 46.3, 1),
      '| cross-check: (663.1 - 34.7) - 612.4 nine months as first reported =', round((pti13 - 34.7) - 612.4, 1))
print('check Q4: FY', pti13, '- nine months revised 600.8 =', round(pti13 - 600.8, 1))
print('2011 pre-tax cut %:', round(100 * (pti11_orig - pti11_rev) / pti11_orig, 1),
      '| 2012 pre-tax cut %:', round(100 * (pti12_orig - pti12_rev) / pti12_orig, 1))
print('2011 diluted EPS', eps11_orig, '->', eps11_rev, 'change %:', round(100 * (eps11_rev / eps11_orig - 1), 1))
print('net of tax: 4.5+12.0+4.5 =', 4.5 + 12.0 + 4.5)
print('2012 vendor incentives footnotes (c)-(b): 25.9-23.6 =', round(25.9 - 23.6, 1),
      'vs text 2.4; 2011 (f)-(e): 22.4-9.5 =', round(22.4 - 9.5, 1), 'vs text 12.9')

print('\n--- C. adjusted pre-tax income ---')
seg = {2013: 1581.7, 2012: 1239.5, 2011: 995.1}            # Note 11, p.134
corp = {2013: -428.5, 2012: -347.2, 2011: -333.3}
gaap = {2013: pti13, 2012: pti12_rev, 2011: pti11_rev}
restr = {2013: 77.0, 2012: 38.0, 2011: 56.4}
restr_rel = {2013: 21.8, 2012: 11.1, 2011: 9.8}
for y in (2013, 2012, 2011):
    adj = seg[y] + corp[y]
    print(y, 'adjusted pre-tax (segments less corporate):', round(adj, 1), '| GAAP:', gaap[y],
          '| excluded:', round(adj - gaap[y], 1), '| excluded as % of GAAP:', round(100 * (adj - gaap[y]) / gaap[y], 1),
          '| restructuring + related:', round(restr[y] + restr_rel[y], 1))
print('restructuring charges three years:', round(sum(restr.values()), 1), '| since 2007 per note: 645.4')

print('\n--- also noted ---')
print('Concession-fee judgment 40.0 as % of FY2013 pre-tax income:', round(100 * 40.0 / pti13, 1))
print('Valuation allowance change (Schedule II): 279.4-226.4 =', round(279.4 - 226.4, 1),
      '| charged to expense 37.9 | 5.7 pts x pre-tax =', round(0.057 * pti13, 1))
print('Effective tax rate FY2013:', round(100 * tax13 / pti13, 1))
print('PLPD reserve:', plpd12, '->', plpd13, 'change', round(plpd13 - plpd12, 1), round(100 * (plpd13 / plpd12 - 1), 1), '%')
print('PLPD / revenue: 2013', round(100 * plpd13 / rev13, 2), '| 2012 revenue (revised)', round(100 * plpd12 / rev12_rev, 2),
      '| 2012 pro forma revenue 10,197.4', round(100 * plpd12 / 10197.4, 2))
print('Revenue growth whole company %:', round(100 * (rev13 / rev12_rev - 1), 1))
print('Doubtful accounts: cash-flow provision 45.9 vs Schedule II charge 41.9, gap', round(45.9 - 41.9, 1),
      '| impairment 44.0 (segment note) vs 40.0 (cash flow), gap', round(44.0 - 40.0, 1))
print('Allowance roll: 29.3+41.9-0.1-40.3 =', round(29.3 + 41.9 - 0.1 - 40.3, 1))
print('Fleet debt availability 23.9 of remaining capacity 1041.1 =', round(100 * 23.9 / 1041.1, 1), '%')
print('Share repurchase: 3.877*22.54 + 23.2*20.14 =', round(3.877 * 22.54 + 23.2 * 20.14, 1))
print('Advertising 213.1 vs 183.9: change', round(213.1 - 183.9, 1), round(100 * (213.1 / 183.9 - 1), 1), '%')


# ---------- quotation check ----------
def page_of(text, pos):
    m = re.findall(r'\[p\. (\d+)\]', text[:pos])
    return int(m[-1]) if m else None


def check_reply(path, text, label='FY2013'):
    if not os.path.exists(path):
        print('\n(reply not written yet)')
        return
    reply = open(path, encoding='utf-8').read()
    ok = bad = 0
    for line in reply.split('\n'):
        quotes = re.findall(r'"([^"]+)"', line)
        pages = [int(p) for p in re.findall(r'p\.\s?(\d+)', line)]
        for rng in re.findall(r'pp\.\s?([\d, and]+)', line):
            pages += [int(p) for p in re.findall(r'\d+', rng)]
        for q in quotes:
            hits = [m.start() for m in re.finditer(re.escape(q), text)]
            if not hits:
                print('NOT FOUND:', q)
                bad += 1
                continue
            hit_pages = sorted({page_of(text, h) for h in hits})
            if any(p in pages for p in hit_pages):
                ok += 1
            else:
                print('PAGE MISMATCH:', q, '| found on', hit_pages, '| line cites', pages)
                bad += 1
    print('\nQuotation check (%s): %d ok, %d failed' % (label, ok, bad))
    print('Word count:', len(re.findall(r'\S+', reply)))


check_reply(REPLY, t13)
