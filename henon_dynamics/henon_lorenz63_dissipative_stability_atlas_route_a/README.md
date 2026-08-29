# HCS-C227 — Lorenz-63 dissipativity and stability atlas

This package proves one complete step for a new local dynamical subtype:
Lorenz-63 has an explicit global absorbing ellipsoid and a complete
equilibrium/local-stability atlas for every \(\sigma,\beta>0\) and real
\(\rho\), including the exact linear Hopf surface and all zero-rate boundary
families.

## Main result

- exact shifted Lyapunov identity and global forward bound;
- origin and symmetric-wing equilibrium classification;
- exact Routh–Hurwitz margin and Hopf factorization;
- separate \(\rho=1\), \(\sigma=0\), \(\beta=0\), and double-zero controls;
- explicit refusal to infer nonlinear Hopf direction or universal chaos.

## Artifacts

- theorem: `THEOREM_PACKAGE.md`;
- source/collision audit: `SOURCE_AUDIT.md`;
- canonical evidence: `results/c227_lorenz_evidence.json`;
- independent verification: `code/`;
- final paper: `paper/main.pdf`;
- strict evaluator: `evaluations/route_a/HCS-C227/2026-08-29.yaml`;
- self-excluded release closure: `C227_RELEASE_MANIFEST.json`.

The strict tuple is
`(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)`, so the overall verdict is
`ROUTE_A_REJECTED`.  Route B is false.  Scope is
`NO_BAD_EULER_OR_ROOT_NUMBER`.
