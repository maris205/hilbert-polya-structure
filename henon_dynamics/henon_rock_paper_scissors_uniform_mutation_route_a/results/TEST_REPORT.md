# C235 test report

Release contract: 28 physical files = 27 manifest-listed payload files plus
the self-excluded `C235_RELEASE_MANIFEST.json`.  Build sidecars and Python
bytecode are excluded before closure.

| Gate | Result |
|---|---|
| source/evaluator/scope lock | PASS |
| simplex, product and period ledger | PASS |
| uniform-mutation Lyapunov/LaSalle face | PASS |
| producer-independent checker | PASS (see manifest) |
| SymPy cross-check | PASS (see manifest) |
| byte replay | PASS |
| hostile mutations | PASS (25/25) |
| three content-distinct paper revisions | PASS |
| two fresh fixed-epoch LuaLaTeX builds per revision | PASS |
| fonts/layout/reference audit | PASS |
| manifest hash closure | PASS |

No target arithmetic, Euler factors, root numbers, automorphy, target
functional equation, or Hilbert–Pólya operator is claimed.
