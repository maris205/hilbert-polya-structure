# HCS-C287 — sharp one-end wave observation and control

For `u_tt-c^2 u_xx=0` on `(0,L)` with homogeneous Dirichlet endpoints, this
package proves

`int_0^(2L/c) |u_x(t,L)|^2 dt = 4 E(0)/c^3`.

Thus one-end observability and HUM boundary controllability hold at and above
the exact time `2L/c`; every shorter window misses a nonzero smooth traveling
pulse.  The same time is the least common revival of the free wave group.

Run:

```bash
python3 -B code/c287_wave_producer.py
python3 -B code/c287_wave_checker.py
python3 -B code/c287_wave_sympy_crosscheck.py
python3 -B code/c287_wave_replay.py
python3 -B code/c287_wave_mutation.py
python3 -B code/c287_release_manifest.py
```

Scope is `NO_BAD_EULER_OR_ROOT_NUMBER`; Route B is disabled.
