# -*- coding: utf-8 -*-
"""Claims added in the gap-fixing pass. Same quote discipline as the first pass."""
import json, sys, io
sys.path.insert(0, r"C:/Users/anuj_/.claude/plugins/cache/research-anything/research-anything/0.1.0/scripts")
from quote_locate import contains

SNAP = ".research/snapshots/%s.txt"


def occurs(sid, quote):
    with io.open(SNAP % sid, encoding="utf-8", errors="replace") as fh:
        return contains(fh.read(), quote)


C = []


def claim(cid, statement, bindings, stance="supported", confidence="moderate",
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


# ===== GAP 1: no independent study linking LLM latency to an outcome =====
claim("c-050",
      "A controlled experiment published at CHI 2026 tested LLM response latency directly, varying time-to-first-token across 2, 9 and 20 seconds over two knowledge-task types with 240 participants.",
      [("s-024", "between-subjects experiment with 240 participants")],
      confidence="high", sq="sq4")
claim("c-051",
      "In that experiment, user interaction behaviour was robust to latency: prompting, copying and refreshing rates did not shift across the 2s, 9s and 20s conditions, while task type did drive behaviour.",
      [("s-024", "user interaction behaviors were robust to latency")],
      confidence="high", sq="sq4")
claim("c-052",
      "The same experiment found the effect of speed ran opposite to the usual assumption: participants served in 2 seconds rated outputs as less thoughtful and less useful than participants who waited 9 to 20 seconds.",
      [("s-024", "participants who experienced 2-second latencies rated the LLM's outputs less thoughtful and useful")],
      stance="mixed", confidence="high", contradicted_by=["s-017"], sq="sq4")
claim("c-053",
      "The authors conclude that latency is not simply a cost to be minimised but a tunable design variable.",
      [("s-024", "latency is not simply a cost to reduce but a tunable design variable")],
      confidence="high", sq="sq4")

# ===== GAP 2: SQ5 unresolved - is speed contractually governed? =====
claim("c-060",
      "Latency is a contractual term, not only an engineering metric: Microsoft's deployment-type table carries a Latency Service Level Agreement column, and Priority processing carries a defined latency target per model.",
      [("s-027", "Priority processing Pay per token (priority tier rate) Defined latency target per model")],
      confidence="high", sq="sq5")
claim("c-061",
      "That same table shows the latency guarantee is what buyers give up on the cheap tiers: Standard deployments carry no latency SLA at all.",
      [("s-027", "Standard Pay per token None Balanced workloads")],
      confidence="high", sq="sq5")

# ===== GAP 3: no measured diffusion interval =====
claim("c-070",
      "A measured diffusion interval exists after all: between December 2025 and January 2026, AMD's inference software stack improved by up to 2x in performance on the same hardware.",
      [("s-028", "From December 2025 to January 2026, AMD's software was improved up to 2x in performance.")],
      confidence="moderate", sq="sq3")
claim("c-071",
      "Over a slightly longer window the same benchmark recorded AMD nearly doubling throughput at equal interactivity in under two months, on unchanged silicon.",
      [("s-028", "AMD has almost doubled the amount of throughput in the span of less than 2 months")],
      confidence="moderate", sq="sq3")
claim("c-072",
      "A second, independently-run benchmark reaches the same structural finding as the first: the fundamental trade-off in LLM inference is throughput against latency, measured as a curve rather than a single number.",
      [("s-028", "The fundamental tradeoff with LLM inference is throughput versus latency.")],
      confidence="high", sq="sq3")

# ===== GAP 4: no first-party OpenAI pricing =====
claim("c-080",
      "OpenAI's own published price list confirms the reported July 2026 figures: gpt-5.6-luna at $0.20 per million input tokens and $1.20 per million output tokens.",
      [("s-032", "gpt-5.6-luna | $0.20 | $0.02 | $0.25 | $1.20")],
      confidence="high", sq="sq1")

# ===== revised conclusions =====
claim("c-110",
      "The interactive-latency case is now evidenced, and the evidence cuts against the thesis rather than for it: within the 2-20 second band, faster responses changed no user behaviour and were judged lower quality.",
      [("s-024", "user interaction behaviors were robust to latency"),
       ("s-024", "participants who experienced 2-second latencies rated the LLM's outputs less thoughtful and useful")],
      stance="mixed", confidence="high", contradicted_by=["s-017"], sq="sq4")
claim("c-111",
      "The claim that leaders do not treat speed as a governed axis is false at the platform layer: latency is already sold as a per-model contractual target, and the absence of that guarantee is what distinguishes the cheaper tiers.",
      [("s-027", "Priority processing Pay per token (priority tier rate) Defined latency target per model"),
       ("s-027", "Standard Pay per token None Balanced workloads")],
      confidence="high", sq="sq5")
claim("c-112",
      "The erosion of a speed lead can now be given a number rather than a characterisation: roughly a doubling of throughput from software alone within one to two months, on fixed hardware.",
      [("s-028", "From December 2025 to January 2026, AMD's software was improved up to 2x in performance."),
       ("s-028", "AMD has almost doubled the amount of throughput in the span of less than 2 months")],
      confidence="moderate", sq="sq3")

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
print("appended %d gap-fix claims, all quotes matched" % len(C))
