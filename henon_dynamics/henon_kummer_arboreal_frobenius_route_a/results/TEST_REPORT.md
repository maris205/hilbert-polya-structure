# Test report

All release lanes pass:

- producer: `C374_PRODUCER_PASS levels=10 group_pairs=5592400 prime_cells=95910 payload_sha256=54155768c4b983d5de2c66b042d481b86135aecc6c7506ee100e6aa6b79127d7`;
- independent checker: 247 assertions PASS;
- SymPy cross-check: 4145 exact checks PASS;
- isolated byte replay: PASS;
- hostile repaired-hash suite: 42 attacks PASS;
- unittest smoke suite: 3/3 PASS;
- optimized-mode refusal under `-O` and `-OO`: PASS;
- strict JSON/YAML schema, A0 controls, weak-A1 lock, scope, source,
  membership, bilingual abstract/keyword layering, PDF, CJK font, text, and
  raster gates: PASS.
