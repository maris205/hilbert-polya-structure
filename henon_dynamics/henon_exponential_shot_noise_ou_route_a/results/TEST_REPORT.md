# Test report

- Independent checker: PASS, 1,600 checks.
- SymPy cross-check: PASS, 126 exact identities.
- Byte replay: PASS, two isolated reproductions.
- Optimized-Python gate: producer, checker, SymPy, replay, mutation, and release scripts refuse `-O`/`-OO`.
- Strict JSON/YAML, canonical rational/decimal, raw and semantic YAML, evaluator authority, nested schema, coordinate, and enumeration locks pass.
- PDF: all rounds are deterministic fresh two-pass LuaLaTeX products with embedded/subset fonts and clean text/raster gates.
