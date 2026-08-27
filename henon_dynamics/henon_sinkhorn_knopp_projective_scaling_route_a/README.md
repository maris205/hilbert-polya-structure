# HCS-C191: Sinkhorn--Knopp projective scaling

This package closes one all-matrix theorem block rather than one numerical
example.  Alternating row/column normalization is classified by support,
total support and full indecomposability; the strictly positive stratum also
receives a Hilbert-projective contraction bound and the exact local rate
`sigma_2(S)^2` at its doubly stochastic limit.

The sharp boundary is part of the result.  Support without total support can
converge only by losing positive entries, total support without full
indecomposability has extra factor gauges, and no dimension-only contraction
constant exists.  The convergent dynamics has no nonconstant recurrent orbit
and no intrinsic rational-prime payload.  Its strict verdict is

```text
(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)
ROUTE_A_REJECTED
```

Finite zero-pattern and exact-rational iterations are regression oracles, not
proofs of the source-locked all-matrix theorems.  See `THEOREM_PACKAGE.md`,
`SOURCE_AUDIT.md`, `results/TEST_REPORT.md`, and `paper/main.pdf`.

Run from the repository root:

```bash
python3 henon_dynamics/henon_sinkhorn_knopp_projective_scaling_route_a/code/c191_sinkhorn_producer.py
python3 henon_dynamics/henon_sinkhorn_knopp_projective_scaling_route_a/code/c191_sinkhorn_checker.py
python3 henon_dynamics/henon_sinkhorn_knopp_projective_scaling_route_a/code/c191_sympy_crosscheck.py
python3 henon_dynamics/henon_sinkhorn_knopp_projective_scaling_route_a/code/c191_replay.py
python3 henon_dynamics/henon_sinkhorn_knopp_projective_scaling_route_a/code/c191_mutation.py
python3 henon_dynamics/henon_sinkhorn_knopp_projective_scaling_route_a/code/c191_release_manifest.py
```

Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.  Route B is false.
