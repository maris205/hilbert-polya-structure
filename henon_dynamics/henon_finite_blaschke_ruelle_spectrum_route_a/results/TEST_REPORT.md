# Executed test receipts

- checker: C380 independent checker PASS: checks=4839
- sympy_crosscheck: C380 symbolic/direct-orbit PASS: checks=409 direct_points=171 max_trace_residual=2.16749e-54
- replay: C380 two-directory replay PASS: sha256=35b49c40f27852bb445baea0479473d75dc169e88750b78e785eeae37881db77
- mutation: C380 repaired-hash mutations PASS: rejected=32/32
- producer: C380 producer PASS: parameters=5 census=24 exact trace and coefficient orders=16 payload=bdf014e65a8aabd16c1eef5bb7a214272d0ea7d59947234723f32b453bfa1cce
- smoke: 3/3 PASS
- optimized_refusals: 12/12 PASS
- yaml_hostile: 10/10 PASS

Finite computations audit the analytic theorem and do not replace it.
