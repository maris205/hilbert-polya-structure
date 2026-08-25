# C149 test report

| Test | Result |
|---|---:|
| independent finite-map checker | PASS, 395 assertions |
| separate SymPy reconstruction | PASS, 277 checks |
| isolated producer replay | PASS, byte-identical |
| repaired-hash mutations | PASS, 41/41 rejected |
| stale payload hash | PASS, 1/1 rejected |
| all-period / finite-cutoff boundary | PASS |
| scope and Route-B authorization | PASS, frozen / not authorized |

The checker builds and iterates the 11-point successor permutation rather than
calling the producer formula.  SymPy reconstructs the rational series and
formal logarithm through the declared finite degree.
