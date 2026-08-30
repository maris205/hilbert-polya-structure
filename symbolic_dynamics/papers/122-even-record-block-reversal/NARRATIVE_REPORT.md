# Narrative and derivation report — P122

Status: **THEOREM PACKAGE COMPLETE / EXTERNAL HOLD**.

## Dynamics and sharp clock

The first changed record block is even.  Its leading entry is its strict
maximum, while reversal places a smaller entry at the first changed position;
this gives strict lexicographic descent.  Splitting a permutation uniquely as
`alpha n beta` reduces every orbit either to `alpha` without cost or to an
`(n-1)`-letter prefix after one step.  This proves the upper bound `n-1`, and
`(2,3,...,n,1)` realizes equality recursively.

## Pointwise fibres

For a target `sigma`, a proposed output segment can have come from an odd
unchanged record block only when its first endpoint is the complete prefix
maximum.  It can have come from an even reversed block only when its last
endpoint is that prefix maximum.  These endpoint tests define admissible
cuts.  Reversing exactly the even target segments reconstructs a word whose
selected starts are precisely its record cuts: the new-segment maximum lies
inside the new segment, so successive block maxima strictly increase, and no
interior entry can create an extra record.  This gives a genuine bijection,
not merely an indegree recurrence.

Partitioning admissible cuts by their last cut gives the displayed `h_j`
dynamic program.  It uses `O(n^2)` arithmetic operations after prefix maxima
are known; no unit-cost bit-runtime claim is made.

## Aggregate image theorem

Fibre nonemptiness uses only the target's record indicators.  The automaton
stores reachable even/odd cut parities, the last-record parity, reachability
immediately before that record, and current reachability.  Relative ranks of
successive permutation entries are independent choices; a record has weight
one and a nonrecord at position `j` has weight `j-1`.  Weighting the 32-state
transition by these multiplicities counts all targets, and summing terminal
states with current reachability one gives the complete image for every
size.  Subtracting from `n!` gives all Garden-of-Eden states.

## Evidence boundary

One implementation enumerates literal sources and targets; the other applies
only the record automaton.  Their agreement through `n=9`, followed by the
transfer through `n=30`, is a strong falsification control but proves no
all-size theorem or ownership assertion.  External circulation remains
**HOLD**.
