# Results

- Canonical evidence: `c227_lorenz_evidence.json`.
- Main positive-parameter rows: 10.
- Exact Lyapunov cancellation rows: 5.
- Degenerate boundary families: 3.
- Independent checker: PASS, 231 assertions.
- SymPy reconstruction: PASS, 14 identities.
- Canonical clean-process replay: PASS, byte identical.
- Hostile mutations: PASS, 17/17 rejected.
- Route-A tuple:
  `(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)`.
- Overall verdict: `ROUTE_A_REJECTED`.
- Route-B invocation: false.

The regression rows include two exact Hopf surfaces, both sides of the
classical and a simple threshold, a no-finite-Hopf case, negative \(\rho\),
and all zero-rate faces.  They are deterministic theorem audits, not fitted
orbit data.
