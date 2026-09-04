# Narrative report — P191 Round 0

## Problem

Represent a positive composition by its internal partial-sum cuts.  At one
epoch, retain the cut ending part `a_i` exactly when `a_i` divides its endpoint
`s_i`, delete every other old cut simultaneously, and read the resulting
coarsening.  The aim is to determine recurrence, fixed states, the sharp
global transient, and every labelled one-step fibre for every total `N`.

## Mechanism

The temporal mechanism is monotone cut deletion.  The first cut is permanent,
so a nonfixed composition has at most `length-2` effective deletions.  Equality
in this bound rigidifies the source to one part two among ones and then forces
that part into the second position.

The inverse mechanism is different.  A source is an increasing path through
its cut positions.  A source edge ending at `v` survives exactly when its
length divides `v`.  Prescribing a target therefore gives a directed path
problem: source edges may not skip target cuts, an internal target endpoint
requires a dividing final edge, and every unretained intermediate cut requires
a nondividing incoming edge.  Mandatory target cuts factor the count over
consecutive target intervals.

## Theorem-level progress

- Fixed states are exactly the compositions whose every nonfinal part divides
  its ending prefix; last-cut decomposition gives an exact fixed-state
  recurrence.
- Every recurrent state is fixed.  The maximum tail is zero for `N<=3` and
  `N-3` for `N>=4`.
- For every `N>=4`, `(1,2,1^(N-3))` is the unique deepest state, with the
  explicit all-time orbit `(1,2+t,1^(N-3-t))`.
- Every target fibre is an exact no-skipped-cut path DP, equivalently a product
  of interval path counts.  Positivity is a complete one-step image criterion.
- The target-local counts sum to all `2^(N-1)` source compositions.

## Subtraction and status

The composition--subset bijection, refinement order, elementary divisibility,
and generic path dynamic programming receive zero contribution credit.  P126
splits parts, P147 merges equal runs, P131 rotates Euclidean quotients, P169
transfers set-partition tokens, P181 reverses a permutation prefix, P185 writes
prefix-diversity words, and P186 rank-compresses subset supports.  None has the
literal predecessor-dependent divisibility cut rule, but this internal
noncollision and the bounded external search are not novelty evidence.

Lifecycle: `ROUND0_AUTHOR_FREEZE / OWNER_AMBER / HOLD_EXTERNAL`.

