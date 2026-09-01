# P140 narrative report

## Research question

What exact stochastic structure survives when majority is used not to update
a fixed population, but to replace a uniformly selected adjacent triple by one
bit and thereby shrink the carrier?

## Mechanism found

The full binary-word chain is large, but a word with exactly two runs stays in
the two-run family. At state `(a,b)`, every possible current window belongs to
one of three classes, with multiplicities determined only by the two block
sizes. This produces an all-parameter two-coordinate Markov reduction.

The absorption split is unusually simple: the chance of terminal one is
`(b-1)/(a+b-2)`. Since the available-window counts depend only on current
length, every position history has the same probability, converting the
absorption law into exact history enumeration. Marking heterogeneous windows
then refines the count to a polynomial recurrence; its linear coefficient has
a reciprocal closed form.

## Continuous-time payoff

Rate-one clocks on current windows give deterministic total rates
`n-2,n-4,...,1`. Equal-rate races split the winning index from the holding
time. Iterating that split proves independence from the entire embedded
history, not only from the endpoint. At the length-one boundary there is no
clock and `tau_1=0` almost surely. For `n=2m+1>=3`, the elapsed time is an
odd-rate hypoexponential sum and exponentiating it yields an exact
`Beta(1/2,m)` variable. Beta--gamma coupling then gives a rate-one Gamma limit
along `m -> infinity`.

## Round-A boundary repair

Hostile review A found one scope defect and no failure of the substantive
kernel, marked-history, or independence results. The original clock corollary
allowed `n=1` implicitly while writing the invalid symbol `Beta(1/2,0)`. The
repaired manuscript now handles `tau_1=0` separately, retains the empty-
product and empty-sum transform boundaries, and restricts the Beta identity to
`m>=1`. No verifier or nonboundary formula changed.

## Boundary and novelty statement

Majority-rule models on fixed spin systems and majority automata are owned
background. The local Boolean gate, consensus vocabulary, exponential-race
facts, and beta--gamma algebra receive no credit. The internal residual is the
joint exact atlas for this shrinking two-run carrier. A targeted literature
search found no direct owner printing that atlas, but the result remains
`HOLD_EXTERNAL`; a bounded non-hit is not novelty clearance.

## What the paper deliberately does not claim

- no general formula for arbitrary multi-run initial words;
- no random discrete stopping count (the count is fixed);
- no equivalence with a ternary-tree model that forgets current positions;
- no new exponential-race, Beta, or Gamma-limit principle;
- no external priority, authorship, posting, or submission authorization.
