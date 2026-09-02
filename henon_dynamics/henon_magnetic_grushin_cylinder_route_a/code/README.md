# Code map

- `c293_grushin_producer.py`: deterministic exact/precision spectral receipt.
- `c293_grushin_checker.py`: strict duplicate-rejecting exact JSON/YAML
  schemas, a canonical evaluation-YAML semantic hash, and producer-independent
  Fourier–Hermite level-sum reconstruction.
- `c293_grushin_sympy_crosscheck.py`: exact oscillator, divisor, count,
  Laurent-coefficient, and flux identities.
- `c293_grushin_replay.py`: two isolated byte-identical evidence productions.
- `c293_grushin_mutation.py`: 75 stale/repaired-hash, raw duplicate, grid,
  numerical, theorem/proof, type, spectral-type, and evaluation-YAML attacks
  (54 evidence JSON and 21 YAML).
- `c293_release_manifest.py`: full executable and six-fresh-PDF release gate.

Python 3, mpmath, SymPy, and PyYAML are required.  The checker imports no producer
module and does not use the producer's closed heat-channel expression.
