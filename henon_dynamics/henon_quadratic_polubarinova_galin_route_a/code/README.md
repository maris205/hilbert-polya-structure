# Code lanes

- `c368_pg_producer.py`: canonical exact rational coefficient and endpoint
  evidence.
- `c368_pg_checker.py`: independent strict-schema recomputation; it never
  imports the producer.
- `c368_pg_sympy_crosscheck.py`: independent symbolic Fourier, area,
  monotonicity, injectivity, and cusp-series checks.
- `c368_pg_replay.py`: two-isolated-directory byte replay.
- `c368_pg_mutation.py`: repaired-hash semantic mutations and strict-parser
  attacks.
- `c368_release_manifest.py`: payload, optimized-mode, deterministic-PDF,
  extracted-text, raster, font, report, and self-excluding manifest closure.

Every executable refuses optimized Python because assertions are part of the
audit contract.
