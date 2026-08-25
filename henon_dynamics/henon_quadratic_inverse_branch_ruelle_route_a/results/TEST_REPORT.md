# C141 test report

## Exact computation

| Test | Result |
|---|---:|
| Producer | PASS; 6 exact period rows |
| Independent full checker | PASS; 82 assertions |
| SymPy/algebra cross-check | PASS; 38 exact checks |
| Byte replay | PASS; byte-identical evidence |
| Mutation suite | PASS; 36 repaired-hash + 1 stale-hash rejection |
| Rooted/primitive receipt | PASS; 126 / 23 |

The producer uses a rational multiplication-matrix solve. The checker imports no producer code and instead uses polynomial extended Euclid. SymPy independently verifies all six quotient traces and controls; low periods additionally use resultant logarithmic derivatives.

## Commands

```bash
python3 code/c141_quadratic_ruelle_producer.py
python3 code/c141_quadratic_ruelle_checker.py
python3 code/c141_sympy_crosscheck.py
python3 code/c141_replay.py
python3 code/c141_mutation.py
```

PDF determinism, fonts, warning scan, text extraction, visual inspection, and manifest closure are recorded in `paper/COMPILE_REPORT.md` after final compilation.
