# C361 test report

- Producer: PASS; 4 panels, 700 tree rows, 2,244 path rows.
- Independent checker: PASS; 2,504 counted assertions; independent Laplacian-cofactor and Faddeev--LeVerrier implementations; no producer import.
- SymPy lane: PASS; 478 symbolic assertions.
- Replay: PASS; two isolated temporary directories, 1,011,198 byte-identical bytes.
- Hostile suite: PASS; 53/53 killed, including 40 repaired-payload attacks, stale-hash control, duplicate/nonfinite JSON, and strict YAML duplicate/merge/non-string/alias/timestamp/unknown/type attacks. Targeted repairs reverse the RN derivative, corrupt the tilt transpose, and separate total, medium, and endpoint path ratios.
- Optimized Python: producer, checker, SymPy, replay, mutation, and release refuse `-O` and `-OO`.
- Evaluation lock: raw SHA `e61d1cc50b0891d2ecefb02bd460bf8b2bde48bf8f78fa6fb0e7524c6c931c7b`; semantic SHA `f8b6e53916659fb22cdc2b4278c5ef43ce5a24ea09ece76e86ada0dd3ff3c09b`.
- PDF gate: fresh two-pass LuaLaTeX builds at epoch 1788480000 are deterministic; settled logs have no warnings or layout faults; all fonts embedded/subset; text sentinels and rasterization pass.
