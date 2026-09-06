# Open-fresh P167 Route-A scout

**Date:** 2026-09-03 UTC  
**Decision:** `KILL_ALL`  
**External state:** `HOLD_EXTERNAL`  
**Paper assignment:** none

## Outcome first

Three genuinely different literal systems were tested.  The only candidate
with two exact axes is `GCM`, a simultaneous greedy retile map on `2 x n`
domino tilings.  It has a sharp all-parameter temporal theorem, a complete
recurrent atlas, an every-target inverse parser, and a Padovan exceptional
fibre.  It is nevertheless killed: after encoding a tiling as a path matching,
the proof is precisely a one-sided traffic/hard-core defect migration into an
alternating recurrent core, with regular-language preimage counts.  Those are
the theorem interfaces already occupied by P90.  The change from particles to
dominoes leaves no independent stochastic, geometric, or inverse theorem.

`SRW` is a star-transposition walk on the conjugacy class of fixed-point-free
involutions, hence lies directly in owned perfect-matching rewiring and
star-factorization machinery.  `OFP` is the defining polarity involution on
flags; its `q+1` fixed flags are the classical absolute conic and all fibres
are singletons.  Neither can coexist as a paper-sized residual.

No bounded-search non-hit is used as evidence of novelty, priority, or freedom
to publish.

## 1. `GCM`: greedy-complement matching / domino-retile dynamics

Let `P_n` be the path on vertices `1,...,n`, and identify a domino tiling of a
`2 x n` rectangle with a matching `E` of `P_n`: an edge `i(i+1)` represents
the two horizontal dominoes in columns `i,i+1`, and an unmatched vertex is a
vertical domino.  Define `C_n(E)` by deleting the vertices covered by `E` and,
in each remaining interval, taking edges greedily from its left endpoint.

Equivalently, in composition notation with parts `1,2`,

```text
each old 2       -> 11,
each maximal 1^r -> 2^floor(r/2) 1^(r mod 2).
```

This is the literal tiling rule in the idea ledger; the path matching is only
an exact encoding used for proof and verification.

### 1.1 Sharp temporal theorem

Put

```text
P = {1,3,5,...} intersect {1,...,n-1}.
```

For a matching `E`, let `b(E)` be the least even starting position of an edge,
with `b(E)=infinity` if no such edge occurs.  If `b(E)=2j`, then all edges of
`E` strictly to its left lie in `P`.  On those canonical pairs the greedy
complement simply chooses the pairs omitted by `E`.  Vertex `2j-1` is left
unmatched because `2j` is covered by the bad edge, and after that edge the
greedy scan restarts no earlier than `2j+2`.  Hence

```text
b(C_n(E)) > b(E)
```

whenever the left side is finite.  There are exactly
`floor((n-1)/2)` even edge positions.  It follows that every state enters the
set of matchings contained in `P` within that many steps.

If `E subset P`, then

```text
C_n(E) = P minus E.
```

Thus these and only these states are recurrent.  There are
`2^floor(n/2)` of them.  For `n>=2` they form two-cycles; for `n=1` the empty
matching is fixed.  The bound is sharp: for

```text
E_star = {2,6,10,...} intersect {1,...,n-1},
```

a direct induction through the alternating covered and uncovered blocks gives

```text
b(C_n^t(E_star)) = 2(t+1),
0 <= t < floor((n-1)/2).
```

Therefore

```text
max_E depth(E) = floor((n-1)/2).
```

This proof covers `n=1,2` without a hidden positive-depth convention.

### 1.2 Exact one-step every-target fibres

Write a source composition uniquely as

```text
1^r0 2 1^r1 2 ... 2 1^rk
```

and set

```text
A(2j)   = 2^j,
A(2j+1) = 2^j 1.
```

Its target word is exactly

```text
A(r0) 11 A(r1) 11 ... 11 A(rk).
```

Consequently the fibre over an arbitrary target word `y` is the number of
parses of `y` by the regular expression

```text
A (11 A)*,       A in 2* (epsilon | 1).
```

This is an all-parameter target-dependent inverse algorithm, including zero
fibres.  `verify_scout.py` implements this parser independently of source
enumeration and compares it with every target through `n=18`.

For the all-vertical target, a source lies in the fibre iff its path matching
is maximal: otherwise two adjacent uncovered vertices would create a target
edge.  If `a_n` denotes this fibre, the first source edge gives the standard
recurrence

```text
a_0=a_1=a_2=1,        a_n=a_(n-2)+a_(n-3)  (n>=3).
```

The resulting values for `n=1,...,18` are

```text
1,1,2,2,3,4,5,7,9,12,16,21,28,37,49,65,86,114.
```

### 1.3 Why the exact package is still killed

Both axes are controlled by the same finite transducer.  The temporal proof
tracks a one-sided defect moving at unit speed until an alternating hard-core
configuration is reached; the inverse proof counts the corresponding regular
preimages.  P90 already occupies the finite traffic interface with a sharp
core-entry theorem, alternating hard-core recurrent states, and exact
preimage enumeration.  `GCM` has a different literal rule and is not asserted
to be conjugate to Rule 184, but its dominant proof and theorem silhouette
transfer without a residual geometric axis.  The Padovan fibre is static
maximal-matching enumeration, not a second dynamic mechanism.

```text
GCM: KILL_INTERNAL_TRAFFIC_TRANSDUCER
```

## 2. `SRW`: rooted star-switch walk on perfect matchings

Let `m=2n`, let `M` be a fixed-point-free involution on `[m]`, and distinguish
label `0`.  Sample `v` uniformly from `[m]` and set

```text
M' = (0 v) M (0 v).
```

If `a=M(0)`, the branches `v=0,a` hold.  For every
`b notin {0,a}`, exactly one choice, `v=M(b)`, makes the new root partner `b`.
Thus the root-partner chain on `m-1` states has diagonal probability `2/m`,
off-diagonal probability `1/m`, and nontrivial eigenvalue `1/m`.  Starting
with partner `a`, for every `t>=0`,

```text
Pr(A_t=a) = 1/(m-1) + (m-2)/(m-1) m^(-t),
Pr(A_t=b) = (1-m^(-t))/(m-1),  b != a.
```

In labelled-history counts these are respectively

```text
(m^t+m-2)/(m-1),       (m^t-1)/(m-1).
```

The one-step hold probability recovers `n=m/2`.  Each generator is an
involution, so the full chain is reversible with uniform stationary law; star
transpositions generate `S_m`, so their conjugation action is transitive on
the fixed-point-free involutions and the chain is irreducible.

However, an arbitrary matching endpoint count is precisely a coefficient of

```text
(1 + sum_(v=1)^(m-1) (0 v))^t
```

acting by conjugation on that conjugacy class.  This is the standard
star-transposition/Jucys--Murphy factorization engine on the perfect-matching
association scheme.  Perfect-matching rewiring walks directly own the same
two-pair switch primitive.  After subtracting those owners, only the lazy
complete-graph marginal remains, not an independent target atlas.

```text
SRW: KILL_DIRECT_MATCHING_REWIRING_OWNER
```

## 3. `OFP`: orthogonal flag polarity

Let `q` be odd and let `theta` be a nondegenerate orthogonal polarity of
`PG(2,q)`.  On the incident flags define

```text
D(p,l) = (theta(l),theta(p)).
```

Because a polarity reverses incidence and satisfies `theta^2=1`, this is an
involution.  A flag is fixed exactly when `l=theta(p)` and `p` is absolute.
The absolute points of a nondegenerate orthogonal polarity form a conic with
`q+1` points.  Since `PG(2,q)` has `q^2+q+1` points and every point lies on
`q+1` lines, the functional graph has

```text
fixed flags = q+1,
two-cycles  = ((q^2+q+1)(q+1)-(q+1))/2.
```

The fixed shell recovers `q`, but each target has exactly one source and both
the exceptional shell and the recovery formula are consequences of the same
classical polarity definition.  There is no inverse mass after owner
subtraction.

```text
OFP: KILL_DIRECT_POLARITY_INVOLUTION
```

## 4. Executable falsification boundary

The self-contained verifier uses no seed, floating point, network, timestamp,
third-party dependency, paper code, or earlier scout code.  It checks:

- the tiling and path-matching implementations of `GCM` against one another;
- all states through `n=18`, the leftmost-defect inequality, exact recurrent
  locus, sharp witness, every target parser, and exceptional fibre recurrence;
- all perfect matchings through `n=5`, every labelled `SRW` branch,
  reversibility, irreducibility, uniform column mass, and the root-partner law
  for `0<=t<=5`; and
- the full orthogonal flag involution for prime fields `q=3,5,7,11`, including
  point/flag counts and every orbit.

The frozen run makes `60,169` exact assertions.  Finite enumeration is
counterexample pressure for the displayed all-parameter proofs, not a novelty
argument.

```text
GREEN 0
KILL 3
FINAL KILL_ALL
HOLD_EXTERNAL
```
