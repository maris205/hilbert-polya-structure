# C186 executable certificate

Run from the repository root:

```bash
python3 henon_dynamics/henon_euler_top_elliptic_action_angle_route_a/code/c186_euler_top_producer.py
python3 henon_dynamics/henon_euler_top_elliptic_action_angle_route_a/code/c186_euler_top_checker.py
python3 henon_dynamics/henon_euler_top_elliptic_action_angle_route_a/code/c186_sympy_crosscheck.py
python3 henon_dynamics/henon_euler_top_elliptic_action_angle_route_a/code/c186_replay.py
python3 henon_dynamics/henon_euler_top_elliptic_action_angle_route_a/code/c186_mutation.py
python3 henon_dynamics/henon_euler_top_elliptic_action_angle_route_a/code/c186_release_manifest.py
```

The producer evaluates 180 exact rational parameter sentinels covering both regular energy regimes, together with all axial stability types and the intermediate-axis separatrix. The independent checker reconstructs every coefficient identity and high-precision elliptic quantity without importing producer code. SymPy separately proves the symbolic coefficient identities. Replay fixes canonical bytes, and mutation tests require semantic rejection even after the payload hash is repaired.

The finite rows are regression evidence. The all-parameter theorem is proved in `THEOREM_PACKAGE.md` and the paper; it is not inferred from the census.
