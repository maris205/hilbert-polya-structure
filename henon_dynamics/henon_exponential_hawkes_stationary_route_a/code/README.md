# C265 executable certificate

- `c265_hawkes_producer.py`: canonical evidence producer using exact rational
  arithmetic.
- `c265_hawkes_checker.py`: producer-independent generator/Fourier/cluster
  reconstruction.
- `c265_hawkes_sympy_crosscheck.py`: generic symbolic validation.
- `c265_hawkes_replay.py`: two fresh paths versus released bytes.
- `c265_hawkes_mutation.py`: repaired-hash semantic mutations and stale-hash
  control.
- `c265_release_manifest.py`: full release gate and self-excluded manifest.

All Python invocations use `-B`; no bytecode is part of the package.
