# HCS-C306 — Killed noncolliding walkers

This package closes, for every `L>=1` and `1<=k<=L`, the continuous-time
nearest-neighbour system on the ordered chamber in which a boundary attempt or
collision attempt kills the trajectory.  It contains the one-particle sine
kernel, Karlin--McGregor determinant, complete Slater spectrum, the full
absorption-time finite sum, its leading asymptotics, the unique QSD, and the
ground-state Doob transform.

The model is not reflecting exclusion.  Its forbidden moves retain their
rate as killing.  Exact finite sums are provided for first passage; no simpler
elementary closed form is asserted.

## Reproduce

From this directory, run:

```text
python3 code/c306_walkers_producer.py
python3 code/c306_walkers_checker.py
python3 code/c306_walkers_sympy_crosscheck.py
python3 code/c306_walkers_replay.py
python3 code/c306_walkers_mutation.py
python3 code/c306_release_manifest.py
```

The last command rebuilds all three manuscript rounds twice in isolated
directories, verifies warning-free logs, embedded/subset fonts, text
sentinels, rendered pages, the exact 27-file payload ledger, and then writes
the self-excluded release manifest.  Run it twice to verify stable manifest
bytes.

Route A is rejected with tuple `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,
A4_FORMAL_HINT)`; the finite symmetric generator is only a candidate-local
operator analogy.  Route B is locked and the scope literal is
`NO_BAD_EULER_OR_ROOT_NUMBER`.
