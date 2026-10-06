import json, re, urllib.request
from pathlib import Path
src = Path("C:/Users/aaron/Dev/wiresift-valuation/scripts/valuation_core.py").read_text(encoding="utf-8")
UA = re.search(r'^UA\s*=\s*["\'](.+?)["\']', src, re.M).group(1)
def get(u): return urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA}), timeout=60).read()
def rows(block):
    return list(zip(block["filingDate"], block["form"], block["accessionNumber"], block["primaryDocument"], block.get("items", [""]*len(block["form"])), block["reportDate"]))
out = {}
for cik, extra in ((1364479, "CIK0001364479-submissions-001.json"), (47129, None)):
    s = json.loads(get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json"))
    blocks = [s["filings"]["recent"]]
    if extra: blocks.append(json.loads(get(f"https://data.sec.gov/submissions/{extra}")))
    allr = [r for b in blocks for r in rows(b)]
    sel = sorted(r for r in allr if "2010-12-01" <= r[0] <= "2014-06-30" and (r[1] in ("10-K","10-Q","DEF 14A","10-K/A","10-Q/A") or (r[1]=="8-K" and any(i in r[4] for i in ("2.02","4.01","4.02","2.01")))))
    out[cik] = sel
    print(cik, s["name"], len(sel))
    for r in sel: print("  ", r[0], r[1], r[5], r[2], r[3], r[4])
Path(r"Events\CFA Vancouver Forensic\tests\hertz-fy2013\build\filing_index.json").write_text(json.dumps(out, indent=1))
