# HCS-C260 — projective Möbius cycle atlas

This package proves and certifies the complete `PGL_2(F_q)` action on `P^1(F_q)` for every prime power. It includes the four dynamical types, arbitrary-iterate fixed counts, primitive cycles, finite zeta and Koopman closure, exact reversors, characteristic-two classification, and exact type/order census.

Key artifacts:

- `THEOREM_PACKAGE.md`: self-contained theorem and proof.
- `results/c260_pgl2_evidence.json`: exact 18-field regression receipt.
- `code/c260_pgl2_checker.py`: producer-independent direct-permutation checker.
- `paper/main.pdf`: final round-2 manuscript.
- `evaluations/route_a/HCS-C260/2026-08-31.yaml`: Route-A decision.
- `C260_RELEASE_MANIFEST.json`: self-excluded content-addressed closure.

Run the five verification commands in `code/README.md`, then run `python3 -B code/c260_release_manifest.py` after the paper artifacts exist.

Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`. Source Artin--Mazur zeta and a finite permutation Koopman operator are not target Euler factors or a Hilbert--Polya construction.
