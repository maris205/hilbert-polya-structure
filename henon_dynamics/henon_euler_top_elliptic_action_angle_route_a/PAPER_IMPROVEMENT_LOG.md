# C186 paper improvement log

## Round 0 -- derivation skeleton

The first draft froze the inverse-inertia convention and recorded the two Jacobi charts. Its weakness was that the singular layer, action coordinates, and sampled-time owner were only terse remarks.

## Round 1 -- full energy atlas

The second draft added the six axial linearizations, the four explicit heteroclinic branches, stable endpoint periods, KKS cap actions, and the action--period identity. It also separated finite regression rows from the all-parameter proof.

## Round 2 -- hostile boundary revision

The final draft made the time-map statement iterate-exact, proved that sufficiently large iterates have positive-dimensional fixed circles, and replaced any suggestion of a finite global Artin--Mazur count by an explicit stop. It added degenerate symmetric/zero-momentum boundaries, source attribution, the Koopman direct integral, and strict Route-A nonclaims.

The three archived PDFs are content-distinct. This internal improvement process is not external peer review.

## Final release normalization

The cross-package audit repaired two missing LaTeX command markers in the
Markdown rendering of the heteroclinic formula.  More importantly, it caught
an inconsistent Poisson-sign statement: with the frozen Euler convention the
raw axial momentum has bracket \(-1\) with the displayed angle.  The final
paper and proof now use the cap momenta \(G-M_3\) and \(G-M_1\), which have
bracket \(+1\), and the evidence adds independent symbolic and hostile checks
for that convention.  The exact 4,268-checker/25-SymPy/20-mutation counts are
also machine-readable.  All affected evidence, PDFs, reports, and hashes were
regenerated.
