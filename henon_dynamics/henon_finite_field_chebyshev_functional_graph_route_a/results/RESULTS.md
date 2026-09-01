# Exact results

The frozen evidence SHA-256 is `e6a19af6b27e300f3ce2c9b20c6ff0eb6d93678c504c991cf427bc483e5aa3c3`; its internal canonical payload hash is `e787db19f3646c68557f92fa0bfbc16cbf8466bd940fd6034a5cda40c32a4c37`.

| item | exact count |
|---|---:|
| field models | 11 |
| degree values `0,...,10` | 11 |
| maps | 121 |
| directly followed case-vertices | 1,914 |
| nonprime-field cases | 77 |
| characteristic-two cases | 33 |
| fixed-count cells | 535 |
| nonzero cycle-factor cells | 203 |
| tail-layer cells | 250 |
| image-rank cells | 371 |
| nonzero zero-Jordan cells | 121 |

The independent checker passes 32,499 assertions, including monicity, exact degree, irreducibility and fixed-`q` model consistency.  SymPy passes 311 exact matrix/rank checks across 64 maps.  Fresh evidence replay is byte-identical, and all 41 repaired-hash hostile mutations are rejected.

The samples include ramification merging in characteristic two, both odd-characteristic branches, identity maps, constant maps, permutation degrees, one-sided singular cover factors and simultaneous singularity on both covers.  They validate the executable formulas but do not replace the all-prime-power proof.
