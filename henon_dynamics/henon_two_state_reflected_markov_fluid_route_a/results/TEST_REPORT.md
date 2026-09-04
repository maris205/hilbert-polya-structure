# Test report

All five computational lanes pass under ordinary Python and explicitly refuse both `python -O` and `python -OO`:

- producer: 81 core rows and 12 boundary rows PASS;
- independent checker: 852 assertions PASS;
- SymPy lane: 36 exact checks PASS;
- isolated replay: two byte-identical temporary-directory runs PASS;
- hostile mutation: 95 attacks PASS.

The release gate additionally verifies strict JSON/YAML parsing, raw and semantic evaluator locks, exact 27-payload membership, warning-free deterministic PDFs, embedded subset fonts, extracted text, rasterization, and self-excluding manifest closure.
