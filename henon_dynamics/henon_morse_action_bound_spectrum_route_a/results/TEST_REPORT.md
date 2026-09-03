# Test report

- Independent checker: PASS, 1,749 checks.
- SymPy cross-check: PASS, 273 exact identities.
- Byte replay: PASS, two isolated reproductions.
- Optimized-Python gate: producer, checker, SymPy, replay, mutation, and release scripts refuse `-O`/`-OO`.
- Strict JSON: duplicate keys and nonfinite constants rejected.
- Strict YAML: duplicate/non-string keys, implicit timestamps, merges, anchors, aliases, schema drift, authority drift, and layer drift rejected.
- PDF: all rounds rebuilt twice with LuaLaTeX; archive bytes deterministic; fonts embedded and subset; text and raster gates pass.
