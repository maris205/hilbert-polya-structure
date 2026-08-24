# C135 results

- Formal determinant:
  `Delta=1-x00-x11+x00*x11-x01*x10`.
- Replay prefix: 2,046 rooted words and 226 primitive cycles through period ten.
- `000111` edge vector: `(2,1,1,2)`; rooted trace multiplicity: 6.
- `001011` edge vector: `(1,2,2,1)`; rooted trace multiplicity: 12.
- Exact separating difference:
  `1-sqrt(2)-sqrt(3)+sqrt(6) != 0`.
- Remaining primitive nonrotation collision:
  `001011` and `001101`, common vector `(1,2,2,1)`.
- First same-edge-count primitive collision period: 6.
- All closed binary words satisfy `N01=N10`; `tau01-tau10` is invisible.
- Validation: checker 2,121, SymPy 37, byte replay PASS, mutations 43/43
  (`42` repaired-hash plus `1` stale-hash).

Evidence SHA-256:
`9980adaab9eb511fca367b83620d557ee2227a5e9c979b6c7c8ae9a73aebee36`.

Final two-page PDF SHA-256:
`0a0ab1a405e2fdec843d26a6fa1de81d74ce12768721dd21dcee29502882c808`.

Strict verdict: `(A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`.
