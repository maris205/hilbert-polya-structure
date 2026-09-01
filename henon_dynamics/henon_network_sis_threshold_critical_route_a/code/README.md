# C271 executable certificate

Run, from the package root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c271_sis_producer.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c271_sis_checker.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c271_sis_sympy_crosscheck.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c271_sis_replay.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c271_sis_mutation.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c271_release_manifest.py
```

The producer uses exact rational regular-network regression rows.  The checker
rebuilds adjacency matrices, connectivity, thresholds, equilibria, Jacobian
rates, and critical scalar solutions without importing producer code.  These
finite receipts do not replace the all-network proof.
