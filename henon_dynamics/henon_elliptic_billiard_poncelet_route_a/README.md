# HCS-C275 — elliptic-billiard Poncelet rigidity

This package closes the positive-orientation elliptic-caustic sector of the
Euclidean billiard inside the confocal ellipse `E(f)`, `0<f<e<1`.  It gives an
explicit Jacobi covering and rigid-rotation conjugacy, proves strict
monotonicity in both eccentricities and the two rotation-number endpoints,
and classifies every reduced rational rotation as a Poncelet family of common
minimal period.

The decisive obstruction is equally explicit: at rotation `p/q`, the
restricted `q`-th return is the identity on an entire invariant circle and has
unit tangent derivative.  Thus an ordinary isolated-orbit Euler product is not
available on this family.  This is not an ambient unipotent statement, and no
claim is made about hyperbolic caustics.

The Dirichlet Laplacian on the smooth bounded ellipse is a coherent ambient
quantum billiard on `L^2(Omega_f)`, with domain
`H^2(Omega_f) cap H_0^1(Omega_f)`, self-adjointness, compact resolvent, and
complex-conjugation time reversal.  It is nevertheless only an A4 formal
hint: its continuous physical-time unitary group has not been converted into
a quantum return with the frozen one-reflection clock, nor shown to retain
the fixed-caustic orbit phases and weights.

Run the six commands in [`code/README.md`](code/README.md).  The final paper is
[`paper/main.pdf`](paper/main.pdf).  The strict Route-A tuple is
`(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`, overall
`ROUTE_A_REJECTED`; Route B is disabled under
`NO_BAD_EULER_OR_ROOT_NUMBER`.
