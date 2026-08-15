# Round-2 author repair record (not independent authority)

Date: 2026-08-14 UTC

This record documents the minimal author repair of the sole Round-2 blocker.
It is not an independent review, is not a `DEPLOYMENT_PASS`, and authorizes no
registered/P4 execution.

## Frozen bindings

- Source-lock v2 SHA-256:
  `205b6969b3c1b2ce7e448a4d8b43df59706d34e79db3bc70ca271d302fa499a1`.
- Round-2 reviewed-tree SHA-256, which received `DEPLOYMENT_FAIL`:
  `8716715b9449e2943bfbe1e0566c61d2271260cada2f23c6aa70c6b44d4e5b37`.
- Repaired tree SHA-256 requiring a fresh Round-3 review:
  `dd346942647bdd74f2c435d5396a720950d6bed246e88686d15f898e18afe3f4`.
- Complete historical V1/V2 review file SHA-256:
  `430e321596f665b9e4720683bede7de7dd844e97c1e3e39cabbcd45bee2e200c`.
- Safe JUnit SHA-256:
  `e2f318c9f4c14d640c16a3d889bd8417e5d1fd49c68f9a9adcec4e7aa96dc529`.
- Current safe preflight SHA-256:
  `fdb746a5790157c45e5cda6708ad145050ca3729146d3cc8d3c2783d46c7861a`.

## Minimal scanner repair

The scanner now rejects a forbidden callable or path I/O method when it is
stored as a value, rather than waiting for a later direct call.  This covers
tuple, list, set, dictionary and comprehension elements; direct, annotated and
named assignments; return/yield values; and higher-order call arguments.  The
existing alias fixed point remains in place.

The regression constructs a complete temporary copy of the exact closed-world
tree, replaces only the allowed `tests/test_algebra.py` path, and independently
checks all three Round-2 attacks:

1. named tuple containing `os.system`;
2. named dictionary containing built-in `open`;
3. named tuple containing a bound `Path.read_text` method for the forbidden
   resource name.

In each case the inventory itself passes, while executable isolation fails on
`forbidden_callable_storage`.  The legal exact type check
`type(value) is float` remains accepted, and the live reviewed tree has zero
scanner findings.

## Authority history and safe checks

The V1 and V2 failure authorities remain unchanged and are each required
exactly once.  A future deployment authority must use
`BASE2_CLOCK_CODE_REVIEW_V3`, `review_round=3`, the repaired tree hash, the
frozen source-lock hash, an independent reviewer flag, and verdict
`DEPLOYMENT_PASS`.

- Python AST parse/compile: 23 files passed.
- Safe tests: 36 passed, 0 failed, 0 errors, 0 skipped.
- Closed-world scanner: passed with 0 findings.
- Safe wrapper from the project root: passed and generated no bytecode.
- Current gate: `READY_FOR_INDEPENDENT_PRE_EXECUTION_REVIEW`; V3 authority is
  intentionally absent.
- Registered candidate runs: 0; registered periods executed: none.
- P4, prime-table data, Riemann-zero data, floating orbit matching, and network
  access were not invoked.

A fresh independent Round-3 review is required before any registered execution.
