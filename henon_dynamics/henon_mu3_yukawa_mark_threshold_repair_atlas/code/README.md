# C80 reproducibility commands

```bash
python3 code/c80_threshold_repair_atlas.py
python3 code/c80_threshold_repair_atlas_checker.py
python3 code/c80_sympy_crosscheck.py
python3 code/c80_threshold_repair_atlas_replay_checker.py
python3 code/c80_mutation_test.py
```

The JSON profile is intentionally complete (65536 rows x 20 targets).  The
checker reconstructs the finite closure and target-minimal antichains; it does
not use the producer's threshold rows as an input to the calculation.
