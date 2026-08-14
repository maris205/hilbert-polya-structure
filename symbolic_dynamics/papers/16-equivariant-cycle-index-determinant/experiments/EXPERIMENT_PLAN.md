# Experiment Plan

**Problem:** Determine exactly what survives when the Paper 15 signed
Koszul-subset shift is lifted from scalar cycle counts to label-equivariant
cycle-index data.

**Method thesis:** A formal Burnside/species ledger detects a nonzero `pqr`
character residual, but arithmetic specialization prevents it from becoming a
character-resolved Fredholm decomposition of the target scalar determinant.

**Date:** 2026-08-14

## Claim map

| Claim | Why it matters | Minimum convincing evidence | Blocks |
|---|---|---|---|
| C1: formal residual | Establishes that scalar cancellation hides genuine label motion | Exact `S_3` sets, character, marks, and power-degree certificate | B1, B2 |
| C2: incompatibility | Prevents a formal character ledger from being oversold as an arithmetic operator | Exact symmetry, rank-one, diagonal, and limit audits | B3, B4, B5 |
| Anti-claim: arithmetic selectivity | Rules out prime-specific interpretation of universal tensor algebra | Composite, shuffled, random, and generic controls | B6 |

## Paper storyline

- Main paper must show the exact `pqr` residual and the fixed-fiber symmetry/
  diagonal-mixed-factor dichotomy.
- Appendix may contain the full `n<=7` character tables and analytic cutoff
  tables.
- No numerical zero comparison, fitting, or unrelated system family is allowed.

## Experiment blocks

### B1 — Squarefree primitive cycle ledger

- **Claim tested:** C1.
- **Task:** Enumerate cyclic ordered set partitions of `[n]`, `n=2..7`, with
  sign `(-1)^(n+m)`; compute conjugacy-class fixed counts and orbit types.
- **Metrics:** exact totals, positive/negative counts, virtual characters,
  cyclic-subgroup marks, orbit-size/stabilizer identities.
- **Success:** frozen counts and `pqr` certificate pass exactly.
- **Failure:** stop C1 and inspect cyclic canonicalization.
- **Priority:** MUST-RUN.

### B2 — Power/Adams firewall

- **Claim tested:** C1 and the scalar-sign firewall.
- **Task:** prove computationally that `r>1` cannot reach squarefree degree;
  compare `b(x)^r` with `b(x^r)` by exact target coefficients; test the `C2`
  sign carrier.
- **Metrics:** integer coefficients and Boolean certificates.
- **Success:** every frozen case passes.
- **Failure:** stop the λ-/power-compatible formulation.
- **Priority:** MUST-RUN.

### B3 — Fixed-fiber symmetry and rank-one visibility

- **Claim tested:** C2.
- **Task:** compute distinct/equal-weight stabilizers and the rank-one isotypic
  dimensions for `n=2..8`.
- **Metrics:** stabilizer order, rank, trivial/nontrivial dimensions and
  determinants.
- **Success:** distinct stabilizer order one; all nontrivial eigenvalues zero
  and determinants one.
- **Failure:** refutes the no-go theorem.
- **Priority:** MUST-RUN.

### B4 — Diagonal analytic lift

- **Claim tested:** C2.
- **Task:** compare the pure Euler determinant with the exact diagonal
  superdeterminant; record every subset-size exponent.
- **Metrics:** exact rational ratio and symbolic mixed-factor certificate.
- **Success:** mismatch for all `n>=2`.
- **Failure:** refutes the mixed-composite theorem.
- **Priority:** MUST-RUN.

### B5 — Projective and Schatten limits

- **Claim tested:** C2.
- **Task:** verify `x_new=0` consistency; compute prime/composite cutoff products
  for all frozen `N,sigma,q`; compare with the theorem `q sigma > 1`.
- **Metrics:** exact projective checks, partial log-products, predicted class.
- **Success:** formal limit checks pass; analytic tables agree with the frozen
  classification label.
- **Failure:** stop the corresponding limit claim.
- **Priority:** MUST-RUN.

### B6 — Inventory controls

- **Claim tested:** anti-claim.
- **Task:** repeat determinant, stabilizer, and mixed-factor checks on all
  frozen inventories and seeds.
- **Metrics:** exact pass/fail counts.
- **Success:** all controls reproduce the finite theorems, triggering
  `PROVES_TOO_MUCH`.
- **Failure:** audit hidden inventory dependence.
- **Priority:** MUST-RUN.

## Run order and milestones

| Milestone | Goal | Runs | Decision gate | Cost | Risk |
|---|---|---|---|---|---|
| M0 | sanity | `n=3` cycle/character and `n=2,r=2` ghost witness | both exact certificates pass | CPU seconds | canonical rotation bug |
| M1 | core enumeration | B1 and B2 | frozen counts/characters pass | CPU seconds | sign convention |
| M2 | no-go algebra | B3 and B4 | every exact theorem passes | CPU seconds | transfer/diagonal conflation |
| M3 | limits | B5 | projective and threshold tables complete | CPU seconds | floating cutoff misinterpretation |
| M4 | controls/freeze | B6, tests, reports, SHA | all exact tests pass | CPU seconds | nondeterministic ordering |

## Compute and data budget

- GPU-hours: `0`.
- External datasets: none.
- Network: not required.
- Exact arithmetic: Python integers and `fractions.Fraction`.
- Floating arithmetic is restricted to descriptive Schatten cutoff products;
  theorem labels are determined analytically by `q*sigma>1`.

## Final checklist

- [x] Claims and anti-claim frozen before execution.
- [x] Cutoffs, seeds, controls, and stop rules frozen.
- [x] Exact output tables generated.
- [x] Tests pass from a clean invocation.
- [x] Report separates theorem certificates from descriptive cutoff values.
- [x] Bundle checksum frozen.
