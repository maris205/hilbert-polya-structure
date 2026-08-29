# C235 reproducibility code

`c235_rps_producer.py` writes the exact-rational/high-precision receipt
`results/c235_rps_evidence.json`.  It uses an endpoint-cancelled quadrature for
the conservative product levels and fixed-step RK4 only as a labelled finite
diagnostic for the mutation face.

The producer-independent `c235_rps_checker.py` re-derives the roots,
quadratures, vector field, Lyapunov derivative, contraction face and tangent
linearization without importing producer code.  `c235_rps_sympy_crosscheck.py`
checks the algebraic identities, `c235_rps_replay.py` checks byte equality in
two fresh temporary trees, and `c235_rps_mutation.py` rejects 25 stale or
hash-repaired hostile mutations.

All scripts are deterministic under `PYTHONDONTWRITEBYTECODE=1` and do not
read prime tables, target zeros, or any external arithmetic data.
