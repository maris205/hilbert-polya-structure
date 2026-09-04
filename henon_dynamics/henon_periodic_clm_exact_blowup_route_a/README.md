# HCS-C377: periodic CLM exact blow-up closure

This independent theorem package solves the inviscid nonadvective periodic Constantin–Lax–Majda equation `ω_t=ωHω` for arbitrary conserved mean under the fixed convention `H(e^{ikx})=-i sign(k)e^{ikx}`. It proves the periodic Tricomi reduction, both exact Möbius solutions, necessary-and-sufficient forward breakdown clocks in both mean strata, a complete one-mode phase diagram, and simple-first-pole self-similar profiles with a correctly conditional global inverse-time rate.

The strict tuple is `(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)`, the verdict is `ROUTE_A_REJECTED`, and Route B is not invoked. Scope literal: `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Reproduce

```bash
python -B code/c377_periodic_clm_producer.py
python -B code/c377_periodic_clm_checker.py
python -B code/c377_periodic_clm_sympy_crosscheck.py
python -B code/c377_periodic_clm_replay.py
python -B code/c377_periodic_clm_mutation.py
python -B -m unittest tests/test_c377_smoke.py
python -B code/c377_release_manifest.py --build-pdfs
python -B code/c377_release_manifest.py --write
python -B code/c377_release_manifest.py
```
