# C237 test report

All commands were run from the package directory with
`PYTHONDONTWRITEBYTECODE=1 python3 -B`.

| check | result |
|---|---|
| producer | `C237_PRODUCER_PASS`, 40 rows, payload hash recorded in manifest |
| producer-independent checker | PASS, 411 assertions |
| SymPy cross-check | PASS, 26 symbolic identities |
| clean byte replay | PASS, 34,870 bytes |
| hostile mutations | PASS, 32/32 rejected (all five boundary rows semantically locked) |
| fixed-epoch LuaLaTeX | two passes for rounds 0, 1 and 2 |
| PDF/layout/fonts | 2 pages, embedded subset fonts, no final-pass layout/reference warnings |

The checker tests all serialized matrix, transition, correlation, rate,
Kalman, Gibbs and boundary cells, including the critical Jordan prefactor and
the \(\omega=0\) no-stationary-position face.
