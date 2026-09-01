# C276 executable certificate

The six commands below form independent release gates.

- `c276_random_mapping_producer.py` exhausts all maps for `n<=7`, emits the
  exact formula atlas and scaling receipts, and binds the evidence payload.
- `c276_random_mapping_checker.py` imports no producer code.  It traces every
  orbit independently, canonicalizes cycles, and reconstructs every formula.
- `c276_random_mapping_sympy_crosscheck.py` verifies Stirling sums, forest
  determinants, normalizations, collision tails, and cycle expectations.
- `c276_random_mapping_replay.py` runs the producer in a fresh process and
  demands byte identity.
- `c276_random_mapping_mutation.py` repairs every changed payload hash and
  requires the checker to reject every semantic mutation.
- `c276_release_manifest.py` reruns all gates and closes the 27-payload ledger.

Run from the repository root with Python 3 and `PYTHONDONTWRITEBYTECODE=1`.
No script downloads data or imports another C276 executable.
