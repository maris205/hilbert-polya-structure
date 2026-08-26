# C177 results

Status: all theorem-certificate and release gates pass.

- All integers \(b\ge2\): exact fixed grids \(j/(b^n-1)\) and \(b^n-1\) fixed points for every \(n\) (`PROVED`).
- Exact periods: Möbius law \(P_b(n)\), integral primitive-cycle count \(C_b(n)=P_b(n)/n\), and coefficientwise product (`PROVED`).
- Artin--Mazur zeta: \((1-z)/(1-bz)\) (`PROVED`).
- Koopman/Perron: \(1\oplus S^{(\aleph_0)}\), explicit adjoint Fourier filter, and closed-unit-disk spectrum (`PROVED`).
- Operator boundary: proper isometry, noncompact, no finite Schatten membership, no ordinary Fredholm determinant for \(z\ne0\) (`PROVED`).
- Mixing: sharp \(b^{-ns}\) homogeneous-Sobolev correlation factor (`PROVED`).
- Finite sentinels: 132 periodic rows, 1,595 Wold rows, and 352 correlation rows.
- Independent checker: 3,980 assertions.
- SymPy: 3,927 checks.
- Replay: exact bytes.
- Mutation suite: 18/18 repaired-hash and 1/1 stale-hash mutations rejected.
- Citation and reference registries: zero entries.

Route-A v0.2 decision: `(A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)`, overall `ROUTE_A_REJECTED`, Route B false. The complete degree-only dynamics are reusable as a negative control; they do not pass the intrinsic-arithmetic gate.
