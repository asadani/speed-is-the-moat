# Verification report

**Verdict: PASS**

| | |
|---|---|
| Report | `research/report.md` |
| Sources in ledger | 33 |
| Claims in ledger | 65 |
| Claims cited by the report | 65 |
| Hard failures | 0 |
| Warnings | 28 |

## Hard failures

None. Every cited claim resolves to a ledger row, binds an existing source,
and locates its evidence in a snapshot whose hash still matches.

## Warnings

Advisory. These do not block the report.

### W2 -- Assertion with no marker

- **report.md:3** -- unbound assertion (asserts something about a named entity)
  **Question.** Now that per-token cost is broadly understood, does inference speed constitute a durable differentiator for LLM systems — o...
- **report.md:7** -- unbound assertion (asserts something about a named entity)
  **Answer, in one line.** Speed is not a moat.
- **report.md:21** -- unbound assertion (asserts something about a named entity)
  Cost per unit of capability is collapsing on every measure available.
- **report.md:62** -- unbound assertion (contains a figure)
  The brief set 2x as the floor below which a speed advantage is strategically uninteresting.
- **report.md:69** -- unbound assertion (contains a figure)
  If you are on open weights, there is 5–8x.
- **report.md:74** -- unbound assertion (asserts something about a named entity)
  *Confidence: moderate on the open-weight figures, low on the proprietary comparison.* Every cross-provider number above comes from a sing...
- **report.md:108** -- unbound assertion (asserts 'strongest')
  The custom-silicon argument is the strongest case against this report's conclusion, and it cannot be settled here — the only source makin...
- **report.md:117** -- unbound assertion (asserts 'largest')
  When the two largest GPU vendors describe the same results, one says speed and the other says efficiency — which tells you the framing is...
- **report.md:126** -- unbound assertion (asserts 'best')
  This part of the thesis is the best-evidenced, and it is documented as a product tier rather than as an achievement.
- **report.md:147** -- unbound assertion (asserts something about a named entity)
  Where speed genuinely compounds is agentic work.
- **report.md:185** -- unbound assertion (asserts something about a named entity)
  Latency and throughput do not appear in that list.
- **report.md:188** -- unbound assertion (asserts something about a named entity)
  Latency is not an ungoverned engineering metric that leaders have failed to notice.
- **report.md:197** -- unbound assertion (asserts something about a named entity)
  Speed is not an unclaimed strategic axis waiting for someone to own it; it is a solved commercial problem at the platform layer that many...
- **report.md:203** -- unbound assertion (asserts something about a named entity)
  What remains genuinely unverified is the *enterprise* layer: whether buying organisations actually set internal latency SLOs and hold ven...
- **report.md:224** -- unbound assertion (asserts something about a named entity)
  Four things follow concretely:
- **report.md:230** -- unbound assertion (asserts something about a named entity)
  Model-class choice determines whether a speed programme has anything to work with.
- **report.md:248** -- unbound assertion (asserts something about a named entity)
  Four were closed by further gathering; what follows is what actually remains.
- **report.md:251** -- unbound assertion (contains a figure)
  **Still single-source at the API-provider layer.** Every cross-provider figure in §2 comes from one point-in-time snapshot of one benchma...
- **report.md:257** -- unbound assertion (asserts 'best')
  It is the best evidence in this corpus and it does not settle voice, real-time, or long-horizon agentic work.
- **report.md:267** -- unbound assertion (asserts something about a named entity)
  **No independent auditor pass.** Claims were bound by exact quote and mechanically quote-checked against snapshots, but no fresh-context ...
- **report.md:270** -- unbound assertion (asserts something about a named entity)
  **Out of scope by design:** organisational execution speed, training speed, model quality rankings, GPU supply-chain economics, self-host...

### W3 -- Figure in a cited sentence is not in the claim

- **report.md:21** -- the figure 16 does not appear in [^c-003] or its quoted evidence
  They are measuring different things — Epoch regresses across capability milestones on six benchmarks, a16z tracks a single MMLU-equivalence
- **report.md:50** -- the figure 5.6 does not appear in [^c-011] or its quoted evidence
  Dividing those figures gives 6.8x on generation rate and 5.6x on wall clock — and the slower endpoint was the cheaper one, at $0.10 against
- **report.md:251** -- the figure 6.8 does not appear in [^c-070], [^c-072] or its quoted evidence
  The corroborating benchmark[^c-070][^c-072] measures *hardware and serving stacks*, not API endpoints, so it confirms the shape of the findi
- **report.md:251** -- the figure 4 does not appear in [^c-070], [^c-072] or its quoted evidence
  The corroborating benchmark[^c-070][^c-072] measures *hardware and serving stacks*, not API endpoints, so it confirms the shape of the findi
- **report.md:251** -- the figure 31 does not appear in [^c-070], [^c-072] or its quoted evidence
  The corroborating benchmark[^c-070][^c-072] measures *hardware and serving stacks*, not API endpoints, so it confirms the shape of the findi
- **report.md:260** -- the figure 5 does not appear in [^c-060] or its quoted evidence
  **The enterprise governance layer is still unverified.** §5 establishes that platforms sell latency contractually[^c-060].
- **report.md:264** -- the figure 3 does not appear in [^c-070], [^c-071] or its quoted evidence
  **No measured diffusion interval for a named technique.** §3 now gives a rate of improvement[^c-070][^c-071], which is not the same as timin

---

Rules are defined in `docs/LEDGER-SPEC.md` section 5.
