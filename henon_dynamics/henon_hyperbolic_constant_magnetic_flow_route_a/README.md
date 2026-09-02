# HCS-C289: constant magnetic flow on the hyperbolic plane

This self-contained Route-A package classifies every constant-field magnetic trajectory on the simply connected surface of curvature `-kappa^2`.  It proves the circle/horocycle/hypercycle/geodesic trichotomy, the exact circle period, and the nilpotent critical boundary from the raw Lorentz-frame generator.  The classical result is explicitly source-owned; the contribution of this package is a proof-and-audit closure, not a literature-originality claim.

Frozen inputs: source commit `7fbe9db30cc460a82883533d7cfb2edd988c5b65`, evaluator v0.2.0 SHA-256 `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`, epoch `1788307200`, and scope `NO_BAD_EULER_OR_ROOT_NUMBER`.

Run the full release gate:

```bash
python3 code/c289_release_manifest.py
```

The verdict is `(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`, overall `ROUTE_A_REJECTED`; Route B is not invoked.
