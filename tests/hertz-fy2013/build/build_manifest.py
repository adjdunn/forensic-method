"""Write pack/events.txt and pack/manifest.md from build/text_pack_log.json and the raw 8-Ks."""
import json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from htmltext import html_to_text

PACK = HERE.parent / "pack"
RAW = HERE / "raw"
CIK = 1364479
LOG = json.loads((HERE / "text_pack_log.json").read_text())
sel = {r["accessionNumber"]: r for r in json.loads((RAW / "selected.json").read_text())}


def url(acc, doc):
    return f"https://www.sec.gov/Archives/edgar/data/{CIK}/{acc.replace('-', '')}/{doc}"


def plain(acc):
    r = sel[acc]
    return html_to_text((RAW / acc / r["primaryDocument"]).read_bytes()).replace("\u0000PB\u0000", "")


# ------------------------------------------------------------------ events.txt
EVENTS = [
    ("0001104659-11-002763", "Item 5.02(b): retirement of Gerald A. Plescia as President of Hertz Equipment Rental Corporation (HERC), effective January 25, 2011."),
    ("0001104659-11-012462", "Item 5.02(e): Separation Agreement and General Release entered into on February 28, 2011 with Gerald Plescia in connection with his retirement as President of HERC."),
    ("0001104659-11-038414", "Item 5.02(e): agreement of July 7, 2011 between Hertz Europe Limited and Michel Taride regarding living accommodations beyond June 2011."),
    ("0001104659-11-047033", "Item 5.02(b): Gregory S. Ledford, Nathan K. Sleeper and Robert F. End (Sponsor nominees) resigned from the boards of Hertz Holdings and The Hertz Corporation, effective August 12, 2011."),
    ("0001104659-11-050850", "Item 2.01: on September 1, 2011 The Hertz Corporation acquired the entire equity interest in Donlen Corporation and certain of its affiliates."),
    ("0001104659-11-059209", "Amendment to the September 8, 2011 Form 8-K (Donlen acquisition), filed to provide financial statements of the business acquired and pro forma financial information under Item 9.01."),
    ("0001104659-12-016281", "Item 5.02(d): Michael F. Koehler and Linda Fayne Levinson elected directors, effective March 7, 2012 (the filing also reports Item 5.03)."),
    ("0000950157-12-000499", "Item 2.01: on November 19, 2012 Hertz completed the acquisition of Dollar Thrifty Automotive Group, Inc. The Item 2.01 text is reproduced verbatim below."),
    ("0001104659-13-006116", "Amendment to the November 20, 2012 Form 8-K (Dollar Thrifty acquisition), filed to provide financial statements of the business acquired and pro forma financial information under Item 9.01."),
    ("0001104659-13-042914", "Item 5.02(b) and (d): Angel L. Morales resigned as a director; Carolyn Everson and Debra J. Kelly-Ennis elected directors on May 15, 2013 (the filing also reports Items 5.03 and 5.07)."),
    ("0001104659-13-064568", "Item 5.02: David Wasserman (a CD&R nominee) and Brian Bernasek (a Carlyle nominee) resigned as directors on August 15, 2013, following termination of the Stockholders Agreement on May 9, 2013."),
    ("0001104659-13-072719", "Item 5.02(b) and (c): Elyse Douglas resigned as Senior Executive Vice President and Chief Financial Officer effective October 1, 2013; David J. Rosenberg to succeed her as Chief Financial Officer on an interim basis."),
    ("0001104659-13-080596", "Item 5.02(d): Philippe P. Laffont elected a director, effective October 31, 2013."),
    ("0001104659-13-086067", "Amendment to the November 4, 2013 Form 8-K: on November 14, 2013 Mr. Laffont was elected to the Executive and Finance Committee."),
    ("0001104659-13-087902", "Item 5.02: appointment of Thomas C. Kennedy as Senior Executive Vice President and Chief Financial Officer, effective December 9, 2013, succeeding interim CFO David J. Rosenberg."),
]
ev_accs = [a for a, _ in EVENTS]
# completeness: every in-window 8-K with 2.01 / 4.01 / 4.02 / 5.02 must be listed
need = [a for a, r in sel.items() if r["form"].startswith("8-K") and any(x in r.get("items", "") for x in ("2.01", "4.01", "4.02", "5.02"))]
assert sorted(need) == sorted(ev_accs), (set(need) ^ set(ev_accs))
no4 = [a for a, r in sel.items() if r["form"].startswith("8-K") and any(x in r.get("items", "") for x in ("4.01", "4.02"))]
assert not no4

dtg = plain("0000950157-12-000499")
m = re.search(r"Item 2\.01\. Completion of Acquisition or Disposition of Assets\.\s*(.*?)\s*Item 7\.01\.", dtg, re.S)
dtg_text = m.group(1).strip()

out = ["EVENTS: Hertz Global Holdings, Inc. (SEC CIK 1364479)",
       "Current reports on Form 8-K (and 8-K/A) filed 1 January 2011 to 31 March 2014 under Items 2.01, 4.01, 4.02 and 5.02.",
       "Source: EDGAR submissions index for CIK 1364479. Descriptions are taken from each report's own text.",
       "",
       "Item 4.01 (change in certifying accountant): no report filed in this window.",
       "Item 4.02 (non-reliance on previously issued financial statements): no report filed in this window.",
       ""]
for acc, desc in sorted(EVENTS, key=lambda e: (sel[e[0]]["filingDate"], e[0])):
    r = sel[acc]
    out.append(f"{r['filingDate']} | Form {r['form']} | Items {r['items']} | accession {acc}")
    out.append(f"  {desc}")
    out.append(f"  {url(acc, r['primaryDocument'])}")
    if acc == "0000950157-12-000499":
        out.append("")
        out.append("  Item 2.01 text, verbatim:")
        out.append("")
        for para in dtg_text.split("\n"):
            if para.strip():
                out.append("  " + para.strip())
                out.append("")
    out.append("")
events_txt = "\n".join(out).rstrip() + "\n"
(PACK / "events.txt").write_text(events_txt, encoding="utf-8")

# ------------------------------------------------------------------ manifest
files = {f["file"]: f for f in LOG["files"]}
AR_ORDER = ["business", "risk-factors", "legal", "mdna", "critical-estimates", "market-risk", "auditor-report",
            "financial-statements", "NOTES", "schedule-ii", "controls", "related-parties"]
Q_ORDER = ["financial-statements", "NOTES", "mdna", "risk-factors"]


def ordered(label, order):
    fl = [f for f in LOG["files"] if f.get("filing") == label and f["form"] in ("10-K", "10-Q")]
    res = []
    for key in order:
        if key == "NOTES":
            res += sorted([f for f in fl if f["section"].startswith("notes-")], key=lambda f: f["section"])
        else:
            res += [f for f in fl if f["section"] == key]
    assert len(res) == len(fl), label
    return res


rows = []
for label in ("AR-FY2011", "AR-FY2012", "AR-FY2013"):
    rows += ordered(label, AR_ORDER)
for label in ("Q1-FY2011", "Q2-FY2011", "Q3-FY2011", "Q1-FY2012", "Q2-FY2012", "Q3-FY2012", "Q1-FY2013", "Q2-FY2013", "Q3-FY2013"):
    rows += ordered(label, Q_ORDER)
rel = sorted([f for f in LOG["files"] if f["section"] == "release"], key=lambda f: (f["filed"], f["accession"]))
rows += rel
rows += sorted([f for f in LOG["files"] if f["section"] == "proxy"], key=lambda f: f["filed"])
assert len(rows) == len(LOG["files"])

OTHER_WHAT = {
    "OTHER-2011-01-25": ("Two press releases: HERC president retirement with selected HERC financial expectations for 2011 (EX-99.1), and updated full year 2010 guidance issued January 24, 2011 (EX-99.2)", "FY2010 guidance; FY2011 HERC outlook"),
    "OTHER-2011-02-25": ("Slides accompanying the February 23, 2011 earnings call, with non-GAAP reconciliations", "Q4 2010 and FY2010"),
    "OTHER-2011-05-02": ("Slides accompanying the April 27, 2011 earnings call, with non-GAAP reconciliations", "Q1 2011"),
    "OTHER-2011-08-08": ("Slides accompanying the August 3, 2011 earnings call, with non-GAAP reconciliations", "Q2 2011"),
    "OTHER-2011-11-07": ("Slides accompanying the November 2, 2011 earnings call, with non-GAAP reconciliations", "Q3 2011"),
    "OTHER-2012-02-27": ("Slides accompanying the February 23, 2012 earnings call, with non-GAAP reconciliations", "Q4 2011 and FY2011"),
    "OTHER-2012-05-07": ("Slides accompanying the May 3, 2012 earnings call, with non-GAAP reconciliations", "Q1 2012"),
    "OTHER-2012-08-01": ("Slides accompanying the July 31, 2012 earnings call, with non-GAAP reconciliations", "Q2 2012"),
    "OTHER-2012-11-06": ("Slides accompanying the November 1, 2012 earnings call, with non-GAAP reconciliations", "Q3 2012"),
    "OTHER-2013-02-28": ("Slides accompanying the February 25, 2013 earnings call, with non-GAAP reconciliations", "Q4 2012 and FY2012"),
    "OTHER-2013-05-03": ("Slides accompanying the April 30, 2013 earnings call, with non-GAAP reconciliations", "Q1 2013"),
    "OTHER-2013-07-30": ("Press release of July 29, 2013 announcing a correction to the previously released second quarter earnings announcement", "Q2 2013"),
    "OTHER-2013-08-01-a": ("Press release of July 31, 2013 providing clarification to the calculation of total revenue per transaction day (total RPD)", "Q2 2013"),
    "OTHER-2013-08-01-b": ("Slides accompanying the July 29, 2013 earnings call, with non-GAAP reconciliations", "Q2 2013"),
    "OTHER-2013-11-06": ("Slides accompanying the November 5, 2013 earnings call, with non-GAAP reconciliations", "Q3 2013"),
    "OTHER-2014-03-20": ("Slides accompanying the March 18, 2014 earnings call, with non-GAAP reconciliations", "Q4 2013 and FY2013"),
}
ER_PERIOD = lambda s: f"{s[:2]} {s[-4:]}"


def per_short(f):
    if f["form"] == "10-K":
        return f["filing"].replace("AR-", "")
    if f["form"] == "10-Q":
        q, y = f["filing"].split("-")
        return f"{q} {y[2:]}"
    return f["period"]


ids = {}
table = ["| ID | File | What it is | Period | Source document and URL |", "|---|---|---|---|---|",
         "| P0 | manifest.md | This file | | |",
         "| P1 | statements.xlsx | Statement workbook (built separately) | Quarters Q1 2011 to Q4 2013; years FY2009 to FY2013 | Built from the 10-K and 10-Q filings listed below; see its LOCATORS sheet |"]
n = 2
for f in rows:
    pid = f"P{n}"
    n += 1
    ids[f["file"]] = pid
    if f["section"] == "release":
        nm = f["file"].split("/")[1][:-4]
        if nm.startswith("ER-"):
            p = nm[3:]
            what = f"Earnings press release (Exhibit 99.1), with non-GAAP reconciliation tables. Opens with the 8-K's Item 2.02 text"
            period = f"{p[:2]} {p[-4:]}" + (" and FY" + p[-4:] if p.startswith("Q4") else "")
        else:
            what, period = OTHER_WHAT[nm]
        src = f"Form 8-K filed {f['filed']} (acc. {f['accession']}), {', '.join(f['exhibits'])}: {f['url']}"
    elif f["section"] == "proxy":
        what = f["what"]
        period = f["period"]
        src = f"DEF 14A filed {f['filed']}: {f['url']}"
    else:
        what = f["what"]
        period = per_short(f)
        form = "10-K" if f["form"] == "10-K" else "10-Q"
        src = f"Form {form} filed {f['filed']}: {f['url']}"
    table.append(f"| {pid} | {f['file']} | {what} | {period} | {src} |")
ev_id = f"P{n}"
table.append(f"| {ev_id} | events.txt | 8-K reports under Items 2.01, 4.01, 4.02 and 5.02, 1 Jan 2011 to 31 Mar 2014, with the Dollar Thrifty Item 2.01 text verbatim | 2011 to Q1 2014 | EDGAR filing index for CIK 1364479; each entry carries its accession number and URL |")
last_id = ev_id

fl = LOG["filings"]
units_line = "; ".join(f"{k}: {v['units']}" for k, v in fl.items())
fw_id = ids["AR-FY2013_notes-02-summary-of-significant-accounting-policies.txt"]
bs_id = ids["AR-FY2013_financial-statements.txt"]
ar_id = ids["AR-FY2013_auditor-report.txt"]
rf_skipped = {k: v["risk_factors_text"] for k, v in fl.items() if "risk_factors_text" in v}

hdr = f"""# Manifest

Test pack T1: Hertz Global Holdings, Inc., as an analyst could read it on 31 March 2014.

| Field | Value |
|---|---|
| Company | Hertz Global Holdings, Inc. (SEC CIK 1364479), parent of The Hertz Corporation. Only the Hertz Global Holdings filings are used |
| Ticker and exchange | HTZ, New York Stock Exchange |
| Reporting framework | US GAAP. The FY2013 10-K's Note 2 refers to "accounting principles generally accepted in the United States of America, or GAAP" ({fw_id}, p. 83); the audit opinions cite the same basis ({ar_id}) |
| Expense presentation | Neither a by-function cost-of-sales format nor a by-nature format: the statement of operations lists revenues by business (car rental, equipment rental and other; labelled worldwide car rental, worldwide equipment rental and all other operations in the FY2013 10-K) and then expenses as direct operating; depreciation of revenue earning equipment and lease charges; selling, general and administrative; interest expense; interest income; and other (income) expense, net. There is no cost-of-sales or gross-profit line |
| PP&E measurement model | Cost. Revenue earning equipment (cars, other equipment) and property and equipment are both carried "at cost" less accumulated depreciation on the balance sheet ({bs_id}); no class is on revaluation |
| Audit standard | PCAOB. Auditor PricewaterhouseCoopers LLP, Florham Park, New Jersey, integrated audit of the financial statements and internal control. The reports predate critical audit matters, so none are given |
| Reporting currency | USD |
| Units | statements.xlsx: USD millions. Text files keep each filing's own units. Statements are in thousands of dollars in the FY2011 and FY2012 10-Ks and the 10-Qs for Q1 2011 to Q1 2013, and in millions of dollars in the FY2013 10-K and the Q2 2013 and Q3 2013 10-Qs (checked from each statement header). Earnings-release tables are in millions |
| Fiscal year end | 31 December |
| Periods covered | Quarters: Q1 2011 to Q4 2013 (there is no Q4 10-Q; the workbook's LOCATORS sheet shows how each Q4 value was obtained). Years: FY2009 to FY2013. The earliest annual report in the text files is the FY2011 10-K, whose statements of operations and cash flows also cover FY2010 and FY2009 and whose balance sheet also covers 31 December 2010 |
| Non-GAAP regime | Regulation G and Item 10(e) of Regulation S-K |
| Pack built | 25 September 2026, by Claude (build agent) from EDGAR originals. Scripts: build/download_text.py, build/htmltext.py, build/build_text_pack.py, build/build_manifest.py. Raw downloads in build/raw/ |
| Cut-off | Nothing filed after 31 March 2014 is in the pack |

## How the text files are made

- Each file is the filing's own text, converted from the EDGAR HTML: tags stripped, entities unescaped, one table row per line with cells separated by " | ". A dollar sign, an opening parenthesis or a percent sign printed in its own table cell is joined to the number beside it. Multi-row column headings are flattened one row per line, so read column headings against the data rows with care.
- The only added text is the SOURCE line at the top of each file, and, where a file joins two parts of a filing, a separator line starting "---" that names the part that follows.
- Running page headers printed on each page (for example "ITEM 7. ... (Continued)" or "NOTES TO CONSOLIDATED FINANCIAL STATEMENTS (Continued)") are kept as printed.
- Page markers: `[p. N]` marks the START of printed page N; all text after it, up to the next marker, is on that page. A section file begins with the marker of the page on which the section starts. In the 10-Ks, the 10-Qs, the two proxy statements and ER-Q4-FY2013, N is the printed page number taken from the page footer. The cover and table-of-contents pages before printed page 1 carry no marker. In all other files under releases/ (the other twelve earnings releases, the call slides and the other press releases) the exhibits carry no printed page numbers, so N counts HTML page breaks from the start of each exhibit (for slides, N is the slide number); these are not printed numbers.
- Section keys follow PACK-SPEC. In the annual reports: business (Item 1), risk-factors (Item 1A), legal (Item 3 plus the contingencies note), mdna (Item 7, whole), critical-estimates (the "Critical Accounting Policies and Estimates" part of Item 7, from that heading to the heading "Recent Accounting Pronouncements"; the same text is also in mdna), market-risk (Item 7A, which refers to Item 7, plus the Item 7 "Market Risks" discussion from that heading to the heading "Income Taxes"), auditor-report, financial-statements (all of Item 8: audit report, statements, notes, Schedule I and Schedule II), notes-NN-title (one file per note), schedule-ii, controls (Item 9A), related-parties (Item 13 plus the related-party note). In the 10-Qs: financial-statements (Part I Item 1, statements and notes), notes-NN-title, mdna (Part I Item 2) and risk-factors (Part II Item 1A, where it has more than a no-change statement).
- Note counts were checked against each filing's XBRL FilingSummary (one detail-tagged block per note): every filing matches. FY2011 10-K 17 notes, FY2012 18, FY2013 19; 10-Qs Q1 2011 17, Q2 2011 17, Q3 2011 16, Q1 2012 17, Q2 2012 17, Q3 2012 17, Q1 2013 18, Q2 2013 18, Q3 2013 18. The four notes to Schedule I (parent-company condensed information) are inside the financial-statements files only.

## Files

"""

limits = f"""
## Known limits of this pack

- The balance sheet is unclassified: there are no total current assets or total current liabilities, and debt is a single line. Checklist rows that need working capital totals or a current/non-current split can only be approximated from individual lines.
- There is no cost-of-sales or gross-profit line. Expenses are presented as described in the header table; gross-margin rows cannot be run as specified.
- The pack is as of 31 March 2014 and excludes everything filed later, including the DEF 14A filed 11 April 2014. There is therefore no proxy covering 2013 compensation; PROXY-2012 covers fiscal 2011 and PROXY-2013 covers fiscal 2012.
- The FY2013 10-K/A (filed 20 March 2014, accession 0001364479-14-000008, https://www.sec.gov/Archives/edgar/data/1364479/000136447914000008/hgh2013form10-ka.htm) has no section files. Its explanatory note states that its sole purpose is to correct an error in Exhibit 23.1 (the auditor's consent) and that it repeats the entire text of the original filing with no other changes. A comparison of the two consents shows the corrected consent lists only the Form S-8 registration statements; the original also listed Form S-3 file numbers 333-159348 and 333-173125. A text comparison of the 10-K/A body with the original 10-K found no other differences apart from the amendment cover, the explanatory note and the signature page (the 10-K/A does not repeat the block of individual officer and director signatures dated March 19, 2014).
- The FY2009 and FY2010 10-Ks have no text files (the FY2010 10-K was filed 25 February 2011). In the text files, FY2009 and FY2010 appear only as comparative columns in the FY2011 10-K; the workbook's LOCATORS sheet gives the source of each FY2009 and FY2010 value it holds.
- releases/ also holds the Q4 2010 earnings release (ER-Q4-FY2010) and two other FY2010-cycle Item 2.02 filings (OTHER-2011-01-25, OTHER-2011-02-25), because they were filed inside the window (January and February 2011). The quarters in scope remain Q1 2011 to Q4 2013.
- Hertz filed its earnings call slides as separate Item 2.02 8-Ks; these are the OTHER files. The earnings releases were filed under Item 2.02 with Item 7.01, so the Item 2.02 text at the top of each ER file is a cross-reference to Item 7.01.
- 10-Q Part II Item 1A contains only a no-material-change statement in {', '.join(sorted(rf_skipped))}, so no risk-factors file was made for those quarters. In each, the single sentence says there is no material change in the risk factors reported in the most recent annual report on Form 10-K (Q1-FY2012 also refers to Part II Item 1A of an earlier report). The sentence is not in any pack file; read it at the 10-Q source URL.
- From the 10-Qs only the financial statements, notes, MD&A and risk factors are extracted. Part I Items 3 and 4 and Part II Item 1 (legal proceedings) are not separate files.
- Items 10 to 14 of each 10-K are incorporated by reference from the proxy statement. The related-parties files therefore hold the Item 13 cross-reference plus the related-party note; the proxy's "Certain Relationships and Related Party Transactions" section is not extracted. The proxy files hold the "Executive Compensation" section only (named executive officers, CD&A including incentive-plan metrics and targets, Compensation Committee Report and the compensation tables through the termination and change-in-control disclosures).
- The market-risk file boundary is a judgment: Item 7 prints "Market Risks", "Interest Rate Risk", "Foreign Currency Risk", "Other Risks" and "Inflation" as headings of the same style, so the extract runs from "Market Risks" to "Income Taxes". The whole of Item 7 is in each mdna file.
- Text files were not proofread line by line against the printed filings. Table rows with many columns can be hard to align; for any number used in a finding, check the row against the source URL.
- No sections failed to isolate: every requested section was found in every filing.
"""

manifest = hdr + "\n".join(table) + "\n" + limits
for bad in ("—",):
    assert bad not in manifest, "em-dash in manifest"
(PACK / "manifest.md").write_text(manifest, encoding="utf-8")
assert "—" not in "\n".join(out[:6])
print("rows", len(rows), "ids P2 to", last_id)
