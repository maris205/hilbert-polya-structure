# C140 test report

| Test | Result |
|---|---|
| exact producer | PASS |
| independent standard-library checker | PASS, 2,028 assertions |
| independent SymPy reconstruction | PASS, 53 checks |
| cover trace versus intrinsic label enumeration, periods 1–15 | PASS |
| exceptional all-zero correction at every replay period | PASS |
| rational zeta and fifteen logarithmic coefficients | PASS |
| canonical byte replay | PASS |
| repaired-hash mutations | PASS, 53/53 rejected |
| stale-payload-hash mutation | PASS, 1/1 rejected |
| independent fixed-epoch double PDF build | PASS, both builds byte-identical to release PDF |
| embedded fonts and clean final logs | PASS |
| two-page visual inspection | PASS |
| release-manifest closure | PASS, 27/27 payload files after manifest generation |

The checker imports no producer module and never identifies cover path
multiplicity with intrinsic label-point multiplicity.  Infinite claims are
proved independently of the finite prefix.
