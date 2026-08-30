# P117 narrative report

## Problem

Parallel local rules on runs often look like ordinary cellular automata, but
this rule reads maximal runs and can make two previously separated runs
coalesce in one round.  The question is whether that nonlocality produces
long or complicated recurrence.

## Early exact signal

The bit values are less informative than the run boundaries.  A boundary
survives exactly when the run on each side has the same parity.  Hence the
boundary set only shrinks, and recurrence immediately becomes an
equal-parity condition.

## Main progression

The recurrent condition yields a complete fixed/two-cycle census by cyclic
compositions.  For odd circumference, simple boundary loss already gives
the sharp clock.  For even circumference, raw boundary count is too weak.
Labelling each boundary by its site parity exposes a second shrinking
dynamics and the cost \(|q|+e(q)\), whose four-unit drop gives the exact
clock.

## Residual after subtraction

Binary runs, cyclic compositions, shrinking-cell models, and static run
enumeration receive zero contribution credit.  The labelled census is a
routine corollary once the temporal classification is known.  The residual
is only the map-specific conjunction of boundary survival, exact recurrence,
and two sharp clocks.  A bounded owner search found no identical package,
but that search miss is not a novelty or priority certificate.

## Claim ceiling

The paper gives maximum preperiods, not every transient layer or basin.
It treats labelled cyclic words, not rotation classes.  External circulation
remains HOLD.
