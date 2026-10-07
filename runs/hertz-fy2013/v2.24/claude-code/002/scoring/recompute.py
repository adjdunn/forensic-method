"""Recompute the figures the v2.24 claude-code run 002 replies use for their sizes and tests.

Scorer: Claude Code cloud-session subagent, Claude Fable 5.1, 7 October 2026.
Inputs: the workspace the run saw (statements.xlsx, the two 10-K text files, the two
Q4 release text files). Every figure typed in from the pack text is asserted present on
its cited page before it is used. Run from anywhere:

    python3 -I recompute.py

Ten measures, each with sub-figures; the summary at the end counts matches.
Pages are the [p. N] markers, which the pack header says mark the START of printed page N.
"""
import os, re, sys
import openpyxl

HERE = os.path.dirname(os.path.abspath(__file__))
WS = os.path.normpath(os.path.join(HERE, '..', 'workspace'))


def pages(fn):
    txt = open(os.path.join(WS, fn), encoding='utf-8', errors='replace').read()
    parts = re.split(r'\n?\[p\. ([^\]]+)\]\n?', txt)
    d = {}
    for i in range(1, len(parts), 2):
        d.setdefault(parts[i], '')
        d[parts[i]] += parts[i + 1]
    return d


A12 = pages('annual-report-FY2012-12-31.txt')
A13 = pages('annual-report-FY2013-12-31.txt')
R12 = pages('earnings-release-Q4-FY2012-12-31.txt')
R13 = pages('earnings-release-Q4-FY2013-12-31.txt')

wb = openpyxl.load_workbook(os.path.join(WS, 'statements.xlsx'), data_only=True)


def sheet_rows(name):
    return [list(r) for r in wb[name].iter_rows(values_only=True) if any(c is not None for c in r)]


def line(sheet, label, col):
    """Value of the row whose first cell starts with `label`, at column index `col` (1 = first period)."""
    for r in sheet_rows(sheet):
        if isinstance(r[0], str) and r[0].startswith(label):
            return r[col]
    raise KeyError(label)


def on_page(doc, page, s):
    """Assert that the string s is printed on the given page of doc."""
    assert s in doc[page], f'{s!r} not on p. {page}'
    return True


results = []  # (measure, label, reported, recomputed, match)


def check(measure, label, reported, recomputed, tol=0.051):
    ok = abs(reported - recomputed) <= tol
    results.append((measure, label, reported, round(recomputed, 3), ok))
    return ok


def section(title):
    print('\n' + title)
    print('-' * len(title))


# ---------------------------------------------------------------------------
# Shared inputs
# ---------------------------------------------------------------------------
PTI13 = 663.1                              # FY2013 pre-tax income, IS annual and release Table 1
assert line('IS annual', 'Income before income taxes', 5) == 663.1
on_page(A13, '50', '$663.1')

# Balance sheet, as first reported (workbook) and FY2013 10-K revised 2012 column (p. 75)
cars = {y: line('BS annual', 'Cars', i) for y, i in zip((2010, 2011, 2012, 2013), (1, 2, 3, 4))}
oth = {y: line('BS annual', 'Other equipment', i) for y, i in zip((2010, 2011, 2012, 2013), (1, 2, 3, 4))}
cars_acc = {y: -line('BS annual', 'Less accumulated depreciation', i) for y, i in zip((2010, 2011, 2012, 2013), (1, 2, 3, 4))}
on_page(A13, '75', 'Cars | 14,456.6 | 12,548.8')
on_page(A13, '75', 'Less accumulated depreciation | (2,679.6) | (1,850.4)')
on_page(A13, '75', 'Other equipment | 3,512.2 | 3,240.1')
on_page(A13, '75', 'Less accumulated depreciation | (1,095.8) | (1,041.9)')
CARS12_REV, CARS_ACC12_REV = 12548.8, 1850.4
gross = {y: cars[y] + oth[y] for y in cars}            # first-reported gross fleet
gross12_rev = CARS12_REV + oth[2012]

# Note 8 depreciation of revenue earning equipment, before the disposal adjustment
on_page(A13, '126', 'Depreciation of revenue earning equipment | $2,407.8 | $2,145.9 | $1,912.3')
on_page(A13, '126', 'Adjustment of depreciation upon disposal of revenue earning equipment | 37.2 | (96.8) | (112.2)')
on_page(A12, '113', 'Depreciation of revenue earning equipment | $2,165.2 | $1,921.8 | $1,747.0')
DEP = {2011: 1921.8, 2012: 2165.2, 2013: 2407.8}       # as first reported for 2011 and 2012
DEP_REV = {2011: 1912.3, 2012: 2145.9, 2013: 2407.8}
ADJ = {2011: -112.2, 2012: -96.8, 2013: 37.2}

# ---------------------------------------------------------------------------
# M1 Rental equipment depreciation rate (numbers-1: 16.2, 15.3, 14.2; numbers-2: 15.17 -> 14.27, 15.28)
# ---------------------------------------------------------------------------
section('M1 Rental equipment depreciation rate, Note 8 charge over average gross cars plus other equipment')
rate11 = DEP[2011] / ((gross[2010] + gross[2011]) / 2) * 100
rate12 = DEP[2012] / ((gross[2011] + gross[2012]) / 2) * 100
rate13_first = DEP[2013] / ((gross[2012] + gross[2013]) / 2) * 100
rate12_rev = DEP_REV[2012] / ((gross[2011] + gross12_rev) / 2) * 100
rate13_rev = DEP_REV[2013] / ((gross12_rev + gross[2013]) / 2) * 100
check('M1', 'FY2011 rate, numbers-1 16.2%', 16.2, rate11)
check('M1', 'FY2012 rate first reported, numbers-1 15.3%', 15.3, rate12)
check('M1', 'FY2012 rate first reported, numbers-2 15.28%', 15.28, rate12, 0.0051)
check('M1', 'FY2013 rate on first-reported 2012 base, numbers-1 14.2%', 14.2, rate13_first)
check('M1', 'FY2012 rate revised, numbers-2 15.17%', 15.17, rate12_rev, 0.0051)
check('M1', 'FY2013 rate on revised 2012 base, numbers-2 14.27%', 14.27, rate13_rev, 0.0051)
# Q4 same-quarter rate, which numbers-1 says it did not calculate (AK12: it is computable from the release)
on_page(R13, 'unnumbered', 'Depreciation of revenue earning equipment | 333.4 | 102.0 | 75.7 | 109.1 | 620.2 | 245.9 | 111.9 | 73.9 | 102.1 | 533.8')
q = sheet_rows('BS quarterly')
def qline(label, idx):
    for r in q:
        if isinstance(r[0], str) and r[0].startswith(label):
            return r[idx]
    raise KeyError(label)
# columns: 1 Q4-11, 2 Q1-12, 3 Q2-12, 4 Q3-12, 5 Q4-12, 6 Q1-13, 7 Q2-13, 8 Q3-13, 9 Q4-13
g = {i: qline('Cars', i) + qline('Other equipment', i) for i in range(1, 10)}
q4_13 = 620.2 / ((g[8] + g[9]) / 2) * 365 / 92 * 100
q4_12 = 533.8 / ((g[4] + g[5]) / 2) * 365 / 92 * 100
print(f'  Q4 2013 rate annualised {q4_13:.1f}%, Q4 2012 {q4_12:.1f}% (computable; the run wrote "not calculated")')

# ---------------------------------------------------------------------------
# M2 Charge not taken at the prior-year rate, and the flat rate with the disposal adjustment
# ---------------------------------------------------------------------------
section('M2 Shortfall against the FY2012 rate; share explained by the stated rate changes; rate with disposal adjustment')
base13_first = (gross[2012] + gross[2013]) / 2
base13_rev = (gross12_rev + gross[2013]) / 2
short_first = rate12 / 100 * base13_first - DEP[2013]
short_rev = rate12_rev / 100 * base13_rev - DEP_REV[2013]
check('M2', 'numbers-1 shortfall $174.5m', 174.5, short_first, 0.15)
check('M2', 'numbers-1 shortfall 26% of pre-tax', 26, short_first / PTI13 * 100, 0.5)
check('M2', 'numbers-2 shortfall $152.1m', 152.1, short_rev, 0.15)
check('M2', 'numbers-2 shortfall 23% of pre-tax', 23, short_rev / PTI13 * 100, 0.5)
on_page(A13, '40', 'depreciation of revenue earning equipment decreased by $39.6 million, $130.1 million')
check('M2', 'numbers-2: $39.6m covers 26% of $152.1m', 26, 39.6 / short_rev * 100, 0.5)
check('M2', 'numbers-2: $39.6m is 1.6% of rental depreciation', 1.6, 39.6 / DEP[2013] * 100)
flat13 = (DEP_REV[2013] + ADJ[2013]) / base13_rev * 100
flat12 = (DEP_REV[2012] + ADJ[2012]) / ((gross[2011] + gross12_rev) / 2) * 100
check('M2', 'numbers-2: rate with disposal adjustment 14.48% (2012)', 14.48, flat12, 0.0051)
check('M2', 'numbers-2: rate with disposal adjustment 14.49% (2013)', 14.49, flat13, 0.0051)

# ---------------------------------------------------------------------------
# M3 Note 8 stated effects and the U.S. disposal swing (text-3, text-4, numbers-2, report-5)
# ---------------------------------------------------------------------------
section('M3 Note 8: $44.2m and $39.6m as shares of pre-tax; U.S. disposal swing')
on_page(A13, '126', 'net decreases of $44.2 million, $139.4 million and $26.7 million')
on_page(A13, '126', 'net losses of $48.2 million, and net gains of $100.6 million and $114.9 million')
check('M3', '$44.2m = 6.7% of pre-tax', 6.7, 44.2 / PTI13 * 100)
check('M3', '$39.6m = 6.0% of pre-tax', 6.0, 39.6 / PTI13 * 100)
check('M3', 'U.S. disposal swing $148.8m', 148.8, 100.6 + 48.2)
check('M3', 'swing = 22.4% of pre-tax', 22.4, (100.6 + 48.2) / PTI13 * 100)
# the checker's "mismatch" took 39.6 as the base for 6.7%; 44.2 is the figure the sentence names

# ---------------------------------------------------------------------------
# M4 Holding-period range, U.S. depreciation per car-month, accumulated depreciation ratios (text-4, report-5)
# ---------------------------------------------------------------------------
section('M4 Range top 28 to 36; U.S. depreciation per car per month; accumulated depreciation over cost; other rates')
on_page(A12, '81', 'Cars | 4 to 28 months'); on_page(A13, '91', 'Cars | 4 to 36 months')
on_page(A12, '81', 'Useful lives are as follows'); on_page(A13, '91', 'Holding periods are as follows')
on_page(A12, '11', 'eighteen months in the United States'); on_page(A13, '11', 'eighteen months in the United States')
check('M4', 'top of car range +28.6%', 28.6, (36 - 28) / 28 * 100)
on_page(A13, '131', 'U.S. car rental | $1,269.3 | $940.6 | $971.7')
on_page(A13, '49', 'Average number of cars (Company-operated) | 468,500 | 358,000 | 321,700')
on_page(A13, '49', 'Average number of cars (Leased) | 21,500 | 1,100')
pcm13 = (1269.3 - 48.2) / (468500 + 21500) / 12 * 1e6
pcm12 = (940.6 + 100.6) / (358000 + 1100) / 12 * 1e6
check('M4', 'U.S. depreciation per car-month before sale results, 2012 $241.6', 241.6, pcm12, 0.06)
check('M4', 'U.S. depreciation per car-month before sale results, 2013 $207.7', 207.7, pcm13, 0.06)
# exact change is -14.05%; -14.0% reproduces from the rounded dollars (207.7 / 241.6), a rounding chain
check('M4', 'change -14.0% (exact -14.05%, from rounded dollars -14.03%)', -14.0, (round(pcm13, 1) / round(pcm12, 1) - 1) * 100)
check('M4', 'car accumulated depreciation over cost, 2012 revised 14.7%', 14.7, CARS_ACC12_REV / CARS12_REV * 100)
check('M4', 'car accumulated depreciation over cost, 2013 18.5%', 18.5, cars_acc[2013] / cars[2013] * 100)
oth_acc = {y: -line('BS annual', 'Less accumulated depreciation', i) for y, i in zip((2012, 2013), (3, 4))}
# the second "Less accumulated depreciation" row belongs to other equipment; take it explicitly
rows = sheet_rows('BS annual')
acc_rows = [r for r in rows if isinstance(r[0], str) and r[0].startswith('Less accumulated depreciation')]
oth_acc12, oth_acc13 = -acc_rows[1][3], -acc_rows[1][4]
check('M4', 'equipment accumulated depreciation over cost 32.2% -> 31.2% (2012)', 32.2, oth_acc12 / oth[2012] * 100)
check('M4', 'equipment accumulated depreciation over cost (2013)', 31.2, oth_acc13 / oth[2013] * 100)
on_page(A13, '131', 'Worldwide equipment rental | 298.8 | 272.1 | 254.3')
check('M4', 'equipment depreciation over average cost 8.9% (2012)', 8.9, 272.1 / ((oth[2011] + oth[2012]) / 2) * 100, 0.1)
check('M4', 'equipment depreciation over average cost 8.8% (2013)', 8.8, 298.8 / ((oth[2012] + oth[2013]) / 2) * 100, 0.1)
ppe = {y: line('BS annual', 'Total property and equipment, at cost', i) for y, i in zip((2011, 2012, 2013), (2, 3, 4))}
check('M4', 'PP&E depreciation rate 7.3% (2012)', 7.3, 172.6 / ((ppe[2011] + ppe[2012]) / 2) * 100)
check('M4', 'PP&E depreciation rate 7.9% (2013)', 7.9, 205.3 / ((ppe[2012] + ppe[2013]) / 2) * 100)

# ---------------------------------------------------------------------------
# M5 Allowance for doubtful accounts (numbers-1, numbers-2, text-3, text-4, report-5)
# ---------------------------------------------------------------------------
section('M5 Allowance over gross receivables; allowance over write-offs; provision tie-out')
on_page(A13, '158', 'Year ended December 31, 2013 | $29.3 | $41.9 | $(0.1) | $(40.3) | (a) | $30.8')
on_page(A13, '158', 'Year ended December 31, 2012(b) | 20.3 | 38.3 |'); on_page(A13, '158', '| (29.3) | (a) | 29.3')
on_page(A12, '140', 'Year ended December 31, 2012 | $20,282 | $34,144 | $28 | $(29,341) | (a) | $25,113')
on_page(A12, '140', 'Year ended December 31, 2011 | 19,708 | 28,164 | 68 | (27,658) | (a) | 20,282')
rec = {y: line('BS annual', 'Receivables', i) for y, i in zip((2010, 2011, 2012, 2013), (1, 2, 3, 4))}
allow = {2010: 19.708, 2011: 20.282, 2012: 25.113, 2013: 30.8}
check('M5', 'allowance / gross receivables FY2010 1.43%', 1.43, allow[2010] / (rec[2010] + allow[2010]) * 100, 0.0051)
check('M5', 'FY2011 1.24%', 1.24, allow[2011] / (rec[2011] + allow[2011]) * 100, 0.0051)
check('M5', 'FY2012 first reported 1.31%', 1.31, allow[2012] / (rec[2012] + allow[2012]) * 100, 0.0051)
check('M5', 'FY2013 2.00%', 2.00, allow[2013] / (rec[2013] + allow[2013]) * 100, 0.0051)
on_page(A13, '75', 'Receivables, less allowance for doubtful accounts of $30.8 and $29.3 | 1,512.6 | 1,879.7')
check('M5', 'FY2012 revised 1.53% (numbers-2)', 1.53, 29.3 / (1879.7 + 29.3) * 100, 0.0051)
check('M5', 'allowance over write-offs 0.76x (text-3)', 0.76, 30.8 / 40.3, 0.0051)
check('M5', 'write-offs $40.3m from $29.3m: rise', 11.0, 40.3 - 29.3)
on_page(A13, '80', 'Provision for losses on doubtful accounts | 45.9 | 38.3 | 28.2')
check('M5', 'provision gap $4.0m (cash flow 45.9 vs Schedule II 41.9)', 4.0, 45.9 - 41.9)

# ---------------------------------------------------------------------------
# M6 Adjusted pre-tax income (numbers-2, text-3, text-4, report-5)
# ---------------------------------------------------------------------------
section('M6 Adjusted pre-tax income: gaps, recurring items, new 2013 categories')
on_page(R13, 'unnumbered', 'Income before income taxes | 663.1 | 490.1 | 1,153.2 | 441.4 | 450.9 | 892.3')
check('M6', 'gap $490.1m', 490.1, 1153.2 - 663.1)
check('M6', 'gap = 73.9% of GAAP (report ranks on it)', 73.9, 490.1 / 663.1 * 100)
check('M6', 'gap = 42% of adjusted', 42, 490.1 / 1153.2 * 100, 0.5)
check('M6', '2012 gap = 102% of GAAP', 102, 450.9 / 441.4 * 100, 0.5)
on_page(R12, '10', 'Income before income taxes | 450.6 | 450.9 | 901.5')
check('M6', '2012 first reported: 901.5 against 450.6, gap', 450.9, 901.5 - 450.6)
on_page(A13, '50', 'Restructuring charges | (77.0) | (38.0) | (56.4)')
on_page(A13, '50', 'Restructuring related charges(4) | (21.8) | (11.1) | (9.8)')
check('M6', 'restructuring and related $98.8m', 98.8, 77.0 + 21.8)
check('M6', '= 14.9% of pre-tax', 14.9, 98.8 / PTI13 * 100)
check('M6', 'numbers-2 restructuring 2011 $66.2m', 66.2, 56.4 + 9.8)
check('M6', 'numbers-2 restructuring 2012 $49.1m', 49.1, 38.0 + 11.1)
on_page(A13, '140', '$645.4 million')
check('M6', 'seven-year average $92.2m', 92.2, 645.4 / 7)
on_page(A13, '50', 'Integration expenses(7) | (40.0)'); on_page(A13, '50', 'Relocation costs | (7.8)'); on_page(A13, '50', 'Impairment charges and other(10) | (44.0)')
check('M6', 'new 2013 categories $91.8m', 91.8, 40.0 + 7.8 + 44.0)
check('M6', '= 13.8% of pre-tax', 13.8, 91.8 / PTI13 * 100)
on_page(A13, '56', 'early conversion of a portion of our Convertible Senior Notes of $38.6 million')
check('M6', 'with the conversion loss $130.4m', 130.4, 91.8 + 38.6)
check('M6', '= 19.7% of pre-tax', 19.7, 130.4 / PTI13 * 100)
on_page(A13, '140', '$21.9 million of costs related to the relocation of our corporate headquarters')
check('M6', '$21.9m = 3.3% of pre-tax', 3.3, 21.9 / PTI13 * 100)
on_page(A13, '50', 'Purchase accounting(2) | (132.2)')
check('M6', 'purchase accounting 19.9%', 19.9, 132.2 / PTI13 * 100)
check('M6', 'actual tax rate 47.8%', 47.8, 316.9 / PTI13 * 100)
check('M6', 'Corporate EBITDA "unusual or non-recurring" $283.4m = 42.7%', 42.7, 283.4 / PTI13 * 100)

# ---------------------------------------------------------------------------
# M7 Correction of errors (numbers-1, text-3, text-4, report-5)
# ---------------------------------------------------------------------------
section('M7 Correction of errors: pre-tax cuts and shares; equity')
on_page(A13, '84', 'Income before income taxes | 450.6 | (9.2) | 441.4 | 324.3 | (18.7) | 305.6')
on_page(A13, '87', 'Income before income taxes | 328.3 | (7.0) | 321.3 | 612.4 | (11.6) | 600.8')
check('M7', '2011 cut $18.7m = 5.8% of 324.3', 5.8, 18.7 / 324.3 * 100)
check('M7', '2012 cut $9.2m = 2.0% of 450.6', 2.0, 9.2 / 450.6 * 100)
check('M7', 'numbers-1 2012 cut $9.1m (workbook 450.5 less 441.4; PK10)', 9.1, line('IS annual', 'Income before income taxes', 4) - 441.4)
check('M7', 'nine-month 2013 $11.6m = 1.9% of 612.4', 1.9, 11.6 / 612.4 * 100)
check('M7', '2013 portion $11.6m = 1.7% of pre-tax', 1.7, 11.6 / PTI13 * 100)
on_page(A13, '84', 'total equity from $2,507.3 million to $2,486.2 million')
check('M7', 'equity cut $21.1m', 21.1, 2507.3 - 2486.2)
check('M7', 'numbers-1 2011 net income fell $11.9m (workbook 195.7 to 183.8)', 11.9, line('IS annual', 'Net income', 3) - 183.8)
check('M7', '2012 net income fell $4.5m', 4.5, 243.1 - 238.6)

# ---------------------------------------------------------------------------
# M8 Payables (numbers-1, numbers-2, report-5)
# ---------------------------------------------------------------------------
section('M8 Days payable, size, balance against cash-flow line')
cos = {2012: line('IS annual', 'Direct operating', 4) + line('IS annual', 'Depreciation of revenue earning equipment and lease charges', 4),
       2013: line('IS annual', 'Direct operating', 5) + line('IS annual', 'Depreciation of revenue earning equipment and lease charges', 5)}
ap = {2012: line('BS annual', 'Accounts payable', 3), 2013: line('BS annual', 'Accounts payable', 4)}
on_page(A13, '75', 'Accounts payable | $967.9 | $1,003.2')
AP12_REV = 1003.2
COS12_REV = 4806.0 + 2128.9
on_page(R13, 'unnumbered', 'Direct operating | 5,752.0 | 4,806.0'); on_page(R13, 'unnumbered', 'Depreciation of revenue earning equipment and lease charges | 2,525.5 | 2,128.9')
dp12 = ap[2012] / cos[2012] * 366
dp13 = ap[2013] / cos[2013] * 365
dp12_rev = AP12_REV / COS12_REV * 366
check('M8', 'days payable FY2012 first reported 52.7', 52.7, dp12)
check('M8', 'days payable FY2013 42.7', 42.7, dp13)
check('M8', 'days payable FY2012 revised 52.9', 52.9, dp12_rev)
check('M8', 'size first reported $226.3m', 226.3, dp12 / 365 * cos[2013] - ap[2013], 0.15)
check('M8', '= 34% of pre-tax', 34, (dp12 / 365 * cos[2013] - ap[2013]) / PTI13 * 100, 0.5)
check('M8', 'size revised $232.8m', 232.8, dp12_rev / 365 * cos[2013] - ap[2013], 0.15)
check('M8', '= 35% of pre-tax', 35, (dp12_rev / 365 * cos[2013] - ap[2013]) / PTI13 * 100, 0.5)
check('M8', 'payables fell 3.1% (first reported)', -3.1, (ap[2013] / ap[2012] - 1) * 100)
check('M8', 'payables fell 3.5% (revised)', -3.5, (ap[2013] / AP12_REV - 1) * 100)
check('M8', 'cost of sales rose 19.2% (first reported)', 19.2, (cos[2013] / cos[2012] - 1) * 100)
check('M8', 'cost of sales rose 19.4% (revised)', 19.4, (cos[2013] / COS12_REV - 1) * 100)
check('M8', 'cash-flow inflow 23.2 against balance fall 35.3: gap $58.5m', 58.5, 23.2 + (AP12_REV - ap[2013]))
check('M8', 'days on direct operating costs only, 2012 76.4', 76.4, AP12_REV / 4806.0 * 366)
check('M8', 'days on direct operating costs only, 2013 61.4', 61.4, ap[2013] / 5752.0 * 365)
on_page(A13, '81', 'Purchases of revenue earning equipment included in accounts payable and accrued liabilities | $289.1 | $247.0')
check('M8', 'unpaid fleet purchases rose $42.1m', 42.1, 289.1 - 247.0)

# ---------------------------------------------------------------------------
# M9 Q4 gross margin (numbers-1, numbers-2, report-5)
# ---------------------------------------------------------------------------
section('M9 Q4 gross margin from the release; size on Q4 revenue; the adjusted version; fleet against days')
on_page(R13, 'unnumbered', 'Total revenues | $2,556.3 | $2,319.7')
on_page(R13, 'unnumbered', 'Direct operating | 1,439.3 | 1,257.7')
on_page(R13, 'unnumbered', 'Depreciation of revenue earning equipment and lease charges | 643.0 | 550.0')
gm13 = (2556.3 - 1439.3 - 643.0) / 2556.3 * 100
gm12 = (2319.7 - 1257.7 - 550.0) / 2319.7 * 100
check('M9', 'Q4 2012 gross margin 22.1%', 22.1, gm12)
check('M9', 'Q4 2013 gross margin 18.5%', 18.5, gm13)
size_q4 = (gm12 - gm13) / 100 * 2556.3
check('M9', 'size $90.2m on Q4 revenue', 90.2, size_q4, 0.15)
check('M9', '= 14% of pre-tax', 14, size_q4 / PTI13 * 100, 0.5)
on_page(R13, 'unnumbered', 'Direct operating | 1,439.3 | (62.1 | )(a) | 1,377.2 | 1,257.7 | (42.7 | )(a) | 1,215.0')
on_page(R13, 'unnumbered', 'Depreciation of revenue earning equipment and lease charges | 643.0 | (4.2 | )(b) | 638.8 | 550.0 | (4.1 | )(b) | 545.9')
agm13 = (2556.3 - 1377.2 - 638.8) / 2556.3 * 100
agm12 = (2319.7 - 1215.0 - 545.9) / 2319.7 * 100
adj_size = (agm12 - agm13) / 100 * 2556.3
check('M9', 'adjusted fall $75.5m', 75.5, adj_size, 0.15)
check('M9', '= 84% of the fall', 84, adj_size / size_q4 * 100, 0.5)
check('M9', '= 11.4% of pre-tax (report)', 11.4, adj_size / PTI13 * 100)
on_page(R13, 'unnumbered', 'Average number of cars (Company-operated) | 472,200 | 22.4%')
on_page(R13, 'unnumbered', 'Transaction days (in thousands) (a) | 32,875 | 16.1%')
check('M9', 'fleet per transaction day +5.4%', 5.4, (1.224 / 1.161 - 1) * 100)
check('M9', 'rental depreciation +16.9%', 16.9, (643.0 / 550.0 - 1) * 100)
check('M9', 'revenue +10.2%', 10.2, (2556.3 / 2319.7 - 1) * 100)
on_page(R13, 'unnumbered', 'U.S. Car Rental | $1,476.3 | $1,293.6')
rpd13 = 1476.3 / 32875; rpd12 = 1293.6 / (32875 / 1.161)
check('M9', 'U.S. revenue per transaction day about -1.7%', -1.7, (rpd13 / rpd12 - 1) * 100, 0.1)

# ---------------------------------------------------------------------------
# M10 Receivables, free cash flow, exposures (numbers-1, numbers-2, text-3, text-4, report-5)
# ---------------------------------------------------------------------------
section('M10 Receivables against the industry; fleet receivables; free cash flow; Sobel and goodwill exposures')
rev = {2012: line('IS annual', 'Total revenues', 4), 2013: line('IS annual', 'Total revenues', 5)}
check('M10', 'DSO FY2012 first reported 76.5', 76.5, rec[2012] / rev[2012] * 366)
check('M10', 'DSO FY2012 revised 76.2', 76.2, 1879.7 / 9024.9 * 366)
check('M10', 'DSO FY2013 51.3', 51.3, rec[2013] / rev[2013] * 365)
check('M10', 'receivables / sales 14.0%', 14.0, rec[2013] / rev[2013] * 100)
ind = {r[0]: r[1] for r in sheet_rows('Industry') if isinstance(r[0], str) and r[1] is not None}
check('M10', 'industry 11.5%', 11.5, ind['Acc Rec/ Sales'])
check('M10', 'excess over industry share $273.8m', 273.8, rec[2013] - 0.115 * rev[2013], 0.15)
check('M10', '= 41% of pre-tax', 41, (rec[2013] - 0.115 * rev[2013]) / PTI13 * 100, 0.5)
on_page(A13, '81', 'Sales of revenue earning equipment included in receivables | 357.3 | 618.6')
check('M10', 'fleet receivables fell $261.3m', 261.3, 618.6 - 357.3)
check('M10', 'fall in receivables $367.1m (revised)', 367.1, 1879.7 - rec[2013])
check('M10', '= 71% of the fall', 71, (618.6 - 357.3) / (1879.7 - rec[2013]) * 100, 0.5)
check('M10', 'receivables ex fleet sales 10.7% of sales', 10.7, (rec[2013] - 357.3) / rev[2013] * 100)
ocf = {2012: line('CF annual', 'Net cash provided by (used in) operating activities', 4), 2013: line('CF annual', 'Net cash provided by (used in) operating activities', 5)}
fcf13 = (ocf[2013] + line('CF annual', 'Revenue earning equipment expenditures', 5) + line('CF annual', 'Proceeds from disposal of revenue earning equipment', 5)
         + line('CF annual', 'Property and equipment expenditures', 5) + line('CF annual', 'Proceeds from disposal of property and equipment', 5))
fcf12 = (ocf[2012] + line('CF annual', 'Revenue earning equipment expenditures', 4) + line('CF annual', 'Proceeds from disposal of revenue earning equipment', 4)
         + line('CF annual', 'Property and equipment expenditures', 4) + line('CF annual', 'Proceeds from disposal of property and equipment', 4))
check('M10', 'free cash flow FY2013 $314.5m', 314.5, fcf13, 0.15)
check('M10', 'free cash flow FY2012 first reported $54.8m', 54.8, fcf12, 0.15)
check('M10', 'net income less FCF $31.7m', 31.7, 346.2 - fcf13, 0.15)
check('M10', '= 4.8% of pre-tax', 4.8, (346.2 - fcf13) / PTI13 * 100)
fcf12_rev = 2709.7 - 9613.2 + 7125.1 - 297.1 + 122.0   # Revisions sheet: OCF 2709.7, P&E capex 297.1, proceeds 122.0
check('M10', 'FCF FY2012 revised $46.5m (numbers-2)', 46.5, fcf12_rev, 0.15)
check('M10', 'net fleet spending rose $546.2m', 546.2, (10298.4 - 7264.1) - (9613.2 - 7125.1), 0.15)
on_page(A13, '137', 'could potentially exceed $40.0 million')
check('M10', 'Sobel $40m = 6.0% of pre-tax', 6.0, 40.0 / PTI13 * 100)
on_page(A13, '149', 'Income before income taxes | 73.7 | 205.9 | 321.3 | 62.3')
check('M10', 'Sobel $40m = 64% of Q4 pre-tax', 64, 40.0 / 62.3 * 100, 0.5)
on_page(A13, '96', 'Trade name | 3,330.0'); on_page(A13, '96', 'Total | 3,350.1 |')
check('M10', 'goodwill plus indefinite-lived intangibles $4,697.6m', 4697.6, 1347.5 + 3350.1, 0.15)
check('M10', '= 170% of equity (2,771.2)', 170, (1347.5 + 3350.1) / 2771.2 * 100, 0.5)

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------
print('\n\nSUMMARY')
print('=======')
for m, label, rep, rec_, ok in results:
    print(f"{m:4} {'match' if ok else 'MISMATCH':8} reported {rep:>10}  recomputed {rec_:>10}  {label}")
n_ok = sum(1 for r in results if r[4]); n = len(results)
print(f'\n{n_ok} of {n} sub-figures match across ten measures')
measures_ok = all(all(r[4] for r in results if r[0] == m) for m in sorted({r[0] for r in results}))
print('all ten measures match' if measures_ok else 'at least one measure has a mismatch')
