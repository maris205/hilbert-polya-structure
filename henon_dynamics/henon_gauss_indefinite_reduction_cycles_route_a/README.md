# HCS-C364 — Gauss Indefinite Reduction Cycles

This package proves a complete fixed-discriminant theorem for the Gauss shift on primitive reduced real quadratic irrationals: finite bijection, all cycles, exact period matrices and multipliers, reversal, fixed counts, finite Artin--Mazur zeta, and Koopman determinant.

## Frozen identity

- Candidate: `HCS-C364`
- Obstruction: `HEN-O348`
- Source commit: `323ea43f6970544467f8a89f0ed9be0c7c39f896`
- Evaluation date: `2026-09-04`
- Fixed epoch: `1788480000`
- Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`
- Route tuple: `(A0_WEAK_ARITHMETIC_RELATION,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`
- Overall: `ROUTE_A_EXPLORATORY`; Route B false.

## Reproduction

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c364_gauss_reduction_producer.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c364_gauss_reduction_checker.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c364_gauss_reduction_sympy_crosscheck.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c364_gauss_reduction_replay.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c364_gauss_reduction_mutation.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c364_release_manifest.py
```

The checked receipt currently contains 469 discriminants, 5,387 states, 775 cycles, 11,256 fixed-power rows, 117,887 independent checker assertions, 3,403 SymPy identities, and 47/47 rejected hostile mutations. Release metadata and PDF digests are owned by `C364_RELEASE_MANIFEST.json` after final closure.

Finite computation is a convention and regression receipt only. The infinite family is proved in `THEOREM_PACKAGE.md` and `paper/main.pdf`.
