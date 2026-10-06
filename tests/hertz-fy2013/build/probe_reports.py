import re, urllib.request
from pathlib import Path
src = Path("C:/Users/aaron/Dev/wiresift-valuation/scripts/valuation_core.py").read_text(encoding="utf-8")
UA = re.search(r'^UA\s*=\s*["\'](.+?)["\']', src, re.M).group(1)
def get(u): return urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA}), timeout=90).read()
acc = "0001445305-13-000446"
fs = get(f"https://www.sec.gov/Archives/edgar/data/1364479/{acc.replace('-','')}/FilingSummary.xml").decode("utf-8", "replace")
print(len(fs)); print(fs[:2500])
