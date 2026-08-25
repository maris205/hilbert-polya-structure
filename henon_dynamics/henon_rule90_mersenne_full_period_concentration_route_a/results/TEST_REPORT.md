# C155 test report

| Test | Result |
|---|---:|
| independent binary-matrix checker | PASS, 2,291 assertions |
| separate SymPy quotient-ring path | PASS, 2,255 checks |
| isolated producer replay | PASS, byte-identical |
| repaired-hash mutations | PASS, 53/53 rejected |
| stale payload hash | PASS, 1/1 rejected |
| all-`r` / finite-ledger boundary | PASS |
| probability and cycle-average normalizations | PASS |
| scope and Route-B authorization | PASS, frozen / not authorized |

The checker reconstructs divisor fixed spaces with binary matrices and checks
proper-time dependence independently for all rings through `L=63`; SymPy
reconstructs all 494 proper-time cells through `L=255`.
