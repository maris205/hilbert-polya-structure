# HCS-C169: irrational Furstenberg skew-shift spectral obstruction

This package proves, for every irrational parameter, the complete iterate law, empty periodic ledger and \(\zeta_{AM}=1\), Haar--Koopman Fourier decomposition, exact reversor, and non-Schatten/ordinary-Fredholm obstruction.

The explicit progress is a complete spectral and operator-ownership theorem for a new Route-A subtype. The conservative verdict is `(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)`. Empty periodic data cannot carry the target. Route B remains false.

Run:

```bash
python code/c169_skew_shift_producer.py
python code/c169_skew_shift_checker.py
python code/c169_sympy_crosscheck.py
python code/c169_replay.py
python code/c169_mutation.py
python code/c169_release_manifest.py
```

The manuscript is `paper/main.pdf`. The JSON evidence is a finite regression sentinel; all-parameter conclusions are supported by `THEOREM_PACKAGE.md` and the manuscript proof.
