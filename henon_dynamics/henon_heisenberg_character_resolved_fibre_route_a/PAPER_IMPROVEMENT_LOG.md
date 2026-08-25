# C151 paper improvement log

No external or cross-model reviewer was available or claimed.  Both rounds
are genuine internal theorem/scope audits without numerical scores.

## Round 0 to round 1

The first draft stated that the rotation was representative invariant but did
not show the lattice calculation.  That gap matters because the formula uses
both `v` and `m=(A^n-I)v`.

**Fix:** add the automorphism polarization identity, introduce
`s=(A^n-I)r`, and use `det(A^nv,A^nr)=det(v,r)` to reduce the change to an
explicit integer.  Add the clean-kernel statement and distinguish horizontal
class count from actual component count.

## Round 1 to round 2

The second audit found that an attractive early Lucas/parity pattern was not
an all-iterate theorem and that the root-of-unity sum needed an explicit
denominator justification.

**Fix:** extend the exact ledger to `n=12`, record the counterexamples at
`n=10,12`, delete the extrapolation, prove `Q_n=2D_n^2` by the adjugate and
degree-two denominator bound, and state that the projector is a finite
character filter rather than an operator trace formula.

## Final audit

The final artifact is checked against exact evidence, independent direct-
cocycle and SymPy paths, replay, hostile mutations, scope flags, deterministic
compilation, embedded fonts, clean logs, extracted text, and rendered pages.

## Final terminology cross-review

A separate read-only cross-review confirmed the mathematics and found one
remaining terminology ambiguity in auxiliary release documents.  Those
documents now say "central cyclic root-of-unity projector" rather than the
unqualified "character projector", matching the theorem and paper's explicit
statement that the generally quadratic rotation is not a homomorphism of the
horizontal quotient.
