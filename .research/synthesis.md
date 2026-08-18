# Synthesis: is inference speed the next durable differentiator?

Worked from `claims.jsonl` (49 claims, 23 sources). Organised by the brief's five
sub-questions. Every conclusion below is itself a bound claim (`c-100`–`c-109`).

---

## SQ1 — Has token cost actually commoditised?

**Converged.** Price per unit of capability is collapsing, and every source agrees
on the direction. Epoch AI measured 9x–900x per year across six benchmarks with a
median of 50x (`c-001`), accelerating after January 2024 to a median of 200x
(`c-002`). a16z independently reports 10x per year (`c-004`). OpenAI cut two
GPT-5.6 tiers by 20% and 80% in July 2026, three weeks after launch (`c-005`).

**Contested — and the disagreement is informative.** Epoch's median (50x/yr) and
a16z's headline (10x/yr) differ by 5x. They are not measuring the same thing:
Epoch fits a log-linear regression to the cheapest model clearing each capability
milestone across six benchmarks; a16z tracks MMLU-equivalence on a single curve.
Neither is wrong; the definition drives the number, which is the market-lens trap
in its textbook form. Epoch also cautions its own fastest rates may not persist
(`c-003`). Recorded as `stance: mixed` on `c-004`.

**Conclusion (`c-100`, moderate).** The brief's premise is half right. Cost is
*understood* — 98% of FinOps practitioners now manage AI spend (`c-040`). But cost
is not *settled*: it is still the axis on which frontier vendors publicly compete,
under explicit pressure from cost-sensitive buyers (`c-007`). Treating cost as
finished business and speed as the successor axis mis-describes a market where the
price war is currently the loudest thing happening.

---

## SQ2 — How large is the speed spread?

**Converged, with an important split by model class.**

*Open-weight models, competitively served.* On Gemma 4 31B at 131k context,
Cerebras returned 1,357 median output tokens/sec and a 2.43s total response
(`c-010`); SambaNova returned 201 tokens/sec and 13.49s on the same model and
context (`c-011`). That is 6.8x on generation rate and 5.6x on wall clock. On
Qwen3.6 27B, Groq returned 463 tokens/sec / 14.58s (`c-012`) against DeepInfra's
53 tokens/sec / 117.94s (`c-013`) — 8.1x wall clock, though that pair is not
like-for-like: DeepInfra's endpoint is FP8 at 262k context.

*Proprietary frontier models.* Claude Opus 5 (max) through Amazon Bedrock showed
44.88s total response (`c-014`), against 54.58s from Anthropic's own API and
61.68s via Google — roughly 1.4x.

**Single-source dependency — flagged.** Every cross-provider number above comes
from one snapshot of one benchmarker (`s-014`). It is a T2 independent source that
publishes its method, but it is one source, point-in-time, and MLPerf was captured
for corroboration of *method* rather than of these specific figures. If `s-014` is
withdrawn, SQ2 has no quantified answer.

**Measurement caveats that survive into the conclusion.** Output speed is defined
as tokens/sec *after* the first token, so it excludes the wait a user actually
feels (`c-015`); figures are P50 over a trailing 72 hours (`c-016`); TTFT includes
network latency from a single test location and can advantage providers by
geography (`c-017`).

**Conclusions.** `c-101` (moderate): the open-weight spread is 5–8x, far above the
2x threshold the brief set as the floor for strategic interest. `c-102` (low, single
source): the proprietary spread is ~1.4x, below it. The available speed advantage
is conditional on being able to choose who serves the weights.

---

## SQ3 — Does a lead persist?

**Converged, and this is where the thesis takes its real damage.**

The optimisations that once separated a fast serving stack from a slow one —
chunked prefill, prefix caching, speculative decoding, disaggregated prefill/decode
— are now listed as standard features of open-source vLLM (`c-024`). The frontier
advances in "incremental releases that can be just days apart" (`c-020`), fast
enough that SemiAnalysis states point-in-time benchmarks go stale and stop
representing achievable performance (`c-021`); the industry's answer was to
re-benchmark nightly across hundreds of chips (`c-022`).

**What does persist**, on weaker evidence: custom silicon reaches a low-latency
tier GPU providers cannot match by tuning batch size alone, but occupies "a
distinct and expensive corner" (`c-028`); and model labs hold a structural cost
advantage by backfilling idle capacity with training and research (`c-027`). Both
from a single T3 practitioner source (`s-004`) — flagged.

**The reframe.** Latency and throughput are not one axis but opposite ends of one
batch-size curve, with no free lunch on the same hardware (`c-025`), and where a
provider sits on it is a commercial decision as much as a technical one (`c-026`).
Nvidia's own framing of the same benchmark stresses performance per dollar and per
megawatt, not latency leadership (`c-029`).

**Provenance note.** The exact phrase "Speed is the moat" appears in this corpus
as a quote from AMD's VP of GPU Software in a benchmark launch post (`c-023`,
`c-109`). That is a reason to test the claim carefully, not to dismiss it — but it
should be known that the slogan has a vendor origin.

**Conclusions.** `c-103` (high): a software-derived speed lead is not durable, and
erodes faster than any procurement cycle can re-evaluate. `c-104` (moderate): what
persists is position on a curve, which is bought, not won.

---

## SQ4 — Does speed convert into outcomes?

**Converged on the throughput side.** The "same budget, very different wall clock"
effect is not speculative — it is a published product tier. Anthropic's batch API
charges 50% of standard prices with most batches under an hour (`c-030`) and a hard
24-hour expiry (`c-031`); OpenAI's is the same trade in the same shape (`c-032`).
Even inside that window a single 300k-token generation can exceed an hour (`c-033`).
Latency is sold as a tier, with priority requests prioritised over all others
(`c-034`).

**Counter-evidence, and it matters.** That purchasable priority tier is being
withdrawn, not expanded: Anthropic states Priority Tier capacity commitments are no
longer available for purchase (`c-035`). If buying latency were a growing market,
this is not the move one would expect.

**Contested / weak on the interactive side.** The most-repeated business case for
low latency is Amazon's "100ms = 1% of sales" — an e-commerce page-load finding
recycled into AI latency marketing, not a measurement of LLM inference (`c-038`,
`c-106`, recorded as `contradicted`, low confidence). This is the citation-laundering
trap the general lens warns about, and the corpus contains no independent study
linking LLM response latency to a business outcome.

**The mechanism that does hold.** Agentic workloads multiply sequential calls per
task — ~41 turns for office work, up to 200 tool-call turns for code QA (`c-036`),
heavy-tailed at every step (`c-037`). That is how a per-token rate becomes hours of
wall clock (`c-108`).

**Conclusion (`c-105`, high).** The effect is real and documented, but as a
*purchasable tier* rather than an earned advantage, and the documented ceiling is
24 hours per batch — not a month. The brief's "1 day vs 1 month" is directionally
supported in structure and unsupported in magnitude.

---

## SQ5 — Is speed governed as a strategic axis?

**Weakest sub-question in the project. Read the confidence carefully.**

Managing AI spend is now near-universal: 98% of 1,192 State of FinOps respondents,
up from 31% two years earlier (`c-040`). The priorities that displaced pure cost
optimisation are governance, forecasting, organisational alignment and expanding
coverage (`c-041`), with mature practice moving toward unit economics and
influencing technology selection (`c-042`) — the surface a speed criterion would
have to occupy.

Latency and throughput do not appear in that priority list. **That is
absence-of-mention in one press summary of one survey, not a measured finding**,
and it must not be written up as evidence that leaders ignore speed.

**Counter-signal.** Speed is being institutionalised at the benchmark layer:
MLPerf v5.1 expanded latency-constrained interactive scenarios explicitly for
agentic applications (`c-043`), drawing a record 27 submitters (`c-044`).
Conclusion `c-107` (moderate).

**The brief's claim that few leaders treat speed as a long-horizon axis is
consistent with everything found here and was not verified.** See gaps.

---

## Overall answer

**"Speed is the moat" is false as stated and points at something true.**

False as stated, because a moat implies an advantage a competitor cannot cross,
and the evidence shows the opposite: serving optimisations diffuse into open-source
defaults (`c-024`), the frontier moves in days (`c-020`), and position on the
latency/throughput curve is purchased by choosing a batch size and a price tier
(`c-104`, `c-105`), not defended.

True in what it points at, on three counts. The dispersion is real and large where
weights are openly served — 5–8x between providers of an identical model (`c-101`).
It is *persistently* available, because it comes from where providers choose to sit
on the curve rather than from anyone's cleverness, so it does not close the way a
technology gap closes. And agentic workloads multiply per-call latency into
wall-clock task time (`c-108`), which is the mechanism that makes the dispersion
matter more now than it did for single-turn chat.

So the durable asset is not speed. It is **the capability to keep re-choosing** —
to re-evaluate placement on the cost/latency/throughput surface faster than the
frontier moves, given that the frontier moves in days (`c-103`) and typical
governance reviews do not. That is an attention-and-process advantage, and it is
closer to the brief's own instinct ("not many leaders add speed as the long-horizon
axis") than to its literal thesis.

**One correction to the framing worth carrying into the report:** speed and cost
are not sequential axes. They are two readings of the same batch-size curve
(`c-025`), and OpenAI's own account of its price cuts attributes them to efficiency
work (`c-006`). A speed programme that ignores this will keep rediscovering that
its latency wins show up as cost wins, and vice versa.

---

## What would break these conclusions

- **`c-101`/`c-102` rest on one snapshot of one benchmarker.** If Artificial
  Analysis's provider figures are systematically wrong — wrong test geography,
  unrepresentative prompts, providers tuning for the benchmark — SQ2 has no answer
  and the "5–8x" number should not be repeated.
- **`c-103` would break** if a provider demonstrated a speed lead sustained across
  multiple model generations that open-source stacks did not close. Nothing in this
  corpus shows that; the custom-silicon case (`c-028`) is the nearest candidate and
  rests on a single T3 source.
- **The strongest honest case against the overall answer** is the custom-silicon
  argument: if the low-latency tier genuinely cannot be reached by GPU batch tuning
  (`c-028`), then a hardware-backed speed moat exists at the extreme, and the fact
  that it is expensive today says nothing about whether it stays expensive. This
  corpus cannot settle it — the only source making the argument is also the only
  source making the counter-argument.
- **`c-100` would break** if the July 2026 price cuts turn out to be a one-off
  rather than continuing competition.

## Gaps

**Checked and absent**
- No independent study in this corpus links LLM response latency to a measured
  business outcome. What circulates is recycled e-commerce page-load data (`c-106`).
- No source quantifies how quickly a specific inference optimisation went from
  proprietary to commodity. The diffusion evidence is qualitative (`c-020`, `c-024`);
  the brief asked for an interval and there is not one.
- No evidence supporting a *one-month* wall-clock figure for the same task at the
  same budget. Documented ceiling is 24 hours per batch (`c-031`, `c-032`).

**Not checked**
- Self-hosted serving economics, where the buyer controls batch size directly. Out
  of the gathered corpus, though squarely relevant to the decision.
- Regional and multi-region latency effects, flagged by `c-017` and not pursued.
- Whether enterprise procurement contracts actually carry latency SLOs. This is the
  direct test of SQ5 and it was not run.

**Unknowable from public sources**
- Provider batch sizes, scheduling policy, and per-tier margins. These determine the
  whole latency/throughput picture (`c-025`, `c-026`) and none of it is disclosed.
- Whether Anthropic's withdrawal of purchasable Priority Tier (`c-035`) reflects
  capacity constraints, weak demand, or a pricing change. The fact is public; the
  reason is not.

## Corpus integrity notes

- **`s-010` (GMI Cloud) captured only page navigation, not article text.** It was
  registered as a source but no claim binds to it, and the disconfirming argument it
  was meant to carry was re-sourced from `s-004` and `s-022` instead.
- **OpenAI's first-party price-cut announcement returned HTTP 403** to both capture
  routes. The July 2026 price claims therefore rest on CNBC's reporting (`s-016`),
  T3 rather than T1.
- **Disconfirming searches did run** and did return material: `c-035` (tier
  withdrawn), `c-038`/`c-106` (folklore evidence base), `c-029` (Nvidia competing on
  efficiency not latency), `c-102` (spread nearly absent for proprietary models),
  and `c-100` (cost still the live axis). This corpus is not one-sided.

---

# Revision: gap-fixing pass

Four of the six gaps named above were closed by further gathering. Two of the
closures changed the answer rather than merely supporting it, which is recorded
here rather than silently folded into the prose.

## Closed — and it changed the finding

**SQ4, interactive latency.** The first pass reported that no independent study
linked LLM latency to an outcome, leaving only recycled e-commerce folklore
(`c-038`, `c-106`). A CHI 2026 controlled experiment exists: 240 participants,
time-to-first-token varied across 2/9/20 seconds, two knowledge-task types
(`c-050`). Findings: interaction behaviour was robust to latency (`c-051`), and
perceived quality ran *backwards* — 2-second responses were rated less thoughtful
and less useful than 9–20-second ones (`c-052`), with the authors concluding
latency is a tunable design variable rather than a pure cost (`c-053`).

Recorded as `stance: mixed` on `c-052` and `c-110`, contradicting `s-017`. This is
a genuine reversal of the assumption the thesis rests on for interactive work, and
it narrows the speed case to throughput and agentic wall-clock.

**SQ5, governance.** The first pass left this unresolved, resting on
absence-of-mention in one survey. It is now answered directly and against the
thesis: Microsoft's deployment-type documentation carries an explicit *Latency
Service Level Agreement* column, with Priority processing and Provisioned tiers
carrying a defined latency target per model (`c-060`) and Standard carrying none
(`c-061`). Latency is already a priced, tiered contract term (`c-111`).

The premise therefore needs revising, not confirming: speed is not an unclaimed
strategic axis, it is a solved commercial problem at the platform layer that many
buyers have not exercised.

## Closed — supporting the existing finding

**SQ3, erosion interval.** The brief asked for an interval and the first pass could
not supply one. A second independent benchmark records AMD's inference software
improving up to 2x between December 2025 and January 2026 (`c-070`) and nearly
doubling throughput at equal interactivity in under two months (`c-071`), on
unchanged silicon. The half-life of a software-derived speed lead is therefore
roughly one to two months (`c-112`). This is the strongest single number in the
project and it sharpens rather than alters the conclusion.

**SQ1, first-party pricing.** OpenAI's published price list was reached through the
documentation markdown route after the announcement page returned 403, confirming
the CNBC-reported figures at $0.20/$1.20 per million tokens for the cheapest tier
(`c-080`). The July 2026 pricing claims no longer rest on T3 reporting alone.

**Corpus integrity.** The GMI Cloud source that captured only navigation (`s-010`)
was re-captured successfully as `s-033`. The original row is retained unedited, as
the ledger rules require.

## Still open

- **The API-provider spread is still single-source.** `s-028` corroborates that
  large dispersion exists and that the throughput/latency curve is real (`c-072`),
  but it measures hardware and serving stacks, not API endpoints. The specific
  6.8x figure between two named providers still rests on `s-014` alone.
- **The latency experiment is narrow** — 2–20s, knowledge tasks, crowdsourced
  participants. It does not cover voice, real-time, or long-horizon agentic work.
- **Enterprise-layer governance remains unverified.** Platforms sell latency
  contractually; whether buyers set and enforce internal latency SLOs would need
  procurement documents.
- **No named technique timed from paper to commodity default.** A rate of
  improvement is not the same measurement the brief asked for.
- **No independent auditor pass** was run over the bindings.

## Net effect on the overall answer

The conclusion is unchanged in direction and stronger in evidence. "Speed is the
moat" fails on three counts now rather than one: the lead has a measured half-life
of one to two months (`c-112`), the latency premium is a purchasable contract term
rather than an earned advantage (`c-111`), and the interactive business case is
contradicted by the only controlled study in the corpus (`c-110`).

What survives is narrower and more useful than the thesis: dispersion is real,
placement is a decision most organisations make by default, and the compounding
case for speed lives in agentic wall-clock, not in interface responsiveness.
