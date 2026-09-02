# HCS-C288 — one-dimensional delta point interaction

This package freezes, in units `hbar=2m=1`, the self-adjoint operator

`H_alpha=-d^2/dx^2`,  `psi'(0+)-psi'(0-)=alpha psi(0)`.

One theorem closes its quadratic form, resolvent, spectrum, unique attractive
bound state, two-channel scattering matrix, heat kernel, relative heat trace,
purely absolutely continuous continuum with no singular-continuous sector,
and all sign/threshold faces.  The finite receipt audits conventions; the
arbitrary-parameter theorem is analytic.

The independent checker rejects duplicate JSON keys, requires exact schemas
and unique complete grids, and reconstructs heat values from the resolvent by
inverse Laplace transformation and an integrated diagonal trace.  It reports
1,726 assertions; the hostile suite rejects 30/30 semantic, structural,
raw-JSON, and stale-hash specimens.

Run from this directory:

```bash
python3 -B code/c288_delta_producer.py
python3 -B code/c288_delta_checker.py
python3 -B code/c288_delta_sympy_crosscheck.py
python3 -B code/c288_delta_replay.py
python3 -B code/c288_delta_mutation.py
python3 -B code/c288_release_manifest.py
```

The strict Route-A tuple is
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)` with overall
`ROUTE_A_REJECTED`.  Scope is `NO_BAD_EULER_OR_ROOT_NUMBER`; Route B is off.
