# Paper 11 reproduction protocol

Run the complete deterministic control pipeline from any working directory:

```bash
bash papers/11-indiscrete-convolution/experiments/reproduce.sh
```

The script:

1. exports a stable locale, disables Python bytecode, and fixes the Python
   hash seed;
2. runs the complete `unittest` suite;
3. regenerates the checked-in results and runs strict `--verify-only`;
4. generates two fresh temporary result sets;
5. verifies both fresh sets;
6. compares every fresh CSV and manifest byte-for-byte with the checked-in
   version and with each other; and
7. rejects `__pycache__`, `.pyc`, and `.pyo` artifacts in the scoped Paper-11
   code, experiments, and results directories.

The temporary directories are created with `mktemp -d` and removed on exit.
No network, random source, external package, external dataset, target-zero
data, or fitting is used.
