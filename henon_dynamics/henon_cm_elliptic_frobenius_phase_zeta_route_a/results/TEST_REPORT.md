# Test report

- producer: `C382_PRODUCER_PASS {'prime_max': 1000, 'degree_max': 24, 'prime_count': 167, 'prime_degree_cells': 4008} b62daf82a23568fa07efcdbc1b097c477eedd3f81461116da6a574b9dd0cf831`
- checker: `C382 independent checker: PASS (17674 assertions)`
- sympy: `C382 SymPy cross-check: PASS (508 exact checks)`
- replay: `C382 byte replay: PASS 7357c6fbe5868be50f18cfc482b45eb5b4c274b9bb1cd3b1ca957e1cb793db81`
- mutation: `C382 hostile mutation suite: PASS (55 attacks)`
- smoke: `3 tests PASS`

Every lane refuses optimized Python; strict JSON/YAML, source/scope and PDF gates pass.
