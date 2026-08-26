# Test report

All executable tests passed on 2026-08-26 from repository commit `bbb809ee198bc9ad5f196383baab1e3d9de38e43`.

```text
C180_PRODUCER_PASS formula_rows=108 torsion_rows=16 wold_rows=5880
C180_CHECKER_PASS assertions=43184
C180_SYMPY_PASS checks=18065 sympy_version=1.14.0
C180_REPLAY_PASS bytes=1618066 sha256=1a059d8843579bc893bf3460117434fa828d46a294cda6a18e7a298b02ca82ec
C180_MUTATION_PASS repaired_hash_rejections=23 stale_hash_rejections=1
```

The direct torsion test constructs rational torus points rather than substituting the closed formulas. The independent checker imports no producer code. Replay compares raw bytes. Mutation tests repair the embedded payload hash before invoking the semantic checker, so hash consistency alone cannot pass them.

PDF determinism, font embedding, layout, and manifest closure are reported separately in `paper/COMPILE_REPORT.md` and `C180_RELEASE_MANIFEST.json`.
