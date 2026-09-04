# Test report

All computational lanes pass:

- producer: 561 aspects, 35904 modal cells, 62 thresholds, and 390 rigid rows PASS;
- independent unfactorized checker: 37030 assertions PASS;
- SymPy exact verifier: 2470 checks PASS;
- isolated replay: two byte-identical temporary-directory builds PASS;
- hostile mutation suite: 64 attacks PASS (54 repaired-hash JSON, 1 stale-hash,
  3 malformed/root JSON, and 6 YAML attacks);
- unittest smoke suite: 3/3 PASS.

Every executable lane refuses `python -O` and `python -OO`.  The release gate also verifies strict JSON/YAML parsing, raw and semantic evaluator locks, exact 35-payload membership, deterministic warning-free PDFs, embedded subset fonts, extracted text, rasterization, and self-excluding manifest closure.
