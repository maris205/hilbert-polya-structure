# C146 narrative report

## Outcome

C146 adds a genuinely nonabelian compact dynamical subtype.  The frozen
Heisenberg lattice automorphism has a hyperbolic horizontal quotient but fixes
the center.  This mixed behavior produces a clean central circle at every
iterate and forces every ordinary isolated-orbit stability denominator to
vanish.

## Explicit progress

The package does not merely state that a central eigenvalue is one.  It fixes
an upper-triangular coordinate convention, derives the integer-valued central
correction needed for lattice preservation, proves the all-iterate clean
component, computes the Lefschetz cancellation, and gives the exact
`L_(2n)-2` toral control ledger through iterate 20.

## Important correction

The nontrivial circle bundle prevents horizontal counts from being lifted
mechanically.  The class `(1/5,2/5)` is fixed by `A^2` on the base, yet the
central fixed equation has fractional obstruction `-4/5`.  Internal review
therefore replaced the intended `|det(A^n-I)|` nilmanifold component theorem
with a proved central-component theorem plus an explicit counterexample.

## Route-A interpretation

This is a useful negative subtype: clean periodic families obstruct the
ordinary isolated-orbit determinant before any target comparison.  The
Haar preservation supplies the natural Koopman unitary on `L^2(N,Haar)` with
the same iterate clock, but no bridge to the clean-family orbit weights is
constructed.  This supports only a formal lift hint.  The strict tuple is
`(A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)` and Route B remains disabled.
