# C144 test report

| Test | Result |
|---|---:|
| independent checker | PASS, 172,437 assertions |
| SymPy cross-check | PASS, 83 exact checks |
| isolated producer replay | PASS, byte-identical |
| repaired-hash mutations | PASS, 36/36 rejected |
| stale-hash mutation | PASS, 1/1 rejected |
| theorem cutoff audit | PASS, finite ledgers labeled sentinels |
| Route-B and scope flags | PASS, false / frozen literal |

The checker reconstructs the fixed point by substitution rather than importing
producer functions.  It audits 172,437 conditions, including recurrence cells,
dyadic block identities, full approximant windows, certificate arithmetic, and
scope structure.  SymPy independently verifies the signed substitution
polynomial product and formal zeta coefficients.
