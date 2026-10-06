import json, re, sys, urllib.request
from pathlib import Path
src = Path("C:/Users/aaron/Dev/wiresift-valuation/scripts/valuation_core.py").read_text(encoding="utf-8")
UA = re.search(r'^UA\s*=\s*["\'](.+?)["\']', src, re.M).group(1)
def get(u): return urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA}), timeout=60).read()
for cik in (1364479, 47129, 1657853):
    s = json.loads(get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json"))
    print(cik, s.get("name"), "| former:", [f["name"] for f in s.get("formerNames", [])], "| extra files:", [f["name"] for f in s["filings"].get("files", [])])
    r = s["filings"]["recent"]
    rows = [(d, f, a, p) for f, a, p, d in zip(r["form"], r["accessionNumber"], r["primaryDocument"], r["filingDate"]) if "2011-01-01" <= d <= "2014-06-30" and f in ("10-K", "10-Q", "DEF 14A", "10-K/A", "10-Q/A")]
    print("  in recent list, 2011-2014H1:", len(rows), sorted(rows)[:3], "earliest recent:", min(r["filingDate"]))
