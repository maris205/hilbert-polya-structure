# C261 test report

All release gates run from the package root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c261_airy_producer.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c261_airy_checker.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c261_airy_sympy_crosscheck.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c261_airy_replay.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c261_airy_mutation.py
```

| gate | result |
|---|---|
| producer | PASS; 2,806 modular, 101 DFT, 10 support rows |
| independent checker | PASS; 50,765 assertions |
| SymPy/modular reconstruction | PASS; 301,200 identities |
| clean-process replay | byte-identical PASS |
| hostile mutations | 41/41 rejected |
| paper rounds | three distinct 2-page PDFs; duplicate fresh builds byte-identical |
| final fonts/log/visual | 23 embedded/subset font entries; clean log and two-page visual PASS |

The checker imports neither producer functions nor producer data structures.
Its DFT and valuation reconstruction is independent of the stored hashes.
