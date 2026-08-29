# C229 code ledger

- `c229_cir_producer.py` writes the canonical high-precision JSON certificate.
- `c229_cir_checker.py` independently reconstructs every boundary, transform,
  Gamma, Laguerre, gap and atom row (235 assertions).
- `c229_cir_sympy_crosscheck.py` proves 18 generic Riccati, PDE, limit,
  Laguerre, stationary-flux and Feller identities.
- `c229_cir_replay.py` checks clean-process byte identity.
- `c229_cir_mutation.py` runs 20 hostile schema/provenance/numeric mutations.
- `c229_release_manifest.py` performs the final 28-file closure and PDF audit.

All scripts set `PYTHONDONTWRITEBYTECODE` in release/replay paths; build
sidecars are excluded and removed before manifest generation.
