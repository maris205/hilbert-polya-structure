# C359 test report

- producer: PASS; 8 canonical, 72 orbit, 3 irrational, 2,048 quantum, and 7 boundary rows;
- independent checker: PASS (17,437 checks);
- independent SymPy lane: PASS (8,039 identities);
- isolated replay: PASS (364,809 bytes in two temporary directories);
- optimized interpreter refusal: PASS for `-O` and `-OO` on all five executable lanes;
- canonical JSON, duplicate/nonfinite rejection, exact rational strings, raw/semantic YAML locks, exact nested coordinates, and source/scope/theorem ownership: PASS;
- PDF and release-manifest gates: reported in `paper/COMPILE_REPORT.md` and `C359_RELEASE_MANIFEST.json`.
