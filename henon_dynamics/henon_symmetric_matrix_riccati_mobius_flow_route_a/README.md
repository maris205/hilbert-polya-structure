# HCS-C309: symmetric matrix Riccati Möbius flow

This package proves an all-dimensional theorem for `Xdot=I-X^2` on real
symmetric matrices: exact solution, complete maximal-time/pole atlas,
forward limits and rates, gradient obstruction to recurrence, Grassmann
Morse--Bott equilibrium strata, and the full Fréchet derivative of the time
map.

Run the five evidence lanes from the repository root:

```bash
python -B henon_dynamics/henon_symmetric_matrix_riccati_mobius_flow_route_a/code/c309_riccati_producer.py
python -B henon_dynamics/henon_symmetric_matrix_riccati_mobius_flow_route_a/code/c309_riccati_checker.py
python -B henon_dynamics/henon_symmetric_matrix_riccati_mobius_flow_route_a/code/c309_riccati_sympy_crosscheck.py
python -B henon_dynamics/henon_symmetric_matrix_riccati_mobius_flow_route_a/code/c309_riccati_replay.py
python -B henon_dynamics/henon_symmetric_matrix_riccati_mobius_flow_route_a/code/c309_riccati_mutation.py
```

The final release verifier is `code/c309_release_manifest.py`.  The Route-A
result is rejected at A0--A3 with only an `A4_FORMAL_HINT`; Route B is locked.
