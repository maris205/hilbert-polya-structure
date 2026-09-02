# Code lanes

- `c317_newton_schulz_producer.py` deterministically emits exact evidence.
- `c317_newton_schulz_checker.py` independently reconstructs all frozen matrices and audits every static field.
- `c317_newton_schulz_sympy_crosscheck.py` checks residual, Jordan, block, and canonical-alpha identities from fresh symbols.
- `c317_newton_schulz_replay.py` requires byte-identical regeneration.
- `c317_newton_schulz_mutation.py` attacks hashes, parsers, semantics, and the Route-A YAML.
- `c317_release_manifest.py` closes the 27-payload release and three deterministic PDF rounds.

All Python lanes reject optimized execution so that assertions cannot be silently removed.
