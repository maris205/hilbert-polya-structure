# Exact code lanes

- `c347_kuramoto_producer.py` writes the canonical exact evidence.
- `c347_kuramoto_checker.py` independently rebuilds and exact-locks all semantic fields and ledgers; it does not import the producer.
- `c347_kuramoto_sympy_crosscheck.py` checks 60 independent symbolic identities.
- `c347_kuramoto_replay.py` compares two isolated productions with the checked artifact.
- `c347_kuramoto_mutation.py` requires every repaired-hash, stale-hash, nested-schema, JSON, and YAML attack to fail.
- `c347_release_manifest.py` runs every lane, optimized-mode refusals, deterministic PDF rebuilds, font/text/raster checks, and the 27-payload closure.

All Python entry points refuse optimized execution because assertions and explicit validation are part of the certificate.
