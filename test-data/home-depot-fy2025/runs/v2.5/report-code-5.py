# Turn 3 (prompt 5: report). Checks on the report: quotations, size shares, and that no other number is new.
# Run from the company folder:  python runs/v2.5/report-code-5.py [path to report, default runs/v2.5/report-5.md]
import re, sys, openpyxl
sys.stdout.reconfigure(encoding="utf-8")
F26 = "annual-report-FY2026-02-01-key-sections.txt"
F25 = "annual-report-FY2025-02-02-key-sections.txt"
T = {"26": open(F26, encoding="utf-8").read(), "25": open(F25, encoding="utf-8").read()}
REPLIES = {n: open(f"runs/v2.5/{n}.md", encoding="utf-8").read() for n in ("text-3", "text-4", "numbers-1", "numbers-2")}
report = open(sys.argv[1] if len(sys.argv) > 1 else "runs/v2.5/report-5.md", encoding="utf-8").read()

wb = openpyxl.load_workbook("statements.xlsx", data_only=True)
def sheet(name):
    rows = list(wb[name].iter_rows(values_only=True)); hdr = rows[0]
    return {r[0]: dict(zip(hdr[1:], r[1:])) for r in rows[1:] if r[0]}
IS, BS = sheet("IS annual"), sheet("BS annual")
Y25, Y24 = "FY (ended 2026-02-01)", "FY (ended 2025-02-02)"
PRETAX = IS["Earnings before provision for income taxes"][Y25]
print("base: latest year's pre-tax income", PRETAX)

# ---------- 1. sizes: (item, amount in $M, kind of amount, share as written in the report) ----------
ltd = lambda y: BS["Current installments of long-term debt"][y] + BS["Long-term debt, excluding current installments"][y]
borrow_change = ltd(Y25) + BS["Short-term debt"][Y25] - ltd(Y24) - BS["Short-term debt"][Y24]
SIZES = [
    ("1 Store-business costs", 21313 - 20574, "fall in Primary operating income: effect on reported income", "4.0%"),
    ("2 Goodwill in Other (SRS and GMS)", 13780, "balance at risk: possible future loss, not an income effect", "74.1%"),
    ("2 Amortization left out of adjusted EPS", 607, "gap between adjusted and reported figures", "3.3%"),
    ("3 Long-term debt plus commercial paper, change", borrow_change, "balance-sheet movement", "12.8%"),
    ("4 Inventory built", 1498, "balance-sheet movement (cash-flow line)", "8.1%"),
    ("4 Shrink sensitivity", 79, "company-stated effect of a 10% change in the shrink rate", "0.4%"),
    ("5 1% of customer receivables", 26, "possible future loss (illustrative)", "0.1%"),
]
ok_sizes = True
for item, amt, kind, written in SIZES:
    share = f"{amt / PRETAX * 100:.1f}%"
    good = share == written and written in report
    ok_sizes &= good
    print("OK  " if good else "FAIL", item, "| amount", amt, "| share", share, "| written", written, "|", kind)
assert borrow_change == 2389
print("ALL SIZES OK" if ok_sizes else "SIZE CHECK FAILED")

# ---------- 2. quotations: exact substring of the cited file, on the cited page ----------
def page_of(t, pos):
    p = re.findall(r"\[p\. (\d+)\]", t[:pos]); return int(p[-1]) if p else None
CITES = [
    ("non-recurring", "26", 34), ("lower legal-related benefits", "25", 34),
    ("exceeded", "26", 60), ("substantially exceeded", "26", 60),
    ("as we seek to reduce our outstanding debt", "26", 35),
    ("higher average inventory levels", "26", 32),
    ("not material", "26", 48), ("increasingly use trade credit", "26", 24),
]
found = re.findall(r'"([^"]+)"', report)
missing = [q for q in found if q not in [c[0] for c in CITES]]
ok_q = not missing
print("\nquotations in report:", len(found), "| distinct:", len(set(found)), "| without a citation record:", missing)
for qt, f, pg in CITES:
    pages = sorted({page_of(T[f], m.start()) for m in re.finditer(re.escape(qt), T[f])})
    good = pg in pages and qt in report
    ok_q &= good
    print("OK  " if good else "FAIL", "FY20" + f, "p.", pg, "found on", pages, "|", qt)
print("ALL QUOTES OK" if ok_q else "QUOTE CHECK FAILED")

# page references that carry no quotation: (file, page, text that must sit on that page)
REFS = [("26", 55, "Net sales | $151,966 | $153,108"), ("26", 55, "Operating income | 20,574 | 316 | 20,890"), 
        ("26", 41, "Sufficiency of audit evidence over certain merchandise inventories"), ("25", 42, "Estimation of store shrink"), ("26", 35, "ROIC | 25.7%"), ("25", 61, "Average daily short-term borrowings"),
        ("26", 61, "maximum amount outstanding during that period was $5.8 billion"), ("26", 39, "approximately $79 million"), ("25", 39, "approximately $95 million"),
        ("26", 42, "We identified the sufficiency of audit evidence"), ("26", 48, "Customer receivables | 2,588"), ("26", 24, "increasingly use trade credit")]
ok_r = True
for f, pg, s in REFS:
    pages = sorted({page_of(T[f], m.start()) for m in re.finditer(re.escape(s), T[f])})
    ok_r &= pg in pages
    print("OK  " if pg in pages else "FAIL", "FY20" + f, "p.", pg, pages, "|", s)
print("ALL PAGE REFERENCES OK" if ok_r else "PAGE REFERENCE CHECK FAILED")

# ---------- 3. no other number is new ----------
def nums(text):
    out = set()
    for m in re.finditer(r"(?<![\w.])\$?\(?(\d[\d,]*\.?\d*)", text):
        out.add(m.group(1).replace(",", "").rstrip("."))
    return out
in_replies = set().union(*(nums(v) for v in REPLIES.values()))
in_docs = nums(T["26"]) | nums(T["25"])
for ws in wb:
    for row in ws.iter_rows(values_only=True):
        for c in row:
            if isinstance(c, (int, float)): in_docs.add(str(c).rstrip("0").rstrip(".") if isinstance(c, float) else str(c))
shares = {s[3].rstrip("%") for s in SIZES}
structural = {"1", "2", "3", "4", "5"}           # item numbers
body = re.sub(r"\(?(?:FY20\d\d )?pp?\. [\d, \-and]+\)?", " ", report)   # page references are checked above, not here
new, docs_only = [], []
for n in sorted(nums(body), key=lambda x: float(x)):
    if n in in_replies or n in structural: continue
    if n in shares: continue
    (docs_only if n in in_docs else new).append(n)
print("\nnumbers in report:", len(nums(body)), "| size shares (the permitted new numbers):", sorted(shares))
print("in the attached documents but in no earlier reply:", docs_only)
print("new (in neither):", new)
print("NO NEW NUMBERS" if not new else "NEW NUMBERS FOUND")
print("\nwords:", len(re.findall(r"\S+", report)), "| em-dash:", "—" in report, "| banned words:", [w for w in ("fraud", "manipulat", "red flag") if w in report.lower()])
