# SD-C19 Experiment Tracker

| Run | Purpose | Frozen scale | Exact result | Status |
|---|---|---|---|---|
| R001 | sanity | two-atom formal/lift/transition | `3/3` pass | DONE |
| R002 | formal `C2` | `n=1..10` | zero mismatch in all four determinant comparisons | DONE |
| R003 | trace repetitions | 300 coefficients | `300/300` exact | DONE |
| R004 | `C_m` characters | 350 rows | `350/350` exact | DONE |
| R005 | regular local determinant | `m=2..8` | `7/7` exact | DONE |
| R006 | fiber dynamics | `n=1..10` | 10 transitive; 9 mixing; one period two | DONE |
| R007 | primitive/lift census | 350 rows | all pilot counts reproduced; mixed lifts remain | DONE |
| R008 | naturality rigidity | 72,079 tables / 35 cells | one power rule per cell | DONE |
| R009 | coboundary controls | 63 gauge + 21 negative | `63/63` trivial; `21/21` witnessed | DONE |
| R010 | transition boundary | four exact controls | one gauge factor; three leaks | DONE |
| R011 | inventory controls | 64 rows / 16 seeds | `64/64`; identity pass-rate margin zero | DONE |
| R012 | full tests | 14 | `14/14` pass | DONE |
| R013 | artifact integrity | JSON/CSV/cache/prototype diff | parse, LF, cache, diff clean | DONE |
| R014 | deterministic freeze | two complete runs | identical result-ledger SHA | DONE |
