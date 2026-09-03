# C327 executable lanes

- `c327_kronig_penney_producer.py` writes deterministic canonical evidence.
- `c327_kronig_penney_checker.py` is producer-independent and owns the strict
  JSON/YAML schemas, hashes, every nested row, and every numerical formula.
- `c327_kronig_penney_sympy_crosscheck.py` reconstructs the exact algebra.
- `c327_kronig_penney_replay.py` compares two isolated fresh outputs with the
  checked-in evidence bytes.
- `c327_kronig_penney_mutation.py` submits repaired-hash semantic attacks and
  strict-parser/evaluator attacks to the independent checker.
- `c327_release_manifest.py` runs every lane, optimized-mode refusal, six
  fresh paper builds, PDF checks, and the exact release ledger.

No checker imports the producer.  All commands use the frozen source commit,
epoch, evaluator authority/version/hash, scope literal, and Route-A result.
