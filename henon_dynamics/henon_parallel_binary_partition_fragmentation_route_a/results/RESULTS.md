# Results

The analytic theorem is proved for every `n>=1`, every integer `t>=0`, and
every starting/terminal labelled partition.  The archived exact evidence has:

- 278 complete transition-state rows for `1<=n<=6`;
- 44,168 full matrix cells including zeros;
- 1,860 listed nonzero transition probabilities;
- 81 time-law rows and 405 block-count coefficient cells;
- 104 absorption-mass rows;
- five critical-window diagnostic rows.

All probability entries are exact integers or reduced rationals.  The decimal
critical rows are explicitly diagnostic and are not proof inputs.

The independent checker passes 3,570 assertions.  The SymPy cross-check passes
17,910 symbolic/cell assertions, including characteristic polynomials,
determinants, squarefree annihilators, eigenspace dimensions, matrix powers,
and polynomial occupancy identities.  Deterministic replay is byte-identical,
and all 57 hostile mutations are killed.

Evidence payload SHA-256:
`1fcd7d727f3fd75ce99257c2ee69c6ecc7ff2332ad582628ad72ac9473043c10`.

Evidence file SHA-256:
`011f146e1fecfb88a6cc4a692d95a8267b9549cfefa43628083ab1aa21b06a03`.

The Route-A verdict is exactly
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL) / ROUTE_A_REJECTED`.
