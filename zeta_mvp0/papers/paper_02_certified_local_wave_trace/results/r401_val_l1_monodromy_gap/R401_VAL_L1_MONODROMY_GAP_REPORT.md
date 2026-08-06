# R401-VAL-L1-MG-V2 local monodromy gap

Milestone status: **PASS_LOCAL_MONODROMY_GAP**.

Exact-rational parsing of all 202 frozen CAPD monodromy enclosures proves
`D_M = 4 - tr(M) > 3` throughout the accepted local fast branch.

Every displayed decimal below has exactly 18 places and
is generated directly from the exact fraction.  Lower bounds are rounded
downward and upper bounds are rounded upward; no binary floating-point
conversion is used.

- 128-bit minimum lower bound (downward):
  `3.835992606647717183` at
  `S048`; exact
  `479499075830964647977619704227032239226154693/125000000000000000000000000000000000000000000`;
- 256-bit minimum lower bound (downward):
  `3.850741968945794693` at
  `S049`; exact
  `385074196894579469387613658291110538545744780951414621536980801422153198627515135319/100000000000000000000000000000000000000000000000000000000000000000000000000000000000`;
- 128-bit maximum interval width (upward):
  `0.054493101512001146`; exact
  `10898620302400229029559993523404715625722307/200000000000000000000000000000000000000000000`;
- 256-bit maximum interval width (upward):
  `0.025036862429395394`; exact
  `5007372485879078731405407280141575363658644979935648484451374108247366648119552289/200000000000000000000000000000000000000000000000000000000000000000000000000000000000`;
- inherited all-job phase-slope lower bound (downward):
  `8.955040964476345874`
  at 128-bit
  `S000`; exact
  `111938012055954323433615300299077846499814991/12500000000000000000000000000000000000000000`;
- every paired 128/256 interval intersects.

The inherited positive phase-slope certificate gives
`dK_epsilon/dQ_plus > 0` at the `P_plus=0` event.  Thus the energy shell is
regular there and `dot(P_plus)=-dK_epsilon/dQ_plus` is nonzero, so the event
section is transverse to the Hamiltonian flow.  Hamiltonian symplecticity
and the invariant flag
`span(X_K) subset ker(dK) subset T_z(R^4)` give
`chi_M(t)=(t-1)^2 chi_DPi(t)` on the quotient, including possible unit
Jordan blocks.  Hence `D_M` is the determinant of the energy-section
transverse Poincare return on the periodic orbit.  This is a local-branch gap
only.  The independent event-projected determinant,
Taylor-model residual, root-complement tree, global cover, and `delta_tr`
promotion remain open.
