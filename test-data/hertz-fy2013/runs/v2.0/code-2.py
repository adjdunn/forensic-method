# Turn 2: follow the flags. Inputs are pulled from named rows of the attached text files
# (annual reports and results releases) and from statements.xlsx; all arithmetic is here.
import json, os
from common import *
import openpyxl

A13, A12, R13, R12 = "FY2013 annual report", "FY2012 annual report", "FY2013 release", "FY2012 release"
def pct(a, b): return (a / b - 1) * 100
out = {}

# ---------- Flag 1: receivables
rec13, rec12r = row(A13, "Receivables, less allowance", page=75)[-2:]          # 1,512.6 ; 1,879.7 (revised)
rec12, rec11 = [x / 1000 for x in row(A12, "Receivables, less allowance", page=72)[-2:]]   # first reported
fleet13, fleet12r, fleet11r = row(A13, "Sales of revenue earning equipment included in receivables", page=81)
rev13, rev12r, rev11r = row(A13, "Total revenues", page=76)
proforma12 = row(A13, "2012 supplemental pro forma", page=99)[0]
other13, other12, other11 = rec13 - fleet13, rec12r - fleet12r, rec11 - fleet11r
q4disp13, q4disp12 = row(R13, "Proceeds from disposal of revenue earning equipment", after="FLEET GROWTH")[4], row(R13, "Proceeds from disposal of revenue earning equipment", after="FLEET GROWTH")[9]
q4buy13, q4buy12 = row(R13, "Revenue earning equipment expenditures", after="FLEET GROWTH")[4], row(R13, "Revenue earning equipment expenditures", after="FLEET GROWTH")[9]
sch13 = row(A13, "Year ended December 31, 2013", page=158)          # begin, expense, translation, deductions, end
sch12 = row(A13, "Year ended December 31, 2012(b)", page=158)
sch12_first = [x / 1000 for x in row(A12, "Year ended December 31, 2012", page=140)]
prov13, prov12r, prov11 = row(A13, "Provision for losses on doubtful accounts", page=80)
cf_rec13 = row(A13, "Receivables", page=80)[0]
out["flag1"] = dict(
    rec_change_revised=rec13 - rec12r, rec_change_revised_pct=pct(rec13, rec12r),
    rec_change_first=rec13 - rec12, rec12_first=rec12, rec12_revised=rec12r,
    fleet_rec=(fleet13, fleet12r), fleet_rec_change=fleet13 - fleet12r,
    fleet_share_of_fall=(fleet13 - fleet12r) / (rec13 - rec12r) * 100,
    other_rec=(other13, other12), other_rec_change=other13 - other12, other_rec_pct=pct(other13, other12),
    revenue_growth_revised=pct(rev13, rev12r),
    other_days_2013=other13 / rev13 * 365, other_days_2012=other12 / rev12r * 366,
    other_days_2012_proforma=other12 / proforma12 * 366, other_days_2011=other11 / rev11r * 365,
    q4_disposal_proceeds=(q4disp13, q4disp12), q4_disposal_pct=pct(q4disp13, q4disp12),
    q4_fleet_purchases=(q4buy13, q4buy12), q4_purchases_pct=pct(q4buy13, q4buy12),
    allowance=(sch13[0], sch13[-1]), charged_2013=sch13[1], writeoffs=(-sch13[3], -sch12[2]),
    writeoffs_pct=pct(-sch13[3], -sch12[2]), cf_provision_2013=prov13, cf_minus_schedule=prov13 - sch13[1],
    allowance_2012_first_vs_revised=(sch12_first[-1], sch12[-1]), cf_receivables_line=cf_rec13,
    allow_pct_2013=sch13[-1] / (sch13[-1] + rec13) * 100, allow_pct_2012r=sch12[-1] / (sch12[-1] + rec12r) * 100,
)

# ---------- Flag 2: corrections
c2010, c2011, c2012 = 4.4 + 2.4, 12.9 + 6.2 - 0.4, 2.4 + 3.6 + 3.2      # components stated on p. 83
adj12 = row(A13, "Income before income taxes", page=84)                 # 450.6, (9.2), 441.4, 324.3, (18.7), 305.6
adj9m13 = row(A13, "Income before income taxes", page=87)               # 328.3,(7.0),321.3,612.4,(11.6),600.8
q4pti13 = row(R13, "Income (loss) before income taxes", page="unnumbered")[0]
sga = row(A13, "Selling, general and administrative", page=84)
dre = row(A13, "Depreciation of revenue earning equipment and lease charges", page=84)
out["flag2"] = dict(
    prior_2010=c2010, y2011=c2011, y2012=c2012, sum_prior_years=c2010 + c2011 + c2012,
    table_adj_2012=adj12[1], table_adj_2011=adj12[4], nine_months_2013=adj9m13[4],
    total=c2010 + c2011 + c2012 - adj9m13[4], release_total=47.9, release_minus_10k=47.9 - (c2010 + c2011 + c2012 - adj9m13[4]),
    pct_of_pretax_2011=adj12[4] / adj12[3] * 100, pct_of_pretax_2012=adj12[1] / adj12[0] * 100,
    pct_of_pretax_9m13=adj9m13[4] / adj9m13[3] * 100, total_vs_q4_pretax=(c2010 + c2011 + c2012 - adj9m13[4]) / q4pti13 * 100,
    q4_pretax=q4pti13, sga_adj=(sga[1], sga[4]), dre_adj=(dre[1], dre[4]),
)

# ---------- Flag 3: fourth-quarter margin
wb = openpyxl.load_workbook(os.path.join(DATA, "statements.xlsx"), data_only=True)
def xl(sheet, label, col):
    ws = wb[sheet]; hdr = [c.value for c in ws[1]]
    for r in ws.iter_rows(min_row=2, values_only=True):
        if r[0] == label: return r[hdr.index(col)]
def gm(rev, dop, dre): return (rev - dop - dre) / rev * 100
q13, q12 = "Q4 (ended 2013-12-31)", "Q4 (ended 2012-12-31)"
gm_first = [gm(xl("IS quarterly", "Total revenues", q), xl("IS quarterly", "Direct operating", q),
               xl("IS quarterly", "Depreciation of revenue earning equipment and lease charges", q)) for q in (q13, q12)]
t1 = lambda lab: row(R13, lab, page="unnumbered")[:2]          # Table 1, three months: 2013, 2012
rv, do, dp, sg, tx = t1("Total revenues"), t1("Direct operating"), t1("Depreciation of revenue earning equipment and lease charges"), t1("Selling, general and administrative"), t1("(Provision) benefit for taxes on income")
gm_rev = [gm(rv[i], do[i], dp[i]) for i in (0, 1)]
adj_do = row(R13, "Direct operating", after="Reported | Adjustments | Adjusted")           # 1439.3, (62.1, 1377.2, 1257.7, (42.7, 1215.0
us_rev = row(R13, "U.S. Car Rental", after="SEGMENT AND OTHER INFORMATION")[:2]
us_dep = row(R13, "Depreciation of revenue earning equipment and lease charges", after="CONDENSED CONSOLIDATED STATEMENT OF OPERATIONS BY REPORTABLE SEGMENTS")
us_dep13, us_dep12 = us_dep[0], us_dep[6]
fleet_g, days_g, rpd_g = 22.4, 16.1, -1.4                        # release Table 4, U.S. car rental, three months
shares_q4 = 464.3
out["flag3"] = dict(
    gm_first_basis=gm_first, gm_revised=gm_rev, fall_revised_pts=gm_rev[0] - gm_rev[1],
    fall_in_money=(gm_rev[1] - gm_rev[0]) / 100 * rv[0],
    cost_ratio=[(do[i] + dp[i]) / rv[i] * 100 for i in (0, 1)],
    eps_impact_after_tax=0.12 * shares_q4, eps_impact_pretax_at_35=0.12 * shares_q4 / 0.65,
    us_rev_growth=pct(*us_rev), us_dep=(us_dep13, us_dep12), us_dep_growth=pct(us_dep13, us_dep12),
    rev_per_car=(1 + pct(*us_rev) / 100) / (1 + fleet_g / 100) * 100 - 100,
    dep_per_car=(1 + pct(us_dep13, us_dep12) / 100) / (1 + fleet_g / 100) * 100 - 100,
    days_per_car=(1 + days_g / 100) / (1 + fleet_g / 100) * 100 - 100,
    q4_tax_rate=-tx[0] / q4pti13 * 100, q4_tax=tx[0],
    adj_do_ratio=(adj_do[2] / rv[0] * 100, adj_do[5] / rv[1] * 100),
    sga_q4=sg, sga_q4_growth=pct(*sg),
    adj_pretax_q4=(186.3, 210.7), adj_pretax_q4_growth=pct(186.3, 210.7),
)

# ---------- Flag 4: fleet depreciation
n8 = row(A13, "Depreciation of revenue earning equipment |", page=126)        # 2,407.8 2,145.9 1,912.3
disp = row(A13, "Adjustment of depreciation upon disposal", page=126)
cars13, cars12r = row(A13, "Cars", page=75); oth13, oth12r = row(A13, "Other equipment", page=75)
cars12, cars11 = [x / 1000 for x in row(A12, "Cars", page=72)]; oth12, oth11 = [x / 1000 for x in row(A12, "Other equipment", page=72)]
g13, g12r, g11 = cars13 + oth13, cars12r + oth12r, cars11 + oth11
g10 = xl("BS annual", "Cars", "FY (ended 2010-12-31)") + xl("BS annual", "Other equipment", "FY (ended 2010-12-31)")
pti13, pti12r, pti11r = row(A13, "Income before income taxes", page=76)
seg_dep = row(A13, "U.S. car rental", page=131, nth=2)            # depreciation of REE and lease charges by segment
seg_rev = row(A13, "U.S. car rental", page=131, nth=0)
us_fleet_fy_g = 31.2                                               # release Table 4, year
out["flag4"] = dict(
    gross_fleet=(g13, g12r, g11, g10),
    rate_before_disposal=(n8[0] / ((g13 + g12r) / 2) * 100, n8[1] / ((g12r + g11) / 2) * 100, n8[2] / ((g11 + g10) / 2) * 100),
    dep_before_disposal_growth=pct(n8[0], n8[1]), avg_gross_growth=pct((g13 + g12r) / 2, (g12r + g11) / 2),
    us_rate_cut=(44.2, 139.4, 26.7), net_rate_change=(44.2 - 5.0 + 0.4, 139.4 - 8.8 - 0.5, 26.7 - 12.9 + 4.4),
    cut_pct_pretax=(44.2 / pti13 * 100, 139.4 / pti12r * 100, 26.7 / pti11r * 100),
    disposal_adj=disp, disposal_swing=disp[0] - disp[1], us_disposal_swing=48.2 + 100.6,
    us_seg_dep=seg_dep[:2], us_seg_dep_growth=pct(seg_dep[0], seg_dep[1]), us_seg_rev_growth=pct(seg_rev[0], seg_rev[1]),
    us_dep_per_company_car_change=(1 + pct(seg_dep[0], seg_dep[1]) / 100) / (1 + us_fleet_fy_g / 100) * 100 - 100,
    first_reported_2012_cut=130.6, check_139_4_less_8_8=139.4 - 8.8,
)

# ---------- Flag 5: other assets, restricted cash, payables
pre13, pre12r = row(A13, "Prepaid expenses and other assets", page=75)
rc13, rc12r = row(A13, "Restricted cash and cash equivalents", page=75)
ap13, ap12r = row(A13, "Accounts payable", page=75)
fleet_ap = row(A13, "Purchases of revenue earning equipment included in accounts payable", page=81)
ppe_ap = row(A13, "Purchases of property and equipment included in accounts payable", page=81)
do13, do12r, do11r = row(A13, "Direct operating", page=76)
rc_fleet = row(R13, "Restricted Cash Associated with Fleet Debt", after="NET CORPORATE DEBT, NET FLEET DEBT")     # 771.7, 456.6, 494.0 ...
deriv = row(A13, "instruments under ASC 815 |", page=142)                                 # 12.7, 4.5, 14.2, 5.5
acc13, acc12r = row(A13, "Accrued liabilities", page=75)
oap13, oap12 = ap13 - fleet_ap[0] - ppe_ap[0], ap12r - fleet_ap[1] - ppe_ap[1]
out["flag5"] = dict(
    prepaid=(pre13, pre12r), prepaid_change=pre13 - pre12r, prepaid_pct=pct(pre13, pre12r),
    china_notes=151.0, china_share=151.0 / (pre13 - pre12r) * 100, deriv_assets_change=deriv[0] - deriv[1],
    prepaid_untraced=pre13 - pre12r - 151.0 - (deriv[0] - deriv[1]),
    restricted=(rc13, rc12r), restricted_change=rc13 - rc12r, restricted_pct=pct(rc13, rc12r),
    restricted_fleet=(-rc_fleet[0], -rc_fleet[2]), restricted_fleet_change=-rc_fleet[0] + rc_fleet[2],
    restricted_fleet_share=(-rc_fleet[0] + rc_fleet[2]) / (rc13 - rc12r) * 100,
    payables=(ap13, ap12r), payables_pct=pct(ap13, ap12r), capital_items_in_ap=(fleet_ap[0] + ppe_ap[0], fleet_ap[1] + ppe_ap[1]),
    other_payables=(oap13, oap12), other_payables_pct=pct(oap13, oap12), direct_operating_growth=pct(do13, do12r),
    other_payable_days=(oap13 / do13 * 365, oap12 / do12r * 366),
    accrued=(acc13, acc12r), accrued_pct=pct(acc13, acc12r),
)

# ---------- Adjusted earnings
gap = lambda adj, rep: (adj - rep, (adj - rep) / rep * 100)
ni13, ni12r = 346.2, 238.6
out["adjusted"] = dict(
    fy2013=gap(1153.2, 663.1), fy2012_revised=gap(892.3, 441.4), fy2012_first=gap(901.5, 450.6), fy2011_first=gap(680.5, 324.3),
    adj_ni_multiple=(749.6 / ni13, 588.9 / ni12r, 595.0 / 243.1),
    restructuring_3yrs=(77.0, 38.0, 56.4), restructuring_related=(21.8, 11.1, 9.8), other_unusual=(50.7, 44.0),
    acquisition_plus_integration=(18.5 + 40.0, 163.7, 18.8), purchase_accounting=(132.2, 109.6, 87.6), debt_charges=(68.4, 83.6, 130.4),
    restructuring_since_2007=645.4, eff_tax=(47.8, 45.9), assumed_tax=(35, 34),
    adj_ni_at_actual_rate_2013=1153.2 * (1 - 0.478), adj_ni_reported_2013=749.6,
    fcf=(448.7, 155.1), dtg_excluded=129.6, corporate_cash_flow_2012=-2183.4,
)

# ---------- Reserves
pl13, pl12 = row(A13, "Public liability and property damage", page=75)
pl11 = 281.5
out["reserves"] = dict(
    pl=(pl13, pl12), pl_growth=pct(pl13, pl12), pl_pct_rev=(pl13 / rev13 * 100, pl12 / rev12r * 100, pl12 / proforma12 * 100, pl11 / rev11r * 100),
    utb=row(A13, "Balance at December 31", page=129), utb_prior=row(A13, "Decrease attributable to tax positions taken during prior periods", page=129),
    utb_2012_first=row(A12, "Balance at December 31", page=116),
    restructuring_accrual=(48.4, 21.0), us_unusual_credit_q4=-9.6, advantage_support_pv=15.6,
)

def show(d, ind=0):
    for k, v in d.items():
        if isinstance(v, dict): print(" " * ind + k + ":"); show(v, ind + 2)
        elif isinstance(v, (list, tuple)): print(" " * ind + f"{k}: " + ", ".join(f"{x:,.2f}" if isinstance(x, float) else str(x) for x in v))
        else: print(" " * ind + f"{k}: {v:,.2f}" if isinstance(v, float) else " " * ind + f"{k}: {v}")
show(out)

if os.path.exists(os.path.join(HERE, "reply-2.md")):
    print(); check_quotes("reply-2.md"); print("words:", wc("reply-2.md"))
