# Executable lanes

- `c378_dyson_ou_producer.py`: canonical JSON evidence.
- `c378_dyson_ou_checker.py`: code-independent, strict-schema reconstruction.
- `c378_dyson_ou_sympy_crosscheck.py`: symbolic Hermite, Vandermonde,
  Slater, partition-product, and gap checks.
- `c378_dyson_ou_replay.py`: two isolated byte-identical builds.
- `c378_dyson_ou_mutation.py`: repaired-hash JSON and strict-YAML attacks.
- `c378_release_manifest.py`: all-lane, three-round deterministic-PDF, and
  exact file-ledger release gate.

Every script refuses Python optimized mode so assertions cannot be silently
removed.
