# AM1 nonauthor original-coordinate check: frozen before execution

2026-09-08 UTC. Coordinator-requested independent review of the complete
AM1 candidate. No admission. Only this review directory is writable.
The author producer is read but must not be imported or executed.

For every a in [-145,1] compute the functional graph of

    F_a(x,y)=(y,y(y+1)/2+a-x)

on the SAME original-coordinate square {-19,...,19}^2. Every edge leaving
that square goes to an escape terminal. There is no doubled coordinate,
filtered alphabet, iterative pruning or period cutoff in this checker.

Proof of the box: for any integral periodic scalar sequence and
M=max |x_i|, the recurrence gives M^2-5M-2|a|<=0. Since |a|<=145,
M^2-5M-290<=0. At M=20 the left side is 10 and thereafter it strictly
increases on integers, so M<=19. Integrality is separately checked in
the analytic review. Thus the box contains the ENTIRE periodic locus
for each residual parameter, not a conjectural height range.

Use path-index cycle detection on a finite functional graph: traverse
each unseen vertex until an escape, a previously completed vertex, or
a repeated vertex on the current path. In the last case retain precisely
the cycle suffix. Then mark the path completed. Every graph vertex is
processed once. Cycles are disjoint, and rotation canonicalization does
not identify reversals. This proves period-unbounded finite completeness
without using the author's injective-pruning algorithm.

Only AFTER computing all 147 independent graphs, load the author's
FINITE_CORE_RESULTS.json and compare every full oriented cycle and expanded
periodic-state set. Validate the author file's range, period labels, word
primitivity, per-parameter counts, and summary against our output. Record
input/producer/checker hashes. The producer hash is read-only provenance,
not evidence that it was rerun. Independent output is created exclusively;
no successful unchanged rerun is planned. A mismatch must be reported, not
silently repaired or used to fit the expected answer.
