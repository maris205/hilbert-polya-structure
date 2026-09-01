# HCS-C279 — path-graph total-variation flow

This package proves the complete real-time dynamics of the Euclidean
total-variation gradient flow on every finite unweighted path.  A maximal
constant block moves with an explicit signed boundary-flux velocity.  Blocks
can merge, including several adjacent collisions at the same time, but never
split.  The resulting trajectory is exact and piecewise affine, reaches the
initial mean in finite time, and at every time equals the unique
Rudin--Osher--Fatemi (ROF) minimizer with the same parameter.

The theorem is **PROVABLE AS STATED** for all `n>=1` and all real initial
vectors.  The ROF equivalence is deliberately path-specific: no extension to
arbitrary branched, cyclic, weighted, or differently normalized graphs is
claimed.

## Release surface

- theorem, proof, and boundaries: `THEOREM_PACKAGE.md`
- exact finite evidence: `results/c279_path_tv_evidence.json`
- independent reconstruction, symbolic audit, replay, and mutations: `code/`
- Route-A evaluation: `evaluations/route_a/HCS-C279/2026-09-01.yaml`
- manuscript and three substantive revisions: `paper/`
- content-addressed closure: `C279_RELEASE_MANIFEST.json`

The locked scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.  The strict tuple is
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`; Route B is not authorized.
