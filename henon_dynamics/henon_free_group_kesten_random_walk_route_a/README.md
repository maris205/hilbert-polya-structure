# HCS-C355 — Free-group Kesten random walk

This package freezes the uniform symmetric random walk on the free group \(F_d\), \(d\ge2\), with degree \(D=2d\).  It proves the complete Kesten root measure and full purely absolutely continuous spectrum, the radial birth--death chain, exact even-return and first-return laws, transience, escape speed, radial CLT, and the critical rank-one \(\mathbb Z\) boundary.

The exact JSON receipt has 1,997 finite rows.  It checks normalization and combinatorics only; the infinite-tree spectral and probability claims are proved analytically in `THEOREM_PACKAGE.md` and `paper/main.pdf`.

Route-A result: `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`, overall `ROUTE_A_REJECTED`; Route B is locked off under `NO_BAD_EULER_OR_ROOT_NUMBER`.
