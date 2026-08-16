# Paper 37 exact experiment report — SD-C39

## Outcome

The frozen prototype is reproduced exactly and the negative Route-A
conclusion is confirmed: `STOP_LOCAL_COEFFICIENT_SATURATION` /
`ROUTE_A_REJECTED`. The same-object analytic determinant exists, but
direct graded relator cancellation leaks on mixed consequences; full
normal-closure saturation is theorem-owned and erases every closed
factor. Route B remains locked.

## Canonical exact counts

| Evidence | Exact result |
|---|---:|
| evaluator assertions | 131/131 |
| affine direct cancellations | 8/8 |
| affine bounded mixed leaks | 8/8 |
| random direct cancellations | 9/48 |
| random conditional mixed leaks | 9/9 |
| paired all-direct matches | 2/24 |
| paired conditional mixed leaks | 2/2 |

The affine direct-match rate is `1/1`;
the random-control rate is `3/16`,
an exact difference of `13/16`.
Every preregistered affine row with `r>=2` matches
`-4*r^4*(r-1)` exactly.

## Reproducibility and separation

- Fresh/cold runs: 3/3 byte-identical.
- Run C executed from an isolated temporary code copy that was removed.
- Source and evaluator use disjoint directories and a JSON-only
  subprocess boundary; neither imports the other.
- Metadata states absent/null/empty/populated and simulated future
  manifest absence/presence leave scientific and Route bytes unchanged.
- Integration checks: 32/32.
- Scientific aggregate SHA-256: `b17967f294da018e2e045ae70ac7731f5612f4bd4693115ea33dbaebb7fc0d6e`.

## Evidence boundary

The CSV files are the raw finite tables; `results/analysis_summary.json`
contains exact rational rates and their baseline delta. These finite
runs audit formulas, controls, separation, and reproducibility. They do
not prove trace class, the arbitrary-rank nilpotence criterion, or the
normal-closure saturation theorem.
