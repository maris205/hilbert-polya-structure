# HCS-C284 — Thomson polygon point-vortex stability

This frozen package reconstructs the equal positive planar point-vortex
regular polygon from its logarithmic Hamiltonian through its raw Cartesian
Hessian and every radial–tangential DFT block.  With

`q_m=m*(N-m)` and `c=Gamma/(4*pi*R^2)`, the reduced sign is

`2*(N-1)-q_m`.

Thus `N=3..6` is linearly elliptic, `N=7` is linearly degenerate exactly in
`m=3,4`, and every `N>=8` is linearly hyperbolic.  No nonlinear stability of
the heptagon is claimed.

## Reproduce

From this directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python -B code/c284_point_vortex_producer.py
PYTHONDONTWRITEBYTECODE=1 python -B code/c284_point_vortex_checker.py
PYTHONDONTWRITEBYTECODE=1 python -B code/c284_point_vortex_sympy_crosscheck.py
PYTHONDONTWRITEBYTECODE=1 python -B code/c284_point_vortex_replay.py
PYTHONDONTWRITEBYTECODE=1 python -B code/c284_point_vortex_mutation.py
PYTHONDONTWRITEBYTECODE=1 python -B code/c284_release_manifest.py
```

The checker independently rebuilds the raw `2N by 2N` Cartesian Hessian for
every `N=3..64`; it does not import producer code.  It also verifies explicit
symmetry-slice vectors and exact JSON schemas, including duplicate-key,
type/order, and semantic-uniqueness rejection.  The release contains 27 payload
files and the self-excluded `C284_RELEASE_MANIFEST.json`, for 28 physical files.

## Frozen authority

- source commit: `3878fa5282ca89f75700b3ef9d623f54dcb7bcf9`
- evaluation date: `2026-09-02`
- fixed epoch: `1788307200`
- evaluator: Route-A v0.2.0,
  SHA-256 `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`
- tuple: `(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`
- verdict: `ROUTE_A_REJECTED`; Route B is not authorized
- scope: `NO_BAD_EULER_OR_ROOT_NUMBER`

The theorem is classical-owner material reconstructed under one explicit
convention.  The package makes no claim of invention or literature priority.
