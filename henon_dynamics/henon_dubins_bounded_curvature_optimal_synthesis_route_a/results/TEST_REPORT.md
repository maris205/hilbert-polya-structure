# C310 test report

| lane | retained result |
|---|---|
| producer | 30 poses / 180 cells / 1,978 leaves |
| independent checker | 2,087 checks, PASS |
| SymPy | 21 identity groups, PASS |
| isolated replay | byte-identical, PASS |
| hostile mutation | 30/30 rejected |
| release | exact manifest and deterministic PDF rounds |

The checker independently evaluates all six formulas, feasibility tests,
canonical boundary conventions, every segment, terminal pose, Euclidean
lower bound, all ties, word coverage, Route-A tuple, and scope flags.
