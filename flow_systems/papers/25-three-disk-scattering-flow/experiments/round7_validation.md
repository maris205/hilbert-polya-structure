# P25 Round-7 validation report

## Material Passport

- Origin skill: `ars-codex:academic-research-suite`
- Origin stage: ARS Stage 1 research
- Candidate: `P25-Q-SYMBOL-NO-REPEAT-PHASE-CALIBRATOR`
- Freeze SHA-256: `41fec487b1473fe65adeaadebde769cdf065d67db7f53232e8202879a6fabddb`
- Core SHA-256: `9c3daaa1feffa23090cc4edf5c3cdf0398389f814ef4f0f6b14cad254f23d4d9`

## Exact replay

- The theorem domain is every integer `q>=2`; the finite replay is `q=2,...,8`.
- Exact replay degrees: `0,...,12`.
- Count rows: `84`; direct-trace mismatches: `0`.
- Prefix rows: `182`; coefficient mismatches: `0`.
- Primitive-count Euler products, trace exponentials, and reciprocal determinants agree exactly.

## Theorem

```text
tr(A_q^n) = (q-1)^n + (q-1)(-1)^n
P_n(q) = (1/n) sum_(d|n) mu(d) tr(A_q^(n/d))
det(I-u z A_q) = (1-(q-1)u z)(1+u z)^(q-1)
zeta_(q,-1)(z) = zeta_(q,+1)(-z)
```

## Route boundary

The exact A1--A2 tuple belongs only to this non-arithmetic unit-roof symbolic
family.  A0 fails by construction, so the overall Route-A verdict is
`ROUTE_A_REJECTED`.  This theorem supplies a universal negative-control
calibrator, not a physical three-disk determinant or a target-divisor result.
The physical flow remains `UNASSIGNED`; Route B remains closed.
