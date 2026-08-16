# Test report

Command:

    bash code/run_c73.sh

Results:

- main certificate: PASS;
- independent check: PASS;
- normal Python tests: 8/8 PASS;
- optimized Python tests: 8/8 PASS;
- dependency locks: 6/6 PASS;
- mutation audit: 25/25 rejected;
- formal tail coefficients: 96/96 in the certificate and 120/120 in tests;
- independent regularized pole reconstructions: 63/63 levels PASS.

The main certificate core SHA-256 is
`e86dfc15315675dba93c159d953b0a7d0277aacf28ae8b34dbdc7bb58734ee64`.
The normal and optimized suites exercise the same exact arithmetic and claim
firewalls; bytecode generation is disabled.
