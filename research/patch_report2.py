# -*- coding: utf-8 -*-
"""Second revision pass: section 6 and the limitations, after the gap-fixing round."""
import io

p = ".research/report.md"
s = io.open(p, encoding="utf-8").read().split("\n## References")[0].rstrip() + "\n"

edits = []


def sub(old, new):
    edits.append((old, new))


sub("""**It deserves a standing owner — but not the one the thesis implies.** Not a team
chasing the fastest provider, because that lead diffuses in days[^c-103] and the
chase never ends. A function that owns *placement*: which workloads sit on which
tier, re-examined on a cadence matched to a frontier that moves in
days[^c-020], not to a quarterly review.

Three things follow concretely:

1. **Classify workloads by tier before comparing vendors.** The batch/standard/
   priority split is where the largest wall-clock difference for a fixed budget
   actually lives[^c-030][^c-032], and it is available today without changing
   provider.
2. **Treat the open-weight/proprietary distinction as the gate.** Speed shopping
   pays 5–8x on open weights[^c-101] and roughly nothing on proprietary
   models[^c-102]. Model-class choice determines whether a speed programme has
   anything to work with.
3. **Budget for re-evaluation, not for a winner.** Any benchmark you run goes stale
   quickly[^c-021]; the sustainable version of this is a recurring re-measurement
   against your own workload, not a vendor selection defended for a year.""",
    """**It deserves an owner, but a procurement one rather than a research one.** Not a
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
   users may not reward.""")

sub("""## Limitations

- **Single-source dependency.** All cross-provider speed figures (§2) come from one
  point-in-time snapshot of one benchmarker. This is the load-bearing wall of the
  report and the most likely thing to be wrong.
- **The erosion interval is qualitative.** The brief asked how long a speed
  optimisation takes to go from proprietary to commodity. The evidence shows that it
  does[^c-024] and that the cadence is fast[^c-020], but no source in this corpus
  gives a measured interval.
- **No first-party OpenAI pricing source.** OpenAI's own price-cut announcement
  returned HTTP 403 to both capture routes, so the July 2026 figures rest on CNBC's
  reporting rather than primary disclosure.
- **One registered source captured no usable text.** A GMI Cloud article intended as
  disconfirming evidence extracted only page navigation. No claim binds to it; its
  argument was re-sourced elsewhere.
- **SQ5 is unresolved**, not answered. See §5.
- **No independent auditor pass.** Claims were bound by exact quote and mechanically
  quote-checked against snapshots, but the suite's independent claim-auditor agent
  was not dispatched, so no fresh-context reviewer confirmed that the quotes mean
  what the claims need them to mean.
- **Out of scope by design:** organisational execution speed, training speed, model
  quality rankings, GPU supply-chain economics, self-hosted serving, and any
  specific vendor recommendation.""",
    """## Limitations

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
that captured only navigation was re-captured successfully.""")

sub("""The conclusion flips toward "speed is a moat" if the custom-silicon tier proves
unreachable by GPU batch tuning over multiple model generations[^c-028] rather than
being a temporary and expensive corner. It flips further away if the open-weight
spread[^c-101] turns out to be an artefact of one benchmarker's test geography or
prompt mix[^c-017].""",
    """The conclusion flips toward "speed is a moat" if the custom-silicon tier proves
unreachable by GPU batch tuning over multiple model generations[^c-028] rather than
being a temporary and expensive corner — that is the one structural argument this
corpus cannot close. It flips further away if the open-weight spread[^c-101] turns
out to be an artefact of one benchmarker's test geography or prompt mix[^c-017].

The finding most likely to be overturned by better evidence is the interactive-
latency reversal[^c-052]. It is a single experiment, and a second study finding the
opposite would restore the conventional view. The finding least likely to be
overturned is the erosion rate[^c-112]: two independent benchmarks, measuring
different layers, both report software gains arriving faster than procurement can
respond.""")

for old, new in edits:
    if old not in s:
        raise SystemExit("ANCHOR NOT FOUND:\n%s" % old[:200])
    s = s.replace(old, new, 1)

io.open(p, "w", encoding="utf-8").write(s)
print("applied %d edits" % len(edits))
