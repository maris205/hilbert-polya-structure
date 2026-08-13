# Experiment Plan

**Problem**: Decide the scalar homogeneous Hénon Poisson-boundary anomaly.

**Method thesis**: The scalar cubic scaling lift is functorially gauge
trivial, and its natural Hardy compression is outside the restricted
unitary group; therefore no canonical scalar anomaly determinant survives.

**Date**: 2026-08-13

## Claim Map

| Claim | Why it matters | Minimum convincing evidence | Block |
|---|---|---|---|
| C1: scalar lift is equivariantly trivial | decides whether the Hénon phase creates prime holonomy | one gauge simultaneously trivializes rational descent and all scaling, with repetition telescoping | B1 |
| C2: natural index escape is unavailable | prevents a formal coboundary from being promoted to a determinant anomaly | zero relative-projection index and an exact non-VMO witness for both physical and log-scaling Hardy coordinates | B2 |

## Paper Storyline

- Main paper must prove C1 and C2.
- Appendix contains exact rational bounds and mutation tests.
- Prime scans, zero scans, alternative fitted polarizations, and broad
  parameter sweeps are intentionally cut.

## Experiment Blocks

### B1: Equivariant cocycle and prime holonomy

- Claim tested: C1.
- Task: replay the cocycle and quotient-compatibility identities
  coefficientwise; telescope prime repetitions.
- Compared systems: homogeneous cubic versus the inhomogeneous C36 control.
- Metric: groupoid class, closed holonomy, dependence on gauge.
- Success criterion: class zero and holonomy one for arbitrary symbolic
  \(p,r\).
- Failure interpretation: any residual gauge-invariant phase reopens the
  anomaly route.
- Priority: MUST-RUN.

### B2: Static index and Hardy admissibility

- Claim tested: C2.
- Task: compute essential codimension of the two boundary hyperplanes and
  certify shrinking-interval mean oscillation.
- Metrics: trace of projection difference; lower bound for normalized
  \(L^2\) mean oscillation; compactness status.
- Success criterion: essential codimension zero and oscillation lower bound
  \(>51/100\).
- Failure interpretation: a compact Hardy commutator would reopen a genuine
  determinant-line index.
- Priority: MUST-RUN.

## Run Order and Milestones

| Milestone | Goal | Runs | Decision gate | Cost | Risk |
|---|---|---|---|---|---|
| M0 | source lock | hash C35/C36/Hénon/Route-A inputs | all files present | seconds | source drift |
| M1 | algebraic closure | cocycle, descent, prime telescoping | exact zero differences | seconds | chronology error |
| M2 | index obstruction | hyperplane projection and VMO bounds | zero index + noncompact commutator | seconds | wrong index convention |
| M3 | assurance | independent checker and mutations | all gates/tests pass | seconds | fail-open schema |

## Compute and Data Budget

- No GPU.
- No prime or Riemann-zero table.
- Exact integer/rational arithmetic plus deterministic file hashing.
- Biggest bottleneck: mathematical scope, not computation.

## Risks and Mitigations

- Noninjective Poisson map: do not infer an image-pair index.
- Exotic polarization: state it outside scope.
- Tautological mother divisor: do not score inherited \(\xi\) as Hénon
  evidence.
- Checker overclaim: use type-strict mutations and an independent replay.

## Final Checklist

- [x] Main theorem has one decisive fork.
- [x] Negative result selects a genuinely different nonscalar next door.
- [x] No zero fitting or cutoff exploration.
- [x] Route-A scope remains conservative.
