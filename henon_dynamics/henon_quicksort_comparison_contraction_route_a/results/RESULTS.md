# Results — HCS-C302

The global analytic result gives every finite Quicksort comparison law by a
PGF recurrence, exact mean and variance, convergence to the unique centered
finite-variance contraction fixed point, an `L3` license, and the exact
positive third moment `16*zeta(3)-19`.

The current exact certificate contains:

- 13 PGF rows (`0<=n<=12`) and 173 nonzero coefficient cells;
- integer permutation counts summing to `n!` in every row;
- raw moments through order three and normalized centered moments;
- 527 exact pivot rows for the `(n+1)`-centered recurrence (`2<=n<=32`);
- six exact/decimal variance-limit diagnostics;
- exact integral receipts for the `2/3` contraction, variance, and third
  moment, plus the rational positivity lower bound `67/1500`.

The independent checker passes 8,377 assertions, including exhaustive
enumeration of all permutations through `n=9`.  The SymPy lane passes 2,424
symbolic/cell assertions.  Replay is byte-identical and all 72 hostile
mutations are killed.

Evidence payload SHA-256:
`8f1092fa6172e1199583e8ef942cc7d5713102eef96fe9991a2af4f34f057a6b`.

Evidence file SHA-256:
`0ceba774a464fa86ffa9cb20c44b4b7c57aafb3c6d5aec5a63f1417f92e788fc`.

The strict evaluation is
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL) / ROUTE_A_REJECTED`.
