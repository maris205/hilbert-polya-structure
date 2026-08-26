# C170 results

Status: all proof, symbolic, exhaustive-regression, replay, and mutation gates pass.

- Every \(N\ge1\), every marker word: exact cycle classification by \(\eta\) (`PROVED`).
- \(\eta=+1\): two \(N\)-cycles; \(\eta=-1\): one \(2N\)-cycle (`PROVED`).
- All-time fixed counts, zeta, Koopman determinant, and root multiplicities (`PROVED`).
- Prefix gauge, unfolded orbit coordinate, reversor, and antiunitary (`PROVED`).
- Self-adjoint boundary \(L\le2\) (`PROVED`).
- Class rows: 48, through \(N=24\).
- Exhaustive sentinel: 2,046 marker configurations, 36,868 labelled states, 36,868 fixed-time checks, and 73,736 reversal identities through \(N=10\).
- Independent checker: 114,056 assertions.
- SymPy: 221 polynomial/matrix checks.
- Mutation suite: 16/16 repaired-hash plus 1/1 stale-hash mutations rejected.
- Citation and reference registries: 0 entries.

Route-A v0.2 decision: `(A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)`, overall `ROUTE_A_REJECTED`, Route B false. The source classification remains theorem progress, but A0 failure rejects it as a primary Hilbert--Pólya candidate.
