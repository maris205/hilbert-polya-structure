# HCS-C265 — exponential Hawkes stationary and covariance atlas

This package closes one source-local theorem for the univariate exponential
linear Hawkes process

`d lambda_t = -b(lambda_t-nu)dt + a dN_t`,

with predictable event intensity `lambda_(t-)`.  It contains the joint affine
count/intensity transform, the subcritical stationary Laplace law, every
stationary intensity moment, intensity covariance, the complete counting
covariance measure including its Dirac atom, a no-`1/(2*pi)` Bartlett spectrum,
window-count variance, Borel clusters, and all declared parameter boundaries.

The three covariance objects are deliberately separate.  The source point-
process spectrum is not a target divisor, an Euler product, or a Hilbert--Pólya
operator.

## Reproduce

```bash
python3 -B code/c265_hawkes_producer.py
python3 -B code/c265_hawkes_checker.py
python3 -B code/c265_hawkes_sympy_crosscheck.py
python3 -B code/c265_hawkes_replay.py
python3 -B code/c265_hawkes_mutation.py
python3 -B code/c265_release_manifest.py
```

The frozen source baseline is
`a24c701881d22a4e49eaa2a44b94395c3c540b3d`; the build epoch is
`1788048000`; the scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Main artifacts

- `THEOREM_PACKAGE.md` — proof dependencies and exact theorem.
- `results/c265_hawkes_evidence.json` — canonical executable evidence.
- `paper/main.pdf` — final manuscript, byte-equal to round 2.
- `C265_RELEASE_MANIFEST.json` — self-excluded 27-payload ledger.
