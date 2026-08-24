# C129 results

- Branch contraction: `||A||_infinity=1/4`; separation gap: `11/16`.
- Rooted closed words through period eight: 284.
- Primitive cycles through period eight: 40; theorem valid at every period.
- Original twisted symbolic determinant:
  `1-(zeta_5^3/2)z-(zeta_5^3/6)z^2-z^3/30`.
- Control twisted symbolic determinant:
  `1-z/2-(zeta_5^3/6)z^2-z^3/30`.
- Exact Hardy trace:
  `Tr(L_chi^n)=Tr(W_chi^n)/((1-8^(-n))(1-16^(-n)))`.
- Linear Hardy Fredholm coefficient changes from
  `-(64/105)zeta_5^3` to `-64/105`.
- The trivial character makes every all-order trace and determinant coincide
  and recovers C124.
- Validation: 71 independent checker assertions, 49 SymPy checks, exact byte
  replay, and 35/35 registered repaired-hash mutations rejected.

Evidence SHA-256:
`191774477cdc635d0ab8f45efd17acc1ca9cac4d2a5f133d685ce61c22b395df`.

Final PDF SHA-256:
`c3e4fc5b46116583dea7f1dff2c084e0ea348adff269b4484f3579d36e86ae35`.

Strict verdict: `(A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`.
