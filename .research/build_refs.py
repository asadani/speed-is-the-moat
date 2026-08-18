# -*- coding: utf-8 -*-
"""Generate the report's References section from the ledgers, so it cannot drift."""
import json, io, re, datetime

MARKER_RE = re.compile(r"\[\^(c-\d{3,})\]")

sources = {}
for line in io.open(".research/sources.jsonl", encoding="utf-8"):
    if line.strip():
        r = json.loads(line)
        sources[r["sid"]] = r

claims = {}
for line in io.open(".research/claims.jsonl", encoding="utf-8"):
    if line.strip():
        r = json.loads(line)
        claims[r["cid"]] = r

report = io.open(".research/report.md", encoding="utf-8").read()
body = report.split("\n## References")[0].rstrip()

cited = []
for cid in MARKER_RE.findall(body):
    if cid not in cited:
        cited.append(cid)

missing = [c for c in cited if c not in claims]
if missing:
    raise SystemExit("markers with no ledger row: %s" % ", ".join(missing))

today = datetime.date.today().isoformat()
out = [body, "", "## References", ""]
for cid in sorted(cited):
    cl = claims[cid]
    out.append("[^%s]: %s" % (cid, cl["statement"]))
    for b in cl["bindings"]:
        s = sources[b["sid"]]
        pub = s.get("publisher") or "unknown publisher"
        date = s.get("published") or "n.d."
        url = s.get("url", "")
        accessed = s.get("accessed") or s.get("captured") or today
        if accessed and len(accessed) > 10:
            accessed = accessed[:10]
        loc = b["locator"]["value"]
        if len(loc) > 60:
            loc = loc[:57] + "..."
        out.append('    - %s "%s" - *%s*, %s, %s. <%s> (accessed %s) [%s]'
                   % (b["sid"], loc, s.get("title", ""), pub, date, url, accessed, s["tier"]))
    flags = []
    if cl["stance"] != "supported":
        flags.append("stance: %s" % cl["stance"])
    flags.append("confidence: %s" % cl["confidence"])
    if cl.get("contradicted_by"):
        flags.append("contradicted by %s" % ", ".join(cl["contradicted_by"]))
    out.append("    - _(%s)_" % "; ".join(flags))
    out.append("")

io.open(".research/report.md", "w", encoding="utf-8").write("\n".join(out) + "\n")
print("references generated for %d cited claims (of %d in ledger)" % (len(cited), len(claims)))
