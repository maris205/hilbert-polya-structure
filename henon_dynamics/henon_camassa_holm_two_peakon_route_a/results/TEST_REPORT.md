# C278 test report

| surface | result |
|---|---|
| deterministic producer | PASS |
| producer-independent reconstruction | PASS, 551 assertions |
| SymPy conservation/reduction/asymptotic identities | PASS, 10 identities |
| fresh-directory byte replay | PASS |
| repaired-hash hostile mutations | PASS, 41/41 |
| stale-hash control | PASS |
| scope and Route-A locks | PASS |

The checker imports no producer module.  It reconstructs both explicit
branches from `P,D,t`, recalculates `p_1,p_2,E`, verifies the same-sign centre
and positions, checks all three stored collision scalings and all four
boundary records, and locks the exact top-level and nested schemas, model,
complete proof/theorem/nonclaim contracts, scope map, and reference metadata.
The CH1993 reference lock includes the exact full venue string `Physical
Review Letters 71(11) (1993), 1661-1664`; a repaired-hash venue mutation is
explicitly required to fail.
