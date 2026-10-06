"""Download the rendered statement reports (R files) for every Hertz Global Holdings
10-K and 10-Q in the pack window, from each filing's FilingSummary.xml.

Writes build/raw/R/<accession>/ with FilingSummary.xml and the balance sheet,
income statement and cash flow reports, plus build/statement_filings.json.
"""
import json, re, time, urllib.request
from pathlib import Path

HERE = Path(__file__).parent
src = Path("C:/Users/aaron/Dev/wiresift-valuation/scripts/valuation_core.py").read_text(encoding="utf-8")
UA = re.search(r'^UA\s*=\s*["\'](.+?)["\']', src, re.M).group(1)
CIK = 1364479


def get(u):
    for attempt in range(6):
        time.sleep(0.4 * (2 ** attempt) if attempt else 0.4)
        try:
            return urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA}), timeout=90).read()
        except urllib.error.HTTPError as e:
            if e.code in (429, 503) and attempt < 5:
                continue
            raise


def filings():
    s = json.loads(get(f"https://data.sec.gov/submissions/CIK{CIK:010d}.json"))
    blocks = [s["filings"]["recent"]] + [json.loads(get(f"https://data.sec.gov/submissions/{f['name']}")) for f in s["filings"].get("files", [])]
    out = []
    for b in blocks:
        for d, f, a, p, r in zip(b["filingDate"], b["form"], b["accessionNumber"], b["primaryDocument"], b["reportDate"]):
            if f in ("10-K", "10-Q") and "2010-01-01" <= d <= "2014-03-31":
                out.append({"filed": d, "form": f, "acc": a, "doc": p, "period": r})
    return sorted(out, key=lambda x: x["filed"])


def pick_reports(fs: str):
    reps = []
    for block in re.findall(r"<Report\b.*?</Report>", fs, re.S):
        long = re.search(r"<LongName>(.*?)</LongName>", block, re.S)
        fn = re.search(r"<HtmlFileName>(.*?)</HtmlFileName>", block) or re.search(r"<XmlFileName>(.*?)</XmlFileName>", block)
        if not (long and fn):
            continue
        name = long.group(1).strip()
        low = name.lower()
        if "parenthetical" in low or "- statement -" not in low and " statement " not in low:
            continue
        kind = None
        if "balance sheet" in low:
            kind = "BS"
        elif "cash flow" in low:
            kind = "CF"
        elif ("operations" in low or "income" in low) and "comprehensive" not in low and "equity" not in low:
            kind = "IS"
        if kind:
            reps.append({"kind": kind, "name": name, "file": fn.group(1)})
    return reps


def main():
    fl = filings()
    raw = HERE / "raw" / "R"
    for f in fl:
        base = f"https://www.sec.gov/Archives/edgar/data/{CIK}/{f['acc'].replace('-', '')}/"
        d = raw / f["acc"]
        d.mkdir(parents=True, exist_ok=True)
        fsp = d / "FilingSummary.xml"
        if not fsp.exists():
            try:
                fsp.write_bytes(get(base + "FilingSummary.xml"))
            except urllib.error.HTTPError as e:
                f["reports"] = []
                f["missing"] = f"FilingSummary.xml HTTP {e.code}"
                print(f["filed"], f["form"], f["period"], f["acc"], "NO FilingSummary", e.code)
                continue
        reps = pick_reports(fsp.read_text("utf-8", "replace"))
        f["reports"] = reps
        for r in reps:
            p = d / r["file"]
            if not p.exists():
                p.write_bytes(get(base + r["file"]))
        print(f["filed"], f["form"], f["period"], f["acc"], [(r["kind"], r["file"]) for r in reps])
    (HERE / "statement_filings.json").write_text(json.dumps(fl, indent=1))


if __name__ == "__main__":
    main()
