# C243 test report

All commands were run with `PYTHONDONTWRITEBYTECODE=1 python3 -B`.

| gate | result |
|---|---|
| deterministic producer | `C243_PRODUCER_PASS` (14 fixed, 13 levels) |
| independent checker | `PASS` (995 assertions) |
| SymPy and quadrature crosscheck | `C243_SYMPY_PASS` (13 identities, 3 quadratures) |
| byte replay | `C243_REPLAY_PASS` |
| repaired-hash mutation | `PASS 28/28` |
| PDF/manifest audit | recorded by `c243_release_manifest.py` |

The checker rejects changed signs, linearization bases, roots, elliptic
periods, separatrix component counts, pole warnings, boundary criteria,
source/evaluator locks, route flags, and scope flags.
