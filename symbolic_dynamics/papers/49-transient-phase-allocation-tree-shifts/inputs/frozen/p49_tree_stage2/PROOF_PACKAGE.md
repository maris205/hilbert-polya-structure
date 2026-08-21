# Self-contained proof package

## Claim status

Claims C0--C7 in `THEOREM_CONTRACT.md` are `PROVABLE AS STATED` under their
displayed hypotheses.  C4's necessity clause is
`PROVABLE AFTER WEAKENING / EXTRA ASSUMPTION`, where the extra assumption is
the explicitly declared full nonzero Fourier support of `c`.  Every item in
the nonclaim table is `NOT CURRENTLY JUSTIFIED` and is not used below.

The proof imports no BLW dimension equality or spectral upper bound.

## Dependency map

```text
Lemma 1 (cylinder dimension)
  -> Lemma 3 (complete cyclic block)
  -> Lemma 4 (fixed feeder stratum)
  -> Theorem 5 (finite one-level optimizer)
  -> Theorem 10 (L-level optimizer and convergence)

Lemma 2 (periodic weighted limit)
  -> Lemma 3
  -> Lemma 4

Lemma 6 (mean and invertibility of H)
  -> Theorem 7 (saturation)
  -> Theorem 8 (Fourier/divisibility)
  -> Theorem 10

Theorem 7
  -> Theorem 9 (p=2 formulas)
  -> Corollary 11 (four-state counterexample)
```

## Lemma 1: equiprobable cylinder dimension

Let `X` be one of the fixed-phase strata appearing in the contract.  Suppose
its distinct depth-`n` cylinders number `P_n`, and suppose a compatible Borel
probability measure `mu` assigns every such cylinder mass `1/P_n`.  Then

```text
dim_H X = liminf_n log(P_n)/|Delta_n|.
```

### Upper bound

Let the liminf be `L`, and fix `s>L`.  There is a subsequence `n_q` with
`log P_(n_q) <= (s-epsilon)|Delta_(n_q)|` for some `epsilon>0`.  The
depth-`n_q` cylinders cover `X`, each with diameter at most
`exp(-|Delta_(n_q)|)`.  Hence their total `s`-cost is at most

```text
P_(n_q) exp(-s|Delta_(n_q)|)
<= exp(-epsilon|Delta_(n_q)|) -> 0.
```

Thus the `s`-dimensional Hausdorff measure vanishes and `dim_H X<=L`.

### Lower bound

Fix `0<=s<L`.  For all sufficiently large `n`,
`P_n>=exp(s|Delta_n|)`.  A ball whose radius lies between two consecutive
metric scales is a depth cylinder at the corresponding scale, intersected
with `X`.  If it is a depth-`n` cylinder, then

```text
mu(B) <= 1/P_n <= exp(-s|Delta_n|) <= radius(B)^s.
```

The finitely many larger scales are absorbed into one constant.  The mass
distribution argument gives `dim_H X>=s`; letting `s` increase to `L` proves
the lemma.  If `L=0`, the lower inequality is automatic.  A singleton is
therefore handled without a separate positive-dimension assumption.

The required measures exist in this package because, after phases are
fixed, labels at every vertex are chosen independently and uniformly within
the forced phase.  Their finite-dimensional marginals are compatible.

## Lemma 2: periodic weighted limit

Let `x=(x_0,...,x_(p-1))` be any real `p`-periodic vector and let

```text
S_(n,h)(x) = sum_(ell=0)^n d^ell x_(h+ell).
```

If `n` tends to infinity with `n congruent r mod p`, then

```text
S_(n,h)(x)/|Delta_n| -> H_(h+r)(x).
```

Indeed, put `u=n-ell` and use `|Delta_n|=(d^(n+1)-1)/(d-1)`.  The limit is

```text
(d-1)/d * sum_(u=0)^infinity d^(-u) x_(h+r-u).
```

Writing `u=t+kp`, with `0<=t<p`, and summing the geometric series gives

```text
(d-1)/(d^p-1)
* sum_(t=0)^(p-1) d^(p-1-t) x_(h+r-t),
```

which is `H_(h+r)(x)`.  This also proves convergence when `p=1`.

## Lemma 3: the complete cyclic block

Fix a root phase `h`.  Completeness of every bipartite block means that the
label at each vertex may be chosen independently from its forced phase.
There are `d^ell` vertices at level `ell`, so the exact prefix count is

```text
P_(n,h) = product_(ell=0)^n a_(h+ell)^(d^ell).
```

Taking logs and applying Lemma 2 with `x=c` shows that the `p` residue
subsequences have limits

```text
H_h(c), H_(h+1)(c), ..., H_(h+p-1)(c).
```

Their minimum is independent of `h`.  Lemma 1 gives the dimension of the
root-phase stratum, and the whole cyclic block is the finite union of the
`p` root-phase strata.  Hausdorff dimension of a finite union is the maximum
of the member dimensions.  All members have the same value, hence

```text
dim_H T_C(a) = min_j H_j(c).
```

For later reference, every row of `C(a)^p` has row sum `product_j a_j`.
The all-one vector is therefore an eigenvector with that eigenvalue, while
the maximum-row-sum bound supplies the reverse spectral inequality.  Thus

```text
rho(C(a))^p = product_j a_j,
bar(c) = log rho(C(a)).
```

This last calculation is elementary and does not invoke an imported
dimension-versus-spectral-radius statement.

## Lemma 4: a fixed one-level feeder stratum

Fix an ordered phase assignment of the `d` children of `r`, and let `m_s`
be the number assigned phase `s`.  For total depth `n>=1`, the exact count is

```text
P_(n,m) = product_s product_(ell=0)^(n-1)
          a_(s+ell)^(m_s d^ell).
```

Define `b_k=(1/d) sum_s m_s c_(s+k)`.  Then

```text
log P_(n,m) = d * sum_(ell=0)^(n-1) d^ell b_ell.
```

Since

```text
d|Delta_(n-1)| / |Delta_n| -> 1,
```

Lemma 2 shows that the residue limits of
`log P_(n,m)/|Delta_n|` are exactly the cyclic list `H_j(b)`.  Lemma 1 gives

```text
dim_H X_m = min_j H_j(b).
```

Linearity and circular covariance of `H` also give, term by term,

```text
H_j(b) = (1/d) sum_s m_s H_(s+j)(c).
```

This proves both displayed versions of `D_1(m;c)`.

## Theorem 5: the finite one-level optimization

There are only `p^d` ordered child-phase assignments.  The root-`r` stratum
is their finite union.  Grouping assignments by their weak composition and
using Lemma 4 yields

```text
dim_H(root-r stratum)
= max_(m_s>=0, sum m_s=d) D_1(m;c).
```

The whole Markov hom tree-shift is the finite union of this stratum and the
core-root strata.  For any phase `s`, the concentrated composition
`m_s=d`, `m_t=0` for `t!=s`, gives

```text
D_1(m;c) = min_j H_(s+j)(c) = dim_H T_C(a).
```

Thus the feeder maximum already dominates the core, proving C2.  If a
declared model admits only a finite composition set `F`, the identical
finite-union proof gives `max_(m in F) D_1(m;c)` for its feeder stratum.

Transience is essential to this proof: a return edge would allow arbitrarily
many feeder visits and destroy the finite decomposition.

## Lemma 6: mean preservation and invertibility of `H`

The weights defining every `H_j` sum to one.  Summing over `j` and using
cyclic reindexing gives

```text
(1/p) sum_j H_j(x) = (1/p) sum_j x_j.
```

The circular operator `x -> H(x)` is invertible.  To see this without an
external theorem, evaluate its kernel on a `p`th root of unity `z`.  Apart
from the positive normalization, its multiplier is

```text
sum_(t=0)^(p-1) d^(p-1-t) z^t
= (d^p-z^p)/(d-z)
= (d^p-1)/(d-z),
```

which is nonzero because `d>=2` and `|z|=1`.  Therefore

```text
H(x) is constant if and only if x is constant.
```

The same calculation shows that `H` preserves the set of nonzero Fourier
modes: its multiplier vanishes at none of them.

## Theorem 7: exact saturation

The mean of `b(m)` is `bar(c)`.  By Lemma 6, the mean of the `p` values
`H_j(b(m))` is also `bar(c)`.  Their minimum therefore satisfies

```text
D_1(m;c) <= bar(c).
```

The minimum equals the mean exactly when all `p` values equal the mean.
By invertibility in Lemma 6, this is equivalent to `b(m)` being constant,
which is precisely

```text
sum_s m_s c_(s+k) is independent of k.
```

Exponentiation is injective, so this is equivalent to

```text
product_s a_(s+k)^(m_s) is independent of k.
```

This proves C3 using exact integers, with no approximate comparison of
logarithms.

## Theorem 8: Fourier support and divisibility

If `p|d`, choose `m_s=d/p`.  Every shifted convolution sum is then
`(d/p)sum_s c_s`, so Theorem 7 gives saturation.

For necessity under the declared hypothesis, take the discrete Fourier
transform of

```text
b_k=(1/d)sum_s m_s c_(s+k).
```

Up to the harmless reversal dictated by the transform convention, every
nonzero mode is a product

```text
hat(b)(q) = d^(-1) hat(m)(-q) hat(c)(q).
```

If every nonzero `hat(c)(q)` is nonzero and `b` is constant, then every
nonzero Fourier mode of `m` vanishes.  Inverse Fourier transformation makes
`m` constant.  Since its entries are integers summing to `d`, this is
possible exactly when `p|d`, with `m_s=d/p`.

The hypothesis cannot be deleted.  For

```text
p=4, d=2, a=(2,3,2,3), m=(1,1,0,0),
```

the four shifted products in Theorem 7 are all `6`.  Thus the composition
saturates although `p` does not divide `d`.  Here `c` has a missing nonzero
Fourier mode because it has period two.

## Theorem 9: the `p=2` formulas

For `p=2`, the definition reduces to

```text
H_0(c) = (d c_0+c_1)/(d+1),
H_1(c) = (d c_1+c_0)/(d+1).
```

Their mean is `mu=(c_0+c_1)/2` and their absolute difference is
`(d-1)|c_1-c_0|/(d+1)`.  Taking the smaller value proves

```text
component = mu - (d-1)Delta/(2(d+1)).
```

For `m=(k,d-k)`, the two entries of `b` have difference

```text
b_0-b_1 = ((2k-d)/d)(c_0-c_1)
```

and mean `mu`.  Applying the just-proved two-phase calculation to `b`
gives

```text
D_1((k,d-k);c)
= mu - (d-1)|2k-d|Delta/(2d(d+1)).
```

If `d` is even, the minimum possible `|2k-d|` is zero.  If `d` is odd, it is
one.  This proves the even/odd optimizer.  When `Delta>0`, comparison with
the component penalty proves strict improvement, and Theorem 7 gives exact
even-arity saturation.  When `Delta=0`, the penalty vanishes for every `k`,
so every composition saturates.  These cases exhaust the boundary.

## Theorem 10: the `L`-level feeder

Fix the top transient root `r_0` and a phase assignment of the `d^L` core
roots at level `L`, with composition `m`.  For total depth `n>=L`, exact
counting gives

```text
P_(n,L,m) = product_s product_(ell=0)^(n-L)
            a_(s+ell)^(m_s d^ell).
```

Because

```text
|Delta_(n-L)|/|Delta_n| -> d^(-L),
```

the proof of Lemma 4 gives the residue limits

```text
(1/d^L) sum_s m_s H_(s+j)(c),
```

and Lemma 1 proves the exact `D_L(m;c)` formula.  The phase assignments are
finite in number, so the top-root stratum has dimension `D_L^*(c)`.

The full Markov shift also permits roots in the core and at later transient
states.  A root at `r_q` has an optimizer with only `L-q` transient levels.
If `m` is a composition of `d^K`, then `d m` is a composition of
`d^(K+1)` and

```text
D_(K+1)(d m;c) = D_K(m;c).
```

Hence `D_K^*` is nondecreasing in `K`.  Concentrated compositions also
dominate the core value.  Therefore the largest stratum is the top-root
stratum and the full shift has dimension `D_L^*(c)`.

The mean-preservation proof of Theorem 7 applies verbatim with denominator
`d^L`.  Thus

```text
D_L(m;c)=bar(c)
iff sum_s m_s c_(s+k) is independent of k.
```

This is the exact saturation law at every finite level.  Uniform allocation
is available when `p|d^L`; necessity needs the same Fourier-support
hypothesis as Theorem 8.

It remains to separate finite exact optimization from convergence.  Put
`N=d^L`, and choose a balanced composition whose entries are
`floor(N/p)` or `ceil(N/p)`.  Write `m_s=N/p+e_s`.  Then

```text
sum_s e_s=0, |e_s|<1,
```

and for every residue `j`,

```text
|(1/N)sum_s m_s H_(s+j)(c)-bar(c)|
<= p max_j H_j(c)/N.
```

The optimized minimum is no smaller than this balanced minimum and no
larger than its residue mean `bar(c)`.  Therefore

```text
0 <= bar(c)-D_L^*(c) <= p max_j H_j(c)/d^L -> 0.
```

This proves convergence without replacing the exact denominator `d^L` by a
continuous simplex.  A restricted feeder family inherits the convergence
only if it contains compositions with the displayed `O(1)` coordinate
discrepancy; no such access is assumed silently.

## Corollary 11: four-state strict max-SCC failure

Take `d=2`, phase sizes `(1,2)`, and states `(r,a,b1,b2)` with adjacency

```text
0 1 1 1
0 0 1 1
0 1 0 0
0 1 0 0.
```

The cyclic core has `c=(0,log 2)`.  Theorem 9 gives

```text
dim_H(core) = log(2)/3.
```

For the feeder composition `(1,1)`, even-arity saturation gives

```text
D_1((1,1);c) = bar(c) = log(2)/2.
```

Theorem 5 and the universal mean upper bound show that this is the dimension
of the full shift.  The transient root therefore creates Hausdorff dimension
strictly exceeding the dimension of the only cyclic essential SCC.  No BLW
spectral upper bound is used.

## Boundary and hypothesis audit

- `p=1`: `H_0(c)=c_0`; all compositions are the sole one-part composition,
  and every formula reduces to `log a_0`.
- `a_j=1`: `c_j=0`; prime-factor and measure arguments remain valid.  If
  every `a_j=1`, every stratum is finite or singleton and all dimensions are
  zero.
- Zero entries in `m` are allowed and are used by concentrated controls.
- `L=1` in Theorem 10 is exactly Theorem 5.
- `d=1`, `a_j=0`, incorrect composition totals, incomplete cyclic blocks,
  return edges, and unrestricted-composition claims for incomplete feeder
  rows are outside the contract and are rejection controls.
- All limits use the exact BLW tree-metric denominator `|Delta_n|`; the
  feeder denominator `d^L` appears only after taking the ratio
  `|Delta_(n-L)|/|Delta_n|`.

## Remaining proof risks

No internal logical gap remains in C0--C7 under the frozen hypotheses.  The
following are deliberately unresolved rather than silently generalized:

1. arbitrary reducible graphs with several communicating cyclic blocks;
2. feeder return edges or other non-transient phase reuse;
3. incomplete phase-to-phase incidence blocks;
4. finite-level divisibility necessity when Fourier modes of `c` vanish;
5. any claim depending on a version-sensitive BLW equality clause.

Package status remains `HOLD_FOR_INDEPENDENT_STAGE2_AUDIT`.
