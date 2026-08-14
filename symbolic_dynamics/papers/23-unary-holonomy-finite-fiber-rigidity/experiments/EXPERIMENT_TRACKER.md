# Experiment Tracker — SD-C25

| ID | Status | Deterministic output |
|---|---|---|
| E1 | PASS | 4,095 cycles and 8,390,655 exact edges; zero source-policy mismatch |
| E2 | PASS | 288 unary maps, 1,054,474 configurations, 8,067,400 comparisons; zero mismatch |
| E3 | PASS | 11 constructive composite witnesses |
| E4 | PASS | 48 matrix cases and 2,832 exact residuals; all zero |
| E5 | PASS | 56 oracle-containing memorizer controls; all exact |
| E6 | PASS | 16 canonical rows, 128 power traces, 12 determinant checks; (1-w^2) firewall exact |
| E7 | PASS | 144 directed-rounding rows; all intervals ordered |
| E8 | PASS | two imported certificates, 5 transient and 40 recurrent control rows |
| E9 | PASS | 4,095 exact roof/marker rows; first mismatch at (k=2) |
| E10 | PASS | 32/32 tests, byte-identical double run, integrity and SHA verification |

No GPU, stochastic fit, target-zero search, review loop, or Route-B run was
used.

