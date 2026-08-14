# HCS-C53 methodology blueprint

## M1. Freeze before transforming

Use the literal C51 source order and the C52 implementation commit recorded
in `README.md`. The closing coefficient \(\rho\), order-24 group convention,
and C52 rank ledger are immutable inputs.

## M2. Prove equations symbolically

Derive the monomial reversal \(M_n\) for a symbolic \(n\), then solve its
fixed vectors explicitly. The determinant formula for \(B_n\) is part of
the proof. Finite computer checks are regression tests only and may not be
presented as the proof of the all-\(n\) theorem.

## M3. Separate four descent layers

1. Equation-level descent is elementary and valid for every \(n\ge2\).
2. Smoothness/motive claims use only the certified rows \(n=2,3,4\).
3. Chow projector descent uses the Galois-stable graph sum and rational
   restriction/corestriction.
4. Strict compatibility uses correspondence traces; integral coefficients
   require the separate monic-factor/algebraic-integer argument.

No layer may borrow a stronger conclusion from a later layer.

## M4. Analyze local factors place by place

Use Artin formalism over the quadratic extension. Treat split primes and
inert primes separately. The split identity yields exponent \(4/n\); the
inert identity squares Frobenius eigenvalues and supplies the proof firewall
against a global half-root.

## M5. Preserve the geometric boundary

A conic-bundle/Prym route is not part of C53. Any future quadric-bundle
realization must begin with an independent flatness theorem, discriminant
calculation, and source audit.

## M6. Validation standard

Every machine artifact must be deterministic, exact, source-locked, and
independently checked. A replay validates identities and provenance; it does
not replace the written family proof or establish analytic continuation.
