# C138 test report

All commands were run from the repository root on 2026-08-24.

| Test | Result |
|---|---|
| producer | PASS; canonical evidence emitted |
| independent checker | PASS; determinant, controls, 14,760 rooted and 1,905 primitive receipts reconstructed without producer import |
| separate SymPy reconstruction | PASS; 197 exact checks |
| deterministic replay | PASS; byte-identical evidence |
| mutation suite | PASS; 45/45 rejected = 44 repaired-hash semantic + 1 stale-hash |

Commands:

```text
python henon_dynamics/henon_magnetic_quantum_graph_route_a/code/c138_magnetic_graph_producer.py
python henon_dynamics/henon_magnetic_quantum_graph_route_a/code/c138_magnetic_graph_checker.py
python henon_dynamics/henon_magnetic_quantum_graph_route_a/code/c138_sympy_crosscheck.py
python henon_dynamics/henon_magnetic_quantum_graph_route_a/code/c138_replay.py
python henon_dynamics/henon_magnetic_quantum_graph_route_a/code/c138_mutation.py
```

The independent checker closes all evidence schemas and preserves Laurent orientation data.  It does not import the producer.
