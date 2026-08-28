# Results

The canonical receipt is `c221_nls_evidence.json`.

| Ledger | Count | Meaning |
|---|---:|---|
| profile rows | 15 | stationary ODE and sech derivative probes |
| integral rows | 3 | mass, norms, Hamiltonian, action and VK scaling |
| spectrum rows | 15 | three exact eigenpair residuals on each \(\omega,x\) probe |
| factorization rows | 15 | scaled \(P_2\) and \(P_1\) ladder identities |
| boundary rows | 4 | zero-frequency, defocusing, periodic and higher-dimensional faces |

The independent checker passes 497 assertions; the SymPy cross-check passes 19
identities; replay is byte exact; and all 17 hostile mutations are rejected
(16 repaired-hash/unknown-key cases plus one stale-hash case).  These finite
rows are regression evidence only; the theorem package carries the continuum
quantifiers.  The strict Route-A verdict is rejected with Route B false.
