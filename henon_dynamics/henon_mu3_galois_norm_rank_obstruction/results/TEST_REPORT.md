# HCS-C45 test report

- exact certificate producer: PASS;
- independent checker: 12/12 gates PASS;
- complete split-prime trace ledger through 499: 45/45 PASS;
- chronological second-moment ledger: 11/11 PASS;
- mutation and regression suite: 28/28 PASS;
- floating-point spectral calculations: none;
- Riemann-zero data: none;
- averaged chronological dynamics: none.

The producer and checker use separate implementations of both zero-fibre
counters.  Unexpected checker exceptions are reported as `ERROR`, never
softened to an expected mathematical `FAIL`.
