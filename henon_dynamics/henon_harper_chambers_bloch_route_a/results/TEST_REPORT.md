# Test report

All computational lanes pass:

- producer: 390 panels and 74880 fibers PASS;
- independent characteristic/fiber checker: 1139690 assertions PASS;
- SymPy exact cyclotomic verifier: 1557 checks PASS;
- isolated replay: two byte-identical temporary-directory builds PASS;
- hostile repaired-hash mutation suite: 107 attacks PASS;
- unittest smoke suite: 3/3 PASS.

Every executable lane refuses `python -O` and `python -OO`.  The release gate additionally verifies strict JSON/YAML parsing, raw and semantic evaluator locks, exact 35-payload membership, deterministic warning-free PDFs, embedded subset fonts, extracted text, rasterization, and self-excluding manifest closure.
