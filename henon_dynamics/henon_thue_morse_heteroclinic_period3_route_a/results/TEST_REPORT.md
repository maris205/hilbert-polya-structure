# C154 test report

| Test | Result |
|---|---:|
| independent symbolic checker | PASS, 549 assertions |
| separate SymPy reconstruction | PASS, 357 checks |
| isolated producer replay | PASS, byte-identical |
| repaired-hash mutations | PASS, 47/47 rejected |
| stale payload hash | PASS, 1/1 rejected |
| all-period / finite-cutoff boundary | PASS |
| dense-full-orbit / forward-transitivity boundary | PASS |
| scope and Route-B authorization | PASS, frozen / not authorized |

The checker reconstructs the interface windows, period-three phases,
Möbius ledger, and all-window Thue--Morse certificates without importing the
producer.  SymPy separately reconstructs the formal zeta series.
