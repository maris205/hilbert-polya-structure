# HCS-C296 — rotation-reduced circular hard-rod shape flow

Frozen obstruction identifier: `HEN-O280`.

This package proves a complete all-event theorem for equal-mass hard rods on a
circle **after quotienting global rotation**.  Excluded-volume compression
with `L=ell-N*a` is conjugate to free phase points modulo common position
translation and `S_N`; simultaneous contacts, invariants, no Zeno, and the
full distinct/repeated-velocity return criterion are closed.

The complete physical angle is deliberately absent.  `N=1` proves that the
same length-`L` statement for the unreduced physical phase space is false.

Run from the repository root:

```bash
python -B henon_dynamics/henon_hard_rod_rotation_reduced_shape_route_a/code/c296_hard_rod_producer.py
python -B henon_dynamics/henon_hard_rod_rotation_reduced_shape_route_a/code/c296_hard_rod_checker.py
python -B henon_dynamics/henon_hard_rod_rotation_reduced_shape_route_a/code/c296_hard_rod_sympy_crosscheck.py
python -B henon_dynamics/henon_hard_rod_rotation_reduced_shape_route_a/code/c296_hard_rod_replay.py
python -B henon_dynamics/henon_hard_rod_rotation_reduced_shape_route_a/code/c296_hard_rod_mutation.py
python -B henon_dynamics/henon_hard_rod_rotation_reduced_shape_route_a/code/c296_release_manifest.py
```

The strict tuple is
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`, with overall
`ROUTE_A_REJECTED`, Route B disabled, and literal scope
`NO_BAD_EULER_OR_ROOT_NUMBER`.
