# HCS-C135: edge-roof nonlattice suspension

This package refines C130's symbol-count suspension clock to an exact
directed-edge roof on the full binary shift.  It proves the all-period formal
determinant and primitive product, separates `000111` from `001011`, and proves
the remaining `001011`/`001101` collision and off-diagonal orientation
blindness.

## Reproduce

```bash
python3 code/c135_edge_roof_producer.py
python3 code/c135_edge_roof_checker.py
python3 code/c135_sympy_crosscheck.py
python3 code/c135_replay.py
python3 code/c135_mutation.py
```

The exact receipt is `results/c135_edge_roof_evidence.json`, the manuscript is
`paper/main.pdf`, and the evaluator record is
`evaluations/route_a/HCS-C135/2026-08-24.yaml`.

Strict verdict:

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
ROUTE_A_EXPLORATORY
route_b_invocation_allowed: false
```

The primitive product is dynamical, not arithmetic.  Scope firewall:
`NO_BAD_EULER_OR_ROOT_NUMBER`.
