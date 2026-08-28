# C214 test report

| command | result |
|---|---|
| `c214_brownian_producer.py` | PASS; 81/27/9/108/27 rows |
| `c214_brownian_checker.py` | PASS; 2352 assertions; producer not imported |
| `c214_brownian_sympy_crosscheck.py` | PASS; 122 symbolic/row checks |
| `c214_brownian_replay.py` | PASS; canonical bytes reproduced |
| `c214_brownian_mutation.py` | PASS; 26 repaired + 1 stale rejection |
| LuaLaTeX fixed-epoch double build | PASS; no undefined refs/overfull boxes |
| PDF text/font/page audit | PASS; 3 pages, all fonts embedded |

The rows are regression evidence only; the all-parameter identities are
stated with their analytic proof boundary.
