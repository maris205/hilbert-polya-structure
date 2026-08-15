# Round-3 author repair record (not independent authority)

Date: 2026-08-14 UTC

This record documents the minimal author repair of the sole Round-3 scanner
blocker.  It is not an independent review, is not a `DEPLOYMENT_PASS`, and
authorizes no registered/P4 execution.

## Frozen bindings

- Source-lock v2 SHA-256:
  `205b6969b3c1b2ce7e448a4d8b43df59706d34e79db3bc70ca271d302fa499a1`.
- Round-3 reviewed-tree SHA-256, which received `DEPLOYMENT_FAIL`:
  `dd346942647bdd74f2c435d5396a720950d6bed246e88686d15f898e18afe3f4`.
- Repaired tree SHA-256 requiring fresh Round-4 review:
  `7a5ea42ea52d35bf4d6608b1175a43ab81ceaa9ed8fbfd0e35e183920dbdd27a`.
- Complete historical V1/V2/V3 review file SHA-256:
  `806fe981fc0c626d6e1c49b43dcf1a4b5d1cf611e097c4ca1f6f1b75cbcee902`.
- Safe JUnit SHA-256:
  `0ae6e50d240b7d2663447ae6897b6807d8cee9a073e7be88febc2c48225beeb6`.
- Current safe preflight SHA-256:
  `4ec2cf534415043ecb047674cef78e88bf77f20d434d734d642c7ad3906d337e`.

## Minimal capability-flow repair

One recursive forbidden-capability value analysis now covers conditional
expression branches, lambda implicit returns and defaults, Boolean value
producers, literal containers, starred/named expressions, direct and annotated
assignments, explicit returns/yields, function and keyword-only defaults, and
higher-order call arguments.  It does not descend into exact type-comparison
expressions, so `type(value) is float` remains a permitted type predicate.

The regression suite installs each Round-3 source separately as the exact
allowed `tests/test_algebra.py` in a complete temporary closed-world tree:

1. `os.system if True else len` assigned and called;
2. a lambda implicitly returning `os.system`;
3. a function whose default argument captures `os.system`.

All three retain a passing closed-world inventory but fail executable isolation
with `forbidden_callable_storage`.  A fourth complete-tree positive fixture
containing `return type(value) is float` passes with zero findings.

## Authority history and safe checks

The V1, V2 and V3 failure authorities remain unchanged and are each required
exactly once.  Any future deployment authority must use
`BASE2_CLOCK_CODE_REVIEW_V4`, `review_round=4`, the repaired tree hash, the
frozen source-lock hash, an independent reviewer flag, and verdict
`DEPLOYMENT_PASS`.

- Python AST parse/compile: 23 files passed.
- Safe tests: 38 passed, 0 failed, 0 errors, 0 skipped.
- Closed-world scanner: passed with 0 findings.
- Safe wrapper from the project root: passed and generated no bytecode.
- Current gate: `READY_FOR_INDEPENDENT_PRE_EXECUTION_REVIEW`; V4 authority is
  intentionally absent.
- Registered candidate runs: 0; registered periods executed: none.
- P4, prime-table data, Riemann-zero data, floating orbit matching, and network
  access were not invoked.

A fresh independent Round-4 review is required before any registered execution.
