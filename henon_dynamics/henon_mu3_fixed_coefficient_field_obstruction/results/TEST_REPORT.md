# HCS-C44 test report

The final release runner performs four layers:

1. isolated deterministic producer replay and byte comparison;
2. independent exact checker replay;
3. targeted fail-closed mutation/regression tests;
4. complete SHA-256 artifact-manifest verification.

Final pre-provenance replay:

- independent checker: 12/12 gates passed;
- mutation/regression suite: 26/26 tests passed;
- exact control ledger: 45/45 split primes through 499;
- producer replay: byte-identical;
- manifest verification: completed after the paper and Route-A freeze.

No floating-point quantity, Riemann zero datum, or fitted parameter enters a
theorem gate.
