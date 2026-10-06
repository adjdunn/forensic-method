"""Cut a key-sections annual report down to what the chat prompts read, for companies whose two reports
are too large to attach to one chat conversation.

Usage: python chat_cut.py <company-folder> <fiscal-year> [<fiscal-year> ...]
Reads  annual-report-FY<year>-MM-DD-key-sections.txt and writes annual-report-FY<year>-MM-DD-chat.txt beside it.

What is cut, and why it is safe for the prompts:
- Item 1 (business): only the pages that describe the company, its segments, its fleet or assets, and its risk
  management are kept. Airport concessions, reservations, regulation and "available information" go.
- Item 7 (MD&A): the comparison of the prior year with the year before it goes; it is the prior report's own
  comparison, which the prior report already holds.
- Item 8 (notes): the debt note keeps its summary table and loses the facility-by-facility descriptions; the
  pension, stock compensation and financial instruments notes keep their opening paragraphs only. The parent-only
  Schedule I goes. Schedule II (valuation and qualifying accounts) stays.
Every cut is marked in the text with a line in square brackets, so the model can say when something it needs
has been cut rather than guess. Page markers are untouched, so citations still work against the full report.
"""
import re, sys
from pathlib import Path

KEEP_ITEM1_HEADINGS = ("Our Company", "Corporate History", "Our Markets", "Our Business Segments", "Fleet",
                       "Risk Management", "Third-Party Liability", "Seasonality", "Employees", "All Other Operations")
TRIM_NOTES = {  # note title fragment -> characters kept
    "Debt": 6000,
    "Employee Retirement Benefits": 2500,
    "Stock-Based Compensation": 2000,
    "Financial Instruments": 4000,
}
MARK = "[Cut in this chat copy: {}. The full report has it.]"


def last_marker(cut_text):
    """The page marker the text after a cut falls under: the last one inside the cut region, or none."""
    ms = re.findall(r"\[p\. \d+\]", cut_text)
    return (ms[-1] + "\n") if ms else ""


def pages(text):
    """Split text into (page_number, segment) in order; text before the first marker gets page None."""
    marks = [(m.start(), int(m.group(1))) for m in re.finditer(r"\[p\. (\d+)\]", text)]
    out = []
    prev = 0
    prev_n = None
    for pos, n in marks:
        out.append((prev_n, text[prev:pos]))
        prev, prev_n = pos, n
    out.append((prev_n, text[prev:]))
    return out


def cut_item1(text):
    kept, dropped = [], []
    for n, seg in pages(text):
        heads = set(re.findall(r"(?m)^([A-Z][A-Za-z ,&'-]{3,50})$", seg))
        keep = n is None or bool(heads & set(KEEP_ITEM1_HEADINGS)) or "holding period" in seg
        (kept if keep else dropped).append((n, seg))
        if not keep and (not kept or not kept[-1][1].endswith("\n" + MARK.format("page " + str(n)) + "\n")):
            pass
    out = []
    run = []
    for n, seg in pages(text):
        if (n, seg) in kept:
            if run:
                out.append("\n" + MARK.format(f"business description pages {run[0]} to {run[-1]}") + "\n\n")
                run = []
            out.append(seg)
        else:
            run.append(n)
    if run:
        out.append("\n" + MARK.format(f"business description pages {run[0]} to {run[-1]}") + "\n")
    return "".join(out)


def cut_item7(text, fy):
    m = re.search(rf"(?m)^Year Ended December 31, {fy - 1} Compared with Year Ended December 31, {fy - 2}[^\n]*$", text)
    if not m:
        return text
    end = re.search(r"(?m)^Capital Expenditures$", text[m.start():])
    if not end:
        return text
    cut = text[m.start():m.start() + end.start()]
    return (text[:m.start()] + MARK.format(f"the comparison of {fy - 1} with {fy - 2}, which the prior year's report holds")
            + "\n\n" + last_marker(cut) + text[m.start() + end.start():])


def cut_item8(text):
    heads = [(m.start(), m.group(0)) for m in re.finditer(r"(?m)^Note \d+[^\n]*$|^SCHEDULE I$|^SCHEDULE II$", text)]
    # drop "(Continued)" repeats so each note is one block
    blocks = []
    for pos, h in heads:
        key = re.sub(r"\s*\(Continued\)\s*$", "", h)
        if blocks and blocks[-1][1] == key:
            continue
        blocks.append((pos, key))
    blocks.append((len(text), "END"))
    out = [text[:blocks[0][0]]]
    in_schedule_1 = False
    dropped = ""  # text cut so far since the last kept text, so its last page marker can be restored
    for (p, h), (q, _) in zip(blocks, blocks[1:]):
        seg = text[p:q]
        if h == "SCHEDULE I":
            in_schedule_1 = True
            out.append(MARK.format("Schedule I, the parent company's condensed statements") + "\n\n")
        if h == "SCHEDULE II":
            in_schedule_1 = False
        if in_schedule_1:
            dropped += seg
            continue
        prefix, dropped = last_marker(dropped), ""
        for frag, keep in TRIM_NOTES.items():
            if frag in h and len(seg) > keep + 500:
                cutpoint = seg.rfind("\n", 0, keep)
                dropped = seg[cutpoint:]
                seg = seg[:cutpoint] + "\n\n" + MARK.format(f"the rest of {h.split(chr(8212))[-1].strip() if chr(8212) in h else h}") + "\n\n"
                break
        out.append(prefix + seg)
    return "".join(out)


def main():
    folder = Path(sys.argv[1])
    for fy in map(int, sys.argv[2:]):
        src = next(folder.glob(f"annual-report-FY{fy}-*-key-sections.txt"))
        text = src.read_text(encoding="utf-8")
        parts = re.split(r"(?m)^=== (Item \w+) ===\n", text)
        header, items = parts[0], [(parts[i], parts[i + 1]) for i in range(1, len(parts), 2)]
        out = [header.rstrip("\n") + "\nChat copy: cut for attachment to one conversation; each cut is marked in square brackets. "
               "Page markers are those of the full report.\n\n"]
        for name, body in items:
            if name == "Item 1":
                body = cut_item1(body)
            elif name == "Item 7":
                body = cut_item7(body, fy)
            elif name == "Item 8":
                body = cut_item8(body)
            out.append(f"=== {name} ===\n{body}")
        dst = src.with_name(src.name.replace("-key-sections", "-chat"))
        result = "".join(out)
        dst.write_text(result, encoding="utf-8")
        print(f"{dst.name}: {len(text):,} -> {len(result):,} chars (~{len(result) // 4:,} tokens)")


if __name__ == "__main__":
    main()
