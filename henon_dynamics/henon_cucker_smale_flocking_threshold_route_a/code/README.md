# Code lanes

- `c362_cucker_smale_producer.py`: canonical exact evidence producer;
- `c362_cucker_smale_checker.py`: independent full-schema recomputation;
- `c362_cucker_smale_sympy_crosscheck.py`: separate symbolic derivation lane;
- `c362_cucker_smale_replay.py`: two isolated byte-identical producer runs;
- `c362_cucker_smale_mutation.py`: repaired-hash, stale-hash, parser, route,
  theorem, normalization, and boundary attacks;
- `c362_release_manifest.py`: 27-payload ledger, three-round PDF, font, text,
  raster, optimized-mode, and deterministic release gate.

Every executable refuses optimized Python and is intended to run with
`PYTHONDONTWRITEBYTECODE=1`.
