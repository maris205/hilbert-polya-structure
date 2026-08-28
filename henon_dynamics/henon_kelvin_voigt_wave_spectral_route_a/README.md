# HCS-C218: Kelvin--Voigt wave spectral atlas

This release freezes the one-dimensional Dirichlet Kelvin--Voigt equation

`u_tt - u_xx - b u_txx = 0` on `(0, pi)`, `b >= 0`,

at the physical time clock.  The sine modes expose an exact underdamped /
critical-Jordan / overdamped atlas.  The slow roots approach the non-eigenvalue
essential spectral point `-1/b`, while the fast roots escape to minus infinity.
The package proves the exact spectral-abscissa gap, its unique optimal damping,
energy dissipation, and the noncompact semigroup boundary.

Reproduce the certificate with:

```text
python3 code/c218_kv_producer.py
python3 code/c218_kv_checker.py
python3 code/c218_kv_sympy_crosscheck.py
python3 code/c218_kv_replay.py
python3 code/c218_kv_mutation.py
python3 code/c218_release_manifest.py
```

Route A is intentionally rejected with
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`.  No target arithmetic,
Euler factors, root numbers, automorphy, or Hilbert--Polya operator is claimed.
