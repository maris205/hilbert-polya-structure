# HCS-C320: Darboux--Halphen modular dynamics

This package fixes one complete convention for the Darboux--Halphen system
and proves a theta/q-series solution, PSL(2,C) covariance, modular-generator
permutations, the Chazy reduction, discriminant transport, and every
pair-collision stratum, together with cusp and pole boundaries.

The evidence contains 129 exact coefficient rows through `Q^128`, six
100-digit independent theta/ODE/`S,T` witnesses, 18 rational reciprocal-
collision rows, and 15 axis equilibria: 1,705 audited scalar leaves.  The
producer-independent checker uses Jacobi products rather than the producer's
formal division and performs 1,945 checks.  SymPy closes 345 identities,
replay is byte exact, and 56/56 hostile repaired-digest/YAML mutations are
rejected.

The strict Route-A result is
`(A0_WEAK_ARITHMETIC_RELATION,A1_FAIL,A2_FAIL,A3_PARTIAL_ANALYTIC_STRUCTURE,A4_FAIL)`,
overall `ROUTE_A_REJECTED`.  Intrinsic modular coefficients do not become
target local data or an Euler product.  Route B stays locked under
`NO_BAD_EULER_OR_ROOT_NUMBER`.

## Reproduce

```bash
python -B code/c320_darboux_halphen_producer.py
python -B code/c320_darboux_halphen_checker.py
python -B code/c320_darboux_halphen_sympy_crosscheck.py
python -B code/c320_darboux_halphen_replay.py
python -B code/c320_darboux_halphen_mutation.py
python -B code/c320_release_manifest.py
```

The paper is `paper/main.pdf`; `C320_RELEASE_MANIFEST.json` is the exact
release ledger.
