# C139 test report

| Test | Result |
|---|---|
| exact producer | PASS |
| independent standard-library checker | PASS, 16,467 assertions |
| independent SymPy reconstruction | PASS, 35 checks |
| all period-1-to-12 state traces versus word enumeration | PASS |
| exact determinant and `y=1` control | PASS |
| memory-3 witness and width-4 separation | PASS |
| residual primitive nonrotation collision | PASS |
| canonical byte replay | PASS |
| repaired-hash mutations | PASS, 48/48 rejected |
| stale-payload-hash mutation | PASS, 1/1 rejected |
| independent fixed-epoch double PDF build | PASS, both builds byte-identical to release PDF |
| embedded fonts and clean final logs | PASS |
| two-page visual inspection | PASS |
| release-manifest closure | PASS, 27/27 payload files after manifest generation |

The checker imports no producer module.  Infinite identities are proved in
`THEOREM_PACKAGE.md`; the finite replay is only a sentinel.
