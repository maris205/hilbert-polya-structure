# C262 test report

Run from the package root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c262_hill_producer.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c262_hill_checker.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c262_hill_sympy_crosscheck.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c262_hill_replay.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c262_hill_mutation.py
```

| gate | result |
|---|---|
| producer | PASS; 900 grid + 6 boundary rows |
| independent checker | PASS; 19,849 assertions |
| SymPy | PASS; 289 exact identities |
| clean replay | byte-identical PASS |
| hostile mutations | 41/41 rejected |
| three paper rounds | distinct 2-page hashes; duplicate fresh builds byte-identical |
| fonts/log/visual | 21 embedded/subset font entries; clean log and two-page visual PASS |

The checker imports no producer function and reconstructs segment transfers
with an independent entire-series implementation.
