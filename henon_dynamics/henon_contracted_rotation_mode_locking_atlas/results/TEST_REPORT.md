# C240 test report

Release contract: 28 physical files = 27 manifest-listed payload files plus
the self-excluded manifest.  Python bytecode and LaTeX sidecars are removed
before closure.

| Gate | Result |
|---|---|
| source/evaluator/epoch/scope lock | PASS |
| Fraction word generation and primitive/cyclic filters | PASS (747 per slope) |
| affine fixed points and half-open interval solver | PASS (2241 rows; 138 nonempty) |
| endpoint equality audit and direct iteration | PASS (295 probes) |
| producer-independent checker | PASS (6763 assertions) |
| SymPy cross-check | PASS (119 identities) |
| byte replay | PASS |
| hostile mutations | PASS (33/33) |
| three content-distinct paper revisions | PASS |
| two fresh fixed-epoch LuaLaTeX builds per revision | PASS |
| fonts/layout/reference audit | PASS |
| manifest hash closure | PASS |

The receipt and paper explicitly record `A0_FAIL`, `A2_FAIL`, `A3_FAIL`, and
`ROUTE_A_REJECTED`; no target arithmetic or quantum claim is made.
