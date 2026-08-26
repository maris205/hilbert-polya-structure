# Reproduction

Run the complete deterministic package from the Paper 10 directory:

```bash
./experiments/reproduce.sh
```

The script:

1. disables Python bytecode and runs the full unit-test suite;
2. regenerates the checked-in CSVs and manifest;
3. runs verify-only hash, row, metric, active-lock, and implementation checks;
4. generates two new copies in independent `mktemp` directories;
5. compares all eleven generated files byte for byte; and
6. rejects `__pycache__` directories and `.pyc` files in the package scope.

The command uses no network or randomness. Its cleanup trap removes only the
temporary directory it creates. This is a reproducibility and regression
runner, not a proof runner: exhaustive finite maps do not prove an actual
arithmetic-space theorem, finite circle meshes do not classify the full circle,
and finite prefixes do not prove an infinite `ell1` or unboundedness result.
