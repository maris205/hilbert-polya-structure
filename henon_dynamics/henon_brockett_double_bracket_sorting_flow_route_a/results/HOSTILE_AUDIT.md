# C185 hostile audit

This is an internal artifact-bound audit, not external peer review and not an
independent error process.

The mutation suite recalculates the canonical payload hash after each of 67
semantic attacks.  It rejects attacks on identity/date/source commit, scope,
evaluator version/path/hash, every source-lock field, all nine theorem strings,
the `n<=7` cutoff, permutation values, heights, inversions, individual mode
rates and signs, mode digests, summary counts, rational matrix digests and
Lyapunov values, both repeated-spectrum controls including the
source-stabilizer/tangent distinction, all Brockett bibliographic
fields including year and DOI, the classical/package attribution boundary,
each Route-A layer, Route B, forbidden scope flags, nonclaims, and integrity
metadata.  A separate stale-hash attack is rejected before semantic trust.

The most consequential attacks fail:

- replacing A0 or A1 FAIL by a passing label;
- changing autonomous time to a hand-assigned logarithmic prime clock;
- promoting a tangent linearization to a target determinant;
- claiming all initial conditions sort, rather than excluding saddle stable
  manifolds;
- absorbing repeated spectra into the simple theorem;
- claiming a full Bruhat/Schubert closure result;
- changing Brockett’s source year to 1900 or assigning classical ownership to
  this package;
- promoting the state-dependent Lax generator to Route-B readiness;
- treating finite regression as the all-size proof.

The mathematical audit separately checks the sign convention: for `i<j`, a
pair rate is positive exactly at an inversion.  Thus `inv(pi)` is the unstable
dimension of the ascent flow and the Morse index of `-Tr(HN)`, not the Morse
index of `Tr(HN)`.  The repeated-source sentinel records its zero algebraic
rate as stabilizer/non-tangent on the smaller orbit.  The repeated-target
sentinel exhibits a non-diagonal commuting equilibrium and one genuine tangent
zero mode, preventing an accidental hyperbolicity claim beyond the frozen
assumptions.
