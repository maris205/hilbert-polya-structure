# C84 reproducibility commands

Run from the project directory:

```bash
python3 code/c84_minimum_repair_matroid.py
python3 code/c84_minimum_repair_matroid_checker.py
python3 code/c84_sympy_graph_crosscheck.py
python3 code/c84_replay_checker.py
python3 code/c84_mutation_test.py
```

The producer writes canonical JSON.  The checker accepts `--evidence PATH`,
reconstructs the C75 point-set closure table, enumerates every deletion set
and every minimum repair witness independently, and verifies basis exchange
without importing producer code.
