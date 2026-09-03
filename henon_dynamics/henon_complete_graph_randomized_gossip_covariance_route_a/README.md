# HCS-C333: complete-graph randomized gossip covariance

This package proves the endpoint-aware second-moment transfer spectrum for
relaxed uniform pairwise gossip on `K_N`, including explicit invariant-block
projectors, the `eta=0` eigenspace merger, exact
covariance evolution, sharp mean-square consensus, and every low-dimensional
or relaxation-endpoint face.

## Reproduce

```bash
python -B code/c333_gossip_producer.py
python -B code/c333_gossip_checker.py
python -B code/c333_gossip_sympy_crosscheck.py
python -B code/c333_gossip_replay.py
python -B code/c333_gossip_mutation.py
python -B code/c333_release_manifest.py
```

The checker is producer-independent.  Replay is isolated and byte exact.
The mutation lane repairs the payload hash after semantic attacks.  The
release command performs fresh two-pass LuaLaTeX builds for all three rounds,
checks extracted text, rasterization, embedded/subset fonts, the exact
27-payload ledger, and optimized-Python refusal.

Scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.  Route tuple:

`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`.

Overall verdict: `ROUTE_A_REJECTED`; Route B is not authorized.
