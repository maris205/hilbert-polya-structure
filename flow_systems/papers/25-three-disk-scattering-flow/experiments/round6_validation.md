# P25 Round-6 validation report

## Material Passport

- Origin Skill: `ars-codex:academic-research-suite` plus experiment validation
- Origin Stage: Stage 1 research
- Verification Status: `VERIFIED / REPRODUCIBLE`
- Typed candidate: `THREE-DISK-NO-REPEAT-MASLOV-SYMBOLIC`
- Core-output SHA-256: `003321db003a71ae2713400e553701ad75db26c22655cff99cbbb25bcf2d1f77`

## Exact replay

- Frozen oriented primitive owners through length 12: `747`.
- Every lengthwise ledger count equals the exact Mobius-inversion count.
- Primitive Euler product, trace exponential, and reciprocal determinant agree
  coefficient-by-coefficient modulo `z^13` for both conventions.
- Unweighted denominator: `[1, 0, -3, -2]`.
- Collision-phase denominator: `[1, 0, -3, 2]`.
- Coefficient mismatches: `0`.

## Theorem and decision

```text
zeta_0(z)  = 1 / ((1-2z)(1+z)^2)
zeta_pi(z) = zeta_0(-z) = 1 / ((1+2z)(1-z)^2)
```

The collision-parity phase is therefore an exact `z -> -z` substitution.  It
does not supply arithmetic specificity.

## Route and scope boundary

The formal tuple

```text
(A0_FAIL, A1_PASS_ANALYTIC, A2_ANALYTIC_DETERMINANT, A3_FAIL, A4_FAIL)
overall = ROUTE_A_REJECTED
```

belongs only to the unit-roof symbolic suspension.  It is not a tuple for the
physical Euclidean-flight-length billiard, and its A2 coordinate is not a
Gutzwiller--Voros, exact multiple-scattering, quantum-resonance, Riemann, or
Dedekind determinant result.  The physical P25 tuple remains `UNASSIGNED`.
Route B remains closed.
