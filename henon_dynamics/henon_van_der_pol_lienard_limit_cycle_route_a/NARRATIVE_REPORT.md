# C249 narrative report

The round makes one large, coherent step: it replaces a qualitative mention
of a nonlinear oscillator by a sign-complete Liénard certificate.  The frozen
flow is
\[
 \dot x=y,\qquad \dot y=\mu(1-x^2)y-x,
\]
so the damping primitive is
\(F(x)=\mu(x^3/3-x)\).  For positive \(\mu\), its single positive zero and
monotonic exterior satisfy the classical uniqueness hypotheses.  Exactly one
hyperbolic attracting cycle surrounds the origin.  Negative \(\mu\) reverses
time and stability; the zero face is the explicitly solvable center with a
continuum of period-\(2\pi\) ovals.

The identity ledger links three viewpoints.  The energy obeys
\(\dot E=\mu(1-x^2)y^2\), so every nonzero-\(\mu\) periodic cycle has zero
net balance.  The
planar divergence is \(\mu(1-x^2)\), hence the tangent multiplier is one and
the transverse Floquet multiplier is the exponential of its cycle integral.
The section \(x=0,y>0\) turns the cycle into one fixed point of a return map.

Five DOP853 rows at \(\mu=0.1,0.5,1,2,4\) provide reproducible values.  The
period grows from approximately 6.2871 to 10.2035, while the measured
transverse multiplier contracts from approximately 0.5331 to
\(1.28\times10^{-25}\).  These numbers are regression receipts only; the
all-parameter conclusion comes from the Liénard theorem, not from sampling.

The model remains intentionally non-arithmetic.  No prime/zero table, Euler
factor, root number, automorphy, target determinant, or Hilbert--Pólya
operator is introduced.  Thus the route tuple is
`(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)` with overall
`ROUTE_A_REJECTED`.
