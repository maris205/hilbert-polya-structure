# C85 reproducibility commands

```bash
python3 code/c85_threshold_vector_poset_rigidity.py
python3 code/c85_threshold_vector_poset_rigidity_checker.py
python3 code/c85_sympy_lattice_crosscheck.py
python3 code/c85_replay_checker.py
PYTHONDONTWRITEBYTECODE=1 python3 code/c85_mutation_test.py
```

The producer groups the frozen C80 profile matrix after rebuilding closure.
The independent checker enumerates the 54-point group and reconstructs all
thresholds from target-minimal support antichains.  The mutation test builds
that independent expected object once and submits twenty-three altered
canonical receipts to the same validation boundary.
