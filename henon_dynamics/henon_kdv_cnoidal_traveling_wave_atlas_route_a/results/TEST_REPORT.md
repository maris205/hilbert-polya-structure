# C256 test report

All release gates pass from the package root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c256_kdv_producer.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c256_kdv_checker.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c256_kdv_sympy_crosscheck.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c256_kdv_replay.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c256_kdv_mutation.py
```

| gate | result |
|---|---|
| producer | `C256_PRODUCER_PASS`; 12 periodic and 12 boundary rows |
| independent checker | PASS; 602 assertions |
| SymPy reconstruction | PASS; 245 identities |
| clean-process replay | byte-identical PASS |
| hostile mutations | 49/49 rejected |
| three paper rounds | hashes distinct; 2, 2, and 3 pages |
| duplicate fresh builds | byte-identical for every round |
| final fonts | 21 embedded/subset entries |
| final second-pass log | no layout, reference, citation, or package warning |
| visual/text inspection | all three pages PASS |

The checker imports neither producer functions nor producer data structures.
Its period/moment path integrates the cubic-root quadrature after an endpoint
regularization; the displayed `K/E` formulas are then compared independently.
