# C145 test report

| Test | Result |
|---|---:|
| independent binary-matrix checker | PASS, 6,520 assertions |
| SymPy polynomial-gcd path | PASS, 1,177 exact checks |
| isolated producer replay | PASS, byte-identical |
| repaired-hash mutations | PASS, 42/42 rejected |
| stale-hash mutation | PASS, 1/1 rejected |
| exact-period divisibility | PASS, all 576 cells |
| non-squarefree even-length sentinel | PASS, `L=6,n=2` |
| scope and Route-B flags | PASS |

The checker independently exponentiates Rule-90 binary matrices, computes
kernel ranks, performs Möbius inversion, and directly enumerates selected
state spaces.  SymPy reconstructs every gcd without importing producer code.
