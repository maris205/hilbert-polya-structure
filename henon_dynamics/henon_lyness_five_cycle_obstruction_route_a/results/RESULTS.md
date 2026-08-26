# C173 exact results

## Claim-bearing results

- (F^5=I) globally on ((0,\infty)^2).
- The unique fixed point is
  ((\phi,\phi)), (\phi=(1+\sqrt5)/2).
- Every other point has exact period five.
- (\operatorname{Fix}(F^n)) is the singleton fixed point for
  (5\nmid n), and the entire positive quadrant for (5\mid n).
- The classical Artin--Mazur zeta is undefined because the fifth fixed set
  is uncountable.
- (dx\,dy/(xy)) is invariant and (R(x,y)=(y,x)) satisfies
  (RFR=F^{-1}).
- (Uf=f\circ F) is unitary, (U^5=I), and each of its five cyclic
  Fourier eigenspaces is infinite-dimensional.
- Thus (U) is noncompact, is in no finite Schatten class, is not trace
  class or self-adjoint, and has no ordinary trace-class Fredholm
  determinant.

## Deterministic validation

- Evidence payload SHA-256:
  `f96c44000538c10fbd3928991b44bcb7f003b6deb890d81045fa358b8d5ec97b`.
- Evidence file SHA-256:
  `6695e3ad62be2f1125d7a9e5488f6a78c7ad2c101c9fee1e896770e69fb28240`.
- Independent checker: 891 assertions.
- SymPy reconstruction: 207 exact checks.
- Repaired-hash semantic mutations rejected: 49/49.
- Stale-hash mutation rejected: 1/1.
- Byte replay: exact.
- Rational sentinel rows: 100; fixed-set sentinel depth: 50.

## Route decision

`(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)`;
overall `ROUTE_A_REJECTED`; `route_b_invocation_allowed: false`.

The finite ledgers do not prove the all-point statements.  They guard the
implementation of the separate symbolic proof.
