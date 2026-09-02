# HCS-C310: Dubins bounded-curvature optimal synthesis

This independent paper package turns the six Dubins path families into a
complete boundary-safe global synthesis: explicit formulas, feasibility,
degeneracies, ties, scaling/reflection, and direct endpoint replay.

```bash
python -B henon_dynamics/henon_dubins_bounded_curvature_optimal_synthesis_route_a/code/c310_dubins_producer.py
python -B henon_dynamics/henon_dubins_bounded_curvature_optimal_synthesis_route_a/code/c310_dubins_checker.py
python -B henon_dynamics/henon_dubins_bounded_curvature_optimal_synthesis_route_a/code/c310_dubins_sympy_crosscheck.py
python -B henon_dynamics/henon_dubins_bounded_curvature_optimal_synthesis_route_a/code/c310_dubins_replay.py
python -B henon_dynamics/henon_dubins_bounded_curvature_optimal_synthesis_route_a/code/c310_dubins_mutation.py
```

The final release verifier is `code/c310_release_manifest.py`.
