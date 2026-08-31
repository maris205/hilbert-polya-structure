# C261 executable evidence

- `c261_airy_producer.py` creates exact modular phase hashes, high-precision
  cubic DFT rows, and state-period receipts.
- `c261_airy_checker.py` independently reconstructs every phase, fixed stride,
  DFT coefficient, inverse transform, Parseval identity, and support period.
- `c261_airy_sympy_crosscheck.py` proves the Airy mode, cubic periodicity,
  valuation stride, and finite-character identities.
- `c261_airy_replay.py` regenerates evidence in a clean process and requires
  byte equality.
- `c261_airy_mutation.py` repairs hashes after semantic attacks and requires
  every attack to be rejected.
- `c261_release_manifest.py` runs all gates and builds the self-excluded
  27-payload content-addressed ledger.
