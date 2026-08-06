# Exact result artifacts

All producer artifacts are deterministic and target-blind.

- `certificate.json`: authoritative mathematical and computational ledger;
- `periodic_counts.csv`: (N_n^{(2)}), torus controls, corrections, Lucas
  counts, exact-period points, primitive orbits, and zeta coefficients through
  period (20);
- `valuation_distribution.csv`: exact word count and mass at each
  (2)-adic valuation;
- `congruence_tower.csv`: finite-monoid recurrence versus direct enumeration
  for levels (2^1,\ldots,2^8);
- `chronology_witnesses.json`: the rational/natural-boundary period-five pair
  and repetition valuation checks;
- `recurrence_screen.json`: finite-prefix Berlekamp--Massey screens over three
  primes; these are evidence only, not nonrationality theorems;
- `independent_check.json`: a separate nested-matrix implementation and
  characteristic-polynomial repetition audit;
- `ARTIFACT_HASHES.sha256`: final immutable checksums.

The authoritative analytic results do not depend on the recurrence screen.
They follow from exact fixed-point indices, the mod-(2) language theorem,
uniform expansion, and the Bell--Miles--Ward single-automorphism theorem.

