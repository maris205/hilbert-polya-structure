# C149 results

- Infinite component: nonempty minimal Thue--Morse subshift, zero periodic
  points at every positive period.
- Attached skeleton: four cycles of lengths `1,2,3,5`, totaling 11 points.
- All-period fixed count: `sum_(ell|n) ell` over the four declared lengths.
- Primitive skeleton: one cycle at each declared length, no others.
- Source zeta: `1/((1-z)(1-z^2)(1-z^3)(1-z^5))`.
- Structural cost: every nonempty finite disjoint attachment destroys
  minimality.
- Replay: 60 period rows, 31 zeta coefficients, 32 aperiodicity receipts.
- Independent checker: 395 assertions; SymPy: 277 checks.
- Mutation audit: 41 repaired-hash plus one stale-hash rejection.

Evidence SHA-256: `774babf27a162728f63f4d1a76877e8d7c412c9f1c62286e3463868875084dfc`.
