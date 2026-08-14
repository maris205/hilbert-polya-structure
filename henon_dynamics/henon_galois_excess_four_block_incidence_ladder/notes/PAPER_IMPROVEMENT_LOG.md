# Paper improvement log

## Round 1

- Replaced an unsupported irreducibility sentence by an exact modulo-13
  certificate and implemented the same test in the primary and independent
  computation paths.
- Added the reduced polynomial and gcd-degree fields to the JSON
  certificates and unit tests.
- Renamed the period-one finite-sharpness row from `A1` to `C1`, avoiding a
  collision with the family `A_m`, which begins at `m=3`.
- Repaired the `Counter` typography in the reproducibility section.
- Mirrored the finite-memory/Hölder distinction in the abstract, README,
  proof package, evaluator files and executable claim firewall.

## Round 2

- Recomputed every all-width insertion row independently through width 64.
- Rechecked the radical period-six orbit, both trace embeddings, the
  reciprocal multiplier field, the exact logarithmic chain and the
  determinant-one width-five minor.
- Confirmed that the paper claims only a one-sided Hölder necessary
  condition and keeps the unrestricted/two-sided question open.
- Recompiled deterministically, checked references, fonts and extracted
  text, and visually inspected representative pages.

The second hostile review found no unresolved correction.
