# Test report

All five computational lanes pass under ordinary Python and explicitly refuse both `python -O` and `python -OO`:

- producer: 36 exact systems and 3 two-body rows PASS;
- independent checker: 385 assertions PASS;
- SymPy lane: 16 exact checks PASS;
- isolated replay: two byte-identical temporary-directory runs PASS;
- hostile mutation: 70 attacks PASS.

The release gate additionally verifies strict JSON/YAML parsing, raw and semantic evaluator locks, exact 27-payload membership, warning-free deterministic PDFs, embedded subset fonts, extracted text, rasterization, and self-excluding manifest closure.
