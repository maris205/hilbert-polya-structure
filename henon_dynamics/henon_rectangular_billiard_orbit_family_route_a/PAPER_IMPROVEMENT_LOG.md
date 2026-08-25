# C147 paper improvement log

No external or cross-model reviewer was available or claimed.  The two rounds
are genuine internal theorem/scope audits without numerical scores.

## Round 0 to round 1

The initial draft called each direction a “positive-measure family.”  That is
true only in a fixed-direction transverse slice; a single direction has zero
angular measure in the full energy shell.  It also described the transverse
parameter as one open interval, although vertex offsets can split the circle.

**Fix:** state the transverse circle-minus-finite-offsets decomposition into
open cylinders, assert only positive transverse length, and explicitly record
zero ambient Liouville measure.

## Round 1 to round 2

The second audit found orientation and symmetry bookkeeping too compressed.
In particular, the ordered ledger retains coordinate swaps while the
minimality claim quotients them, and axis directions are outside the positive
pair ledger.

**Fix:** distinguish four signed sectors, their two time-reversal pairs,
coordinate swap, and axis boundary classes; add the Dirichlet reflection count
and phase; state exactly which equivalence relation is used by the square-65
minimality proof and why the cutoff covers every square below 65.  Replace the
scalar Poincare shorthand by the family-tangent unit eigenvector of the full
reduced derivative.  Specify the Dirichlet half-wave, its principal-symbol
clock, domain, unitary group, and antiunitary time reversal.

## Final audit

The final PDF is checked against the exact evidence, strict scope flags,
fixed-epoch double compilation, embedded fonts, clean logs, extracted text,
and rendered pages.  Remaining limitation: no clean-family trace
regularization and no target comparison.
