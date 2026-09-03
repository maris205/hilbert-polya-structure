# HCS-C327: delta-comb Kronig--Penney band-gap atlas

This package gives an all-parameter operator and spectral theorem for

\[
H_{a,g}=-\frac{d^2}{dx^2}+g\sum_{n\in\mathbb Z}\delta(x-na),
\qquad a>0,\quad g\in\mathbb R.
\]

It closes the quadratic-form realization, transfer matrix, Floquet
discriminant, pure absolutely continuous spectrum, Bloch multiplicities, the
complete sign-dependent band atlas (including `ga=-4`), open Bragg gaps,
controlled high-energy gap widths, and the band-indexed IDS/DOS.

## Reproduce

```bash
python3 -B code/c327_kronig_penney_producer.py
python3 -B code/c327_kronig_penney_checker.py
python3 -B code/c327_kronig_penney_sympy_crosscheck.py
python3 -B code/c327_kronig_penney_replay.py
python3 -B code/c327_kronig_penney_mutation.py
python3 -B code/c327_release_manifest.py
```

Every executable lane explicitly refuses `python -O`.  The final release gate
also rebuilds each of three substantive PDF revisions twice in isolated
directories at the fixed epoch, compares exact bytes, scans logs, verifies
embedded/subset fonts, extracts text, rasterizes every page, and enforces the
27-payload/28-physical-file ledger.

## Route-A result

Strict tuple:

`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`.

Overall verdict: `ROUTE_A_REJECTED`; Route B is locked.  Scope is
`NO_BAD_EULER_OR_ROOT_NUMBER`.
