# Reproducibility

Run from this directory with ordinary, nonoptimized Python:

```bash
python -B code/c369_s4_frobenius_producer.py
python -B code/c369_s4_frobenius_checker.py
python -B code/c369_s4_frobenius_sympy_crosscheck.py
python -B code/c369_s4_frobenius_replay.py
python -B code/c369_s4_frobenius_mutation.py
python -m unittest tests/test_c369_smoke.py
python -B code/c369_release_manifest.py --write --build-pdfs
python -B code/c369_release_manifest.py
```

The producer uses an explicit low-degree polynomial gcd/powering algorithm.
The checker never imports it and instead factors with SymPy's low-level
finite-field `gf_factor` backend.  The symbolic lane independently checks
the discriminant, witness products, `S4` class sizes, permutation matrices,
Möbius inversion, formal logarithmic derivatives, and the ramified gcd.
The replay performs two isolated byte-identical evidence builds.  The
hostile suite repairs the inner payload hash after semantic mutations.
The checker and hostile suite also lock the C12A/C369 ownership split and the
exact collision-boundary strings.

The release gate refuses `python -O` and `python -OO`, strictly parses JSON
and YAML, locks the evaluator bytes and semantics, builds all three
conditional manuscript rounds twice under epoch `1788480000`, rejects
warnings, checks embedded subset fonts, extracts text, rasterizes every
page, and closes a self-excluding file manifest.
