# C183 executable paths

Run in order:

```bash
python3 code/c183_random_transposition_producer.py
python3 code/c183_random_transposition_checker.py
python3 code/c183_sympy_crosscheck.py
python3 code/c183_replay.py
python3 code/c183_mutation.py
python3 code/c183_release_manifest.py
```

The checker reimplements partitions, hook dimensions, character ratios, exact moments, direct ordered-pair word enumeration, determinant-factor strings, metadata cutoffs, source registry, Route-A qualifications, and the frozen-owner/weighted-path-owner boundary without importing producer code. It also verifies the primitive weighted path product for \(P_2\) through degree eight. Finite enumeration is a regression sentinel; the all-size theorem is proved in `THEOREM_PACKAGE.md` and the manuscript.
