# C153 test report

The exact producer, producer-independent checker, SymPy reconstruction, byte
replay, and hostile mutation suite pass on the frozen evidence.

| Test | Result |
|---|---|
| producer | PASS, 624 rank + 192 alpha + 20 period ledgers |
| independent checker | PASS, 6,193 assertions |
| SymPy reconstruction | PASS, 213 checks |
| direct tensor normal forms | PASS, all sources for `k<=4`, `0<=n<=2k` |
| direct literal matrix ranks | PASS, `k<=3`, `0<=n<=2k` |
| direct trace sentinels | PASS, `k<=5`, `n<=8` in checker; `k<=3`, `n<=10` in SymPy |
| byte replay | PASS |
| repaired-hash semantic mutations | PASS, 52/52 rejected |
| stale-payload-hash mutation | PASS, 1/1 rejected |
| fixed-epoch isolated double PDF build | PASS, both byte-identical to release PDF |
| font/log/text/visual checks | PASS, two pages inspected |
| release manifest closure | PASS, 27/27 payload files after manifest generation |

No external reviewer or model-independence claim is made.  “Independent” here
means independent implementation within the package, not an independent error
process.
