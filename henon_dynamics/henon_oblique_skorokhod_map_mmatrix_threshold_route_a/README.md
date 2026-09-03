# HCS-C346 / HEN-O330 — oblique Skorokhod map

This package proves the sharp all-input well-posedness threshold for the
two-dimensional orthant Skorokhod problem with

`R=[[1,-rho],[-sigma,1]]`, `rho,sigma>=0`.

Unique global regulation for every cadlag input holds exactly when
`rho*sigma<1`.  The proof gives the running-supremum fixed point, the exact
weighted contraction factor `sqrt(rho*sigma)`, quantitative input stability,
monotone Picard convergence, causality, continuity preservation and time-change
covariance.  Explicit critical nonuniqueness and critical/supercritical
no-solution inputs make the threshold sharp.  Normal, triangular, corner and
simultaneous-jump faces are closed.

Route-A tuple:

`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`

Overall verdict: `ROUTE_A_REJECTED`; Route B stays locked under
`NO_BAD_EULER_OR_ROOT_NUMBER`.

Run:

```bash
python3 -B code/c346_skorokhod_producer.py
python3 -B code/c346_skorokhod_checker.py
python3 -B code/c346_skorokhod_sympy_crosscheck.py
python3 -B code/c346_skorokhod_replay.py
python3 -B code/c346_skorokhod_mutation.py
python3 -B code/c346_release_manifest.py
```

The release has 28 physical files and 27 self-excluding manifest payloads.
