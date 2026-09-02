# Claim-driven experiment plan

## Exact lane

Compute `C(n,m)` recursively by the unique component containing vertex 1.
For every row, form reduced rational CDF, PMF and tail values, then derive raw
moments 1 through 4 from the general tail-sum identity.  Check zero support,
Cayley's tree endpoint, the complete graph, and the maximum disconnected edge
count.

## Independent lane

Rebuild the recurrence without importing the producer.  Exhaust every labeled
graph mask through `n=6` (33,867 masks total) with an independent union-find
connectivity test.  Verify all recurrence cells through `n=12`, exact
probability normalization and support.  Use SymPy polynomial component
decomposition and abstract tail telescoping as a third lane.

## Asymptotic lane

Evaluate exact without-replacement isolated-vertex factorial moments at five
finite sizes, three window offsets and orders 1 through 4.  These 60 decimal
rows are diagnostics only; the all-`n` Poisson/Gumbel claim is proved by the
factorial-moment expansion and spanning-tree component bounds.

## Hostile lane

Attack model replacement, count cells, list lengths, bool/float aliases,
support, CDF/PMF/tails, moments, window coordinates, route/scope, canonical
JSON, strict YAML, the C301/C291/C276 collision map, repaired and stale hashes,
and optimized Python.
