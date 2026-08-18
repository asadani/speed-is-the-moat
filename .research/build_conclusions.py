# -*- coding: utf-8 -*-
"""Append synthesised conclusions to claims.jsonl. A conclusion is a claim."""
import json, sys, io
sys.path.insert(0, r"C:/Users/anuj_/.claude/plugins/cache/research-anything/research-anything/0.1.0/scripts")
from quote_locate import contains

SNAP = ".research/snapshots/%s.txt"


def occurs(sid, quote):
    with io.open(SNAP % sid, encoding="utf-8", errors="replace") as fh:
        return contains(fh.read(), quote)


C = []


def conclusion(cid, statement, bindings, stance="supported", confidence="moderate",
               contradicted_by=None, sq=None):
    row = {"cid": cid, "statement": statement,
           "bindings": [{"sid": s, "locator": {"kind": "quote", "value": q},
                         "verified_by": "quote-match"} for s, q in bindings],
           "stance": stance, "confidence": confidence, "verified": "pass"}
    if contradicted_by:
        row["contradicted_by"] = contradicted_by
    if sq:
        row["subquestion"] = sq
    C.append(row)


conclusion("c-100",
           "The premise that cost is a settled axis does not hold: per-token price is still where frontier vendors compete publicly, with cuts of 20 and 80 percent landing three weeks after a model launch under pressure from cost-sensitive buyers.",
           [("s-016", "The company is facing pressure to cater to a more cost-sensitive customer base"),
            ("s-016", "reducing the price of Terra by 20% to $2 per million input tokens and $12 per million output tokens")],
           confidence="moderate", sq="sq1")

conclusion("c-101",
           "For an open-weight model that many providers serve, the cross-provider speed spread is roughly 5x to 8x on identical weights - far above the 2x threshold below which a speed advantage would be strategically uninteresting.",
           [("s-014", "Cerebras Gemma 4 31B 131k Open 30 $0.24 1,357 0.79 2.43"),
            ("s-014", "SambaNova Gemma 4 31B 131k Open 30 $0.10 201 2.37 13.49 8.63")],
           confidence="moderate", sq="sq2")

conclusion("c-102",
           "For a proprietary frontier model the same spread nearly disappears - about 1.4x in end-to-end response time across three resellers - so the size of any available speed advantage depends on whether the buyer can choose who serves the weights.",
           [("s-014", "Amazon Bedrock Claude Opus 5 (max) 1M Proprietary 63 $2.34 52 35.35 44.88")],
           confidence="low", sq="sq2")

conclusion("c-103",
           "A speed lead built in software is not durable: the techniques that once distinguished a fast stack are now standard open-source features, and the frontier moves in releases days apart, which is faster than any procurement or re-evaluation cycle.",
           [("s-006", "Advanced features: chunked prefill, prefix caching, guided & speculative decoding, disaggregated P/D"),
            ("s-022", "increase the Pareto frontier of performance in incremental releases that can be just days apart")],
           confidence="high", sq="sq3")

conclusion("c-104",
           "What persists is not speed but position: latency and throughput are opposite ends of one batch-size curve, and where a provider sits on it is a commercial decision rather than a capability an incumbent can be locked out of.",
           [("s-004", "There is no free lunch, you cannot have both minimum latency and maximum throughput on the same hardware."),
            ("s-004", "Where a provider sets their batch size is a business decision as much as a technical one")],
           confidence="moderate", sq="sq3")

conclusion("c-105",
           "The 'same budget, very different wall-clock' effect is real and documented, but as a purchasable tier rather than an earned advantage: identical work runs at half price if the buyer accepts a 24-hour window instead of an interactive response.",
           [("s-013", "most batches finishing in less than 1 hour while reducing costs by 50% and increasing throughput"),
            ("s-012", "50% lower costs, a separate pool of significantly higher rate limits, and a clear 24-hour turnaround time")],
           confidence="high", sq="sq4")

conclusion("c-106",
           "The business case for interactive speed rests on weaker evidence than the case for throughput: the most-cited number is an e-commerce page-load result recycled into AI latency marketing, not a measurement of LLM latency.",
           [("s-017", "Amazon once found that every 100 milliseconds of delay could cost 1% in sales")],
           stance="contradicted", confidence="low", contradicted_by=["s-017"], sq="sq4")

conclusion("c-107",
           "Speed is being institutionalised at the benchmark layer even if not yet at the governance layer: MLPerf added latency-constrained interactive scenarios explicitly for agentic applications, drawing record participation.",
           [("s-005", "tests performance under lower latency constraints as required for agentic and other applications of LLMs"),
            ("s-005", "sets a record for the number of participants submitting systems for benchmarking at 27")],
           confidence="moderate", sq="sq5")

conclusion("c-108",
           "Agentic workloads are the mechanism that converts per-token speed into wall-clock outcome, because they multiply sequential model calls per task - tens of turns typically, up to 200 - with heavy tails at every step.",
           [("s-008", "The office work use case averages about 41 turns per trace"),
            ("s-008", "Most attributes have heavy tails, especially number of turns, assistant tokens per turn, tool output tokens per turn, and tool call latency.")],
           confidence="moderate", sq="sq4")

conclusion("c-109",
           "'Speed is the moat' is, in its most prominent published use, a hardware vendor's marketing line rather than an analytic finding - which is a reason to test the claim, not to dismiss it.",
           [("s-022", "Speed is the moat. ... Anush Elangovan, VP GPU Software, AMD")],
           confidence="high", sq="sq3")

bad = []
for row in C:
    for b in row["bindings"]:
        if not occurs(b["sid"], b["locator"]["value"]):
            bad.append((row["cid"], b["sid"], b["locator"]["value"][:70]))

if bad:
    print("QUOTE CHECK FAILED for %d binding(s):" % len(bad))
    for cid, sid, q in bad:
        print("  %s -> %s : %s" % (cid, sid, q))
    sys.exit(1)

with io.open(".research/claims.jsonl", "a", encoding="utf-8") as fh:
    for row in C:
        fh.write(json.dumps(row, ensure_ascii=False) + "\n")
print("appended %d conclusions, all quotes matched" % len(C))
