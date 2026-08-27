# Test report

All tests were run with Python 3 exact rational arithmetic from the package
root.

| Command | Result |
|---|---|
| `python3 code/c192_hyperplane_producer.py` | PASS; 8 cases, 316 faces, 94 chambers, 75 flats |
| `python3 code/c192_hyperplane_checker.py` | PASS; 20,609 assertions |
| `python3 code/c192_sympy_crosscheck.py` | PASS; 3,398 checks |
| `python3 code/c192_replay.py` | PASS; 116,204 bytes reproduced exactly |
| `python3 code/c192_mutation.py` | PASS; 74 repaired-hash plus 1 stale-hash rejection |

The checker imports no producer module.  It uses subset dynamic programming for
the weighted-order law, whereas the producer enumerates weighted permutations.
It also reconstructs the support lattice and Möbius function from serialized
zero sets before recomputing every transition cell and probability bound.

The SymPy oracle independently computes exact matrix characteristic
polynomials, `det(I-zK)`, power traces, and eigenspace dimensions.  No floating
point tolerance is used.

Publication checks and manifest closure are recorded in `paper/COMPILE_REPORT.md`
and `C192_RELEASE_MANIFEST.json`.
