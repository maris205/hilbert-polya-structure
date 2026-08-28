# Paper 26 Round-8 complete-taxonomy freeze

Date: **2026-08-28**

## Frozen question

Can the Round-7 exact Schreier-homology classifier be extended, without a
floating-point zero test, from the four `p=5` survivors to all 138 frozen
Round-4 Hecke cycle-owner instances and all 55 word/prime groups, so that the
Round-6 quadratic moment verdicts become exact and exhaustive?

## Frozen inputs

- `results/round4_hecke_cycle_ledger.csv`, SHA-256
  `f906df349b8f1fa2864fed592792e0fff63ba246a069179b7bd8cfdf46520662`;
- `results/round6_quadratic_degree_moment_ledger.csv`, SHA-256
  `f95e1435c9293f8e008cebf80084ea2b522b76186dbd684b5e3997c5e588edea`;
- the Round-7 exact model
  `Gamma_0(11)\PSL(2,Z)=P^1(F_11)` with 12 cosets, 24 Schreier
  arcs, relation rank 21, rational `Y_0(11)` homology dimension 3, one cusp
  direction, and compact dimension 2; and
- the predeclared scalar laws `lambda_p=a_p`, `a_p^2`, and the explicitly
  secondary negative control `a_p^2-p`.

No orbit, word, prime, scalar law, or survivor is selected after the exact
classification is seen.

## Exact decision rule

Write a rational homology class as `h=(x,y,z)` in the frozen Schreier
coordinates.  The real involution is frozen as

```text
tau(x,y,z)=(-x,y+z,-z),
h+tau(h)=(0,2y+z,0),
k(h)=2y+z.
```

The source classes have `k!=0`.  For every cycle owner `delta`, the normalized
real newform-period ratio is therefore frozen as the exact rational number

```text
rho(delta)=k(delta)/k(source).
```

The four mutually exclusive instance classes are:

1. `FULL_COMPLEX_SOURCE_KERNEL`: the class is zero in compact homology;
2. `REAL_PROJECTION_ONLY_KERNEL`: the compact class is nonzero but `k=0`;
3. `TRUE_REAL_PROJECTION_NONKERNEL`: `k!=0`; and
4. `DEGENERATE_OR_OTHER`: normalization or a required exact certificate is
   unavailable.  This category fails closed and is not silently merged with a
   kernel.

For degree `d`, freeze

```text
M_d = sum_(deg(delta)=d) rho(delta)^2.
```

For a scalar law `lambda_p`, the all-`s` second-variation group criterion is

```text
M_1=lambda_p,
M_d=0 for every d>1.
```

Because `M_d` is a rational sum of squares, the nonunit-degree obligation is
equivalent to every degree-`d` owner lying in the exact real-projection
kernel.  Round-6 binary64 values are retained only as cross-checks; they do
not decide any zero.

## Significant-result gate

Round 8 passes only if all conditions hold:

- 138/138 owner instances are regenerated exactly and classified in one of
  the four disjoint categories;
- 55/55 word/prime groups are classified for all three frozen scalar laws;
- the exact classifier accounts for all 51 primary failures and all four
  primary survivors, including the full-kernel/projection-only split;
- `DEGENERATE_OR_OTHER=0`, unresolved rows are zero, and no float is used to
  prove a zero;
- two isolated builds are byte-identical and the checked-in artifacts pass
  verify-only replay; and
- Stage 1, the conservative Route-A tuple, A2 non-entry, and the Route-B
  prohibition remain unchanged.

## Claim boundary

This is a complete exact taxonomy of the **frozen finite output multiset**.  It
is not a complete enumeration of primitive `Gamma_0(11)` conjugacy classes,
does not deduplicate conjugate owners across instances, and does not construct
or continue a global dynamical determinant.  It uses no rational-prime target
table and no Riemann-zero data.  Formal status remains

```text
(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)
```

with `ROUTE_A_EXPLORATORY`; Route B is not invoked.
