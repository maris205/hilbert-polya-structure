# Test report

Command:

    bash code/run_c74.sh

Results:

- main certificate: PASS;
- independent reconstruction: PASS;
- normal Python tests: 16/16 PASS;
- optimized Python tests: 16/16 PASS;
- P72/P73 dependency locks: 6/6 PASS;
- exact coefficient rows: 96/96 PASS independently;
- mutation audit: 35/35 rejected.

The main certificate core SHA-256 is
`fd19d1f930c4b5d05440336fc348e78f7fd37a6d6d9ad633be2457bf2173a807`.
