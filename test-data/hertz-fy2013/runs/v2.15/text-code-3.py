# Step 3, read the footnotes: Hertz Global Holdings, FY2013 annual report.
# Every number in the reply is computed here; every quotation is checked against the file and page.
import re, os, openpyxl

BASE = r"C:\Users\aaron\OneDrive\Desktop\Master\WireSift Research\Events\CFA Vancouver Forensic\test-data\hertz-fy2013"
R13 = os.path.join(BASE, "annual-report-FY2013-12-31-key-sections.txt")
XLS = os.path.join(BASE, "statements.xlsx")
OUT = os.path.join(BASE, "runs", "v2.15", "text-3.md")

txt = open(R13, encoding="utf-8").read()
marks = [(m.start(), int(m.group(1))) for m in re.finditer(r"\[p\. (\d+)\]", txt)]

def pages_of(q):
    out, i = [], txt.find(q)
    while i != -1:
        p = None
        for pos, n in marks:
            if pos <= i: p = n
            else: break
        out.append(p); i = txt.find(q, i + 1)
    return out

# ---------- figures from the statements workbook (FY2013 column, as reported) ----------
wb = openpyxl.load_workbook(XLS, data_only=True)
def sheet(name):
    ws = wb[name]; rows = list(ws.iter_rows(values_only=True)); hdr = rows[0]
    col = [i for i, h in enumerate(hdr) if h and "2013-12-31" in str(h)][0]
    return {r[0]: r[col] for r in rows[1:] if r[0]}
IS, BS, CF = sheet("IS annual"), sheet("BS annual"), sheet("CF annual")
pretax = IS["Income before income taxes"]                     # 663.1
revenue = IS["Total revenues"]                                # 10,771.9
recv = [v for k, v in BS.items() if k.startswith("Receivables")][0]   # 1,512.6
equity = BS["Total equity"]                                   # 2,771.2
goodwill = BS["Goodwill"]                                     # 1,347.5
pldp = BS["Public liability and property damage"]             # 347.7
cf_provision = CF["Provision for losses on doubtful accounts"]        # 45.9
assert abs(pretax - 663.1) < 0.05 and abs(revenue - 10771.9) < 0.05

# ---------- figures from the notes (page in comment); each is asserted to be in the text ----------
def need(s, page):
    assert page in pages_of(s), (s, page, pages_of(s))
need("Year ended December 31, 2013 | $29.3 | $41.9 | $(0.1) | $(40.3) | (a) | $30.8", 158)
allow_end, writeoffs, sched_provision = 30.8, 40.3, 41.9
need("Trade name | 3,330.0 | \u2014 | 3,330.0", 96); tradename = 3330.0
need("net losses of $48.2 million, and net gains of $100.6 million", 126)
rate_cut, us_loss_13, us_gain_12 = 44.2, 48.2, 100.6
need("Average number of cars (Company-operated) | 468,500 | 358,000 | 321,700", 49)
need("Average number of cars (Leased) | 21,500 | 1,100", 49)
need("U.S. car rental | $1,269.3 | $940.6 | $971.7", 131)
us_dep = {2013: 1269.3, 2012: 940.6}; cars = {2013: 468500, 2012: 358000}; leased = {2013: 21500, 2012: 1100}
need("Restructuring charges | (77.0) | (38.0) | (56.4)", 50)
need("Restructuring related charges(4) | (21.8) | (11.1) | (9.8)", 50)
need("we incurred $645.4 million", 140)
adj = {"purchase accounting": 132.2, "debt-related": 68.4, "restructuring": 77.0, "restructuring related": 21.8,
       "derivative": 1.0, "acquisition": 18.5, "integration": 40.0, "relocation": 7.8, "debt premiums": 28.7,
       "impairment and other": 44.0, "other": 50.7}
seg_total, other_recon = 1581.7, 428.5
need("Total reportable segments | 1,581.7 | 1,239.5 | 995.1", 50)
need("totaling $46.3 million, of which $34.7 million", 83)
err_total, err_prior = 46.3, 34.7
need("Income before income taxes | 450.6 | (9.2) | 441.4 | 324.3 | (18.7) | 305.6", 84)
need("Income before income taxes | 328.3 | (7.0) | 321.3 | 612.4 | (11.6) | 600.8", 87)
need("Operating leases and concession agreements(3) | 2,727.7", 70)
need("Purchase obligations(5) | 4,757.6", 70)
need("dividended $467.2 million", 106)
need("$3.1 million for the executive officers", 147)
need("Impairment charges and other | 40.0", 80)
need("fair value of debt securities was $151.0 million", 145)

# ---------- calculations ----------
pct = lambda x: 100 * x / pretax
c = {}
c["allow_cover"] = allow_end / writeoffs
c["recv_days"] = recv / revenue * 365
c["intang"] = goodwill + tradename
c["intang_eq"] = 100 * c["intang"] / equity
rents = [141.3, 116.9, 88.9, 66.8, 46.5, 195.7]; conc = [407.9, 310.3, 249.1, 188.9, 152.0, 685.6]; eq_l = [52.6, 16.0, 8.0, 1.2]
c["lease_sum"] = sum(rents) + sum(conc) + sum(eq_l)
assert abs(c["lease_sum"] - 2727.7) < 0.05                    # Note 10 schedules add up to the Item 7 table
assert abs(23.2 * 20.14 - 467.2) < 0.2                        # buy-back of Sponsor shares
c["sobel"] = pct(40.0)
c["restr"] = adj["restructuring"] + adj["restructuring related"]
c["adj_total"] = sum(adj.values())
assert abs((seg_total - other_recon - pretax) - c["adj_total"]) < 0.05
c["dep_co"] = {y: us_dep[y] * 1e6 / cars[y] / 12 for y in us_dep}
c["dep_all"] = {y: us_dep[y] * 1e6 / (cars[y] + leased[y]) / 12 for y in us_dep}
c["dep_co_chg"] = 100 * (c["dep_co"][2013] / c["dep_co"][2012] - 1)
c["dep_all_chg"] = 100 * (c["dep_all"][2013] / c["dep_all"][2012] - 1)
c["dep_pair"] = rate_cut + us_loss_13
e12, e11 = 9.2, 18.7
e_pre = 4.4 + 2.4                                             # 2010: Brazil and other (p. 83)
assert abs(e12 + e11 + e_pre - err_prior) < 0.05
assert abs((12.9 + 2.4) + (4.4 + 6.2 + 3.6) + (2.4 + 3.2 - 0.4) - err_prior) < 0.05
e13 = err_total - err_prior
assert abs(e13 - 11.6) < 0.05
c["e11_pct"] = 100 * e11 / 324.3
c["prov_gap"] = cf_provision - sched_provision
assert abs(c["prov_gap"] - (44.0 - 40.0)) < 0.05

# keyword check for areas the documents may not cover (whole file)
low = txt.lower()
absent = {k: (k not in low) for k in ["unbilled", "factoring", "supplier finance", "critical audit matter", "bill-and-hold", "warranty reserve"]}
has_item13 = "=== Item 13 ===" in txt

# ---------- quotations: (text, cited page) ----------
Q = {
 "rev": ("recognized over the period the revenue earning equipment is rented", 90),
 "res": ("relatively minor adjustments to our recorded liability", 45),
 "cap": ("net decreases of $44.2 million", 126),
 "imp": ("no impairment existed", 94),
 "obs": ("minimum non-cancelable terms", 70),
 "rel": ("none of our outstanding debt at December 31, 2013 was with related parties", 148),
 "con": ("could potentially exceed $40.0 million", 137),
 "aud": ("effective internal control over financial reporting", 74),
 "adj": ("certain one-time charges and nonoperational items", 50),
 "reloc": ("$40 million to $45 million", 65),
 "ind": ("indicative of the residual values experienced in the U.S.", 126),
 "decl": ("declining residual values", 126),
 "mon": ("monthly per vehicle depreciation costs decreased", 42),
 "aud2": ("maintained, in all material respects, effective internal control over financial reporting", 74),
 "mat": ("correcting these errors in the fourth quarter would have been material to the fourth quarter", 83),
 "unk": ("unknowingly not met", 108),
 "notmat": ("will not be material", 137),
 "unspec": ("an unspecified amount", 138),
 "io": ("Impairment charges and other", 50),
}
q = {k: v[0] for k, v in Q.items()}

f1 = lambda x: f"{x:,.1f}"
reply = f"""**1. Policy profile**

| Area | What the report says | Where it sits | Why |
|---|---|---|---|
| 1. Revenue recognition | "{q['rev']}" (p. 90) | Typical | Booked over the rental period, normal for a rental business (general practice). |
| 2. Reserves and allowances | "{q['res']}" (p. 45) | Can't tell | No roll-forward for the ${f1(pldp)}m self-insurance reserve, so the claim cannot be tested; the bad-debt allowance is {c['allow_cover']:.2f} of the year's write-offs. |
| 3. Capitalized costs and useful lives | U.S. rate changes gave "{q['cap']}" in depreciation (p. 126) | Leans aggressive | Rates were lowered in the year U.S. car disposals moved to a ${us_loss_13}m net loss. |
| 4. Impairment and goodwill | "{q['imp']}" (p. 94) | Can't tell | No headroom is given for goodwill and unamortized trade names of ${c['intang']:,.1f}m, {c['intang_eq']:.0f}% of equity. |
| 5. Off the balance sheet | Leases and concessions shown at "{q['obs']}" (p. 70) | Typical | Lease minimums (${f1(2727.7)}m) and purchase obligations (${f1(4757.6)}m) carry amounts; Note 10 adds up to the table. |
| 6. Related parties | "{q['rel']}" (p. 148) | Typical | The Sponsors sold out in 2013; what remains is small and disclosed. |
| 7. Contingencies | A judgment "{q['con']}" (p. 137) | Leans aggressive | A possible loss of {c['sobel']:.1f}% of pre-tax income is called not material and the amount accrued is not given. |
| 8. Auditor's report and controls | "{q['aud']}" (p. 74) | Leans aggressive | Clean opinion and no material weakness, in a year that corrected ${err_total}m of errors. |
| 9. Adjusted measures | Leaves out "{q['adj']}" (p. 50) | Leans aggressive | Restructuring is left out in all three years; exclusions total {pct(c['adj_total']):.1f}% of pre-tax income. |

**2. Full write-ups**

**Adjusted measures: costs called one-time recur every year**
- **The report says:** adjusted pre-tax income (company-wide) leaves out "{q['adj']}" (Item 7, footnote (c), p. 50).
- **Test:** the claim does not hold for restructuring, charged at $77.0m, $38.0m and $56.4m in 2013, 2012 and 2011 and $645.4m since 2007 (Note 14, p. 140). Size: restructuring and related charges of ${c['restr']:.1f}m are {pct(c['restr']):.1f}% of 2013 pre-tax income (${pretax:,.1f}m); all exclusions, ${c['adj_total']:.1f}m, are {pct(c['adj_total']):.1f}%.
- **Reading:** most likely the reporting stretched: a cost charged in every year shown is presented as outside operations. A year with no restructuring, integration or relocation charge would point to an ordinary reading.
- **Read next:** the 2014 quarterly reports; the report itself expects "{q['reloc']}" more of relocation cost (p. 65).

**Depreciation: U.S. rates cut while U.S. car sales turned to losses**
- **The report says:** rate cuts lowered U.S. depreciation by ${rate_cut}m and were "{q['ind']}" (Note 8, p. 126).
- **Test:** contradicted in the same note: U.S. vehicle disposals gave net losses of ${us_loss_13}m in 2013 after net gains of ${us_gain_12}m in 2012, from "{q['decl']}" (p. 126). The claim that U.S. "{q['mon']}" (p. 42) holds only if the {leased[2013]:,} leased cars are counted (${c['dep_all'][2013]:.0f} a month against ${c['dep_all'][2012]:.0f}, {c['dep_all_chg']:+.1f}%); on company-operated cars it rose {c['dep_co_chg']:.1f}% (${c['dep_co'][2013]:.0f} against ${c['dep_co'][2012]:.0f}). Size: ${rate_cut}m is {pct(rate_cut):.1f}% of pre-tax income, a change in estimate; with the disposal loss, {pct(c['dep_pair']):.1f}%.
- **Reading:** possibly the reporting stretched, since lower rates leave more book value to lose on sale when used-car prices fall. Disposal gains returning in 2014 with no rate increase would point to an ordinary reading.
- **Read next:** disposal gains or losses and rate changes by quarter in the 2014 reports.

**Controls: rated effective in a year that corrected ${err_total}m of errors**
- **The report says:** the company "{q['aud2']}" (auditor's report, p. 74).
- **Test:** hard to square with Note 2: ${err_total}m of errors found in the fourth quarter, ${err_prior}m from 2012 and earlier, where "{q['mat']}" (p. 83); a debt requirement was also "{q['unk']}" at year end (p. 108). The 2011 error is {c['e11_pct']:.1f}% of that year's pre-tax income as first reported, yet called not material. Size: ${err_total}m is {pct(err_total):.1f}% of 2013 pre-tax income, a net reduction of income from corrections.
- **Reading:** can't tell: prior years may be revised for immaterial errors without a material weakness (general practice), but errors in three areas across four years possibly mean controls were weaker than stated. A single cause since fixed would point to an ordinary reading.
- **Read next:** the first-quarter 2014 report, for further revisions or a changed controls conclusion.

**3. Also noted**
- The Nevada class action could bring a judgment over $40.0m, yet the report says the outcome "{q['notmat']}" and gives no accrual (p. 137).
- A shareholder class action filed in November 2013 over the company's 2013 disclosures seeks "{q['unspec']}" (p. 138).
- The bad-debt provision is ${cf_provision}m in the cash flow statement (p. 80) and ${sched_provision}m in Schedule II (p. 158); the ${c['prov_gap']:.1f}m gap is not explained, and matches the gap between the $40.0m vehicle impairment (p. 80) and the $44.0m "{q['io']}" (p. 50).

**4. Not in the documents:** critical audit matters (the auditor's report has none), receivables sold or factored, supplier finance, amounts earned but not yet billed, the amount of interest capitalized, and Item 13 on related parties.
"""

# ---------- checks before saving ----------
fails = []
for k, (s, p) in Q.items():
    pg = pages_of(s)
    if p not in pg: fails.append((k, s, p, pg))
    if s not in reply: fails.append((k, "quote not used in reply"))
assert all(absent[k] for k in ["unbilled", "factoring", "supplier finance", "critical audit matter"]), absent
assert not has_item13
assert "\u2014" not in reply and "\n>" not in reply
words = len(re.findall(r"\S+", reply))
print("quotation check:", "ALL PASS (%d quotes)" % len(Q) if not fails else fails)
print("words:", words)
print({k: (round(v, 2) if isinstance(v, float) else v) for k, v in c.items()})
print("absent keywords:", absent)
if not fails:
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(reply)
    print("saved", OUT)
