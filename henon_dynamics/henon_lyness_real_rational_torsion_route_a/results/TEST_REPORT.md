# Executed test report

Commands and exact reproducible output families:

- Producer PASS: 24 orbit rows, 288 exact steps, 11 cycles, 59 cycle points,
  5 centers, 5 endpoint intervals, 1280 denominator controls, 690 witnesses.
- Independent checker PASS with the same complete population.
- Symbolic/high-precision PASS: exact_identities=35, enclosure_controls=11, quadrature_controls=24,
  working_digits=90, a1_error_below=1e-70; integrals are not interval certificates.
- Two-directory byte replay PASS.
- Hostile repaired-hash/type/YAML PASS: 38/38 rejected; semantic=31,
  JSON=2, YAML=5.

Smoke: 3/3 passed in an actual unittest discovery run.
Optimized-mode refusals are reconstructed by the release command.
The release manifest retains their actual outcome with the complete lane
receipts, rather than accepting this prose as a validation source.
