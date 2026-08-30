# C246 test report

Release contract: 28 physical files = 27 manifest-listed payload files plus
the self-excluded manifest.  Python bytecode and LaTeX sidecars are removed
before closure.

| Gate | Result |
|---|---|
| source/evaluator/epoch/scope lock | PASS |
| square-affine recurrence with (2a/\rho) | PASS (27 tuples) |
| independent checker | PASS (75 assertions) |
| SymPy cross-check | PASS (96 identities) |
| byte replay | PASS |
| hostile mutations | PASS (36/36) |
| two substantive revisions and three PDFs | PASS |
| fixed-epoch double LuaLaTeX builds, fonts, text and visual audit | PASS |
| manifest hash closure | PASS |

The receipt explicitly distinguishes stationary Markov-renewal/Palm occupation
from iid regeneration for positive beta and retains all Route-A failures.
