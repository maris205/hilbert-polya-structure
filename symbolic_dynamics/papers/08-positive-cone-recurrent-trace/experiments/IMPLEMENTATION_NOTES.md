# SD-C10 Implementation Notes

Run from this paper directory:

```bash
python code/sdc10_positive_cone_experiment.py
pytest -q code/test_sdc10_positive_cone_experiment.py
sha256sum -c results/SHA256SUMS.txt
```

Dependencies are `numpy`, `scipy`, `sympy`, and `pytest`.  The executable
generates tensor atoms internally and writes the frozen JSON/CSV results to
`results/` by default.  It does not load Riemann-zero or target-spectrum
data.

The exact path enumerator uses matrix convention `[target, source]` and
left-multiplies cocycle labels.  The first chiral backtrack is verified with
opaque variables.  Numerical sweeps use IEEE-754 binary64 and fixed grids;
they are not promoted to infinite-cutoff theorems.

The word-ball computation is intentionally labelled a finite/rooted proxy.
Free-group balls are non-Følner, so normalized finite-section outputs are
not treated as a Fuglede--Kadison determinant or Brown measure.
