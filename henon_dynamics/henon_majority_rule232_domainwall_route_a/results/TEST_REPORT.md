# Test report

Environment: CPython 3, `python3 -B`, `PYTHONDONTWRITEBYTECODE=1`, fixed
source commit `3ff451e904f8f063e88c40ef87f4697a6586b1a5`.

| command | outcome |
|---|---|
| `c251_majority_producer.py` | PASS; deterministic JSON payload |
| `c251_majority_checker.py` | PASS; 1,855 independent assertions |
| `c251_majority_sympy_crosscheck.py` | PASS; 569 symbolic identities |
| `c251_majority_replay.py` | PASS; byte-identical clean replay |
| `c251_majority_mutation.py` | PASS; 40/40 hostile mutations rejected |

The checker rebuilds every state for (n\le14), factors the four-state graph
independently, and verifies all (216) run-matrix receipts.  The mutation
suite covers provenance, frozen-map semantics, transfer entries, direct
trajectories, route flags, scope flags, unknown keys, and stale payload hashes.
