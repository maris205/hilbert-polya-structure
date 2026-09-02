# Narrative report — P152

**Status:** `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.

## The dynamics in plain language

A triangular book has `r` triangles sharing one physical edge.  Every edge is
signed, and a page is imbalanced when the product of its three signs is
negative.  At an active epoch, an imbalanced page and then one of its three
edges are chosen uniformly, and that edge is flipped.  A private edge repairs
only the chosen page; the common spine toggles every page simultaneously.

That geometry creates the exact count chain

```text
k -> k-1 with probability 2/3,
k -> r-k with probability 1/3.
```

The reflection is the useful signal.  Marking time by `z` and spine flips by
`u` produces a Bellman system with the reflected index `r-k`.  Pairing the
equation with its reflection removes that index and leaves a constant-
coefficient second-order recurrence.  Its solution is a Chebyshev-rational
joint transform for every book size and starting count.

## Why there are several theorem axes

The bivariate transform gives the complete joint law in rational form.  Two
different specializations then expose interpretable coarse information:

- differentiating in the time mark yields the quadratic mean
  `k(r+2-k)/2`, with sharp minima and maxima over the starting count;
- setting the spine mark to `-1` gives
  `P(J odd)=k/(r+2)`.

Together, the exact mean and parity probability recover both the book size
and the initial imbalance count, subject to an explicit integer feasibility
test.  For arbitrary candidate data, `m>0` and `0<q<1` are checked before the
square root is formed.  Neither statistic alone identifies the pair: the
manuscript keeps one collision for each single statistic.  A private-choice
block gives a separate pathwise absorption certificate and exponential tail.

## Ownership boundary

The update rule is not claimed.  Antal--Krapivsky--Redner own local triad
dynamics and its `p=1/3` equiprobable-edge specialization; Istrate owns the
same probabilistic kernel on general graphs and its triadic-dual/XOR encoding;
Istrate--Bonchis--Marin subtract generic hypergraph particle-system and drift
language.  Sehrawat--Bhattacharjya own the signed-book carrier and its static
switching-class count.  Generic Bellman, Markov-resolvent, Chebyshev,
tail-sum, and quadratic-concavity facts also receive zero credit.

The manuscript is therefore framed only as an exact special-carrier law for
an owned kernel.  The claim-bearing conjunction is the spine-marked
Chebyshev transform, sharp count-clock law, exact mean/parity inverse, and
boundary-complete absorption certificate.  The bounded source search is not
an ownership-completeness, novelty, or priority statement.

## Collision controls

- Unlike the killed triangular-book deletion process, the present chain
  preserves every edge and flips signs; a spine update reflects the count.
- Unlike the P145 vertex-push chain, this process is absorbing and selected
  through an active imbalanced triangle.
- Unlike P138, the XOR encoding is stochastic and is fully subtracted as
  prior framework.
- Unlike P151, the main object is a bivariate reflection/Chebyshev law, not a
  labelled-leaf first-passage continuant.
- A friendship graph shares one vertex rather than one edge; there the count
  simply decreases deterministically.

## Evidence and limits

The all-parameter result is proved symbolically.  The frozen Round-2 verifier
supplies 199,581 integer/rational checks over literal bit states, transform
vectors, means, parity laws, inverse states, extrema, and small boundaries.
It now also compares the inverse iff with 7,335 bounded exact candidates,
explicitly rejects 7,266 of them, verifies both printed scalar collisions,
sums exact private-block masses, and tests 546 finite tail inequalities.
Those checks are counterexample pressure, not proof or a source certificate.

Review A's two artifact findings closed in Round 1.  Review B's single
candidate-domain finding closed in Round 2; no Critical, Major, or Minor item
remains unresolved.

The paper treats uniform page and physical-edge choices, active update-epoch
time, a known triangular-book carrier, exact coarse observations, and recovery
only of `(r,k)`.  It does not treat noisy inversion, nonuniform kernels,
all-triad physical time, arbitrary graphs, full sign-state recovery, or
friendship/windmill carriers.
