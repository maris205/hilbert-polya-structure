# Deterministic control results

Command:

```bash
python3 code/verify_cocktail_majority.py
```

Status: **PASS**.

- all `87,380` states across `n=1,...,8` are exhaustively evaluated;
- instrumented audit counts **309,038 actual assert executions**;
- the iterate fixed-count grid contains `8 x 12 = 96` `(n,k)` cases;
- the closed formulas for fixed points, genuine two-cycles, and both
  consensus basins agree in every case.

This is an exact finite regression over the displayed range, not a proof of
the all-`n` statements or a novelty claim.
