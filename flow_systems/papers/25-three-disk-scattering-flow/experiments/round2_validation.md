# P25 Round-2 validation report

## Material Passport

- Origin Skill: experiment-agent
- Origin Mode: run + validate
- Origin Date: 2026-08-27
- Verification Status: VERIFIED
- Version Label: p25_round2_validation_v1

## Execution and reproducibility

- Determinism class: deterministic in the recorded Python/NumPy/SciPy environment.
- Reproducibility verdict: `REPRODUCIBLE`.
- Core-output combined SHA-256: `cd305c868bf4db359a27b1aab683ea200125eacfbd0e0b3546766220b2c11306`.
- Primitive oriented symbolic words through length 12: 747.
- Ledger rows across three geometries: 2241.
- Actual billiard rows `NUMERICALLY_CERTIFIED`: 2241.
- Actual billiard rows `NOT_ESTABLISHED`: 0.
- Finite-difference stability cross-check certified/open: 9 / 2232.

## Residual envelope on established rows

- Maximum stationarity residual: `3.192e-14`.
- Maximum specular-reflection residual: `3.796e-14`.
- Maximum independent length residual: `2.132e-14`.
- Maximum independent angle residual: `4.604e-08`.
- Maximum 80-digit monodromy determinant residual: `4.000e-55`.
- Maximum binary64-versus-80-digit trace relative residual: `9.734e-16`.

## Target-free controls

- Neighbor log-half-density correlation, `d/a=5.8` vs `6.0`: `0.999998520`.
- Neighbor log-half-density correlation, `d/a=6.2` vs `6.0`: `0.999998755`.
- Frozen stop threshold: `0.98`.
- Original period/log-half-density correlation: `-0.968441708`.
- Shuffled-period/log-half-density correlation: `-0.965354088`.
- Random-stability/log-period correlation: `-0.017961530`.
- Fixed `-1/2` exponent RMSE on rank/composite/random integer labels:
  `1.556276299` /
  `1.104094546` /
  `2.076723109`.
- Prime or zero tables used: `false`.
- Statistic-level verdict: `[STOP_SCOPED]` / `STOP_SCOPED`.

The stop applies only to treating generic instability half-density persistence as
arithmetic evidence.  It does not assign a formal A0--A4 tuple and does not
alter the separately frozen `[MODELING_CHOICE] ABSENT_BY_CONSTRUCTION` source
status.

## File hashes

- `results/round2_metrics.json`: `af480edb8b64e99d1be014b5faa0784421b4a6763cbdc4a6e80915615a918802`
- `results/three_disk_controls_round2.csv`: `1fd877bea412685f68202a38b26404c91d4946c5cb42a40124c2cdb06dd8a688`
- `results/three_disk_primitive_ledger_round2.csv`: `25584d28155ac80f63260830816a9cdf3ec54b8587c07edac600765783ed2736`


## Claim boundary

The symbolic enumeration is exact for oriented primitive cyclic words over
three labels with no adjacent repetition through topological length 12.  A
center-polygon length is always labeled a proxy.  A row is called an actual
billiard orbit only when both solvers, the specular residual, visibility,
independent length, and angle agreement pass the frozen thresholds.  An `OPEN`
finite-difference stability cross-check is not silently promoted.  The 80-digit
monodromy rebuild repairs cancellation in long products but is not counted as
an independent physical stability derivation.  No exact
multiple-scattering determinant, dynamical-zeta divisor, or arithmetic owner is
claimed.
