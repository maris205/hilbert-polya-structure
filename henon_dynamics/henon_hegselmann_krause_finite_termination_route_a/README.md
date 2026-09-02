# HCS-C312: one-dimensional HK finite termination

This independent package proves exact finite stopping with a cubic bound,
complete fixed-cluster geometry, and piecewise rational cell dynamics for
homogeneous one-dimensional bounded-confidence averaging.

```bash
python -B henon_dynamics/henon_hegselmann_krause_finite_termination_route_a/code/c312_hk_producer.py
python -B henon_dynamics/henon_hegselmann_krause_finite_termination_route_a/code/c312_hk_checker.py
python -B henon_dynamics/henon_hegselmann_krause_finite_termination_route_a/code/c312_hk_sympy_crosscheck.py
python -B henon_dynamics/henon_hegselmann_krause_finite_termination_route_a/code/c312_hk_replay.py
python -B henon_dynamics/henon_hegselmann_krause_finite_termination_route_a/code/c312_hk_mutation.py
```

The release entry point is `code/c312_release_manifest.py`.
