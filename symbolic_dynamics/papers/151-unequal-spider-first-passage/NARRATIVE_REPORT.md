# Narrative report — P151

**Status:** **ROUND-2 INTERNAL REVIEW ACCEPTED / HOLD_EXTERNAL**

## Technical story

The process is elementary, but unequal arms prevent radial lumping: the leaf
label and the clock remain coupled.  The useful normalization is not a full
matrix inverse.  It is one centre excursion.  A failed excursion returns to
the same renewal state, while a successful excursion records its arm.  The
killed one-dimensional transforms share continuant denominators, so summing
failed excursions produces one common rational denominator for all marked
leaves.

The explicit unequal-spider continuant factorization is the first residual
axis; generic finite-chain marked laws and moment matrices are already owned
background.  Its denominator also contains the moment information, but a
second proof route makes the compact scalar specialization transparent:
compute the first two durations of one arm attempt and apply a stopped-renewal
identity.  This produces a three-statistic formula using
`H=sum ell_i^-1`, `L=sum ell_i`, and `C=sum ell_i^3`.

The prior mean `L/H` becomes useful only after ownership subtraction.  With
`r` and `L` fixed, strict integer unit transfers identify both equality
classes: one long arm minimizes the mean, while balanced arms maximize it.
The same prior endpoint law gives the final residual axis.  Endpoint ratios
recover only the primitive integer ray of the arm vector; a common dilation
is exactly invisible.  One additional scalar, the mean, grows quadratically
under dilation and therefore recovers the scale.

## What the paper must not claim

The paper does not claim the endpoint harmonic measure or expected absorption
time.  It does not claim equal-arm star hitting distributions.  It does not
claim general spider spectral analysis, generic rationality or time/place
laws of absorbing finite chains, or general-tree PGF algorithms.  Its inverse
result does not estimate unknown transitions,
recover unknown tree topology, handle noisy observations, or compete with
network tomography.

## Evidence summary

The paper-local verifier compares a literal vertex-state probability recursion
with the continuant rational formula coefficient by coefficient.  Additional
exact checks cover quotient derivatives, excursion moments, all bounded
fixed-mass equality classes, primitive-ray recovery, and equal-arm collapse as
an owned control.  Its cold replay passed 1,446,432 assertions byte for byte.
Review B also used a separate exact absorbing-system route, made two isolated
byte-identical builds, and inspected all six pages clean.  Enumeration is
falsification pressure, not a proof or source-clearance argument.

## Status

Hostile Review A's 0 Critical / 1 Major / 3 Minor findings were repaired;
Hostile Review B accepted with 0 / 0 / 0 surviving findings.  The internal
paper decision is **ROUND-2 INTERNAL REVIEW ACCEPTED**, while external status
remains `HOLD_EXTERNAL`.  A bounded source non-hit is not a novelty, priority,
authorship, or release certificate.
