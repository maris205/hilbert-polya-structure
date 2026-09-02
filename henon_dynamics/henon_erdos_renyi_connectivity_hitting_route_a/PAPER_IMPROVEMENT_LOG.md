# Two-round paper improvement log

## Round 0 to round 1

The initial manuscript closed every finite hitting law but stopped before the
threshold.  The first revision added the exact isolated-vertex factorial
moment and its logarithmic asymptotic.  A hostile proof review rejected the
insufficient shortcut “no isolated vertices implies connected”; the repair
introduced a required spanning-tree factor and exact hypergeometric absence
probability, then summed component sizes in two ranges.

## Round 1 to round 2

The second review targeted overclaiming and edge cases.  The revision made
the floor/event equivalence explicit, separated `G(n,m)` from `G(n,p)`, and
closed `n=1`, `n=2`, maximum disconnected size, and finite out-of-range
software behavior.  It explicitly denies a pathwise last-isolated identity
and any moment convergence.  Evidence cutoffs, source ownership, scope, and
AI use were added.

## Final integrity pass

The moment telescoping factor, factorial-moment normalization, component
union-bound probability, two summation ranges, and Gumbel sign were checked
independently.  A control-character scan was added after an early malformed
LaTeX spacing command was found and repaired before archive builds.

## Cross-red-team hardening

The final closure now defines the falling factorial explicitly as
`(x)_{r↓}`, using the same notation in the theorem package, manuscript, and
machine proof certificate.  It also internalizes the registry-checked C301,
C291, and C276 collision boundary in the paper, source audit, evidence,
independent checker, repaired-hash mutation suite, and release manifest.
