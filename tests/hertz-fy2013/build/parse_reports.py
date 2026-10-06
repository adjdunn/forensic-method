"""Parse the rendered statement reports (R*.xml and R*.htm) into rows:
(kind, label, element, period, value_in_millions), one set per filing.

period is ("D", start, end) for durations or ("I", end) for instants.
Writes build/parsed.json.
"""
import html, json, re
from datetime import date, timedelta
from pathlib import Path

HERE = Path(__file__).parent
RAW = HERE / "raw" / "R"
MONTHS = {m: i for i, m in enumerate(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], 1)}


def num(s: str):
    s = html.unescape(s).replace("$", "").replace(",", "").replace("\xa0", " ").strip()
    if not s or s in ("-", "—"):
        return None
    neg = s.startswith("(") and s.endswith(")")
    s = s.strip("()").strip()
    try:
        v = float(s)
    except ValueError:
        return None
    return -v if neg else v


def scale_of(text: str) -> float:
    t = text.lower()
    if "in thousands" in t:
        return 0.001
    if "in millions" in t:
        return 1.0
    if "in billions" in t:
        return 1000.0
    return 1e-6  # raw dollars


def parse_date(s: str) -> date:
    m = re.match(r"(\w{3})\.? (\d{1,2}), (\d{4})", s.strip())
    return date(int(m.group(3)), MONTHS[m.group(1)], int(m.group(2)))


def start_from(end: date, months: int) -> date:
    y, mth = end.year, end.month - months + 1
    while mth <= 0:
        mth += 12
        y -= 1
    return date(y, mth, 1)


def parse_xml(p: Path, kind: str):
    """Old-style InstanceReport XML. NumericAmount is in whole units (dollars, shares)."""
    x = p.read_text("utf-8", "replace")
    colsec = re.search(r"<Columns>(.*?)</Columns>", x, re.S).group(1)
    cols = {}
    for c in re.findall(r"<Column>(.*?)</Column>", colsec, re.S):
        cid = re.search(r"<Id>(\d+)</Id>", c).group(1)
        pt = re.search(r"<PeriodType>(.*?)</PeriodType>", c)
        if pt:
            e = re.search(r"<PeriodEndDate>(.*?)T", c).group(1)
            if pt.group(1) == "duration":
                cols[cid] = ("D", re.search(r"<PeriodStartDate>(.*?)T", c).group(1), e)
            else:
                cols[cid] = ("I", e)
        else:
            labels = re.findall(r'<Label Id="\d+" Label="(.*?)"', c)
            d = parse_date(labels[-1]).isoformat()
            m = re.match(r"(\d+) Months Ended", labels[0]) if len(labels) > 1 else None
            cols[cid] = ("D", start_from(date.fromisoformat(d), int(m.group(1))).isoformat(), d) if m else ("I", d)
    if kind == "BS":  # older renderer labels balance-sheet columns as durations; they are period-end balances
        cols = {k: ("I", v[-1]) for k, v in cols.items()}
    rows = []
    for r in re.findall(r"<Row>(.*?)</Row>", x, re.S):
        if "<IsAbstractGroupTitle>true</IsAbstractGroupTitle>" in r[:200]:
            continue
        label = html.unescape(re.search(r"<Label>(.*?)</Label>", r, re.S).group(1)).strip()
        el = re.search(r"<ElementName>(.*?)</ElementName>", r)
        el = el.group(1).replace("_", ":", 1) if el else ""
        per_share = "PerShare" in el
        shares = "Shares" in el and not per_share
        for c in re.findall(r"<Cell>(.*?)</Cell>", r, re.S):
            if "<IsNumeric>true</IsNumeric>" not in c:
                continue
            cid = re.search(r"<Id>(\d+)</Id>", c).group(1)
            if cid not in cols:
                continue
            v = float(re.search(r"<NumericAmount>(.*?)</NumericAmount>", c).group(1))
            if not (per_share or shares):
                v = v * 1e-6
            elif shares:
                v = v * 1e-6  # shares in millions, to match later filings
            rows.append((kind, label, el, cols[cid], v))
    return rows


def parse_htm(p: Path, kind: str):
    h = p.read_text("utf-8", "replace")
    title = re.search(r"<th class=\"tl\"[^>]*>(.*?)</th>", h, re.S)
    scale = scale_of(re.sub(r"<[^>]+>", " ", title.group(1)) if title else "")
    trs = re.findall(r"<tr[^>]*>(.*?)</tr>", h, re.S)
    head = [t for t in trs if "<th" in t]
    body = [t for t in trs if "<td" in t]
    # header expansion
    groups = []
    dates = []
    if len(head) >= 2:
        for m in re.finditer(r"<th class=\"th\"([^>]*)>(.*?)</th>", head[0], re.S):
            span = re.search(r'colspan="(\d+)"', m.group(1))
            groups += [re.sub(r"<[^>]+>", "", m.group(2)).strip()] * int(span.group(1) if span else 1)
        dates = [re.sub(r"<[^>]+>", "", d).strip() for d in re.findall(r"<th class=\"th\"[^>]*>(.*?)</th>", head[1], re.S)]
    else:
        dates = [re.sub(r"<[^>]+>", "", d).strip() for d in re.findall(r"<th class=\"th\"[^>]*>(.*?)</th>", head[0], re.S)]
        groups = [""] * len(dates)
    cols = []
    for g, d in zip(groups, dates):
        e = parse_date(d)
        m = re.match(r"(\d+) Months Ended", g)
        if m:
            cols.append(("D", start_from(e, int(m.group(1))).isoformat(), e.isoformat()))
        else:
            cols.append(("I", e.isoformat()))
    rows = []
    for t in body:
        tds = re.findall(r"<td[^>]*>(.*?)</td>", t, re.S)
        if not tds:
            continue
        el = re.search(r"defref_([A-Za-z0-9-]+)_([A-Za-z0-9]+)", tds[0])
        el = f"{el.group(1)}:{el.group(2)}" if el else ""
        label = html.unescape(re.sub(r"<[^>]+>", "", tds[0])).strip()
        is_ratio = "PerShare" in el
        for i, c in enumerate(tds[1:]):
            if i >= len(cols):
                break
            v = num(re.sub(r"<[^>]+>", "", c))
            if v is None:
                continue
            if not is_ratio and "shares" not in label.lower():
                v = v * scale
            rows.append((kind, label, el, cols[i], v))
    return rows


def main():
    fl = json.loads((HERE / "statement_filings.json").read_text())
    out = []
    for f in fl:
        if f["filed"] < "2011-02-01":
            continue  # 2010 quarterlies are outside the pack; FY2009-FY2010 come from the FY2010 10-K
        for r in f.get("reports", []):
            p = RAW / f["acc"] / r["file"]
            rows = parse_xml(p, r["kind"]) if p.suffix == ".xml" else parse_htm(p, r["kind"])
            out.append({"acc": f["acc"], "form": f["form"], "filed": f["filed"], "period": f["period"], "kind": r["kind"], "rows": rows})
    (HERE / "parsed.json").write_text(json.dumps(out, indent=0))
    # union of elements per kind, with labels and first/last filing seen
    seen = {}
    for blk in out:
        for kind, label, el, per, v in blk["rows"]:
            k = (kind, el or label)
            seen.setdefault(k, {"labels": set(), "n": 0})
            seen[k]["labels"].add(label)
            seen[k]["n"] += 1
    for (kind, el), d in sorted(seen.items()):
        print(f"{kind} | {el:70} | n={d['n']:3} | {' / '.join(sorted(d['labels']))[:110]}")


if __name__ == "__main__":
    main()
