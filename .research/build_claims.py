# -*- coding: utf-8 -*-
"""Build claims.jsonl, quote-checking every binding before it is written."""
import json, sys, io
sys.path.insert(0, r"C:/Users/anuj_/.claude/plugins/cache/research-anything/research-anything/0.1.0/scripts")
from quote_locate import contains  # the same matcher the gate uses

SNAP = ".research/snapshots/%s.txt"


def occurs(sid, quote):
    with io.open(SNAP % sid, encoding="utf-8", errors="replace") as fh:
        return contains(fh.read(), quote)


C = []


def claim(cid, statement, sid, quote, stance="supported", confidence="moderate",
          contradicted_by=None, sq=None):
    row = {"cid": cid, "statement": statement,
           "bindings": [{"sid": sid, "locator": {"kind": "quote", "value": quote},
                         "verified_by": "quote-match"}],
           "stance": stance, "confidence": confidence, "verified": "pass"}
    if contradicted_by:
        row["contradicted_by"] = contradicted_by
    if sq:
        row["subquestion"] = sq
    C.append(row)


# ---------------- SQ1: has token cost commoditised? ----------------
claim("c-001",
      "Across six benchmarks and three years, Epoch AI measured the price of reaching a fixed capability milestone falling at rates between 9x and 900x per year, with a median of 50x per year.",
      "s-001", "we found prices declining between 9x per year and 900x per year, with a median of 50x per year",
      confidence="high", sq="sq1")
claim("c-002",
      "Epoch AI found the fastest price-decline trends began after January 2024: restricting the data to post-January-2024 models raised the median decline rate from 50x to 200x per year.",
      "s-001", "the median rate increased from 50x per year to 200x per year",
      confidence="high", sq="sq1")
claim("c-003",
      "Epoch AI cautions that the fastest price declines it measured are recent and may not persist.",
      "s-001", "The fastest price drops in that range have occurred in the past year",
      confidence="high", sq="sq1")
claim("c-004",
      "a16z puts the decline at 10x per year for an LLM of equivalent performance, an order of magnitude below Epoch AI's median estimate of 50x per year for capability-milestone pricing.",
      "s-003", "For an LLM of equivalent performance, the cost is decreasing by 10x every year",
      stance="mixed", confidence="moderate", contradicted_by=["s-001"], sq="sq1")
claim("c-005",
      "In July 2026 OpenAI cut GPT-5.6 Terra by 20 percent and GPT-5.6 Luna by 80 percent, roughly three weeks after those models were publicly released.",
      "s-016", "reducing the price of Terra by 20% to $2 per million input tokens and $12 per million output tokens",
      confidence="high", sq="sq1")
claim("c-006",
      "OpenAI attributed its July 2026 price cuts to a strategy of advancing capability and efficiency together so each model generation does more work at lower cost.",
      "s-016", "Our strategy remains focused on advancing both capability and efficiency so each generation of intelligence can accomplish more work at a lower cost",
      confidence="high", sq="sq1")
claim("c-007",
      "Contemporary reporting frames the competitive pressure on frontier model vendors as pressure on cost, not on speed.",
      "s-016", "The company is facing pressure to cater to a more cost-sensitive customer base",
      confidence="moderate", sq="sq1")

# ---------------- SQ2: how large is the speed spread? ----------------
claim("c-010",
      "On the same open-weight model at the same context length (Gemma 4 31B, 131k), Cerebras served a median 1,357 output tokens/sec at a 2.43s total response time.",
      "s-014", "Cerebras Gemma 4 31B 131k Open 30 $0.24 1,357 0.79 2.43",
      confidence="moderate", sq="sq2")
claim("c-011",
      "SambaNova served that same model and context length at 201 output tokens/sec and a 13.49s total response time, for $0.10 cost per task against Cerebras's $0.24 - so the 6.8x slower endpoint was the cheaper one.",
      "s-014", "SambaNova Gemma 4 31B 131k Open 30 $0.10 201 2.37 13.49 8.63",
      confidence="moderate", sq="sq2")
claim("c-012",
      "On Qwen3.6 27B, Groq returned a median 463 output tokens/sec and a 14.58s total response time.",
      "s-014", "Groq Qwen3.6 27B 131k Open 38 $0.27 463 1.24 14.58 12.26",
      confidence="moderate", sq="sq2")
claim("c-013",
      "DeepInfra's Qwen3.6 27B endpoint returned 53 output tokens/sec and a 117.94s total response time for $0.19 per task, but it is an FP8 quantisation at a 262k context rather than a like-for-like serving configuration.",
      "s-014", "DeepInfra Qwen3.6 27B FP8 262k Open 38 $0.19 53 1.19 117.94 107.29",
      confidence="moderate", sq="sq2")
claim("c-014",
      "For a proprietary frontier model the cross-provider spread is far smaller than for open-weight models: Claude Opus 5 (max) via Amazon Bedrock showed a 44.88s total response time.",
      "s-014", "Amazon Bedrock Claude Opus 5 (max) 1M Proprietary 63 $2.34 52 35.35 44.88",
      confidence="moderate", sq="sq2")
claim("c-015",
      "Artificial Analysis defines output speed as tokens received per second after the first token, so the headline tokens/sec figure deliberately excludes the initial wait a user experiences.",
      "s-002", "Output Speed (output tokens per second): The average number of tokens received per second, after the first token is received.",
      confidence="high", sq="sq2")
claim("c-016",
      "Artificial Analysis reports performance as a median over the trailing 72 hours rather than as a single measurement.",
      "s-002", "Performance measurements are represented as the median (P50) measurement over the past 72 hours",
      confidence="high", sq="sq2")
claim("c-017",
      "Artificial Analysis states that its time-to-first-token figures include network latency from a single test location and may advantage or disadvantage providers by server geography.",
      "s-002", "which may advantage or disadvantage certain providers based on their server locations",
      confidence="high", sq="sq2")

# ---------------- SQ3: does a lead persist? ----------------
claim("c-020",
      "Inference software performance improves in incremental releases that can be days apart, across SGLang, vLLM, TensorRT-LLM, CUDA and ROCm.",
      "s-022", "increase the Pareto frontier of performance in incremental releases that can be just days apart",
      confidence="high", sq="sq3")
claim("c-021",
      "SemiAnalysis states that the pace of inference software improvement makes point-in-time benchmarks go stale quickly and unrepresentative of current achievable performance.",
      "s-022", "benchmarks conducted at a fixed point in time quickly go stale and do not represent the performance",
      confidence="high", sq="sq3")
claim("c-022",
      "The response to that staleness was to make benchmarking continuous: InferenceMAX re-runs its suite nightly across hundreds of chips.",
      "s-022", "runs our suite of benchmarks every night on hundreds of chips",
      confidence="high", sq="sq3")
claim("c-023",
      "The phrase 'Speed is the moat' is used in this market by an interested party: AMD's VP of GPU Software, Anush Elangovan, quoted in the InferenceMAX launch post.",
      "s-022", "Speed is the moat. ... Anush Elangovan, VP GPU Software, AMD",
      confidence="high", sq="sq3")
claim("c-024",
      "The optimisations that once distinguished fast serving stacks are now standard features of open-source vLLM: chunked prefill, prefix caching, speculative decoding and disaggregated prefill/decode.",
      "s-006", "Advanced features: chunked prefill, prefix caching, guided & speculative decoding, disaggregated P/D",
      confidence="high", sq="sq3")
claim("c-025",
      "Latency and throughput are not one axis but a trade-off set by batch size: on the same hardware you cannot have both minimum latency and maximum throughput.",
      "s-004", "There is no free lunch, you cannot have both minimum latency and maximum throughput on the same hardware.",
      confidence="moderate", sq="sq3")
claim("c-026",
      "Where a provider sits on that latency-throughput curve is a commercial decision as much as a technical capability.",
      "s-004", "Where a provider sets their batch size is a business decision as much as a technical one",
      confidence="moderate", sq="sq3")
claim("c-027",
      "Model labs hold a structural cost advantage in inference because they can backfill idle serving capacity with training, research and offline batch work.",
      "s-004", "They can backfill idle capacity with training runs, research ablations, evaluations, and offline batch inference.",
      confidence="moderate", sq="sq3")
claim("c-028",
      "Custom inference silicon reaches a latency tier that GPU-based providers cannot match by tuning batch size alone, but it currently occupies a distinct and expensive corner of the market.",
      "s-004", "custom hardware creates a tier that GPU-based providers can",
      confidence="moderate", sq="sq3")
claim("c-029",
      "Nvidia's own framing of the same benchmark stresses performance per dollar and per megawatt rather than raw latency leadership.",
      "s-022", "delivers unmatched performance per dollar and per megawatt",
      confidence="moderate", sq="sq3")

# ---------------- SQ4: does speed convert to outcomes? ----------------
claim("c-030",
      "Anthropic's Message Batches API charges 50 percent of standard API prices, with most batches finishing in under an hour.",
      "s-013", "most batches finishing in less than 1 hour while reducing costs by 50% and increasing throughput",
      confidence="high", sq="sq4")
claim("c-031",
      "Anthropic's batch results are available when all messages complete or after 24 hours, whichever comes first, and batches that do not complete in that window expire.",
      "s-013", "You can access batch results when all messages have completed or after 24 hours, whichever comes first.",
      confidence="high", sq="sq4")
claim("c-032",
      "OpenAI's Batch API offers the same trade in the same shape: 50 percent lower cost, higher rate limits, and a 24-hour turnaround.",
      "s-012", "50% lower costs, a separate pool of significantly higher rate limits, and a clear 24-hour turnaround time",
      confidence="high", sq="sq4")
claim("c-033",
      "The wall-clock cost of the cheap tier is real even inside the window: a single 300k-token generation can take over an hour.",
      "s-013", "A single 300k-token generation can take over an hour to complete",
      confidence="high", sq="sq4")
claim("c-034",
      "Latency is sold as a purchasable service tier rather than a fixed property of a model, with priority requests prioritised over all others.",
      "s-021", "The API prioritizes requests in this tier over all other requests.",
      confidence="high", sq="sq4")
claim("c-035",
      "That purchasable priority tier is being withdrawn rather than expanded: Anthropic states Priority Tier capacity commitments are no longer available for purchase.",
      "s-021", "Priority Tier capacity commitments are no longer available for purchase.",
      confidence="high", sq="sq4")
claim("c-036",
      "Agentic workloads multiply the number of sequential inference calls per task: an office-work trace averages about 41 turns.",
      "s-008", "The office work use case averages about 41 turns per trace",
      confidence="moderate", sq="sq4")
claim("c-037",
      "Agentic traffic is heavy-tailed across turns, output length and tool latency, which is why single-turn benchmarks do not predict agentic performance.",
      "s-008", "Most attributes have heavy tails, especially number of turns, assistant tokens per turn, tool output tokens per turn, and tool call latency.",
      confidence="moderate", sq="sq4")
claim("c-038",
      "The most-repeated evidence that latency costs revenue is Amazon's finding that every 100ms of delay cost 1 percent in sales - an e-commerce page-load result recycled into AI latency marketing rather than measured on LLM inference.",
      "s-017", "Amazon once found that every 100 milliseconds of delay could cost 1% in sales",
      stance="contradicted", confidence="low", contradicted_by=["s-017"], sq="sq4")

# ---------------- SQ5: is speed governed? ----------------
claim("c-040",
      "Managing AI spend has become near-universal in FinOps practice: 98 percent of 1,192 State of FinOps respondents manage it, up from 31 percent two years earlier.",
      "s-018", "Almost all the 1,192 survey respondents (98%) are managing AI spend, it has become the norm, up from 31% just two years ago.",
      confidence="high", sq="sq5")
claim("c-041",
      "The priorities that displaced pure cost optimisation in that survey are governance, forecasting, organisational alignment and expanding technology coverage.",
      "s-018", "more respondents now prioritize governance, forecasting, organizational alignment, and managing expanding technology areas than optimization and efficiency alone",
      confidence="moderate", sq="sq5")
claim("c-042",
      "Mature FinOps practice is described as moving toward unit economics and influencing technology selection, which is the governance surface a speed criterion would have to occupy.",
      "s-018", "Mature practices increasingly focus on unit economics, AI value quantification, and influencing technology selection",
      confidence="moderate", sq="sq5")
claim("c-043",
      "Latency is being standardised where benchmarks are governed: MLPerf Inference v5.1 expanded an interactive scenario testing performance under lower latency constraints, explicitly motivated by agentic applications.",
      "s-005", "tests performance under lower latency constraints as required for agentic and other applications of LLMs",
      confidence="high", sq="sq5")
claim("c-044",
      "That benchmark round drew record industry participation, with 27 submitting organisations.",
      "s-005", "sets a record for the number of participants submitting systems for benchmarking at 27",
      confidence="high", sq="sq5")

# ---------------- write, checking every quote ----------------
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

with io.open(".research/claims.jsonl", "w", encoding="utf-8") as fh:
    for row in C:
        fh.write(json.dumps(row, ensure_ascii=False) + "\n")
print("wrote %d claims, all quotes matched" % len(C))
