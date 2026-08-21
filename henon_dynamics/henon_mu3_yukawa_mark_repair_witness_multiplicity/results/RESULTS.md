# C79 results

The canonical receipt has SHA-256
`147a9b77e0ee7459040a7cc3c026bb21bce950a806e4fbc3ce0441dc9bb6c879`.

| `(rho,W)` | count |
|---|---:|
| `(0,1)` | 30400 |
| `(1,1)` | 30400 |
| `(1,4)` | 1984 |
| `(1,7)` | 192 |
| `(1,8)` | 128 |
| `(2,4)` | 1984 |
| `(2,7)` | 192 |
| `(2,8)` | 128 |
| `(2,25)` | 64 |
| `(3,25)` | 64 |

The witness marginal is `60800 v + 3968 v^4 + 384 v^7 + 256 v^8 +
128 v^25`; setting `v=1` recovers the C78 distance distribution.

The direct checker, symbolic expansion, replay, and hostile mutation audit all
pass.  Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.
