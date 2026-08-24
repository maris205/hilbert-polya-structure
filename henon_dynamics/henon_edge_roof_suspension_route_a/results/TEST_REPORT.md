# C135 test report

| Test | Result |
|---|---|
| exact producer | PASS |
| independent standard-library checker | PASS, 2,121 assertions |
| independent SymPy reconstruction | PASS, 37 checks |
| all period-one-to-ten trace dictionaries | PASS |
| requested period-six separation | PASS |
| remaining primitive collision and nonrotation | PASS |
| `N01=N10` conservation | PASS for every one of 2,046 replay words and proved generally |
| canonical byte replay | PASS |
| repaired-hash mutations | PASS, 42/42 registered cases rejected |
| stale-payload-hash mutation | PASS, 1/1 rejected |
| deterministic double PDF build | PASS, two isolated fixed-epoch builds byte-identical |
| embedded fonts and clean final logs | PASS |
| two-page visual inspection | PASS |
| release-manifest closure | PASS, 27/27 payload files |

The prefix is replay evidence only.  The checker imports no producer code and
closes all claim-bearing object schemas.
