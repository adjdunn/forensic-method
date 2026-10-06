import re, openpyxl, os, shutil
D = r"C:\Users\aaron\OneDrive\Desktop\Master\WireSift Research\Events\CFA Vancouver Forensic\test-data\home-depot-fy2025"
wb = openpyxl.load_workbook(D + r"\statements.xlsx", data_only=True)
def sheet(name):
    ws=wb[name]; rows=list(ws.iter_rows(values_only=True)); hdr=rows[0]; d={}
    for r in rows[1:]:
        if r[0] is None: continue
        d[r[0]]={hdr[i]:r[i] for i in range(1,len(hdr)-1)}
    return d
IS=sheet('IS annual'); BS=sheet('BS annual'); CF=sheet('CF annual')
qIS=sheet('IS quarterly'); qBS=sheet('BS quarterly'); qCF=sheet('CF quarterly')

FY = ['FY (ended 2022-01-30)','FY (ended 2023-01-29)','FY (ended 2024-01-28)','FY (ended 2025-02-02)','FY (ended 2026-02-01)']
days_fy = {FY[0]:364, FY[1]:364, FY[2]:364, FY[3]:371, FY[4]:364}   # fiscal 2024 (ended 2025-02-02) = 53 weeks
# From annual-report note 3, p.58 (not in the workbook): PP&E at cost components and depreciation expense
ppe_cost = {'FY (ended 2024-01-28)':53257, 'FY (ended 2025-02-02)':55783, 'FY (ended 2026-02-01)':59467}
land     = {'FY (ended 2024-01-28)':9027,  'FY (ended 2025-02-02)':9060,  'FY (ended 2026-02-01)':9499}
cip      = {'FY (ended 2024-01-28)':1192,  'FY (ended 2025-02-02)':1521,  'FY (ended 2026-02-01)':1654}
dep_note = {'FY (ended 2023-01-29)':2756, 'FY (ended 2024-01-28)':3020, 'FY (ended 2025-02-02)':3283, 'FY (ended 2026-02-01)':3452}

def g(d,line,col):
    return d.get(line,{}).get(col)
def pct(a,b): return None if (a is None or b is None or b==0) else 100.0*a/b
def growth(a,b): return None if (a is None or b is None or b==0) else 100.0*(a/b-1)

R={}
for i,c in enumerate(FY):
    r={}
    sales=g(IS,'Net sales',c); cogs=g(IS,'Cost of sales',c); gp=g(IS,'Gross profit',c); oi=g(IS,'Operating income',c)
    ni=g(IS,'Net earnings',c); sga=g(IS,'Selling, general and administrative',c)
    ocf=g(CF,'Net cash provided by operating activities',c); capex=-g(CF,'Capital expenditures',c); acq=g(CF,'Payments for businesses acquired, net',c)
    rec=g(BS,'Receivables, net',c); inv=g(BS,'Merchandise inventories',c); ap=g(BS,'Accounts payable',c); ta=g(BS,'Total assets',c)
    ca=g(BS,'Total current assets',c); ppe=g(BS,'Net property and equipment',c); cl=g(BS,'Total current liabilities',c); ltd=g(BS,'Long-term debt, excluding current installments',c)
    dd=days_fy[c]
    r.update(sales=sales,cogs=cogs,ni=ni,ocf=ocf,capex=capex,acq=acq,rec=rec,inv=inv,ap=ap,ta=ta,sga=sga)
    r['DSO']= None if rec is None else rec/sales*dd
    r['DIO']= None if inv is None else inv/cogs*dd
    r['DPO']= None if ap is None else ap/cogs*dd
    r['GM']=pct(gp,sales); r['OM']=pct(oi,sales)
    r['FCF']=ocf-capex; r['FCF_NI']=r['FCF']/ni
    r['rec_sales']=pct(rec,sales); r['inv_sales']=pct(inv,sales); r['ap_sales']=pct(ap,sales)
    r['capex_dep']= None if c not in dep_note else capex/dep_note[c]
    if i>0:
        p=FY[i-1]
        psales=g(IS,'Net sales',p); pcogs=g(IS,'Cost of sales',p); psga=g(IS,'Selling, general and administrative',p)
        prec=g(BS,'Receivables, net',p); pinv=g(BS,'Merchandise inventories',p); pap=g(BS,'Accounts payable',p); pta=g(BS,'Total assets',p)
        r['sales_g']=growth(sales,psales); r['cogs_g']=growth(cogs,pcogs); r['sga_g']=growth(sga,psga)
        r['rec_g']=growth(rec,prec); r['inv_g']=growth(inv,pinv); r['ap_g']=growth(ap,pap)
        r['gap_rec']= None if r['rec_g'] is None else r['rec_g']-r['sales_g']
        r['gap_inv']= None if r['inv_g'] is None else r['inv_g']-r['cogs_g']
        r['gap_ap'] = None if r['ap_g'] is None else r['ap_g']-r['cogs_g']
        r['accruals']= None if (ta is None or pta is None) else 100.0*(ni-ocf)/((ta+pta)/2)
        if c in ppe_cost and p in ppe_cost:
            gd_t=ppe_cost[c]-land[c]-cip[c]; gd_p=ppe_cost[p]-land[p]-cip[p]
            r['dep_rate']=100.0*dep_note[c]/((gd_t+gd_p)/2)
        if prec is not None and pta is not None:
            pgp=g(IS,'Gross profit',p)
            pca=g(BS,'Total current assets',p); pppe=g(BS,'Net property and equipment',p); pcl=g(BS,'Total current liabilities',p); pltd=g(BS,'Long-term debt, excluding current installments',p)
            DSRI=(rec/sales)/(prec/psales)
            GMI=(pgp/psales)/(gp/sales)
            AQI=(1-(ca+ppe)/ta)/(1-(pca+pppe)/pta)
            SGI=sales/psales
            dep_t=dep_note[c]; dep_p=dep_note[p]
            DEPI=(dep_p/(dep_p+pppe))/(dep_t/(dep_t+ppe))
            SGAI=(sga/sales)/(psga/psales)
            TATA=(ni-ocf)/ta
            LVGI=((ltd+cl)/ta)/((pltd+pcl)/pta)
            M=-4.84+0.920*DSRI+0.528*GMI+0.404*AQI+0.892*SGI+0.115*DEPI-0.172*SGAI+4.679*TATA-0.327*LVGI
            r.update(DSRI=DSRI,GMI=GMI,AQI=AQI,SGI=SGI,DEPI=DEPI,SGAI=SGAI,TATA=TATA,LVGI=LVGI,M=M)
    R[c]=r

# Latest quarter: Q2 (ended 2026-08-02) vs Q2 (ended 2025-08-03); 13 weeks each. Neither is a mixed-basis Q4.
Q={'cur':'Q2 (ended 2026-08-02)','prev':'Q2 (ended 2025-08-03)'}
Qstart={'Q2 (ended 2026-08-02)':'Q1 (ended 2026-05-03)','Q2 (ended 2025-08-03)':'Q1 (ended 2025-05-04)'}
Qyago={'Q2 (ended 2026-08-02)':'Q2 (ended 2025-08-03)','Q2 (ended 2025-08-03)':'Q2 (ended 2024-07-28)'}
RQ={}
for k,c in Q.items():
    r={}
    sales=g(qIS,'Net sales',c); cogs=g(qIS,'Cost of sales',c); gp=g(qIS,'Gross profit',c); oi=g(qIS,'Operating income',c); ni=g(qIS,'Net earnings',c)
    ocf=g(qCF,'Net cash provided by operating activities',c); capex=-g(qCF,'Capital expenditures',c)
    rec=g(qBS,'Receivables, net',c); inv=g(qBS,'Merchandise inventories',c); ap=g(qBS,'Accounts payable',c); ta=g(qBS,'Total assets',c)
    ta0=g(qBS,'Total assets',Qstart[c])
    y=Qyago[c]; ysales=g(qIS,'Net sales',y); ycogs=g(qIS,'Cost of sales',y); yrec=g(qBS,'Receivables, net',y); yinv=g(qBS,'Merchandise inventories',y); yap=g(qBS,'Accounts payable',y)
    r.update(sales=sales,cogs=cogs,ni=ni,ocf=ocf,capex=capex,rec=rec,inv=inv,ap=ap,ta=ta)
    r['DSO']=rec/sales*91; r['DIO']=inv/cogs*91; r['DPO']=ap/cogs*91
    r['GM']=pct(gp,sales); r['OM']=pct(oi,sales)
    r['FCF']=ocf-capex; r['FCF_NI']=r['FCF']/ni
    r['sales_g']=growth(sales,ysales); r['cogs_g']=growth(cogs,ycogs)
    r['rec_g']=growth(rec,yrec); r['inv_g']=growth(inv,yinv); r['ap_g']=growth(ap,yap)
    r['gap_rec']=r['rec_g']-r['sales_g']; r['gap_inv']=r['inv_g']-r['cogs_g']; r['gap_ap']=r['ap_g']-r['cogs_g']
    r['accruals']=100.0*(ni-ocf)/((ta+ta0)/2)
    RQ[k]=r

IND={'rec_sales':2.8,'inv_sales':16.8,'ap_sales':9.4,'GM':34.2,'OM':11.9,'capex_dep':1.2}

# ---------------- verification of figures and quotation against the filing text ----------------
def pages(txt):
    parts = re.split(r'(\[p\. (\d+)\])', txt); out={None:parts[0]}; i=1
    while i < len(parts):
        out[int(parts[i+1])]=parts[i+2]; i+=3
    return out
AR26 = pages(open(D + r"\annual-report-FY2026-02-01-key-sections.txt", encoding='utf-8', errors='replace').read())
AR25 = pages(open(D + r"\annual-report-FY2025-02-02-key-sections.txt", encoding='utf-8', errors='replace').read())
QUOTE = "The valuation allowance related to these receivables was not material to our consolidated financial statements at the end of fiscal 2025 or fiscal 2024."
assert QUOTE in AR26[48], "quote not found on p.48"
p58_26 = AR26[58].replace("\n", " | "); p58_25 = AR25[58].replace("\n", " | ")
for s in ["Property and equipment, at cost | 59,467 | 55,783", "Land | $9,499 | $9,060", "Construction in progress | 1,654 | 1,521",
          "Depreciation and finance lease amortization expense | $3,452 | $3,283 | $3,020"]:
    assert s in p58_26, s
for s in ["Property and equipment, at cost | 55,783 | 53,257", "Land | $9,060 | $9,027", "Construction in progress | 1,521 | 1,192",
          "Depreciation and finance lease amortization expense | $3,283 | $3,020 | $2,756"]:
    assert s in p58_25, s
p74_26 = AR26[74].replace("\n", " | "); p74_25 = AR25[74].replace("\n", " | ")
assert "Receivables | 1,831 | Merchandise inventories | 1,988" in p74_25
assert "Receivables | 899 | Merchandise inventories | 568" in p74_26
p48_26 = AR26[48].replace("\n", " | ")
assert "Customer receivables | 2,588 | 1,896" in p48_26

# ---------------- report ----------------
def f1(v, d=1):  return "" if v is None else f"{v:.{d}f}"
def fs(v, d=1):  return "" if v is None else f"{v:+.{d}f}"
def fx(v):       return "" if v is None else f"{v:.2f}"
cols = FY + [Q['prev'], Q['cur']]
hdr = ["FY 2022-01-30","FY 2023-01-29","FY 2024-01-28","FY 2025-02-02","FY 2026-02-01","Q2 2025-08-03","Q2 2026-08-02","Industry"]
def cell(c,k,fn):
    r = R[c] if c in R else RQ['prev' if c==Q['prev'] else 'cur']
    return fn(r.get(k))
rows = [
 ("Days sales outstanding",            'DSO',      f1, None),
 ("Days inventory",                    'DIO',      f1, None),
 ("Days payable",                      'DPO',      f1, None),
 ("Receivables growth minus sales growth (pts)",      'gap_rec', fs, None),
 ("Inventory growth minus cost-of-sales growth (pts)",'gap_inv', fs, None),
 ("Payables growth minus cost-of-sales growth (pts)", 'gap_ap',  fs, None),
 ("Receivables / sales (%)",           'rec_sales', f1, IND['rec_sales']),
 ("Inventory / sales (%)",             'inv_sales', f1, IND['inv_sales']),
 ("Payables / sales (%)",              'ap_sales',  f1, IND['ap_sales']),
 ("Gross margin (%)",                  'GM',        f1, IND['GM']),
 ("Operating margin (%)",              'OM',        f1, IND['OM']),
 ("Accruals: (NI - OCF) / avg assets (%)", 'accruals', f1, None),
 ("Free cash flow / net income (x)",   'FCF_NI',    fx, None),
 ("Capex / depreciation (x)",          'capex_dep', fx, IND['capex_dep']),
 ("Depreciation rate (%)",             'dep_rate',  f1, None),
 ("Beneish M-score",                   'M',         fx, None),
]
quarter_blank = {'rec_sales','inv_sales','ap_sales','capex_dep','dep_rate','M'}
lines = ["| Measure | " + " | ".join(hdr) + " |", "|---|" + "---:|"*len(hdr)]
for name,k,fn,ind in rows:
    vals=[]
    for c in cols:
        if c in (Q['prev'],Q['cur']) and k in quarter_blank: vals.append("")
        else: vals.append(cell(c,k,fn))
    vals.append("" if ind is None else f"{ind:.1f}")
    lines.append(f"| {name} | " + " | ".join(vals) + " |")
table = "\n".join(lines)

A,B,C,Dd,E = [R[c] for c in FY]; Qp,Qc = RQ['prev'],RQ['cur']; L=E
gm_lo=min(B['GM'],C['GM'],Dd['GM'],E['GM']); gm_hi=max(B['GM'],C['GM'],Dd['GM'],E['GM'])
acq_fy25 = -g(CF,'Payments for businesses acquired, net',FY[3]); acq_fy26 = -g(CF,'Payments for businesses acquired, net',FY[4])
ex_gms_inv_g = growth(g(BS,'Merchandise inventories',FY[4])-568, g(BS,'Merchandise inventories',FY[3]))
d_ap = g(CF,'Changes in accounts payable and accrued expenses',FY[4]); d_inv = g(CF,'Changes in merchandise inventories',FY[4])
d_tax = g(CF,'Changes in income taxes payable',FY[4]); d_tax_p = g(CF,'Changes in income taxes payable',FY[3])
rev_other = 4262-656

md = f"""{table}

Cost line: the reported "Cost of sales". Substitutes: depreciation (for the depreciation rate, capex/depreciation and DEPI) is the note-3 "Depreciation and finance lease amortization expense" (annual reports p.58) over property and equipment at cost less land and construction in progress from the same note, since the workbook has no gross figure; days use 364 (371 for the 53-week year ended 2025-02-02) and 91 for quarters; the latest quarter is Q2 ended 2026-08-02 against Q2 ended 2025-08-03, so the mixed-basis Q4 columns were not needed.

**Flags**

1. **Receivables outrunning sales.** FY 2025-02-02: receivables {Dd['rec_g']:+.1f}% vs sales {Dd['sales_g']:+.1f}% (gap {Dd['gap_rec']:+.1f} pts), DSO {C['DSO']:.1f} to {Dd['DSO']:.1f} days; FY 2026-02-01 gap {E['gap_rec']:+.1f} pts, DSO {E['DSO']:.1f}; Q2 2026-08-02 gap {Qc['gap_rec']:+.1f} pts, DSO {Qp['DSO']:.1f} to {Qc['DSO']:.1f}; receivables/sales {L['rec_sales']:.1f}% vs industry 2.8% (BS "Receivables, net", IS "Net sales"; DSRI {Dd['DSRI']:.2f} in FY 2025-02-02 is the same movement). Acquisitions could explain most of it: ${acq_fy25:,}M and ${acq_fy26:,}M paid for businesses (CF annual "Payments for businesses acquired, net") brought $1,831M and $899M of receivables (annual reports p.74).
2. **Operating cash flow fell faster than earnings.** FY 2026-02-01: OCF {growth(E['ocf'],Dd['ocf']):.1f}% to ${E['ocf']:,}M against net earnings {growth(E['ni'],Dd['ni']):.1f}%; accruals {C['accruals']:.1f}% to {Dd['accruals']:.1f}% to {E['accruals']:.1f}% over three years, FCF/net income {C['FCF_NI']:.2f} to {Dd['FCF_NI']:.2f} to {E['FCF_NI']:.2f}. CF annual: "Changes in accounts payable and accrued expenses" {d_ap:,}, "Changes in merchandise inventories" {d_inv:,}, "Changes in income taxes payable" {d_tax:,} after {d_tax_p:+,} a year earlier.
3. **Payables down while cost of sales up, and low against the industry.** FY 2026-02-01: payables {E['ap_g']:+.1f}% vs cost of sales {E['cogs_g']:+.1f}% (gap {E['gap_ap']:+.1f} pts), DPO {Dd['DPO']:.1f} to {E['DPO']:.1f} days, after a {Dd['gap_ap']:+.1f}-pt gap the year before (BS annual "Accounts payable"). Payables/sales {L['ap_sales']:.1f}% vs industry 9.4%: {IND['ap_sales']-L['ap_sales']:.1f} pts ({100*(1-L['ap_sales']/IND['ap_sales']):.0f}%) below, the widest of the six industry gaps.
4. **Inventory growing faster than cost of sales two years running.** Gap {Dd['gap_inv']:+.1f} pts in FY 2025-02-02 and {E['gap_inv']:+.1f} pts in FY 2026-02-01; days inventory {C['DIO']:.1f} to {Dd['DIO']:.1f} to {E['DIO']:.1f} (BS annual "Merchandise inventories"). Acquired inventory was $1,988M (SRS) and $568M (GMS); excluding GMS, FY 2026-02-01 inventory still grew {ex_gms_inv_g:.1f}%. The level is below the industry ({L['inv_sales']:.1f}% vs 16.8% of sales).
5. **Operating margin sliding while gross margin holds.** {B['OM']:.1f}% to {C['OM']:.1f}% to {Dd['OM']:.1f}% to {E['OM']:.1f}% from FY 2023-01-29 to FY 2026-02-01 (IS annual "Operating income"), gross margin {gm_lo:.1f}-{gm_hi:.1f}% throughout; SG&A {E['sga_g']:+.1f}% vs sales {E['sales_g']:+.1f}% in the latest year. The level is still above the industry 11.9%.

**Revised figures:** the Revisions sheet lists four changes and none moved income, operating cash flow or equity: intangible assets (${rev_other:,}M) were moved out of "Other assets" at 2024-01-28, and intangible amortization was split out of the cash-flow D&A line (-179, -186, -52).

**Not calculated:** allowance for doubtful accounts (no figure in the workbook or either annual report; the FY 2026-02-01 report says only "{QUOTE}" p.48); accruals and M-score before FY 2024-01-28 and depreciation rate before FY 2025-02-02 (no balance sheet before 2023-01-29 and no gross property figure before 2024-01-28 in the documents); quarterly M-score and quarterly industry shares.
"""
md = md.replace("\u2212", "-")
out_dir = os.path.join(D, "runs", "v2.6"); os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "numbers-1.md"), "w", encoding="utf-8") as f:
    f.write(md)
shutil.copyfile(os.path.abspath(__file__), os.path.join(out_dir, "numbers-code-1.py"))
print(md)
print("WORDS:", len(md.split()))
