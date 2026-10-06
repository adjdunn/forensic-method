# Turn 2 (prompt 4: compare the footnotes). Alignment of the two reports, calculations, quotation checks.
import re, os, sys, difflib
import openpyxl

BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FY13 = os.path.join(BASE, 'annual-report-FY2013-12-31-key-sections.txt')
FY12 = os.path.join(BASE, 'annual-report-FY2012-12-31-key-sections.txt')
XLSX = os.path.join(BASE, 'statements.xlsx')
REPLY = os.path.join(BASE, 'runs', 'v2.2', 'text-4.md')

t13 = open(FY13, encoding='utf-8').read()
t12 = open(FY12, encoding='utf-8').read()


def page_of(text, pos):
    m = re.findall(r'\[p\. (\d+)\]', text[:pos])
    return int(m[-1]) if m else None


# ---------------------------------------------------------------- alignment
def sections(text):
    out = {}
    marks = [(m.start(), m.group(1)) for m in re.finditer(r'=== Item (\w+) ===', text)]
    for i, (pos, name) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(text)
        out[name] = (pos, text[pos:end])
    return out


def sentences(block, base, full):
    # returns list of (normalised sentence, raw sentence, page)
    res = []
    for m in re.finditer(r'[^\n]+', block):
        line = m.group(0)
        if re.match(r'\[p\. \d+\]', line) or line.startswith('ITEM ') or 'NOTES TO CONSOLIDATED' in line \
                or line.startswith('HERTZ GLOBAL HOLDINGS') or line.startswith('Operations (Continued)'):
            continue
        for s in re.split(r'(?<=[.;:])\s+(?=[A-Z“"(])', line):
            s = s.strip()
            if len(s) < 25:
                continue
            norm = s.replace('‑', '-').replace('’', "'")
            norm = re.sub(r'\$?[\d,]+\.?\d*%?', '#', norm)            # numbers
            norm = re.sub(r'\b(20\d\d|January|February|March|April|May|June|July|August|September|October|November|December)\b', '#', norm)
            norm = re.sub(r'licensee', 'franchisee', norm, flags=re.I)
            norm = re.sub(r'audited annual consolidated', 'consolidated', norm)
            norm = re.sub(r'\s+', ' ', norm).lower()
            res.append((norm, s, page_of(full, base + m.start())))
    return res


def align(name12, name13, show=True, cutoff=0.6):
    s12 = sentences(*[(sec12[name12][1]), sec12[name12][0], t12])
    s13 = sentences(*[(sec13[name13][1]), sec13[name13][0], t13])
    n12 = [x[0] for x in s12]
    n13 = [x[0] for x in s13]
    set12, set13 = set(n12), set(n13)
    dropped = [x for x in s12 if x[0] not in set13]
    added = [x for x in s13 if x[0] not in set12]
    if show:
        print('\n################ Item', name12, ': %d sentences FY2012, %d FY2013; %d not in FY2013, %d new in FY2013'
              % (len(s12), len(s13), len(dropped), len(added)))
        add_norm = [a[0] for a in added]
        used = set()
        for d in dropped:
            best = difflib.get_close_matches(d[0], add_norm, n=1, cutoff=cutoff)
            if best:
                j = add_norm.index(best[0])
                used.add(j)
                print('\n~ REWORDED  FY2012 p.%s: %s\n            FY2013 p.%s: %s' % (d[2], d[1][:900], added[j][2], added[j][1][:900]))
            else:
                print('\n- DROPPED   FY2012 p.%s: %s' % (d[2], d[1][:700]))
        for j, a in enumerate(added):
            if j not in used:
                print('\n+ ADDED     FY2013 p.%s: %s' % (a[2], a[1][:700]))
    return dropped, added


sec12, sec13 = sections(t12), sections(t13)

if len(sys.argv) > 1 and sys.argv[1] == 'align':
    for item in sys.argv[2:]:
        align(item, item)
    sys.exit()

# ---------------------------------------------------------------- workbook
wb = openpyxl.load_workbook(XLSX, data_only=True)


def rows(name):
    r = list(wb[name].iter_rows(values_only=True))
    return r[0], r[1:]


def val(sheet, line, col_contains, nth=0):
    hdr, rr = rows(sheet)
    ci = [i for i, h in enumerate(hdr) if h and col_contains in str(h)][0]
    hits = [r for r in rr if r[0] == line]
    return hits[nth][ci]


def revised(statement, line, period_contains, elem=None):
    hdr, rr = rows('Revisions')
    for r in rr:
        if r[0] == statement and r[1] == line and period_contains in str(r[3]) and (elem is None or elem in str(r[2])):
            return r[4], r[6]
    raise KeyError((statement, line, period_contains))


cars13 = val('BS annual', 'Cars', '2013-12-31')
cars12_o, cars12_r = revised('Balance sheet', 'Cars', '2012-12-31')
cars11 = val('BS annual', 'Cars', '2011-12-31')
cars10 = val('BS annual', 'Cars', '2010-12-31')
acc13 = -val('BS annual', 'Less accumulated depreciation', '2013-12-31', 0)
acc12_o, acc12_r = revised('Balance sheet', 'Less accumulated depreciation', '2012-12-31', 'PropertySubjectToOrAvailableForOperatingLeaseAccumulatedDepreciation')
acc12_o, acc12_r = -acc12_o, -acc12_r
acc11 = -val('BS annual', 'Less accumulated depreciation', '2011-12-31', 0)
acc10 = -val('BS annual', 'Less accumulated depreciation', '2010-12-31', 0)
eq13 = val('BS annual', 'Other equipment', '2013-12-31')
eq12 = val('BS annual', 'Other equipment', '2012-12-31')
eq11 = val('BS annual', 'Other equipment', '2011-12-31')
eqacc13 = -val('BS annual', 'Less accumulated depreciation', '2013-12-31', 1)
eqacc12 = -val('BS annual', 'Less accumulated depreciation', '2012-12-31', 1)
eqacc11 = -val('BS annual', 'Less accumulated depreciation', '2011-12-31', 1)
rec13 = val('BS annual', 'Receivables, less allowance for doubtful accounts of $30.8 and $29.3', '2013-12-31')
rec12_o, rec12_r = revised('Balance sheet', 'Receivables, less allowance for doubtful accounts of $30.8 and $29.3', '2012-12-31')
rev13 = val('IS annual', 'Total revenues', '2013-12-31')
rev12_o, rev12_r = revised('Income statement', 'Total revenues', '12 months ended 2012-12-31')
rev11_o, rev11_r = revised('Income statement', 'Total revenues', '12 months ended 2011-12-31')
pti13 = val('IS annual', 'Income before income taxes', '2013-12-31')
pti12_o, pti12_r = revised('Income statement', 'Income before income taxes', '12 months ended 2012-12-31')
plpd = {y: val('BS annual', 'Public liability and property damage', '%d-12-31' % y) for y in (2010, 2011, 2012, 2013)}
ppe13 = val('BS annual', 'Total property and equipment, at cost', '2013-12-31')
ppe12 = val('BS annual', 'Total property and equipment, at cost', '2012-12-31')
ppe11 = val('BS annual', 'Total property and equipment, at cost', '2011-12-31')
dppe13 = val('CF annual', 'Depreciation of property and equipment', '2013-12-31')
dppe12 = val('CF annual', 'Depreciation of property and equipment', '2012-12-31')

print('=== A. Cars: stated holding period against the numbers ===')
print('Stated range: FY2012 note "4 to 28 months" -> FY2013 note "4 to 36 months": max up', 36 - 28, 'months,', round(100 * (36 / 28 - 1), 1), '%')
print('Stated U.S. average: eighteen months both years; international fourteen -> thirteen')
for y, c, a in ((2010, cars10, acc10), (2011, cars11, acc11), (2012, cars12_r, acc12_r), (2013, cars13, acc13)):
    print(y, 'cars at cost', round(c, 1), 'accumulated depreciation', round(a, 1), '=', round(100 * a / c, 1), '% of cost')
print('   2012 as first reported:', round(100 * acc12_o / cars12_o, 1), '%')
# company-wide depreciation on cars, per month, as % of average cost (rough: includes Donlen and international cars)
dep_ree = {2013: 2407.8, 2012: 2145.9}                 # FY2013 Note 8 p.126 (2012 as revised)
equip_dep = {2013: 298.8 + 26.2, 2012: 272.1 + 13.5}   # equipment segment depreciation with disposal gains added back
car_dep = {y: dep_ree[y] - equip_dep[y] for y in dep_ree}
avg_cost = {2013: (cars13 + cars12_r) / 2, 2012: (cars12_r + cars11) / 2}
for y in (2012, 2013):
    r = car_dep[y] / avg_cost[y] / 12
    print(y, 'car depreciation before disposal results', round(car_dep[y], 1), '/ average cars at cost', round(avg_cost[y], 1),
          '=', round(100 * r, 2), '% of cost per month')
r13 = car_dep[2013] / avg_cost[2013] / 12
r12 = car_dep[2012] / avg_cost[2012] / 12
print('months of depreciation carried at year end (accumulated / monthly charge): 2012',
      round(acc12_r / (car_dep[2012] / 12), 1), '| 2013', round(acc13 / (car_dep[2013] / 12), 1))
# U.S. fleet turnover (rough): average company-operated cars / non-program cars sold
us_fleet = {2013: 468500, 2012: 358000}        # FY2013 Item 7 p.49
us_sold = {2013: 197700, 2012: 136400}         # FY2013 Item 7 p.42
nonprog = {2013: 0.91, 2012: 0.95, 2011: 0.83}  # year-end share of non-program cars, p.42
for y in (2012, 2013):
    avg_np = us_fleet[y] * (nonprog[y] + nonprog[y - 1]) / 2
    print(y, 'U.S. non-program fleet (rough)', round(avg_np), '/ non-program cars sold', us_sold[y], '=', round(12 * avg_np / us_sold[y], 1), 'months')
print('U.S. non-program cars sold growth %:', round(100 * (us_sold[2013] / us_sold[2012] - 1), 1),
      '| U.S. average fleet growth %:', round(100 * (us_fleet[2013] / us_fleet[2012] - 1), 1))
print('U.S. rate cut 2013 44.2 as % of company pre-tax income', round(100 * 44.2 / pti13, 1))

print('\n=== B. Residual values: wording against disposal results ===')
print('FY2012 report, car rental worldwide: net gains 83.2 (2012), 98.9 (2011)')
print('FY2013 report: U.S. 100.6 gain (2012) -> 48.2 loss (2013); intl losses 17.3 -> 15.2')
print('check 2012 split: 100.6 - 17.3 =', round(100.6 - 17.3, 1), '; 2011: 114.9 - 16.0 =', round(114.9 - 16.0, 1))
print('rate-change split: 139.4 - 8.8 =', round(139.4 - 8.8, 1), '(FY2012 said 130.6); 26.7 - 12.9 =', round(26.7 - 12.9, 1), '(FY2012 said 13.8)')
print('U.S. disposal result per non-program car sold: 2012', round(100.6e6 / us_sold[2012]), '| 2013', round(-48.2e6 / us_sold[2013]))
print('Disposal channels: FY2012 all cars 33% auction / 47% dealer / 13% retail / 7% other')
w_us, w_int = 197700, 64500
for name, us, intl in (('auction', 47, 12), ('dealer direct', 39, 83), ('retail', 14, 5)):
    print('  FY2013 combined (weighted by non-program cars sold, rough):', name, round((us * w_us + intl * w_int) / (w_us + w_int), 1), '% | U.S. alone', us, '%')
print('Retail car sales locations 26 -> 65: +', round(100 * (65 / 26 - 1)), '%')

print('\n=== C. Pricing measure (RPD) ===')
print('FY2012 definition: rental rate revenue 5,952.4 of car rental segment revenue 7,633.0; excluded non-rental rate revenue 1,676.6 =',
      round(100 * 1676.6 / 7633.0, 1), '% of segment revenue')
print('non-rental rate revenue growth 2012: ', round(100 * (1676.6 / 1256.7 - 1), 1), '% | rental rate revenue growth:', round(100 * (5952.4 / 5675.1 - 1), 1), '%')
print('U.S. 2012: old RPD 39.07, new Total RPD 46.33: difference', round(46.33 - 39.07, 2), '=', round(100 * (46.33 / 39.07 - 1), 1), '% higher')
print('U.S. 2012 change: old basis -3.1% (FY2012 p.42); new basis', round(100 * (46.33 / 47.67 - 1), 1), '%')
print('U.S. 2013 Total RPD change:', round(100 * (47.00 / 46.33 - 1), 1), '% | 2013 U.S. revenue ex sublease 6,259.4 / 133,181 days =', round(6259.4e6 / 133181e3, 2))
print('International 2012: old 42.30 -> new 53.52')
# The 1,676.6 above includes Donlen leasing revenue (old car rental segment), so it is not used in the reply.
# Cleaner: U.S. 2012 under both definitions, same 105,539 thousand transaction days.
old_rev_us = 39.07 * 105539e3 / 1e6
print('U.S. 2012 rental rate revenue implied by old RPD:', round(old_rev_us, 1), '| total rental revenue (new, FY2013 p.50): 4,889.5 | newly counted:',
      round(4889.5 - old_rev_us, 1), '=', round(100 * (4889.5 - old_rev_us) / 4889.5, 1), '% of the new total')

print('\n=== D. Adjusted pre-tax income ===')
print('2012 total reportable segments: FY2012', 1247.1, '-> FY2013', 1239.5, 'diff', round(1239.5 - 1247.1, 1))
print('2013 new exclusion lines: integration 40.0 + relocation 7.8 + impairment and other 44.0 + premiums on debt 28.7 + other 50.7 =',
      round(40.0 + 7.8 + 44.0 + 28.7 + 50.7, 1), '=', round(100 * (40.0 + 7.8 + 44.0 + 28.7 + 50.7) / pti13, 1), '% of 2013 pre-tax income')
print('cash items inside the debt lines 2013: premiums 28.7 + conversion cash premiums 11.9 =', round(28.7 + 11.9, 1))
print('restructuring since 2007: FY2012 568.4 + 2013 charge 77.0 =', round(568.4 + 77.0, 1), '(FY2013 says 645.4)')

print('\n=== E. Allowance, bad debt, reserves ===')
print('2012 allowance: FY2012', 25.113, '-> FY2013', 29.3, ': +', round(29.3 - 25.113, 1), '=', round(100 * (29.3 / 25.113 - 1), 1), '%')
print('2012 charge to expense: 34.144 -> 38.3; 2012 write-offs 29.3; 2013 charge 41.9, write-offs 40.3 (+', round(100 * (40.3 / 29.3 - 1), 1), '%)')
print('allowance / gross receivables: 2012 as first reported', round(100 * 25.113 / (rec12_o + 25.113), 2), '| 2012 revised',
      round(100 * 29.3 / (rec12_r + 29.3), 2), '| 2013', round(100 * 30.8 / (rec13 + 30.8), 2))
print('Schedule II charge / total revenue: 2012 (revised)', round(100 * 38.3 / rev12_r, 2), '| 2013', round(100 * 41.9 / rev13, 2),
      '| cash-flow provision 45.9 / revenue', round(100 * 45.9 / rev13, 2))
print('stated bad debt: 0.3% of U.S. car rental revenue, 0.3% international, 0.4% HERC, both years')
seg13 = {'us': 6324.4, 'intl': 2382.5, 'herc': 1538.0}
print('implied 2013 bad debt at the stated rates:', round(0.003 * seg13['us'] + 0.003 * seg13['intl'] + 0.004 * seg13['herc'], 1),
      'vs Schedule II 41.9 and cash flow 45.9')
seg12 = {'car': 7633.0, 'herc': 1385.4}
print('implied 2012 bad debt at the stated rates:', round(0.003 * seg12['car'] + 0.004 * seg12['herc'], 1), 'vs Schedule II 34.1 (first reported) / 38.3 (revised)')
for y in (2011, 2012, 2013):
    print(y, 'PLPD reserve', plpd[y], 'change', round(plpd[y] - plpd[y - 1], 1), round(100 * (plpd[y] / plpd[y - 1] - 1), 1), '%')
print('PLPD / transaction days (worldwide car rental): 2012', round(plpd[2012] * 1e6 / 148787e3, 2), '$ per day | 2013', round(plpd[2013] * 1e6 / (133181e3 + 45019e3), 2))
print('transaction days growth, worldwide car rental:', round(100 * ((133181 + 45019) / 148787 - 1), 1), '% | U.S.:', round(100 * (133181 / 105539 - 1), 1), '%')
print('PLPD / revenue: 2012 revised', round(100 * plpd[2012] / rev12_r, 2), '| 2012 pro forma 10,197.4', round(100 * plpd[2012] / 10197.4, 2), '| 2013', round(100 * plpd[2013] / rev13, 2))

print('\n=== F. Equipment and other useful lives ===')
for y, c, a in ((2011, eq11, eqacc11), (2012, eq12, eqacc12), (2013, eq13, eqacc13)):
    print(y, 'other equipment at cost', c, 'accumulated', a, '=', round(100 * a / c, 1), '%')
for y, d, avgc in ((2012, 272.1 + 13.5, 3069.0), (2013, 298.8 + 26.2, 3401.2)):
    rate = d / avgc
    print(y, 'equipment depreciation before disposal gains', round(d, 1), '/ average acquisition cost', avgc, '=', round(100 * rate, 1), '% a year;',
          'months of depreciation carried:', round(12 * (eqacc12 if y == 2012 else eqacc13) / d, 1), '(stated average age 43 months, range 24 to 108)')
print('Property and equipment: depreciation / average cost: 2012', round(100 * dppe12 / ((ppe12 + ppe11) / 2), 1), '% | 2013', round(100 * dppe13 / ((ppe13 + ppe12) / 2), 1), '%')
print('Other intangibles: amortization 121.5 / gross amortizable 1,167.2 =', round(100 * 121.5 / 1167.2, 1), '% -> implied life', round(1167.2 / 121.5, 1),
      'years | 2012: 83.9 /', 1152.2, '=', round(100 * 83.9 / 1152.2, 1), '% (Dollar Thrifty concessions held 43 days)')
print('FY2013 states "3 to 10 years" (table), "two to fifteen years" (text), Donlen 16 and 20 years, concessions nine years')

print('\n=== F2. Extra tests used in the reply ===')
print('Bad debt at the top of rounding (0.35%, 0.35%, 0.45%): 2012', round(0.0035 * seg12['car'] + 0.0045 * seg12['herc'], 1),
      '| 2013', round(0.0035 * (seg13['us'] + seg13['intl']) + 0.0045 * seg13['herc'], 1))
days = {2011: 137301, 2012: 148787, 2013: 133181 + 45019}     # worldwide car rental transaction days, thousands
for y in (2011, 2012, 2013):
    print(y, 'PLPD reserve per car rental transaction day: $', round(plpd[y] * 1e6 / (days[y] * 1e3), 2))
print('transaction days growth: 2012', round(100 * (days[2012] / days[2011] - 1), 1), '% | 2013', round(100 * (days[2013] / days[2012] - 1), 1),
      '% | two years', round(100 * (days[2013] / days[2011] - 1), 1), '%')
print('PLPD growth two years:', round(100 * (plpd[2013] / plpd[2011] - 1), 1), '% | per day 2013 vs 2011:',
      round(100 * ((plpd[2013] / days[2013]) / (plpd[2011] / days[2011]) - 1), 1), '%')
f13, f12 = 720.8e6 / 133181e3, 539.1e6 / 105539e3            # U.S. fleet related expenses per transaction day (FY2013 pp.49, 53, 59)
print('U.S. fleet related expenses per transaction day: 2012 $', round(f12, 2), '| 2013 $', round(f13, 2), '| change %', round(100 * (f13 / f12 - 1), 1))
print('U.S. depreciation per company-operated car per month: 2012', round(940.6e6 / 358000 / 12, 2), '| 2013', round(1269.3e6 / 468500 / 12, 2),
      '| change %', round(100 * ((1269.3 / 468500) / (940.6 / 358000) - 1), 1))
print('Exclusion lines new in FY2013 (integration 40.0, relocation 7.8, impairment and other 44.0):', round(40.0 + 7.8 + 44.0, 1),
      '=', round(100 * (40.0 + 7.8 + 44.0) / pti13, 1), '% of 2013 pre-tax income')
print('Intangibles implied life (gross amortizable / amortization): 2012', round(1152.2 / 83.9, 1), '| 2013', round(1167.2 / 121.5, 1), 'years')
print('Retail share: FY2012 all cars 13% | FY2013 U.S. 14%, international 5%, combined (rough)', round((14 * w_us + 5 * w_int) / (w_us + w_int), 1), '%')

print('\n=== G. Other figures shown differently ===')
print('Advertising 2012: FY2012 158.0 -> FY2013 183.9 (+', round(183.9 - 158.0, 1), '); 2011: 145.8 -> 168.2 (+', round(168.2 - 145.8, 1), ')')
print('Advertising growth 2012: FY2012 basis', round(100 * (158.0 / 145.8 - 1), 1), '% | FY2013 basis', round(100 * (183.9 / 168.2 - 1), 1), '%')
print('Short-term borrowings in the maturity table: FY2012 5,718.7 of 6,218.8 due within a year -> FY2013 927.2 of 2,053.3')
print('  share of total debt due within a year: FY2012', round(100 * 6218.8 / 15473.8, 1), '% | FY2013', round(100 * 2053.3 / 16302.6, 1), '%')
print('Restructuring 2012 cash payments: FY2012 26.8 -> FY2013 36.8')
print('Dollar Thrifty excluded from 2012 control assessment: 21% of assets, 2% of revenue')


# ---------------------------------------------------------------- quotation check
def check_reply(path):
    if not os.path.exists(path):
        print('\n(reply not written yet)')
        return
    reply = open(path, encoding='utf-8').read()
    ok = bad = 0
    for line in reply.split('\n'):
        # table rows of part 3: first cell is one quotation found in both reports, second cell gives "p. N, p. M" (FY2012, FY2013)
        cells = [c.strip() for c in line.split('|')]
        if line.startswith('| "') and len(cells) > 3:
            q = re.match(r'"([^"]+)"', cells[1]).group(1)
            pp = [int(x) for x in re.findall(r'p\.\s?(\d+)', cells[2])]
            for doc, text, pg in (('FY2012', t12, pp[0]), ('FY2013', t13, pp[1])):
                hits = [h.start() for h in re.finditer(re.escape(q), text)]
                if hits and pg in {page_of(text, h) for h in hits}:
                    ok += 1
                else:
                    print('TABLE QUOTE FAILS', doc, ':', q, '| cited', pg, '| found on', sorted({page_of(text, h) for h in hits}))
                    bad += 1
            line = '|'.join(cells[3:])      # remaining cells are checked like ordinary text
        # every quotation must be followed, within a word or two, by its own cite:
        # "..." (FY2012 report, p. N) or "..." (FY2013 report, p. N)
        for m in re.finditer(r'"([^"]+)"', line):
            q = m.group(1)
            c = re.match(r'[^"(]{0,14}\((FY2012|FY2013)[^)]*?p\.\s?(\d+)\)', line[m.end():m.end() + 50])
            if not c:
                print('QUOTE WITHOUT CITE:', q)
                bad += 1
                continue
            doc, pg = c.group(1), int(c.group(2))
            text = t12 if doc == 'FY2012' else t13
            hits = [h.start() for h in re.finditer(re.escape(q), text)]
            if not hits:
                print('NOT FOUND in', doc, ':', q)
                bad += 1
            elif pg not in {page_of(text, h) for h in hits}:
                print('PAGE MISMATCH', doc, ':', q, '| found on', sorted({page_of(text, h) for h in hits}), '| cited', pg)
                bad += 1
            else:
                ok += 1
    print('\nQuotation check: %d ok, %d failed' % (ok, bad))
    print('Word count:', len(re.findall(r'\S+', reply)))


check_reply(REPLY)
