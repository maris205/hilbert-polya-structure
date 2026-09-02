# Research question — HCS-C302

Can one self-contained paper connect every finite comparison-cost distribution
of classical randomized Quicksort to its asymptotic distributional dynamics:
exact PGFs, closed mean and variance, a rigorously unique contraction fixed
point, convergence of the varying-subproblem recurrence, and a licensed exact
third moment that decisively rules out a Gaussian limit?

The answer is yes under a frozen model: a uniform permutation of distinct keys,
a value-independent pivot with uniform rank (represented by the first key),
`n-1` pivot comparisons, and comparison-only cost.  The normalization is
exactly `(n+1)`, and empty/extreme subproblems remain in the recurrence.

Success requires two proof closures often hidden in shorthand: the fixed-point
contraction must be connected to finite `Y_n` by a mixed-subproblem limsup
argument, and existence in `L2` must be upgraded to `L3` before cubing.  The
resulting source probability laws must not be promoted to arithmetic dynamics.
