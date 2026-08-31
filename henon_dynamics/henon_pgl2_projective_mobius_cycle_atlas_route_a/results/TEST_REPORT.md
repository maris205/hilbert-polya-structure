# Test report

| gate | result |
|---|---|
| producer exhaustive enumeration | PASS |
| independent direct-permutation checker | PASS — 6,159,318 assertions |
| symbolic/algebraic cross-check | PASS — 193 identities |
| byte-for-byte replay | PASS |
| repaired-hash semantic mutation | PASS — 40/40 rejected |
| odd/even characteristic faces | PASS |
| prime and extension fields | PASS |
| split/nonsplit involution boundary | PASS |
| arbitrary-`q` proof separated from finite evidence | PASS |

All commands run with bytecode disabled. The release gate reruns every executable before hashing the final ledger.
