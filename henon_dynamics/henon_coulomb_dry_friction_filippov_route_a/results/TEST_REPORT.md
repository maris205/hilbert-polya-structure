# C238 test report

Release contract: 28 physical files = 27 manifest-listed payload files plus
the self-excluded `C238_RELEASE_MANIFEST.json`.  Python bytecode and LaTeX
sidecars are removed before closure.

| Gate | Result |
|---|---|
| source/evaluator/scope lock | PASS |
| maximal-monotone selection and energy law | PASS |
| rest map and finite capture count | PASS |
| signed first-turn phase ledger | PASS |
| harmonic `c=0` boundary | PASS |
| producer-independent checker | PASS (see manifest) |
| SymPy cross-check | PASS (see manifest) |
| byte replay | PASS |
| hostile mutations | PASS (28/28) |
| three content-distinct paper revisions | PASS |
| two fresh fixed-epoch LuaLaTeX builds per revision | PASS |
| fonts/layout/reference audit | PASS |
| manifest hash closure | PASS |

No target arithmetic, Euler factors, root numbers, automorphy, target
functional equation, or Hilbert–Pólya operator is claimed.
