# Speed Is the Moat

<p align="center">
  <img src="speed-is-the-moat-cover.png"
       alt="Book cover reading SPEED IS THE MOAT, subtitled a practical guide to building compounding advantage in the AI era, by Anuj Sadani, over a long-exposure photograph of light trails curving toward a city skyline at dusk."
       width="320">
</p>

<p align="center"><em><strong>The claim, as it is usually made.</strong><br>
What follows is the test of it.</em></p>

---

A verified research report testing a claim that circulates widely in AI
engineering: that now token cost is understood, **inference speed is the next
durable differentiator** — the moat.

It is not. But the instinct behind it points at something real, and the useful
version of the finding is narrower and more actionable than the slogan.

**Verdict: PASS** — 33 sources captured, 65 claims bound to exact quoted
passages, 0 hard failures.

---

## The question

> Now that per-token cost is broadly understood and largely commoditised, does
> inference speed (latency and throughput) constitute a durable differentiator
> for LLM systems, or is it a lead that erodes as fast as it is won?

## The answer in five findings

1. **The dispersion is real and large.** For an open-weight model that many
   providers serve, the spread between providers of *identical weights* is
   roughly 5–8x. For proprietary frontier models it collapses to about 1.4x. So
   the size of any available speed advantage depends on whether you can choose
   who serves the weights.

2. **A lead has a measured half-life of one to two months.** Independent
   benchmarks record inference software delivering up to 2x throughput gains on
   *unchanged silicon* inside a single month. That is shorter than most
   procurement cycles. It is the central reason "moat" is the wrong word.

3. **Latency is bought, not won.** It is already a priced contract term:
   platform documentation carries an explicit Latency SLA column, with defined
   per-model latency targets on priority and provisioned tiers, and none on the
   standard tier. Most organisations sit on the ungoverned tier by default
   rather than by decision.

4. **The interactive business case is contradicted by the only controlled
   study in the corpus.** A CHI 2026 experiment (240 participants, TTFT varied
   across 2/9/20 seconds) found user behaviour robust to latency — and found
   2-second responses rated *less* thoughtful and useful than 9–20-second ones.
   The widely-cited "100ms = 1% of sales" figure is an e-commerce page-load
   result recycled into AI latency marketing.

5. **Where speed compounds is agentic wall-clock.** Agentic traces run tens of
   sequential turns — up to 200 tool-call turns for code QA — with heavy tails
   at every step. That multiplication is how a per-token rate becomes hours.

The phrase "Speed is the moat" appears in this corpus as a quote from AMD's VP
of GPU Software in a benchmark launch post. Nvidia describes the same benchmark
results in terms of performance per dollar and per megawatt.

---

## Repository contents

| Path | What it is |
|---|---|
| `speed-is-the-moat.md` | The report. Every checkable sentence carries a `[^c-NNN]` marker resolving to the claims ledger, with a generated References section. |
| `speed-is-the-moat.html` | Self-contained essay version, styled for screen and print. |
| `SUMMARY.md` | The condensed argument and the numbers. |
| `.research/` | The verification workspace. This is the part that makes the report checkable. |
| `speed-is-the-moat-cover.png` | Cover art. |
| `LICENSE` | CC BY-NC-ND 4.0. Does not cover captured third-party sources. |

### The verification workspace

| File | Role |
|---|---|
| `.research/brief.md` | The question, sub-questions, out-of-scope list, and what would change the conclusion — written *before* gathering. |
| `.research/lens.yaml` | The source standard: what T1–T4 mean here, recency window, known traps. |
| `.research/sources.jsonl` | 33 captured sources with tier, publisher, caveats, and a sha256 of the snapshot. |
| `.research/snapshots/` | The captured bytes. A source that was not snapshotted does not exist. |
| `.research/claims.jsonl` | 65 claims, each bound to a source at a quote locator, with stance and confidence. |
| `.research/synthesis.md` | Agreement, disagreement, single-source dependencies, and gaps — including the revision pass. |
| `.research/verification-report.md` | The gate's verdict, rule by rule. |
| `.research/state.yaml` | Pipeline state and the gap ledger. |
| `.research/build_*.py`, `patch_report*.py` | The scripts that built the ledgers and the report, kept so the construction is reproducible rather than asserted. |

---

## How to check this report yourself

Every factual sentence binds to a passage in a file in this repository. Nothing
requires trusting the author, and nothing requires network access.

Pick any claim marker in the report, say `[^c-052]`, then:

```bash
# 1. read the claim, its stance and its confidence
grep '"c-052"' .research/claims.jsonl | python -m json.tool

# 2. read the passage it binds to, in the captured source
grep -n "rated the LLM" .research/snapshots/s-024.txt

# 3. confirm the snapshot has not been altered since capture
sha256sum .research/snapshots/s-024.txt
grep '"s-024"' .research/sources.jsonl
```

To re-run the whole gate:

```bash
python <research-anything>/scripts/verify_claims.py --workspace .research
```

The gate fails the report if a marker resolves to nothing, a quote does not
occur in its snapshot, a snapshot hash has changed, or a contested claim is
presented as settled.

---

## How it was built

Produced with the [`research-anything`](https://github.com/asadani/research-anything)
pipeline: **scope → gather → verify → synthesize → report**, with a verification
gate that decides whether the report ships.

It ran in two passes. The first passed the gate with six named gaps. The second
closed four of them — and two of those closures *changed the answer*, which is
recorded in `.research/synthesis.md` rather than quietly folded into the prose.
The sub-question on organisational governance moved from "unresolved" to
"answered, against the thesis."

## What this report does not establish

- The 6.8x figure between two named API providers rests on **one** benchmarker.
  The corroborating benchmark measures hardware and serving stacks, not API
  endpoints — it confirms the shape, not that specific number.
- The latency experiment covers 2–20 second time-to-first-token on knowledge
  tasks. It does not settle voice, real-time, or long-horizon agentic work.
- Whether buying organisations set and enforce *internal* latency SLOs is still
  unverified; that needs procurement contracts this project did not obtain.
- No single named optimisation was timed from paper to commodity default.
- No independent auditor pass was run over the bindings; every locator is a
  mechanical quote-match against a snapshot.

These are stated in the report as well. A limitations section that only lives in
a README is a limitations section nobody reads.

---

## A note on the cover

The cover states the thesis in its popular form — and in its *other* form. "Build,
learn, ship, repeat" is a claim about *organisational execution velocity*: how fast
a team learns and ships.

This report does not test that claim. It was ruled out of scope deliberately, and
the brief says so before any evidence was gathered:

> **Organisational execution speed.** "Ship fast as a moat" is a different thesis
> about company velocity. Named explicitly because the phrase "speed is the moat"
> is commonly used that way; this project is about *inference* speed only.

What is tested here is the narrower, more measurable claim: that **inference**
speed — latency and throughput — is a durable differentiator. On that question the
answer is no, for the reasons above.

So the cover is the proposition and the repository is the audit. They are meant to
disagree. If they agreed, one of them would not have been worth writing.
