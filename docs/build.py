"""Build the public page (docs/index.html) and the sample-output pages (docs/outputs/*.html) from the repository.

    python docs/build.py

The page is generated, never hand-edited: the prompts come from tools/prompts/, the sample outputs from a named run
folder, so the page cannot drift from the files. Served by GitHub Pages from the docs/ folder.
"""
import datetime as dt, html, json, re
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
PROMPTS = ROOT / "tools" / "prompts"
VERSION = "v2.26"
SAMPLES = [  # (slug, title, run folder, one line on what to notice)
    ("home-depot", "The Home Depot, fiscal 2025", "runs/home-depot-fy2025/v2.26/claude-code/001",
     "A large retailer with two recent acquisitions and no known accounting problem. Notice that nothing is called a contradiction, "
     "every reading is ordinary or can't tell, and the report still gives an analyst five places to look."),
    ("hertz", "Hertz Global Holdings, fiscal 2013", "runs/hertz-fy2013/v2.26/claude-code/001",
     "A company that was later the subject of an SEC enforcement order over its depreciation accounting, run on the filings as they "
     "stood in March 2014 and nothing later. Notice the first item: a sentence in the audited notes set against the numbers in the same "
     "note, with the company's own stated reason beside it."),
]
REPLY_FILES = [("report-5.md", "The report"), ("numbers-1.md", "Prompt 1, scan the numbers"), ("numbers-2.md", "Prompt 2, follow the flags"),
               ("text-3.md", "Prompt 3, read the footnotes"), ("text-4.md", "Prompt 4, compare the footnotes")]

PROMPT_INFO = [
    ("1-scan-the-numbers.md", "Scan the numbers", "Numbers track, step 1",
     "Calculates the standard measures from the spreadsheet and picks up to five movements worth a closer look, each with a size and how long it has run. It does not explain them."),
    ("2-follow-the-flags.md", "Follow the flags", "Numbers track, step 2",
     "Finds the company's explanation for each flag in the reports and releases, tests it against the numbers it relies on, and chooses a reading."),
    ("3-read-the-footnotes.md", "Read the footnotes", "Text track, step 1",
     "Judges where each accounting policy sits in the latest report as it stands: leans conservative, typical, leans aggressive, or can't tell. Tests every claim a number can test."),
    ("4-compare-the-footnotes.md", "Compare the footnotes", "Text track, step 2",
     "Puts the two reports side by side: what changed, what stayed the same while the numbers moved, and what the company discloses as a change in estimate."),
    ("5-report.md", "Report", "Last, in the text conversation",
     "Gathers everything the four replies found, merges it by account, and ranks it by strength of evidence for an analyst deciding where to spend reading time."),
]

CSS = """
:root{--ink:#1d1d1b;--muted:#5c5c58;--navy:#223a55;--rule:#d9d9d4;--band:#f5f5f2;--bg:#ffffff;--accent:#2b5c8a}
@media (prefers-color-scheme: dark){:root:not([data-theme=light]){--ink:#e8e8e4;--muted:#a6a6a0;--navy:#9db8d6;--rule:#3a3a38;--band:#1c1c1b;--bg:#121211;--accent:#8ab4e0}}
:root[data-theme=dark]{--ink:#e8e8e4;--muted:#a6a6a0;--navy:#9db8d6;--rule:#3a3a38;--band:#1c1c1b;--bg:#121211;--accent:#8ab4e0}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.55 Georgia,"Times New Roman",serif}
main{max-width:760px;margin:0 auto;padding:40px 16px 80px}
h1{font:600 34px/1.15 "Segoe UI",system-ui,sans-serif;color:var(--navy);margin:0 0 6px}
h2{font:600 22px/1.25 "Segoe UI",system-ui,sans-serif;color:var(--navy);margin:48px 0 12px;padding-top:18px;border-top:1px solid var(--rule)}
h3{font:600 17px/1.3 "Segoe UI",system-ui,sans-serif;margin:22px 0 6px}
p{margin:0 0 14px}
.lede{font-size:19px;color:var(--ink)}
.meta{font:14px/1.5 "Segoe UI",system-ui,sans-serif;color:var(--muted);margin-bottom:28px}
.status{display:inline-block;font:13px/1 "Segoe UI",system-ui,sans-serif;background:var(--band);border:1px solid var(--rule);border-radius:4px;padding:6px 10px;margin:0 0 20px}
a{color:var(--accent)}
ul,ol{padding-left:22px;margin:0 0 14px} li{margin:4px 0}
table{border-collapse:collapse;width:100%;font:15px/1.4 "Segoe UI",system-ui,sans-serif;margin:8px 0 18px}
th{text-align:left;background:var(--navy);color:#fff;padding:7px 9px;font-weight:600}
td{padding:7px 9px;border-bottom:1px solid var(--rule);vertical-align:top}
tr:nth-child(even) td{background:var(--band)}
details{border:1px solid var(--rule);border-radius:6px;margin:10px 0;background:var(--band)}
summary{cursor:pointer;padding:12px 14px;font:600 16px/1.3 "Segoe UI",system-ui,sans-serif;list-style:none}
summary::-webkit-details-marker{display:none}
summary::before{content:"+ ";color:var(--accent)} details[open] summary::before{content:"\\2013 "}
summary small{display:block;font-weight:400;color:var(--muted);margin-top:3px}
.prompt{padding:0 14px 14px}
.prompt pre{white-space:pre-wrap;font:14px/1.5 "Segoe UI",system-ui,sans-serif;background:var(--bg);border:1px solid var(--rule);border-radius:4px;padding:14px;max-height:420px;overflow:auto;margin:8px 0}
button.copy{font:600 14px/1 "Segoe UI",system-ui,sans-serif;background:var(--navy);color:#fff;border:0;border-radius:4px;padding:9px 14px;cursor:pointer}
button.copy:hover{opacity:.9}
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:14px 0 18px}
.step{background:var(--band);border:1px solid var(--rule);border-radius:6px;padding:14px}
.step b{display:block;font:600 15px/1.3 "Segoe UI",system-ui,sans-serif;color:var(--navy);margin-bottom:6px}
.step p{font-size:15px;margin:0}
@media (max-width:640px){.steps{grid-template-columns:1fr}}
.cards{display:grid;grid-template-columns:1fr 1fr;gap:14px}
@media (max-width:640px){.cards{grid-template-columns:1fr}}
.card{border:1px solid var(--rule);border-radius:6px;padding:16px;background:var(--band)}
.card h3{margin-top:0}
.card p{font-size:15px}
footer{margin-top:60px;padding-top:18px;border-top:1px solid var(--rule);font:14px/1.6 "Segoe UI",system-ui,sans-serif;color:var(--muted)}
.reply{margin:28px 0}
.reply h2{margin-top:36px}
.reply table{font-size:14px}
.reply pre{white-space:pre-wrap;font-size:14px}
nav.top{font:14px/1.5 "Segoe UI",system-ui,sans-serif;color:var(--muted);margin-bottom:24px}
nav.top a{margin-right:14px}

.hero{background:#0f1b2d;color:#e9eef5;margin:0 -16px;padding:48px 16px 40px}
.hero .in{max-width:760px;margin:0 auto}
.hero .kicker{font:600 12px/1 "Segoe UI",system-ui,sans-serif;letter-spacing:.12em;text-transform:uppercase;color:#7fb3e6;margin-bottom:14px}
.hero h1{color:#fff;font-size:40px;margin-bottom:12px}
.hero p{color:#c9d4e2;font-size:18px;max-width:640px}
.hero .pill{display:inline-block;font:13px/1 "Segoe UI",system-ui,sans-serif;color:#e9eef5;border:1px solid #37527a;border-radius:999px;padding:7px 12px;margin:6px 0 22px}
.hero .btns a{display:inline-block;font:600 15px/1 "Segoe UI",system-ui,sans-serif;text-decoration:none;border-radius:6px;padding:12px 16px;margin:0 10px 10px 0}
.hero .btns a.primary{background:#4f8fd6;color:#fff}
.hero .btns a.ghost{color:#e9eef5;border:1px solid #37527a}
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin:28px 0 8px}
@media (max-width:640px){.stats{grid-template-columns:1fr 1fr}}
.stat{border:1px solid var(--rule);border-radius:6px;padding:14px 14px 12px;background:var(--band)}
.stat b{display:block;font:700 30px/1 "Segoe UI",system-ui,sans-serif;color:var(--navy);margin-bottom:6px}
.stat span{font:14px/1.35 "Segoe UI",system-ui,sans-serif;color:var(--muted)}
.flow{background:#0f1b2d;color:#e9eef5;border-radius:10px;padding:26px 22px 18px;margin:18px 0 8px;font-family:"Segoe UI",system-ui,sans-serif}
.flow .kicker{font:600 12px/1 "Segoe UI",system-ui,sans-serif;letter-spacing:.12em;text-transform:uppercase;color:#7fb3e6;margin-bottom:10px}
.flow h3{color:#fff;margin:0 0 20px;font-size:21px;line-height:1.25}
.flow .grid{display:grid;grid-template-columns:150px 28px 1fr 28px 170px;gap:10px;align-items:stretch}
.flow .col{display:flex;flex-direction:column;gap:10px}
.flow .lab{font:600 11px/1 "Segoe UI",system-ui,sans-serif;letter-spacing:.1em;text-transform:uppercase;color:#7fb3e6;margin-bottom:2px}
.flow .in{background:#162741;border:1px solid #2b456b;border-radius:6px;padding:9px 10px;font-size:13px;line-height:1.3}
.flow .in b{display:block;color:#fff;font-size:13px}
.flow .in span{color:#9fb0c6}
.flow .note{font-size:12px;color:#9fb0c6;line-height:1.3;margin-top:4px}
.flow .arrow{display:flex;flex-direction:column;align-items:center;justify-content:center;color:#7fb3e6;font-size:12px;text-align:center;line-height:1.2}
.flow .arrow i{font-style:normal;font-size:22px;line-height:1;display:block}
.flow .track{border:1px solid #2b456b;border-radius:8px;padding:12px;background:#132238}
.flow .track .lab{margin-bottom:8px}
.flow .cards{display:grid;grid-template-columns:1fr 24px 1fr;gap:8px;align-items:stretch}
.flow .card{background:#1b2f4d;border:1px solid #35527c;border-radius:6px;padding:10px 11px;font-size:13px;line-height:1.3}
.flow .card b{display:block;color:#fff;margin-bottom:3px}
.flow .card b em{font-style:normal;color:#7fb3e6;margin-right:6px}
.flow .card span{color:#c9d4e2}
.flow .card .arrow{height:100%}
.flow .final{background:#4f8fd6;color:#fff;border-radius:8px;padding:16px 14px;display:flex;flex-direction:column;justify-content:center;font-size:13px;line-height:1.35}
.flow .final b{display:block;font-size:15px;margin-bottom:6px}
.flow .final b em{font-style:normal;color:#dbe9f8;margin-right:6px}
.flow .cap{text-align:center;color:#c9d4e2;font-size:14px;margin:18px 0 0}
@media (max-width:700px){.flow .grid{grid-template-columns:1fr}.flow .arrow{flex-direction:row;gap:8px;padding:4px 0}.flow .arrow i{transform:rotate(90deg)}.flow .cards{grid-template-columns:1fr}.flow .card .arrow i{transform:rotate(90deg)}}
.finding{border-left:4px solid var(--accent);background:var(--band);padding:14px 18px;margin:16px 0 8px;font-size:16px}
.finding .who{font:600 13px/1 "Segoe UI",system-ui,sans-serif;color:var(--muted);text-transform:uppercase;letter-spacing:.08em;margin-bottom:8px}
.finding ul{margin:6px 0 8px}
.finding li{margin:3px 0}
.finding .more{font:14px "Segoe UI",system-ui,sans-serif}
"""

JS = """
document.querySelectorAll('button.copy').forEach(function(b){b.addEventListener('click',function(){
  var t=document.getElementById(b.dataset.target).textContent;
  navigator.clipboard.writeText(t).then(function(){var o=b.textContent;b.textContent='Copied';setTimeout(function(){b.textContent=o},1500)});
})});
"""


def md(text: str) -> str:
    return markdown.markdown(text, extensions=["tables", "sane_lists"])


def prompt_body(name: str) -> str:
    text = (PROMPTS / name).read_text(encoding="utf-8")
    return text.split("\n---\n", 1)[1].strip() if "\n---\n" in text else text


def page(title: str, body: str, nav: str = "") -> str:
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><style>{CSS}</style></head>
<body><main>{nav}{body}</main><script>{JS}</script></body></html>"""


def build_index() -> str:
    today = dt.date.today().strftime("%d %B %Y").lstrip("0")
    parts = []
    parts.append(f"""
<div class="hero"><div class="in">
<div class="kicker">Open source, in testing</div>
<h1>Forensic Method</h1>
<p>Five prompts that run a forensic accounting review of a public company's filings in Claude or ChatGPT, and the test harness that checks every quotation, figure and claim they produce.</p>
<span class="pill">Prompts {VERSION} &middot; two companies tested &middot; page built {today}</span>
<div class="btns"><a class="primary" href="#prompts">Get the prompts</a><a class="ghost" href="#outputs">See a sample output</a><a class="ghost" href="https://github.com/adjdunn/forensic-method">Repository</a></div>
</div></div>
<div class="stats">
<div class="stat"><b>13</b><span>runs, every one checked against the filings</span></div>
<div class="stat"><b>0</b><span>fabricated numbers or misquoted sentences found</span></div>
<div class="stat"><b>0</b><span>claims taken from outside the attached documents</span></div>
<div class="stat"><b>7 of 7</b><span>runs since v2.23 passed the answer key on the enforcement case</span></div>
</div>
<p class="lede">You attach a company's filings, paste five short prompts in order across two conversations, and finish with a one-page list of items worth an analyst's time, each with a page reference, a size, and a reading of what is most likely going on. The prompts are below with copy buttons; the outputs and the test results are below them; the code that checks them is in the repository.</p>
""")
    parts.append("""
<h2 id="idea">The idea</h2>
<ul>
<li>AI can do the whole job: extract the numbers, calculate the ratios, spot the trends and flags, read the footnotes, and compare them from one year to the next.</li>
<li>Extraction and ratios are the easy part. A data terminal, a spreadsheet or a script does them too. The prompts calculate in code so a result can be re-run and checked.</li>
<li>The value is in what comes after: picking the movements that matter, following each one into the footnotes and press releases for the company's explanation, and testing that explanation against the company's own numbers.</li>
<li>Separately, the footnotes are read for what no ratio shows: where each accounting policy sits, what changed between two years, and what stayed the same while the numbers around it moved.</li>
<li>This is not only about fraud. Most of what it finds is a business weakening or earnings of poor quality, which is far more common and matters just as much.</li>
</ul>
""")
    parts.append("""
<h2 id="run">How to run it</h2>
<div class="flow">
<div class="kicker">The workflow</div>
<h3>A multi-step workflow: five prompts, two separate AI conversations, one final report.</h3>
<div class="grid">
<div class="col"><div class="lab">Inputs</div>
<div class="in"><b>Annual report</b><span>this year and last</span></div>
<div class="in"><b>Quarterly release</b><span>this year and last</span></div>
<div class="in"><b>Financial statements</b><span>as a spreadsheet</span></div>
<div class="note">Attached once to each conversation</div></div>
<div class="arrow"><i>&rarr;</i>attach</div>
<div class="col">
<div class="track"><div class="lab">Numbers &middot; conversation 1</div><div class="cards">
<div class="card"><b><em>1</em>Scan the numbers</b><span>Flags up to five movements, each with a size</span></div>
<div class="arrow"><i>&rarr;</i></div>
<div class="card"><b><em>2</em>Follow the flags</b><span>Tests the company's explanation for each flag</span></div></div></div>
<div class="track"><div class="lab">Text &middot; conversation 2</div><div class="cards">
<div class="card"><b><em>3</em>Read the footnotes</b><span>Reads nine areas of this year's notes and tests every claim</span></div>
<div class="arrow"><i>&rarr;</i></div>
<div class="card"><b><em>4</em>Compare the footnotes</b><span>Compares with last year's notes: what changed, what stayed the same</span></div></div></div>
</div>
<div class="arrow"><i>&rarr;</i>attach the replies</div>
<div class="final"><b><em>5</em>Final report</b>Merges both tracks. Ranks on strength of evidence, then size. Adds nothing new.</div>
</div>
<p class="cap">A single-prompt version is available and simpler to run, but less thorough.</p>
</div>
<p>Works in Claude or ChatGPT on a plan that accepts file uploads and runs code. One prompt per message; read each reply before sending the next. About 45 minutes end to end. The full user guide, with what each file must contain and how to read the results, is <a href="https://claude.ai/code/artifact/22260383-1e93-444d-8f9d-6acacf4f4886">here</a>.</p>
""")
    parts.append('<h2 id="prompts">The prompts</h2><p>Each prompt is a page or less. Expand one to read it; Copy takes the whole thing. The headers tell you which conversation and which files.</p>')
    for i, (fname, title, track, purpose) in enumerate(PROMPT_INFO, 1):
        body = prompt_body(fname)
        parts.append(f"""
<details><summary>{i}. {html.escape(title)}<small>{html.escape(track)}. {html.escape(purpose)}</small></summary>
<div class="prompt"><button class="copy" data-target="p{i}">Copy prompt {i}</button><pre id="p{i}">{html.escape(body)}</pre></div></details>""")
    single = prompt_body("single/review.md")
    parts.append(f"""
<h3>The single-prompt experiment</h3>
<p>The same rules in one message, for one conversation. Tested once so far: it found the central contradiction at Hertz and passed the answer key, in less than half the words, but it dropped the company's own sentence linking lower depreciation to longer holding periods and buried the unchanged 18-month average in a table. Use it for a first pass; use the five prompts when the finding has to stand up to another reader.</p>
<details><summary>Single prompt<small>One conversation, same five files, one reply.</small></summary>
<div class="prompt"><button class="copy" data-target="ps">Copy the single prompt</button><pre id="ps">{html.escape(single)}</pre></div></details>
""")
    parts.append("""<h2 id="outputs">What it produces</h2>
<p>Here is the first item from the Hertz report, as the model wrote it. This is what a finding looks like: the company's own sentence, the number in the same note that contradicts it, the pages, the size, and a reading that is a judgment, not a verdict.</p>
<div class="finding"><div class="who">Hertz Global Holdings, fiscal 2013 &middot; item 1 of 5 &middot; level 1, audited notes</div>
<b>Car depreciation: rates cut while the same note shows losses on car sales</b>
<ul>
<li>Note 8 says the U.S. rate cuts ($44.2m) were "indicative of the residual values experienced". The same note shows a $48.2m U.S. loss on sales "due to declining residual values" (p.126).</li>
<li>The word "strong" was dropped from that sentence this year (FY2012 p.113).</li>
<li>The car holding-period range was extended from 4 to 28 months to 4 to 36 months and relabelled from "useful lives" to "holding periods" (p.81 to p.91). It is not presented as a change in estimate.</li>
<li>The U.S. average holding period stays at "eighteen months" (p.11, both years). Yet the MD&amp;A newly cites "longer holding periods" (p.53).</li>
<li>Size: $152.1m of depreciation not charged at the 2012 rate, 22.9% of pre-tax income. Ranks on 22.9%.</li>
</ul>
<p class="more">Reading: most likely the reporting is stretched (one track), possibly (the other). The SEC's 2018 order against the company turned on the same depreciation estimates. The prompts never saw the order; the run used nothing filed after March 2014. <a href="outputs/hertz.html">Read the whole report and the four replies behind it.</a></p>
</div>
<p>Two companies, the same five prompts, run the same way. Each page holds the report and the four replies behind it, exactly as the model wrote them, with nothing edited.</p><div class="cards">""")
    for slug, title, run, notice in SAMPLES:
        parts.append(f'<div class="card"><h3><a href="outputs/{slug}.html">{html.escape(title)}</a></h3><p>{html.escape(notice)}</p></div>')
    parts.append("</div>")
    parts.append("""
<h2 id="results">Test results</h2>
<p>Every run is checked the same way: each quotation is looked up in the filing and must be exact and on the cited page; each figure is checked against the filing or recomputed; shares of pre-tax income are recomputed; banned words and anything from after the filing date are flagged. Hertz has an answer key written from the SEC's order before any run, so each Hertz run is also scored by an independent agent on what the order says was visible at the time.</p>
<table>
<tr><th>Company</th><th>Runs</th><th>Result</th></tr>
<tr><td>The Home Depot, fiscal 2025 (no known problem)</td><td>Chat, then four harness runs, prompts v2.22 to v2.26</td><td>Clean every time. No sentence called a contradiction; every reading ordinary or can't tell. The five flag sizes from prompt 1 were identical in all four harness runs.</td></tr>
<tr><td>Hertz Global Holdings, fiscal 2013 (SEC order, 2018)</td><td>Two chat runs and five harness runs, v2.22 to v2.26, plus the single prompt</td><td>Fail, narrowly, at v2.22 (the unchanged 18-month holding-period average was found but not carried into the report). Pass at v2.23 and every version since, on every run, including the chat app. The central item, a note that calls rate cuts "indicative of the residual values" in a year of a $48 million loss on car sales, was found from the filings alone in every run.</td></tr>
</table>
<p>Across the eleven runs, roughly 500 quotations and 900 recomputed figures: no fabricated number, no misquoted sentence, no quotation off its cited page, zero uses of banned words, nothing from after the cutoff. What changed between versions was judgment, not facts: which sentence reached the report, how items were ranked, which number a claim was tested against. The full record, every run and every change, is in <a href="https://github.com/adjdunn/forensic-method/blob/main/tools/TESTS.md">TESTS.md</a>; the scorecards sit beside each run.</p>
<p>What it has not done yet: it has run on two companies, one of them with an answer key. Three more are built and waiting for keys. No pass rate is claimed until that is done.</p>
""")
    parts.append("""
<h2 id="wrong">What it gets wrong</h2>
<p>Everything below happened in our runs. The fixes are in the prompts now; the pattern is worth knowing anyway.</p>
<ol>
<li><b>It uses the wrong number to check a claim.</b> A company said a deal was "not material". The model measured it against a bigger, unrelated figure and concluded the company was wrong. Every number was real; the comparison was not, and the output looked perfect. The prompts now make it say what a sentence claims before testing it, and test only with a number that matches.</li>
<li><b>It finds the right sentence and then doesn't use it.</b> The key sentence was on page 11 of both reports. The model's own search found it, then left it out of the answer. The prompts now make it list every match with its page before it tests anything, so a sentence found and not read is visible.</li>
<li><b>It rewrites the company's words.</b> The filing said "optimization of fleet holding periods". The model wrote "extended holding periods". Same direction, stronger claim. Always read the quotation against the document.</li>
<li><b>It ranks by whatever number is biggest.</b> Given three sizes for one finding it picked the largest, and put a weaker finding on top. The prompts now define what counts as the strongest evidence and make the report say which size an item ranks on.</li>
</ol>
<p>What did not go wrong, across hundreds of checked quotations and figures: it never invented a number and never misquoted a document. The failures were in judgment, not facts. Check the judgments.</p>
""")
    parts.append("""
<h2 id="next">What's next</h2>
<ul>
<li>Answer keys for Under Armour and Kraft Heinz, written from their SEC orders, so the scorecard covers four companies; then a Canadian IFRS filer, and a held-back company the method is never tuned on.</li>
<li>Two fictional companies with planted flags and an answer key, for teaching: one resolves benign in the notes, one does not.</li>
<li>Short videos of the prompts running. None yet.</li>
<li>The manual: a sourced reference for AI-assisted forensic accounting, public when its last chapter is rewritten for this prompt set.</li>
</ul>
""")
    parts.append(f"""
<footer>
<p>Built by Aaron Dunn, CFA, <a href="https://wiresift.com">WireSift Research</a>. First presented to CFA Society Vancouver, December 2026. Everything here is open source under the <a href="https://github.com/adjdunn/forensic-method/blob/main/LICENSE">MIT licence</a>: use it, adapt it, keep the notice; the companies named are test subjects, chosen because their filings and, for one, the SEC's findings are public. Items the method raises are things to investigate, not conclusions.</p>
<p>Prompts {VERSION}. Page built {today} from the repository by <code>docs/build.py</code>.</p>
</footer>""")
    return page("Forensic Method", "".join(parts))


def tidy_lists(text: str) -> str:
    """The model's markdown: nested bullets indented two spaces, and lists starting right under a bold title line.
    Python-Markdown wants four-space nesting and a blank line before a list."""
    out, prev = [], ""
    for line in text.split("\n"):
        stripped = line.lstrip(" ")
        indent = len(line) - len(stripped)
        is_item = stripped.startswith(("- ", "* ")) or re.match(r"\d+\. ", stripped) is not None
        prev_stripped = prev.lstrip(" ")
        prev_item = prev_stripped.startswith(("- ", "* ")) or re.match(r"\d+\. ", prev_stripped) is not None
        if indent and (is_item or prev_item or prev.startswith(" ")):
            line = "    " * ((indent + 1) // 2) + stripped  # two spaces become four, four become eight
        if is_item and not indent and prev.strip() and not prev_item and not prev.startswith(" "):
            out.append("")  # a blank line before a list that starts under a title
        out.append(line)
        prev = line
    return "\n".join(out)


def build_output(slug: str, title: str, run: str, notice: str) -> str:
    run_dir = ROOT / run
    record = json.loads((run_dir / "run.json").read_text(encoding="utf-8"))
    nav = '<nav class="top"><a href="../index.html">Forensic Method</a> &rsaquo; What it produces</nav>'
    head = f"""<h1>{html.escape(title)}</h1>
<p class="meta">Prompts {record['prompts_version']}, run through the harness on {', '.join(record.get('models') or ['the model'])} on {record['started'][:10]}, with these files: {', '.join(record['files'])}. Every quotation and figure below was checked against the filings afterwards; the checker's reports are in the repository beside the replies. Nothing here is edited, except that a dash the model drew as an em-dash is shown as a hyphen.</p>
<p>{html.escape(notice)}</p>
<p>Contents: """ + " &middot; ".join(f'<a href="#{f[:-3]}">{html.escape(label)}</a>' for f, label in REPLY_FILES) + "</p>"
    body = [head]
    for f, label in REPLY_FILES:
        text = (run_dir / f).read_text(encoding="utf-8").replace("—", "-")  # the package carries no em-dashes; a blank cell the model drew as one becomes a hyphen
        text = tidy_lists(text)
        body.append(f'<section class="reply" id="{f[:-3]}"><h2>{html.escape(label)}</h2>{md(text)}</section>')
    body.append(f'<footer><p><a href="../index.html">Back to Forensic Method</a>. Run folder in the repository: <code>{run}</code>.</p></footer>')
    return page(f"{title}: Forensic Method sample output", "".join(body), nav)


def main():
    (DOCS / "outputs").mkdir(parents=True, exist_ok=True)
    (DOCS / "index.html").write_text(build_index(), encoding="utf-8")
    for slug, title, run, notice in SAMPLES:
        (DOCS / "outputs" / f"{slug}.html").write_text(build_output(slug, title, run, notice), encoding="utf-8")
    (DOCS / ".nojekyll").write_text("", encoding="utf-8")
    print("built docs/index.html and", ", ".join(f"docs/outputs/{s}.html" for s, *_ in SAMPLES))


if __name__ == "__main__":
    main()
