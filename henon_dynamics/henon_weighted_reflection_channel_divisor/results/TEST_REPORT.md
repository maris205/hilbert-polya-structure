# Test report

Command:

    PYTHONDONTWRITEBYTECODE=1 bash code/run_c75.sh

Results:

- main certificate: PASS;
- independent reconstruction: PASS;
- exact primary weighted coefficients: 48/48;
- independent weighted coefficients: 64/64;
- positive-fiber geometry rows: 72/72;
- normal Python tests: 12/12 PASS;
- optimized Python tests: 12/12 PASS;
- dependency locks: 9/9 PASS;
- mutation audit: 38/38 rejected.

The main certificate core SHA-256 is
`8d6993045f20d089e0fc36a26b123e559ab2826268aee705340ce23d6c8e3661`.
