# Working-capital analysis: Under Armour, statements.xlsx + FY2015 and FY2016 annual reports
import calendar, datetime as dt, re, os, sys
import openpyxl
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)
wb = openpyxl.load_workbook(os.path.join(BASE, "statements.xlsx"), data_only=True)

def sheet(name):
    rows = list(wb[name].iter_rows(values_only=True))
    hdr = rows[0]
    ends = [dt.date.fromisoformat(re.search(r"ended (\d{4}-\d{2}-\d{2})", h).group(1)) for h in hdr[1:-1]]
    data = {}
    for r in rows[1:]:
        if r[0] and r[0] not in data:
            data[r[0]] = dict(zip(ends, r[1:-1]))
    return data

isa, bsa = sheet("IS annual"), sheet("BS annual")
isq, bsq = sheet("IS quarterly"), sheet("BS quarterly")
REV, COGS, AR, INV, AP = "Net revenues", "Cost of goods sold", "Accounts receivable, net", "Inventories", "Accounts payable"

def year_days(d): return 366 if calendar.isleap(d.year) else 365
def quarter_days(d):
    start_month = d.month - 2
    return (d - dt.date(d.year, start_month, 1)).days + 1
def prior(d):  # same period end a year earlier
    return dt.date(d.year - 1, d.month, d.day)
def g(series, d):
    p = prior(d)
    if p not in series or series[p] in (None, 0) or series.get(d) is None: return None
    return series[d] / series[p] - 1

def measures(i_s, b_s, daysfn):
    out = {}
    for d in sorted(b_s[AR]):
        if d not in i_s[REV]: continue
        n = daysfn(d)
        m = {"days": n,
             "DSO": b_s[AR][d] / i_s[REV][d] * n,
             "DIO": b_s[INV][d] / i_s[COGS][d] * n,
             "DPO": b_s[AP][d] / i_s[COGS][d] * n}
        gr = {k: g(s, d) for k, s in [("rev", i_s[REV]), ("cogs", i_s[COGS]), ("ar", b_s[AR]), ("inv", b_s[INV]), ("ap", b_s[AP])]}
        m.update({"g_" + k: v for k, v in gr.items()})
        if None not in gr.values():
            m["gap_ar"] = gr["ar"] - gr["rev"]; m["gap_inv"] = gr["inv"] - gr["cogs"]; m["gap_ap"] = gr["ap"] - gr["cogs"]
        out[d] = m
    return out

ann = measures(isa, bsa, year_days)
qtr = measures(isq, bsq, quarter_days)

# Reserves netted against receivables, USD millions, from the annual reports
# FY2015 report p. 37 / p. 50 / p. 52 (2015, 2014); FY2016 report p. 41 / p. 55 / p. 57 (2016, 2015)
allow = {2014: 3.7, 2015: 5.9, 2016: 11.3}
returns = {2014: 68.9, 2015: 94.5, 2016: 146.2}
res = {}
for y in allow:
    d = dt.date(y, 12, 31)
    net, rev = bsa[AR][d], isa[REV][d]
    gross = net + allow[y] + returns[y]
    res[y] = dict(gross=gross, allow_gross=allow[y] / gross, allow_rev=allow[y] / rev,
                  ret_gross=returns[y] / gross, ret_rev=returns[y] / rev,
                  dso_gross=gross / rev * year_days(d))

def p(x, f="{:.1f}"): return "n/a" if x is None else f.format(x)
print("ANNUAL")
for d, m in ann.items():
    print(d, m["days"], "DSO", p(m["DSO"]), "DIO", p(m["DIO"]), "DPO", p(m["DPO"]),
          "| growth rev/cogs/ar/inv/ap", *[p(m.get("g_" + k) and m["g_" + k] * 100) for k in ("rev", "cogs", "ar", "inv", "ap")],
          "| gaps", *[p(m.get(k) is not None and m[k] * 100 or m.get(k)) for k in ("gap_ar", "gap_inv", "gap_ap")])
print("QUARTERLY")
for d, m in qtr.items():
    print(d, m["days"], "DSO", p(m["DSO"]), "DIO", p(m["DIO"]), "DPO", p(m["DPO"]),
          "| growth rev/cogs/ar/inv/ap", *[p(m["g_" + k] * 100) if m.get("g_" + k) is not None else "n/a" for k in ("rev", "cogs", "ar", "inv", "ap")],
          "| gaps", *[p(m[k] * 100) if k in m else "n/a" for k in ("gap_ar", "gap_inv", "gap_ap")])
print("RESERVES")
for y, r in res.items():
    print(y, "gross", p(r["gross"]), "allow %gross", p(r["allow_gross"] * 100, "{:.2f}"), "%rev", p(r["allow_rev"] * 100, "{:.2f}"),
          "returns %gross", p(r["ret_gross"] * 100), "%rev", p(r["ret_rev"] * 100, "{:.2f}"), "DSO on gross", p(r["dso_gross"]))
for y in (2015, 2016):
    print(y, "reserve growth: allowance", p((allow[y] / allow[y - 1] - 1) * 100), "returns", p((returns[y] / returns[y - 1] - 1) * 100),
          "gross AR", p((res[y]["gross"] / res[y - 1]["gross"] - 1) * 100))
# Other items used in the reply
print("Sports Authority receivable 32.5 as % of net AR FY2015:", p(32.5 / bsa[AR][dt.date(2015, 12, 31)] * 100))
print("Product purchase obligations 2015 -> 2016:", p((684.511 / 1537.915 - 1) * 100), "%")
print("AP + purchase obligations:", p(200.5 + 1537.9), p(409.7 + 684.5))
print("Q4 gross margin:", {d.year: p((isq[REV][d] - isq[COGS][d]) / isq[REV][d] * 100) for d in isq[REV] if d.month == 12})
print("Inventory obsolescence deferred tax asset growth 2016:", p((15.479 / 11.956 - 1) * 100), "2015:", p((11.956 / 8.198 - 1) * 100))
cfa = sheet("CF annual")
print("Changes in reserves and allowances (CF annual):", cfa["Changes in reserves and allowances"])
print("Operating cash flow:", cfa["Net cash provided by (used in) operating activities"], "AP line:", cfa["Accounts payable"])
cfq = sheet("CF quarterly")
print("CF quarterly AP:", {str(d): v for d, v in cfq["Accounts payable"].items() if d.year >= 2015})

# Chart: quarterly year-over-year growth, balance vs flow
qs = [d for d in qtr if "gap_ar" in qtr[d]]
labels = [f"Q{(d.month) // 3} {d.year}" for d in qs]
fig, axes = plt.subplots(1, 3, figsize=(15, 5), dpi=100)
for ax, (title, bk, fk, bl, fl) in zip(axes, [
        ("Receivables", "g_ar", "g_rev", "Accounts receivable, net", "Net revenues"),
        ("Inventory", "g_inv", "g_cogs", "Inventories", "Cost of goods sold"),
        ("Payables", "g_ap", "g_cogs", "Accounts payable", "Cost of goods sold")]):
    ax.plot(labels, [qtr[d][bk] * 100 for d in qs], marker="o", label=bl)
    ax.plot(labels, [qtr[d][fk] * 100 for d in qs], marker="s", label=fl)
    ax.axhline(0, color="grey", linewidth=0.8)
    ax.set_title(f"{title}: year-over-year growth by quarter")
    ax.set_ylabel("Growth vs same quarter a year earlier (%)")
    ax.tick_params(axis="x", rotation=45)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.28), ncol=2, frameon=False)
fig.tight_layout()
fig.savefig(os.path.join(HERE, "prompt-1-v1.3-chart.png"), facecolor="white")
print("chart saved")

# Quotation check: every quoted passage in the reply must be an exact substring of the cited report,
# and the nearest [p. N] marker above it must match the cited page.
REPORTS = {"FY2015": os.path.join(BASE, "annual-report-FY2015-12-31-key-sections.txt"),
           "FY2016": os.path.join(BASE, "annual-report-FY2016-12-31-key-sections.txt")}
QUOTES = [
 ("FY2016", 37, "primarily due to the timing of shipments and a higher proportion of sales to our international customers with longer payment terms"),
 ("FY2015", 33, "primarily due to the timing of shipments."),
 ("FY2016", 37, "primarily due to the timing of inventory payments as well as significant increases in inventory in-transit in the current period"),
 ("FY2016", 31, "$15.2 million in bad debt expense"),
 ("FY2016", 29, "a $2.9 million adjustment related to a return credit for footwear"),
 ("FY2015", 37, "we do not currently believe that the exposure to our receivables as of December 31, 2015 is materially impacted"),
 ("FY2016", 41, "are recorded as an offset to accounts receivable"),
 ("FY2015", 33, "early deliveries of product to meet key seasonal floor set dates, as well as strategic investments in auto-replenishment products"),
 ("FY2016", 30, "increased liquidation and discounting"),
 ("FY2016", 36, "as a change in estimate, we reversed $48.0 million of incentive compensation accruals"),
 ("FY2016", 27, "our growth was challenged due to the disruption of the North American retail environment"),
 ("FY2016", 37, "significant increases in inventory in-transit"),
]
def check_quotes(reply_text=None):
    ok = True
    for doc, page, q in QUOTES:
        t = open(REPORTS[doc], encoding="utf-8").read()
        hits = [m.start() for m in re.finditer(re.escape(q), t)]
        pages = [int(re.findall(r"\[p\. (\d+)\]", t[:h])[-1]) for h in hits]
        good = page in pages
        inreply = (reply_text is None) or (q in reply_text)
        ok &= good and inreply
        print("OK " if good and inreply else "FAIL", doc, "p.", page, "found on pages", pages, "| in reply:", inreply, "|", q[:60])
    if reply_text is not None:
        quoted = re.findall(r'"([^"]+)"', reply_text)
        listed = {q for _, _, q in QUOTES}
        labels = {"Accounts receivable, net", "Net revenues", "Accounts payable", "Cost of goods sold", "Inventories",
                  "Purchase of businesses, net of cash acquired", "Accrued expenses", "Changes in reserves and allowances",
                  "Gross profit", "Other assets acquired", "Product purchase obligations", "Inventory obsolescence reserves"}
        for q in quoted:
            if q not in listed and q not in labels:
                ok = False; print("UNLISTED QUOTE:", q)
    print("ALL QUOTES VERIFIED" if ok else "QUOTE CHECK FAILED")
    return ok
reply_path = os.path.join(HERE, "prompt-1-v1.3-reply.md")
if os.path.exists(reply_path):
    rt = open(reply_path, encoding="utf-8").read()
    check_quotes(rt)
    # flags table: no cell over 40 words
    for line in rt.split(chr(10)):
        if line.startswith("| **"):
            print("cell word counts:", [len(c.split()) for c in line.strip("|").split("|")])
    print("reply word count:", len(rt.split()))
else:
    check_quotes()
