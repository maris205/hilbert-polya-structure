# Implementation Notes

Run from the paper directory:

```bash
python code/sdc09_successor_experiment.py
python code/virtual_character_context.py
pytest -q code/test_sdc09_successor_experiment.py
```

The main run takes about 22 seconds on the development CPU because it
includes a 150-decimal cutoff audit.  Use `--skip-high-precision` for a fast
binary64 rerun.  Python dependencies are `numpy`, `scipy`, `sympy`,
`mpmath`, and `pytest` for the tests.

`det(I-L_t^*L_t)` is evaluated twice on small prefixes: directly by dense
linear algebra and by a Hermitian-tridiagonal continuant recurrence.  The
large-cutoff scan uses the recurrence, which is linear in cutoff size per
grid point.  Roots are refined only inside sign-changing brackets by 60
bisection steps.

The apparent binary64 stabilization after `N=8` is not recorded as exact.
The 150-decimal audit resolves the first-root shifts as approximately
`3.52e-13` (`8 -> 16`), `3.66e-38` (`16 -> 32`), and `1.73e-100`
(`32 -> 64`); the next shift is below the retained 150-digit computation.
