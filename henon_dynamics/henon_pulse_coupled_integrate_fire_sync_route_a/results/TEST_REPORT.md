# C245 test report

Release contract: 28 physical files = 27 manifest-listed payload files plus
the self-excluded manifest.  Python bytecode and LaTeX sidecars are removed
before closure.

| Gate | Result |
|---|---|
| source/evaluator/epoch/scope lock | PASS |
| exact rational event and avalanche producer | PASS (441 rows) |
| independent checker | PASS (4,438 assertions) |
| SymPy cross-check | PASS (330 identities) |
| byte replay | PASS |
| hostile mutations | PASS (41/41) |
| two substantive revisions and three PDFs | PASS |
| fixed-epoch double LuaLaTeX builds, fonts, text and visual audit | PASS |
| manifest hash closure | PASS |

The receipt and paper explicitly retain `A0_FAIL`, `A2_FAIL`, `A3_FAIL`, and
`ROUTE_A_REJECTED`; no arithmetic or target spectral claim is made.
