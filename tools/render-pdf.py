"""Render a prompt reply (markdown) to a styled PDF, for reading and for slides.

Usage: python render-pdf.py <reply.md> <out.pdf> [--title "..."] [--subtitle "..."]
Handles the markdown the prompts produce: pipe tables, paragraphs with **bold**, numbered and bulleted lists
(a list item may run over several indented lines), and ### headings. Built with reportlab; fonts from Windows.
"""
import argparse, re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import KeepTogether, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

FONTS = Path(r"C:\Windows\Fonts")
pdfmetrics.registerFont(TTFont("Serif", str(FONTS / "georgia.ttf")))
pdfmetrics.registerFont(TTFont("Serif-Bold", str(FONTS / "georgiab.ttf")))
pdfmetrics.registerFont(TTFont("Serif-Italic", str(FONTS / "georgiai.ttf")))
pdfmetrics.registerFont(TTFont("Sans", str(FONTS / "segoeui.ttf")))
pdfmetrics.registerFont(TTFont("Sans-Bold", str(FONTS / "segoeuib.ttf")))
pdfmetrics.registerFontFamily("Serif", normal="Serif", bold="Serif-Bold", italic="Serif-Italic", boldItalic="Serif-Bold")
pdfmetrics.registerFontFamily("Sans", normal="Sans", bold="Sans-Bold", italic="Sans", boldItalic="Sans-Bold")

NAVY = colors.HexColor("#223a55")
INK = colors.HexColor("#1d1d1b")
GREY = colors.HexColor("#5c5c58")
RULE = colors.HexColor("#d9d9d4")
BAND = colors.HexColor("#f5f5f2")

S = {
    "title": ParagraphStyle("title", fontName="Serif", fontSize=19, leading=23, textColor=INK, spaceAfter=2),
    "sub": ParagraphStyle("sub", fontName="Sans", fontSize=9, leading=12, textColor=GREY, spaceAfter=10),
    "h2": ParagraphStyle("h2", fontName="Sans-Bold", fontSize=12, leading=15, textColor=NAVY, spaceBefore=14, spaceAfter=5, keepWithNext=1),
    "h3": ParagraphStyle("h3", fontName="Sans-Bold", fontSize=10.5, leading=13, textColor=INK, spaceBefore=9, spaceAfter=3, keepWithNext=1),
    "body": ParagraphStyle("body", fontName="Serif", fontSize=10.3, leading=14.2, textColor=INK, spaceAfter=5),
    "note": ParagraphStyle("note", fontName="Sans", fontSize=8.6, leading=11.5, textColor=colors.HexColor("#3f3f3b"), backColor=BAND, borderPadding=(4, 6, 4, 6), spaceBefore=4, spaceAfter=10, leftIndent=3),
    "li": ParagraphStyle("li", fontName="Serif", fontSize=10.3, leading=14, textColor=INK, spaceAfter=1, leftIndent=16, bulletIndent=0, bulletFontName="Sans-Bold", bulletFontSize=9.5),
    "li2": ParagraphStyle("li2", fontName="Sans", fontSize=9, leading=12, textColor=colors.HexColor("#3f3f3b"), spaceAfter=7, leftIndent=16),
    "cell": ParagraphStyle("cell", fontName="Sans", fontSize=8, leading=9.6, textColor=INK, alignment=TA_LEFT),
    "cellr": ParagraphStyle("cellr", fontName="Sans", fontSize=8, leading=9.6, textColor=INK, alignment=TA_RIGHT),
    "head": ParagraphStyle("head", fontName="Sans-Bold", fontSize=7.8, leading=9.4, textColor=colors.white),
    "headr": ParagraphStyle("headr", fontName="Sans-Bold", fontSize=7.8, leading=9.4, textColor=colors.white, alignment=TA_RIGHT),
    "foot": ParagraphStyle("foot", fontName="Sans", fontSize=8, leading=10.5, textColor=colors.HexColor("#7a7a74"), spaceBefore=14),
}


def inline(s: str) -> str:
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<i>\1</i>", s)
    s = re.sub(r"`(.+?)`", r"<font face='Sans'>\1</font>", s)
    return s


def is_num(s: str) -> bool:
    return bool(re.fullmatch(r"[-+\u2212]?[\d.,]+\s*(%|x|pts)?|n/a|", s.strip()))


def table_flowable(rows, width):
    head, body = rows[0], rows[2:] if re.fullmatch(r"\s*\|?[\s:|-]+\|?\s*", rows[1]) else rows[1:]
    def cells(r): return [c.strip() for c in r.strip().strip("|").split("|")]
    h = cells(head); data = [cells(r) for r in body]
    ncol = len(h)
    data = [r + [""] * (ncol - len(r)) for r in data]
    numeric = [all(is_num(r[j]) for r in data if j < len(r)) for j in range(ncol)]
    out = [[Paragraph(inline(c), S["headr"] if numeric[j] and j else S["head"]) for j, c in enumerate(h)]]
    for r in data:
        out.append([Paragraph(inline(c), S["cellr"] if numeric[j] and j else S["cell"]) for j, c in enumerate(r)])
    if sum(numeric[1:]) >= (ncol - 1) / 2:  # a table of figures: a wide label column, equal number columns
        first = min(0.34 * width, 150) if ncol > 4 else 0.4 * width
        widths = [first] + [(width - first) / max(1, ncol - 1)] * (ncol - 1)
    else:  # a table of text: widths follow how much each column has to say
        weight = [max(8, min(70, max(len(r[j]) for r in [h] + data))) ** 0.75 for j in range(ncol)]
        widths = [width * w / sum(weight) for w in weight]
    t = Table(out, colWidths=widths, repeatRows=1)
    style = [("BACKGROUND", (0, 0), (-1, 0), NAVY), ("VALIGN", (0, 0), (-1, -1), "TOP"),
             ("LINEBELOW", (0, 1), (-1, -1), 0.4, RULE), ("TOPPADDING", (0, 0), (-1, -1), 2.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5),
             ("LEFTPADDING", (0, 0), (-1, -1), 4), ("RIGHTPADDING", (0, 0), (-1, -1), 4)]
    for i in range(2, len(out), 2):
        style.append(("BACKGROUND", (0, i), (-1, i), BAND))
    t.setStyle(TableStyle(style))
    return t


def build(text: str, out: Path, title: str, subtitle: str):
    doc = SimpleDocTemplate(str(out), pagesize=letter, leftMargin=16 * mm, rightMargin=16 * mm, topMargin=16 * mm, bottomMargin=16 * mm,
                            title=title or out.stem, author="")
    width = letter[0] - 32 * mm
    story = []
    if title: story.append(Paragraph(inline(title), S["title"]))
    if subtitle: story.append(Paragraph(inline(subtitle), S["sub"]))
    lines = text.replace("\r", "").split("\n")
    i = 0
    pending_title = None
    while i < len(lines):
        ln = lines[i]
        if not ln.strip():
            i += 1; continue
        if ln.lstrip().startswith("|"):
            rows = []
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                rows.append(lines[i]); i += 1
            story.append(table_flowable(rows, width)); story.append(Spacer(1, 6)); continue
        m = re.match(r"^(#{1,3})\s+(.*)", ln)
        if m:
            story.append(Paragraph(inline(m.group(2)), S["h2"] if len(m.group(1)) <= 2 else S["h3"])); i += 1; continue
        m = re.match(r"^(\d+)\.\s+(.*)", ln)
        if m or re.match(r"^[-*]\s+", ln):
            ordered = bool(m)
            n = 0
            while i < len(lines) and (re.match(r"^(\d+)\.\s+", lines[i]) if ordered else re.match(r"^[-*]\s+", lines[i])):
                n += 1
                first = re.sub(r"^(\d+\.|[-*])\s+", "", lines[i]); i += 1
                extra = []
                while i < len(lines) and lines[i].startswith((" ", "	")) and lines[i].strip():
                    extra.append(lines[i].strip()); i += 1
                bullet = f"{n}." if ordered else "•"
                paras = [Paragraph(inline(first), S["li"], bulletText=bullet)] + [Paragraph(inline(e), S["li2"]) for e in extra]
                if pending_title is not None:  # keep a title on the same page as its first item
                    paras = [pending_title] + paras
                    pending_title = None
                story.append(KeepTogether(paras))
                # a blank line between items does not end the list if the next line is another item
                j = i
                while j < len(lines) and not lines[j].strip():
                    j += 1
                if j < len(lines) and (re.match(r"^(\d+)\.\s+", lines[j]) if ordered else re.match(r"^[-*]\s+", lines[j])):
                    i = j
            story.append(Spacer(1, 4)); continue
        para = [ln]; i += 1
        while i < len(lines) and lines[i].strip() and not lines[i].lstrip().startswith(("|", "#")) and not re.match(r"^(\d+\.|[-*])\s+", lines[i]):
            para.append(lines[i]); i += 1
        p = " ".join(x.strip() for x in para)
        if re.fullmatch(r"\*\*[^*]+\*\*", p):  # a bold line on its own is a title: keep it with what follows
            j = i
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines) and re.match(r"^(\d+\.|[-*])\s+", lines[j]):
                pending_title = Paragraph(inline(p), S["h3"]); i = j
            else:
                story.append(Paragraph(inline(p), S["h3"]))
        else:
            story.append(Paragraph(inline(p), S["note"] if p.startswith(("Cost line", "**Cost line")) else S["body"]))
    story.append(Paragraph("Items to check, not findings. Every figure was calculated in code from the attached documents; the code is available on request.", S["foot"]))
    doc.build(story)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src"); ap.add_argument("out")
    ap.add_argument("--title", default=""); ap.add_argument("--subtitle", default="")
    a = ap.parse_args()
    out = Path(a.out).resolve(); out.parent.mkdir(parents=True, exist_ok=True)
    build(Path(a.src).read_text(encoding="utf-8"), out, a.title, a.subtitle)
    print("wrote", out, out.stat().st_size, "bytes")


if __name__ == "__main__":
    main()
