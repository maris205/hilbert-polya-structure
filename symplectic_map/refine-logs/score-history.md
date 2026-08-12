# Refinement Score History

## Scoring policy

Only scores actually returned by an independent review are recorded. Missing rounds
are left unscored rather than assigned inferred values. A model-based technical review
is not represented as human peer review.

| Round | Artifact reviewed | Theory | Method | Contribution | Novelty | Feasibility | Validation | Readiness | Reported weighted score | Verdict |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 0 | Original proposal plus internal audit | -- | -- | -- | -- | -- | -- | -- | -- | Not independently scored |
| 1 | Pre-implementation Hénon-homotopy candidate package | 6 | 5 | 5 | 4 | 6 | 4 | 3 | **5.0/10** | `REVISE`; arithmetic candidate `RETHINK`; narrowed paper `REVISE` |
| 2 | Post-confirmatory narrow negative/diagnostic package | 7 | 8 | 6 | 4 | 8 | 8 | 7 | **6.8/10** | Green-light narrow paper; arithmetic/HP claims remain closed |
| 3 | Compiled final manuscript and frozen artifacts | 8 | 8 | -- | 5 | -- | 9 | 8 | **7.8/10 overall** | Publishable technical report/preprint after wording fixes; fixes implemented |

## Round-1 blockers to a higher score

- the upstream arithmetic seed was not established;
- closest direct priors substantially narrowed novelty;
- the obstruction was elementary rather than a sufficient contribution;
- the primary statistic, censoring, and controls were not yet fully frozen;
- branch identity and \(u_c\) completeness were unresolved;
- no confirmatory result existed;
- the multiplier-prime and zeta claims lacked an intrinsic blind mechanism.

## Changes made after the scored review

- Source-lock v2 freezes a single parity-polarity endpoint statistic, trajectory
  splits, exposure gates, \(\rho\)-grid, bootstrap, neighbor controls, and Holm
  correction.
- Direct-prior and novelty audits are explicit.
- The high-\(a\) positive control now matches primitive binary-necklace counts through
  period 10, with maximum cyclic residual \(1.42\times10^{-13}\).
- The current software suite passes 30 tests when run with `PYTHONPATH=.`.
- The \(u_c\) ledger remains explicitly incomplete.
- Multiplier-prime, zeta, and quantization work remains closed.

These changes are progress notes, not a rescoring. A new score should be entered only
after the revised package and its confirmatory artifacts undergo another independent
review.

## Target for the next review

The next review should receive:

1. source-lock v2 and its hash;
2. development/validation/test access log;
3. confirmatory polarity and exposure result;
4. neighbor-control Holm table and temporal nulls;
5. high-\(a\) count/audit artifacts;
6. \(u_c\) incompleteness and branch-event report;
7. manuscript claims cross-referenced to `CLAIM_MATRIX.md`.
