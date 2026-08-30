# C241 research question

Can the classical Lüroth map be given a complete, exact, and auditable
periodic-orbit atlas that simultaneously (i) handles every finite branch word,
(ii) separates primitive necklaces from repetitions, (iii) records exact
fixed-point and multiplier data, and (iv) states the finite weighted identity
and its countable-alphabet convergence boundary without overclaiming a target
arithmetic interpretation?

## Answer delivered by this package

Yes for the source-local theorem.  The affine inverse branches contract, so
each finite word has one rational fixed point and an integer multiplier; Möbius
inversion gives primitive necklaces; the full countable alphabet yields
countably infinitely many points at every positive period.  The finite cutoff
identity is exact, while the full \(A(s)\) converges absolutely only for
\(\Re(s)>1/2\).  Absolute primitive-product convergence additionally needs
\(|z|A(\Re(s))<1\); the rational expression is meromorphic away from zeros in
the larger half-plane.  At \(s=1\), telescoping gives \(A(1)=1\) and a pole at
\(z=1\).

The Route-A assessment is `A0_FAIL / A1_PASS_ANALYTIC / A2_FAIL / A3_FAIL /
A4_FORMAL_HINT`: no rational-prime carrier, target divisor, zero correspondence,
or Hilbert–Pólya operator is claimed.
