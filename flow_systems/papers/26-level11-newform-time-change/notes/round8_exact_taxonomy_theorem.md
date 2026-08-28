# Round-8 theorem — complete exact homology and moment taxonomy

Evidence status: **PROVED** for the frozen 138-instance / 55-group finite
ledger.  Scope: **Stage 1 / Route A A0--A1**.

## Theorem 1 — exact real-period coordinate

In the frozen Schreier model of `Y_0(11)`, rational homology has coordinates
`(x,y,z)`, the cusp direction is `Q(-1,0,0)`, and compact homology is the
two-dimensional quotient by that direction.  The real involution induced by
`z -> -conjugate(z)` acts by

```text
tau(x,y,z)=(-x,y+z,-z).
```

Consequently its compact `+1` eigenspace is one-dimensional and

```text
h+tau(h)=(0,k(h),0),  k(h)=2y+z.
```

For every frozen source owner `M`, `k(M)` is nonzero.  If `delta` is any of
the 138 frozen Hecke cycle owners, linearity of integration and the real
structure give

```text
Re integral_delta(omega_f) / Re integral_M(omega_f)
  = k(delta)/k(M) in Q.
```

Thus real-period vanishing is decided exactly by `k(delta)=0`; no numerical
tolerance is involved.  Since `X_0(11)` has genus one, the complex period of
the normalized holomorphic differential vanishes exactly when the compact
homology class vanishes.

### Proof certificate

Schreier rewriting for
`Gamma_0(11)\PSL(2,Z)=P^1(F_11)` produces 24 arcs and 35
relations of rank 21.  The resulting three exact dual coordinates contain one
cusp direction.  Applying the integral conjugation map to an exact rational
basis gives the displayed involution matrix

```text
[[-1,0,0],
 [ 0,1,1],
 [ 0,0,-1]].
```

The builder checks this formula on every frozen owner.  Quotienting the cusp
direction leaves one `+1` and one `-1` compact direction.  Real integration
factors through the `+1` direction, establishing the ratio formula.  Genus
one makes the period map on compact real homology injective, proving the full
complex-kernel clause.

## Theorem 2 — exhaustive instance taxonomy

The 138 owner instances split exactly and mutually exclusively as follows:

| prime | full complex kernel | real-projection-only kernel | true nonkernel | total |
|---:|---:|---:|---:|---:|
| 2 | 0 | 0 | 18 | 18 |
| 3 | 0 | 0 | 22 | 22 |
| 5 | 2 | 2 | 26 | 30 |
| 7 | 0 | 0 | 30 | 30 |
| 13 | 0 | 0 | 38 | 38 |
| **all** | **2** | **2** | **134** | **138** |

There are no degenerate, floating-artifact, or unresolved instances.  The two
full kernels are the degree-five owners for `LRRLRRR` and `LLRLLRLR` at
`p=5`.  The two projection-only kernels are the degree-five owners for
`LLLRLLRLR` and `LLLRLRLLR` at `p=5`.

## Theorem 3 — exact quadratic-moment equivalence

For a word/prime group, put

```text
rho_delta = k(delta)/k(M),
M_d = sum_(deg(delta)=d) rho_delta^2.
```

For any predeclared `p`-only scalar `lambda_p`, the finite all-`s`
second-variation recurrence is equivalent to

```text
M_1=lambda_p,
M_d=0 for all d>1.
```

Every `M_d` is a nonnegative rational sum of squares.  Therefore, for `d>1`,
`M_d=0` if and only if every degree-`d` output owner is a full or
real-projection-only kernel.  This proves that the quadratic-moment residual
criterion and the exact kernel taxonomy are equivalent on all nonunit-degree
bins.

## Corollary — all 55 groups and three frozen laws

The exact group counts are:

| scalar law | full-kernel survivor | projection-only survivor | true failure | total |
|---|---:|---:|---:|---:|
| `a_p` | 2 | 2 | 51 | 55 |
| `a_p^2` | 2 | 2 | 51 | 55 |
| `a_p^2-p` (secondary control) | 0 | 0 | 55 | 55 |

For each primary law, every group at `p=2,3,7,13` fails.  At `p=5`, seven
groups fail and the same four groups survive, because `a_5=a_5^2=1`, their
degree-one normalized moment is exactly one, and their degree-five moment is
exactly zero.

The failure mechanisms are fully accounted for:

- for `a_p`, all 51 failures violate both the degree-one scalar obligation and
  a nonunit-degree zero obligation;
- for `a_p^2`, 47 failures violate both obligations and four satisfy the
  degree-one obligation but have a true nonkernel at nonunit degree; and
- for the `a_p^2-p` control, 51 violate both obligations, while the four
  primary survivor groups have zero nonunit mass but fail the degree-one
  scalar obligation.

All 165 exact group/law verdicts agree with the inherited Round-6 binary64
statuses, but this agreement is a cross-check rather than the proof.

## Interpretation

The four finite positives are completely explained by topology and
real-structure parity.  They are not evidence for a new primitive
prime-to-orbit assignment or Euler factor.  Conversely, the other 134
instances are exact nonkernels, so the 51/55 primary failures are not
quadrature artifacts.

This strengthens the finite negative result while preserving its boundary:
the positive-word ledger is not a complete primitive conjugacy census, global
cross-instance conjugacy deduplication has not been run, and there is no
global determinant, continuation theorem, A2 root campaign, target-zero
comparison, or Route-B construction.
