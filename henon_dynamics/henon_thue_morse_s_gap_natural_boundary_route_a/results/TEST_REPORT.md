# C159 test report

| gate | receipt |
|---|---|
| deterministic producer | PASS; 18 fixed rows and 49 formal cells |
| independent checker | PASS; 742 assertions |
| SymPy reconstruction | PASS; 118 checks through degree 24 |
| canonical replay | PASS; byte-identical evidence |
| hostile mutations | PASS; 45/45 repaired-hash plus 1/1 stale-hash rejected |
| theorem cutoff audit | PASS; finite rows labeled sentinels |
| scope firewall | PASS; no forbidden input or claim flag |

PDF determinism, fonts, warnings, and manifest closure are recorded in the
paper compile report and release manifest after final compilation.
