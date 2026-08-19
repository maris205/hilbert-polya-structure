# C72 code

Run from the project directory:

```bash
python3 code/c72_coordinate_core_atlas.py
python3 code/c72_coordinate_core_atlas_checker.py
python3 code/c72_group_crosscheck.py
python3 code/c72_coordinate_core_atlas_replay_checker.py
python3 code/c72_mutation_test.py
```

The producer uses exact rational residues followed by cached finite-group
closure.  The checker verifies all coordinate relations back in the original
integer presentation, enumerates the abstract core lattice independently,
and compares actual subgroups.  The GAP lane checks the 20-subgroup,
ten-isomorphism-type inventory.
