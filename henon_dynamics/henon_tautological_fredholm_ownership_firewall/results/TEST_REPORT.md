# Test report

Command:

    PYTHONDONTWRITEBYTECODE=1 bash code/run_c77.sh

Result:

- main certificate: PASS;
- independent reconstruction: PASS;
- normal Python tests: 12/12 PASS;
- optimized Python tests: 12/12 PASS;
- P75--P76 byte-level dependency locks: 6/6 PASS;
- protected schema and claim mutations: 38/38 rejected;
- singleton certificate rows: 24/24;
- independent exact rational cyclic determinants: 10/10;
- primary rank-one checks: 6/6; independent checks: 3/3.

The main certificate core SHA-256 is
`f11d28ba20b4f6677023d0db5eaf0b8d8ff6b15f82526abd29ffd8c0eb705cfc`.
