# C195 exact results

## Theorem result

For every \(\nu>0,L>0,m\in\mathbb R,s>3/2\), the fixed-mean periodic
viscous-Burgers semiflow is globally conjugate to the positive projectivization of
\(e^{t(\nu\partial_x^2-m\partial_x)}\). Every orbit is global and converges to the
unique constant \(m\); hence the nonconstant periodic and recurrent sets are empty.
The first active Fourier mode of the positive lift supplies the exact leading
decay, and the full linearized spectrum is
\(-\nu(2\pi k/L)^2-i m(2\pi k/L)\).

## Exact certificate

- 24 deterministic strictly positive trigonometric lifts.
- 24 zero cleared-denominator Burgers-generator residuals.
- 60 exact Hermitian-reality residual cells.
- 24 positive initial margins and 24 positive snapshot margins.
- 24 exact two-step/one-step semigroup identities.
- 24 exact first-mode leading coefficients, decay exponents, and remainder gaps.
- 408 exact linearized-spectrum cells.
- 1,490 producer-independent checker assertions.
- 129 separate SymPy checks across 9 selected cases.
- 22/22 repaired-hash semantic mutations rejected.
- 1/1 stale-hash mutation rejected.
- Exact byte replay passed.

Evidence SHA-256: `042f0e30d987c9889dc5a74ed14a27c73531af914e96931108905794e67f9354`.
Semantic payload SHA-256:
`aa28a3030ea2332bd6a23e8c0b1585807c0222cbc02a3862ea44a0edf7bbb9f6`.

## Interpretation

The finite rows are regression only, never proof of the infinite-dimensional
statement. The projective heat lift is classical Hopf--Cole source structure.
It produces no arithmetic carrier or orbit ledger. The exact route tuple is
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`; overall status is rejected and
Route B remains false.
