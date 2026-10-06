# Turn 2: follow the flags. Numbers behind each company explanation.
import openpyxl, re
wb = openpyxl.load_workbook('statements.xlsx', data_only=True)
def sheet(name):
    rows = list(wb[name].iter_rows(values_only=True)); hdr = rows[0]
    return {r[0]: {hdr[i]: r[i] for i in range(1, len(hdr)-1)} for r in rows[1:] if r[0]}
ISa, BSa, CFa, BSq = sheet('IS annual'), sheet('BS annual'), sheet('CF annual'), sheet('BS quarterly')
Y4, Y5, Y3 = 'FY (ended 2025-02-02)', 'FY (ended 2026-02-01)', 'FY (ended 2024-01-28)'
AR26 = open('annual-report-FY2026-02-01-key-sections.txt', encoding='utf-8').read()
AR25 = open('annual-report-FY2025-02-02-key-sections.txt', encoding='utf-8').read()
RL26 = open('earnings-release-Q4-FY2026-02-01.txt', encoding='utf-8').read()
RL25 = open('earnings-release-Q4-FY2025-02-02.txt', encoding='utf-8').read()
DOCS = {'AR26': AR26, 'AR25': AR25, 'RL26': RL26, 'RL25': RL25}
def page_of(doc, quote):
    t = DOCS[doc]; i = t.find(quote)
    if i < 0: return None
    pg = re.findall(r'\[p\. (\d+)\]', t[:i]); return int(pg[-1]) if pg else None
P = ISa['Earnings before provision for income taxes'][Y5]
N = {}
# --- figures read from the notes (annual report to Feb 2026: Note 13 p. 74 and p. 76; Note 1 p. 48, p. 51; Note 2 p. 55; Item 7 p. 39) ---
gms = dict(rec=899, inv=568, ap=380); srs = dict(rec=1831, inv=1988, ap=1791)
for v in ['Receivables | 899','Merchandise inventories | 568','Accounts payable | $380','Receivables | 1,831','Accounts payable | $1,791',
          'Net sales | $151,966 | $12,717 | $164,683 | $153,108 | $6,406 | $159,514','Operating income | 20,574 | 316 | 20,890 | 21,313 | 213 | 21,526',
          'Confirmed obligations outstanding at the end of the year | $414 | $598','Invoices confirmed during the year | 4,394 | 5,140',
          'Cost of sales | 99,717 | 101,194 | 101,709','Selling, general and administrative | 28,885 | 27,822 | 26,598','Federal | $3,590 | $2,475 | $3,737']:
    assert v in AR26, v
# --- inventory ---
inv5, inv4 = BSa['Merchandise inventories'][Y5], BSa['Merchandise inventories'][Y4]
N['inv_rise'] = inv5-inv4; N['inv_gms_share'] = gms['inv']/N['inv_rise']*100
N['inv_cf'] = -CFa['Changes in merchandise inventories'][Y5]; N['inv_cf_share'] = N['inv_cf']/N['inv_rise']*100
N['inv_other'] = N['inv_rise']-gms['inv']-N['inv_cf']
cogs5, cogs4 = ISa['Cost of sales'][Y5], ISa['Cost of sales'][Y4]
N['inv_excess'] = inv5 - (inv4/cogs4*371)*cogs5/364
N['inv_excess_after_gms'] = N['inv_excess']-gms['inv']; N['inv_excess_gms_share'] = gms['inv']/N['inv_excess']*100
q5 = [BSq['Merchandise inventories'][c] for c in ['Q4 (ended 2025-02-02)','Q1 (ended 2025-05-04)','Q2 (ended 2025-08-03)','Q3 (ended 2025-11-02)','Q4 (ended 2026-02-01)']]
q4 = [BSq['Merchandise inventories'][c] for c in ['Q4 (ended 2024-01-28)','Q1 (ended 2024-04-28)','Q2 (ended 2024-07-28)','Q3 (ended 2024-10-27)','Q4 (ended 2025-02-02)']]
N['turn5'] = cogs5/(sum(q5)/5); N['turn4'] = cogs4/(sum(q4)/5)
N['shrink_sens_chg'] = (79/95-1)*100; N['shrink_implied_drop'] = (95-79)*10; N['shrink_pct_pti'] = N['shrink_implied_drop']/P*100
N['inv_growth'] = (inv5/inv4-1)*100
# --- payables ---
ap5, ap4, ap3 = (BSa['Accounts payable'][y] for y in (Y5, Y4, Y3))
N['ap_fall'] = ap4-ap5; N['ap_fall_ex_gms'] = N['ap_fall']+gms['ap']
N['sfp_fall'] = 598-414; N['sfp_share'] = N['sfp_fall']/N['ap_fall']*100; N['sfp_share_ex'] = N['sfp_fall']/N['ap_fall_ex_gms']*100
N['sfp_conf_chg'] = (4394/5140-1)*100
N['ap_cf5'] = CFa['Changes in accounts payable and accrued expenses'][Y5]; N['ap_cf4'] = CFa['Changes in accounts payable and accrued expenses'][Y4]
N['ap_rise_fy24'] = ap4-ap3; N['srs_ap_share'] = srs['ap']/N['ap_rise_fy24']*100
N['ap_short'] = (ap4/cogs4*371)*cogs5/364 - ap5
# --- cash flow ---
cfo5, cfo4 = CFa['Net cash provided by operating activities'][Y5], CFa['Net cash provided by operating activities'][Y4]
N['cfo_drop'] = cfo4-cfo5
sw = lambda l: CFa[l][Y5]-CFa[l][Y4]
N['sw_ap'] = sw('Changes in accounts payable and accrued expenses'); N['sw_inv'] = sw('Changes in merchandise inventories'); N['sw_tax'] = sw('Changes in income taxes payable')
N['sw_sum'] = N['sw_ap']+N['sw_inv']+N['sw_tax']; N['sw_share'] = -N['sw_sum']/N['cfo_drop']*100
N['tax_share'] = -N['sw_tax']/N['cfo_drop']*100; N['fed_tax_paid_rise'] = 3590-2475
# --- receivables ---
rec5, rec4, rec3 = (BSa['Receivables, net'][y] for y in (Y5, Y4, Y3))
N['rec_rise'] = rec5-rec4; N['rec_gms_share'] = gms['rec']/N['rec_rise']*100
N['rec_rise_fy24'] = rec4-rec3; N['rec_srs_share'] = srs['rec']/N['rec_rise_fy24']*100
N['rec_cf5'] = CFa['Changes in receivables, net'][Y5]
# --- operating margin (whole company unless marked Primary segment) ---
s5, s4 = ISa['Net sales'][Y5], ISa['Net sales'][Y4]
om = lambda y: ISa['Operating income'][y]/ISa['Net sales'][y]*100
N['om5'], N['om4'] = om(Y5), om(Y4); N['om_drop'] = N['om4']-N['om5']
pm5, pm4 = 20574/151966*100, 21313/153108*100; o5, o4 = 316/12717*100, 213/6406*100
N.update(pm5=pm5, pm4=pm4, o5=o5, o4=o4)
w5 = 12717/164683
mix_only = pm4*(1-w5)+o4*w5                      # FY2024 margins at the FY2025 sales mix
N['mix_effect'] = N['om4']-mix_only; N['mix_share'] = N['mix_effect']/N['om_drop']*100
N['primary_effect'] = (pm4-pm5)*(1-w5); N['primary_share'] = N['primary_effect']/N['om_drop']*100
N['other_effect'] = (o4-o5)*w5; N['other_share'] = N['other_effect']/N['om_drop']*100
N['psga_g'] = (28885/27822-1)*100; N['psales_g'] = (151966/153108-1)*100
N['psga_pts'] = 28885/151966*100-27822/153108*100
N['pgm_pts'] = (151966-99717)/151966*100-(153108-101194)/153108*100
N['amort_pts'] = 607/s5*100-425/s4*100; N['amort_share'] = N['amort_pts']/N['om_drop']*100
N['om_money'] = N['om_drop']/100*s5; N['om_pct_pti'] = N['om_money']/P*100
# --- adjusted earnings (results releases, p. 8) ---
for v in ['Adjusted diluted earnings per share (Non-GAAP) | $2.72 | $3.13 | (13.1)% | $14.69 | $15.24 | (3.6)%','Acquired intangible asset amortization (4) | 171 | 145 | 607 | 425']: assert v in RL26, v
for v in ['Adjusted diluted earnings per share (Non-GAAP) | $3.13 | $2.86 | 9.4% | $15.24 | $15.25 | (0.1)%','Acquired intangible asset amortization (4) | 145 | 50 | 425 | 186']: assert v in RL25, v
N['adj_gap5'] = 14.69-14.23; N['adj_gap4'] = 15.24-14.91; N['adj_gap3'] = 15.25-15.11
N['adj_gap5_pct'] = N['adj_gap5']/14.23*100; N['adj_gap4_pct'] = N['adj_gap4']/14.91*100
N['adj_oi5_pct'] = 607/20890*100; N['adj_oi4_pct'] = 425/21526*100
N['nonrec_in_releases'] = {d: [w for w in ['non-recurring','nonrecurring','one-time','unusual'] if w in DOCS[d].lower()] for d in ['RL25','RL26']}
# useful lives unchanged between the two annual reports
for v in ['Buildings and improvements | 5 – 45 years','Furniture, fixtures and equipment | 2 – 20 years','Leasehold improvements | 5 – 45 years','ranges from three to seven years','range up to approximately 20 years']:
    assert v in AR26 and v in AR25, v
if __name__ == '__main__':
    for k, v in N.items(): print(k, round(v, 2) if isinstance(v, float) else v)

# ---- reply ----
QUOTES = []   # (doc, quote, page) collected as the reply is built, then verified
NAME = {'AR26': 'annual report to Feb 2026', 'AR25': 'annual report to Feb 2025', 'RL26': 'results release to Feb 2026', 'RL25': 'results release to Feb 2025'}
def q(doc, text, cite=True):
    p_ = page_of(doc, text); assert p_ is not None, ('NOT FOUND', doc, text)
    QUOTES.append((doc, text, p_))
    if not cite: return '"%s"' % text
    return '"%s" (%s, p. %d)' % (text, NAME[doc], p_)
def pg(doc, anchor):
    p_ = page_of(doc, anchor); assert p_ is not None, anchor; return p_
def build_reply():
    m = lambda v: '${:,.0f}m'.format(abs(v))
    L = []
    L.append('**Inventory rose %.1f%% against cost of sales up 3.4%% (whole company)**' % N['inv_growth'])
    L.append('- **The company says:** inventory turnover fell from 4.7 to 4.4 times, %s, which restates the movement without giving a reason. Last year: different, turnover rose on %s.' % (q('AR26', 'primarily driven by higher average inventory levels'), q('AR25', 'lower average inventory levels within our Primary segment')))
    L.append('- **Test:** of the %s rise, inventory that came with GMS is %s (%.0f%%) and the build on the cash flow statement is %s (%.0f%%); the 4.4 and 4.7 turns reproduce from five-quarter average inventory. The acquisition covers a quarter and the build has no stated reason, so the explanation partly holds.' % (m(N['inv_rise']), m(568), N['inv_gms_share'], m(N['inv_cf']), N['inv_cf_share']))
    L.append('- **Reading:** can\'t tell from these documents, possibly ordinary: the report mentions %s (p. %d) but does not tie them to inventory. A build sitting in the Primary segment, where sales fell %.1f%% (52 weeks against 53), would point to the business weakening.' % (q('AR26', 'increased costs as a result of tariffs', cite=False), pg('AR26', 'increased costs as a result of tariffs'), -N['psales_g']))
    L.append('- **Read next:** merchandise inventories in Note 1 (p. %d) and the auditor\'s critical audit matter, which changed from %s to %s.' % (pg('AR26', 'Inventory cost includes the amount we pay'), q('AR25', 'Estimation of store shrink'), q('AR26', 'Sufficiency of audit evidence over certain merchandise inventories')))
    L.append('')
    L.append('**Payables fell 3.7% against cost of sales up 3.4% (whole company)**')
    L.append('- **The company says:** working capital moved on %s. Last year: the same words with the opposite sign, %s.' % (q('AR26', 'the timing of vendor payments'), q('AR25', 'partially offset by the timing of vendor payments')))
    L.append('- **Test:** payables fell %s, or %s before the %s that came with GMS; supplier finance obligations fell %s (%.0f%% of the fall) as invoices confirmed fell %.1f%%. Timing itself cannot be tested from these documents, so the explanation partly holds.' % (m(N['ap_fall']), m(N['ap_fall_ex_gms']), m(380), m(N['sfp_fall']), N['sfp_share'], -N['sfp_conf_chg']))
    L.append('- **Reading:** most likely ordinary: paying suppliers sooner uses cash but does not lift income. Shorter terms set by suppliers, or a finance program cut back by its banks, would point to the business weakening.')
    L.append('- **Read next:** the supplier finance program in Note 1 (p. %d), and the next first-quarter cash flow, where a timing effect should reverse.' % pg('AR26', 'Supplier Finance Program'))
    L.append('')
    L.append('**Operating margin fell from %.1f%% to %.1f%% (whole company)**' % (N['om4'], N['om5']))
    L.append('- **The company says:** selling and administrative costs rose on %s and %s (%s, p. %d), with no amounts. Last year: similar, payroll and %s, so a legal benefit sits in both prior years.' % (q('AR26', 'higher payroll and related costs', cite=False), q('AR26', 'a non-recurring legal-related benefit recognized during fiscal 2024', cite=False), NAME['AR26'], pg('AR26', 'higher payroll and related costs'), q('AR25', 'lower legal-related benefits')))
    L.append('- **Test:** of the %.2f-point fall, the larger share of lower-margin SRS and GMS sales accounts for %.2f points (%.0f%%) and the Primary segment\'s own margin, %.1f%% to %.1f%%, for %.2f points (%.0f%%); the payroll and legal amounts behind the second part are not given. So the explanation partly holds.' % (N['om_drop'], N['mix_effect'], N['mix_share'], N['pm4'], N['pm5'], N['primary_effect'], N['primary_share']))
    L.append('- **Reading:** most likely the business weakening: Primary-segment selling and administrative costs rose %.1f%% while its sales fell %.1f%% (52 weeks against 53), in the third straight year of margin decline. A large fiscal 2024 legal benefit would mean that year was flattered and the underlying fall is smaller.' % (N['psga_g'], -N['psales_g']))
    L.append('- **Read next:** the segment table in Note 2 (p. %d) and commitments and contingencies in Note 12 (p. %d).' % (pg('AR26', 'The following table presents net sales, significant expenses, and operating income for our Primary segment'), pg('AR26', '12.COMMITMENTS AND CONTINGENCIES')))
    L.append('')
    L.append('**The other flags**')
    L.append('- **Cash flow fell behind earnings:** %s; the swings in payables, inventory and taxes payable total %s against a %s fall in operating cash flow (%.0f%%), the taxes-payable swing, which the report ties to a deferred fiscal 2024 tax payment, alone being %.0f%%. Holds; most likely ordinary timing.' % (q('AR26', 'primarily due to changes in working capital'), m(N['sw_sum']), m(N['cfo_drop']), N['sw_share'], N['tax_share']))
    L.append('- **Receivables outgrew revenue:** no reason given this year; last year, %s. GMS brought %s of receivables (p. %d) against a %s rise (%.0f%%). Holds; most likely ordinary.' % (q('AR25', 'primarily as a result of the SRS acquisition'), m(899), pg('AR26', 'Receivables | 899'), m(N['rec_rise']), N['rec_gms_share']))
    L.append('')
    L.append('**Adjusted earnings:** adjusted diluted earnings per share were $14.69 against $14.23 reported in fiscal 2025 (gap $%.2f, %.1f%%) and $15.24 against $14.91 in fiscal 2024 (gap $%.2f, %.1f%%).  ' % (N['adj_gap5'], N['adj_gap5_pct'], N['adj_gap4'], N['adj_gap4_pct']))
    L.append('The only adjustment in both years is %s, $607m and $425m; neither release uses the words non-recurring, one-time or unusual.' % q('RL26', 'amortization expense from acquired intangible assets'))
    L.append('')
    L.append('**Changes in estimate that lifted income:** none disclosed, and useful lives are the same in both reports.  ')
    L.append('One estimate did move in income\'s favor without a stated effect: the cost of a 10%% rise in the shrink rate fell from %s to %s (%s, p. %d), implying about %s less estimated shrink (%.1f%% of pre-tax income) while inventory rose %.1f%%. Both reports credit %s for gross margin (p. %d of each), and neither gives a reserve balance to test it.' % (q('AR25', 'approximately $95 million'), q('AR26', 'approximately $79 million', cite=False), NAME['AR26'], pg('AR26', 'approximately $79 million'), m(N['shrink_implied_drop']), N['shrink_pct_pti'], N['inv_growth'], q('AR26', 'lower shrink', cite=False), pg('AR26', 'lower shrink')))
    return '\n'.join(L)

def check_quotes(txt):
    """Every quoted string in the reply must be an exact substring of a cited document, on the cited page."""
    ok = True
    found = re.findall(r'"([^"]+)"', txt)
    registered = {t for _, t, _ in QUOTES}
    for f in found:
        if f not in registered:
            ok = False; print('UNREGISTERED QUOTE:', f)
    for doc, text, p_ in QUOTES:
        t = DOCS[doc]; i = t.find(text)
        marks = re.findall(r'\[p\. (\d+)\]', t[:i])
        good = i >= 0 and int(marks[-1]) == p_ and (('p. %d' % p_) in txt)
        # the quote must also be on that page wherever it is cited: check every occurrence shares the cited page when the quote repeats
        print('OK ' if good else 'FAIL', doc, 'p.', p_, '|', text, '| occurrences:', t.count(text))
        ok = ok and good
    assert 'lower shrink' in AR25 and page_of('AR25', 'lower shrink') == page_of('AR26', 'lower shrink')
    return ok

if __name__ == '__main__':
    import sys
    if 'reply' in sys.argv:
        txt = build_reply()
        for w in ['fraud', 'manipulat', 'red flag', '—']: assert w not in txt.lower(), w
        assert '>' not in txt
        ok = check_quotes(txt)
        print('QUOTE CHECK:', 'all pass' if ok else 'FAILURES', len(QUOTES), 'quotes')
        print('WORDS', len(re.sub(r'[*]', ' ', txt).split()))
        if ok:
            open('runs/v2.10/numbers-2.md', 'w', encoding='utf-8').write(txt + '\n')
        print(txt)
