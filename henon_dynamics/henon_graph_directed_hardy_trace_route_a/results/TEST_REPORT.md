# C124 test report

| Test | Result |
|---|---|
| exact producer | PASS |
| independent standard-library checker | PASS, 53 assertions |
| fresh SymPy reconstruction | PASS, 31 checks |
| explicit polynomial finite sections | PASS, maximum checked dimension 30 |
| canonical byte replay | PASS |
| hostile evidence mutations | PASS, 17/17 rejected |
| deterministic double PDF build | PASS, checked-in = isolated A = isolated B |
| embedded fonts and final-log scan | PASS, all embedded and no warnings |
| rendered-page inspection | PASS, both pages |
| release-manifest closure | PASS, 27/27 content files |

The replay prefix comprises 284 rooted words, 40 primitive cycles, eight power
traces, and Taylor coefficients through degree eight.  All arithmetic is exact.
