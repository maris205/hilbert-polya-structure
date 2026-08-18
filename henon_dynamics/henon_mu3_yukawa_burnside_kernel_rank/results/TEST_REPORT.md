# HCS-C63 prefreeze test report

Commands:

```text
python3 -m py_compile code/*.py
python3 code/c63_kernel.py
python3 code/c63_kernel_checker.py
python3 code/c63_kernel_replay_checker.py
python3 code/c63_mutation_test.py
```

Producer result:

```text
{"ambient_order": 51840, "class_count": 25,
 "hminus_type": "S16", "hplus_type": "S15",
 "matrix_sha256": "e912b0f37f69ac1e23cf432915aa4258818312f84fba776986876c7625a84a9b",
 "nullity_over_Q": 3, "rank_over_Q": 13,
 "status": "PREFREEZE_G3_PASS", "type_count": 16}
```

Structural checker result:

```text
{"ambient_order": 51840, "class_count": 25,
 "matrix_sha256": "e912b0f37f69ac1e23cf432915aa4258818312f84fba776986876c7625a84a9b",
 "nullity_over_Q": 3, "primitive_four_term_support": 8,
 "primitive_restricted_rank": 7, "rank_over_Q": 13,
 "status": "PASS", "type_count": 16}
```

The hostile suite rejected 10 mutations covering source hashes, scope,
status, matrix entries, rank, basis, relation placement, support rank, full
Burnside overclaim, and arithmetic overclaim.

The independent source replay returned:

```text
{"ambient_order": 51840, "class_count": 25, "hminus_type": "S16",
 "hplus_type": "S15", "lambda_exterior_zero": true,
 "lambda_symmetric_zero": true, "matrix_shape": [25, 16],
 "nullity_over_Q": 3, "rank_over_Q": 13, "status": "REPLAY_PASS",
 "type_count": 16}
```
