# Turn 1: scan the numbers. Home Depot, fiscal years to FY2025 (ended 2026-02-01).
import openpyxl, re, json
wb = openpyxl.load_workbook('statements.xlsx', data_only=True)
def sheet(name):
    ws = wb[name]; rows = list(ws.iter_rows(values_only=True))
    hdr = rows[0]; d = {}
    for r in rows[1:]:
        if r[0] is None: continue
        d[r[0]] = {hdr[i]: r[i] for i in range(1, len(hdr)-1)}
    return d
ISa, BSa, CFa = sheet('IS annual'), sheet('BS annual'), sheet('CF annual')
ISq, BSq = sheet('IS quarterly'), sheet('BS quarterly')
Y = {'FY2021':'FY (ended 2022-01-30)','FY2022':'FY (ended 2023-01-29)','FY2023':'FY (ended 2024-01-28)',
     'FY2024':'FY (ended 2025-02-02)','FY2025':'FY (ended 2026-02-01)'}
days = {'FY2021':364,'FY2022':364,'FY2023':364,'FY2024':371,'FY2025':364}  # FY2024 = 53 weeks (annual report)
def a(sh, line, y): return sh[line][Y[y]]
rev = lambda y: a(ISa,'Net sales',y); cogs = lambda y: a(ISa,'Cost of sales',y)
rec = lambda y: a(BSa,'Receivables, net',y); inv = lambda y: a(BSa,'Merchandise inventories',y)
ap = lambda y: a(BSa,'Accounts payable',y); ta = lambda y: a(BSa,'Total assets',y)
ni = lambda y: a(ISa,'Net earnings',y); cfo = lambda y: a(CFa,'Net cash provided by operating activities',y)
capex = lambda y: -a(CFa,'Capital expenditures',y); pti = lambda y: a(ISa,'Earnings before provision for income taxes',y)
# property note (annual reports, Note 3, p. 58 of each text file)
dep = {'FY2022':2756,'FY2023':3020,'FY2024':3283,'FY2025':3452}
gross = {'FY2023':53257-9027-1192,'FY2024':55783-9060-1521,'FY2025':59467-9499-1654}  # cost less land less CIP
R = {}
bsy = ['FY2022','FY2023','FY2024','FY2025']
for y in bsy:
    r = {}
    r['dso'] = rec(y)/rev(y)*days[y]; r['dio'] = inv(y)/cogs(y)*days[y]; r['dpo'] = ap(y)/cogs(y)*days[y]
    r['gm'] = a(ISa,'Gross profit',y)/rev(y)*100; r['om'] = a(ISa,'Operating income',y)/rev(y)*100
    r['fcf'] = cfo(y)-capex(y); r['fcf_ni'] = r['fcf']/ni(y)
    r['rec_s'] = rec(y)/rev(y)*100; r['inv_s'] = inv(y)/rev(y)*100; r['ap_s'] = ap(y)/rev(y)*100
    r['capex_dep'] = capex(y)/dep[y]
    R[y] = r
for y in ['FY2021']:
    R[y] = {'gm':a(ISa,'Gross profit',y)/rev(y)*100,'om':a(ISa,'Operating income',y)/rev(y)*100,'fcf':cfo(y)-capex(y),'fcf_ni':(cfo(y)-capex(y))/ni(y)}
prev = {'FY2022':'FY2021','FY2023':'FY2022','FY2024':'FY2023','FY2025':'FY2024'}
g = lambda f,y: (f(y)/f(prev[y])-1)*100
for y in ['FY2023','FY2024','FY2025']:
    r = R[y]; p = prev[y]
    r['rev_g']=g(rev,y); r['cogs_g']=g(cogs,y)
    r['rec_gap']=g(rec,y)-g(rev,y); r['inv_gap']=g(inv,y)-g(cogs,y); r['ap_gap']=g(ap,y)-g(cogs,y)
    r['rec_g']=g(rec,y); r['inv_g']=g(inv,y); r['ap_g']=g(ap,y)
    r['accr']=(ni(y)-cfo(y))/((ta(y)+ta(p))/2)*100
    # Beneish
    DSRI=(rec(y)/rev(y))/(rec(p)/rev(p)); GMI=(R[p]['gm'])/(r['gm'])
    nca=lambda z: 1-(a(BSa,'Total current assets',z)+a(BSa,'Net property and equipment',z))/ta(z)
    AQI=nca(y)/nca(p); SGI=rev(y)/rev(p)
    dr=lambda z: dep[z]/(dep[z]+a(BSa,'Net property and equipment',z))
    DEPI=dr(p)/dr(y)
    sga=lambda z: a(ISa,'Selling, general and administrative',z)/rev(z)
    SGAI=sga(y)/sga(p)
    TATA=(ni(y)-cfo(y))/ta(y)
    lev=lambda z:(a(BSa,'Total current liabilities',z)+a(BSa,'Long-term debt, excluding current installments',z))/ta(z)
    LVGI=lev(y)/lev(p)
    M=-4.84+0.920*DSRI+0.528*GMI+0.404*AQI+0.892*SGI+0.115*DEPI-0.172*SGAI+4.679*TATA-0.327*LVGI
    r['M']=M; r['Mparts']=dict(DSRI=DSRI,GMI=GMI,AQI=AQI,SGI=SGI,DEPI=DEPI,SGAI=SGAI,TATA=TATA,LVGI=LVGI)
for y in ['FY2024','FY2025']:
    R[y]['deprate']=dep[y]/((gross[y]+gross[prev[y]])/2)*100
R['FY2024']['deprate_52']=dep['FY2024']*52/53/((gross['FY2024']+gross['FY2023'])/2)*100
# Latest quarter the documents cover: Q4 FY2025 (13 weeks, ended 2026-02-01) vs Q4 FY2024 (14 weeks, ended 2025-02-02).
# Income statement and balance sheet from the two results releases (p. 5, p. 6 of each).
Q = {'Q4 FY2025':dict(rev=38198,cogs=25732,gp=12466,oi=3849,rec=5597,inv=25817,ap=11491,days=91),
     'Q4 FY2024':dict(rev=39704,cogs=26670,gp=13034,oi=4495,rec=4903,inv=23451,ap=11938,days=98)}
# Q4 FY2023 (for the year-earlier gaps and persistence): release for FY2024 gives its comparative column
t = open('earnings-release-Q4-FY2025-02-02.txt',encoding='utf-8').read()
def row(label, txt):
    m = re.search(r'^'+re.escape(label)+r' \| (.+)$', txt, re.M); return [c.strip() for c in m.group(1).split('|')]
num = lambda s: float(s.replace('$','').replace(',','').replace('(','-').replace(')',''))
p5 = t[t.find('[p. 5]'):t.find('[p. 6]')]; p6 = t[t.find('[p. 6]'):t.find('[p. 7]')]
print('release FY2024 p5 header check:', [l for l in p5.split('\n') if 'in millions' in l])
print('release FY2024 p6 header check:', [l for l in p6.split('\n') if 'in millions' in l])
Q['Q4 FY2023']=dict(rev=num(row('Net sales',p5)[1]),cogs=num(row('Cost of sales',p5)[1]),gp=num(row('Gross profit',p5)[1]),oi=num(row('Operating income',p5)[1]),
    rec=num(row('Receivables, net',p6)[1]),inv=num(row('Merchandise inventories',p6)[1]),ap=num(row('Accounts payable',p6)[1]),days=91)
assert num(row('Net sales',p5)[0])==Q['Q4 FY2024']['rev'] and num(row('Receivables, net',p6)[0])==4903
# cross-check release against spreadsheet
assert ISq['Net sales']['Q4 (ended 2026-02-01)']==38198 and ISq['Cost of sales']['Q4 (ended 2025-02-02)']==26670 and ISq['Net sales']['Q4 (ended 2024-01-28)']==Q['Q4 FY2023']['rev']
for k,q in Q.items():
    q['dso']=q['rec']/q['rev']*q['days']; q['dio']=q['inv']/q['cogs']*q['days']; q['dpo']=q['ap']/q['cogs']*q['days']
    q['gm']=q['gp']/q['rev']*100; q['om']=q['oi']/q['rev']*100
for k,p in [('Q4 FY2025','Q4 FY2024'),('Q4 FY2024','Q4 FY2023')]:
    q,pp=Q[k],Q[p]; gg=lambda f:(q[f]/pp[f]-1)*100
    q['rev_g']=gg('rev'); q['cogs_g']=gg('cogs')
    q['rec_gap']=gg('rec')-gg('rev'); q['inv_gap']=gg('inv')-gg('cogs'); q['ap_gap']=gg('ap')-gg('cogs')
# Flags: size and persistence
P=pti('FY2025'); F={}
exp_rec=R['FY2024']['dso']*rev('FY2025')/days['FY2025']; F['rec_excess']=rec('FY2025')-exp_rec
exp_inv=R['FY2024']['dio']*cogs('FY2025')/days['FY2025']; F['inv_excess']=inv('FY2025')-exp_inv
exp_ap=R['FY2024']['dpo']*cogs('FY2025')/days['FY2025']; F['ap_short']=exp_ap-ap('FY2025')
F['fcf_gap']=R['FY2025']['fcf']-ni('FY2025')
F['om_drop']=(R['FY2024']['om']-R['FY2025']['om'])/100*rev('FY2025')
sgar=lambda z: a(ISa,'Selling, general and administrative',z)/rev(z)
F['sga_rise']=(sgar('FY2025')-sgar('FY2024'))*rev('FY2025')
F['gw_int']=a(BSa,'Goodwill','FY2025')+a(BSa,'Intangible assets, net','FY2025')
F['pct']={k:(v/P*100) for k,v in F.items() if isinstance(v,(int,float))}
F['acq']={y:-a(CFa,'Payments for businesses acquired, net',y) for y in Y}
F['ap_ind_gap']=(9.4-R['FY2025']['ap_s'])/100*rev('FY2025')
F['rec_ind_gap']=(R['FY2025']['rec_s']-2.8)/100*rev('FY2025')
out=dict(R=R,Q=Q,F=F,P=P,gross=gross)
if __name__=='__main__':
    for y in ['FY2021']+bsy: print(y,{k:(round(v,3) if isinstance(v,float) else v) for k,v in R[y].items()})
    for k,q in Q.items(): print(k,{a_:round(b_,2) for a_,b_ in q.items()})
    print(F); print('pretax',P)

# ---- reply ----
def build_reply():
    ys=['FY2022','FY2023','FY2024','FY2025']; qs=['Q4 FY2024','Q4 FY2025']
    def line(label, key, fmt, ind='', qkey=None, yrs=ys):
        cells=[(fmt.format(R[y][key]) if (y in yrs and key in R[y]) else '') for y in ys]
        qc=[(fmt.format(Q[q][qkey]) if qkey and qkey in Q[q] else '') for q in qs]
        return '| '+' | '.join([label]+cells+qc+[ind])+' |'
    f1='{:.1f}'; f2='{:+.1f}'
    T=['| Measure | FY2022 (to Jan 2023) | FY2023 (to Jan 2024) | FY2024 (to Feb 2025, 53 weeks) | FY2025 (to Feb 2026) | Q4 FY2024 (14 weeks) | Q4 FY2025 (13 weeks) | Industry |',
       '|---|---|---|---|---|---|---|---|']
    T.append(line('Days sales outstanding','dso',f1,qkey='dso'))
    T.append(line('Days inventory','dio',f1,qkey='dio'))
    T.append(line('Days payable','dpo',f1,qkey='dpo'))
    T.append(line('Receivables growth less revenue growth (pts)','rec_gap',f2,qkey='rec_gap'))
    T.append(line('Inventory growth less cost-of-sales growth (pts)','inv_gap',f2,qkey='inv_gap'))
    T.append(line('Payables growth less cost-of-sales growth (pts)','ap_gap',f2,qkey='ap_gap'))
    T.append(line('Gross margin (%)','gm',f1,'34.2',qkey='gm'))
    T.append(line('Operating margin (%)','om',f1,'11.9',qkey='om'))
    T.append(line('Accruals (% of average assets)','accr',f1))
    T.append('| Free cash flow vs net income ($m) | '+' | '.join('{:,.0f} vs {:,.0f}'.format(R[y]['fcf'],ni(y)) for y in ys)+' | | | |')
    T.append(line('Depreciation rate (%)','deprate','{:.2f}'))
    T.append(line('Beneish M-score (vs prior year)','M','{:.2f}'))
    T.append(line('Receivables / sales (%)','rec_s',f1,'2.8'))
    T.append(line('Inventory / sales (%)','inv_s',f1,'16.8'))
    T.append(line('Payables / sales (%)','ap_s',f1,'9.4'))
    T.append(line('Capital spending / depreciation (x)','capex_dep','{:.2f}','1.2'))
    r5,r4,r3,r2=R['FY2025'],R['FY2024'],R['FY2023'],R['FY2022']; q5,q4,q3=Q['Q4 FY2025'],Q['Q4 FY2024'],Q['Q4 FY2023']
    pc=F['pct']; m=lambda v:'${:,.0f}m'.format(abs(v))
    L=[]
    L.append('\n'.join(T))
    L.append('')
    L.append(f"Cost line: cost of sales. Days use 364 per year (371 in FY2024, a 53-week year) and 91 or 98 per quarter; depreciation and gross depreciable assets come from the property note, and both fourth quarters come from the results releases because the spreadsheet marks its fourth-quarter cash flow columns mixed basis.")
    L.append('')
    L.append('**Flags**')
    L.append('')
    L.append(f"1. **Receivables outgrew revenue.** Receivables rose {r5['rec_g']:.1f}% in FY2025 against revenue up {r5['rev_g']:.1f}%, after {r4['rec_g']:.1f}% against {r4['rev_g']:.1f}% in FY2024; days went {r3['dso']:.1f} to {r4['dso']:.1f} to {r5['dso']:.1f}, and sit at {r5['rec_s']:.1f}% of sales against 2.8% for the industry. Acquisitions took {m(F['acq']['FY2024'])} of cash in FY2024 and {m(F['acq']['FY2025'])} in FY2025.  \n   Size: {pc['rec_excess']:.1f}% of FY2025 pre-tax income, using the excess balance at FY2024 days ({m(F['rec_excess'])}). Run: three years; two same-quarter comparisons ({q3['dso']:.1f}, {q4['dso']:.1f}, {q5['dso']:.1f} days).")
    L.append(f"2. **Cash flow fell behind earnings.** Operating cash flow fell {-(cfo('FY2025')/cfo('FY2024')-1)*100:.1f}% in FY2025 while net income fell {-(ni('FY2025')/ni('FY2024')-1)*100:.1f}%; free cash flow went from {r3['fcf_ni']:.2f} to {r4['fcf_ni']:.2f} to {r5['fcf_ni']:.2f} times net income, and accruals from {r3['accr']:.1f}% to {r4['accr']:.1f}% to {r5['accr']:.1f}%.  \n   Size: {abs(pc['fcf_gap']):.1f}% of pre-tax income, using the gap between free cash flow and net income ({m(F['fcf_gap'])}). Run: two years.")
    L.append(f"3. **Inventory outgrew cost of sales.** Inventory rose {r5['inv_g']:.1f}% in FY2025 against cost of sales up {r5['cogs_g']:.1f}%; days went {r3['dio']:.1f} to {r4['dio']:.1f} to {r5['dio']:.1f}, and {q4['dio']:.1f} to {q5['dio']:.1f} in the fourth quarter. The FY2025 acquisition spending could explain part.  \n   Size: {pc['inv_excess']:.1f}% of pre-tax income, using the excess balance at FY2024 days ({m(F['inv_excess'])}). Run: two years.")
    L.append(f"4. **Operating margin kept falling.** {r2['om']:.1f}% in FY2022, then {r3['om']:.1f}%, {r4['om']:.1f}% and {r5['om']:.1f}%, with gross margin flat near {r5['gm']:.1f}%; the fourth quarter went {q4['om']:.1f}% to {q5['om']:.1f}%.  \n   Size: {pc['om_drop']:.1f}% of pre-tax income, using the FY2025 margin decline times FY2025 sales ({m(F['om_drop'])}). Run: three years; two same-quarter comparisons.")
    L.append(f"5. **Payables fell while cost of sales grew, and sit below the industry.** Payables fell {-r5['ap_g']:.1f}% in FY2025 against cost of sales up {r5['cogs_g']:.1f}%; days went {r4['dpo']:.1f} to {r5['dpo']:.1f}, and payables are {r5['ap_s']:.1f}% of sales against 9.4% for the industry. This overlaps flag 2.  \n   Size: {pc['ap_short']:.1f}% of pre-tax income, using the shortfall against FY2024 days ({m(F['ap_short'])}). Run: one year, reversing FY2024's rise.")
    L.append('')
    L.append("**Revised figures:** none moved income or equity; the four later changes are reclassifications (intangible assets of $3,606m split out of other assets at January 2024, and intangible amortization of $179m, $186m and $52m split out of depreciation on the cash flow statement).")
    L.append('')
    L.append("**Not calculated:** the allowance as a share of gross receivables (both annual reports say only that it was not material); the depreciation rate before FY2024 (no gross property balance for January 2023); fourth-quarter accruals and free cash flow (the releases give cash flow for the full year only); FY2022 growth gaps, accruals and M-score (no balance sheet before January 2023).")
    return '\n'.join(L)
if __name__=='__main__':
    import sys
    if 'reply' in sys.argv:
        txt=build_reply()
        # checks: no banned words, no em-dashes
        import re as _re
        for w in ['fraud','manipulat','red flag','\u2014']: assert w not in txt.lower(), w
        open('runs/v2.10/numbers-1.md','w',encoding='utf-8').write(txt+'\n')
        body=_re.sub(r'[|*]',' ',txt)
        print(txt); print('WORDS',len(body.split()))
