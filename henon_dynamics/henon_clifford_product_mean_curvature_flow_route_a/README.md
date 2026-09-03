# HCS-C319: Clifford-product mean-curvature flow

This package closes the full scalar dynamics of
`S^p(cos(theta)) x S^q(sin(theta))` in the unit sphere for every
`p,q>=1`.  In `y=sin(theta)^2` the mean-curvature flow is exactly
`y'=2((p+q)y-q)`.  The paper proves both ancient branches, their exact
finite forward lifespans, focal collapses, Type-I cylindrical blow-ups,
strict area dissipation, and the complete index/nullity of the stationary
minimal Clifford product.

The evidence enumerates 100 dimension pairs, 600 branch witnesses, and
3,600 spectral cells.  A producer-independent checker performs 22,738
checks, SymPy closes 1,204 exact identities, replay is byte exact, and all
39 hostile evidence/YAML mutations are rejected.

The strict Route-A result is
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`, with overall verdict
`ROUTE_A_REJECTED`.  The Jacobi operator is source-local; it is not a
Hilbert--Polya operator.  Route B stays locked under
`NO_BAD_EULER_OR_ROOT_NUMBER`.

## Reproduce

```bash
python -B code/c319_clifford_producer.py
python -B code/c319_clifford_checker.py
python -B code/c319_clifford_sympy_crosscheck.py
python -B code/c319_clifford_replay.py
python -B code/c319_clifford_mutation.py
python -B code/c319_release_manifest.py
```

The readable result is `paper/main.pdf`; `C319_RELEASE_MANIFEST.json` is the
content-addressed release ledger.
