"""HTML filing -> plain text, keeping table rows as one line with ' | ' between cells,
and marking every page-break element with a sentinel so printed page numbers can be recovered."""
import html as htmlmod
import re
from lxml import etree, html as lh

PB = "\u0000PB\u0000"
BLOCK = {"p", "div", "br", "tr", "table", "h1", "h2", "h3", "h4", "h5", "h6", "li", "ul", "ol",
         "center", "blockquote", "pre", "hr", "body", "dl", "dt", "dd", "caption", "thead", "tbody"}
SKIP = {"script", "style", "head", "title"}


def decode(b: bytes) -> str:
    try:
        s = b.decode("utf-8")
    except UnicodeDecodeError:
        s = b.decode("cp1252", "replace")
    return s


def fix_c1(s: str) -> str:
    # numeric refs like &#151; decode to C1 controls in lxml; map them through cp1252
    def f(m):
        try:
            return bytes([ord(m.group(0))]).decode("cp1252")
        except Exception:
            return " "
    return re.sub("[\u0080-\u009f]", f, s)


def is_pagebreak(el) -> bool:
    st = (el.get("style") or "").lower().replace(" ", "")
    return "page-break-before:always" in st or "page-break-after:always" in st


def norm_ws(s: str) -> str:
    s = s.replace(" ", " ").replace("​", "")
    return re.sub(r"[ \t\r\n\f\v]+", " ", s)


def cell_text(td) -> str:
    parts = []
    walk(td, parts, in_cell=True)
    t = "".join(parts).replace(PB, " ")
    t = re.sub(r"\s*\n\s*", " ", t)
    return norm_ws(t).strip()


def merge_cells(cells):
    out = []
    pending = ""
    for c in cells:
        if not c:
            continue
        if c in ("$", "(", "$(", "($", "€", "£", "C$", "US$"):
            pending += c
            continue
        if c in (")", "%", ")%", "%)", "pts", "bps") and out:
            out[-1] = out[-1] + c
            continue
        out.append(pending + c if pending else c)
        pending = ""
    if pending:
        out.append(pending)
    return out


def table_rows(tbl, parts):
    parts.append("\n")
    for tr in tbl.iter("tr"):
        # only rows whose nearest table ancestor is this table
        anc = tr.getparent()
        while anc is not None and anc.tag != "table":
            anc = anc.getparent()
        if anc is not tbl:
            continue
        if any(is_pagebreak(x) for x in tr.iter() if isinstance(x.tag, str)):
            parts.append(PB)
        cells = []
        for td in tr:
            if not isinstance(td.tag, str) or td.tag not in ("td", "th"):
                continue
            nested = td.find(".//table")
            if nested is not None:
                sub = []
                table_rows(nested, sub)
                cells.append(" ".join(x.strip() for x in "".join(sub).split("\n") if x.strip()))
            else:
                cells.append(cell_text(td))
        cells = merge_cells(cells)
        if cells:
            parts.append(" | ".join(cells) + "\n")
    parts.append("\n")


def walk(el, parts, in_cell=False):
    tag = el.tag if isinstance(el.tag, str) else None
    if tag is None:
        # comment / PI: keep tail only
        if el.tail:
            parts.append(norm_ws(el.tail))
        return
    tag = tag.lower()
    if tag in SKIP:
        if el.tail:
            parts.append(norm_ws(el.tail))
        return
    pb = is_pagebreak(el)
    st = (el.get("style") or "").lower().replace(" ", "")
    pb_before = "page-break-before:always" in st
    if pb and pb_before and not in_cell:
        parts.append("\n" + PB + "\n")
    if tag == "table" and not in_cell:
        table_rows(el, parts)
    else:
        if tag in BLOCK:
            parts.append("\n")
        if el.text:
            parts.append(norm_ws(el.text))
        for ch in el:
            walk(ch, parts, in_cell)
        if tag in BLOCK:
            parts.append("\n")
    if pb and not pb_before and not in_cell:
        parts.append("\n" + PB + "\n")
    if el.tail:
        parts.append(norm_ws(el.tail))


def html_to_text(b: bytes) -> str:
    s = decode(b)
    # strip SGML wrapper if present
    s = re.sub(r"(?is)^.*?(<html)", r"\1", s, count=1) if re.search(r"(?i)<html", s) else s
    s = re.sub(r"(?is)</html>.*$", "</html>", s)
    doc = lh.document_fromstring(s)
    parts = []
    walk(doc, parts)
    t = "".join(parts)
    t = fix_c1(t)
    lines = [ln.strip() for ln in t.split("\n")]
    out = []
    blank = False
    for ln in lines:
        if not ln:
            if not blank and out:
                out.append("")
            blank = True
            continue
        out.append(ln)
        blank = False
    return "\n".join(out).strip() + "\n"


PAGENUM = re.compile(r"^(?:page\s+)?((?:[A-Z]{1,2}-)?\d{1,3}|[ivxlc]{1,6}|[A-Z]-?\d{1,3})$", re.I)
RUNNING_HEAD = re.compile(r"^(table of contents|index)$", re.I)


def apply_page_markers(t: str, mode: str = "auto"):
    """Split on page-break sentinels. Each page's printed number is its footer (last line before the
    break). Emit a start-of-page marker [p. N] before each page's content and drop the footer line.
    mode 'auto': printed numbers if at least half the pages carry one, else count pages (1, 2, 3 ...).
    Returns (text, info dict)."""
    chunks = t.split(PB)
    pages = []
    for i, ch in enumerate(chunks):
        lines = ch.split("\n")
        # drop running navigation header at top of page
        j = 0
        while j < len(lines) and not lines[j].strip():
            j += 1
        if i > 0 and j < len(lines) and RUNNING_HEAD.match(lines[j].strip()):
            lines = lines[j + 1:]
        k = len(lines) - 1
        while k >= 0 and not lines[k].strip():
            k -= 1
        num = None
        if k >= 0:
            m = PAGENUM.match(lines[k].strip().strip("|").strip())
            if m:
                num = m.group(1)
                lines = lines[:k]
        body = "\n".join(lines).strip("\n")
        pages.append([num, body])
    # drop empty trailing / leading pages
    pages = [p for p in pages if p[1].strip() or p[0]]
    n_printed = sum(1 for p in pages if p[0])
    use_printed = mode == "printed" or (mode == "auto" and n_printed >= max(1, len(pages) // 2))
    out = []
    seen_numbered = False
    for idx, (num, body) in enumerate(pages, start=1):
        if use_printed:
            if num:
                seen_numbered = True
                out.append(f"[p. {num}]")
            elif seen_numbered:
                out.append("[p. unnumbered]")
        else:
            out.append(f"[p. {idx}]")
        out.append(body)
        out.append("")
    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    info = {"pages": len(pages), "printed": n_printed, "mode": "printed" if use_printed else "count",
            "unnumbered_after_first": sum(1 for x in out if x == "[p. unnumbered]")}
    return text.strip() + "\n", info
