"""Download the Hertz Global Holdings (CIK 1364479) filings needed for the text pack.
Raw files land in build/raw/<accession>/. Cut-off: filed on or before 2014-03-31."""
import json, re, time, urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
RAW = HERE / "raw"
RAW.mkdir(exist_ok=True)
src = Path("C:/Users/aaron/Dev/wiresift-valuation/scripts/valuation_core.py").read_text(encoding="utf-8")
UA = re.search(r'^UA\s*=\s*["\'](.+?)["\']', src, re.M).group(1)
CIK = 1364479
CUTOFF = "2014-03-31"


def get(u):
    for attempt in range(6):
        time.sleep(0.2 if attempt == 0 else 2 * attempt)
        try:
            return urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": UA}), timeout=90).read()
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504) and attempt < 5:
                print("  retry", e.code, u)
                continue
            raise


def fetch(u, dest):
    if dest.exists() and dest.stat().st_size > 0:
        return dest.read_bytes()
    b = get(u)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(b)
    return b


# 1. Full submission list (recent + older file) for event 8-Ks (5.02, 4.01, 4.02, 2.01)
subs_path = RAW / "submissions.json"
if not subs_path.exists():
    s = json.loads(get(f"https://data.sec.gov/submissions/CIK{CIK:010d}.json"))
    blocks = [s["filings"]["recent"]]
    for f in s["filings"].get("files", []):
        blocks.append(json.loads(get(f"https://data.sec.gov/submissions/{f['name']}")))
    rows = []
    for b in blocks:
        n = len(b["form"])
        for i in range(n):
            rows.append({k: b[k][i] for k in ("filingDate", "form", "accessionNumber", "primaryDocument", "items", "reportDate") if k in b})
    subs_path.write_text(json.dumps(rows, indent=0))
rows = json.loads(subs_path.read_text())

sel = []
for r in rows:
    d, f, it = r["filingDate"], r["form"], r.get("items", "")
    if not ("2011-01-01" <= d <= CUTOFF):
        continue
    if f in ("10-K", "10-K/A", "10-Q", "10-Q/A", "DEF 14A"):
        sel.append(r)
    elif f in ("8-K", "8-K/A") and any(x in it for x in ("2.01", "2.02", "4.01", "4.02", "5.02")):
        sel.append(r)
sel.sort(key=lambda r: (r["filingDate"], r["accessionNumber"]))
(RAW / "selected.json").write_text(json.dumps(sel, indent=1))
print(len(sel), "filings selected")

# 2. For each: filing index (JSON listing of the folder) and every htm/txt document
for r in sel:
    acc = r["accessionNumber"]
    nodash = acc.replace("-", "")
    base = f"https://www.sec.gov/Archives/edgar/data/{CIK}/{nodash}/"
    d = RAW / acc
    try:
        idx = fetch(f"{base}{acc}-index.htm", d / "index.htm").decode("latin-1")
    except Exception as e:
        print("  index.htm failed, using complete submission .txt headers", acc, e)
        txt = fetch(f"{base}{acc}.txt", d / f"{acc}.txt").decode("latin-1")
        idx = ""
        for typ, nm in re.findall(r"<TYPE>([^\n<]+)\s*<SEQUENCE>[^\n]*\s*<FILENAME>([^\n<]+)", txt):
            nm = nm.strip()
            idx += f'<tr><td>x</td><td>{nm}</td><td><a href="{nm}">{nm}</a></td><td>{typ.strip()}</td></tr>'
    # document table: rows with type column
    docs = re.findall(r'<tr[^>]*>(.*?)</tr>', idx, re.S | re.I)
    listing = []
    for row in docs:
        cells = re.findall(r'<td[^>]*>(.*?)</td>', row, re.S | re.I)
        if len(cells) >= 4:
            m = re.search(r'href="([^"]+)"', cells[2])
            if not m:
                continue
            href = m.group(1)
            name = href.rsplit("/", 1)[-1]
            typ = re.sub(r"<[^>]+>", "", cells[3]).strip()
            desc = re.sub(r"<[^>]+>", "", cells[1]).strip()
            listing.append({"name": name, "type": typ, "desc": desc})
    (d / "listing.json").write_text(json.dumps(listing, indent=1))
    want = []
    for L in listing:
        t = L["type"].upper()
        if not L["name"].lower().endswith((".htm", ".html", ".txt")):
            continue
        if r["form"].startswith("8-K"):
            if t.startswith("8-K") or t.startswith("EX-99"):
                want.append(L["name"])
        elif r["form"] == "10-K/A":
            want.append(L["name"])
        else:
            if L["name"] == r["primaryDocument"] or t in ("10-K", "10-Q", "DEF 14A"):
                want.append(L["name"])
    for nm in dict.fromkeys(want):
        fetch(base + nm, d / nm)
    print(r["filingDate"], r["form"], r.get("items", ""), acc, want)
