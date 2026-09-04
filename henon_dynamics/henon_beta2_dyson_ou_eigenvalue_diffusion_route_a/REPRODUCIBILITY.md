# Reproducibility

From this package directory, run:

```bash
python -B code/c378_dyson_ou_producer.py
python -B code/c378_dyson_ou_checker.py
python -B code/c378_dyson_ou_sympy_crosscheck.py
python -B code/c378_dyson_ou_replay.py
python -B code/c378_dyson_ou_mutation.py
python -B -m unittest tests/test_c378_smoke.py
python -B code/c378_release_manifest.py --build-pdfs
python -B code/c378_release_manifest.py --write
python -B code/c378_release_manifest.py
```

The producer is canonical. The checker imports no producer code and rebuilds
all exact rows; its kernel determinant uses a Leibniz sum rather than the
producer's matrix determinant. The replay compares bytes from two isolated
directories. The hostile suite repairs internal hashes before asking the
checker to reject semantic mutations.

PDF builds use the checked-in `paper/main_round0.tex`, `main_round1.tex`, and
`main_round2.tex` wrappers under LuaLaTeX, `SOURCE_DATE_EPOCH=1788480000`,
suppressed optional metadata, two fresh builds per revision round,
strictly increasing page counts, embedded Latin and `Droid Sans Fallback`
checks, bilingual text extraction, rasterization, and a warning-free
settled-log gate.
