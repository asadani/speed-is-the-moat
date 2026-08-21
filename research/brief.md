# Research brief: Is inference speed the next durable differentiator for LLM systems?

## Question

Now that per-token cost is broadly understood and largely commoditised, does
inference speed (latency and throughput) constitute a *durable* differentiator --
a moat -- for LLM systems and the organisations that build on them, or is it a
lead that erodes as fast as it is won?

## Decision this feeds

Whether an engineering or AI leader should treat inference speed as a
**long-horizon strategic axis** -- something with an owner, a budget line, an SLO,
and a procurement criterion -- rather than as a per-project tuning exercise
handled after cost and quality are settled.

Concretely, the answer changes:
- whether speed gets its own line in AI/FinOps governance alongside $/token
- whether vendor and inference-framework selection is re-run on a schedule
- whether "same budget, same task, 1 day vs 1 month" is a real, sizeable effect
  worth organising around, or an anecdote

## Sub-questions

1. **Has token cost actually commoditised?** What do published price histories and
   price-per-unit-capability trends show for frontier and open-weight models, and
   how converged is pricing across vendors for comparable capability? (Tests the
   brief's own premise. If cost is *not* settled, the "next axis" framing is
   premature.)

2. **How large is the speed spread today?** For comparable models and tasks, what
   is the measured variation in latency (TTFT, end-to-end) and throughput
   (output tokens/sec, requests/sec at fixed concurrency) across serving vendors
   and inference frameworks? A moat requires a gap; this measures the gap.

3. **Does a speed lead persist or erode?** What is the observed diffusion rate of
   inference performance gains -- speculative decoding, continuous batching,
   paged/quantised KV cache, disaggregated prefill/decode, new silicon -- from
   first appearance to commodity availability in open frameworks? And where a lead
   has persisted, what structural feature (custom silicon, vertical integration,
   capacity contracts, workload-specific tuning) held it there?

4. **Does speed convert into outcomes?** What evidence links latency or throughput
   to things a business measures -- task completion, agentic loop viability,
   user abandonment, throughput-bound batch job wall-clock time? Specifically:
   is the "1 day vs 1 month for the same budget and task" magnitude supportable?

5. **Are organisations actually treating speed as a strategic axis?** What does
   published practice show about how AI/FinOps governance, SLOs, and procurement
   criteria handle latency and throughput versus cost -- i.e. is the brief's
   claim that "not many leaders add speed as a long-horizon axis" true?

## Out of scope

- **Organisational execution speed.** "Ship fast as a moat" is a different thesis
  about company velocity. Named explicitly because the phrase "speed is the moat"
  is commonly used that way; this project is about *inference* speed only.
- **Training and fine-tuning speed.** Time-to-train, cluster efficiency, and
  training-cost curves are a separate economics.
- **Model quality rankings.** Accuracy/capability leaderboards are covered only
  where the quality-speed trade-off is inseparable from the speed claim (e.g.
  quantisation, reasoning-token budgets, draft models).
- **GPU supply chain and hardware procurement economics** as a topic in itself.
  Custom silicon appears only as a candidate structural moat under SQ3.
- **Non-LLM ML inference** (recsys, vision, classical serving).
- **A vendor recommendation for a specific stack.** No workload, region, model, or
  concurrency profile has been specified, so no "pick X" answer is in scope.

## What a good answer looks like

A verdict on the thesis with four things attached:

1. A **measured spread** in latency and throughput across providers/frameworks for
   at least one comparable model-and-task pair, from a benchmark that publishes
   its method, hardware, version, and date.
2. An **erosion rate**: dated evidence of at least one specific optimisation going
   from proprietary/novel to commodity, with the interval.
3. A **transfer function**: evidence connecting a speed delta to an outcome delta,
   with the workload class named (interactive vs agentic vs batch), since the
   "1 day vs 1 month" claim is a throughput claim and only holds for some classes.
4. An **adoption reading**: whether speed is governed or improvised in practice.

### What would change my mind

The thesis **fails** if any of these hold:
- the measured spread across serious providers for comparable output is small
  (say, within ~2x on both TTFT and tokens/sec) -- no gap, no moat;
- leads demonstrably close within a quarter or two with no structural barrier, so
  speed is a *tempo* advantage rather than a moat;
- the speed-to-outcome link only holds for interactive UX, where it is a
  well-known product concern rather than a novel strategic axis;
- governance evidence shows leaders already track latency/throughput as first-class,
  making the "few leaders do this" premise false.

The thesis **strengthens** if the spread is large and persistent, if it is
*workload-dependent* in a way that rewards sustained internal expertise, and if
the erosion evidence shows the frontier moving faster than typical procurement
re-evaluation cycles -- which would make speed a moat made of *attention*, not
technology.

## Lens

`technical` (primary), with a documented `market` overlay -- see `lens.yaml`.

T1 means the artifact itself: a benchmark harness and its published numbers, a
provider's live price/rate-limit page, a framework's release notes and source, an
API response. T2 means first-party engineering documentation and independent
reproducible benchmarks that publish method, hardware, model version, and date.
T4 explicitly includes vendor speed claims, which are dense in this topic.

Recency window: **2 years**, tightened to **12 months** for any throughput or
latency figure. A tokens/sec number from an inference stack two minor versions
back is describing a different program.

## Known traps

From the technical lens:
- A vendor benchmark is strong evidence of what the vendor claims, weak evidence
  of what you will see. This topic is unusually dense with them.
- Benchmarks run on the vendor's preferred workload, hardware, batch size, or
  tuning.
- Stale comparison tables whose numbers were true for a version nobody runs.
- Reading a roadmap aspiration as a shipped feature.
- "It scales" with no number attached.

From the market lens:
- A figure every source repeats and no source computed.
- Comparing numbers built on different definitions -- critical here, since
  "tokens/sec" means output-only or total, single-stream or aggregate, and
  "latency" means TTFT or end-to-end, depending on who is publishing.

Specific to this question:
- **Speed and cost are not independent.** Faster serving is often *how* cost falls;
  treating them as sequential axes may be the brief's own weak point, and the
  research must test rather than assume it.
- **Reasoning models changed the unit.** Output-token volume per task rose sharply,
  so tokens/sec and time-to-answer decoupled. A source predating that shift is
  measuring a different world.
- **Confirmation risk:** the user holds the thesis. Disconfirming search is
  mandatory here, not decorative.
