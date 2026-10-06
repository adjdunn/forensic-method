"""Build one test-data folder per company from SEC EDGAR.

Each folder gets what a user of the five prompts would attach:
  statements.xlsx               income statement, balance sheet, cash flow, annual and quarterly,
                                as presented by the company and as originally reported
  annual-report-<FY>.txt        the last two annual reports, as text with [p. N] page markers
  annual-report-<FY>-key-sections.txt   Items 1A, 3, 7, 8 and 9A only (10-K filers), for chat size limits
  earnings-release-Q4-<FY>.txt  the fourth-quarter results release for the same two years
  README.md                     what is here, where it came from, what to attach for each prompt

Usage: python build.py [slug ...]      (no slug = all companies)
Downloads are cached in _build/cache/ so reruns do not hit EDGAR again.
"""
import html, json, re, sys, time, urllib.error, urllib.request
from datetime import date, timedelta
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill

import htmltext

HERE = Path(__file__).parent
ROOT = HERE.parent
CACHE = HERE / "cache"
_src = Path("C:/Users/aaron/Dev/wiresift-valuation/scripts/valuation_core.py").read_text(encoding="utf-8")
UA = re.search(r'^UA\s*=\s*["\'](.+?)["\']', _src, re.M).group(1)

COMPANIES = {
    "hertz-fy2013": dict(
        name="Hertz Global Holdings, Inc.", cik=1364479, start="2012-01-01", asof="2014-03-31",
        profile="US GAAP. Resolved SEC case (order December 2018): subrogation allowances, undisclosed extension of fleet holding periods, reaffirmed guidance. Restated in 2015. EDGAR now lists this filer as Herc Holdings (the old Hertz Global Holdings renamed after the 2016 spin-off); the filings are Hertz's.",
        answer_key="../../tests/hertz-fy2013/answer-key.md"),
    "under-armour-fy2016": dict(
        name="Under Armour, Inc.", cik=1336917, start="2015-01-01", asof="2017-03-31",
        profile="US GAAP. Resolved SEC case (order May 2021): undisclosed pull-forwards of next-quarter orders, Q3 2015 to Q4 2016. The order makes no finding that GAAP was violated."),
    "kraft-heinz-fy2017": dict(
        name="The Kraft Heinz Company", cik=1637459, start="2016-01-01", asof="2018-12-31",
        profile="US GAAP. Resolved SEC case (order September 2021): supplier cost savings recognized early, lowering cost of sales and lifting Adjusted EBITDA, Q4 2015 to 2018. Restated in 2019. The 2015 merger is in the comparatives."),
    "home-depot-fy2025": dict(
        name="The Home Depot, Inc.", cik=354950, start="2024-01-01", asof="2026-09-26",
        profile="US GAAP. No known enforcement case. Two large acquisitions in the window: SRS (fiscal 2024) and GMS (fiscal 2025, through SRS), per the fiscal 2025 10-K. The benign test: balance-sheet jumps that an acquisition explains."),
    "cae-fy2026": dict(
        name="CAE Inc.", cik=1173382, start="2024-04-01", asof="2026-09-26",
        profile="IFRS, Canadian, files a 40-F with the SEC. No known enforcement case. The workbook is annual only: the build reads 10-Q and annual-report XBRL, and CAE files its quarterly reports on Form 6-K."),
}

HEAD_FONT, HEAD_FILL = Font(bold=True, color="FFFFFF"), PatternFill("solid", fgColor="223A55")
DERIVED_FONT, DERIVED_FILL = Font(italic=True), PatternFill("solid", fgColor="FFF4D6")
MONTHS = {m: i for i, m in enumerate(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], 1)}
KIND_NAME = {"IS": "Income statement", "BS": "Balance sheet", "CF": "Cash flow"}


# ---------------------------------------------------------------- download
_last = [0.0]


def get(url: str, cache_path: Path) -> bytes:
    if cache_path.exists():
        return cache_path.read_bytes()
    for attempt in range(6):
        wait = 0.15 if attempt == 0 else 0.5 * 2 ** attempt
        time.sleep(max(0, _last[0] + wait - time.time()))
        _last[0] = time.time()
        try:
            b = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=120).read()
            cache_path.parent.mkdir(parents=True, exist_ok=True)
            cache_path.write_bytes(b)
            return b
        except urllib.error.HTTPError as e:
            if e.code in (429, 503) and attempt < 5:
                continue
            raise


def submissions(slug, cik):
    base = CACHE / slug / "submissions"
    s = json.loads(get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json", base / "main.json"))
    blocks = [s["filings"]["recent"]]
    for f in s["filings"].get("files", []):
        blocks.append(json.loads(get(f"https://data.sec.gov/submissions/{f['name']}", base / f["name"])))
    out = []
    for b in blocks:
        for i in range(len(b["accessionNumber"])):
            out.append({"form": b["form"][i], "filed": b["filingDate"][i], "acc": b["accessionNumber"][i],
                        "doc": b["primaryDocument"][i], "period": b["reportDate"][i], "items": b.get("items", [""] * 99999)[i]})
    return s["name"], sorted(out, key=lambda x: x["filed"])


def base_url(cik, acc):
    return f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-', '')}/"


def filing_index(slug, cik, acc):
    """[(type, description, filename)] from the filing's -index.htm."""
    h = get(base_url(cik, acc) + f"{acc}-index.htm", CACHE / slug / acc / "index.htm").decode("utf-8", "replace")
    out = []
    for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", h, re.S):
        tds = re.findall(r"<td[^>]*>(.*?)</td>", tr, re.S)
        href = re.search(r'href="([^"]+)"', tr)
        if len(tds) >= 4 and href:
            fn = href.group(1).split("/")[-1].replace("ix?doc=", "")
            out.append((re.sub(r"<[^>]+>", "", tds[3]).strip(), re.sub(r"<[^>]+>", "", tds[1]).strip(), fn))
    return out


# ---------------------------------------------------------------- parse rendered statements (R files)
def decode(b: bytes) -> str:
    try:
        return b.decode("utf-8")
    except UnicodeDecodeError:
        return b.decode("cp1252", "replace")


def clean(s: str) -> str:
    s = re.sub(r'<span style="display: ?none[^"]*">.*?</span>', " ", s, flags=re.S)
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", html.unescape(s)).replace("�", "'").strip()


def num(s: str):
    s = re.sub(r"\[\d+\]", "", s).replace("$", "").replace(",", "").replace("\xa0", " ").strip()
    s = re.sub(r"^[A-Z]{1,3}\s", "", s)
    if not s or s in ("-", "—", "–"):
        return None
    neg = s.startswith("(") and s.endswith(")")
    try:
        v = float(s.strip("()").strip())
    except ValueError:
        return None
    return -v if neg else v


def find_date(s: str):
    m = re.search(r"([A-Z][a-z]{2})\.? (\d{1,2}), (\d{4})", s)
    return date(int(m.group(3)), MONTHS[m.group(1)], int(m.group(2))).isoformat() if m and m.group(1) in MONTHS else None


def scale_of(title: str) -> float:
    t = re.sub(r"shares in \w+", "", title.lower())
    for k, v in (("in thousands", 0.001), ("in millions", 1.0), ("in billions", 1000.0)):
        if k in t:
            return v
    return 1e-6


def currency_of(title: str) -> str:
    m = re.search(r"\b([A-Z]{3}) \(", title)
    return m.group(1) if m else "USD"


def months_between(s: str, e: str) -> int:
    return max(1, round(((date.fromisoformat(e) - date.fromisoformat(s)).days + 1) / 30.44))


def is_per_share(el: str, label: str) -> bool:
    l = label.lower()
    return "PerShare" in el or "per share" in l or "per common share" in l


def is_shares(el: str, label: str) -> bool:
    l = label.lower()
    return not is_per_share(el, label) and ("NumberOfShares" in el or "SharesOutstanding" in el or "(in shares)" in l)


def is_unscaled(el: str, label: str) -> bool:
    return is_per_share(el, label) or is_shares(el, label)


def share_scale(title: str) -> float:
    """Share counts to millions."""
    t = title.lower()
    m = re.search(r"shares in (thousands|millions|billions)", t)
    if m:
        return {"thousands": 0.001, "millions": 1.0, "billions": 1000.0}[m.group(1)]
    if re.search(r"except (share|shares)", t):
        return 1e-6
    if re.search(r"\([A-Z]{3} \$\)", title):  # older renderer: shares follow the stated scale
        return scale_of(title) if scale_of(title) != 1e-6 else 1e-6
    return 1e-6


def with_sections(rows):
    """Where an element appears more than once in a statement (share classes, segments), add the heading it sits under."""
    counts = {}
    for key, *_ in rows:
        counts[key.split("#")[0]] = counts.get(key.split("#")[0], 0) + 1
    return [(key, f"{label} [{sec}]" if counts[key.split("#")[0]] > 1 and sec else label, vals) for key, label, vals, sec in rows]


def parse_htm(text: str, kind: str):
    tbl = re.search(r'<table class="report".*?</table>', text, re.S)
    tbl = tbl.group(0) if tbl else text
    trs = re.findall(r"<tr[^>]*>(.*?)</tr>", tbl, re.S)
    title, rows_exp = "", []
    for t in (t for t in trs if "<th" in t):
        exp = []
        for m in re.finditer(r"<th\b([^>]*)>(.*?)</th>", t, re.S):
            if 'class="tl"' in m.group(1):
                title = clean(m.group(2))
                continue
            span = re.search(r'colspan="?(\d+)', m.group(1))
            exp += [clean(m.group(2))] * int(span.group(1) if span else 1)
        rows_exp.append(exp)
    ncols = max((len(r) for r in rows_exp), default=0)
    cols = []
    for i in range(ncols):
        texts = [r[i] for r in rows_exp if i < len(r) and r[i]]
        mon = next((int(m.group(1)) for t in texts for m in [re.search(r"(\d+) Months Ended", t)] if m), None)
        d = next((find_date(t) for t in texts if find_date(t)), None)
        other = [t for t in texts if not re.search(r"Months Ended", t) and not find_date(t)]
        if not d or other:
            cols.append(None)  # a member column (restatement split, segment) or no date: skip
        elif kind == "BS" or not mon:
            cols.append(("I", d))
        else:
            cols.append(("D", mon, d))
    scale, cur = scale_of(title), currency_of(title)
    rows, seen, section, member = [], {}, "", False
    for t in (t for t in trs if "<td" in t):
        tds = re.findall(r"<td\b[^>]*>(.*?)</td>", t, re.S)
        if not tds:
            continue
        m = re.search(r"defref_([A-Za-z0-9-]+?)_(\w+)", tds[0])
        if not any(num(clean(c)) is not None for c in tds[1:]):
            # a member heading (share class, segment) labels the rows under it; an abstract heading only
            # until the first member heading
            if re.search(r"defref_[^'\"]*=", tds[0]):
                section, member = clean(tds[0]).replace(" [Member]", ""), True
            elif clean(tds[0]) and not member:
                section = clean(tds[0])
            continue
        if not m:
            continue
        el = f"{m.group(1)}:{m.group(2)}"
        seen[el] = seen.get(el, 0) + 1
        key = el if seen[el] == 1 else f"{el}#{seen[el]}"
        label = clean(tds[0])
        vals = {}
        for i, c in enumerate(tds[1:]):
            if i >= len(cols) or cols[i] is None:
                continue
            v = num(clean(c))
            if v is None or cols[i] in vals:
                continue
            vals[cols[i]] = v if is_per_share(el, label) else v * (share_scale(title) if is_shares(el, label) else scale)
        rows.append((key, label, vals, section))
    return with_sections(rows), title, cur


def parse_xml(text: str, kind: str):
    """Old InstanceReport XML (filings to about 2011). NumericAmount is in whole units."""
    colsec = re.search(r"<Columns>(.*?)</Columns>", text, re.S).group(1)
    cols = {}
    for c in re.findall(r"<Column>(.*?)</Column>", colsec, re.S):
        cid = re.search(r"<Id>(\d+)</Id>", c).group(1)
        pt = re.search(r"<PeriodType>(.*?)</PeriodType>", c)
        e = re.search(r"<PeriodEndDate>(.*?)T", c)
        s = re.search(r"<PeriodStartDate>(.*?)T", c)
        labels = re.findall(r'<Label Id="\d+" Label="(.*?)"', c)
        if e and s and pt and pt.group(1) == "duration" and kind != "BS":
            cols[cid] = ("D", months_between(s.group(1), e.group(1)), e.group(1))
        elif e:
            cols[cid] = ("I", e.group(1))
        elif labels:
            d = find_date(labels[-1])
            m = re.match(r"(\d+) Months Ended", labels[0]) if len(labels) > 1 else None
            cols[cid] = ("D", int(m.group(1)), d) if m and kind != "BS" else ("I", d)
    rows, seen = [], {}
    for r in re.findall(r"<Row>(.*?)</Row>", text, re.S):
        el = re.search(r"<ElementName>(.*?)</ElementName>", r)
        if not el:
            continue
        el = el.group(1).replace("_", ":", 1)
        seen[el] = seen.get(el, 0) + 1
        key = el if seen[el] == 1 else f"{el}#{seen[el]}"
        label = html.unescape(re.search(r"<Label>(.*?)</Label>", r, re.S).group(1)).strip()
        vals = {}
        for c in re.findall(r"<Cell>(.*?)</Cell>", r, re.S):
            if "<IsNumeric>true</IsNumeric>" not in c:
                continue
            cid = re.search(r"<Id>(\d+)</Id>", c).group(1)
            if cid in cols and cols[cid] not in vals:
                v = float(re.search(r"<NumericAmount>(.*?)</NumericAmount>", c).group(1))
                vals[cols[cid]] = v if is_per_share(el, label) else v * 1e-6
        rows.append((key, label, vals, ""))
    return with_sections(rows), "", "USD"


def pick_reports(fs: str):
    found = {}
    for block in re.findall(r"<Report\b.*?</Report>", fs, re.S):
        long = re.search(r"<LongName>(.*?)</LongName>", block, re.S)
        fn = re.search(r"<HtmlFileName>(.*?)</HtmlFileName>", block) or re.search(r"<XmlFileName>(.*?)</XmlFileName>", block)
        if not (long and fn):
            continue
        low = html.unescape(long.group(1)).lower()
        if "parenthetical" in low or "- statement -" not in low:
            continue
        if "balance sheet" in low or "financial position" in low or "financial condition" in low:
            kind = "BS"
        elif "cash flow" in low:
            kind = "CF"
        elif any(w in low for w in ("operations", "income", "earnings", "loss")) and "equity" not in low and "comprehensive" not in low:
            kind = "IS"
        else:
            continue
        found.setdefault(kind, (long.group(1).strip(), fn.group(1)))  # first report of each kind
    return found


def statement_filings(slug, cik, filings, annual_form):
    out = []
    for f in filings:
        if f["form"] not in (annual_form, "10-Q"):
            continue
        d = CACHE / slug / f["acc"]
        try:
            fs = get(base_url(cik, f["acc"]) + "FilingSummary.xml", d / "FilingSummary.xml").decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            print("  no FilingSummary", f["form"], f["period"], e.code)
            continue
        f = dict(f, tables={}, titles={}, currency=None)
        for kind, (name, fn) in pick_reports(fs).items():
            raw = decode(get(base_url(cik, f["acc"]) + fn, d / fn))
            rows, title, cur = parse_xml(raw, kind) if fn.endswith(".xml") else parse_htm(raw, kind)
            f["tables"][kind] = rows
            f["titles"][kind] = name
            f["currency"] = f["currency"] or cur
        print(f"  {f['form']:5} {f['period']} filed {f['filed']} {sorted(f['tables'])}")
        out.append(f)
    return out


# ---------------------------------------------------------------- assemble
class Store:
    """Every (kind, row key, period) value from every filing, oldest filing first."""

    def __init__(self, sf):
        self.sf = sorted(sf, key=lambda f: f["filed"])
        self.vals = {}   # (kind, key, per) -> [(filing, value)]
        self.labels = {}  # (kind, key) -> latest label
        for f in self.sf:
            for kind, rows in f["tables"].items():
                for key, label, vals in rows:
                    self.labels[(kind, key)] = label
                    for per, v in vals.items():
                        self.vals.setdefault((kind, key, per), []).append((f, v))
        # the filing that first reported each period, per statement
        self.origin = {}
        for (kind, key, per), lst in self.vals.items():
            f = lst[0][0]
            cur = self.origin.get((kind, per))
            if cur is None or f["filed"] < cur["filed"]:
                self.origin[(kind, per)] = f

    def first(self, kind, key, per):
        """The value as originally reported: from the filing that first reported the period. A line that only
        appears for that period in a later filing (a line split out or added afterwards) returns nothing here,
        so it is not added on top of the original line it was carved from; it is listed on the Revisions sheet."""
        x = self.vals.get((kind, key, per))
        if not x or x[0][0] is not self.origin.get((kind, per)):
            return (None, None)
        return (x[0][1], x[0][0])

    def added_later(self):
        """(kind, key, per, value, filing) for lines that first appear for a period in a later filing."""
        return [(kind, key, per, lst[0][1], lst[0][0]) for (kind, key, per), lst in self.vals.items()
                if lst[0][0] is not self.origin.get((kind, per))]

    def order(self, kind, forms):
        master = []
        for f in reversed(self.sf):
            if f["form"] not in forms or kind not in f["tables"]:
                continue
            prev = None
            for key, _, _ in f["tables"][kind]:
                if key not in master:
                    master.insert(master.index(prev) + 1 if prev in master else (0 if prev is None else len(master)), key)
                prev = key
        return master


def fiscal_periods(store, annual_form):
    fy = sorted({per[2] for (kind, key, per) in store.vals if kind == "IS" and per[0] == "D" and per[1] == 12
                 and any(f["form"] == annual_form for f, _ in store.vals[(kind, key, per)])})
    q3m = sorted({per[2] for (kind, key, per) in store.vals if kind == "IS" and per[0] == "D" and per[1] == 3})
    quarters = []  # (qnum, end, prev_end_in_year or None, fy_end or None)
    for e in q3m:
        prev_fy = max((x for x in fy if x < e), default=None)
        if prev_fy is None:
            continue
        qn = round((date.fromisoformat(e) - date.fromisoformat(prev_fy)).days / 91.3)
        if 1 <= qn <= 3:
            quarters.append((qn, e))
    for e in fy:
        prev_fy = max((x for x in fy if x < e), default=None)
        nine = [per[2] for (kind, key, per) in store.vals if kind == "IS" and per[0] == "D" and per[1] == 9 and prev_fy and prev_fy < per[2] < e]
        if nine:
            quarters.append((4, e))
    quarters.sort(key=lambda q: q[1])
    return fy, quarters


BALANCE_ROW = re.compile(r"(beginning|end) of (the )?(period|year|quarter)|, beginning|, ending|, end$", re.I)


def build_workbook(slug, cfg, store, annual_form, out_path):
    fy, quarters = fiscal_periods(store, annual_form)
    q3m = {e for _, e in quarters}
    wb = Workbook()
    wb.remove(wb.active)
    sources, revisions, cross_revisions = [], [], []
    cur = next((f["currency"] for f in store.sf if f["currency"]), "USD")

    def header(ws, cols):
        ws.append(["Line"] + cols + ["XBRL element"])
        for c in ws[1]:
            c.font, c.fill = HEAD_FONT, HEAD_FILL
        ws.column_dimensions["A"].width = 62
        ws.freeze_panes = "B2"

    def ytd_start(e):
        return [q for q in quarters if q[1] == e][0][0] * 3

    def prev_q(e):
        qn = [q for q in quarters if q[1] == e][0][0]
        cands = [x for n, x in quarters if n == qn - 1 and x < e]
        return max(cands) if cands else None

    def qvalue(kind, key, e):
        label = store.labels[(kind, key)]
        unscaled = is_unscaled(key, label)
        if kind == "BS":
            v, f = store.first(kind, key, ("I", e))
            return v, [f] if f else [], False
        qn = [q for q in quarters if q[1] == e][0][0]
        if kind == "IS" and qn < 4:
            v, f = store.first(kind, key, ("D", 3, e))
            if v is not None:
                return v, [f], False
        if qn == 1:
            v, f = store.first(kind, key, ("D", 3, e))
            return v, [f] if f else [], False
        if unscaled or (kind == "CF" and BALANCE_ROW.search(label)):
            return None, [], False
        p = prev_q(e)
        v1, f1 = store.first(kind, key, ("D", qn * 3, e))
        v0, f0 = store.first(kind, key, ("D", (qn - 1) * 3, p)) if p else (None, None)
        if v1 is None or v0 is None:
            return None, [], False
        return v1 - v0, [f1, f0], True

    def avalue(kind, key, e):
        per = ("I", e) if kind == "BS" else ("D", 12, e)
        v, f = store.first(kind, key, per)
        return v, [f] if f else [], False

    def fdesc(f):
        return f"{f['form']} for the period ended {f['period']}, filed {f['filed']} (accession {f['acc']})"

    for kind in ("IS", "BS", "CF"):
        for scope, cols, fn, forms in (("annual", fy, avalue, (annual_form,)),
                                       ("quarterly", [e for _, e in quarters], qvalue, ("10-Q", annual_form))):
            if not cols:
                continue
            labels = [f"FY (ended {e})" if scope == "annual" else f"Q{[q for q in quarters if q[1] == e][0][0]} (ended {e})" for e in cols]
            ws = wb.create_sheet(f"{kind} {scope}")
            header(ws, labels)
            col_src = {c: set() for c in labels}
            col_derived = {c: False for c in labels}
            built = []
            for key in store.order(kind, forms):
                label = store.labels[(kind, key)]
                row, derived_cells = [label], []
                for ci, e in enumerate(cols):
                    v, fs, der = fn(kind, key, e)
                    if v is not None:
                        v = round(v, 4) if is_per_share(key, label) else round(v, 1)
                        col_src[labels[ci]].update(fdesc(f) for f in fs if f)
                        if der:
                            derived_cells.append(ci)
                            col_derived[labels[ci]] = True
                    row.append(v)
                if all(x is None for x in row[1:]):
                    continue
                # same label under a new XBRL element (a standard change, e.g. revenue under ASC 606): one row
                el = key.split("#")[0]
                twin = next((b for b in built if b[0][0].lower() == label.lower() and el not in b[1].split(" / ")), None)
                conflicts = [i for i, (x, y) in enumerate(zip(twin[0][1:], row[1:])) if x is not None and y is not None and abs(x - y) >= 0.05] if twin else []
                if twin and len(conflicts) <= 2:
                    # the row whose data starts earlier keeps its values where both report (as originally reported)
                    start = lambda r: next(i for i, x in enumerate(r[1:]) if x is not None)
                    old, new = (twin[0], row) if start(twin[0]) <= start(row) else (row, twin[0])
                    for i in conflicts:
                        cross_revisions.append([KIND_NAME[kind], label, f"{twin[1]} / {el}", f"{labels[i]} ({scope})", old[i + 1],
                                                "earlier filing, before the XBRL element changed", new[i + 1],
                                                "later filing, under the new element", round(new[i + 1] - old[i + 1], 4)])
                    twin[0][1:] = [x if x is not None else y for x, y in zip(old[1:], new[1:])]
                    twin[2].update(derived_cells)
                    twin[1] += " / " + el
                    continue
                built.append([row, key.split("#")[0], set(derived_cells)])
            keep = [ci for ci in range(len(cols)) if any(r[0][ci + 1] is not None for r in built)]
            ws.delete_rows(1)
            header(ws, [labels[ci] for ci in keep])
            for row, els, derived_cells in built:
                ws.append([row[0]] + [row[ci + 1] for ci in keep] + [els])
                for j, ci in enumerate(keep):
                    if ci in derived_cells:
                        cell = ws.cell(ws.max_row, j + 2)
                        cell.font, cell.fill = DERIVED_FONT, DERIVED_FILL
            for c in (labels[ci] for ci in keep):
                how = "Derived cells (shaded): year to date in the later filing minus year to date in the earlier one." if col_derived[c] else ""
                sources.append([ws.title, c, "; ".join(sorted(col_src[c])), how])

    # revisions: the same line and period shown differently in a later filing
    periods = {("I", e) for e in fy} | {("D", 12, e) for e in fy} | {("I", e) for e in q3m} | {("D", m, e) for e in q3m for m in (3, 6, 9)}
    for (kind, key, per), lst in store.vals.items():
        if per not in periods or len(lst) < 2:
            continue
        f0, v0 = lst[0]
        label = store.labels[(kind, key)]
        tol = 0.005 if is_per_share(key, label) else 0.5
        for f1, v1 in lst[1:]:
            if abs(v1 - v0) > tol:
                pdesc = f"as at {per[1]}" if per[0] == "I" else f"{per[1]} months ended {per[2]}"
                revisions.append([KIND_NAME[kind], label, key.split("#")[0], pdesc, round(v0, 4 if tol < 1 else 1), fdesc(f0),
                                  round(v1, 4 if tol < 1 else 1), fdesc(f1), round(v1 - v0, 4 if tol < 1 else 1)])
                break
    # A fourth quarter is worked out as the full year minus nine months. If the annual report changed figures for
    # earlier periods, the full year is on the revised basis and the nine months are as first reported, so the
    # derived quarter absorbs the corrections. Mark the lines affected, cell by cell; mark the whole column only
    # when a headline total (revenue, operating income, pre-tax or net income, operating cash flow) is affected.
    revising = {}  # kind -> annual accession -> set of XBRL elements whose earlier figures it changed
    for (kind, key, per), lst in store.vals.items():
        if per in periods and per[0] == "D" and len(lst) > 1 and not is_unscaled(key, store.labels[(kind, key)]):
            for f1, v1 in lst[1:]:
                if abs(v1 - lst[0][1]) > 0.5:
                    revising.setdefault(kind, {}).setdefault(f1["acc"], set()).add(key.split("#")[0])
    annual_acc = {f["period"]: f["acc"] for f in store.sf if f["form"] == annual_form}
    TOTALS = re.compile(r"NetIncomeLoss|ProfitLoss|IncomeLossFromContinuingOperationsBefore|OperatingIncomeLoss|GrossProfit|"
                        r"NetCashProvidedByUsedInOperatingActivities|:Revenues$|SalesRevenue|RevenueFromContractWithCustomer")
    MIXED_FILL = PatternFill("solid", fgColor="F8D7B0")
    mixed = []
    for kind in ("IS", "CF"):
        if f"{kind} quarterly" not in wb.sheetnames:
            continue
        ws = wb[f"{kind} quarterly"]
        elcol = ws.max_column
        for c in ws[1]:
            m = re.match(r"Q4 \(ended (\d{4}-\d{2}-\d{2})\)$", str(c.value or ""))
            els = revising.get(kind, {}).get(annual_acc.get(m.group(1))) if m else None
            if not els:
                continue
            hit = []
            for r in range(2, ws.max_row + 1):
                row_els = set(str(ws.cell(r, elcol).value or "").split(" / "))
                if row_els & els and ws.cell(r, c.column).value is not None:
                    ws.cell(r, c.column).fill = MIXED_FILL
                    hit.append(str(ws.cell(r, 1).value))
            if not hit:
                continue
            whole = any(TOTALS.search(e) for e in els)
            names = "; ".join(hit[:8]) + (f"; and {len(hit) - 8} more" if len(hit) > 8 else "")
            mixed.append(f"{ws.title}, {c.value}: {'the whole column, including headline totals' if whole else 'only these lines'}: {names}")
            c.value = c.value + (" [mixed basis]" if whole else f" [{len(hit)} line{'s' if len(hit) != 1 else ''} mixed basis]")
    rs = wb.create_sheet("Revisions")
    rs.append(["Statement", "Line (latest label)", "XBRL element", "Period", "As first reported", "First reported in",
               "As shown later", "Shown later in", "Difference"])
    for c in rs[1]:
        c.font, c.fill = HEAD_FONT, HEAD_FILL
    rs.column_dimensions["B"].width = 55
    for r in sorted(revisions, key=lambda r: (r[0], r[3])) + cross_revisions:
        rs.append(r)
    if not revisions and not cross_revisions:
        rs.append(["None found: every line and period in these filings was shown the same way each time it appeared."])
    # lines that a later filing shows for a period the original filing did not break out
    late = []
    for kind, key, per, v, f in store.added_later():
        if per not in periods or abs(v) < 0.05:
            continue
        label = store.labels[(kind, key)]
        # the same line under a renamed XBRL element is not a new line: skip it when the original filing
        # reported the same amount under the same label
        renamed = any(k2 != key and store.labels.get((kind, k2), "").lower() == label.lower()
                      and store.first(kind, k2, per)[0] is not None and abs(store.first(kind, k2, per)[0] - v) < 0.5
                      for (kd, k2, p2) in store.vals if kd == kind and p2 == per)
        if renamed:
            continue
        pdesc = f"as at {per[1]}" if per[0] == "I" else f"{per[1]} months ended {per[2]}"
        late.append([KIND_NAME[kind], label, key.split("#")[0], pdesc, "not shown as its own line", fdesc(store.origin[(kind, per)]),
                     round(v, 4 if is_per_share(key, label) else 1), fdesc(f), "line added later"])
    if late:
        rs.append([])
        rs.append(["Lines added later: a later filing shows these lines for a period whose original filing did not break them out (usually a line split out of another). They are left off the statement sheets for that period, so they are not counted on top of the line they came from."])
        for r in sorted(late, key=lambda r: (r[0], r[3], r[1])):
            rs.append(r)

    ss = wb.create_sheet("Sources")
    ss.append(["Sheet", "Column", "Values taken from", "Note"])
    for c in ss[1]:
        c.font, c.fill = HEAD_FONT, HEAD_FILL
    ss.column_dimensions["C"].width = 110
    for r in sources:
        ss.append(r)
    ss.append([])
    ss.append(["Filings used", "", "Link"])
    for f in store.sf:
        ss.append([f["form"], f"period ended {f['period']}, filed {f['filed']}", base_url(cfg["cik"], f["acc"]) + f["doc"]])

    about = wb.create_sheet("About", 0)
    lines = [
        [cfg["name"]],
        [f"Financial statements from SEC EDGAR filings made from {cfg['start']} to {cfg['asof']}."],
        [f"Units: {cur} millions, except per-share amounts (as presented) and share counts (millions of shares)."],
        ["Lines and labels are the company's own, as presented on the face of each statement. The last column gives the XBRL element."],
        ["As originally reported: each value comes from the first filing in the window that reported it. Later changes are listed on the Revisions sheet."],
        ["Quarterly sheets: quarters two and three of the cash flow, and quarter four of the income statement and cash flow, are derived by subtraction. Derived cells are shaded and in italics. Per-share amounts and share counts are not derived."],
        ["Where a company reclassified lines during a year, a derived quarter can mix the old and new presentation. The Revisions sheet shows every such change."],
        ["Balance sheets are period-end balances. Notes (allowance, inventory detail, useful lives) are in the annual report text, not here."],
        ["Sources sheet: the filing behind every column, with links."],
        ["Industry sheet: the matching industry row from Aswath Damodaran's public tables (receivables, inventory and payables as shares of sales; margins; capital spending against depreciation). Use it to judge whether a level is ordinary for the industry; the statement sheets show movements."],
    ]
    if mixed:
        lines.append(["Mixed-basis fourth quarters. A fourth quarter is the full year minus nine months; where the annual report changed a line's earlier figures, the full year is revised while the nine months are as first reported, so that line's quarter absorbs the change. Affected cells are shaded orange. A heading marked [mixed basis] means a headline total is affected: take that quarter from the results release. A heading marked with a number of lines (for example [1 line mixed basis]) means only the named lines are affected, usually a reclassification between two lines: the rest of the column, including its totals, is sound."])
        for mline in mixed:
            lines.append(["   " + mline])
    for l in lines:
        about.append(l)
    about["A1"].font = Font(bold=True, size=14)
    about.column_dimensions["A"].width = 150
    wb.save(out_path)
    return fy, quarters, len(revisions) + len(cross_revisions), cur


# ---------------------------------------------------------------- documents
ITEM_RE = re.compile(r"^\W*item\s*(\d{1,2}[a-c]?)\b", re.I | re.M)
KEEP = ["1", "1A", "3", "7", "8", "9A"]


def key_sections(text: str) -> str:
    heads = [(m.start(), m.group(1).upper()) for m in ITEM_RE.finditer(text)]
    # some filers repeat the heading on every page ("ITEM 7. ... (Continued)"): a run of the same item is one section
    heads = [h for i, h in enumerate(heads) if i == 0 or h[1] != heads[i - 1][1]]
    heads.append((len(text), "END"))
    best = {}
    for i, (pos, item) in enumerate(heads[:-1]):
        length = heads[i + 1][0] - pos
        if item in KEEP and length > best.get(item, (0, 0))[1]:
            best[item] = (pos, length)
    parts = []
    for item in KEEP:
        if item not in best:
            continue
        pos, length = best[item]
        before = text[:pos]
        pm = list(re.finditer(r"^\[p\. [^\]]+\]$", before, re.M))
        lead = (pm[-1].group(0) + "\n") if pm else ""
        parts.append(f"=== Item {item} ===\n{lead}{text[pos:pos + length].strip()}\n")
    # statements printed after Item 15 (F-pages) when Item 8 only points to them
    if "8" in best and best["8"][1] < 30000:
        f1 = re.search(r"^\[p\. F-1\]$", text, re.M)
        if f1:
            parts.append("=== Financial statements (F-pages) ===\n" + text[f1.start():].strip() + "\n")
    return "\n".join(parts)


def doc_text(slug, cik, acc, fn):
    raw = get(base_url(cik, acc) + fn, CACHE / slug / acc / fn)
    if fn.lower().endswith((".htm", ".html")):
        t, info = htmltext.apply_page_markers(htmltext.html_to_text(raw))
        return t, info
    return raw.decode("utf-8", "replace"), {"pages": 0, "mode": "plain"}


def doc_header(cfg, what, f, fn):
    return (f"{cfg['name']}\n{what}\nFiled with the SEC {f['filed']}, accession {f['acc']}\n"
            f"Source: {base_url(cfg['cik'], f['acc'])}{fn}\n"
            f"Converted from the filed HTML to text for testing. [p. N] marks the start of printed page N.\n"
            + "=" * 80 + "\n\n")


def annual_reports(slug, cfg, filings, annual_form, outdir, n=2):
    ann = [f for f in filings if f["form"] == annual_form][-n:]
    made = []
    for f in ann:
        fy = f["period"]
        if annual_form == "40-F":
            idx = filing_index(slug, cfg["cik"], f["acc"])
            texts = []
            for typ, desc, fn in sorted(idx, key=lambda x: x[0]):
                if not typ.startswith("EX-99") or not fn.lower().endswith((".htm", ".html")):
                    continue
                t, _ = doc_text(slug, cfg["cik"], f["acc"], fn)
                if len(t) > 20000:
                    desc = html.unescape(desc or fn)
                    texts.append((desc, f"########## Exhibit {typ}: {desc} ##########\n\n{t}"))
            body = "\n\n".join(t for _, t in texts)
            fname = f"annual-report-FY{fy}.txt"
            (outdir / fname).write_text(doc_header(cfg, f"Form 40-F annual report (annual information form, MD&A, audited statements) for the year ended {fy}", f, "") + body, encoding="utf-8")
            made.append((fname, len(body), f"40-F exhibits for the year ended {fy}: annual information form, MD&A, audited statements"))
            ks = "\n\n".join(t for d, t in texts if re.search(r"MD&A|DISCUSSION|FINANCIAL STATEMENTS", d, re.I))
            kname = f"annual-report-FY{fy}-key-sections.txt"
            (outdir / kname).write_text(doc_header(cfg, f"Form 40-F for the year ended {fy}: MD&A (includes risks) and audited statements with notes; annual information form left out", f, "") + ks, encoding="utf-8")
            made.append((kname, len(ks), "same 40-F, MD&A and audited statements only"))
        else:
            t, info = doc_text(slug, cfg["cik"], f["acc"], f["doc"])
            fname = f"annual-report-FY{fy}.txt"
            (outdir / fname).write_text(doc_header(cfg, f"Form 10-K for the fiscal year ended {fy}", f, f["doc"]) + t, encoding="utf-8")
            made.append((fname, len(t), f"10-K for the fiscal year ended {fy}, full text ({info['pages']} pages; " + ("page markers are the printed page numbers)" if info['mode'] == 'printed' else "page markers count pages from the start, because the filing's own page numbers could not be read)")))
            ks = key_sections(t)
            kname = f"annual-report-FY{fy}-key-sections.txt"
            (outdir / kname).write_text(doc_header(cfg, f"Form 10-K for the fiscal year ended {fy}: Items 1, 1A, 3, 7, 8 and 9A only", f, f["doc"]) + ks, encoding="utf-8")
            made.append((kname, len(ks), "same 10-K, Items 1 (business), 1A (risk factors), 3 (legal), 7 (MD&A), 8 (statements and notes), 9A (controls)"))
    return ann, made


def releases(slug, cfg, filings, ann, annual_form, outdir):
    made = []
    for a in ann:
        fy_end = date.fromisoformat(a["period"])
        lo, hi = fy_end.isoformat(), (fy_end + timedelta(days=100)).isoformat()
        if annual_form == "40-F":
            cands = [f for f in filings if f["form"] == "6-K" and lo < f["filed"] <= hi]
        else:
            cands = [f for f in filings if f["form"] == "8-K" and "2.02" in (f["items"] or "") and lo < f["filed"] <= hi]
        found = None
        for f in cands:
            for typ, desc, fn in filing_index(slug, cfg["cik"], f["acc"]):
                if not typ.startswith("EX-99") or not fn.lower().endswith((".htm", ".html")):
                    continue
                t, _ = doc_text(slug, cfg["cik"], f["acc"], fn)
                if annual_form != "40-F" or re.search(r"fourth[- ]quarter", t[:20000], re.I):
                    found = (f, fn, t)
                    break
            if found:
                break
        if not found:
            print("  no Q4 release found for", a["period"])
            continue
        f, fn, t = found
        fname = f"earnings-release-Q4-FY{a['period']}.txt"
        (outdir / fname).write_text(doc_header(cfg, f"Fourth-quarter and full-year results release for the year ended {a['period']} ({f['form']} exhibit)", f, fn) + t, encoding="utf-8")
        made.append((fname, len(t), f"results release furnished {f['filed']} on {f['form']}"))
    return made


# ---------------------------------------------------------------- per-company README
def readme(slug, cfg, fy, quarters, nrev, cur, files, ann, amendments, annual_form):
    def tok(n): return f"about {round(n / 4 / 1000):,}k tokens"
    rows = "\n".join(f"| `{fn}` | {desc} | {n:,} characters, {tok(n)} |" for fn, n, desc in files)
    qs = f"{len(quarters)} quarters, {quarters[0][1]} to {quarters[-1][1]}" if quarters else "none (annual only)"
    amend = "\n".join(f"- {f['form']} filed {f['filed']} for the period ended {f['period']}" for f in amendments) or "- None in the window."
    k = [fn for fn, _, _ in files if "key-sections" in fn]
    reports = [fn for fn, _, _ in files if fn.startswith("annual-report") and "key-sections" not in fn]
    rel = [fn for fn, _, _ in files if fn.startswith("earnings-release")]
    ar = " and ".join(f"`{x}`" for x in (k or reports))
    key = f"\n**Answer key:** [{cfg['answer_key']}]({cfg['answer_key']})\n" if cfg.get("answer_key") else ""
    return f"""# {cfg['name']}: test data

{cfg['profile']}
{key}
**Window:** SEC filings made from {cfg['start']} to {cfg['asof']}. Nothing filed after {cfg['asof']} is included, so the documents show only what an analyst could have read on that date.

## Files

| File | What it is | Size |
|---|---|---|
| `statements.xlsx` | Income statement, balance sheet and cash flow as the company presents them, in {cur} millions. Annual: {len(fy)} fiscal years, {fy[0]} to {fy[-1]}. Quarterly: {qs}. As originally reported; {nrev} later changes listed on the Revisions sheet. An Industry sheet gives Damodaran's industry averages for the matching year | small |
{rows}

Token counts are estimates (characters divided by four). A chat conversation holds roughly 150k to 200k tokens on most plans. If the two full annual reports will not fit, attach the key-sections files instead.

## What to attach for each prompt

| Prompt | Attach |
|---|---|
| 1. Working capital | `statements.xlsx` |
| 2. Earnings quality | Nothing new. Add {' and '.join(f'`{x}`' for x in rel) or 'the releases'} for the adjusted-earnings check |
| 3. Footnote changes | {ar} |
| 4. Consistency check | Nothing new, if prompts 1 to 3 ran in the same conversation |
| 5. Red-flag report | Nothing new |

## Amendments filed in the window

{amend}

## How this was built

`../_build/build.py {slug}` downloads the filings from EDGAR, parses the rendered statement pages (the R files behind each filing's "Financial Report"), and converts the annual reports and releases from HTML to text. Rerunning it reproduces the folder.
"""


def main(slugs):
    for slug in slugs:
        cfg = COMPANIES[slug]
        print(f"== {slug}")
        edgar_name, all_f = submissions(slug, cfg["cik"])
        print("  EDGAR name:", edgar_name)
        filings = [f for f in all_f if cfg["start"] <= f["filed"] <= cfg["asof"]]
        annual_form = "40-F" if any(f["form"] == "40-F" for f in filings) else "10-K"
        amendments = [f for f in filings if f["form"].endswith("/A") and f["form"].split("/")[0] in (annual_form, "10-Q")]
        outdir = ROOT / slug
        outdir.mkdir(exist_ok=True)
        sf = statement_filings(slug, cfg["cik"], filings, annual_form)
        store = Store(sf)
        fy, quarters, nrev, cur = build_workbook(slug, cfg, store, annual_form, outdir / "statements.xlsx")
        print(f"  workbook: {len(fy)} years, {len(quarters)} quarters, {nrev} revisions, {cur}")
        import industry
        print("  industry sheet:", industry.add_sheet(slug, outdir / "statements.xlsx"))
        ann, files = annual_reports(slug, cfg, filings, annual_form, outdir)
        files += releases(slug, cfg, filings, ann, annual_form, outdir)
        for fn, n, _ in files:
            print(f"  {fn}: {n:,} chars")
        (outdir / "README.md").write_text(readme(slug, cfg, fy, quarters, nrev, cur, files, ann, amendments, annual_form), encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1:] or list(COMPANIES))
