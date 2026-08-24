# C134 test report

| Test | Result |
|---|---|
| exact producer | PASS |
| independent standard-library checker | PASS, 71 assertions |
| independent SymPy reconstruction | PASS, 64 checks |
| twelve scaled permutation recoveries | PASS |
| complete `k=1`/`k=6` mod-five alias | PASS |
| faithful Laurent/`q` separation | PASS |
| canonical byte replay | PASS |
| repaired-hash mutations | PASS, 47/47 registered cases rejected |
| stale-payload-hash mutation | PASS, 1/1 rejected |
| deterministic double PDF build | PASS, two isolated fixed-epoch builds byte-identical |
| embedded fonts and clean final logs | PASS |
| two-page visual inspection | PASS |
| release-manifest closure | PASS, 27/27 payload files |

The finite prefix is replay evidence, not a theorem cutoff.  The checker fixes
all claim-bearing object schemas and does not import producer code.  Its exact
source-lock assertions include clock, normalization, determinant convention,
precision, and cutoff; its recovery assertions include all three Newton
identities.
