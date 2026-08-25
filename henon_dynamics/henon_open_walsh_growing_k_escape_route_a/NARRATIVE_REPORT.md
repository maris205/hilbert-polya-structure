# C153 narrative report

## Result

C153 upgrades the finite-`k` open Walsh calculation to a controlled
large-system statement.  The key is not an asymptotic guess: writing
`n=qk+r` exposes exactly which tensor factors have crossed the opening.  Each
untouched factor contributes rank three and each touched factor contributes
rank two.  Once all factors have crossed, the image rank saturates at `2^k`.

At time `floor(alpha*k)`, this gives a piecewise-linear logarithmic escape law:
the positive rate is `alpha log(3/2)` up to one full factor cycle and
`log(3/2)` thereafter.  The `alpha=0` boundary remains the identity.

## Trace geometry

The trace behaves differently.  At fixed period, the factor permutation
remembers `gcd(n,k)`, so the unnormalized sequence ranges over a finite divisor
set rather than approaching a universal value.  Every divisor class recurs on
an explicit infinite subsequence, and equal complex values are merged.  The
period-two odd/even split proves nonconvergence concretely.  Dividing by the
ambient dimension nevertheless forces every fixed-period trace to zero.

## Interpretation and limits

The closed parent has zero escape, while moving the rank-two hole preserves the
rank law only because the moved one-site gate also has a simple zero and two
nonzero eigenvalues.  Its trace data can change.  Thus image escape is robust
under this control but is too coarse to determine trace geometry.

This is an exact source-side growing-system limit, not a full secular limit,
self-adjoint quantization, semiclassical target comparison, or Route-B result.
The conservative tuple is
`(A1_WEAK,A2_FAIL,A3_FAIL,A4_UNITARY_OR_SCATTERING_CANDIDATE)`.
