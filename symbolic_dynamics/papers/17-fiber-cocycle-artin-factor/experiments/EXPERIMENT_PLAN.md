# SD-C19 Exact Experiment Plan

**Problem:** Determine whether the intrinsic `C2` subset-degree cocycle gives a
lawful same-object Artin factor, whether functorial one-letter cleanliness has
any noncyclic escape, and whether the exact factor is arithmetically selective.

**Method thesis:** The parity fiber gives an exact recurrent character factor
at `z=1`; operator-coherent one-letter atom locality forces the cyclic degree
rule, while primitive lifts and inventory controls stop RH promotion.

**Date:** 2026-08-14

## Claim map

| Claim | Minimum convincing evidence | Blocks |
|---|---|---|
| C1: genuine same-object Artin factor | formal `2x2`, character, trace/repetition, and `C_m` certificates with zero mismatch | B1 |
| C2: functorial clean one-letter rules are cyclic and nonselective | exhaustive naturality rules and exact inventory controls | B3, B5 |
| Anti-claim: atom-local factors repair primitive arithmetic | exact base/lift census showing clock multiplication and mixed lifts | B2 |
| Anti-claim: the theorem closes transition dependence | coboundary and noncoboundary transition controls | B4 |

## Frozen blocks

### B1 — same-object determinant

- Systems: `C2`, `n=1..10`; `C_m`, `m=2..8`, all characters.
- Checks: sparse multivariable determinant; 300 collapsed trace/repetition
  coefficients; seven regular local permutation determinants.
- Success: every coefficient, phase, and block-product mismatch equals zero.
- Failure: stop before any Artin-factor claim.
- Priority: MUST-RUN.

### B2 — dynamics and primitive lifts

- Systems: `C2` fiber graph through `n=10`; primitive base necklaces through
  `n=5`, base length `r=10`, group order `m=8`.
- Checks: transitivity/mixing, exact minimal-period recurrence,
  `q=m/gcd(m,c)`, and `gcd(m,c)` lifted-cycle multiplicity.
- Success/stop: frozen pilot counts reproduce; mixed immediate closures and
  singleton clock multiplication remain.
- Priority: MUST-RUN.

### B3 — naturality rigidity

- Systems: all cardinality tables `r_1=1`, maximum degree `2..6`, `m=2..8`.
- Check: first operator-coefficient leakage and selected-character invisibility.
- Success: exactly one operator-coefficient-clean power table per one of 35
  cutoff cells.
- Priority: MUST-RUN.

### B4 — cohomology and transition boundary

- Coboundaries: complete symbolic presentations on 2–4 vertices, cycles through
  length six.
- Transition controls: two-atom subset alphabet and four exact `C2` rules.
- Success: all coboundaries are gauge-trivial; every noncoboundary negative
  control has a periodic witness; strict symbol change leaks at `x^2 y^2`.
- Priority: MUST-RUN.

### B5 — proves-too-much controls

- Inventories: prime, composite-only, shuffled-prime, random rational, and the
  free-commutative formal source.
- Cutoff/seeds: ten atoms, seeds `17000..17015`.
- Metric: exact-identity pass rate and margin relative to the prime inventory.
- Success/stop: `64/64` exact and margin zero, triggering
  `STOP_ARITHMETIC_SELECTIVITY / PROVES_TOO_MUCH`.
- Numeric determinant equality across different inventories is not claimed.
- Priority: MUST-RUN.

## Run order

| Milestone | Runs | Gate | Cost |
|---|---|---|---|
| M0 sanity | two-atom formal, base/lift, transition unit tests | all three pass | CPU subsecond |
| M1 factor | B1 | `GO_GENUINE_ARTIN_FACTOR` | CPU seconds |
| M2 primitives | B2 | `STOP_PRIMITIVE_LIFT` | CPU seconds |
| M3 rigidity/boundary | B3+B4 | unique power rule; periodic witnesses | CPU seconds |
| M4 controls | B5 | pass-rate margin zero | CPU seconds |
| M5 freeze | 14 tests, parse/LF/cache/diff audit, SHA, double run | all pass | CPU under one minute |

## Data and compute

- GPU-hours: `0`.
- External dataset/network: none.
- Arithmetic: integers, `Fraction`, sparse formal polynomials, exact SymPy.
- Forbidden: target zeros, floating root fitting, cross-family repairs.

## Final checklist

- [x] Claims and anti-claims frozen.
- [x] All cutoffs and seeds predeclared.
- [x] Signed repetitions preserved.
- [x] Character blocks separated from the whole regular determinant.
- [x] Primitive base counts separated from lifted-cycle counts.
- [x] Controls and stop decisions mandatory.
