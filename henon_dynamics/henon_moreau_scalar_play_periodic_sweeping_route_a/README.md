# HCS-C332 — scalar periodic Moreau play

This package proves the monotone-segment projection formula, exact Poincaré clamp, complete `D<2r`, `D=2r`, `D>2r` chamber atlas, one-period entrainment, order/nonexpansion, admissible reparameterization invariance, and exact variation/dissipation, including `r=0`, `D=0`, plateaus, and corners.

Route-A tuple:

`(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`

Overall verdict: `ROUTE_A_REJECTED`; Route B stays locked.

Run:

```bash
python3 -B code/c332_moreau_play_producer.py
python3 -B code/c332_moreau_play_checker.py
python3 -B code/c332_moreau_play_sympy_crosscheck.py
python3 -B code/c332_moreau_play_replay.py
python3 -B code/c332_moreau_play_mutation.py
python3 -B code/c332_release_manifest.py
```

The package has 28 physical files and 27 self-excluding manifest payloads.
