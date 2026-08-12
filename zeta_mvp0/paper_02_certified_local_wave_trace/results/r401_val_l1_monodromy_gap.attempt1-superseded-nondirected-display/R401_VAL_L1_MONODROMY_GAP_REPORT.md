# R401-VAL-L1-MG local monodromy gap

Milestone status: **PASS_LOCAL_MONODROMY_GAP**.

Exact-rational parsing of all 202 frozen CAPD monodromy enclosures proves
`D_M = 4 - tr(M) > 3` throughout the accepted local fast branch.

- 128-bit minimum lower bound: `3.83599260664771702`
  at `S048`;
- 256-bit minimum lower bound: `3.8507419689457949`
  at `S049`;
- 128-bit maximum interval width: `0.054493101512001145`;
- 256-bit maximum interval width: `0.0250368624293953942`;
- every paired 128/256 interval intersects.

Hamiltonian symplecticity and the nonzero flow tangent identify this quantity
with the transverse Poincare determinant on the periodic orbit.  This is a
local-branch gap only.  The independent event-projected determinant,
Taylor-model residual, root-complement tree, global cover, and `delta_tr`
promotion remain open.
