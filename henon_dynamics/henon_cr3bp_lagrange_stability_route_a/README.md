# HCS-C290: Lagrange equilibria and linear stability in the planar CR3BP

This package gives a self-contained theorem-and-evidence closure for all five equilibria of the normalized planar circular restricted three-body problem for `0<mu<=1/2`.  It proves collinear existence, uniqueness, and saddle-times-center type; the triangular characteristic polynomial; the exact Gascheau–Routh boundary; and, critically, the defective Jordan structure and linear growth at equality for both triangular points.  Equality is **not stable**.  Strict JSON/YAML contracts separate finite regression evidence from the all-parameter proof.

Frozen inputs: source commit `7fbe9db30cc460a82883533d7cfb2edd988c5b65`, evaluator v0.2.0 SHA-256 `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`, epoch `1788307200`, scope `NO_BAD_EULER_OR_ROOT_NUMBER`.

Run `python3 code/c290_release_manifest.py`.  Route-A tuple: `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`, overall `ROUTE_A_REJECTED`; Route B false.
