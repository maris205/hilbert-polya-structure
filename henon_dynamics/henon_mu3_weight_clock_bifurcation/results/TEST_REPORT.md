# HCS-C51 release-candidate test report

- Independent semantic/checker gates: `15/15 PASS`.
- Targeted mutation and rollback tests: `43/43 PASS`.
- Mutations include source-lock, exact rational/type, Chern/rank, clock
  indexing, center spectrum, Tate/half-weight, coefficient exponent,
  compatible-system rank, restriction-of-scalars scope, cleared skeleton,
  Gamma/Hodge, unknown-key, missing-container, and overclaim attacks.
- Result refresh occurs only after producer, checker, mutation tests, and a
  staged manifest all succeed. The three live artifacts are then promoted
  with rollback; injected failures after move two and move three leave all
  previous targets byte-identical. A successful promotion is followed by a
  live checker/cmp/manifest replay.
- Manifest scope is the complete release project, including root documents,
  both Route-A copies, paper sources/PDF/reports, code, and results.
- `code/run_c51.sh` is executable (`0755`), and the final default replay was
  invoked directly as `./code/run_c51.sh`.

Reproduce with `./code/run_c51.sh` from the project directory.
