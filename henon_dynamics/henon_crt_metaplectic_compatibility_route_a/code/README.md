# HCS-C136 code

- `c136_crt_metaplectic_producer.py` constructs the exact modular receipt.
- `c136_crt_metaplectic_checker.py` independently reconstructs every receipt and
  closes the evidence schema without importing the producer.
- `c136_sympy_crosscheck.py` checks the CRT, kernel, antiunitary, coherence, and
  negative-control congruences through an independent SymPy path.
- `c136_replay.py` regenerates the evidence in a temporary directory and compares
  the bytes.
- `c136_mutation.py` attacks semantic fields after checksum repair and separately
  tests the stale-checksum gate.
- `c136_release_manifest.py` records the 27 payload files and excludes itself.

Run all commands from the package root or repository root with Python 3.  No
network access, prime table, zero table, or floating-point comparison is used.
The checker independently reconstructs antiunitary involution, reversal,
Weyl-swap, and canonical CRT receipts without importing the producer.
