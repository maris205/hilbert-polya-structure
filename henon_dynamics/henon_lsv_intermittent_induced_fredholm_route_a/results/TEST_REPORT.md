# Test execution report

Executed on 2026-09-05:

- Exact producer and independent rational certificate checker: PASS.
- Eight symbolic identities: PASS.
- 165 real certificates, 4,096 complex cells and 121 defect cells at 100 digits: PASS.
- Two isolated working directories and canonical byte replay: PASS.
- Repaired-hash hostile tests: 33/33 rejected.
- Strict JSON/YAML hostile tests: 10/10 rejected.
- Unittest smoke: 3/3 PASS.

The checker imports no producer and calls no square-root routine. It checks
forward branch inequalities and root signs directly; long inverse return
certificates are checked through exact quadratic inclusion inequalities.
The tail certificate positivity and width gates were added after independent
root review, together with a dedicated repaired-hash widening attack.
Return-reference arguments include the excluded target endpoint 1/2 as an
analytic boundary control; these rows do not assert literal return inverses
at a target outside Y.

PDF and final release receipts are separately recorded in
paper/COMPILE_REPORT.md and C381_RELEASE_MANIFEST.json. The nonwrite release
reconstructs all source evidence, reruns these lanes, tests optimized-mode
refusal and strict evaluation locks, and rebuilds all three PDF rounds.
