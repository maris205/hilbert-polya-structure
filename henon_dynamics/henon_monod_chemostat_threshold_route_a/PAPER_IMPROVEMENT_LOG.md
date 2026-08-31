# Paper improvement log

## Round 0 — theorem skeleton

The first manuscript froze the Monod convention, exposed total nutrient, and
stated the three threshold regimes with the invariant-leaf separation.

## Round 1 — proof and boundary repair

The revision added scalar comparison for global convergence, separated the
invariant `X(0)=0` face from positive biomass, computed both triangular
linearizations, and recorded the dilution/no-growth/zero-feed boundaries.
These changes strengthened the theorem rather than polishing wording.

## Round 2 — recurrence and evidence closure

The final revision added the proof that periodicity forces `Q=S_in` and then
collapses to a scalar flow, the critical reciprocal-log law and asymptotic
coefficient, a source-ownership paragraph, and the exact independent-checker,
SymPy and mutation counts.  It also prints the full Route-A tuple and scope
literal.  The three PDFs are pairwise different; the final source generates
`main_round2.pdf` and `main.pdf` byte for byte.
