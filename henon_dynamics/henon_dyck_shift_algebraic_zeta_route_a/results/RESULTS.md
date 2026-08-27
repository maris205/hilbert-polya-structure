# Results

- Six parameter values and periods 1--24 give 144 exact fixed/primitive/orbit
  cells without floating point.
- An independent formal logarithmic derivative reproduces all 144 fixed counts.
- Thirty-three direct periodic-word enumerations reproduce the formula under
  the origin-marked convention.
- SymPy verifies 72 zeta coefficients, the `N=1` full-two-shift cancellation,
  every `N=2..6` double-pole, conjugation, and dominance control, plus six
  entropy/dominant-radius identities.
- The source-locked entropy theorem and periodic growth give
  `h_top(D_N^E)=log(N+1)` for all `N>=1`.
- Byte replay passes; 18 repaired-hash semantic attacks and one stale-hash
  attack are rejected.
- Final paper: 3 balanced pages, 244591 bytes, SHA-256
  `203531a0984884266508021d163ed6a5d03b651919698f34b140495b939c4986`.
- Route A: `(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`,
  `overall=ROUTE_A_REJECTED`, `route_b_invocation_allowed=false`.
