# C137 test report

All commands were run from the repository root on 2026-08-24.

| Test | Result |
|---|---|
| producer | PASS; canonical evidence emitted |
| independent checker | PASS; 18,414 exact word receipts reconstructed without producer import |
| separate SymPy reconstruction | PASS; 18,379 exact checks |
| deterministic replay | PASS; byte-identical evidence |
| mutation suite | PASS; 41/41 rejected = 40 repaired-hash semantic + 1 stale-hash |

Commands:

```text
python henon_dynamics/henon_uniform_mobius_bergman_family_route_a/code/c137_uniform_mobius_producer.py
python henon_dynamics/henon_uniform_mobius_bergman_family_route_a/code/c137_uniform_mobius_checker.py
python henon_dynamics/henon_uniform_mobius_bergman_family_route_a/code/c137_sympy_crosscheck.py
python henon_dynamics/henon_uniform_mobius_bergman_family_route_a/code/c137_replay.py
python henon_dynamics/henon_uniform_mobius_bergman_family_route_a/code/c137_mutation.py
```

The checker closes top-level, nested theorem, receipt, tuple, and scope schemas.  It performs exact rational reconstruction and does not import the producer.
