# Paper improvement log

No external reviewer score or model-family independence is claimed.  Two internal, evidence-anchored hostile reviews produced substantive source changes and preserved PDF snapshots.

## Round 0 — baseline

The two-page baseline froze the magnetic graph, unitary family, Laurent determinant, oriented walk weights, controls, receipts, and strict Route-A boundary.  It was preserved as `paper/main_round0_original.pdf`.

## Round 1 — gauge and antiunitary audit

- Replaced a verbal common-phase argument by the exact `D_c S D_c=S` calculation.
- Derived `J conjugate(P_alpha(k)) J=P_alpha(-k)` and connected it explicitly to `U_-alpha(k)^{-1}`.
- Explained why the reversal identity must change the magnetic parameter rather than hold at fixed nonzero flux.
- Derived the `3×3` determinant from Sylvester's identity and the off-diagonal block structure.
- Moved the long firewall token to display form, eliminating the baseline overfull box.

The revised three-page paper was preserved as `paper/main_round1.pdf`.

## Round 2 — Laurent completeness and orientation audit

- Proved from the bipartite block reduction that all odd powers of `rho` vanish, so the displayed four coefficients are complete rather than truncated.
- Connected operator-level common gauge to ratio-only Laurent coefficients.
- Distinguished individual winding monomials from full-determinant inversion evenness and wrote the reverse map `m -> -m` explicitly.
- Explained the `pi` coefficient change and why nontrivial flux is not a common-gauge artifact.
- Rechecked the `pi/2`, wrong-Kirchhoff, asymmetric-length, tuple, and forbidden-claim controls.
- Corrected a rendered spacing command discovered during page-by-page visual inspection.
- Made the directed-bond block order explicit and distinguished the real
  half-phase lift from its `2*pi` single-edge sign conjugacy, so descent to the
  physical flux torus is stated without claiming entrywise periodicity.

The final three-page paper is preserved as `paper/main_round2.pdf` and is byte-identical to `paper/main.pdf`.
