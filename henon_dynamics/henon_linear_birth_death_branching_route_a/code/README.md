# C208 executable certificate

Run from the repository root:

```bash
python henon_dynamics/henon_linear_birth_death_branching_route_a/code/c208_branching_producer.py
python henon_dynamics/henon_linear_birth_death_branching_route_a/code/c208_branching_checker.py
python henon_dynamics/henon_linear_birth_death_branching_route_a/code/c208_branching_sympy_crosscheck.py
python henon_dynamics/henon_linear_birth_death_branching_route_a/code/c208_branching_replay.py
python henon_dynamics/henon_linear_birth_death_branching_route_a/code/c208_branching_mutation.py
python henon_dynamics/henon_linear_birth_death_branching_route_a/code/c208_release_manifest.py
```

The checker is deliberately producer-independent and reconstructs transition
coefficients by truncated convolution. The SymPy script uses a separate
symbolic route. The replay requires canonical byte identity, and mutations
repair the payload hash before testing semantic rejection except for the
separate stale-hash attack.
