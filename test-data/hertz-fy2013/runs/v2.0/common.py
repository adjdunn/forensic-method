# Shared helpers for turns 2 to 5: read the attached text files, pull numbers from
# named table rows, and check every quotation in a reply against its source file.
import os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.abspath(os.path.join(HERE, "..", ".."))

FILES = {
    "FY2012 annual report": "annual-report-FY2012-12-31-key-sections.txt",
    "FY2013 annual report": "annual-report-FY2013-12-31-key-sections.txt",
    "FY2012 release": "earnings-release-Q4-FY2012-12-31.txt",
    "FY2013 release": "earnings-release-Q4-FY2013-12-31.txt",
}
_cache = {}
def text(doc):
    if doc not in _cache:
        _cache[doc] = open(os.path.join(DATA, FILES[doc]), encoding="utf-8").read()
    return _cache[doc]

PAGE = re.compile(r"^\[p\. ([^\]]+)\]", re.M)
def page_at(doc, pos):
    """Nearest [p. N] marker above character position pos."""
    last = None
    for m in PAGE.finditer(text(doc)):
        if m.start() > pos: break
        last = m.group(1)
    return last

def page_span(doc, page, nth=0):
    """(start, end) character span of the nth block that starts with [p. page]."""
    t = text(doc); ms = list(PAGE.finditer(t))
    hits = [i for i, m in enumerate(ms) if m.group(1) == str(page)]
    i = hits[nth]
    return ms[i].start(), (ms[i+1].start() if i+1 < len(ms) else len(t))

def _num(cell):
    c = cell.strip().replace("$", "").replace(",", "").replace("%", "")
    neg = c.startswith("(") and c.endswith(")")
    c = c.strip("()")
    try: v = float(c)
    except ValueError: return None
    return -v if neg else v

def row(doc, label, page=None, nth=0, after=None):
    """Numbers on the nth line that starts with `label` (optionally on a given page,
    optionally after the first occurrence of the string `after`)."""
    t = text(doc); lo, hi = 0, len(t)
    if page is not None: lo, hi = page_span(doc, page)
    if after is not None:
        a = t.find(after, lo, hi); assert a >= 0, after; lo = a
    seg = t[lo:hi]
    lines = [l for l in seg.split("\n") if l.startswith(label)]
    assert len(lines) > nth, (doc, label, page, after)
    cells = lines[nth].split(" | ")[1:]
    vals = [_num(c) for c in cells]
    return [v for v in vals if v is not None]

QUOTE = re.compile(r'"([^"\n]+)"\s*\(([^()]*?)\)')
def check_quotes(reply_file, verbose=True):
    """Every "quotation" (doc, p. N) in the reply must be an exact substring of the cited
    file and sit under the cited page marker. Returns (n, n_pass, failures)."""
    r = open(os.path.join(HERE, reply_file), encoding="utf-8").read()
    n = ok = 0; fails = []
    for m in QUOTE.finditer(r):
        q, cite = m.group(1), m.group(2)
        doc = next((d for d in FILES if d in cite), None)
        pm = re.search(r"p\. ([A-Za-z0-9]+)", cite)
        if doc is None or pm is None:
            fails.append(("citation not understood", q, cite)); n += 1; continue
        n += 1
        t = text(doc); hits = [x.start() for x in re.finditer(re.escape(q), t)]
        if not hits:
            fails.append(("not an exact substring", q, cite)); continue
        pages = {page_at(doc, h) for h in hits}
        if pm.group(1) not in pages:
            fails.append((f"page is {sorted(pages)} not {pm.group(1)}", q, cite)); continue
        ok += 1
    # quoted strings with no citation right after them
    cited = {m.group(1) for m in QUOTE.finditer(r)}
    loose = [q for q in re.findall(r'"([^"\n]+)"', r) if q not in cited]
    if verbose:
        print(f"{reply_file}: {n} quotations, {ok} pass, {len(fails)} fail; {len(loose)} quoted strings without a citation")
        for f in fails: print("  FAIL:", f)
        for q in loose: print("  uncited:", q)
    return n, ok, fails, loose

def wc(reply_file):
    r = open(os.path.join(HERE, reply_file), encoding="utf-8").read()
    return len(re.findall(r"\S+", r))
