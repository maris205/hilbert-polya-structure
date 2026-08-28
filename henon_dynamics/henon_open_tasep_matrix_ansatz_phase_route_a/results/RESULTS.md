# C220 results

The canonical producer generated:

- 200 positive-rate interior rows over \(L=0,1,2,3,4,5,6,8\);
- 40 zero-rate/boundary rows, including \((\alpha,\beta)=(0,0)\);
- exact DEHP weights for every enumerated configuration;
- exact \(Z_L\), closed-form \(Z_L\), all bond currents, and stationary residuals.
- seven explicit phase rows, including the \(\alpha=\beta=1/2\) multicritical
  phase-boundary junction;
- the coexistence row is restricted to \(0<\alpha=\beta<1/2\); the endpoint
  \((0,0)\) appears only in the zero-rate boundary rows;

The independent checker reconstructs all rows without importing producer code,
and computes exact SymPy nullspaces for every row through \(L=4\).  The
remaining larger rows are covered by the finite-chain irreducibility theorem
while their residuals are still checked exactly.  The separate SymPy program
checks 321 short-word algebra identities plus symbolic generator/current
identities.  Replay is byte-identical; 28 repaired-hash mutations and one
stale-hash mutation are rejected.

The rows are reproducibility sentinels.  They do not numerically prove the
thermodynamic \(L\to\infty\) phase law and do not support a novelty or
priority claim.

The canonical evidence payload hash is
`82def8f1358aa47442bb4af9cdf412952f2cbe562d3ff0814e2f740a98ccf1ed` (file
SHA-256 `811f7238aa5b1f44dae8da54dcacbf84b4db699b65e47da9fb85dbb0ec558396`).
