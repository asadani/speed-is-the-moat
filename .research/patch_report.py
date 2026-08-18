# -*- coding: utf-8 -*-
"""Revise report.md for the gap-fixing pass. Fails loudly if any anchor is missing."""
import io

p = ".research/report.md"
s = io.open(p, encoding="utf-8").read().split("\n## References")[0].rstrip() + "\n"

edits = []


def sub(old, new):
    edits.append((old, new))


# --- headline answer: sharpened by the new evidence -------------------------
sub("""**Answer, in one line.** Speed is not a moat, but the thing the phrase is reaching
for is real: the *dispersion* in speed is large, persistent, and mostly unmanaged —
so the durable advantage is not being fast, it is being organised to keep
re-choosing where you sit.""",
    """**Answer, in one line.** Speed is not a moat. The dispersion in speed is large and
persistent, but a lead within it now has a measured half-life of one to two
months[^c-112], latency is already sold as a contractual tier rather than won[^c-111],
and the one controlled experiment on interactive latency found faster responses
changed no behaviour and were judged *worse*[^c-110]. What is left worth organising
around is placement, not pace.""")

# --- SQ1: first-party pricing now closes the T1 gap -------------------------
sub("""capability and efficiency together[^c-006]. Cost is understood as a practice and
unsettled as a competitive axis[^c-100].""",
    """capability and efficiency together[^c-006]; OpenAI's own published price list
confirms those figures at $0.20 and $1.20 per million tokens for the cheapest
tier[^c-080]. Cost is understood as a practice and unsettled as a competitive
axis[^c-100].""")

# --- SQ3: the erosion interval now has a number -----------------------------
sub("""A lead that diffuses on a days-to-weeks cadence is not a moat. It erodes faster than
any procurement or architecture review can re-evaluate it[^c-103]. What persists is
not speed but position on a curve that is bought rather than won[^c-104].""",
    """A lead that diffuses on a days-to-weeks cadence is not a moat. It erodes faster than
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
throughput-against-latency curve rather than a single number[^c-072].""")

# --- SQ4: the folklore paragraph is replaced by a real experiment -----------
sub("""**One caution on the business case.** The most-repeated evidence that latency costs
revenue is Amazon's finding that every 100ms of delay cost 1% in sales — but this is
contested rather than settled: it is an e-commerce page-load result recycled into AI
latency marketing, not a measurement of LLM inference[^c-038][^c-106]. This corpus
contains no independent study linking LLM response latency to a business outcome.
The throughput case is well-evidenced; the interactive-latency case is not.""",
    """### The interactive case, now that there is real evidence

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
actively contested by the only controlled study in this corpus.""")

# --- SQ5: no longer unresolved ---------------------------------------------
sub("""## 5. Is anyone governing this? Probably not — but I could not prove it""",
    """## 5. Speed *is* governed — at the platform layer, not the enterprise one""")

sub("""Latency and throughput do not appear in that list. **That is absence-of-mention in
one summary of one survey, not a measured finding**, and it should not be reported
as evidence that leaders ignore speed. The brief's claim that few leaders treat
speed as a long-horizon axis is consistent with everything found here and was not
verified. Testing it properly means looking at procurement contracts for latency
SLOs, which this project did not do.""",
    """Latency and throughput do not appear in that list. That is absence-of-mention in one
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
That would need procurement contracts this project did not obtain.""")

for old, new in edits:
    if old not in s:
        raise SystemExit("ANCHOR NOT FOUND:\n%s" % old[:160])
    s = s.replace(old, new, 1)

io.open(p, "w", encoding="utf-8").write(s)
print("applied %d edits" % len(edits))
