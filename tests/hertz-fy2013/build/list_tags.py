import json, re, urllib.request
from pathlib import Path
src = Path("C:/Users/aaron/Dev/wiresift-valuation/scripts/valuation_core.py").read_text(encoding="utf-8")
UA = re.search(r'^UA\s*=\s*["\'](.+?)["\']', src, re.M).group(1)
def get(u): return urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA}), timeout=90).read()
B = Path(r"Events\CFA Vancouver Forensic\tests\hertz-fy2013\build")
raw = get("https://data.sec.gov/api/xbrl/companyfacts/CIK0001364479.json")
(B / "companyfacts_1364479.json").write_bytes(raw)
facts = json.loads(raw)["facts"]
# tags with an FY2013 annual or 2013-12-31 instant value from the FY2013 10-K
acc = "0001364479-14-000006"
rows = []
for ns, tags in facts.items():
    for tag, d in tags.items():
        for unit, fl in d["units"].items():
            for f in fl:
                if f.get("accn") == acc and f["end"] in ("2013-12-31",) and (("start" not in f) or f["start"] == "2013-01-01"):
                    rows.append((ns, tag, unit, "I" if "start" not in f else "FY", f["val"], d.get("label")))
rows.sort(key=lambda r: (r[3], r[1]))
for r in rows: print(f"{r[3]:2} {r[0]:8} {r[1]:80} {r[4]:>18,} {r[2]}")
print(len(rows))
