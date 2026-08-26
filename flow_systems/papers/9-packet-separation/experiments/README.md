# Reproduction

Run the complete deterministic package from the Paper 9 directory:

```bash
./experiments/reproduce.sh
```

The script:

1. disables Python bytecode and runs the full unit-test suite;
2. regenerates the checked-in CSVs and manifest;
3. runs verify-only hash, row, metric, active-lock, and implementation checks;
4. generates two new copies in independent `mktemp` directories;
5. compares all nine generated files byte for byte; and
6. rejects `__pycache__` directories and `.pyc` files in the package scope.

It uses no network or randomness and removes only the temporary directory it
created. This is a reproducibility and regression runner, not a mathematical
proof runner. Finite cylinders do not prove profinite density, finite cyclic
values do not prove source-topology convergence, and finite topology controls
do not prove an infinite quotient separation theorem.
