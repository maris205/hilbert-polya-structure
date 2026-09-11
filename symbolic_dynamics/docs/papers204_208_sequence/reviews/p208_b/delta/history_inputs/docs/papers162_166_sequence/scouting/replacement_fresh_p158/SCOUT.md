# Fresh replacement scout — ternary modular run consolidation

**Decision:** `KILL_INTERNAL_P147_SAME_RUN_CONSOLIDATION_ENGINE`  
**Paper allocation:** none  
**External status:** `HOLD_EXTERNAL`  
**Exact assertions:** 337,738

## Outcome first

This focused lane found a literal finite map with two clean, all-parameter
theorem axes, but it does **not** clear the portfolio threshold.  On the
disjoint union of ternary words of bounded length, simultaneously replace
each maximal constant run by the sum of its letters in `Z/3Z`.  The system
has a sharp absorption clock `N-1`, witnessed at every cap, and a complete
every-target one-step inverse polynomial given by a three-state weighted path.

Those facts are mathematically sound.  Nevertheless, the update is the same
maximal-run consolidation schema as live P147, with the positive additive
monoid replaced by the torsion group `Z/3Z`.  Its inverse theorem is likewise
the same adjacent-distinct run-label path construction: divisibility in P147
becomes a congruence condition here.  Torsion changes the clock from
logarithmic to linear, but the remaining proof is only strict length descent
plus a two-family witness.  That deformation is not enough for another paper.

The lane therefore returns an honest **KILL**, not a quota-filling amber.
A bounded external search found no direct publication stating this exact
modular iterate, but a non-hit is not novelty and cannot cure the internal
collision.

## Pre-screen and collision scope

Before selecting the literal map, the directory titles through P161, the
historical occupancy summaries, and the active P162--P166 scouting and gate
ledgers were screened.  In particular, the following were excluded rather
than recycled:

- random subset/rank intersections (`RTI`) and cut intersections (P158);
- q-ary equality-feedback cellular automata (`CEF`) and the occupied binary
  register/run/parity cluster;
- cyclic partition erosion (`CPE`), exact-shift meet/join systems, and generic
  partition-lattice pullbacks;
- quadratic nilpotent collapse (`QNC`), Frobenius-linear and generic power
  maps, Schur/LDU (`USP`), valuation truncation, and Euclidean/GCD systems;
- normalizer/Frattini/commutator series, finite-linear relabelings, and the
  cyclic-subgroup compression `H -> pH`, which was already reserved beside
  P100;
- classical rowmotion, 0-Hecke sorting, KMP border descent, tree/leaf
  pruning, closure/retraction, Bulgarian solitaire, and the killed current
  nonlinear, geometry/group, stochastic, matching/incidence, and
  poset/language pools.

The selected system is not a renamed member of a current kill row.  It fails
only after comparison with a **live** earlier paper, P147.

## Literal finite dynamical system

For `N>=0`, let

```text
X_N = disjoint_union_{0<=n<=N} (Z/3Z)^n.
```

The empty word is allowed.  Factor a nonempty word uniquely into maximal
constant runs

```text
w = r_1^(ell_1) r_2^(ell_2) ... r_k^(ell_k),
r_i in Z/3Z, ell_i>=1, r_i != r_(i+1).
```

Define the simultaneous update

```text
M(w) = (ell_1 r_1, ell_2 r_2, ..., ell_k r_k) mod 3,
M(empty) = empty.
```

For example,

```text
112121 -> 22121 -> 1121 -> 221 -> 11 -> 2.
```

Length never grows, so this is a self-map of the finite carrier `X_N`.  The
cap is part of the carrier, not an overflow or failure convention.

## Axis A — complete absorption statement and sharp clock

### Theorem A

For every `N>=0`:

1. a word is fixed exactly when adjacent letters are distinct;
2. every orbit reaches a fixed word and there are no nontrivial cycles;
3. the fixed-point count on `X_N` is `3*2^N-2`; and
4. the maximum absorption time is `max(0,N-1)`.

### Proof

If a word has no repeated adjacent letters, every maximal run has length one,
so it is fixed.  Conversely, a repeated adjacent pair belongs to a run of
length at least two; collapsing all runs strictly shortens the word.  Hence a
nonfixed update loses at least one letter.  A nonempty word of length `n` can
therefore make at most `n-1` nonfixed updates.  This proves absorption, rules
out nontrivial cycles, and gives the upper bound.

There are `3*2^(n-1)` fixed words of positive length `n`, and the empty word
is fixed.  Summing over `0<=n<=N` gives `3*2^N-2`.

For sharpness, let `A_n` be the length-`n` prefix of

```text
1121212121...
```

and let `B_n` be the length-`n` prefix of

```text
2212121212....
```

For every `n>=2`, direct run factorization gives

```text
M(A_n)=B_(n-1),    M(B_n)=A_(n-1).
```

Thus `A_n` makes exactly `n-1` nonfixed updates before reaching one letter.
Taking `n=N` proves sharpness; `N=0,1` are the displayed base cases.

This is an all-parameter temporal theorem, but after collision subtraction
its upper bound uses only the decreasing length rank.

## Axis B — every-target, source-length-resolved inverse

Fix a nonempty target `y=(y_1,...,y_k)`.  For `r,y in Z/3Z`, put

```text
A_(r,y)(u) = sum_{ell>=1, ell*r = y (mod 3)} u^ell.
```

Explicitly, with rows indexed by `r=0,1,2` and columns by `y=0,1,2`,

```text
             y=0                 y=1                 y=2
r=0       u/(1-u)                 0                   0
r=1     u^3/(1-u^3)           u/(1-u^3)          u^2/(1-u^3)
r=2     u^3/(1-u^3)          u^2/(1-u^3)          u/(1-u^3).
```

Define the adjacent-distinct path series

```text
Phi_y(u) = sum_{r_i != r_(i+1)} product_i A_(r_i,y_i)(u).
```

### Theorem B

For every target `y` and every `L>=0`,

```text
[u^L] Phi_y(u)
  = number of source words x of length L with M(x)=y.
```

Consequently, for the capped carrier `X_N`, the complete fibre size is

```text
sum_{0<=L<=N} [u^L] Phi_y(u),
```

and `y` is in `M(X_N)` exactly when the least nonzero exponent of `Phi_y` is
at most `N`.  Equivalently, support is decided by the same three-state path
calculation over the min-plus semiring.  The empty target has the single empty
predecessor.

### Proof

Every source has a unique maximal-run factorization.  Its `i`th run has a
letter `r_i`, a positive length `ell_i`, adjacent run letters are unequal,
and it produces target letter `y_i` precisely when
`ell_i*r_i=y_i mod 3`.  The monomial contributed by the run is `u^ell_i`.
Multiplication joins independently chosen runs, the adjacent inequality makes
the factorization maximal, and summation ranges over all possible run-letter
paths.  This construction is reversible, so coefficients count sources
without omission or multiplicity.

This inverse theorem is genuinely logically independent of the length-clock
proof.  It is nonetheless structurally the P147 divisor-path inverse with
`ell*r=y` interpreted in a different coefficient monoid.

## Exact falsification record

[`verify_scout.py`](verify_scout.py) is standalone, deterministic, uses only
the Python standard library, and imports no earlier paper or scout code.  It:

- exhausts every ternary word of each exact length `0..9`;
- compares two independent implementations of the literal update;
- checks fixedness, strict descent, terminality, every depth upper bound, the
  exact fixed count, depth histograms, and the sharp maximum;
- verifies the two witness recurrences for every `0<=n<=1000`; and
- brute-force checks every source and every target in `X_8` against every
  source-length coefficient of the three-state path polynomial, including
  total fibre mass, minimum lift cost, support, and boundary examples.

The run makes exactly **337,738 assertions**.  Its stdout byte-matches
[`CANONICAL.txt`](CANONICAL.txt).  Finite enumeration is counterexample
pressure; Theorems A and B are proved above for all parameters.

Reproduce with:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_scout.py > /tmp/mrc3.out
cmp -s CANONICAL.txt /tmp/mrc3.out
```

## Threshold decision

| gate | result |
|---|---|
| literal finite self-map | pass |
| all-parameter temporal theorem | pass: fixed locus, absorption, no cycles, exact sharp clock |
| independent every-target inverse | pass: complete source-length path polynomial and cap support |
| exact deterministic verifier | pass: 337,738 assertions |
| bounded direct-owner search | non-hit only; remains `HOLD_EXTERNAL` |
| P1--P161 internal collision | **fail: P147 same maximal-run consolidation and adjacent-label inverse engine** |
| residual after subtraction | linear torsion witness plus elementary finite-state weights; below paper scale |

Final decision:

```text
KILL_INTERNAL_P147_SAME_RUN_CONSOLIDATION_ENGINE
```

Do not assign a paper number and do not draft a manuscript from this lane.
