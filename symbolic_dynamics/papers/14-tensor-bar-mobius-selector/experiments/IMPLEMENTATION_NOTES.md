# SD-C16 Implementation Notes

## Reproduction

From this paper-project directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python code/sdc16_tensor_bar_experiment.py
PYTHONDONTWRITEBYTECODE=1 pytest -q -p no:cacheprovider \
  code/test_sdc16_tensor_bar_experiment.py
sha256sum -c results/SHA256SUMS.txt
```

The generator rewrites only `results/`. It uses the Python standard library
plus `mpmath` for selected 80-digit evaluations. No network, GPU, prime-table
file, or zero-table file is required.

## Independent implementations

- `mu_tensor` is computed once by divisor-poset recursion and independently
  by a linear Möbius sieve.
- Bar endpoint coefficients are obtained both from explicit ordered word
  layers and from a recursive Dirichlet inverse.
- The raw determinant is checked from word-length partial sums, the closed
  geometric form, and `1/zeta(s)`.
- The local continuant uses exact `Fraction` arithmetic; selected dense-style
  checks from Paper 13 are not reused as evidence for the global bar object.

## Domain discipline

- Individual bar words are summed only for `Re(s)>sigma_bar`.
- In `1<Re(s)<=sigma_bar`, only endpoint-first finite coefficient grouping is
  used. Numerical Möbius partial sums are labeled observations.
- The global incidence profile, Paper-13-style local character audit, and
  reduced bar determinant are stored as separate readouts. No coordinatewise
  stitching is performed.

## Reproducibility boundary

The exact CSV/JSON artifacts are authoritative for finite claims. Floating
residuals depend on `mpmath` arithmetic but not on platform random state; all
random controls have fixed seeds. `PYTHONDONTWRITEBYTECODE=1` and disabled
pytest cache keep the shareable directory free of generated caches.
