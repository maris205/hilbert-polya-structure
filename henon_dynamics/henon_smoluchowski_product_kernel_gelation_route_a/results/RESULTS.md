# Results

- Exact Cayley coefficient rows: 40.
- Pregel/critical time rows: 5.
- Smoluchowski/Stockmayer postgel rows: 4.
- Flory postgel rows: 4.
- Critical-tail rows: 5.
- Direct cluster equations per time branch: first 20.
- Independent checker: PASS, 696 assertions.
- SymPy reconstruction: PASS, 29 identities.
- Canonical byte replay: PASS.
- Hostile mutations: PASS, 28/28 rejected.
- Route-A tuple:
  `(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)`.
- Overall: `ROUTE_A_REJECTED`; Route B: false.

The decisive result is that postgel Stockmayer mass \(1/t\) and Flory mass
\(q=-W_0(-te^{-t})/t\) belong to different loss closures.  Their coefficient
families coincide only at \(t=1\).
