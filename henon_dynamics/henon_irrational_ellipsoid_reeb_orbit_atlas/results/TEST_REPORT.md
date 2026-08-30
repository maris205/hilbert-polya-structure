# C242 test report

Commands (all with `PYTHONDONTWRITEBYTECODE=1 python3 -B`):

| gate | result |
|---|---|
| deterministic producer | `C242_PRODUCER_PASS`, 48 irrational rows, 3 rational cases |
| independent checker | `PASS` (2089 assertions) |
| SymPy/integer-square crosscheck | `C242_SYMPY_PASS` (59 checks) |
| byte replay | `C242_REPLAY_PASS` |
| repaired-hash mutation | `PASS 29/29` |
| PDF/manifest audit | recorded by `c242_release_manifest.py` |

The checker reconstructs the formulas independently and rejects changed
source/evaluator locks, altered floors or multipliers, rational non-Morse--Bott
claims, route changes, and scope-flag changes.
