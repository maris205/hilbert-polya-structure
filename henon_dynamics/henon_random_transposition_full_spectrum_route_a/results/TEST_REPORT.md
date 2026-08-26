# C183 test report

## Exact executable checks

- Producer: PASS — 193 partition rows, 90 moment rows, 163 collected factor rows.
- Independent checker: PASS — 2,597 assertions; no producer import.
- SymPy reconstruction: PASS — 2,427 checks.
- Canonical replay: PASS — 184,283 exact evidence bytes.
- Mutation suite: PASS — 57 repaired-hash and one stale-hash rejection.

## Coverage

The checker independently reconstructs all partitions, conjugates, hook dimensions, transposition content sums, eigenvalues, regular multiplicities, collected factors and their exact strings, traces, return probabilities, \(L^2\) identities, gap, bottom sectors, source registry, finite cutoffs, owner boundary, Route-A qualifications, and scope locks. A second path enumerates every ordered-pair transition word for \(2\le n\le7\), \(0\le k\le6\). A third exact control enumerates primitive binary path cycles through length eight and verifies the weighted Euler product for \(P_2\).

Finite tests do not prove the all-size theorem. The representation-theoretic and trace--log proofs are carried in `THEOREM_PACKAGE.md` and `paper/main.tex`.
