# Code

- `c371_harper_producer.py` multiplies transfer matrices with polynomial
  entries and emits all-flux dense Bloch evidence.
- `c371_harper_checker.py` never imports the producer.  It reconstructs
  every Chambers polynomial from an explicit Hermitian reference fiber and
  rebuilds every phase panel.
- `c371_harper_sympy_crosscheck.py` implements the exact cyclotomic quotient
  `Q[zeta_q]/Phi_q` and verifies symbolic-lambda Fourier support and
  symmetries through denominator ten.
- `c371_harper_replay.py` requires two isolated byte-identical producer
  runs and equality with the committed evidence.
- `c371_harper_mutation.py` performs repaired-hash semantic mutations and
  hostile JSON/YAML parser attacks.
- `c371_release_manifest.py` runs every lane, smoke tests, deterministic
  paper builds, font/text/raster checks, and the 35-payload release ledger.
