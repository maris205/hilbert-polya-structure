# C140 proof package

## Claim and status

**Status: PROVABLE AS STATED.**  The frozen mod-three gap shift is strictly
sofic with the displayed minimal three-state right-resolving cover.  Its cover
determinant, all-period exceptional-point correction, intrinsic rational zeta,
and primitive label-orbit product are exact.

## Assumptions and notation

Let `X3` consist of bi-infinite binary sequences for which the number of zeros
between every pair of consecutive ones is in `3 Z_{>=0}`; include the all-zero
sequence.  Give label `1` roof time `1` and label `0` roof time `sqrt(2)`.
For a periodic label orbit `gamma`,

```text
ell(gamma)=N1(gamma)+sqrt(2) N0(gamma).
```

Use residue states `0,1,2` and edges

```text
0 --1--> 0,   0 --0--> 1,   1 --0--> 2,   2 --0--> 0.
```

The variables `u,v` mark labels `1,0`, respectively.

## Dependency map

1. Strict soficity uses a local-window contradiction; cover minimality uses
   three distinct follower sets.
2. The determinant is a direct three-by-three computation.
3. Lift uniqueness separates ordinary label points from the all-zero
   exceptional point.
4. The fixed-point correction sums to `log(1+v+v^2)` and gives the intrinsic
   zeta.
5. Unique primitive roots convert the fixed-point logarithm into the primitive
   label-orbit product.

## Theorem 1: strict soficity and the minimal cover

`X3` is sofic but not of finite type.  The displayed graph is its minimal
follower-separated right-resolving presentation.

**Proof.**  A path that reads `1` must be at residue state `0` and returns to
state `0`.  Every read `0` increments the residue modulo three.  Therefore a
finite path between consecutive `1` labels contains exactly a multiple of
three zeros, and every such gap has a path.  The all-zero sequence is read by
the bi-infinite three-cycle of zero edges.  Thus the graph presents exactly
`X3`, proving soficity.

Suppose `X3` were an `L`-step shift of finite type.  Choose `m` with
`3m+1>2L` and repeat the word `1 0^(3m+1)` periodically.  Its zero gap is
`3m+1`, so the sequence is not in `X3`.  Yet each block of length `L+1`
contains at most one `1`.  The all-zero block occurs in the all-zero point.
Any block with one `1`, with `a` visible zeros to its left and `b` to its
right, embeds in an allowed gap `0^(3q)` once `3q>=a+b`.  Hence every
length-`L+1` block of the forbidden periodic point occurs in `X3`, contrary to
an `L`-step local characterization.  Thus `X3` is not an SFT.

The graph is right resolving because no state has two outgoing edges with the
same label, and it is strongly connected.  The past words `1`, `10`, and
`100` are synchronizing: every path with one of those labels ends at residue
state `0`, `1`, or `2`, respectively.  Their intrinsic residual follower
languages are pairwise distinct.  From state `0` the word `1` is allowed
immediately; from state `2` the word `01` is allowed but not from states `0`
or `1`; from state `1` the shortest word ending at the next `1` is `001`.
The follower-set construction of the right Fischer cover assigns distinct
vertices to distinct follower languages of synchronizing pasts, so all three
residuals must occur.  The displayed graph realizes exactly those three
vertices.  It is therefore the minimal follower-separated right-resolving
cover, i.e. the right Fischer cover.  ∎

## Theorem 2: cover determinant

The weighted cover matrix and its determinant are

```text
B(u,v)=[[u,v,0],[0,0,v],[v,0,0]],
D_cov(u,v)=det(I-B)=1-u-v^3.                       (1)
```

**Proof.**  Expanding `I-B` along its second row gives the identity term, the
loop contribution `-u`, and the signed three-zero cycle contribution `-v^3`;
there are no other permutation products.  ∎

Consequently

```text
-log D_cov=sum_(n>=1) Tr(B^n)/n                   (2)
```

as a formal power series of positive total label degree.

## Theorem 3: exact exceptional-point correction

Define the intrinsic weighted sum explicitly by

```text
F_n(u,v)=sum_[x in Fix(sigma^n|X3)] u^N1(x) v^N0(x).
```

Then, for every `n>=1`,

```text
F_n(u,v)=Tr(B(u,v)^n)+(1-3*1_[3|n]) v^n.          (3)
```

**Proof.**  If a bi-infinite label sequence contains a `1`, that coordinate
forces cover state `0`; propagating residues in both directions then gives a
unique lift.  Hence cover and label fixed points agree off the all-zero
sequence, with identical weights.

The all-zero label sequence is a single point fixed by every `sigma^n`, so it
contributes `v^n` to `F_n` for every `n`.  In the cover it has three phase
lifts around one zero-edge orbit of least period three.  Those lifts are fixed
by the `n`th cover shift exactly when `3|n`, and then contribute `3v^n` to
`Tr(B^n)`; otherwise they contribute zero.  Replacing this cover contribution
by the one intrinsic label contribution yields (3).  ∎

This proof is all-period.  The finite replay is not used to infer (3).

## Theorem 4: intrinsic rational zeta and primitive product

Define the intrinsic label zeta formally by

```text
log Z_140(u,v)=sum_(n>=1) F_n(u,v)/n.
```

Then

```text
Z_140(u,v)=(1+v+v^2)/(1-u-v^3),                   (4)
D_140(u,v)=Z_140^(-1)
 =(1-u-v^3)/(1+v+v^2)
 =D_cov(u,v)(1-v)/(1-v^3).                        (5)
```

Moreover,

```text
D_140(u,v)=product_[gamma primitive label orbit]
 (1-u^N1(gamma) v^N0(gamma)).                     (6)
```

**Proof.**  Insert (3) into the logarithm and use (2).  The exceptional term
sums exactly:

```text
sum_(n>=1) v^n/n - sum_(k>=1) 3 v^(3k)/(3k)
 =-log(1-v)+log(1-v^3)
 =log(1+v+v^2).
```

Thus `log Z_140=-log(1-u-v^3)+log(1+v+v^2)`, which gives (4) and (5).

For (6), every intrinsic periodic label point has a unique primitive label
orbit and repetition exponent.  A primitive orbit of length `m` supplies its
`m` rooted points at each repeated period `mk`; its logarithmic contribution
is `sum_(k>=1) q^k/k=-log(1-q)`, where
`q=u^N1 v^N0`.  Each total degree contains finitely many periodic label
words, so the regrouping is coefficientwise finite.  Exponentiating gives
(6).  ∎

The distinction in (5) is essential: `D_cov` is the determinant of the cover
matrix, whereas `D_140` is the intrinsic inverse zeta.  No separate natural
Fredholm operator on label space is constructed for the rational correction.

## Corollary 5: suspension and nonlattice clock

Under

```text
u=z exp(-s),       v=z exp(-sqrt(2)s),
```

equation (6) becomes

```text
D_140(z,s)=product_gamma
 (1-z^|gamma| exp(-s ell(gamma))).                 (7)
```

The label fixed points `[1]` and `[0]` have lengths `1` and `sqrt(2)`.
Their irrational ratio proves the suspension is nonlattice.  It also rules
out a nonzero common imaginary period for the fixed-`z=1` specialization:
invariance under `s -> s+iT` would
force `exp(-iT)=exp(-iT sqrt(2))=1`, hence `T=0`.

The positive roof entropy parameter is the unique positive solution of

```text
1-exp(-h)-exp(-3sqrt(2)h)=0.
```

Indeed the left side is continuous, equals `-1` at zero, tends to `1`, and
has strictly positive derivative.  The exceptional rational factor is finite
and nonzero on the positive real axis and does not move this leading cover
pole.

## Route-A conclusion and open risks

The strictly sofic source and its exceptional-orbit correction are exact, but
they provide no target divisor, functional equation, Gamma factor, counting
law, arithmetic/local data, natural Fredholm owner for `D_140`, self-adjoint
or unitary lift, Hilbert--Polya operator, or Route-B authorization.
Conservative verdict: `(A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`, overall
`ROUTE_A_EXPLORATORY`.
