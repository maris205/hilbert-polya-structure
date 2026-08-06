# R401-VAL-L2-S0 representative local complement

Producer status: **PASS_S0_PRODUCER**.

The validated tree was run on the beginning, middle, and endpoint L1
parameter slabs at 128 and 256 MPFR bits.

| Bits | Slab | Evaluated nodes | Energy excluded | Return excluded | Unresolved | Complete |
|---:|:---:|---:|---:|---:|---:|:---:|
| 128 | S000 | 486 | 18 | 229 | 0 | PASS |
| 128 | S025 | 546 | 31 | 246 | 0 | PASS |
| 128 | S050 | 574 | 44 | 247 | 0 | PASS |
| 256 | S000 | 436 | 18 | 204 | 0 | PASS |
| 256 | S025 | 488 | 31 | 217 | 0 | PASS |
| 256 | S050 | 486 | 41 | 206 | 0 | PASS |

A pass licenses only the complement-engine implementation on these
three representative slabs.  The other 48 slabs, the local phase-cover
tree, the global shell cover, the final determinant cross-check, and all
arithmetic/Hilbert--Polya claims remain open.
