# HCS-C254 — Monod chemostat threshold atlas

This package proves one complete theorem for the positive one-species Monod
chemostat.  The decisive coordinate is total nutrient
`Q=S+X/Y`: it obeys a scalar linear equation even though substrate and biomass
are nonlinearly coupled.  That reduction closes the washout, critical and
survival regimes, global convergence, the transcritical exchange, the exact
invariant-leaf transient, and all declared zero/boundary faces.

The finite artifact contains 18 exact rational parameter receipts.  It checks
conventions and algebra; it is not used as a substitute for the continuous-
parameter proof and contains no experimental observations.

```bash
python code/c254_monod_producer.py
python code/c254_monod_checker.py
python code/c254_monod_sympy_crosscheck.py
python code/c254_monod_replay.py
python code/c254_monod_mutation.py
python code/c254_release_manifest.py
```

The strict Route-A tuple is
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`.  The source has no arithmetic
origin, and every recurrent state is an equilibrium.  The result is therefore
`ROUTE_A_REJECTED`; Route B is disabled under
`NO_BAD_EULER_OR_ROOT_NUMBER`.

The compiled manuscript is [paper/main.pdf](paper/main.pdf).
