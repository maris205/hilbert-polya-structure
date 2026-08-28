# C222 -- global bang--bang synthesis for the bounded double integrator

This package freezes the physical system

`x_dot=v, v_dot=u, |u|<=a`, with `a>0`,

and proves a whole-plane minimum-time theorem to the rest state `(0,0)`.
The result includes a sharp reachable-moment lower bound, the switching
parabola, closed arc lengths and value function, terminal identities,
Pontryagin and HJB certificates, reflection/scaling laws and the `a=0`
boundary.  It is one independent optimal-control paper, not a fragment of a
larger result.

From this directory run:

```text
python3 -B code/c222_double_integrator_producer.py
python3 -B code/c222_double_integrator_checker.py
python3 -B code/c222_double_integrator_sympy_crosscheck.py
python3 -B code/c222_double_integrator_replay.py
python3 -B code/c222_double_integrator_mutation.py
python3 -B code/c222_release_manifest.py
```

The evidence grid is regression evidence only.  The all-state theorem is
proved algebraically and by the sharp rearrangement bound.  The Route-A
verdict is `ROUTE_A_REJECTED`; no Route-B invocation is authorized.

Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.
