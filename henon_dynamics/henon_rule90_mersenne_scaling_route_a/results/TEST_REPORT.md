# C150 test report

| Test | Result |
|---|---:|
| independent binary-matrix checker | PASS, 153 assertions |
| separate SymPy quotient reconstruction | PASS, 276 checks |
| isolated producer replay | PASS, byte-identical |
| repaired-hash mutations | PASS, 44/44 rejected |
| stale payload hash | PASS, 1/1 rejected |
| all-`r` / finite-cutoff boundary | PASS |
| scope and Route-B authorization | PASS, frozen / not authorized |

The checker verifies matrix rank, `F^(L+1)=F`, fixed kernels, Möbius counts,
small-state brute partitions, and power-of-two nilpotency without importing
producer functions.
