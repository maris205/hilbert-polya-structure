# C120 exact-computation programs

- `c120_variational_period3_producer.py` writes the canonical evidence JSON.
- `c120_variational_period3_checker.py` independently recomputes every released mathematical field and never imports the producer.
- `c120_sympy_crosscheck.py` checks the structural, orbit, monodromy, action, and Hessian identities directly.
- `c120_replay.py` requires byte-identical evidence regeneration.
- `c120_mutation.py` requires all 21 hostile receipt mutations to be rejected,
  including attacks on the evaluator-native A1--A4 boundary.
- `c120_release_manifest.py` hashes the closed package after the PDF exists.

All computations are deterministic and use exact rational or symbolic algebra; no floating-point or random path is used.
