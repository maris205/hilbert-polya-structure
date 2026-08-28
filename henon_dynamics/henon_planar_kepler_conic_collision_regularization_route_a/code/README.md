# Code map

- `c216_kepler_producer.py` — emits the canonical exact/decimal evidence receipt.
- `c216_kepler_checker.py` — producer-independent recursive schema and value checker (260 assertions).
- `c216_kepler_sympy_crosscheck.py` — symbolic identities and antiderivative checks (17 checks).
- `c216_kepler_replay.py` — regenerates to a temporary path and checks byte identity.
- `c216_kepler_mutation.py` — repaired-hash, unknown-key, and stale-hash hostile mutations.
- `c216_release_manifest.py` — validates the complete 28-file release contract and writes the self-excluded manifest.

All code uses exact `fractions.Fraction` arithmetic for identities.  `mpmath` is used only for independently recomputed quadratures and displayed decimals.  No producer module is imported by the checker.
