# Subdouble-support shortening of linear codes

**Decision:** `GREEN_OWNER_THIN`.  
**Lifecycle:** `HOLD_EXTERNAL`.  
**Meaning of the decision:** the theorem contract below may be sent to an
independent hostile gate.  It is not a novelty, priority, authorship, paper
allocation, or release determination.

## Outcome first

Two genuinely different literal maps were admitted.  Principal-downset
inclusion on posets was killed because its forward convergence and weak-order
fixed census did not lead to a separate arbitrary-target theorem.  The sole
survivor is a nonlinear, state-dependent shortening map on finite linear
codes.  In exact boxes it exhibited a dyadic depth staircase and an image
criterion depending on two target invariants.  Both extend cleanly to all
prime powers.

The central caution is substantial.  Shortening codes on hitting sets of
low-weight words is existing coding-theory machinery: Jibril et al. prove a
generalized shortening principle that removes prescribed low-weight words
and raises the minimum distance
([DOI 10.1049/iet-com.2011.0693](https://doi.org/10.1049/iet-com.2011.0693)).
That one-step mechanism, standard code parameters, and minimum-distance
language receive zero contribution credit.  The residual considered here is
only the conjunction of the literal state-dependent iteration, the exact
all-time image boundary, and the targetwise extremal inverse slice.

## 1. Literal finite dynamics and conventions

Fix a prime power `q` and `V=F_q^n`.  The phase space is the finite set of all
linear subspaces `C<=V`; coordinates remain labelled.  For nonzero `C`, let

```text
d(C) = min{wt(c): 0 != c in C},
L(C) = {c in C: 0 < wt(c) < 2 d(C)},
U(C) = union_{c in L(C)} supp(c).
```

Define

```text
T(C) = {c in C: c_j=0 for every j in U(C)},       C != 0,
T(0) = 0.                                         (1)
```

Thus `T(C)` is the conventional shortening on `U(C)`, padded by zero
coordinates so that (1) is a self-map of one fixed finite carrier.  It is not
puncturing.  The strict inequality `wt(c)<2d(C)` is part of the literal map;
replacing it by `<=` changes the theorem.

Write

```text
Supp(C) = union_{c in C} supp(c),
z(C)    = n-|Supp(C)|,
s_t     = 2^t-1,
tau(C)  = min{t>=0:T^t(C)=0}.
```

The zero code has depth zero.  A “source” and “target” below are labelled
subspaces, not generator matrices and not monomial-equivalence classes.

## 2. Frozen theorem contract

### Theorem A — pointwise descent and sharp dyadic clock

For every nonzero code `C`, `T(C)` is a proper subcode.  If `T(C)` is
nonzero, then

```text
d(T(C)) >= 2 d(C).                                 (2)
```

Consequently zero is the unique recurrent state and

```text
tau(C) <= floor(log_2(n+1)).                        (3)
```

The bound is sharp for every `n`: if `r=floor(log_2(n+1))`, choose disjoint
coordinate blocks `B_0,...,B_(r-1)` of sizes

```text
|B_i|=2^i
```

and let `C` be the direct sum of one full-support one-dimensional repetition
line on each block.  Then the blocks are removed in order and `tau(C)=r`.

**Proof.**  A minimum word belongs to `L(C)`, so it is excluded by (1) and
the step is proper.  A nonzero word surviving (1) cannot have weight below
`2d(C)`, proving (2).  Along a nonzero orbit put `C_i=T^i(C)`, `d_i=d(C_i)`,
and `U_i=U(C_i)`.  The supports `U_i` are pairwise disjoint, because every
later code is zero on every earlier `U_i`; moreover

```text
|U_i| >= d_i >= 2^i.
```

Thus depth `r` forces `n>=sum_(i<r)2^i=2^r-1`.  The displayed direct sum has
at stage `i` only its `B_i` line below weight `2^(i+1)`, so equality is
attained.  This is a proof for all `q`; finite enumeration is only
counterexample pressure.

### Theorem B — every-time, every-target image

Let `t>=0` and let `D<=F_q^n` be nonzero.  Then

```text
D in im(T^t)
  iff d(D) >= 2^t and z(D) >= 2^t-1.               (4)
```

The zero code belongs to every time image, using itself as a source.

**Necessity.**  If `T^t(C)=D!=0`, all intermediate codes are nonzero.  By
(2), `d(D)>=2^t d(C)>=2^t`.  Their pairwise-disjoint purge supports are zero
coordinates of `D` and have sizes at least `1,2,...,2^(t-1)`, giving
`z(D)>=s_t`.

**Sufficiency and the requested shortening expansion.**  Suppose the two
inequalities in (4) hold.  Select disjoint blocks

```text
B_i subseteq [n]\Supp(D),    |B_i|=2^i,   0<=i<t,
```

and on each `B_i` choose a one-dimensional line `L_i` whose nonzero words
have full support `B_i`.  Set

```text
C = D direct_sum L_0 direct_sum ... direct_sum L_(t-1).   (5)
```

At time `i`, the current code is

```text
D direct_sum L_i direct_sum ... direct_sum L_(t-1).
```

Its distance is `2^i`; the only words of weight strictly below `2^(i+1)`
are the nonzero words of `L_i`.  Indeed every later line has weight at least
`2^(i+1)`, every nonzero word of `D` has weight at least `2^t`, and disjoint
supports make the weight of a mixed word additive.  Hence `U(C_i)=B_i`, so
the next step deletes exactly `L_i`.  After `t` steps the target is `D`.

Formula (4) is an exact targetwise reachability statement, not a count of the
entire fibre.

### Theorem C — sharp targetwise inverse extremizers

Fix `D!=0` and `t>=0`.  Every source `C` with `T^t(C)=D` satisfies

```text
dim(C)-dim(D) >= t,
|Supp(C)\Supp(D)| >= s_t.                           (6)
```

If (4) holds, simultaneous equality in both parts of (6) is possible.  The
simultaneous equality sources are exactly the direct sums (5), with the
blocks and full-support lines as specified there.  Their number is

```text
             z(D)!
----------------------------------  (q-1)^(s_t-t).  (7)
(z(D)-s_t)! product_(i=0)^(t-1) (2^i)!
```

For `t=0`, empty products give one source, namely `D`.

**Proof.**  Every nonzero step is a proper subspace inclusion, proving the
dimension inequality.  The disjoint sets `U_0,...,U_(t-1)` lie in
`Supp(C)\Supp(D)` and have respective sizes at least `2^i`, proving the
support inequality.  Equality forces `d_i=|U_i|=2^i` at every step and a
one-dimensional quotient at every step.  A linear subspace of
`F_q^{U_i}` in which every nonzero vector has full support is one-dimensional:
two independent vectors admit a nontrivial linear combination vanishing in
a chosen coordinate.  Subtracting later residual words from a lift leaves
the full-support line on `U_i`; descending induction gives exactly (5).

To count, choose ordered disjoint blocks of the distinct sizes `2^i`, giving

```text
(z(D))_(s_t) / product_i (2^i)!
```

choices.  A block of size `m` supports `(q-1)^(m-1)` full-support lines, so
the line choices contribute `(q-1)^(s_t-t)`.  This proves (7).

For the zero target, the whole fibre `T^{-t}(0)` contains shallower sources
and is not given by (7).  The correct boundary is: among codes of exact depth
`t>=1`, the minimum dimension is `t`, the minimum support is `s_t`, and the
simultaneous minimizers are counted by (7) with `z(D)` replaced by `n`.

## 3. Why the axes are independent enough for a hostile gate

Theorem A is forward and pointwise: it bounds one source by successive
minimum distances and disjoint purge supports.  Theorem B reverses the map
for an arbitrary prescribed target and is exact at every time; both target
invariants are necessary.  Theorem C is not a restatement of reachability:
it classifies and enumerates the simultaneous minimum-dimension and
minimum-new-support slice inside each nonempty target fibre.  For example, a
target can satisfy (4) with many unused zero coordinates, and (7) varies with
that surplus even though Theorem A's global clock does not.

The contract deliberately does **not** claim a closed count for the complete
fibre.  Counting all extensions with prescribed low-weight support is a much
harder coding problem, and the small-box verifier is not evidence for such a
formula.

## 4. Boundary audit

- `n=0`: zero is the only code and the height is zero.
- `t=0`: every nonzero target satisfies (4); (7) equals one.
- `D=0`: it is always in the image, but the nonzero-target fibre statement is
  replaced by the exact-depth boundary following (7).
- Full-support `D!=0`: `z(D)=0`, so it has no positive-time preimage.
- `2^t-1>n`: the positive time-`t` image is empty; zero remains.
- The alphabet assumption is exactly “finite field of prime-power order.”
- The threshold is strict `<2d`.  Under `<=2d`, a block of size `2d` is
  removed one stage too early and (4)--(7) fail.
- The update is coordinate-permutation equivariant, but the fibre count is
  for labelled codes.  No quotient by code equivalence is taken.
- No polynomial-time claim is made.  Minimum-distance computation is known
  to be intractable in general (Vardy,
  [DOI 10.1109/18.641542](https://doi.org/10.1109/18.641542)).

## 5. Internal collision firewall

| prior system | nearest silhouette | decisive separation |
|---|---|---|
| P100 valuation digit erasure / P115 Cartier decimation | finite algebra with coordinate loss | those updates are fixed arithmetic/linear coordinate maps; (1) recomputes a nonlinear low-weight support union from the entire current code |
| P109 nilpotent-image subspaces | descending subspaces | P109 iterates one fixed nilpotent operator; SDS changes the coordinate kernel at every state and its inverse is controlled by distance plus zero-coordinate capacity |
| P137 rank-feedback `p`-group splitting | resource budget and a sharp clock | P137 has additive marker sizes and a triangular clock with a unique partition witness; SDS has multiplicative distance growth, geometric support layers, a logarithmic clock, many witnesses, and targetwise code extensions |
| P143 Boolean row-inclusion residual | Boolean matrix/subspace encodings | no row-inclusion quotient or residual relation appears in (1) |
| P159 parallel odd-vertex pruning / P160 rectangular cropping | rank-changing deletion | SDS does not change the ambient labels and does not delete graph vertices or rectangular boundary cells; it takes a state-dependent shortening subspace |
| P163 complemented shadows / P164 equality-feedback codes | current-batch set-family or affine-code interfaces | SDS uses neither a shadow kernel nor a cellular-automaton tail/affine coset enumerator |
| killed Schur-square and code-hull candidates | linear codes | SDS is neither a product power nor an orthogonality retraction; every nonzero orbit has positive depth and terminates |

The generic observation “disjoint resources whose minimum sizes grow” is not
claimed as new.  The proposed residual is tied to the literal low-weight
support recomputation and the arbitrary-target statements (4)--(7).

## 6. Killed poset control

For completeness, the other admitted candidate was

```text
x <_(T(P)) y  iff  Down_P(x) is a proper subset of Down_P(y),
```

where `Down_P(x)={u:u<_P x}`.  Every old comparison survives, so the map is
inflationary.  A fixed poset is a weak order: at a fixed point every minimal
element lies below every nonminimal element; remove the first layer and
induct.  Conversely an ordinal sum of antichains is fixed.  Thus the fixed
counts are the ordered Bell numbers `1,3,13,75,541,...`.

This attractive census does not pass the two-axis gate.  The one-step fibre
over a weak order already asks for coupled families of principal downsets
that are nested across target layers and incomparable within layers.  No
factorized all-target inverse or independent image theorem emerged.  It is
also a transitive-relation specialization of the row-inclusion neighborhood
around P143.  Decision: `KILL_NO_INDEPENDENT_TARGET_AXIS`.

## 7. Executable evidence and claim ceiling

[verify_scout.py](verify_scout.py) independently enumerates every labelled
poset through five labels, every binary linear code through length seven, and
every ternary linear code through length four.  It checks the two literal
updates, PDI inflation/fixed classes, SDS descent/distance doubling,
coordinate covariance, sharp heights, every time-image criterion through
time four, and every nonzero target's extremal-fibre formula in those boxes.
The frozen output is [CANONICAL.txt](CANONICAL.txt).

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_scout.py > /tmp/open_fresh_p165.out
cmp -s CANONICAL.txt /tmp/open_fresh_p165.out
```

The transcript reports `413,644` exact assertions.  Enumeration does not
prove the all-parameter statements; the proofs are above.

The status remains `GREEN_OWNER_THIN / HOLD_EXTERNAL`.  A hostile gate must
still decide whether, after assigning zero credit to generalized shortening
and low-weight hitting sets, Theorems B and C leave enough independent
content for a short paper.  A direct owner for (1), (4), or (7) changes the
decision to kill.
