# P25 Round-6 theorem — exact symbolic Zeta and collision phase

Date: **2026-08-28**

## Material Passport

- Origin skill: `ars-codex:academic-research-suite`
- Workflow: ARS Stage-1 research plus deterministic validation
- Typed object: `THREE-DISK-NO-REPEAT-MASLOV-SYMBOLIC`
- Freeze SHA-256:
  `ef84094956894cbc6265ae85f9736fce82056e34bbfb162b23b581abdcbf7013`
- Frozen owner-ledger SHA-256:
  `25584d28155ac80f63260830816a9cdf3ec54b8587c07edac600765783ed2736`
- Core-output SHA-256:
  `003321db003a71ae2713400e553701ad75db26c22655cff99cbbb25bcf2d1f77`
- Target data: none

## Typed continuous-time control

This result concerns the unit-roof suspension of the three-symbol no-repeat
collision shift.  Its clock is symbolic collision count, with `z=exp(-s)`.
It is a derived continuous-time calibrator and not the physical exterior
billiard with Euclidean flight-length roof.

Let

```text
A = [[0,1,1],
     [1,0,1],
     [1,1,0]].
```

Primitive owners are oriented primitive cyclic words modulo rotation;
orientation reversal is retained unless it is already a rotation.  Repetitions
are positive traversal powers.  One collision contributes phase `-1`, so an
owner of length `n_p` has phase `epsilon_p=(-1)^(n_p)`.

## Exact theorem

`[PROVED]`:

```text
zeta_0(z)
 = product_p (1-z^(n_p))^(-1)
 = det(I-zA)^(-1)
 = 1 / ((1-2z)(1+z)^2),

zeta_pi(z)
 = product_p (1-(-1)^(n_p)z^(n_p))^(-1)
 = det(I+zA)^(-1)
 = 1 / ((1+2z)(1-z)^2)
 = zeta_0(-z).
```

These equalities hold first as formal power-series identities.  The primitive
Euler products converge absolutely for `|z|<1/2`, equivalently
`Re(s)>log(2)` under `z=exp(-s)`.  The displayed rational determinant formulas
then provide their meromorphic continuation beyond that disk; no Riemann-target
divisor statement is implied.

Indeed, `A` has eigenvalues `2,-1,-1`, so
`tr(A^n)=2^n+2(-1)^n`.  The standard trace-exponential identity gives
`det(I-zA)^(-1)`.  Möbius inversion separates primitive cycles from their
repetitions.  Replacing every step weight by `-z` yields the collision-phase
identity and the exact substitution `z -> -z`.

## Frozen owner replay

The 747 frozen oriented owners through length 12 have exact length counts

```text
n:       2  3  4  5  6  7  8  9  10  11  12
owners:  3  2  3  6  9 18 30 56  99 186 335.
```

Every count equals

```text
(1/n) sum_(d|n) mu(d) tr(A^(n/d)).
```

Three implementations—primitive Euler multiplication, trace exponential, and
reciprocal determinant recurrence—agree exactly in integer/rational arithmetic
through degree 12 for both conventions.  Thus the frozen owners reproduce the
formal-series identities modulo `z^13`, with zero coefficient mismatches.

## Scientific consequence

The source-owned collision phase is genuine but non-discriminative: it merely
reflects the determinant coordinate.  This closes the proposed positive
phase branch inside the symbolic control and strengthens the negative-control
paper:

```text
COLLISION_PARITY_PHASE=z_to_minus_z_exact_substitution
ARITHMETIC_SPECIFICITY=ABSENT
PAPER_DISPOSITION=RETAIN_AS_METHODS_NEGATIVE_CONTROL_PAPER
```

The theorem is not an exact physical Gutzwiller--Voros or multiple-scattering
determinant identity, does not locate quantum resonances, and does not concern
Riemann or Dedekind zeros.
