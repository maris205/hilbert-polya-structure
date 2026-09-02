# HCS-C300 — complete isothermal Euler Riemann solver

This package proves the unique positive-density self-similar Lax entropy
solution for every one-dimensional isothermal Euler Riemann datum at sound
speed `a>0`.  A single strictly increasing scalar equation determines the
intermediate state and all four shock/rarefaction patterns.  Exact fan
profiles, shock speeds, Lax inequalities, convex entropy, vanishing waves,
the no-vacuum theorem and the singular pressureless boundary are closed in
one paper.

The theorem is independent of C195's periodic viscous scalar Burgers owner.
Its strict Route-A tuple is
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`; overall
`ROUTE_A_REJECTED`; Route B is locked under
`NO_BAD_EULER_OR_ROOT_NUMBER`.

## Artifacts

- `THEOREM_PACKAGE.md`: assumptions, scalar solver, all wave formulas and
  analytic proof.
- `paper/main.pdf`: final manuscript; Rounds 0--2 are retained beside it.
- `results/c300_euler_evidence.json`: canonical exact and high-precision
  branch receipts.
- `evaluations/route_a/HCS-C300/2026-09-02.yaml`: strict Route-A evaluation.
- `code/`: producer, independent checker, symbolic cross-check, replay,
  hostile mutations and release closure.

## Reproduce

```bash
python code/c300_euler_producer.py
python code/c300_euler_checker.py
python code/c300_euler_sympy_crosscheck.py
python code/c300_euler_replay.py
python code/c300_euler_mutation.py
python code/c300_release_manifest.py
```

The release manifest contains exactly 27 payloads and excludes itself from
its content hash.  Finite cases are regression evidence; the arbitrary-data
theorem is analytic.
