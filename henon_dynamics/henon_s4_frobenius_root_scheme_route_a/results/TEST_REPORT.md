# Test report

All computational lanes pass:

- producer: 1228 good-prime rows and 14736 iterate cells PASS;
- independent finite-field checker: 16044 assertions PASS;
- SymPy exact verifier: 187 checks PASS;
- isolated replay: two byte-identical temporary-directory builds PASS;
- hostile mutation suite: 51 attacks PASS;
- unittest smoke suite: 3/3 PASS.

Every executable lane refuses `python -O` and `python -OO`.  The release gate also verifies strict JSON/YAML parsing, raw and semantic evaluator locks, exact 35-payload membership, deterministic warning-free PDFs, embedded subset fonts, extracted text, rasterization, and self-excluding manifest closure.
