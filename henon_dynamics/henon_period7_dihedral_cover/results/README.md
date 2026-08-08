# HCS-C20 results

- `c20_certificate.json` is the deterministic exact producer output.
- `c20_independent_check.json` is a byte-bound PASS report from the
  non-importing checker.

The certificate records:

- the square class `Q6`, the explicit simple branch root `u(sigma)`, and the
  resultant `2^42` with its actual `P_x(u)` remainder;
- the accepted `D7` splitting-field argument and both Riemann--Hurwitz genus
  computations (`g(C)=3`, `g(B)=2`, `g(E)=8`);
- proved good reduction of `B`, `C`, and `E` at `p=5,11,13`, including the
  irreducible specialization, residual-node, infinity, vertical-inertia,
  purity/tame-quotient, and plane-normalization comparison ledgers;
- exact cubic conjugate/minimal-polynomial/norm identities for the certified
  `L_C` factors at those primes;
- direct plane counts over `F_{p^r}`, `r=1,2,3`, the `7+epsilon` node and
  infinity normalization correction, Frobenius power sums, and an independent
  Newton reconstruction of each `L_C`;
- certified degree-16 local factors obtained as `L_B L_C^2` at those primes.

No direct explicit square-root identity for the raw neighbor discriminant is
claimed.  Its square-class interpretation is group-theoretic, with the exact
neighbor norm and septic discriminant supplied as computational inputs.
The good-reduction conclusion is deliberately restricted to 5, 11, and 13.
Here `R` denotes edge reversal and `J=R*tau` the scalar-fixing reflection, so
the scalar quotient is consistently written `C=E/<J>`.
The independent report recomputes the plane counts without `galois` or
`numpy`, using separately verified polynomial-quotient models for every
extension field; the producer retains its vectorized `galois` implementation.
