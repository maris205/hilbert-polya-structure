# C256 executable evidence

- `c256_kdv_producer.py` creates the canonical 90-decimal root, degeneration,
  and Galilean receipt without importing SymPy.
- `c256_kdv_checker.py` independently reconstructs periods and moments by
  regularized root quadrature and checks elliptic nodes.
- `c256_kdv_sympy_crosscheck.py` proves the cubic, `cn^2`, soliton, and
  Galilean algebra exactly.
- `c256_kdv_replay.py` regenerates the evidence in a clean process and
  requires byte equality.
- `c256_kdv_mutation.py` repairs payload hashes after semantic attacks and
  requires the checker to reject every attack.
- `c256_release_manifest.py` runs every gate and builds the self-excluded
  27-payload content-addressed release ledger.
