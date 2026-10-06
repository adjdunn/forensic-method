"""Build the text half of the Hertz FY2013 pack from the raw EDGAR downloads in build/raw/.
Writes section files, releases, proxies and events.txt into ../pack/, and build/text_pack_log.json
(file list with sources, page-marker mode, note counts, gaps) for the manifest."""
import json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from htmltext import html_to_text, apply_page_markers

RAW = HERE / "raw"
PACK = HERE.parent / "pack"
CIK = 1364479
CUTOFF = "2014-03-31"
(PACK / "releases").mkdir(parents=True, exist_ok=True)
(PACK / "proxy").mkdir(parents=True, exist_ok=True)
for old in list(PACK.glob("AR-FY*.txt")) + list(PACK.glob("Q?-FY*.txt")) + list((PACK / "releases").glob("*.txt")) + list((PACK / "proxy").glob("*.txt")):
    old.unlink()

sel = json.loads((RAW / "selected.json").read_text())
assert all(r["filingDate"] <= CUTOFF for r in sel)


def url(acc, doc):
    return f"https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace('-', '')}/{doc}"


ANNUAL = [
    ("AR-FY2011", "0001047469-12-001623", "a2207464z10-k.htm", "2012-02-27", "FY2011 (year ended 31 Dec 2011)"),
    ("AR-FY2012", "0001445305-13-000446", "hgh2012form10-k.htm", "2013-03-04", "FY2012 (year ended 31 Dec 2012)"),
    ("AR-FY2013", "0001364479-14-000006", "hgh2013form10-k.htm", "2014-03-19", "FY2013 (year ended 31 Dec 2013)"),
]
QUARTERLY = [
    ("Q1-FY2011", "0001047469-11-004720", "a2203910z10-q.htm", "2011-05-06", "Q1 2011 (three months ended 31 Mar 2011)"),
    ("Q2-FY2011", "0001047469-11-007031", "a2205046z10-q.htm", "2011-08-05", "Q2 2011 (three and six months ended 30 Jun 2011)"),
    ("Q3-FY2011", "0001047469-11-009145", "a2206040z10-q.htm", "2011-11-07", "Q3 2011 (three and nine months ended 30 Sep 2011)"),
    ("Q1-FY2012", "0001047469-12-005385", "a2209237z10-q.htm", "2012-05-04", "Q1 2012 (three months ended 31 Mar 2012)"),
    ("Q2-FY2012", "0001047469-12-007702", "a2210414z10-q.htm", "2012-08-03", "Q2 2012 (three and six months ended 30 Jun 2012)"),
    ("Q3-FY2012", "0001445305-12-003378", "hghq32012form10-q.htm", "2012-11-02", "Q3 2012 (three and nine months ended 30 Sep 2012)"),
    ("Q1-FY2013", "0001445305-13-001076", "hghq12013form10-q.htm", "2013-05-02", "Q1 2013 (three months ended 31 Mar 2013)"),
    ("Q2-FY2013", "0001364479-13-000006", "hghq22013form10-q.htm", "2013-08-02", "Q2 2013 (three and six months ended 30 Jun 2013)"),
    ("Q3-FY2013", "0001364479-13-000011", "hghq32013form10-q.htm", "2013-11-07", "Q3 2013 (three and nine months ended 30 Sep 2013)"),
]

LOG = {"files": [], "filings": {}, "gaps": []}

PAGE_RE = re.compile(r"^\[p\. [^\]]+\]$")
NOTE_RE = re.compile(r"^Note\s+(\d{1,2})\s*[—–\-:.]+\s*(.+?)\s*$")


def load(acc, doc):
    t = html_to_text((RAW / acc / doc).read_bytes())
    text, info = apply_page_markers(t)
    return text.split("\n"), info


def is_heading_line(s):
    return "|" not in s and "(Continued)" not in s and "(continued)" not in s


def find(lines, pat, start=0, end=None, flags=re.I):
    rx = re.compile(pat, flags)
    end = len(lines) if end is None else end
    for i in range(start, end):
        s = lines[i].strip()
        if is_heading_line(s) and rx.search(s):
            return i
    return None


def page_before(lines, i):
    for k in range(i, -1, -1):
        if PAGE_RE.match(lines[k].strip()):
            return lines[k].strip()
    return None


def section(lines, a, b):
    """Lines a..b-1, with the page marker in force at line a prepended."""
    body = lines[a:b]
    while body and not body[-1].strip():
        body.pop()
    # a trailing page marker with nothing after it belongs to the next section
    while body and PAGE_RE.match(body[-1].strip()):
        body.pop()
        while body and not body[-1].strip():
            body.pop()
    pm = page_before(lines, a)
    head = [pm, ""] if pm and not PAGE_RE.match(lines[a].strip()) else []
    return "\n".join(head + body).strip() + "\n"


def slug(s, n=48):
    s = s.lower().replace("&", "and")
    s = re.sub(r"\([^)]*\)", "", s) if len(s) > n else s
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    if len(s) > n:
        s = s[:n].rsplit("-", 1)[0]
    return s


def write(rel, text, meta):
    p = PACK / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    assert text.strip(), rel
    assert "\u0000" not in text
    p.write_text(text, encoding="utf-8")
    meta = dict(meta)
    meta["file"] = rel.replace("\\", "/")
    meta["chars"] = len(text)
    LOG["files"].append(meta)


def header(company_form, filed, part, src):
    return f"SOURCE: Hertz Global Holdings, Inc. (CIK {CIK}), {company_form}, filed {filed}. {part}. {src}\n\n"


def notes_in(lines, a, b, label):
    """Sequential notes Note 1, Note 2 ... inside [a, b). Stops when numbering restarts."""
    found = []
    expect = 1
    for i in range(a, b):
        s = lines[i].strip()
        if not is_heading_line(s):
            continue
        m = NOTE_RE.match(s)
        if not m:
            continue
        n = int(m.group(1))
        if n == expect:
            found.append((n, m.group(2), i))
            expect += 1
        elif n == 1 and found:
            break
    # every distinct Note k heading in the region, for the count check
    distinct = set()
    for i in range(a, b):
        s = lines[i].strip()
        m = NOTE_RE.match(s) if is_heading_line(s) else None
        if m:
            distinct.add(int(m.group(1)))
    return found


def units_of(text):
    m = re.search(r"\(In (Thousands|Millions) of Dollars", text, re.I)
    return m.group(1).lower() if m else "not found"


# ---------------------------------------------------------------- annual reports
for label, acc, doc, filed, period in ANNUAL:
    lines, info = load(acc, doc)
    src = url(acc, doc)
    form = f"Form 10-K for the fiscal year ended December 31, {label[-4:]}"
    flog = {"form": "10-K", "accession": acc, "url": src, "page_info": info, "sections": {}}
    # skip the table of contents: body starts at the first non-TOC "ITEM 1. BUSINESS"
    it = {}
    keys = [("1", r"^ITEM\s+1\.\s*BUSINESS"), ("1A", r"^ITEM\s+1A\.\s*RISK FACTORS"), ("1B", r"^ITEM\s+1B\."),
            ("2", r"^ITEM\s+2\.\s*PROPERTIES"), ("3", r"^ITEM\s+3\.\s*LEGAL"), ("4", r"^ITEM\s+4\.\s"),
            ("5", r"^ITEM\s+5\.\s"), ("6", r"^ITEM\s+6\.\s"), ("7", r"^ITEM\s+7\.\s"), ("7A", r"^ITEM\s+7A\.\s"),
            ("8", r"^ITEM\s+8\.\s"), ("9", r"^ITEM\s+9\.\s"), ("9A", r"^ITEM\s+9A\.\s"), ("9B", r"^ITEM\s+9B\.\s"),
            ("10", r"^ITEM\s+10\.\s"), ("11", r"^ITEM\s+11\.\s"), ("12", r"^ITEM\s+12\.\s"), ("13", r"^ITEM\s+13\.\s"),
            ("14", r"^ITEM\s+14\.\s"), ("15", r"^ITEM\s+15\.\s")]
    pos = 0
    for k, pat in keys:
        i = find(lines, pat, pos)
        assert i is not None, (label, k)
        it[k] = i
        pos = i + 1
    H = lambda part: header(form, filed, part, src)
    base = {"filing": label, "form": "10-K", "filed": filed, "period": period, "url": src, "page_mode": info["mode"]}

    def put(key, a, b, part, extra=""):
        txt = section(lines, a, b)
        write(f"{label}_{key}.txt", H(part) + txt + extra, dict(base, section=key, what=part))
        flog["sections"][key] = {"lines": [a, b]}
        return txt

    put("business", it["1"], it["1A"], "Item 1. Business")
    put("risk-factors", it["1A"], it["1B"], "Item 1A. Risk Factors")
    legal_a, legal_b = it["3"], it["4"]
    mdna = put("mdna", it["7"], it["7A"], "Item 7. Management's Discussion and Analysis of Financial Condition and Results of Operations")
    # critical estimates: from the heading to "Recent Accounting Pronouncements"
    ce = find(lines, r"^Critical Accounting Policies and Estimates$", it["7"], it["7A"])
    ce_end = find(lines, r"^Recent Accounting Pronouncements$", ce + 1 if ce else it["7"], it["7A"])
    if ce is not None and ce_end is not None:
        put("critical-estimates", ce, ce_end, "Item 7, Critical Accounting Policies and Estimates (also contained in the mdna file)")
    else:
        LOG["gaps"].append(f"{label}: critical-estimates not isolated")
    # market risk: Item 7A plus the Item 7 "Market Risks" subsection it refers to
    mr = find(lines, r"^Market Risks?$", it["7"], it["7A"])
    mr_end = find(lines, r"^Income Taxes$", mr + 1, it["7A"]) if mr is not None else None
    sevena = section(lines, it["7A"], it["8"])
    if mr is not None and mr_end is not None:
        extra = ("\n--- Item 7A refers to the \"Market Risks\" discussion in Item 7. That subsection follows, "
                 "from the heading \"Market Risks\" to the heading \"Income Taxes\" (also contained in the mdna file). ---\n\n"
                 + section(lines, mr, mr_end))
        write(f"{label}_market-risk.txt", H("Item 7A. Quantitative and Qualitative Disclosures About Market Risk, with the Item 7 Market Risks subsection") + sevena + extra,
              dict(base, section="market-risk", what="Item 7A, plus the Item 7 Market Risks subsection it cross-refers to"))
    else:
        write(f"{label}_market-risk.txt", H("Item 7A") + sevena, dict(base, section="market-risk", what="Item 7A"))
        LOG["gaps"].append(f"{label}: Item 7 Market Risks subsection not isolated")
    fs = put("financial-statements", it["8"], it["9"], "Item 8. Financial Statements and Supplementary Data (audit report, statements, notes, Schedule I, Schedule II)")
    flog["units"] = units_of(fs)
    # auditor report: from report heading to the page that carries the balance sheet
    ar = find(lines, r"^REPORT OF INDEPENDENT REGISTERED PUBLIC ACCOUNTING FIRM$", it["8"], it["9"])
    bs = find(lines, r"^CONSOLIDATED BALANCE SHEETS?$", ar, it["9"])
    k = bs
    while k > ar and not PAGE_RE.match(lines[k].strip()):
        k -= 1
    put("auditor-report", ar, k if k > ar else bs, "Item 8, Report of Independent Registered Public Accounting Firm")
    # notes
    s1 = find(lines, r"^SCHEDULE I$", it["8"], it["9"])
    notes_end = s1 if s1 is not None else it["9"]
    notes = notes_in(lines, bs, notes_end, label)
    distinct = sorted({int(NOTE_RE.match(lines[i].strip()).group(1)) for i in range(bs, notes_end)
                       if is_heading_line(lines[i].strip()) and NOTE_RE.match(lines[i].strip())})
    flog["notes"] = {"count": len(notes), "distinct_headings": distinct, "titles": [n[1] for n in notes]}
    if [n[0] for n in notes] != distinct:
        LOG["gaps"].append(f"{label}: note numbering check failed {distinct}")
    rp_note = None
    cont_note = None
    for j, (n, title, i) in enumerate(notes):
        b = notes[j + 1][2] if j + 1 < len(notes) else notes_end
        # the last note ends before the page that starts Schedule I
        if j + 1 == len(notes) and s1 is not None:
            kk = s1
            while kk > i and not PAGE_RE.match(lines[kk].strip()):
                kk -= 1
            b = kk if kk > i else s1
        key = f"notes-{n:02d}-{slug(title)}"
        put(key, i, b, f"Item 8, Notes to Consolidated Financial Statements, Note {n}: {title}")
        if re.search(r"related party", title, re.I):
            rp_note = (i, b, n, title)
        if re.search(r"contingenc", title, re.I):
            cont_note = (i, b, n, title)
    # legal: Item 3 plus the contingencies note
    lg = section(lines, legal_a, legal_b)
    if cont_note:
        lg += (f"\n--- Note {cont_note[2]} to the consolidated financial statements ({cont_note[3]}) follows "
               f"(also its own notes file). ---\n\n" + section(lines, cont_note[0], cont_note[1]))
    else:
        LOG["gaps"].append(f"{label}: no contingencies note found")
    write(f"{label}_legal.txt", H("Item 3. Legal Proceedings, with the contingencies note") + lg,
          dict(base, section="legal", what="Item 3, plus the contingencies note"))
    # Schedule II
    s2 = find(lines, r"^SCHEDULE II$", it["8"], it["9"])
    if s2 is not None:
        put("schedule-ii", s2, it["9"], "Item 8 / Item 15, Schedule II Valuation and Qualifying Accounts")
    else:
        LOG["gaps"].append(f"{label}: Schedule II not found")
    put("controls", it["9A"], it["9B"], "Item 9A. Controls and Procedures")
    # related parties: Item 13 plus the related-party note
    rp = section(lines, it["13"], it["14"])
    if rp_note:
        rp += (f"\n--- Note {rp_note[2]} to the consolidated financial statements ({rp_note[3]}) follows "
               f"(also its own notes file). ---\n\n" + section(lines, rp_note[0], rp_note[1]))
    else:
        LOG["gaps"].append(f"{label}: no related-party note found")
    write(f"{label}_related-parties.txt", H("Item 13. Certain Relationships and Related Transactions, and Director Independence, with the related-party note") + rp,
          dict(base, section="related-parties", what="Item 13, plus the related-party note"))
    LOG["filings"][label] = flog

# ---------------------------------------------------------------- quarterly reports
for label, acc, doc, filed, period in QUARTERLY:
    lines, info = load(acc, doc)
    src = url(acc, doc)
    form = f"Form 10-Q, {period}"
    flog = {"form": "10-Q", "accession": acc, "url": src, "page_info": info, "sections": {}}
    H = lambda part: header(form, filed, part, src)
    base = {"filing": label, "form": "10-Q", "filed": filed, "period": period, "url": src, "page_mode": info["mode"]}

    def put(key, a, b, part):
        txt = section(lines, a, b)
        write(f"{label}_{key}.txt", H(part) + txt, dict(base, section=key, what=part))
        flog["sections"][key] = {"lines": [a, b]}
        return txt

    i1 = find(lines, r"^ITEM\s+[1lI]\.\s*Condensed Consolidated Financial Statements")
    i2 = find(lines, r"^ITEM\s+2\.\s*Management", i1 + 1)
    i3 = find(lines, r"^ITEM\s+3\.\s*Quantitative", i2 + 1)
    p2 = find(lines, r"^PART\s+II\b", i3 + 1)
    r1a = find(lines, r"^ITEM\s+1A\.\s*RISK FACTORS", p2 + 1)
    rnext = find(lines, r"^ITEM\s+(2|3|4|5|6)\.\s", r1a + 1)
    assert None not in (i1, i2, i3, p2, r1a, rnext), label
    fs = put("financial-statements", i1, i2, "Part I, Item 1. Condensed Consolidated Financial Statements (Unaudited), with notes")
    flog["units"] = units_of(fs)
    first = find(lines, r"^Note\s+1\s*[—–\-]", i1, i2)
    notes = notes_in(lines, first, i2, label)
    distinct = sorted({int(NOTE_RE.match(lines[i].strip()).group(1)) for i in range(first, i2)
                       if is_heading_line(lines[i].strip()) and NOTE_RE.match(lines[i].strip())})
    flog["notes"] = {"count": len(notes), "distinct_headings": distinct, "titles": [n[1] for n in notes]}
    if [n[0] for n in notes] != distinct:
        LOG["gaps"].append(f"{label}: note numbering check failed {distinct}")
    for j, (n, title, i) in enumerate(notes):
        b = notes[j + 1][2] if j + 1 < len(notes) else i2
        put(f"notes-{n:02d}-{slug(title)}", i, b, f"Part I, Item 1, Notes to Condensed Consolidated Financial Statements, Note {n}: {title}")
    put("mdna", i2, i3, "Part I, Item 2. Management's Discussion and Analysis of Financial Condition and Results of Operations")
    rf = section(lines, r1a, rnext)
    body = re.sub(r"\[p\. [^\]]+\]|ITEM 1A\. RISK FACTORS", "", rf, flags=re.I).strip()
    flog["risk_factors_chars"] = len(body)
    if len(body) > 300:
        put("risk-factors", r1a, rnext, "Part II, Item 1A. Risk Factors")
    else:
        flog["risk_factors_text"] = body
    LOG["filings"][label] = flog

# ---------------------------------------------------------------- releases
bydate = {}
REL = []
for r in sel:
    if not r["form"].startswith("8-K") or "2.02" not in r.get("items", ""):
        continue
    REL.append(r)
ER_MAP = {  # accession -> period label (results press releases)
    "0001104659-11-009018": "Q4-FY2010",
    "0001104659-11-022448": "Q1-FY2011", "0001104659-11-042686": "Q2-FY2011", "0001104659-11-059608": "Q3-FY2011",
    "0001104659-12-011716": "Q4-FY2011", "0001104659-12-032105": "Q1-FY2012", "0001104659-12-052234": "Q2-FY2012",
    "0001104659-12-072771": "Q3-FY2012", "0001104659-13-013602": "Q4-FY2012", "0001104659-13-034509": "Q1-FY2013",
    "0001104659-13-057165": "Q2-FY2013", "0001104659-13-080717": "Q3-FY2013", "0001104659-14-020429": "Q4-FY2013",
}
dates = {}
for r in REL:
    dates.setdefault(r["filingDate"], []).append(r)
for r in REL:
    acc = r["accessionNumber"]
    d = RAW / acc
    listing = json.loads((d / "listing.json").read_text())
    exs = [L for L in listing if L["type"].upper().startswith("EX-99")]
    parts = []
    infos = []
    for L in exs:
        t = html_to_text((d / L["name"]).read_bytes())
        text, info = apply_page_markers(t)
        infos.append(info["mode"])
        parts.append(f"=== {L['type']} ({L['name']}) {url(acc, L['name'])} ===\n\n" + text)
    body = "\n\n".join(parts)
    main8k = html_to_text((d / r["primaryDocument"]).read_bytes()).replace("\u0000PB\u0000", "")
    m = re.search(r"(ITEM|Item)\s+2\.02.*?(?=\n\s*(ITEM|Item)\s+\d\.\d\d|\n\s*CAUTIONARY|\n\s*SIGNATURE)", main8k, re.S)
    item202 = re.sub(r"\n{2,}", "\n", m.group(0)).strip() if m else ""
    if acc in ER_MAP:
        name = f"releases/ER-{ER_MAP[acc]}.txt"
        what = f"Earnings release (Exhibit 99.1) for {ER_MAP[acc]}"
        per = ER_MAP[acc]
    else:
        same = dates[r["filingDate"]]
        sfx = "" if len(same) == 1 else "-" + "ab"[same.index(r)]
        name = f"releases/OTHER-{r['filingDate']}{sfx}.txt"
        first = re.sub(r"\s+", " ", body[:600])
        what = "Item 2.02 8-K exhibit"
        per = ""
    hdr = (f"SOURCE: Hertz Global Holdings, Inc. (CIK {CIK}), Form 8-K filed {r['filingDate']}, items {r['items']}, "
           f"accession {acc}. {url(acc, r['primaryDocument'])}\n\n"
           f"8-K text of Item 2.02:\n{item202}\n\n")
    write(name, hdr + body.strip() + "\n", {"filing": name.split("/")[1][:-4], "form": "8-K", "filed": r["filingDate"],
                                          "period": per, "url": url(acc, exs[0]["name"]) if exs else url(acc, r["primaryDocument"]),
                                          "section": "release", "what": what, "page_mode": ",".join(infos),
                                          "exhibits": [L["type"] + " " + L["name"] for L in exs], "accession": acc})

# ---------------------------------------------------------------- proxies
for year, acc, doc, filed in (("2012", "0001047469-12-003900", "a2208637zdef14a.htm", "2012-04-05"),
                              ("2013", "0001047469-13-003592", "a2214087zdef14a.htm", "2013-03-28")):
    lines, info = load(acc, doc)
    a = find(lines, r"^EXECUTIVE COMPENSATION$")
    b = find(lines, r"^(AUDIT COMMITTEE REPORT|PROPOSAL\s+\d)", a + 1, flags=0)
    txt = section(lines, a, b)
    src = url(acc, doc)
    hdr = (f"SOURCE: Hertz Global Holdings, Inc. (CIK {CIK}), definitive proxy statement (DEF 14A) filed {filed}. "
           f"Section \"Executive Compensation\": named executive officers, Compensation Discussion and Analysis, "
           f"Compensation Committee Report and compensation tables. {src}\n\n")
    write(f"proxy/PROXY-{year}.txt", hdr + txt, {"filing": f"PROXY-{year}", "form": "DEF 14A", "filed": filed,
                                                "period": f"Compensation for fiscal {int(year) - 1}", "url": src,
                                                "section": "proxy", "what": "Executive compensation section (CD&A and tables)",
                                                "page_mode": info["mode"]})

(HERE / "text_pack_log.json").write_text(json.dumps(LOG, indent=1))
print("files", len(LOG["files"]))
print("gaps", LOG["gaps"])
for k, v in LOG["filings"].items():
    print(k, v.get("units"), v["page_info"], "notes", v["notes"]["count"], v["notes"]["distinct_headings"][-1] if v["notes"]["distinct_headings"] else None, "rf", v.get("risk_factors_chars"))
