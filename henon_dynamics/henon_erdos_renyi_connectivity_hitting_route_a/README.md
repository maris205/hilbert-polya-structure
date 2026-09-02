# HCS-C307 — Connectivity hitting in the random graph process

This package reveals the edges of the complete labeled graph in a uniform
random order and closes the first connected prefix.  It derives the exact
connected-graph recurrence and, from it, every finite CDF, PMF, tail and raw
moment.  It then proves the Gumbel connectivity-hitting limit using exact
isolated-vertex factorial moments and a two-range bound on every other
connected component.

## Reproduce

Run from this directory:

```text
python3 code/c307_connectivity_producer.py
python3 code/c307_connectivity_checker.py
python3 code/c307_connectivity_sympy_crosscheck.py
python3 code/c307_connectivity_replay.py
python3 code/c307_connectivity_mutation.py
python3 code/c307_release_manifest.py
```

The release command verifies the exact 27-payload/28-physical-file tree and
rebuilds every manuscript round twice in each of two fresh directories.

The result is weak convergence only.  It does not assert finite-n equality
with the disappearance of the last isolated vertex and does not assert moment
convergence.  Route A is rejected at all five gates, Route B is locked, and
the scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.

The evidence also carries an exact, mutation-locked collision boundary for
C301 partition refinement, C291 dimer RSA, and C276 uniform random mappings.
