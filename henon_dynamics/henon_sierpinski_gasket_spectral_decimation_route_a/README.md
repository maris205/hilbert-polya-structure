# HCS-C184 — Sierpiński-gasket spectral decimation

This package gives one all-level certificate for the standard unnormalized
Dirichlet graph Laplacian on every finite pre-gasket.  The three outer
corners are removed from the matrix, while their incident edges still
contribute to the diagonal.  The theorem resolves the complete 2-, 5-, and
6-series genealogy under

\[
R(\lambda)=\lambda(5-\lambda),
\]

including birth multiplicities, the forced \(6\mapsto3\) continuation,
dimension closure, a characteristic-polynomial recurrence, a closed
determinant, the heat trace, and the finite spectral zeta.

The classical spectral-decimation theorem and complete finite-gasket
spectrum are attributed to Fukushima and Shima, DOI
`10.1007/BF00249784`.  The package contribution is a source-locked,
content-addressed synthesis and Route-A boundary audit; it does not claim
priority for the classical theorem.  The inverse-branch genealogy advances
the graph-refinement level.  It is not an autonomous physical-time map.

## Run

```bash
python3 code/c184_spectral_decimation_producer.py
python3 code/c184_spectral_decimation_checker.py
python3 code/c184_sympy_crosscheck.py
python3 code/c184_replay.py
python3 code/c184_mutation.py
python3 code/c184_release_manifest.py
```

The final manuscript is `paper/main.pdf`.  The strict Route-A tuple is
`(A0_FAIL, A1_FAIL, A2_FAIL, A3_PARTIAL_ANALYTIC_STRUCTURE,
A4_FORMAL_HINT)`, the overall verdict is `ROUTE_A_REJECTED`, and Route B is
false.  Scope literal: `NO_BAD_EULER_OR_ROOT_NUMBER`.
