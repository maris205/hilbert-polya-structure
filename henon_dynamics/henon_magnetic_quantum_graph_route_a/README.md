# HCS-C138 — gauge-invariant magnetic theta-graph scattering

C138 adds a two-dimensional magnetic-flux torus to the exact theta metric graph of C133.  For edge lengths `(1,2,3)` and degree-three Kirchhoff scattering, it freezes

`U_alpha(k)=P_alpha(k) S P_alpha(k)`

on six directed bonds.  A common shift of all three magnetic phases is an exact gauge redundancy.  The antiunitary `Theta=J K` sends `alpha` to `-alpha` and the evolution to its inverse.  The package derives the complete Laurent secular determinant in powers `rho^0,rho^2,rho^4,rho^6`, keeps oriented winding monomials for primitive walks, and supplies zero-flux, common-gauge, pi-flux, pi/2-reversal, wrong-Kirchhoff, and asymmetric-length controls.

The complete determinant is even under flux reversal because reverse orientations pair.  Individual orbit phases are not collapsed to cosines in the ledger.

Route-A verdict:

`(A1_WEAK, A2_FAIL, A3_FAIL, A4_UNITARY_OR_SCATTERING_CANDIDATE)`; `route_b=false`.

Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.  No target divisor, arithmetic Euler factor, root number, automorphy, or Hilbert–Pólya operator is claimed.
