# C148 exact code

- `c148_walsh_baker_producer.py` constructs canonical evidence using exact
  four-coordinate `Q(sqrt(3),i)` arithmetic.
- `c148_walsh_baker_checker.py` imports no producer code and independently
  reconstructs the matrices, tensor-power action, traces, polynomials, paths,
  controls, and claim boundary.
- `c148_sympy_crosscheck.py` supplies a separate computer-algebra path,
  including literal sparse matrices for `k=1,2` and all coefficients through
  `k=5`.
- `c148_replay.py` demands byte-identical isolated regeneration.
- `c148_mutation.py` repairs the payload hash after semantic corruptions before
  requiring rejection, plus one stale-hash control.
- `c148_release_manifest.py` closes the 27-file payload ledger after the final
  PDF is frozen.

Run from the package directory or repository root:

```text
python code/c148_walsh_baker_producer.py
python code/c148_walsh_baker_checker.py
python code/c148_sympy_crosscheck.py
python code/c148_replay.py
python code/c148_mutation.py
python code/c148_release_manifest.py
```
