# P27 Round-7 theorem — owner-preserving Euler factors escape every fixed prefix

Date: **2026-08-28**

## Material Passport

- Origin skill: `ars-codex:academic-research-suite`
- Workflow: ARS Stage-1 theorem development plus deterministic replay
- Mathematical owner: a fixed primitive conjugacy owner in a descending
  normal residual tower with one unchanged hyperbolic-arclength clock
- Freeze SHA-256:
  `5b136585689f2c4c79ccdd3eb418345100f1261032ad7d2f42efec0bcf576206`
- Core-output SHA-256:
  `551e92315c46dcbb4d01bd84688bb77eca8fcd4a6c2eaec202fe04f621275845`
- Target data: none

## Setting

Let `Gamma=Gamma_1 >= Gamma_2 >= ...` be descending normal finite-index
subgroups with trivial intersection.  Let `g` be a primitive infinite-order
element of `Gamma`, and write

```text
o_n(g) = order of g Gamma_n in Gamma/Gamma_n.
```

For a hyperbolic realization, let `ell(g)>0` be the base geodesic length and
keep the same arclength clock at every level.  The Round-4 theorem proves that
`o_n(g)` divides forward and tends to infinity.  If `g` is primitive, the axis
stabilizer calculation gives

```text
Gamma_n intersect <g> = <g^(o_n(g))>,
```

so the lifted owner has minimal length `o_n(g) ell(g)`.

## Theorem — coefficientwise same-owner escape

`[PROVED]` Introduce the owner variable `x_g=exp(-s ell(g))`.  At level `n`,
the unweighted reciprocal factor of one lifted owner is

```text
E_(n,g)(x_g) = (1-x_g^(o_n(g)))^(-1).
```

Then for every fixed integer `N>=0`, there is `n_0(g,N)` such that

```text
E_(n,g)(x_g) = 1 mod x_g^(N+1)
```

for every `n>=n_0(g,N)`.  Hence `E_(n,g)` converges coefficientwise to 1,
not to the nontrivial base factor `(1-x_g)^(-1)`.

The conclusion is unchanged if the complete normal-cover contribution has a
finite level-dependent lift multiplicity `m_n(g)` or a finite scalar weight
`w_n(g)`:

```text
(1-w_n(g)x_g^(o_n(g)))^(-m_n(g)) = 1 mod x_g^(o_n(g)).
```

Only the first possible nonconstant degree matters.

### Proof

The geometric series for `E_(n,g)` has support

```text
0, o_n(g), 2o_n(g), 3o_n(g), ... .
```

Because `o_n(g)->infinity`, choose `n_0` with `o_n(g)>N` for all
`n>=n_0`.  Every coefficient in degrees 1 through `N` is then zero.  A finite
multiplicity or scalar weight changes coefficients at supported degrees but
cannot create a degree below `o_n(g)`.  QED.

## Corollary — finite panels and fixed time windows

For a fixed finite set `F` of primitive base owners, all `o_n(g)` diverge.
Therefore their minimum diverges, and the multivariate product

```text
product_(g in F) E_(n,g)(x_g)
```

converges coefficientwise to 1.  Equivalently, because `F` is finite and all
`ell(g)>0`, the minimum lifted period

```text
min_(g in F) o_n(g) ell(g)
```

leaves every fixed physical-time window.  No fixed finite base-owner panel
can supply a nontrivial coefficientwise-stable same-owner Euler prefix.

## Exact finite replay

The Round-7 artifact unifies six frozen loop/owner rows over eight levels:

- 24 cusped `Gamma(3n!)` rows have exact quotient orders.  Their base
  conjugacy primitivity remains `NOT_ESTABLISHED`, so their formal factors are
  explicitly only loop-order support diagnostics, not certified primitive
  zeta factors.
- 24 closed genus-2 rows have primitivity proved by primitive homology.  Their
  homology orders are certified lower bounds on the unenumerated full quotient
  orders; no exact full order is fabricated.

For every row, the artifact records that coefficients through degree
`lower_bound-1` vanish.  A second ledger asks for fixed degrees
`1,2,4,...,256`: 54 owner/degree diagnostics are evaluated.  The finite rows
are illustrative certificates; the all-level conclusion comes from the proof,
not extrapolation.

## Route-A consequence

Rounds 1--6 already prove that the inverse-limit periodic set is empty, so A1
fails.  Round 7 sharpens the downstream statement: even the finite-level
factors attached to a fixed base owner cannot retain a nontrivial coefficient
prefix under the unchanged clock.  They disappear from every bounded degree
and time window.

Thus the same-owner record remains

```text
(A0_WEAK_ARITHMETIC_RELATION,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)
overall = ROUTE_A_REJECTED.
```

The theorem does not say that every conceivable normalized tower statistic is
trivial.  A collective limit with rescaled time, level-dependent weights, or
new owner aggregation would be a different candidate and must receive a new
object, clock, normalization, determinant, and source lock before evaluation.

## Limitations and disclosure

The finite replay uses only six frozen rows and does not machine-prove the
group-theoretic asymptotic theorem.  It does not justify interchanging an
infinite owner product with the tower limit.  The nine external positioning
locators from Round 6 remain `HUMAN_CONFIRMATION_PENDING`; no author-read state
is inferred.  AI-assisted research and code generation were used; the theorem
is supplied with the explicit proof above and exact source-bound artifacts.
