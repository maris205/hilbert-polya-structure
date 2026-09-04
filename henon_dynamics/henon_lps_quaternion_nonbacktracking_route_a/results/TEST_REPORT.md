# Test report

- producer: five full groups and 60 iterate rows PASS;
- independent checker: 209099 assertions PASS;
- SymPy lane: 1237 exact checks PASS;
- isolated replay: two byte-identical builds PASS;
- hostile mutation suite: 83 attacks PASS;
- unittest smoke suite: 3/3 PASS.

Every executable refuses optimized Python. The release gate also checks strict JSON/YAML, evaluator locks, deterministic PDFs, fonts, text, rasterization, and the frozen-wrapper bilingual abstract/keyword gates and exact 38-payload ledger.
