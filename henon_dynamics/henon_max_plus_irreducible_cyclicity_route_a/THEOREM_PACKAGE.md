# C188 proof package

## Claim

Let `A` be an `n x n` irreducible matrix over the rational max-plus semiring.
Let `lambda` be its maximum cycle mean, let `B=A-lambda`, let the critical
graph have SCC cyclicities `gamma_1,...,gamma_s`, and put
`gamma=lcm(gamma_1,...,gamma_s)`.

Then:

1. the least ultimate period of the matrix sequence `B^t` is exactly `gamma`;
2. its least transient is
   `T(A)=min{t>=0:B^(t+gamma)=B^t}`;
3. for the standard critical matrices `C,S,R`, a matrix-dependent `T_CSR`
   exists such that `B^t=C S^t R` for all `t>=T_CSR`;
4. every vector orbit and every nonzero projective orbit has ultimate period
   dividing `gamma`, with exact divisor strata described by attraction cones;
5. the normalized eigencone lies in the period-one attraction cone, while the
   ultimate column spans form a `gamma`-periodic family;
6. `gamma=1` gives eventual constancy but no uniform transient, and no bound
   depending only on dimension and support can hold independently of weights;
7. irreducibility is essential to a single-growth-rate statement.

## Status

PROVABLE AS STATED, with the cyclicity and CSR conclusions explicitly imported
from the cited classical sources.  No novelty claim is attached to those
source theorems.

## Assumptions and notation

- `x oplus y=max(x,y)` and `x otimes y=x+y`, with additive zero `-inf`.
- The cited max-times statements are transported through the logarithmic
  semiring isomorphism before restriction to rational max-plus weights.
- A matrix entry `a_ij` is the weight of the edge `i -> j`.
- Matrix powers include `B^0=I`.
- `Col(M)={M x:x in Q_max^n}` is the max-plus column cone.
- Projectivization is restricted to vectors other than the all-`-inf` vector.

For normalized `B`, define

```text
K=(B^gamma)^*=I oplus B^gamma oplus ... oplus B^((n-1)gamma).
```

`C` keeps the critical columns of `K`, `R` keeps its critical rows, and `S`
keeps the normalized critical edges of `B`; every other entry is `-inf`.

## Dependency map

1. Sergeev's source-locked cyclicity theorem gives finite ultimate periodicity
   and says its least period is the critical cyclicity `gamma`.
2. One-equality propagation converts that existence theorem into the exact
   least-transient characterization.
3. Sergeev–Schneider supplies the ultimate CSR equality.
4. Applying the matrix identity to vectors gives period divisibility; max-plus
   homogeneity gives the projective version.
5. Divisor minimality gives the exact attraction strata.
6. Images of consecutive powers give the ultimate-span cycle.
7. An explicit `2 x 2` induction proves the sharp no-uniform-transient result.
8. A reducible diagonal witness proves why one growth normalization cannot be
   asserted outside the frozen family.

## Proof

### 1. Matrix-power period

The critical graph is completely reducible.  By the classical cyclicity
theorem in the first source, the normalized power sequence is ultimately
periodic and its least positive ultimate period is the lcm of the cyclicities
of its critical SCCs.  Under the frozen definition this number is `gamma`.
Thus a finite `T_0` exists with

```text
B^(t+gamma)=B^t  for all t>=T_0,
```

and no smaller positive integer is an ultimate matrix period.

### 2. Exact minimal transient

Suppose `B^(t+gamma)=B^t` for one nonnegative `t`.  Right-multiplying both
sides by `B^k` gives

```text
B^(t+k+gamma)=B^(t+k)
```

for every `k>=0`, by associativity of max-plus matrix multiplication.  Hence
one equality starts the full periodic regime.  The cyclicity theorem makes the
set of such `t` nonempty, so its minimum is exactly the least transient.

### 3. CSR equality

For the displayed `K,C,S,R`, the irreducible normalized specialization of the
Sergeev–Schneider ultimate CSR theorem yields a finite, matrix-dependent
`T_CSR` with `B^t=C S^t R` for every later `t`.  This statement does not impose
a universal transient.  The package searches for the least regression
`T_CSR` only for each declared finite census matrix.

### 4. Vector and projective periods

For every vector `x` and `t>=T`,

```text
B^(t+gamma)x=B^t x.
```

Therefore the least vector ultimate period divides `gamma`.  For a nonzero
vector, projectivization preserves the same equality, and max-plus homogeneity
shows that equality up to an additive scalar also propagates; its least
projective period likewise divides `gamma`.  The divisor can be strict: for
`B=[[−inf,0],[0,−inf]]`, the matrix period is two while `(0,0)` is fixed.

For each divisor `p|gamma`, define

```text
Attr_p(B)={x:B^(T+p)x=B^T x}.
```

The propagation argument proves that this is exactly the set of vectors whose
ultimate period divides `p`.  Hence the exact-period-`p` set is

```text
Attr_p(B) minus union_{q|p, q<p} Attr_q(B).
```

Each `Attr_p` is a two-sided max-plus linear equality set.  Replacing equality
by projective equality gives the corresponding projective strata.

### 5. Eigencone and ultimate spans

If `Bx=x`, then `B^t x=x` for all `t`; thus the normalized eigencone lies in
`Attr_1(B)`.  Put `V_r=Col(B^(T+r))` for `0<=r<gamma`.  Matrix periodicity
gives `V_(r+gamma)=V_r`, and direct composition gives
`B(V_r)=V_(r+1)`.  Every `B^t x` with `t>=T` lies in the corresponding phase
cone.  These statements do not assert that all phase cones are distinct.

### 6. Primitive and unbounded-transient boundary

When `gamma=1`, the matrix powers are eventually constant.  For every integer
`m>=1`, consider

```text
B_m=[[0,-m],[0,-1]].
```

Its support is the same complete two-node digraph, its critical graph is the
loop at the first node, and `gamma=1`.  Induction under max-plus multiplication
gives, for `t>=1`,

```text
B_m^t=[[0,-m],[0,max(-t,-m)]].
```

The lower-right entry changes through `t=m-1` and is constant from `t=m`.
All other entries are already constant, so the minimal transient is exactly
`m`.  Since `m` is arbitrary, no dimension-only or support-only bound that is
independent of the weights exists.

### 7. Reducible boundary

For `D=diag(0,1)`, the two SCC growth rates are zero and one.  Normalizing by
the maximum rate produces `diag(-t,0)` in the `t`th power, which is not
periodic.  Thus the one-growth cyclicity statement cannot be extended to all
reducible matrices.  The cited CSR source instead supplies multiple terms and
growth rates in that setting.  This completes the stated classification. ∎

## Open risks and nonclaims

- The transient is not uniformly bounded by dimension and support alone.
- Individual vector periods need not equal `gamma`.
- Reducible matrices need not admit a single normalized periodic sequence.
- The finite census is not an all-parameter proof.
- No arithmetic local data, target divisor, Hilbert–Pólya operator, external
  review, or acceptance score is asserted.
