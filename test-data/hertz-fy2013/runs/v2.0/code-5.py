# Turn 5: the report adds no new numbers. This script checks that:
# (1) every number in reply-5.md already appears in replies 1 to 4 (page references, years
#     and list numbering aside);  (2) every quotation is exact and on the cited page;
# (3) word counts for all five replies.
import os, re
from common import *

def numbers(s):
    s = s.replace("−", "-")
    return set(re.findall(r"\d[\d,]*\.?\d*", s))

r5 = open(os.path.join(HERE, "reply-5.md"), encoding="utf-8").read()
earlier = "".join(open(os.path.join(HERE, f"reply-{i}.md"), encoding="utf-8").read() for i in (1, 2, 3, 4))

# strip page references, document names, list numbering and years before collecting numbers
body = re.sub(r"\(?\bpp?\. [\d, and to]+", " ", r5)
body = re.sub(r"FY20\d\d|\b20(09|1[0-4])\b|Tables? [\d, and]+|Note \d+|Item \d+|Schedule II", " ", body)
body = re.sub(r"(?m)^\*\*\d\. ", "** ", body)
body = re.sub(r"\b31 December\b|\bitem \d\b", " ", body)
new = sorted(n for n in numbers(body) if n.rstrip(".") not in {x.rstrip(".") for x in numbers(earlier)})
print("numbers in reply 5 not found in replies 1 to 4:", new or "none")

n, ok, fails, loose = check_quotes("reply-5.md")
for i in range(1, 6):
    print(f"reply-{i}.md words: {wc(f'reply-{i}.md')}")
