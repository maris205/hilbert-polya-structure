# Boxed plane-partition layer stripping — strict scout

**Decision:** `KILL_DEFINITION_LEVEL_AND_INTERNAL_COLLISION`  
**Mathematics:** `PASS_EXACT`  
**Paper allocation:** none  
**External status:** `HOLD_EXTERNAL`

## Target

Let `R=[a] x [b]`.  A state in `PP_(a,b,c)` is an `a x b` array
`pi=(pi_(i,j))` with entries in `{0,...,c}` weakly decreasing along rows
and columns.  The literal map is

```text
L(pi)_(i,j) = max(pi_(i,j)-1,0).
```

The scout tests whether the exact orbit, depth census, image tower,
arbitrary-target fibres, and support-refined convolution leave a paper-sized
residual after classical plane-partition and order-polynomial subtraction.

## Status of the derivation

`COHERENT AS STATED`, including all degenerate boundaries.  The candidate is
killed for ownership/thinness rather than a false formula.

## Invariant object and the decisive generalization

For a finite poset `P`, let `PP_P(c)` denote the order-reversing maps

```text
f:P -> {0,...,c}.
```

Write the same symbol `PP_P(c)` for their number when no confusion is
possible.  Define

```text
I_r(f) = {x in P : f(x) >= r},       1 <= r <= c.
```

Each `I_r(f)` is an order ideal and

```text
I_1(f) superseteq I_2(f) superseteq ... superseteq I_c(f).
```

Conversely this multichain reconstructs `f`.  This is the invariant object
organizing every formula below.  The proposed map satisfies

```text
I_r(L^t f) = I_(r+t)(f).
```

Thus `L` is only a left shift of the order-ideal multichain.  The extension
from rectangles to arbitrary finite posets succeeds mathematically and at
the same time proves that the rectangle has no special dynamic engine.

## Exact theorem contract before subtraction

### 1. Iterates, recurrence, and clock

For every `t>=0`,

```text
L^t(f)(x) = max(f(x)-t,0).
```

The zero labelling is the unique recurrent state and

```text
depth(f) = max_(x in P) f(x),
```

where the maximum over an empty poset is zero.  Consequently the sharp
height is `c` when `P` is nonempty and is zero when `P` is empty.  For the
rectangle this is `c` if `ab>0`, and zero if `a=0` or `b=0`.

The proof is coordinatewise: every positive value drops by exactly one per
round, and no coordinate can become positive again.

### 2. Temporal census and image tower

For `d>=0`,

```text
#{f in PP_P(c) : depth(f) <= d} = PP_P(min(d,c)).
```

Hence the exact depth-`d` shell for `1<=d<=c` has size

```text
PP_P(d) - PP_P(d-1),
```

and depth zero contains only the zero state.  Moreover

```text
Im(L^t) = PP_P(max(c-t,0)).
```

For `t<=c`, a target `g` has the explicit source `g+t`; for `t>=c`, only
zero remains.

For `P=[a]x[b]`, MacMahon gives the zero-credit specialization

```text
M_(a,b)(r)
  = product_(i=1)^a product_(j=1)^b (i+j+r-1)/(i+j-1),
```

with empty product one.  Therefore the depth-at-most-`d` census is
`M_(a,b)(min(d,c))` and the time-`t` image has
`M_(a,b)(max(c-t,0))` states.

### 3. Every target and its skew-complement fibre

Assume first `0<=t<=c` and let `g` be a target in `PP_P(c-t)`.  Its positive
support

```text
S = supp(g) = {x : g(x)>0}
```

is an order ideal.  A source `f` of `g` is forced on `S` and free on the
induced complementary poset:

```text
f(x) = g(x)+t                         for x in S,
f restricted to P\S in PP_(P\S)(t).
```

All cross-boundary inequalities are automatic.  If `x in S` lies below a
complement point, its forced value is at least `t+1`, whereas every free
value is at most `t`; the reverse cross relation cannot occur because `S`
is an ideal.  Thus

```text
|L^(-t)(g)| = PP_(P\S)(t).                         (F)
```

For a rectangle, `S` is a northwest Young diagram and `R\S` is the skew
rectangle.  Formula (F) is precisely the count of bounded weak/weak plane
partitions on that skew shape.  It depends only on the support, not on the
positive values of `g`.

Post-cap, `t>=c`, the only target is zero and its fibre is all of
`PP_P(c)`.  In one formula the complementary cap is `min(t,c)`; a nonzero
target can occur only when `t<c`.

The remaining degenerate convention is `c=0`: for every `a,b` the carrier is
the singleton zero array, its height is zero, every iterate is zero, and its
only fibre has size one.  If `a=0` or `b=0`, the carrier is likewise a
singleton for every `c`; hence the nondegenerate phrase “sharp height `c`” is
used only when `ab>0`.

### 4. Support multiplicity and convolution

Adopt the boundary conventions

```text
PP_empty(-1)=1,
PP_Q(-1)=0 for nonempty Q.
```

For an ideal `S` and `0<=t<=c`, the number of targets whose support is
exactly `S` is

```text
PP_S(c-t-1).                                      (T)
```

Indeed, subtract one from every positive target value on `S`.  Combining
(F) and (T) gives the support-resolved source count

```text
PP_S(c-t-1) PP_(P\S)(t),
```

and the exact convolution

```text
PP_P(c)
  = sum_(S in J(P)) PP_S(c-t-1) PP_(P\S)(t),
    0 <= t <= c.                                  (C)
```

At `t=0`, (C) is ordinary decomposition by positive support.  At `t=c`,
only `S=empty` contributes and the zero target has the entire carrier as its
fibre.  In the multichain model, (C) merely cuts a chain of order ideals at
the intermediate ideal `S`; algebraically it is the standard convolution of
zeta-function powers in `J(P)`.

## Decisive finite example

For the `2 x 2 x 2` box there are `20` states.  At `t=1` there are six
targets, one on each northwest support ideal.  Ordered by supports
`empty`, one cell, the two two-cell shapes, three cells, and the full
rectangle, their fibres have sizes

```text
6, 5, 3, 3, 2, 1,
```

which sum to `20`.  At `t=0` every fibre is a singleton; at `t=2` the zero
target has fibre `20`.  These values are exhaustively recovered by the
verifier rather than fitted.

## Determinant boundary

The safe exact object for a skew complement is the bounded order polynomial
`PP_(R\S)(t)`.  Classical lattice-path work supplies determinant technology
for skew plane partitions, but no particular bounded determinant is retained
here: translating among positive/zero-based and ordinary/reverse weak/weak
conventions would add risk and no theorem value.  MacMahon and every such
determinantal specialization would be zero-credit even if appended.

## Exact control

`verify_scout.py` is an independent standard-library brute implementation.
It constructs order-reversing maps literally and checks:

- ten nonisomorphic test posets, including the empty poset, point, chain,
  antichain, `V`, dual `V`, diamond, fence, disjoint chains, and a five-point
  `N`-type poset;
- every rectangle `0<=a,b<=3` and every cap `0<=c<=4`;
- every state and every time `0<=t<=c+1`;
- the iterate, exact point depth, sharp height, and unique recurrent zero;
- every complete image set and every target fibre;
- every ideal support multiplicity and every convolution term;
- MacMahon counts and cumulative depth counts for all audited rectangles.

Frozen receipt:

```text
assertions          183,401
verifier SHA-256    f750e93a6406da643860192078e8d422be3f3cca439fc40957dc383667d99420
canonical SHA-256   458d6fed637f4a024d984c4bcba5be69828e596c705e6aad2cb6628db3cda6c9
fresh replays       2/2 byte-identical
py_compile          PASS
status              PASS
```

Finite enumeration is counterexample pressure, not proof or owner evidence.

## Owner and internal subtraction

The detailed source ledger is `OWNER_SEARCH_LOG.md`.  The following inputs
receive zero contribution credit:

- bounded `P`-partitions/order polynomials;
- their representation by chains of order ideals or ideals in `P x [c]`;
- zeta-polynomial and multichain convolution;
- MacMahon's boxed plane-partition product;
- skew plane partitions, reverse plane partitions, and determinant methods;
- Schur-process/three-dimensional Young-diagram slices;
- general plane-partition dynamics language.

Internally, P126 already occupies the cumulative-depth/all-image/all-fibre
silhouette with a nontrivial code engine.  P160 is decisive: it already gives
a coordinate iterate, sharp absorption, arbitrary-target forced-core fibres,
and support consequences for rectangular corner stripping.  The present map
has the same interface with a strictly simpler proof: scalar thresholding
replaces P160's two-boundary rectangle geometry.  P113, P144, and P149 add
further clock/fibre/image subtraction on partitions, paths, and permutations.

## Paper-threshold decision

The advertised formulas are correct, including every boundary requested.
They do not form two independent residual axes.  The clock is the largest
label in a bounded `P`-partition; the fibre is the omitted prefix of the same
ideal multichain; and the convolution is that multichain split at one ideal.
All three statements have one definition-level proof engine.

```text
MATHEMATICS          PASS_EXACT
GENERAL_POSET_FORM   TRUE_BUT_DEFINITION_LEVEL
DIRECT_OWNER_HIT     NONE_IN_BOUNDED_SEARCH
MECHANISM_OWNER      YES
INTERNAL_COLLISION   DECISIVE_P160; STRONG_P126
SECOND_RESIDUAL_AXIS NONE
DECISION             KILL_DEFINITION_LEVEL_AND_INTERNAL_COLLISION
EXTERNAL             HOLD_EXTERNAL
```

No paper should be created from this contract.  Re-entry would require a
different literal map whose nontrivial temporal invariant and inverse atlas
do not both reduce to shifting and splitting the standard height filtration.
