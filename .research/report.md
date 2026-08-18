# Is speed the moat?

**Question.** Now that per-token cost is broadly understood, does inference speed
constitute a durable differentiator for LLM systems — or a lead that erodes as fast
as it is won?

**Answer, in one line.** Speed is not a moat. The dispersion in speed is large and
persistent, but a lead within it now has a measured half-life of one to two
months[^c-112], latency is already sold as a contractual tier rather than won[^c-111],
and the one controlled experiment on interactive latency found faster responses
changed no behaviour and were judged *worse*[^c-110]. What is left worth organising
around is placement, not pace.

---

## 1. The premise needs one correction first

The thesis assumes cost is settled and speed is the successor axis. The first half
holds; the second does not follow.

Cost per unit of capability is collapsing on every measure available. Epoch AI
found the price of reaching a fixed capability milestone falling between 9x and
900x per year across six benchmarks, with a median of 50x[^c-001], accelerating
after January 2024 to a median of 200x[^c-002]. **The sources disagree on the
headline rate**: a16z reports 10x per year for a model of equivalent
performance[^c-004], five times slower than Epoch's median[^c-001]. They are
measuring different things — Epoch regresses across capability milestones on six
benchmarks, a16z tracks a single MMLU-equivalence curve — and Epoch itself cautions
that its fastest observed rates may not persist[^c-003]. Take the direction as
settled and the magnitude as unsettled.

But "understood" is not "finished". Price is still where frontier vendors compete
in public: OpenAI cut GPT-5.6 Terra by 20% and Luna by 80% in July 2026, three
weeks after those models launched[^c-005], under reported pressure from a
cost-sensitive customer base[^c-007], and attributed the cuts to advancing
capability and efficiency together[^c-006]; OpenAI's own published price list
confirms those figures at $0.20 and $1.20 per million tokens for the cheapest
tier[^c-080]. Cost is understood as a practice and unsettled as a competitive
axis[^c-100].

That last point is the correction that matters. **Speed and cost are not sequential
axes.** They are two readings of the same curve: on fixed hardware you cannot have
both minimum latency and maximum throughput[^c-025], and where a provider sits
between them is a commercial decision as much as a technical one[^c-026]. A speed
programme that treats cost as solved will keep rediscovering that its latency wins
arrive as cost wins, and its cost wins arrive as latency losses.

## 2. The speed spread is real — and much larger than expected

For open-weight models served competitively, the gap between providers of *identical
weights* is not marginal. On Gemma 4 31B at 131k context, Cerebras returned a median
1,357 output tokens/sec with a 2.43s total response time[^c-010]; SambaNova returned
201 tokens/sec and 13.49s on the same model at the same context[^c-011]. Dividing
those figures gives 6.8x on generation rate and 5.6x on wall clock — and the slower
endpoint was the cheaper one, at $0.10 against $0.24 per task[^c-011].

The pattern repeats. On Qwen3.6 27B, Groq returned 463 tokens/sec and 14.58s[^c-012]
against DeepInfra's 53 tokens/sec and 117.94s[^c-013] — though that pair is not
like-for-like, since DeepInfra's endpoint is an FP8 quantisation at 262k
context[^c-013].

**Then the finding that reframes the question.** For a proprietary frontier model,
the spread nearly disappears: Claude Opus 5 (max) via Amazon Bedrock showed a 44.88s
total response time[^c-014], against 54.58s from Anthropic's own API[^c-018] and
61.68s via Google[^c-019] — about 1.4x. The brief set 2x as the floor below which a speed advantage is
strategically uninteresting. Open weights clear it by 3–4x[^c-101]; proprietary
models fall below it[^c-102].

So the size of the speed prize depends on a structural question, not a technical
one: **can you choose who serves the weights?** If you are on a frontier proprietary
model, there is very little speed on the table and the decision is nearly moot. If
you are on open weights, there is 5–8x.

*Confidence: moderate on the open-weight figures, low on the proprietary
comparison.* Every cross-provider number above comes from a single point-in-time
snapshot of one benchmarker. It publishes its method, but it is one source. Its
output-speed metric deliberately excludes the initial wait, measuring tokens/sec
only after the first token arrives[^c-015]; figures are medians over a trailing 72
hours[^c-016]; and its time-to-first-token includes network latency from one test
location, which it acknowledges may advantage or disadvantage providers by
geography[^c-017]. If that source is wrong, this section has no answer.

## 3. A speed lead does not persist — this is where the thesis breaks

The optimisations that once separated a fast serving stack from a slow one —
chunked prefill, prefix caching, speculative decoding, disaggregated prefill/decode
— are now listed as standard features of open-source vLLM[^c-024]. The frontier
moves in "incremental releases that can be just days apart"[^c-020], fast enough
that SemiAnalysis states point-in-time benchmarks go stale and stop representing
achievable performance[^c-021]. The industry's response was not to publish better
benchmarks but to run them nightly across hundreds of chips[^c-022].

A lead that diffuses on a days-to-weeks cadence is not a moat. It erodes faster than
any procurement or architecture review can re-evaluate it[^c-103]. What persists is
not speed but position on a curve that is bought rather than won[^c-104].

**That erosion now has a number attached.** A second benchmark, run independently of
the first, recorded AMD's inference software improving by up to 2x between December
2025 and January 2026[^c-070] — and nearly doubling throughput at equal interactivity
in under two months[^c-071], on unchanged silicon. So the half-life of a
software-derived speed lead is measurable, and it is roughly one to two
months[^c-112]. That is the single most decision-relevant number in this report: it
is shorter than most procurement cycles, shorter than most architecture reviews, and
far shorter than the horizon on which "moat" is normally used. The same source
independently reproduces the structural finding that inference performance is a
throughput-against-latency curve rather than a single number[^c-072].

Two candidate exceptions, both on thin evidence from a single practitioner source.
Custom silicon reaches a low-latency tier GPU providers cannot match by tuning batch
size alone, while occupying "a distinct and expensive corner" of the
market[^c-028]. And model labs hold a structural cost advantage because they can
backfill idle serving capacity with training and research work[^c-027]. The
custom-silicon argument is the strongest case against this report's conclusion, and
it cannot be settled here — the only source making it is also the source
qualifying it.

It is worth knowing where the slogan comes from. In this corpus, the exact phrase
"Speed is the moat" is a quote from AMD's VP of GPU Software in a benchmark launch
post[^c-023][^c-109]. Meanwhile Nvidia's framing of the same benchmark stresses
performance per dollar and per megawatt rather than latency leadership[^c-029].
When the two largest GPU vendors describe the same results, one says speed and the
other says efficiency — which tells you the framing is positioning, not physics.

## 4. "Same budget, one day versus one month" — mostly right, wrong magnitude

This part of the thesis is the best-evidenced, and it is documented as a product
tier rather than as an achievement.

Anthropic's batch API charges 50% of standard prices, with most batches finishing in
under an hour[^c-030], results available on completion or at 24 hours, whichever
comes first, and expiry after that[^c-031]. OpenAI's batch API is the same trade in
the same shape: 50% lower cost, higher rate limits, 24-hour turnaround[^c-032]. Even
inside that window a single 300k-token generation can take over an hour[^c-033].
Latency is explicitly sold, with priority requests prioritised over all
others[^c-034].

So: identical work, identical model, **half the budget, and a wall clock that moves
from seconds to a day**[^c-105]. The structure of the claim is confirmed. The
magnitude is not — the documented ceiling is 24 hours per batch[^c-031][^c-032], and
nothing found here supports a one-month figure for the same task at the same budget.

**The counter-signal deserves attention.** The purchasable priority tier is being
withdrawn rather than expanded: Anthropic states Priority Tier capacity commitments
are no longer available for purchase[^c-035]. If buying latency were a growing
market, that is not the move one would expect.

Where speed genuinely compounds is agentic work. Those workloads multiply sequential
model calls per task — around 41 turns for an office-work trace, up to 200 tool-call
turns for code QA[^c-036][^c-039] — with heavy tails in turns, output length and
tool latency[^c-037]. That multiplication is the mechanism by which a per-token rate
becomes hours of wall clock[^c-108], and it is why the question is sharper now than
it was for single-turn chat.

### The interactive case, now that there is real evidence

The most-repeated business case for low latency is Amazon's "every 100ms costs 1% of
sales" — an e-commerce page-load result recycled into AI latency marketing, not a
measurement of LLM inference[^c-038][^c-106].

There is now a direct test, and **the sources genuinely disagree**. A controlled
experiment published at CHI 2026 varied time-to-first-token across 2, 9 and 20
seconds for 240 participants across two knowledge-task types[^c-050]. Interaction
behaviour was robust to latency — prompting, copying and refreshing rates did not
shift across conditions, while task type did drive behaviour[^c-051]. And the
perception effect ran *backwards*: participants served in 2 seconds rated outputs as
**less thoughtful and less useful** than those who waited 9 to 20 seconds[^c-052],
apparently reading delay as deliberation. The authors conclude latency is not simply
a cost to minimise but a tunable design variable[^c-053].

One experiment on knowledge tasks does not generalise to voice agents, trading, or
anything with a hard real-time constraint, and it says nothing about the 30-second-
plus waits that agentic work produces. But within the band it tested, the best
available evidence contradicts the folklore it replaces[^c-110]. The throughput case
is well-evidenced. The interactive-latency case is not merely unproven — it is
actively contested by the only controlled study in this corpus.

## 5. Speed *is* governed — at the platform layer, not the enterprise one

Managing AI spend is now near-universal: 98% of 1,192 State of FinOps respondents,
up from 31% two years earlier[^c-040]. The priorities that displaced pure cost
optimisation are governance, forecasting, organisational alignment and expanding
technology coverage[^c-041], with mature practice moving toward unit economics and
influencing technology selection[^c-042].

Latency and throughput do not appear in that list. That is absence-of-mention in one
summary of one survey, not a measured finding.

**But the contractual evidence answers the question directly, and it answers it
against the thesis.** Microsoft's deployment-type documentation carries an explicit
*Latency Service Level Agreement* column: Priority processing and Provisioned
deployments both carry a defined latency target per model[^c-060], while Standard
deployments carry none at all[^c-061]. Latency is not an ungoverned engineering
metric that leaders have failed to notice. It is already a procurement term, priced,
tiered, and written into the contract — and what a buyer forfeits on the cheap tier
is precisely the latency guarantee[^c-111].

So the premise needs revising rather than confirming. Speed is not an unclaimed
strategic axis waiting for someone to own it; it is a solved commercial problem at
the platform layer that many buyers have simply not exercised. That is a different
problem with a different fix — an internal procurement and placement decision, not a
research programme.

What remains genuinely unverified is the *enterprise* layer: whether buying
organisations actually set internal latency SLOs and hold vendors to those targets.
That would need procurement contracts this project did not obtain.

There is a counter-signal at the benchmark layer: MLPerf v5.1 expanded
latency-constrained interactive scenarios explicitly for agentic
applications[^c-043], drawing a record 27 submitting organisations[^c-044]. Speed is
being standardised where vendors are measured, whatever is happening inside
enterprise governance[^c-107].

## 6. What follows for the decision

The decision this fed was whether speed deserves a standing owner, budget line and
procurement criterion, or stays a per-project tuning exercise.

**It deserves an owner, but a procurement one rather than a research one.** Not a
team chasing the fastest provider — that lead has a one-to-two-month
half-life[^c-112] and the chase never ends. A function that owns *placement*: which
workloads sit on which contractual tier, given that the tiers already exist and
already price latency[^c-060][^c-061].

Four things follow concretely:

1. **Classify workloads by tier before comparing vendors.** The batch/standard/
   priority split is where the largest wall-clock difference for a fixed budget
   actually lives[^c-030][^c-032], and it is available today without changing
   provider.
2. **Treat the open-weight/proprietary distinction as the gate.** Speed shopping
   pays 5–8x on open weights[^c-101] and roughly nothing on proprietary
   models[^c-102]. Model-class choice determines whether a speed programme has
   anything to work with.
3. **Buy the latency you actually need, and stop paying for the rest.** A latency
   target is a contract term you can already ask for[^c-060]; on the standard tier
   there is no guarantee to enforce[^c-061]. Most organisations are on the
   ungoverned tier by default rather than by decision.
4. **Do not assume faster is better in the interface.** Within 2–20 seconds on
   knowledge tasks, faster changed no behaviour and read as *less* thoughtful[^c-052].
   Spend the latency budget where it compounds — agentic loops with dozens of
   sequential turns[^c-036][^c-108] — not on shaving an interactive response that
   users may not reward.

---

## Limitations

A first pass of this report carried six gaps. Four were closed by further gathering;
what follows is what actually remains.

- **Still single-source at the API-provider layer.** Every cross-provider figure in
  §2 comes from one point-in-time snapshot of one benchmarker. The corroborating
  benchmark[^c-070][^c-072] measures *hardware and serving stacks*, not API endpoints,
  so it confirms the shape of the finding and the existence of large dispersion —
  it does not independently confirm that Cerebras is 6.8x SambaNova on Gemma 4 31B.
  That specific number still rests on one source.
- **The latency experiment is narrow.** It covers 2–20 second time-to-first-token on
  knowledge tasks with crowdsourced participants[^c-050]. It is the best evidence in
  this corpus and it does not settle voice, real-time, or long-horizon agentic work.
- **The enterprise governance layer is still unverified.** §5 establishes that
  platforms sell latency contractually[^c-060]. Whether buying organisations set and
  enforce internal latency SLOs would need procurement contracts this project did
  not obtain.
- **No measured diffusion interval for a named technique.** §3 now gives a rate of
  improvement[^c-070][^c-071], which is not the same as timing one specific
  optimisation from paper to commodity default. That original question is still open.
- **No independent auditor pass.** Claims were bound by exact quote and mechanically
  quote-checked against snapshots, but no fresh-context reviewer confirmed that the
  quotes mean what the claims need them to mean.
- **Out of scope by design:** organisational execution speed, training speed, model
  quality rankings, GPU supply-chain economics, self-hosted serving, and any
  specific vendor recommendation.

**Closed since the first pass:** first-party OpenAI pricing now corroborates the
reported July 2026 figures[^c-080]; the erosion rate has a number[^c-112]; the
interactive-latency question has a controlled experiment instead of
folklore[^c-050]; sub-question 5 has a contractual answer[^c-111]; and the source
that captured only navigation was re-captured successfully.

## What would change the answer

The conclusion flips toward "speed is a moat" if the custom-silicon tier proves
unreachable by GPU batch tuning over multiple model generations[^c-028] rather than
being a temporary and expensive corner — that is the one structural argument this
corpus cannot close. It flips further away if the open-weight spread[^c-101] turns
out to be an artefact of one benchmarker's test geography or prompt mix[^c-017].

The finding most likely to be overturned by better evidence is the interactive-
latency reversal[^c-052]. It is a single experiment, and a second study finding the
opposite would restore the conventional view. The finding least likely to be
overturned is the erosion rate[^c-112]: two independent benchmarks, measuring
different layers, both report software gains arriving faster than procurement can
respond.

## References

[^c-001]: Across six benchmarks and three years, Epoch AI measured the price of reaching a fixed capability milestone falling at rates between 9x and 900x per year, with a median of 50x per year.
    - s-001 "we found prices declining between 9x per year and 900x pe..." - *LLM inference prices have fallen rapidly but unequally across tasks*, Epoch AI, n.d.. <https://epoch.ai/data-insights/llm-inference-price-trends> (accessed 2026-08-18) [T2]
    - _(confidence: high)_

[^c-002]: Epoch AI found the fastest price-decline trends began after January 2024: restricting the data to post-January-2024 models raised the median decline rate from 50x to 200x per year.
    - s-001 "the median rate increased from 50x per year to 200x per year" - *LLM inference prices have fallen rapidly but unequally across tasks*, Epoch AI, n.d.. <https://epoch.ai/data-insights/llm-inference-price-trends> (accessed 2026-08-18) [T2]
    - _(confidence: high)_

[^c-003]: Epoch AI cautions that the fastest price declines it measured are recent and may not persist.
    - s-001 "The fastest price drops in that range have occurred in th..." - *LLM inference prices have fallen rapidly but unequally across tasks*, Epoch AI, n.d.. <https://epoch.ai/data-insights/llm-inference-price-trends> (accessed 2026-08-18) [T2]
    - _(confidence: high)_

[^c-004]: a16z puts the decline at 10x per year for an LLM of equivalent performance, an order of magnitude below Epoch AI's median estimate of 50x per year for capability-milestone pricing.
    - s-003 "For an LLM of equivalent performance, the cost is decreas..." - *Welcome to LLMflation - LLM inference cost is going down fast*, Andreessen Horowitz, n.d.. <https://a16z.com/llmflation-llm-inference-cost/> (accessed 2026-08-18) [T4]
    - _(stance: mixed; confidence: moderate; contradicted by s-001)_

[^c-005]: In July 2026 OpenAI cut GPT-5.6 Terra by 20 percent and GPT-5.6 Luna by 80 percent, roughly three weeks after those models were publicly released.
    - s-016 "reducing the price of Terra by 20% to $2 per million inpu..." - *OpenAI cuts prices for two of its GPT-5.6 AI models as companies grow sensitive to costs*, CNBC, 2026-07-30. <https://www.cnbc.com/2026/07/30/open-ai-price-cut-gpt.html> (accessed 2026-08-18) [T3]
    - _(confidence: high)_

[^c-006]: OpenAI attributed its July 2026 price cuts to a strategy of advancing capability and efficiency together so each model generation does more work at lower cost.
    - s-016 "Our strategy remains focused on advancing both capability..." - *OpenAI cuts prices for two of its GPT-5.6 AI models as companies grow sensitive to costs*, CNBC, 2026-07-30. <https://www.cnbc.com/2026/07/30/open-ai-price-cut-gpt.html> (accessed 2026-08-18) [T3]
    - _(confidence: high)_

[^c-007]: Contemporary reporting frames the competitive pressure on frontier model vendors as pressure on cost, not on speed.
    - s-016 "The company is facing pressure to cater to a more cost-se..." - *OpenAI cuts prices for two of its GPT-5.6 AI models as companies grow sensitive to costs*, CNBC, 2026-07-30. <https://www.cnbc.com/2026/07/30/open-ai-price-cut-gpt.html> (accessed 2026-08-18) [T3]
    - _(confidence: moderate)_

[^c-010]: On the same open-weight model at the same context length (Gemma 4 31B, 131k), Cerebras served a median 1,357 output tokens/sec at a 2.43s total response time.
    - s-014 "Cerebras Gemma 4 31B 131k Open 30 $0.24 1,357 0.79 2.43" - *Artificial Analysis: LLM API Provider Leaderboard*, Artificial Analysis, n.d.. <https://artificialanalysis.ai/leaderboards/providers> (accessed 2026-08-18) [T2]
    - _(confidence: moderate)_

[^c-011]: SambaNova served that same model and context length at 201 output tokens/sec and a 13.49s total response time, for $0.10 cost per task against Cerebras's $0.24 - so the 6.8x slower endpoint was the cheaper one.
    - s-014 "SambaNova Gemma 4 31B 131k Open 30 $0.10 201 2.37 13.49 8.63" - *Artificial Analysis: LLM API Provider Leaderboard*, Artificial Analysis, n.d.. <https://artificialanalysis.ai/leaderboards/providers> (accessed 2026-08-18) [T2]
    - _(confidence: moderate)_

[^c-012]: On Qwen3.6 27B, Groq returned a median 463 output tokens/sec and a 14.58s total response time.
    - s-014 "Groq Qwen3.6 27B 131k Open 38 $0.27 463 1.24 14.58 12.26" - *Artificial Analysis: LLM API Provider Leaderboard*, Artificial Analysis, n.d.. <https://artificialanalysis.ai/leaderboards/providers> (accessed 2026-08-18) [T2]
    - _(confidence: moderate)_

[^c-013]: DeepInfra's Qwen3.6 27B endpoint returned 53 output tokens/sec and a 117.94s total response time for $0.19 per task, but it is an FP8 quantisation at a 262k context rather than a like-for-like serving configuration.
    - s-014 "DeepInfra Qwen3.6 27B FP8 262k Open 38 $0.19 53 1.19 117...." - *Artificial Analysis: LLM API Provider Leaderboard*, Artificial Analysis, n.d.. <https://artificialanalysis.ai/leaderboards/providers> (accessed 2026-08-18) [T2]
    - _(confidence: moderate)_

[^c-014]: For a proprietary frontier model the cross-provider spread is far smaller than for open-weight models: Claude Opus 5 (max) via Amazon Bedrock showed a 44.88s total response time.
    - s-014 "Amazon Bedrock Claude Opus 5 (max) 1M Proprietary 63 $2.3..." - *Artificial Analysis: LLM API Provider Leaderboard*, Artificial Analysis, n.d.. <https://artificialanalysis.ai/leaderboards/providers> (accessed 2026-08-18) [T2]
    - _(confidence: moderate)_

[^c-015]: Artificial Analysis defines output speed as tokens received per second after the first token, so the headline tokens/sec figure deliberately excludes the initial wait a user experiences.
    - s-002 "Output Speed (output tokens per second): The average numb..." - *Language Model API Performance Benchmarking (Methodology)*, Artificial Analysis, n.d.. <https://artificialanalysis.ai/methodology/performance-benchmarking> (accessed 2026-08-18) [T2]
    - _(confidence: high)_

[^c-016]: Artificial Analysis reports performance as a median over the trailing 72 hours rather than as a single measurement.
    - s-002 "Performance measurements are represented as the median (P..." - *Language Model API Performance Benchmarking (Methodology)*, Artificial Analysis, n.d.. <https://artificialanalysis.ai/methodology/performance-benchmarking> (accessed 2026-08-18) [T2]
    - _(confidence: high)_

[^c-017]: Artificial Analysis states that its time-to-first-token figures include network latency from a single test location and may advantage or disadvantage providers by server geography.
    - s-002 "which may advantage or disadvantage certain providers bas..." - *Language Model API Performance Benchmarking (Methodology)*, Artificial Analysis, n.d.. <https://artificialanalysis.ai/methodology/performance-benchmarking> (accessed 2026-08-18) [T2]
    - _(confidence: high)_

[^c-018]: Anthropic's own API served Claude Opus 5 (max) at 51 median output tokens/sec with a 54.58s total response time and $2.34 cost per task.
    - s-014 "Anthropic Claude Opus 5 (max) 1M Proprietary 63 $2.34 51 ..." - *Artificial Analysis: LLM API Provider Leaderboard*, Artificial Analysis, n.d.. <https://artificialanalysis.ai/leaderboards/providers> (accessed 2026-08-18) [T2]
    - _(confidence: moderate)_

[^c-019]: Google served the same model at 53 median output tokens/sec with a 61.68s total response time and $3.31 cost per task - the slowest and most expensive of the three routes to identical weights.
    - s-014 "Google Claude Opus 5 (max) 1M Proprietary 63 $3.31 53 52...." - *Artificial Analysis: LLM API Provider Leaderboard*, Artificial Analysis, n.d.. <https://artificialanalysis.ai/leaderboards/providers> (accessed 2026-08-18) [T2]
    - _(confidence: moderate)_

[^c-020]: Inference software performance improves in incremental releases that can be days apart, across SGLang, vLLM, TensorRT-LLM, CUDA and ROCm.
    - s-022 "increase the Pareto frontier of performance in incrementa..." - *InferenceMAX: Open Source Inference Benchmarking*, SemiAnalysis, n.d.. <https://newsletter.semianalysis.com/p/inferencemax-open-source-inference> (accessed 2026-08-18) [T2]
    - _(confidence: high)_

[^c-021]: SemiAnalysis states that the pace of inference software improvement makes point-in-time benchmarks go stale quickly and unrepresentative of current achievable performance.
    - s-022 "benchmarks conducted at a fixed point in time quickly go ..." - *InferenceMAX: Open Source Inference Benchmarking*, SemiAnalysis, n.d.. <https://newsletter.semianalysis.com/p/inferencemax-open-source-inference> (accessed 2026-08-18) [T2]
    - _(confidence: high)_

[^c-022]: The response to that staleness was to make benchmarking continuous: InferenceMAX re-runs its suite nightly across hundreds of chips.
    - s-022 "runs our suite of benchmarks every night on hundreds of c..." - *InferenceMAX: Open Source Inference Benchmarking*, SemiAnalysis, n.d.. <https://newsletter.semianalysis.com/p/inferencemax-open-source-inference> (accessed 2026-08-18) [T2]
    - _(confidence: high)_

[^c-023]: The phrase 'Speed is the moat' is used in this market by an interested party: AMD's VP of GPU Software, Anush Elangovan, quoted in the InferenceMAX launch post.
    - s-022 "Speed is the moat. ... Anush Elangovan, VP GPU Software, AMD" - *InferenceMAX: Open Source Inference Benchmarking*, SemiAnalysis, n.d.. <https://newsletter.semianalysis.com/p/inferencemax-open-source-inference> (accessed 2026-08-18) [T2]
    - _(confidence: high)_

[^c-024]: The optimisations that once distinguished fast serving stacks are now standard features of open-source vLLM: chunked prefill, prefix caching, speculative decoding and disaggregated prefill/decode.
    - s-006 "Advanced features: chunked prefill, prefix caching, guide..." - *Inside vLLM: Anatomy of a High-Throughput LLM Inference System*, vLLM project, 2025-09-05. <https://vllm.ai/blog/2025-09-05-anatomy-of-vllm> (accessed 2026-08-18) [T2]
    - _(confidence: high)_

[^c-025]: Latency and throughput are not one axis but a trade-off set by batch size: on the same hardware you cannot have both minimum latency and maximum throughput.
    - s-004 "There is no free lunch, you cannot have both minimum late..." - *The Economics of LLM Inference: Batch Sizes, Latency Tiers, and Why Model Labs Have an Advantage*, mlechner (Substack), n.d.. <https://mlechner.substack.com/p/the-economics-of-llm-inference-batch> (accessed 2026-08-18) [T3]
    - _(confidence: moderate)_

[^c-026]: Where a provider sits on that latency-throughput curve is a commercial decision as much as a technical capability.
    - s-004 "Where a provider sets their batch size is a business deci..." - *The Economics of LLM Inference: Batch Sizes, Latency Tiers, and Why Model Labs Have an Advantage*, mlechner (Substack), n.d.. <https://mlechner.substack.com/p/the-economics-of-llm-inference-batch> (accessed 2026-08-18) [T3]
    - _(confidence: moderate)_

[^c-027]: Model labs hold a structural cost advantage in inference because they can backfill idle serving capacity with training, research and offline batch work.
    - s-004 "They can backfill idle capacity with training runs, resea..." - *The Economics of LLM Inference: Batch Sizes, Latency Tiers, and Why Model Labs Have an Advantage*, mlechner (Substack), n.d.. <https://mlechner.substack.com/p/the-economics-of-llm-inference-batch> (accessed 2026-08-18) [T3]
    - _(confidence: moderate)_

[^c-028]: Custom inference silicon reaches a latency tier that GPU-based providers cannot match by tuning batch size alone, but it currently occupies a distinct and expensive corner of the market.
    - s-004 "custom hardware creates a tier that GPU-based providers can" - *The Economics of LLM Inference: Batch Sizes, Latency Tiers, and Why Model Labs Have an Advantage*, mlechner (Substack), n.d.. <https://mlechner.substack.com/p/the-economics-of-llm-inference-batch> (accessed 2026-08-18) [T3]
    - _(confidence: moderate)_

[^c-029]: Nvidia's own framing of the same benchmark stresses performance per dollar and per megawatt rather than raw latency leadership.
    - s-022 "delivers unmatched performance per dollar and per megawatt" - *InferenceMAX: Open Source Inference Benchmarking*, SemiAnalysis, n.d.. <https://newsletter.semianalysis.com/p/inferencemax-open-source-inference> (accessed 2026-08-18) [T2]
    - _(confidence: moderate)_

[^c-030]: Anthropic's Message Batches API charges 50 percent of standard API prices, with most batches finishing in under an hour.
    - s-013 "most batches finishing in less than 1 hour while reducing..." - *Batch processing - Claude Docs*, Anthropic, n.d.. <https://docs.claude.com/en/docs/build-with-claude/batch-processing> (accessed 2026-08-18) [T1]
    - _(confidence: high)_

[^c-031]: Anthropic's batch results are available when all messages complete or after 24 hours, whichever comes first, and batches that do not complete in that window expire.
    - s-013 "You can access batch results when all messages have compl..." - *Batch processing - Claude Docs*, Anthropic, n.d.. <https://docs.claude.com/en/docs/build-with-claude/batch-processing> (accessed 2026-08-18) [T1]
    - _(confidence: high)_

[^c-032]: OpenAI's Batch API offers the same trade in the same shape: 50 percent lower cost, higher rate limits, and a 24-hour turnaround.
    - s-012 "50% lower costs, a separate pool of significantly higher ..." - *OpenAI Batch API guide*, OpenAI, n.d.. <https://platform.openai.com/docs/guides/batch> (accessed 2026-08-18) [T1]
    - _(confidence: high)_

[^c-033]: The wall-clock cost of the cheap tier is real even inside the window: a single 300k-token generation can take over an hour.
    - s-013 "A single 300k-token generation can take over an hour to c..." - *Batch processing - Claude Docs*, Anthropic, n.d.. <https://docs.claude.com/en/docs/build-with-claude/batch-processing> (accessed 2026-08-18) [T1]
    - _(confidence: high)_

[^c-034]: Latency is sold as a purchasable service tier rather than a fixed property of a model, with priority requests prioritised over all others.
    - s-021 "The API prioritizes requests in this tier over all other ..." - *Service tiers - Claude API docs*, Anthropic, n.d.. <https://docs.claude.com/en/api/service-tiers> (accessed 2026-08-18) [T1]
    - _(confidence: high)_

[^c-035]: That purchasable priority tier is being withdrawn rather than expanded: Anthropic states Priority Tier capacity commitments are no longer available for purchase.
    - s-021 "Priority Tier capacity commitments are no longer availabl..." - *Service tiers - Claude API docs*, Anthropic, n.d.. <https://docs.claude.com/en/api/service-tiers> (accessed 2026-08-18) [T1]
    - _(confidence: high)_

[^c-036]: Agentic workloads multiply the number of sequential inference calls per task: an office-work trace averages about 41 turns.
    - s-008 "The office work use case averages about 41 turns per trace" - *Benchmarking Inference Engines on Agentic Workloads*, Applied Compute, n.d.. <https://www.appliedcompute.com/research/inference-benchmark> (accessed 2026-08-18) [T3]
    - _(confidence: moderate)_

[^c-037]: Agentic traffic is heavy-tailed across turns, output length and tool latency, which is why single-turn benchmarks do not predict agentic performance.
    - s-008 "Most attributes have heavy tails, especially number of tu..." - *Benchmarking Inference Engines on Agentic Workloads*, Applied Compute, n.d.. <https://www.appliedcompute.com/research/inference-benchmark> (accessed 2026-08-18) [T3]
    - _(confidence: moderate)_

[^c-038]: The most-repeated evidence that latency costs revenue is Amazon's finding that every 100ms of delay cost 1 percent in sales - an e-commerce page-load result recycled into AI latency marketing rather than measured on LLM inference.
    - s-017 "Amazon once found that every 100 milliseconds of delay co..." - *E-commerce Latency: 100ms = 1% Revenue Lost [Data + Playbook]*, Alhena AI, n.d.. <https://alhena.ai/blog/ai-latency-ecommerce-cx-speed-conversions/> (accessed 2026-08-18) [T4]
    - _(stance: contradicted; confidence: low; contradicted by s-017)_

[^c-039]: Code-QA agentic traces range widest of the three profiles, with tool-call turns reaching 200.
    - s-008 "The code QA use case has the most range with the number o..." - *Benchmarking Inference Engines on Agentic Workloads*, Applied Compute, n.d.. <https://www.appliedcompute.com/research/inference-benchmark> (accessed 2026-08-18) [T3]
    - _(confidence: moderate)_

[^c-040]: Managing AI spend has become near-universal in FinOps practice: 98 percent of 1,192 State of FinOps respondents manage it, up from 31 percent two years earlier.
    - s-018 "Almost all the 1,192 survey respondents (98%) are managin..." - *State of FinOps Survey: AI Value and Skills Top Priorities as FinOps Matures Across Technology Value*, Linux Foundation / FinOps Foundation, n.d.. <https://www.linuxfoundation.org/press/state-of-finops-survey-ai-value-and-skills-top-priorities-as-finops-matures-across-technology-value-98-manage-ai-90-saas-64-licensing-48-data-center-1> (accessed 2026-08-18) [T2]
    - _(confidence: high)_

[^c-041]: The priorities that displaced pure cost optimisation in that survey are governance, forecasting, organisational alignment and expanding technology coverage.
    - s-018 "more respondents now prioritize governance, forecasting, ..." - *State of FinOps Survey: AI Value and Skills Top Priorities as FinOps Matures Across Technology Value*, Linux Foundation / FinOps Foundation, n.d.. <https://www.linuxfoundation.org/press/state-of-finops-survey-ai-value-and-skills-top-priorities-as-finops-matures-across-technology-value-98-manage-ai-90-saas-64-licensing-48-data-center-1> (accessed 2026-08-18) [T2]
    - _(confidence: moderate)_

[^c-042]: Mature FinOps practice is described as moving toward unit economics and influencing technology selection, which is the governance surface a speed criterion would have to occupy.
    - s-018 "Mature practices increasingly focus on unit economics, AI..." - *State of FinOps Survey: AI Value and Skills Top Priorities as FinOps Matures Across Technology Value*, Linux Foundation / FinOps Foundation, n.d.. <https://www.linuxfoundation.org/press/state-of-finops-survey-ai-value-and-skills-top-priorities-as-finops-matures-across-technology-value-98-manage-ai-90-saas-64-licensing-48-data-center-1> (accessed 2026-08-18) [T2]
    - _(confidence: moderate)_

[^c-043]: Latency is being standardised where benchmarks are governed: MLPerf Inference v5.1 expanded an interactive scenario testing performance under lower latency constraints, explicitly motivated by agentic applications.
    - s-005 "tests performance under lower latency constraints as requ..." - *MLCommons Releases New MLPerf Inference v5.1 Benchmark Results*, MLCommons, 2025-09-09. <https://mlcommons.org/2025/09/mlperf-inference-v5-1-results/> (accessed 2026-08-18) [T2]
    - _(confidence: high)_

[^c-044]: That benchmark round drew record industry participation, with 27 submitting organisations.
    - s-005 "sets a record for the number of participants submitting s..." - *MLCommons Releases New MLPerf Inference v5.1 Benchmark Results*, MLCommons, 2025-09-09. <https://mlcommons.org/2025/09/mlperf-inference-v5-1-results/> (accessed 2026-08-18) [T2]
    - _(confidence: high)_

[^c-050]: A controlled experiment published at CHI 2026 tested LLM response latency directly, varying time-to-first-token across 2, 9 and 20 seconds over two knowledge-task types with 240 participants.
    - s-024 "between-subjects experiment with 240 participants" - *The Impact of Response Latency and Task Type on Human-LLM Interaction and Perception*, arXiv / CHI 2026, n.d.. <https://arxiv.org/html/2604.06183> (accessed 2026-08-18) [T2]
    - _(confidence: high)_

[^c-051]: In that experiment, user interaction behaviour was robust to latency: prompting, copying and refreshing rates did not shift across the 2s, 9s and 20s conditions, while task type did drive behaviour.
    - s-024 "user interaction behaviors were robust to latency" - *The Impact of Response Latency and Task Type on Human-LLM Interaction and Perception*, arXiv / CHI 2026, n.d.. <https://arxiv.org/html/2604.06183> (accessed 2026-08-18) [T2]
    - _(confidence: high)_

[^c-052]: The same experiment found the effect of speed ran opposite to the usual assumption: participants served in 2 seconds rated outputs as less thoughtful and less useful than participants who waited 9 to 20 seconds.
    - s-024 "participants who experienced 2-second latencies rated the..." - *The Impact of Response Latency and Task Type on Human-LLM Interaction and Perception*, arXiv / CHI 2026, n.d.. <https://arxiv.org/html/2604.06183> (accessed 2026-08-18) [T2]
    - _(stance: mixed; confidence: high; contradicted by s-017)_

[^c-053]: The authors conclude that latency is not simply a cost to be minimised but a tunable design variable.
    - s-024 "latency is not simply a cost to reduce but a tunable desi..." - *The Impact of Response Latency and Task Type on Human-LLM Interaction and Perception*, arXiv / CHI 2026, n.d.. <https://arxiv.org/html/2604.06183> (accessed 2026-08-18) [T2]
    - _(confidence: high)_

[^c-060]: Latency is a contractual term, not only an engineering metric: Microsoft's deployment-type table carries a Latency Service Level Agreement column, and Priority processing carries a defined latency target per model.
    - s-027 "Priority processing Pay per token (priority tier rate) De..." - *Azure OpenAI provisioned throughput concepts (docs source)*, Microsoft, n.d.. <https://github.com/MicrosoftDocs/azure-ai-docs/blob/main/articles/foundry/openai/includes/concepts-provisioned-throughput-1.md> (accessed 2026-08-18) [T1]
    - _(confidence: high)_

[^c-061]: That same table shows the latency guarantee is what buyers give up on the cheap tiers: Standard deployments carry no latency SLA at all.
    - s-027 "Standard Pay per token None Balanced workloads" - *Azure OpenAI provisioned throughput concepts (docs source)*, Microsoft, n.d.. <https://github.com/MicrosoftDocs/azure-ai-docs/blob/main/articles/foundry/openai/includes/concepts-provisioned-throughput-1.md> (accessed 2026-08-18) [T1]
    - _(confidence: high)_

[^c-070]: A measured diffusion interval exists after all: between December 2025 and January 2026, AMD's inference software stack improved by up to 2x in performance on the same hardware.
    - s-028 "From December 2025 to January 2026, AMD's software was im..." - *InferenceX v2: NVIDIA Blackwell Vs AMD vs Hopper (formerly InferenceMAX)*, SemiAnalysis, n.d.. <https://newsletter.semianalysis.com/p/inferencex-v2-nvidia-blackwell-vs> (accessed 2026-08-18) [T2]
    - _(confidence: moderate)_

[^c-071]: Over a slightly longer window the same benchmark recorded AMD nearly doubling throughput at equal interactivity in under two months, on unchanged silicon.
    - s-028 "AMD has almost doubled the amount of throughput in the sp..." - *InferenceX v2: NVIDIA Blackwell Vs AMD vs Hopper (formerly InferenceMAX)*, SemiAnalysis, n.d.. <https://newsletter.semianalysis.com/p/inferencex-v2-nvidia-blackwell-vs> (accessed 2026-08-18) [T2]
    - _(confidence: moderate)_

[^c-072]: A second, independently-run benchmark reaches the same structural finding as the first: the fundamental trade-off in LLM inference is throughput against latency, measured as a curve rather than a single number.
    - s-028 "The fundamental tradeoff with LLM inference is throughput..." - *InferenceX v2: NVIDIA Blackwell Vs AMD vs Hopper (formerly InferenceMAX)*, SemiAnalysis, n.d.. <https://newsletter.semianalysis.com/p/inferencex-v2-nvidia-blackwell-vs> (accessed 2026-08-18) [T2]
    - _(confidence: high)_

[^c-080]: OpenAI's own published price list confirms the reported July 2026 figures: gpt-5.6-luna at $0.20 per million input tokens and $1.20 per million output tokens.
    - s-032 "gpt-5.6-luna | $0.20 | $0.02 | $0.25 | $1.20" - *OpenAI API pricing (markdown)*, OpenAI, n.d.. <https://platform.openai.com/docs/pricing.md> (accessed 2026-08-18) [T1]
    - _(confidence: high)_

[^c-100]: The premise that cost is a settled axis does not hold: per-token price is still where frontier vendors compete publicly, with cuts of 20 and 80 percent landing three weeks after a model launch under pressure from cost-sensitive buyers.
    - s-016 "The company is facing pressure to cater to a more cost-se..." - *OpenAI cuts prices for two of its GPT-5.6 AI models as companies grow sensitive to costs*, CNBC, 2026-07-30. <https://www.cnbc.com/2026/07/30/open-ai-price-cut-gpt.html> (accessed 2026-08-18) [T3]
    - s-016 "reducing the price of Terra by 20% to $2 per million inpu..." - *OpenAI cuts prices for two of its GPT-5.6 AI models as companies grow sensitive to costs*, CNBC, 2026-07-30. <https://www.cnbc.com/2026/07/30/open-ai-price-cut-gpt.html> (accessed 2026-08-18) [T3]
    - _(confidence: moderate)_

[^c-101]: For an open-weight model that many providers serve, the cross-provider speed spread is roughly 5x to 8x on identical weights - far above the 2x threshold below which a speed advantage would be strategically uninteresting.
    - s-014 "Cerebras Gemma 4 31B 131k Open 30 $0.24 1,357 0.79 2.43" - *Artificial Analysis: LLM API Provider Leaderboard*, Artificial Analysis, n.d.. <https://artificialanalysis.ai/leaderboards/providers> (accessed 2026-08-18) [T2]
    - s-014 "SambaNova Gemma 4 31B 131k Open 30 $0.10 201 2.37 13.49 8.63" - *Artificial Analysis: LLM API Provider Leaderboard*, Artificial Analysis, n.d.. <https://artificialanalysis.ai/leaderboards/providers> (accessed 2026-08-18) [T2]
    - _(confidence: moderate)_

[^c-102]: For a proprietary frontier model the same spread nearly disappears - about 1.4x in end-to-end response time across three resellers - so the size of any available speed advantage depends on whether the buyer can choose who serves the weights.
    - s-014 "Amazon Bedrock Claude Opus 5 (max) 1M Proprietary 63 $2.3..." - *Artificial Analysis: LLM API Provider Leaderboard*, Artificial Analysis, n.d.. <https://artificialanalysis.ai/leaderboards/providers> (accessed 2026-08-18) [T2]
    - _(confidence: low)_

[^c-103]: A speed lead built in software is not durable: the techniques that once distinguished a fast stack are now standard open-source features, and the frontier moves in releases days apart, which is faster than any procurement or re-evaluation cycle.
    - s-006 "Advanced features: chunked prefill, prefix caching, guide..." - *Inside vLLM: Anatomy of a High-Throughput LLM Inference System*, vLLM project, 2025-09-05. <https://vllm.ai/blog/2025-09-05-anatomy-of-vllm> (accessed 2026-08-18) [T2]
    - s-022 "increase the Pareto frontier of performance in incrementa..." - *InferenceMAX: Open Source Inference Benchmarking*, SemiAnalysis, n.d.. <https://newsletter.semianalysis.com/p/inferencemax-open-source-inference> (accessed 2026-08-18) [T2]
    - _(confidence: high)_

[^c-104]: What persists is not speed but position: latency and throughput are opposite ends of one batch-size curve, and where a provider sits on it is a commercial decision rather than a capability an incumbent can be locked out of.
    - s-004 "There is no free lunch, you cannot have both minimum late..." - *The Economics of LLM Inference: Batch Sizes, Latency Tiers, and Why Model Labs Have an Advantage*, mlechner (Substack), n.d.. <https://mlechner.substack.com/p/the-economics-of-llm-inference-batch> (accessed 2026-08-18) [T3]
    - s-004 "Where a provider sets their batch size is a business deci..." - *The Economics of LLM Inference: Batch Sizes, Latency Tiers, and Why Model Labs Have an Advantage*, mlechner (Substack), n.d.. <https://mlechner.substack.com/p/the-economics-of-llm-inference-batch> (accessed 2026-08-18) [T3]
    - _(confidence: moderate)_

[^c-105]: The 'same budget, very different wall-clock' effect is real and documented, but as a purchasable tier rather than an earned advantage: identical work runs at half price if the buyer accepts a 24-hour window instead of an interactive response.
    - s-013 "most batches finishing in less than 1 hour while reducing..." - *Batch processing - Claude Docs*, Anthropic, n.d.. <https://docs.claude.com/en/docs/build-with-claude/batch-processing> (accessed 2026-08-18) [T1]
    - s-012 "50% lower costs, a separate pool of significantly higher ..." - *OpenAI Batch API guide*, OpenAI, n.d.. <https://platform.openai.com/docs/guides/batch> (accessed 2026-08-18) [T1]
    - _(confidence: high)_

[^c-106]: The business case for interactive speed rests on weaker evidence than the case for throughput: the most-cited number is an e-commerce page-load result recycled into AI latency marketing, not a measurement of LLM latency.
    - s-017 "Amazon once found that every 100 milliseconds of delay co..." - *E-commerce Latency: 100ms = 1% Revenue Lost [Data + Playbook]*, Alhena AI, n.d.. <https://alhena.ai/blog/ai-latency-ecommerce-cx-speed-conversions/> (accessed 2026-08-18) [T4]
    - _(stance: contradicted; confidence: low; contradicted by s-017)_

[^c-107]: Speed is being institutionalised at the benchmark layer even if not yet at the governance layer: MLPerf added latency-constrained interactive scenarios explicitly for agentic applications, drawing record participation.
    - s-005 "tests performance under lower latency constraints as requ..." - *MLCommons Releases New MLPerf Inference v5.1 Benchmark Results*, MLCommons, 2025-09-09. <https://mlcommons.org/2025/09/mlperf-inference-v5-1-results/> (accessed 2026-08-18) [T2]
    - s-005 "sets a record for the number of participants submitting s..." - *MLCommons Releases New MLPerf Inference v5.1 Benchmark Results*, MLCommons, 2025-09-09. <https://mlcommons.org/2025/09/mlperf-inference-v5-1-results/> (accessed 2026-08-18) [T2]
    - _(confidence: moderate)_

[^c-108]: Agentic workloads are the mechanism that converts per-token speed into wall-clock outcome, because they multiply sequential model calls per task - tens of turns typically, up to 200 - with heavy tails at every step.
    - s-008 "The office work use case averages about 41 turns per trace" - *Benchmarking Inference Engines on Agentic Workloads*, Applied Compute, n.d.. <https://www.appliedcompute.com/research/inference-benchmark> (accessed 2026-08-18) [T3]
    - s-008 "Most attributes have heavy tails, especially number of tu..." - *Benchmarking Inference Engines on Agentic Workloads*, Applied Compute, n.d.. <https://www.appliedcompute.com/research/inference-benchmark> (accessed 2026-08-18) [T3]
    - _(confidence: moderate)_

[^c-109]: 'Speed is the moat' is, in its most prominent published use, a hardware vendor's marketing line rather than an analytic finding - which is a reason to test the claim, not to dismiss it.
    - s-022 "Speed is the moat. ... Anush Elangovan, VP GPU Software, AMD" - *InferenceMAX: Open Source Inference Benchmarking*, SemiAnalysis, n.d.. <https://newsletter.semianalysis.com/p/inferencemax-open-source-inference> (accessed 2026-08-18) [T2]
    - _(confidence: high)_

[^c-110]: The interactive-latency case is now evidenced, and the evidence cuts against the thesis rather than for it: within the 2-20 second band, faster responses changed no user behaviour and were judged lower quality.
    - s-024 "user interaction behaviors were robust to latency" - *The Impact of Response Latency and Task Type on Human-LLM Interaction and Perception*, arXiv / CHI 2026, n.d.. <https://arxiv.org/html/2604.06183> (accessed 2026-08-18) [T2]
    - s-024 "participants who experienced 2-second latencies rated the..." - *The Impact of Response Latency and Task Type on Human-LLM Interaction and Perception*, arXiv / CHI 2026, n.d.. <https://arxiv.org/html/2604.06183> (accessed 2026-08-18) [T2]
    - _(stance: mixed; confidence: high; contradicted by s-017)_

[^c-111]: The claim that leaders do not treat speed as a governed axis is false at the platform layer: latency is already sold as a per-model contractual target, and the absence of that guarantee is what distinguishes the cheaper tiers.
    - s-027 "Priority processing Pay per token (priority tier rate) De..." - *Azure OpenAI provisioned throughput concepts (docs source)*, Microsoft, n.d.. <https://github.com/MicrosoftDocs/azure-ai-docs/blob/main/articles/foundry/openai/includes/concepts-provisioned-throughput-1.md> (accessed 2026-08-18) [T1]
    - s-027 "Standard Pay per token None Balanced workloads" - *Azure OpenAI provisioned throughput concepts (docs source)*, Microsoft, n.d.. <https://github.com/MicrosoftDocs/azure-ai-docs/blob/main/articles/foundry/openai/includes/concepts-provisioned-throughput-1.md> (accessed 2026-08-18) [T1]
    - _(confidence: high)_

[^c-112]: The erosion of a speed lead can now be given a number rather than a characterisation: roughly a doubling of throughput from software alone within one to two months, on fixed hardware.
    - s-028 "From December 2025 to January 2026, AMD's software was im..." - *InferenceX v2: NVIDIA Blackwell Vs AMD vs Hopper (formerly InferenceMAX)*, SemiAnalysis, n.d.. <https://newsletter.semianalysis.com/p/inferencex-v2-nvidia-blackwell-vs> (accessed 2026-08-18) [T2]
    - s-028 "AMD has almost doubled the amount of throughput in the sp..." - *InferenceX v2: NVIDIA Blackwell Vs AMD vs Hopper (formerly InferenceMAX)*, SemiAnalysis, n.d.. <https://newsletter.semianalysis.com/p/inferencex-v2-nvidia-blackwell-vs> (accessed 2026-08-18) [T2]
    - _(confidence: moderate)_

