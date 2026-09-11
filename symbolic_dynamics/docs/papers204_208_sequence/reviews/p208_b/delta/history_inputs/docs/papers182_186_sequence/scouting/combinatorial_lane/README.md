# P182--P186 combinatorial breadth lane

**Date:** 2026-09-03 UTC  
**Route:** A, Stage 1 breadth/falsification  
**Lifecycle:** `HOLD_EXTERNAL`  
**Paper allocation:** none in this lane

This directory records twelve genuinely different literal finite dynamical
systems on words, subsets, permutations, set partitions, compositions,
graphs, and posets.  A parameter sweep of one update counts once.  Reverse,
complement, scheduler, and obvious parameter variants were excluded before
the denominator was frozen.

The exact standard-library replay is
[`verify_combinatorial_lane.py`](verify_combinatorial_lane.py).  It makes
**23,150,803 explicit assertions** and returns `RESULT=PASS`.  Its canonical
stdout is frozen in [`CANONICAL.txt`](CANONICAL.txt).

## Outcome

Two candidates cross the lane's theorem gate.

1. **`PDD`, prefix-diversity delay on words.**  It has a closed pointwise
   iterate, a sharp pointwise clock, every-time images, every-time
   every-target fibres, and an exact depth CDF.  Exhaustive controls cover all
   `n^n` words through `n=7` (823,543 states at the final rank).
2. **`RCS`, rank-compression support on subsets.**  Its ordered positive gap
   list evolves by subtracting one and deleting zeros.  This gives a closed
   pointwise iterate, the exact maximum-gap clock, every-time images,
   every-time every-target fibres, Fibonacci first images, all basins, and a
   unique deepest state.  Exhaustive controls cover every subset through
   `n=18`.

`DSR`, stable ranking of permutation displacements, is retained only as a
**reserve**.  It converges in every permutation through `S_9` to a
composition-coded fixed set of size `2^(n-1)`, but neither a general clock
proof nor a satisfactory every-target inverse is closed.  It must not be
promoted from its numerical signal alone.

The other nine systems are explicit kills.  In particular, lively periods or
large tails in the cyclic-difference and cyclic-gap maps were treated as
evidence against a uniform theorem, while one-step closures and
canonicalizers were rejected even when their enumerations were exact.

## Claim boundary

The owner search in [`OWNER_SEARCH_LOG.md`](OWNER_SEARCH_LOG.md) is bounded.
It located standard owners for restricted-growth words, rank transforms,
permutation displacement statistics, and the subset-to-multiset stretching
bijection.  Those ingredients receive zero contribution credit.  No inspected
source stated either selected **iterated literal together with its theorem
conjunction**, but that is only a bounded non-hit: it is not novelty,
priority, ownership, freedom-to-operate, or release evidence.

No manuscript, submission, public posting, or external contact is authorized.

