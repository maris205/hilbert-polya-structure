# HCS-C321 — Preferential-attachment degree martingales

This package treats one frozen linear preferential-attachment tree, starting from the single edge on vertices `1,2` and forbidding self-loops and multiple edges.  It proves, in one paper, both the all-order rising-factorial law and moment-determinate square-root limit for every fixed vertex, and the global empirical degree law

`N_k(n)/n -> 4/[k(k+1)(k+2)]`

in `L2` for each fixed degree `k`.  Fixed-vertex degree `D_i(n)` and population count `N_k(n)` are never identified.

Exact rational dynamic programming through nine vertices, an independent weighted-history enumerator, symbolic identities, byte replay, hostile mutations, and optimized-mode rejection close the finite audit.  Those computations are regression witnesses, not proofs of the asymptotic results.

Run `python3 code/c321_release_manifest.py` after the release artifacts exist.  The Route-A result is `ROUTE_A_REJECTED`; Route B is locked under `NO_BAD_EULER_OR_ROOT_NUMBER`.
