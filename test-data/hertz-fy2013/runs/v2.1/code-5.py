# Turn 5: the report adds no new numbers, so there is nothing to calculate. This script checks that
# (a) every number in reply-5.md already appears in replies 1 to 4, and (b) every quotation is exact and on the cited page.
# It also prints word counts and re-runs the quotation check for all five replies.
import re, sys, io, os

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
D = r"C:\Users\aaron\OneDrive\Desktop\Master\WireSift Research\Events\CFA Vancouver Forensic\test-data\hertz-fy2013"
OUT = D + r"\runs\v2.1"
DOCS = {
    "FY2013 annual report": "annual-report-FY2013-12-31-key-sections.txt",
    "FY2012 annual report": "annual-report-FY2012-12-31-key-sections.txt",
    "FY2013 release": "earnings-release-Q4-FY2013-12-31.txt",
    "FY2012 release": "earnings-release-Q4-FY2012-12-31.txt",
}
TXT = {k: open(os.path.join(D, v), encoding="utf-8").read() for k, v in DOCS.items()}


def page_at(text, pos):
    m = re.findall(r"\[p\. (\w+)\]", text[:pos])
    return m[-1] if m else None


def check_quotes(reply_path, quiet=False):
    reply = open(reply_path, encoding="utf-8").read()
    cited = re.findall(r'"([^"]+)" \(((?:FY2013|FY2012) (?:annual report|release))[^)]*?, p\. (\w+)\)', reply)
    ok = 0
    for q, doc, pg in cited:
        t = TXT[doc]
        pages = [page_at(t, m.start()) for m in re.finditer(re.escape(q), t)]
        good = pg in pages
        ok += good
        if not quiet or not good:
            print(("PASS" if good else "FAIL"), f"| {doc} p. {pg} | found on pages {sorted(set(pages))} | {q[:70]}")
    citedset = {q for q, _, _ in cited}
    uncited = [q for q in re.findall(r'"([^"]+)"', reply) if q not in citedset]
    return len(cited), ok, uncited


replies = {n: open(os.path.join(OUT, f"reply-{n}.md"), encoding="utf-8").read() for n in range(1, 6)}
earlier = " ".join(replies[n] for n in range(1, 5))

print("=== Numbers in reply-5 that do not appear in replies 1 to 4 ===")
nums = set(re.findall(r"\$?-?\d[\d,]*\.?\d*%?", replies[5]))
allowed = {"2009", "2010", "2012", "2013", "2014", "4", "5", "1.", "2.", "3.", "4.", "5."}   # years, list numbering, 'Q4', 'top five'
missing = []
for n in sorted(nums):
    core = n.strip("$").rstrip(".")
    if core in allowed or n in allowed:
        continue
    if core not in earlier and core.replace("-", "") not in earlier:
        missing.append(n)
print(missing if missing else "none")

print("\n=== Quotation check, reply-5.md ===")
n, ok, uncited = check_quotes(os.path.join(OUT, "reply-5.md"))
for q in uncited:
    print("UNCITED quoted string:", q, "| in earlier replies:", q in earlier, "| in documents:", [k for k, t in TXT.items() if q in t])
print(f"{n} cited quotations, {ok} pass")

print("\n=== All replies: words and cited quotations ===")
for k in range(1, 6):
    n, ok, uncited = check_quotes(os.path.join(OUT, f"reply-{k}.md"), quiet=True)
    print(f"reply-{k}: {len(replies[k].split())} words; {n} cited quotations, {ok} pass; other quoted strings: {len(uncited)}")

banned = re.compile(r"\b(fraud|manipulat\w*|red flag)", re.I)
for k in range(1, 6):
    hits = banned.findall(replies[k])
    dash = replies[k].count("\u2014")
    print(f"reply-{k}: banned words {hits}; em-dashes {dash}")
