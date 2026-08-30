# C241 narrative report

The classical Lüroth map provides a clean discrete source-local dynamical
system with infinitely many branches.  Its half-open branch
\(I_m=(1/m,1/(m-1)]\) is sent affinely to \((0,1]\), with slope
\(m(m-1)\).  The endpoint distinction matters: \(0\) is the limit at the
excluded left endpoint and is separately fixed by the declared map value.

This structure makes periodic coding exact.  Composing inverse branches along a
finite word gives \(\Phi_w(y)=u_wy+v_w\), \(0<u_w<1\), so the unique fixed
point \(v_w/(1-u_w)\) is rational and its return multiplier is the product of
branch slopes.  Forward itineraries and cyclic rotations are checked exactly;
Möbius inversion separates primitive necklaces from repetitions.  Since the
alphabet is countable, this theorem scales conceptually beyond every finite
receipt: each positive period has countably infinitely many coded points.

The weighted ledger then records a finite-cutoff identity
\(Z_M(z,s)=1/(1-zA_M(s))\).  In the limit,
\(A(s)=\sum_{m\ge2}[m(m-1)]^{-s}\) converges absolutely only for
\(\Re(s)>1/2\).  Absolute primitive-product/log convergence additionally
requires \(|z|A(\Re(s))<1\), whereas the rational expression is meromorphic
away from denominator zeros in the whole half-plane.  At \(s=1\), telescoping
gives \(A(1)=1\), \(z=1\) is a pole, and the cutoff tail is exactly \(1/M\).
Rows at \(s=1/2\) explicitly expose divergence instead of silently applying a
full-alphabet condition.

The package's advance is analytic and reproducible (A1_PASS_ANALYTIC), not an
arithmetic identification: A0, A2, and A3 fail, with A4 recorded as the
formal hint `A4_FORMAL_HINT`.  No target prime/zero data, Euler factor, root
number, automorphy, divisor, functional equation, Hilbert–Pólya operator, or
Route-B input is inferred.
