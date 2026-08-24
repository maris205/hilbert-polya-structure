# HCS-C124: graph-directed Hardy trace bridge

This package certifies an all-period primitive-orbit/trace-class/Fredholm bridge
for one strongly separated three-state affine Hénon system.  It also proves a
negative control: changing branch translations moves the cycles without
changing the determinant.

## Reproduce

```bash
python3 code/c124_hardy_producer.py
python3 code/c124_hardy_checker.py
python3 code/c124_sympy_crosscheck.py
python3 code/c124_replay.py
python3 code/c124_mutation.py
```

The final manuscript is `paper/main.pdf`.  Exact claims are bound to
`results/c124_hardy_evidence.json`; the content ledger is
`C124_RELEASE_MANIFEST.json`.

Strict verdict:

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
ROUTE_A_EXPLORATORY
route_b_invocation_allowed: false
```

The source determinant is exact but has no target-divisor comparison.  Scope
firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.
