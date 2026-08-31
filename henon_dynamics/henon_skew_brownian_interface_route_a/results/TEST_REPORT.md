# Test report

Run from the package root:

```text
python3 -B code/c266_skew_brownian_producer.py
python3 -B code/c266_skew_brownian_checker.py
python3 -B code/c266_skew_brownian_sympy_crosscheck.py
python3 -B code/c266_skew_brownian_replay.py
python3 -B code/c266_skew_brownian_mutation.py
python3 -B code/c266_release_manifest.py
```

The checker imports no producer implementation.  Numerical quadrature uses
60 or more decimal digits, while exit probabilities and mean exit times are
also checked in exact rational arithmetic.  The symbolic pass reconstructs
generic BVP identities.  The release gate additionally checks fixed-epoch PDF
reproducibility, embedded fonts, text, and exact file closure.
