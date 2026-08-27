# C189 executable certificate

Run from the repository root:

```bash
python3 henon_dynamics/henon_watanabe_strogatz_mobius_reduction_route_a/code/c189_ws_producer.py
python3 henon_dynamics/henon_watanabe_strogatz_mobius_reduction_route_a/code/c189_ws_checker.py
python3 henon_dynamics/henon_watanabe_strogatz_mobius_reduction_route_a/code/c189_ws_sympy_crosscheck.py
python3 henon_dynamics/henon_watanabe_strogatz_mobius_reduction_route_a/code/c189_ws_replay.py
python3 henon_dynamics/henon_watanabe_strogatz_mobius_reduction_route_a/code/c189_ws_mutation.py
python3 henon_dynamics/henon_watanabe_strogatz_mobius_reduction_route_a/code/c189_release_manifest.py
```

The producer records exact rational local Riccati jets, disk automorphisms,
generic configurations, collision strata, cross ratios, and constant
generators.  The checker imports no producer code and reconstructs eligible
Möbius maps from three landmarks.  SymPy separately derives the generic
Riccati, `su(1,1)`, circle, cross-ratio, and fixed-root identities.  Replay
fixes canonical bytes, and mutation tests require semantic rejection even
after the payload hash is repaired.

The finite rows are regression evidence.  The all-parameter theorem is proved
in `THEOREM_PACKAGE.md` and the paper; it is not inferred from the census.
