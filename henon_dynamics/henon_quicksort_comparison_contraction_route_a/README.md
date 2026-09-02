# HCS-C302 — Quicksort comparison-cost contraction law

This package gives the exact comparison-count probability-generating
polynomial recurrence for randomized single-pivot Quicksort at every input
size, derives its mean and variance in closed form, and proves convergence of
the exactly centered normalized costs to the unique finite-variance
contraction fixed point.  The exact third centered moment
`16 zeta(3)-19>0` proves that the limit is non-Gaussian.

Two proof gaps are closed explicitly: changing finite subproblem sizes are
handled on one iid-uniform binary tree by a weighted cutoff/limsup inequality,
and the fixed point is proved to lie in `L3` by a Rosenthal-controlled tree
series before its third moment is taken.

The theorem fixes distinct keys, a uniform pivot rank, `n-1` pivot
comparisons and comparison-only cost.  Its strict Route-A tuple is
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`; overall
`ROUTE_A_REJECTED`; Route B is locked under
`NO_BAD_EULER_OR_ROOT_NUMBER`.

## Artifacts

- `THEOREM_PACKAGE.md`: finite recurrence/moments, contraction proof and
  non-Gaussian moment certificate.
- `paper/main.pdf`: final paper; Rounds 0--2 are retained beside it.
- `results/c302_quicksort_evidence.json`: canonical exact PGF and integral
  receipts.
- `evaluations/route_a/HCS-C302/2026-09-02.yaml`: strict Route-A evaluation.
- `code/`: producer, independent checker, symbolic cross-check, replay,
  hostile mutations and release closure.

## Reproduce

```bash
python code/c302_quicksort_producer.py
python code/c302_quicksort_checker.py
python code/c302_quicksort_sympy_crosscheck.py
python code/c302_quicksort_replay.py
python code/c302_quicksort_mutation.py
python code/c302_release_manifest.py
```

The release manifest closes exactly 27 payloads and excludes itself.  Finite
coefficient tables are regression evidence; the all-size recurrence and
limit theorem are analytic.

The certificate contains 13 PGFs with 173 nonzero coefficient cells and 527
centered pivot rows.  The independent checker exhausts every permutation
through `n=9`; the symbolic lane verifies mean/variance recurrences through
`n=80` and rederives the beta-integral moment identity.
