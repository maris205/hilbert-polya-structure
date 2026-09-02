# Results

All analytic and computational gates passed for HCS-C298.

- The theorem gives the global exact solution
  `Ran(P(t))=exp(tA)Ran(P0)` and the corresponding projector formula for
  every real symmetric `A` and every initial rank-`k` projection.
- In simple spectrum, every eigenflag Schubert cell has its exact coordinate
  limit.  The rate is the gap to the actual next nonzero Pluecker weight, not
  an ambient subset-sum gap.  A representable-matroid greedy argument handles
  ambient subset-sum ties.
- In repeated spectrum, the associated-graded flag limit and every
  product-Grassmann Morse--Bott equilibrium component are explicit, including
  tangent, stable-normal, and unstable-normal dimensions.
- The exact ledger contains 80 simple-support cells, 37 repeated-support
  cells, 50 linear modes, and 22 Morse--Bott component rows: 189 audited
  cells across eight simple-spectrum and six repeated-spectrum cases.
- The independent checker passes 2,717 assertions without importing the
  producer; SymPy passes 534 symbolic checks.  Byte replay reproduces the
  74,655-byte JSON, and the hostile suite rejects 116/116 mutations.
- Manuscript rounds are 3, 4, and 4 pages; every font is embedded/subset and
  every settled log is clean.  The final PDF is the round-2 PDF.

Evidence file SHA-256:
`0519b0fd34b0ae5c41e2e92be6970d677229c1571c05552faba8fdf0667d3134`.
Evidence payload SHA-256:
`0d1a24a89ab2eb2d4cbfdea313c5d49d76dbec33e585ac01f603cf3f7a181545`.
Final PDF SHA-256:
`37c2512b70f1042b18b3fc89282fa58f82d65897e9e4c6aab6f8199957477295`.

The strict Route-A tuple is
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`; the overall verdict is
`ROUTE_A_REJECTED` and Route B is locked.
