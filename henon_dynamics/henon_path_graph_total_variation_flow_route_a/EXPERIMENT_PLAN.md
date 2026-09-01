# C279 executable experiment plan

## Claim-driven checks

1. Enumerate all 19,530 vectors in `{-2,-1,0,1,2}^n`, `1<=n<=6`, using exact
   rational arithmetic.  At every event check mass, the minimal feasible edge
   flux, common facet speed, lack of splitting, event-count bound, both
   dissipation identities, ROF KKT conditions at event times and interval
   midpoints, final mean, and the proved consensus-time bound.
2. Retain an ordered SHA-256 transcript of every exact event schedule plus
   per-dimension histograms.  Store eight complete witness traces covering a
   singleton, constant data, endpoint facets, one and two simultaneous
   mergers, mixed plateaus, a generic cascade, and rational data.
3. Add five exact rational stress inputs of dimensions 8 through 12 and lock a
   second transcript digest.
4. Reconstruct all transcripts in a producer-independent coordinate engine.
   It imports no producer code: it solves the plateau edge-flux interpolation,
   forms `-D^T z`, and discovers vanishing jumps directly.
5. Independently use SymPy to reconstruct incidence identities, every possible
   block-flux interpolation through size nine, all sign-chamber dissipation
   identities through size eight, the Poincare coefficient identity through
   size twelve, and a simultaneous collision.
6. Run the producer in two unrelated temporary trees and demand byte identity
   with each other and the retained evidence.
7. Repair the payload hash after 58 semantic attacks and require every attack
   to fail against the actual checker.  Separately alter a payload without
   repairing its hash as the stale-hash control.

The finite grid is deliberately smaller than the all-real theorem.  It is a
high-density implementation and convention audit; the maximal-monotone,
coalescence, finite-extinction, and averaged-subgradient arguments remain the
proof.
