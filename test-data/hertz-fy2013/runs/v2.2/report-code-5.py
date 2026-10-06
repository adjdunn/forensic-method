# Turn 3 (prompt 5: report). Checks only: quotations, and that no number is new.
# Usage: python report-code-5.py [path to the report text]   (default: report-5.md beside this script)
import re, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(os.path.dirname(HERE))
t13 = open(os.path.join(BASE, 'annual-report-FY2013-12-31-key-sections.txt'), encoding='utf-8').read()
t12 = open(os.path.join(BASE, 'annual-report-FY2012-12-31-key-sections.txt'), encoding='utf-8').read()
REPORT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'report-5.md')
report = open(REPORT, encoding='utf-8').read()
earlier = {n: open(os.path.join(HERE, n), encoding='utf-8').read()
           for n in ('text-3.md', 'text-4.md', 'numbers-1.md', 'numbers-2.md')}


def page_of(text, pos):
    m = re.findall(r'\[p\. (\d+)\]', text[:pos])
    return int(m[-1]) if m else None


# ---- 1. quotations: exact substring of the cited report, on the cited page
ok = bad = 0
for line in report.split('\n'):
    for m in re.finditer(r'"([^"]+)"', line):
        q = m.group(1)
        c = re.match(r'[^"(]{0,14}\((FY2012|FY2013),? (?:report, )?p\. (\d+)\)', line[m.end():m.end() + 50])
        if not c:
            print('QUOTE WITHOUT CITE:', q)
            bad += 1
            continue
        doc, pg = c.group(1), int(c.group(2))
        text = t12 if doc == 'FY2012' else t13
        pages = {page_of(text, h.start()) for h in re.finditer(re.escape(q), text)}
        if pg in pages:
            ok += 1
        else:
            print('QUOTE FAILS:', doc, 'p.', pg, '|', q, '| found on', sorted(p for p in pages if p))
            bad += 1
        # every quotation should also have been used in an earlier reply
        if not any(q in e for e in earlier.values()):
            print('  note: quotation not used verbatim in an earlier reply:', q)
print('Quotation check: %d ok, %d failed' % (ok, bad))

# ---- 2. page references: each cited page must hold what is cited (spot facts) and appear in an earlier reply
all_earlier = '\n'.join(earlier.values())


def tokens(s):
    # numbers as written, without $ , % M m signs; keeps a leading minus only for standalone negatives like -3.25
    return re.findall(r'(?<![\w.])-?\d[\d,]*\.?\d*', s)


def norm(tok):
    return tok.replace(',', '').rstrip('.')


earlier_tokens = {norm(t) for t in tokens(all_earlier)}
earlier_tokens |= {t.lstrip('-') for t in earlier_tokens}

# ---- 2a. size shares: each item's amount (taken from an earlier reply) over FY2013 pre-tax income (workbook)
import openpyxl
wb = openpyxl.load_workbook(os.path.join(BASE, 'statements.xlsx'), data_only=True)
rows = list(wb['IS annual'].iter_rows(values_only=True))
col = [i for i, h in enumerate(rows[0]) if h and '2013-12-31' in str(h)][0]
PTI = [r[col] for r in rows if r[0] == 'Income before income taxes'][0]
print('Base: FY2013 income before income taxes, statements.xlsx, IS annual =', PTI)
SIZES = [  # (item, amount in $m, kind of amount, earlier reply the amount comes from)
    ('Fleet depreciation: U.S. rate cuts stated by the company', 44.2, 'effect on reported income (company-stated)', 'text-3, text-4, numbers-2'),
    ('Fleet depreciation: wider estimate, lower charge on 2013 fleet', 152.0, 'effect on reported income (estimate)', 'numbers-2'),
    ('Adjusted pre-tax income: all exclusions', 490.1, 'gap between adjusted and reported', 'text-3, numbers-2'),
    ('Error corrections: out-of-period errors, 2010 to 2013', 46.3, 'effect on reported income (company-stated)', 'text-3'),
    ('Error corrections: the part in the first nine months of 2013', 11.6, 'effect on reported income (company-stated)', 'text-3, numbers-1'),
    ('Advantage sale: impairment of subleased cars', 40.0, 'effect on reported income (charge booked)', 'text-3'),
    ('Receivables: fall not explained by fleet-sale timing', 105.8, 'balance-sheet movement', 'numbers-2'),
    ('Tax valuation allowance: rise in Schedule II', 53.0, 'balance-sheet movement', 'text-3'),
    ('Concession-fee case: possible judgment', 40.0, 'possible future loss', 'text-3, text-4'),
]
allowed_shares = set()
for item, amt, kind, src in SIZES:
    assert norm(str(amt)) in earlier_tokens or norm(str(int(amt))) in earlier_tokens, amt
    share = round(100 * amt / PTI, 1)
    allowed_shares.add('%.1f' % share)
    print('  %-62s %7.1f / %.1f = %5.1f%%   %-44s (amount from %s)' % (item, amt, PTI, share, kind, src))

new = []
for tok in tokens(report):
    n = norm(tok)
    if n in earlier_tokens or n.lstrip('-') in earlier_tokens or n in allowed_shares:
        continue
    new.append(tok)
# list numbering 1-5 and "five" are structure, not figures; report them anyway if absent
print('Numbers in the report:', len(tokens(report)), '| not found in the four earlier replies:', new if new else 'none')
for tok in sorted({norm(t) for t in tokens(report)}, key=lambda x: float(x)):
    src = [n for n, e in earlier.items() if norm(tok) in {norm(t).lstrip('-') for t in tokens(e)} or norm(tok) in {norm(t) for t in tokens(e)}]
    print('  %-8s %s' % (tok, ', '.join(src)))

# ---- 3. banned words, em-dashes, length
for w in ('fraud', 'manipulat', 'red flag', '—'):
    if w in report.lower():
        print('BANNED:', w)
print('Word count:', len(re.findall(r'\S+', report)))
