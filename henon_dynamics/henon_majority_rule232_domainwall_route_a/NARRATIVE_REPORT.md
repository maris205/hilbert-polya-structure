# Narrative report

C251 changes the owner to a nonlinear threshold cellular automaton.  The
central observation is not a short cycle found by search: in wall coordinates
the synchronous majority rule is an exact erosion process.  Adjacent walls
are removed in pairs, so every finite wall block has a deterministic lifetime.

This immediately closes the full periodic picture.  A wall word with a zero
ends in isolated walls, which is precisely a fixed binary word.  The sole
exception is the all-one wall word, available only at even length; it lifts to
the alternating pair and gives one primitive temporal 2-cycle.  The bound
$\lfloor(n-1)/2\rfloor$ is attained for every $n\ge3$: use one zero wall and
a block of $n-1$ walls when $n$ is odd, and two adjacent zero walls with a
block of $n-2$ walls when $n$ is even.

The fixed language is a two-step subshift forbidding `010` and `101`.  Its
four-state pair graph has characteristic polynomial
((\lambda^2-\lambda-1)(\lambda^2-\lambda+1)), yielding the exact Lucas-plus-
sixth-root count.  A second family of run-length graphs, with a parity twist,
counts every transient depth and independently cross-checks the direct state
enumeration.

The result is deliberately source-local.  Rule-232's finite binary clock does
not select rational primes, produce a target divisor, or define a natural
Hilbert--Pólya operator; all Route-A gates beyond the analytic theorem remain
closed.
