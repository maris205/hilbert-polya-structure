# Narrative report — P129

## Core story

A finite set of piles occupies a path with an absorbing root. At each
discrete update, one occupied nonroot site is selected uniformly. Its pile
moves one edge toward the root and merges if the destination is occupied.
The schedule depends on the current number of piles, so the expected number
of updates is not the elapsed absorption time of a collection of independent
walkers.

The useful representation is continuous-time but the target statistic is
discrete.  On the finite accessible sites, use independent rate-one site
clocks.  Strong Markov for that finite clock vector at every effective time
makes the next occupied clock uniform among active piles, including when a
site was previously empty.  Thus the embedded chain is exactly the stated
process.  Label the initial piles in order.  An induction shows that every
current pile carries a consecutive block of initial labels and collisions
merge adjacent blocks.  Hence the number of nonroot piles equals the number
of unresolved interfaces between consecutive initial labels.  The
predictable compensator for the jump count, first on finite intervals and
then by monotone convergence, converts the expected discrete update count
into the integral of this active-pile count; Tonelli separates that integral
into expected interface lifetimes.

For an initial state

$$
S=\{0=s_0<s_1<\cdots<s_r\},
$$

the central identity is

$$
\mathbb E[T_S]=\sum_{i=1}^{r}h(s_{i-1},s_i),
$$

where `h(a,b)` is the meeting-time mean of two ordered rate-one pure-death
paths. It is determined without approximation by

$$
h(a,a)=0,\qquad h(0,b)=b,
$$

$$
h(a,b)=\frac12+\frac{h(a-1,b)+h(a,b-1)}2
\quad(0<a<b).
$$

No independence between distinct interfaces is required. Only the pairwise
marginal lifetime and linearity of the integral are used.

## Full-start consequence

For consecutive positions, a stopped fair-walk ballot calculation gives

$$
h(m-1,m)=\frac{(2m-1)!!}{(2m-2)!!}
=\frac{2m}{4^m}\binom{2m}{m}.
$$

Full occupancy therefore has

$$
\mathbb E[T_n]
=\sum_{m=1}^{n-1}\frac{(2m-1)!!}{(2m-2)!!}
=\frac{4}{3\sqrt\pi}n^{3/2}+O(n^{1/2}).
$$

The arbitrary-state identity is the main result; the full-start formula is
a corollary rather than the only theorem.

## Independent exact-law output

The total-position potential decreases strictly and gives a finite PGF
recursion. For every nonabsorbing rooted initial set,

$$
\operatorname{supp}(T_S)=\{\max S,\max S+1,\ldots,\sum_{v\in S}v\}.
$$

The lower endpoint for full occupancy has probability `1/(n-1)!`, since
the unique shortest schedule removes sites in descending order and collides
at every update. A finite pilot also suggested a simple upper-endpoint mass,
but that formula is outside the paper contract and must not appear as a
proved claim.

## Why the result is not a generic coalescing-walk restatement

Classical coalescing random walks typically attach a random-walk kernel to
each current particle and ask for elapsed coalescence time, density, or voter
consensus. Here motion is deterministic and one-way, while the discrete
scheduler is uniform among current nonroot piles. The statistic counts
embedded jumps. Generic graphical constructions, meeting/hitting-time tools,
voter duality, exact one-dimensional first-passage reductions, and
coalescence-time bounds are mature and receive zero contribution credit.

Three direct modern neighbors further narrow the claim.  Assiotis (2018)
develops coalescing flows for birth--death chains; Hitczenko and Wesołowski
(2025, Theorem 3) connect expected active-particle count to the derivative of
expected jump count in TASEP; and Śniady and Urbán (2026) treat exact
nearest-neighbor coalescence patterns with interval labels.  Those
graphical, label-block, pattern, and active-count/jump mechanisms are all
zero credit here.  The residual is only the exact arbitrary-state
embedded-update mean for this deterministic-rootward, uniform-active-pile
finite chain, together with the proved support and full-start consequences.

The external search is bounded. It found no source stating this literal
kernel together with the general interface-additive jump count, but a
bounded non-hit does not establish novelty. The paper remains
`HOLD_EXTERNAL`.

## Internal firewall

- P114 already owns synchronous deterministic rooted-forest peeling;
  root-directed monotonicity alone earns no credit.
- P117 flips odd maximal runs of labelled cyclic binary words and uses a
  boundary-parity eroder.  It has no pile carrier, rootward motion, or random
  scheduler; eroder language nevertheless earns no credit.
- P121 selects a current adjacent separator, performs product-plus-one
  coalescence, and induces a random-BST/Yule history.  P129 selects a current
  pile, permits noncoalescing moves, and counts effective updates; generic
  adjacent coalescence and random scheduling earn no credit.
- P126 owns synchronous balanced length-increasing refinement; it supplies no
  theorem here.

The residual is the exact conjunction of active-pile scheduling,
deterministic rootward motion, a set-valued collision rule, the compensator
identity for discrete update count, and the arbitrary-state interface sum.

## Evidence package

The paper-local verifier uses integer and exact rational arithmetic only. It
computes the discrete Bellman mean and the independent interface sum for all
16,383 rooted subsets through `n=14`, checks complete PGFs and support for all
2,047 rooted subsets through `n=11`, checks the pair triangle and independent
ballot sum through 80, and freezes deterministic stdout.  These checks test
boundary and implementation mistakes; they do not replace the all-parameter
proofs.
