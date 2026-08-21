# Speed Is the Moat — the condensed argument

**Question.** Now that per-token cost is understood, is inference speed the next
durable differentiator for LLM systems?

**Answer.** No. The dispersion in speed is large and persistent, but a lead
inside it has a measured half-life of one to two months, latency is already sold
as a contractual tier rather than won, and the one controlled experiment on
interactive latency found faster responses changed no behaviour and were judged
*worse*. What is left worth organising around is placement, not pace.

---

## The premise needs one correction first

Cost is *understood* — 98% of 1,192 State of FinOps respondents manage AI spend,
up from 31% two years earlier. Cost is not *settled*: it is still where frontier
vendors compete in public. OpenAI cut GPT-5.6 Terra 20% and Luna 80% in July
2026, three weeks after launch, under reported pressure from cost-sensitive
buyers.

More importantly, **speed and cost are not sequential axes**. They are two
readings of one batch-size curve: on fixed hardware you cannot have both minimum
latency and maximum throughput, and where a provider sits between them is a
commercial decision as much as a technical one.

## The numbers

| Finding | Figure |
|---|---|
| Cross-provider spread, same open weights (Gemma 4 31B, 131k) | **1,357 vs 201** tok/s — 6.8x |
| Same pair, wall clock | **2.43s vs 13.49s** — 5.6x |
| Cross-provider spread, proprietary model (Claude Opus 5) | **44.88s / 54.58s / 61.68s** — 1.4x |
| Half-life of a software speed lead | **up to 2x in one month**, on unchanged silicon |
| Cost of accepting a 24-hour window instead of interactive | **50% of standard price** |
| Latency effect on user behaviour, 2s vs 9s vs 20s TTFT | **no behavioural difference** |
| Latency effect on perceived quality | **2s rated *less* thoughtful and useful than 9–20s** |
| Agentic turns per task | ~41 (office work), up to **200** (code QA) |
| Price decline for fixed capability | 9x–900x/yr, median 50x; 200x/yr post-2024 |

## Why "moat" is the wrong word

The optimisations that once separated a fast serving stack from a slow one —
chunked prefill, prefix caching, speculative decoding, disaggregated
prefill/decode — are now standard features of open-source vLLM. The frontier
moves in "incremental releases that can be just days apart," fast enough that
point-in-time benchmarks go stale; the industry's response was to re-benchmark
nightly across hundreds of chips.

An independent benchmark then puts a number on it: AMD's inference software
improved up to **2x between December 2025 and January 2026**, and nearly doubled
throughput at equal interactivity in under two months — on hardware that did not
change. A lead that erodes on that cadence is shorter-lived than the procurement
cycle meant to capture it.

## Why the interactive case is weaker than assumed

The most-cited evidence that latency costs money — Amazon's "every 100ms costs
1% of sales" — is an e-commerce page-load result from a different era and a
different interaction, recycled into AI latency marketing.

The direct test says something else. A CHI 2026 controlled experiment varied
time-to-first-token across 2, 9 and 20 seconds for 240 participants on two
knowledge-task types. Interaction behaviour was **robust to latency**. Perceived
quality ran **backwards**: 2-second responses were rated less thoughtful and less
useful than 9–20-second ones, with participants reading delay as deliberation.
The authors conclude latency is a tunable design variable, not simply a cost.

One experiment, one band (2–20s), one task family. But within what it tested, the
best available evidence contradicts the folklore it replaces.

## Where speed does pay

**Throughput, and agentic wall-clock.** The "same budget, very different wall
clock" effect is real and documented — as a purchasable tier. Batch APIs at both
OpenAI and Anthropic charge 50% of standard price for a 24-hour window. Identical
work, identical model, half the budget, seconds becoming a day.

The documented ceiling is 24 hours per batch, not a month.

And agentic workloads multiply sequential calls per task — tens of turns
typically, up to 200 — with heavy tails in turns, output length and tool latency.
That multiplication is the mechanism converting a per-token rate into hours of
wall clock, and it is why the question is sharper now than it was for single-turn
chat.

## Speed is already governed — at the platform layer

Microsoft's deployment-type documentation carries an explicit **Latency Service
Level Agreement** column. Priority processing and Provisioned deployments carry a
defined latency target per model. Standard carries none. Batch carries none.

Latency is not an unclaimed strategic axis that leaders failed to notice. It is a
priced, tiered contract term, and what a buyer gives up on the cheap tier is
precisely the latency guarantee. The gap is not strategic vision — it is that
most organisations are on the ungoverned tier by default rather than by decision.

## What to do

1. **Classify workloads by tier before comparing vendors.** The
   batch/standard/priority split holds the largest wall-clock difference
   available for a fixed budget, without changing provider.
2. **Treat open-weight vs proprietary as the gate.** Speed shopping pays 5–8x on
   open weights and roughly nothing on proprietary models.
3. **Buy the latency you need and stop paying for the rest.** A latency target is
   a contract term you can already request; on the standard tier there is nothing
   to enforce.
4. **Do not assume faster is better in the interface.** Spend the latency budget
   where it compounds — agentic loops — not on shaving an interactive response
   users may not reward.

## Provenance

"Speed is the moat" appears in this corpus as a quote from **Anush Elangovan, VP
GPU Software, AMD**, in a benchmark launch post. Nvidia's framing of the same
benchmark stresses performance per dollar and per megawatt. When the two largest
GPU vendors describe identical results and one says speed while the other says
efficiency, the framing is positioning, not physics.

---

*The book: [`speed-is-the-moat.pdf`](speed-is-the-moat.pdf) or [read online](https://tech.anujsadani.in/speed-is-the-moat/).
Underlying report with claim markers: [`.research/report.md`](.research/report.md).
Verification workspace: [`.research/`](.research/). Every figure above is bound
to a captured source at a quote locator; see the README for how to check any of
them.*
