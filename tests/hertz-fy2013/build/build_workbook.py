"""Build pack/statements.xlsx for Hertz Global Holdings, as originally reported,
from the parsed statement reports (build/parsed.json).

Quarters Q1 FY2011 to Q4 FY2013; years FY2009 to FY2013. Units: USD millions.
- Q1 to Q3 income statement: the 3-month column of that quarter's own 10-Q.
- Q2, Q3 cash flow: year-to-date in that 10-Q minus year-to-date in the prior 10-Q.
- Q4 income statement and cash flow: the 10-K full year minus the Q3 10-Q nine months.
- Balance sheets: the period-end column of that period's own filing.
- FY2009: the comparative column in the FY2010 10-K (the FY2009 10-K has no rendered XBRL).
- RESTATED: every mapped annual line as reprinted in the next year's 10-K.
Writes a tie-out report to build/tieout.md.
"""
import json, re
from datetime import date
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill

HERE = Path(__file__).parent
PACK = HERE.parent / "pack"
parsed = json.loads((HERE / "parsed.json").read_text())

# ---- mapping: pack line -> list of elements (first present wins); ("sum", [...]) for derived sums
IS_MAP = {
    "Revenue": ["us-gaap:Revenues"],
    "Selling, general and administrative": ["us-gaap:SellingGeneralAndAdministrativeExpense"],
    "Interest expense": ["us-gaap:InterestExpense"],
    "Interest income": ["us-gaap:InvestmentIncomeInterest"],
    "Pre-tax income": ["us-gaap:IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments"],
    "Income from continuing operations": ["us-gaap:ProfitLoss"],
    "Net income": ["us-gaap:ProfitLoss"],
    "Diluted shares": ["us-gaap:WeightedAverageNumberOfDilutedSharesOutstanding"],
    "Diluted EPS": ["us-gaap:EarningsPerShareDiluted"],
}
# from the cash flow statement, placed on the income statement lines the spec asks for
IS_FROM_CF = {
    "Depreciation (excluding amortization of intangibles)": ["us-gaap:DepreciationNonproduction"],
    "Depreciation of equipment held for rental or lease": ["htz:CostOfServicesDepreciationAsAdjustedForGainLossUponDisposal", "us-gaap:CostOfServicesDepreciation"],
    "Amortization of intangibles": ["us-gaap:AmortizationOfIntangibleAssets"],
}
BS_MAP = {
    "Cash and equivalents": ["us-gaap:CashAndCashEquivalentsAtCarryingValue"],
    "Trade receivables, net": ["us-gaap:AccountsReceivableNet"],
    "Inventory, net": ["us-gaap:InventoryNet"],
    "PP&E, gross": ["us-gaap:PropertyPlantAndEquipmentGross"],
    "Accumulated depreciation": ["us-gaap:AccumulatedDepreciationDepletionAndAmortizationPropertyPlantAndEquipment"],
    "PP&E, net": ["us-gaap:PropertyPlantAndEquipmentNet"],
    "Equipment held for rental or lease, gross": ("sum", ["us-gaap:PropertySubjectToOrAvailableForOperatingLeaseGross", "htz:OtherEquipmentGross"]),
    "Accumulated depreciation, equipment held for rental or lease": ("sum", ["us-gaap:PropertySubjectToOrAvailableForOperatingLeaseAccumulatedDepreciation", "htz:AccumulatedDepreciationOtherEquipment"]),
    "Equipment held for rental or lease, net": ["us-gaap:PropertySubjectToOrAvailableForOperatingLeaseNet"],
    "Goodwill": ["us-gaap:Goodwill"],
    "Intangible assets, net": ["us-gaap:IntangibleAssetsNetExcludingGoodwill"],
    "Total assets": ["us-gaap:Assets"],
    "Trade payables": ["us-gaap:AccountsPayableCurrentAndNoncurrent"],
    # Hertz presents accrued liabilities as one line in some filings and splits out accrued salaries in others;
    # the pack line is the sum of whichever components the filing shows (they never appear alongside a combined total).
    "Accrued liabilities": ("sum", ["us-gaap:AccruedLiabilitiesCurrentAndNoncurrent", "us-gaap:OtherAccruedLiabilitiesCurrentAndNoncurrent", "us-gaap:AccruedSalariesCurrent", "us-gaap:EmployeeRelatedLiabilitiesCurrentAndNoncurrent"]),
    "Income taxes payable": ["us-gaap:TaxesPayableCurrentAndNoncurrent"],
    "Total liabilities": ["us-gaap:Liabilities"],
    "Preferred stock": ["us-gaap:PreferredStockValue"],
    "Common equity": ["us-gaap:StockholdersEquity"],
    "Non-controlling interests": ["us-gaap:MinorityInterest"],
    "Total equity": ["us-gaap:StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest", "us-gaap:StockholdersEquity"],
}
CF_MAP = {
    "Net income": ["us-gaap:ProfitLoss"],
    "Depreciation and amortization": ("sum", [["htz:CostOfServicesDepreciationAsAdjustedForGainLossUponDisposal", "us-gaap:CostOfServicesDepreciation"], "us-gaap:DepreciationNonproduction", "us-gaap:AmortizationOfIntangibleAssets"]),
    "Stock-based compensation": ["us-gaap:ShareBasedCompensation"],
    "Change in receivables": ["us-gaap:IncreaseDecreaseInAccountsReceivable"],
    "Change in payables": ["us-gaap:IncreaseDecreaseInAccountsPayable"],
    "Change in accrued liabilities": ["us-gaap:IncreaseDecreaseInAccruedLiabilities"],
    "Cash from operations": ["us-gaap:NetCashProvidedByUsedInOperatingActivities", "us-gaap:NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"],
    "Capital expenditures (PP&E)": ["us-gaap:PaymentsToAcquireOtherPropertyPlantAndEquipment"],
    "Purchases of equipment held for rental or lease": ["htz:PaymentsToAcquireRevenueEarningEquipment"],
    "Proceeds from disposal of equipment held for rental or lease": ["htz:ProceedsFromSaleOfRevenueEarningEquipment"],
    "Acquisitions, net of cash": ["us-gaap:PaymentsToAcquireBusinessesNetOfCashAcquired"],
    "Proceeds from disposals": ["us-gaap:ProceedsFromSaleOfOtherPropertyPlantAndEquipment"],
    "Cash from investing": ["us-gaap:NetCashProvidedByUsedInInvestingActivities", "us-gaap:NetCashProvidedByUsedInInvestingActivitiesContinuingOperations"],
    "Debt issued": ["us-gaap:ProceedsFromIssuanceOfLongTermDebt"],
    "Debt repaid": ["us-gaap:RepaymentsOfLongTermDebt"],
    "Stock issued": ("sum", ["us-gaap:ProceedsFromIssuanceOfCommonStock", "us-gaap:ProceedsFromStockOptionsExercised", "us-gaap:ProceedsFromIssuanceOfSharesUnderIncentiveAndShareBasedCompensationPlans"]),
    "Stock repurchased": ["us-gaap:PaymentsForRepurchaseOfCommonStock"],
    "Cash from financing": ["us-gaap:NetCashProvidedByUsedInFinancingActivities", "us-gaap:NetCashProvidedByUsedInFinancingActivitiesContinuingOperations"],
    "Interest paid": ["us-gaap:InterestPaidNet"],
    "Income taxes paid": ["us-gaap:IncomeTaxesPaid"],
    "Effect of exchange rates": ["us-gaap:EffectOfExchangeRateOnCashAndCashEquivalents", "us-gaap:EffectOfExchangeRateOnCashAndCashEquivalentsContinuingOperations"],
    "Net change in cash": ["us-gaap:CashAndCashEquivalentsPeriodIncreaseDecrease", "us-gaap:NetCashProvidedByUsedInContinuingOperations"],
}
USED = set()

# ---- template line order (pack spec)
import importlib.util
spec = importlib.util.spec_from_file_location("tmpl", HERE.parents[2] / "tools" / "make_template.py")
T = importlib.util.module_from_spec(spec); spec.loader.exec_module(T)

# ---- filings and periods
def quarter_end(y, q): return date(y, 3 * q, [31, 30, 30, 31][q - 1]).isoformat()
QUARTERS = [(y, q) for y in (2011, 2012, 2013) for q in (1, 2, 3, 4)]
YEARS = [2009, 2010, 2011, 2012, 2013]
QL = [f"Q{q} FY{y}" for y, q in QUARTERS]
YL = [f"FY{y}" for y in YEARS]


def block(period_end: str, form: str, kind: str):
    for b in parsed:
        if b["period"] == period_end and b["form"] == form and b["kind"] == kind:
            return b
    return None


def table(b):
    t = {}
    if not b:
        return t
    for kind, label, el, per, v in b["rows"]:
        key = el or label
        per = tuple(per)
        t.setdefault(key, {}).setdefault(per, v)  # first occurrence per element and period
        t.setdefault("__label__" + key, label)
    return t


def norm_shares(el, v):
    """Share counts appear in millions in some filings and thousands in others; normalize to millions."""
    if v is not None and "SharesOutstanding" in el:
        if v > 1e6:
            return v / 1e6
        if v > 1e4:
            return v / 1e3
    return v


def fetch(t, spec, per):
    """Return (value, elements_used) for a mapping spec at a period."""
    if isinstance(spec, tuple) and spec[0] == "sum":
        total, used = 0.0, []
        for part in spec[1]:
            v, u = fetch(t, part if isinstance(part, list) else [part], per)
            if v is not None:
                total += v
                used += u
        return (total, used) if used else (None, [])
    for opt in spec:
        if isinstance(opt, tuple):
            v, u = fetch(t, opt, per)
            if v is not None:
                return v, u
            continue
        if opt in t and per in t[opt]:
            return norm_shares(opt, t[opt][per]), [opt]
    return None, []


FILINGS = {}  # (form, period_end) -> filing meta
for b in parsed:
    FILINGS[(b["form"], b["period"])] = {"acc": b["acc"], "filed": b["filed"]}


def fid(form, pe):
    f = FILINGS.get((form, pe))
    return f"{form} for period ended {pe} (accession {f['acc']}, filed {f['filed']})" if f else "?"


def dur(start, end): return ("D", start, end)


def q_value(kind, spec, y, q):
    """Discrete quarter value, as originally reported, plus a locator string."""
    pe = quarter_end(y, q)
    if kind == "BS":
        form = "10-K" if q == 4 else "10-Q"
        t = table(block(pe, form, "BS"))
        v, u = fetch(t, spec, ("I", pe))
        return v, u, fid(form, pe), False
    qs = date(y, 3 * q - 2, 1).isoformat()
    if kind == "IS" and q < 4:
        t = table(block(pe, "10-Q", "IS"))
        v, u = fetch(t, spec, dur(qs, pe))
        return v, u, fid("10-Q", pe), False
    # derived: YTD(this) - YTD(previous)
    ystart = date(y, 1, 1).isoformat()
    if q == 1:
        t = table(block(pe, "10-Q", kind))
        v, u = fetch(t, spec, dur(ystart, pe))
        return v, u, fid("10-Q", pe), False
    this_form = "10-K" if q == 4 else "10-Q"
    t1 = table(block(pe, this_form, kind))
    v1, u1 = fetch(t1, spec, dur(ystart, pe))
    ppe = quarter_end(y, q - 1)
    t0 = table(block(ppe, "10-Q", kind))
    v0, u0 = fetch(t0, spec, dur(ystart, ppe))
    if v1 is None or v0 is None:
        return None, [], "", True
    return v1 - v0, u1, f"derived: {fid(this_form, pe)} year to date minus {fid('10-Q', ppe)} year to date", True


def y_value(kind, spec, y):
    pe = date(y, 12, 31).isoformat()
    src_pe = pe if y >= 2010 else date(2010, 12, 31).isoformat()
    t = table(block(src_pe, "10-K", kind))
    per = ("I", pe) if kind == "BS" else dur(date(y, 1, 1).isoformat(), pe)
    v, u = fetch(t, spec, per)
    loc = fid("10-K", src_pe) + (" (comparative column; the FY2009 10-K has no rendered XBRL)" if y < 2010 else "")
    return v, u, loc


# ---- allowance from the receivables caption ("less allowance for doubtful accounts of $19,099 and $19,708")
def allowance(b, pe_first, pe_second):
    if not b:
        return {}
    for kind, label, el, per, v in b["rows"]:
        if el == "us-gaap:AccountsReceivableNet":
            nums = re.findall(r"\$\s?([\d,]+(?:\.\d+)?)", label)
            if len(nums) >= 2:
                sc = 0.001 if "," in nums[0] and "." not in nums[0] else 1.0
                return {pe_first: float(nums[0].replace(",", "")) * sc, pe_second: float(nums[1].replace(",", "")) * sc}
    return {}


def main():
    wb = Workbook(); wb.remove(wb.active)
    HEAD, FILL = Font(bold=True, color="FFFFFF"), PatternFill("solid", fgColor="223A55")
    loc_rows, tie = [], []

    def sheet(name, lines, cols):
        ws = wb.create_sheet(name); ws.append(["Line"] + cols)
        for c in ws[1]: c.font, c.fill = HEAD, FILL
        ws.column_dimensions["A"].width = 56; ws.freeze_panes = "B2"
        return ws

    for kind, lines, maps in (("IS", T.IS, {**IS_MAP, **IS_FROM_CF}), ("BS", T.BS, BS_MAP), ("CF", T.CF, CF_MAP)):
        for suffix, cols in (("_Q", QL), ("_A", YL)):
            ws = sheet(kind + suffix, lines, cols)
            for line in lines:
                row = [line]
                spec = maps.get(line)
                for i, col in enumerate(cols):
                    v, used, loc, derived = None, [], "", False
                    if spec is not None:
                        src_kind = "CF" if (kind == "IS" and line in IS_FROM_CF) else kind
                        if suffix == "_Q":
                            y, q = QUARTERS[i]
                            if line in ("Diluted EPS", "Diluted shares") and q == 4:
                                v = None
                            else:
                                v, used, loc, derived = q_value(src_kind, spec, y, q)
                        else:
                            v, used, loc = y_value(src_kind, spec, YEARS[i])
                        if v is not None:
                            v = round(v, 4) if line == "Diluted EPS" else round(v, 1)
                            USED.update(used)
                            note = ("derived" if derived or len(used) > 1 else "")
                            how = (" + ".join(used) if len(used) > 1 else used[0]) + ("" if src_kind == kind else " (from the cash flow statement)")
                            loc_rows.append([kind + suffix, line, col, "P1-source: " + loc, "face of statement", "Y" if note else "N", how])
                    row.append(v)
                ws.append(row)
            # Hertz reports income tax as "(Provision) benefit"; the spec wants expense as a positive number.
            if kind == "IS":
                r = {c.value: c.row for c in ws["A"]}
                for ci in range(2, len(cols) + 2):
                    pt, ni = ws.cell(r["Pre-tax income"], ci).value, ws.cell(r["Net income"], ci).value
                    if pt is not None and ni is not None:
                        ws.cell(r["Income tax expense"], ci).value = round(pt - ni, 1)
                        loc_rows.append([kind + suffix, "Income tax expense", cols[ci - 2], "derived from the same statement", "", "Y", "Pre-tax income minus net income; the statement presents it as (provision) benefit"])

    # allowance for doubtful accounts into BS sheets and NOTES
    for suffix, cols in (("_Q", QL), ("_A", YL)):
        ws = wb[f"BS{suffix}"]; r = {c.value: c.row for c in ws["A"]}
        for i, col in enumerate(cols):
            if suffix == "_Q":
                y, q = QUARTERS[i]; pe = quarter_end(y, q); form = "10-K" if q == 4 else "10-Q"
                prev = quarter_end(y - 1, 4)
            else:
                y = YEARS[i]; pe = date(y, 12, 31).isoformat(); form = "10-K"; prev = date(y - 1, 12, 31).isoformat()
            src_pe = pe if y >= 2010 else "2010-12-31"
            a = allowance(block(src_pe, form, "BS"), src_pe, prev)
            if pe in a:
                ws.cell(r["Allowance for credit losses"], i + 2).value = round(a[pe], 1)
                loc_rows.append([f"BS{suffix}", "Allowance for credit losses", col, "P1-source: " + fid(form, src_pe), "receivables caption on the balance sheet", "N", "parsed from the caption 'less allowance for doubtful accounts of ...'"])

    # EXTRA: every face line whose element was not mapped
    ex = wb.create_sheet("EXTRA"); ex.append(["Statement", "Company label", "Element"] + QL + YL)
    for c in ex[1]: c.font, c.fill = HEAD, FILL
    ex.column_dimensions["B"].width = 60; ex.column_dimensions["C"].width = 50
    elements = {}
    for b in parsed:
        for kind, label, el, per, v in b["rows"]:
            if el and el not in USED and not el.endswith("Abstract"):
                elements.setdefault((kind, el), label)
    for (kind, el), label in sorted(elements.items()):
        row = [kind, label, el]
        for i in range(len(QL)):
            y, q = QUARTERS[i]
            v = q_value(kind, [el], y, q)[0] if not (kind == "CF" and "CashAndCashEquivalentsAtCarryingValue" in el) else None
            row.append(round(v, 1) if v is not None else None)
        for y in YEARS:
            v = y_value(kind, [el], y)[0] if "CashAndCashEquivalentsAtCarryingValue" not in el else None
            row.append(round(v, 1) if v is not None else None)
        if any(x is not None for x in row[3:]):
            ex.append(row)

    # NOTES (only what the statements carry; the rest is in the note text files)
    ns = wb.create_sheet("NOTES"); ns.append(["Line"] + QL + YL)
    for c in ns[1]: c.font, c.fill = HEAD, FILL
    ns.column_dimensions["A"].width = 56
    for line in T.NOTES:
        row = [line] + [None] * (len(QL) + len(YL))
        if line == "Allowance: provision":
            for i in range(len(QL)):
                y, q = QUARTERS[i]; row[1 + i] = (lambda v: round(v, 1) if v is not None else None)(q_value("CF", ["us-gaap:ProvisionForDoubtfulAccounts"], y, q)[0])
            for j, y in enumerate(YEARS):
                row[1 + len(QL) + j] = (lambda v: round(v, 1) if v is not None else None)(y_value("CF", ["us-gaap:ProvisionForDoubtfulAccounts"], y)[0])
        ns.append(row)

    # NONGAAP: left for the release text files
    ng = wb.create_sheet("NONGAAP"); ng.append(["Measure", "Reconciling line (company's label)"] + QL)
    for c in ng[1]: c.font, c.fill = HEAD, FILL
    ng.append(["Not tabulated in this pack", "The reconciliations are in the earnings release text files (releases/ER-*.txt). See manifest, known limits."])

    # RESTATED: annual lines as reprinted in the next 10-K
    rs = wb.create_sheet("RESTATED"); rs.append(["Statement", "Line", "Year restated", "As originally reported", "As shown in the later annual report", "Difference", "Later report"])
    for c in rs[1]: c.font, c.fill = HEAD, FILL
    rs.column_dimensions["B"].width = 56
    for kind, maps in (("IS", IS_MAP), ("BS", BS_MAP), ("CF", CF_MAP)):
        for line, spec in maps.items():
            for y in (2010, 2011, 2012):
                pe = date(y, 12, 31).isoformat(); later = date(y + 1, 12, 31).isoformat()
                per = ("I", pe) if kind == "BS" else dur(date(y, 1, 1).isoformat(), pe)
                v0 = fetch(table(block(pe, "10-K", kind)), spec, per)[0]
                v1 = fetch(table(block(later, "10-K", kind)), spec, per)[0]
                if v0 is not None and v1 is not None:
                    rs.append([kind, line, f"FY{y}", round(v0, 1), round(v1, 1), round(v1 - v0, 1), fid("10-K", later)])

    lc = wb.create_sheet("LOCATORS"); lc.append(["Sheet", "Line", "Period", "Source file ID", "Page or note", "Derived (Y/N)", "How derived"])
    for c in lc[1]: c.font, c.fill = HEAD, FILL
    for r in loc_rows: lc.append(r)

    # ---- tie-out on the workbook
    def col(ws, line):
        r = {c.value: c.row for c in ws["A"]}[line]
        return [ws.cell(r, ci).value for ci in range(2, ws.max_column + 1)]
    for suffix, cols in (("_Q", QL), ("_A", YL)):
        bs = wb[f"BS{suffix}"]
        ta, tl, te = col(bs, "Total assets"), col(bs, "Total liabilities"), col(bs, "Total equity")
        for c, a, l, e in zip(cols, ta, tl, te):
            if None in (a, l, e):
                tie.append(f"BS{suffix} {c}: cannot test (assets {a}, liabilities {l}, equity {e})")
            elif abs(a - l - e) > 0.2:
                tie.append(f"BS{suffix} {c}: FAIL assets {a} vs liabilities + equity {round(l + e, 1)}")
        cf = wb[f"CF{suffix}"]
        o, i_, f, fx, nc = (col(cf, x) for x in ("Cash from operations", "Cash from investing", "Cash from financing", "Effect of exchange rates", "Net change in cash"))
        for c, *vals in zip(cols, o, i_, f, fx, nc):
            if None in vals[:3] or vals[4] is None:
                tie.append(f"CF{suffix} {c}: cannot test ({vals})")
            elif abs(sum(v or 0 for v in vals[:4]) - vals[4]) > 0.2:
                tie.append(f"CF{suffix} {c}: FAIL sections sum {round(sum(v or 0 for v in vals[:4]), 1)} vs net change {vals[4]}")
    # quarters sum to years, flow lines
    for kind in ("IS", "CF"):
        wq, wa = wb[f"{kind}_Q"], wb[f"{kind}_A"]
        for line in ([l for l in T.IS if l in IS_MAP or l in IS_FROM_CF] if kind == "IS" else list(CF_MAP)):
            if line in ("Diluted EPS", "Diluted shares"):
                continue
            q, a = col(wq, line), col(wa, line)
            for yi, y in enumerate((2011, 2012, 2013)):
                qs = q[yi * 4:(yi + 1) * 4]; av = a[YEARS.index(y)]
                if None not in qs and av is not None and abs(sum(qs) - av) > 0.2:
                    tie.append(f"{kind} {line} FY{y}: FAIL quarters {round(sum(qs), 1)} vs year {av}")

    PACK.mkdir(exist_ok=True)
    wb.save(PACK / "statements.xlsx")
    (HERE / "tieout.md").write_text("# Workbook tie-out\n\n" + ("\n".join(f"- {t}" for t in tie) or "All tests passed.") + "\n")
    print("saved", PACK / "statements.xlsx"); print("tie-out issues:", len(tie)); print("\n".join(tie[:40]))


if __name__ == "__main__":
    main()
