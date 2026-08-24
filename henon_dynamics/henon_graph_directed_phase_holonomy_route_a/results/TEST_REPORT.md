# C129 test report

| Test | Result |
|---|---|
| exact producer | PASS |
| independent standard-library checker | PASS, 71 assertions |
| independent SymPy reconstruction | PASS, 49 checks |
| explicit polynomial finite sections | PASS, maximum dimension 30 |
| canonical byte replay | PASS |
| repaired-hash hostile mutations | PASS, 35/35 registered cases rejected |
| deterministic double PDF build | PASS, checked-in = isolated A = isolated B |
| embedded fonts and final-log scan | PASS, all embedded and no warnings |
| rendered-page inspection | PASS, both pages |
| release-manifest closure | PASS, 27/27 payload files |

The checker imports no producer code and closes the key schemas of every
claim-bearing top-level object.  The exact prefix contains 284 rooted words,
40 primitive cycles, eight power
traces, and Fredholm coefficients through degree eight. The theorem statements
have no period cutoff.
