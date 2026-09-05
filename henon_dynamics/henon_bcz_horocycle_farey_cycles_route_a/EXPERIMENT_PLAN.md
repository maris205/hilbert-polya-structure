# Frozen exact-control plan

No stochastic experiments or GPU computations are required.
For every N=1..64, the producer runs the exact integer floor map from (1,N),
records its whole primitive cycle, all starting-position matrices and five
positive repetitions. It tests the real scales 2/(2N+1) and 1/N, both rational
and exact. The independent checker reconstructs sorted Farey fractions instead
of importing the producer. It checks domain, floor inequality, inverse and
lattice identity at each point. Additional grids are N=2..17 wall probes and
n=1..128 fixed-set descriptions. The symbolic lane is a separate derivation.

Complete expected finite totals: 64 layers, 27,833 marked points, 55,666
rational-scale step controls, 27,833 matrices, 320 repetitions, 16 walls,
128 fixed-iterate rows; 14 universal symbolic identities, 256 exact layer
identities, and 65 ninety-digit non-certified numerical controls.

Hostile tests repair the JSON payload hash after each semantic mutation.
YAML attacks call both the checker and the actual --write release entrypoint.
Optimized Python must refuse before argument handling or writes.
