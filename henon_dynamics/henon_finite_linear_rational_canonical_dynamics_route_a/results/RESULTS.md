# Results

- Eight witnesses, 144 fixed-count formula cells, and exhaustive state graphs
  through 625 states all agree.
- The independent checker recomputes every fixed count from `rank(A^n-I)` and
  recovers transient height from kernel stabilization.
- SymPy verifies 198 polynomial-gcd cells and six full-function Koopman
  characteristic polynomials.
- The nilpotent `F_5` control has 625 states, five periodic states, maximal
  preperiod three, and Koopman zero multiplicity 620.
- The genuine GF(4) nonsemisimple control has period order six under
  `a^2+a+1=0`; substituting `Z/4Z` is rejected.
- Byte replay passes; 17 repaired-hash semantic attacks and one stale-hash
  attack are caught.
- Final paper: 2 balanced pages, 261852 bytes, SHA-256
  `336d039d320202a36f7c3c64af1c6bc7a058431575b8ce4e78336d2e5016a38a`.
- Route A: `(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,
  `overall=ROUTE_A_REJECTED`, `route_b_invocation_allowed=false`.
