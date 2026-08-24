# Paper improvement log — C125

No external reviewer, review score, acceptance prediction, or novelty
judgment is claimed.  Two internal evidence-led revision passes were applied;
the named PDF snapshots are synchronized final release views so none retains
an obsolete claim boundary.

## Round 0 — baseline

The baseline established the determinant fixed-count formula, the rational
zeta, and the Fourier action.  It did not yet distinguish unsigned orbit
cardinalities from signed Lefschetz data, and it stated non-trace-class status
without an explicit compactness witness.

## Round 1 — proof and ownership repair

- added the integer torus-kernel argument and all-order trace recurrence;
- added Möbius primitive counts and a logarithmic series reconstruction;
- replaced an informal spectral assertion by the explicit orthonormal
  sequence \(e_{(j,0)}\mapsto e_{(2j,j)}\);
- separated the Artin--Mazur orbit zeta from any ordinary Koopman Fredholm
  determinant.

## Round 2 — controls and Route-A repair

- added the parabolic nonisolated-fixed-set control;
- added the signed-determinant control and cyclic Fourier-aliasing table;
- added the explicit “Progress over prior gate” comparison to C119 and C121;
- froze the evaluator tuple to
  `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)` and
  `route_b_invocation_allowed=false`;
- tightened target-divisor, analytic, arithmetic, Hilbert--Pólya, and Route-B
  nonclaims;
- added independent reconstruction, 238-check SymPy, replay, 23 hostile
  mutations, deterministic build, font, log, and raster audit provenance.

All three named round PDFs are byte-identical to the final source by design.
The prose history above records the revisions without preserving a binary
snapshot that makes superseded assertions.
