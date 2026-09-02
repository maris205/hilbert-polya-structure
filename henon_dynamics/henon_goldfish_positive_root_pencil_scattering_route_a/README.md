# HCS-C315: positive real goldfish scattering

This package closes an arbitrary-dimension theorem for Calogero's goldfish
flow on the ordered real chamber with strictly positive initial velocities.
The roots of the linear pencil `p(z,t)=P(z)-t Q(z)` remain real, simple,
ordered, and strictly increasing for every real time.  Their signed-time
interlacing gives a complete collision-free solution and an explicit
one-carrier scattering law through the fixed roots of `Q`.

The first inverse-time coefficient is closed for every finite root and for
the ballistic root.  Fourteen exact rational cases through dimension seven
provide regression evidence; the analytic proof, not the finite table,
owns the theorem for every finite `N>=2`.

Reproduce the package with:

```bash
python -B code/c315_goldfish_producer.py
python -B code/c315_goldfish_checker.py
python -B code/c315_goldfish_sympy_crosscheck.py
python -B code/c315_goldfish_replay.py
python -B code/c315_goldfish_mutation.py
python -B code/c315_release_manifest.py
```

The scope firewall is `NO_BAD_EULER_OR_ROOT_NUMBER`; Route B is false.
