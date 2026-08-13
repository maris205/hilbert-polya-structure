# HCS-C36: Hénon Mellin--parity obstruction

C36 follows the only live escape from C35. The infinite dilation orbit of the
cubic Hénon Poisson boundary becomes a two-sign Mellin multiplier. Its parity
scattering ratio has the exact formal symmetries expected from Route A:

\[
S_H(z)S_H(1-z)=I,
\qquad
S_H(1/2+it)^*S_H(1/2+it)=I.
\]

The main result is negative and decisive: the zeta-relevant even symbol has
one certified simple zero in an explicit radius-\(10^{-12}\) disc off the
critical line but inside the critical strip. This produces an extra
pole/zero pair in the natural Hénon scattering divisor and closes the
unrenormalized adelic H6 Route-A lift.

This project intentionally separates:

- exact symbol identities;
- the discovery-stage high-precision zero evidence;
- the released Arb/Rouché interval certificate;
- and the conditional reference-cancellation escape.

No RH proof, zero matching, or Route-B claim is made.

## Reproduce the theorem certificate

```bash
./code/run_c36.sh
```

The independent checker passes 9/9 gates and the mutation suite passes
25/25 tests. The result is `NUMERICALLY_CERTIFIED` in the interval-arithmetic
sense: the proof combines complex-ball enclosures with an analytic Rouché
majorant, rather than treating decimal agreement as a theorem.

## Large pivot

The inhomogeneous candidate is stopped. The next project uses the homogeneous
area-preserving deformation

\[
H_0(q,p)=(-6q^2-p,q),
\qquad P_0(q)=2q^3,
\]

whose Mellin symbol is strip-safe and explicit. Its decisive gate is whether
an ambient scaling coboundary becomes a nontrivial index on the Poisson
boundary quotient. This is an anomaly-or-closure problem, not another zero
scan.
