# C215 test report

| command | result |
|---|---|
| `c215_kingman_producer.py` | PASS; 312/12/48/60 transition/holding/MRCA/branch rows |
| `c215_kingman_checker.py` | PASS; 3408 assertions; producer not imported |
| `c215_kingman_sympy_crosscheck.py` | PASS; 379 symbolic/row checks |
| `c215_kingman_replay.py` | PASS; canonical bytes reproduced |
| `c215_kingman_mutation.py` | PASS; 26 repaired + 1 stale rejection |
| LuaLaTeX fixed-epoch double build | PASS; no undefined refs/overfull boxes |
| PDF text/font/page audit | PASS; 2 pages, all fonts embedded |

The finite rows are regression evidence only.  The projective coupling and
all-`n` theorem are stated separately from marginal numerical calculations.
