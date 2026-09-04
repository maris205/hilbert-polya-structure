# HCS-C358: May--Leonard cyclic competition

This package proves a complete all-orbit trichotomy in the strict cyclic
competition chamber:

- global coexistence below `a+b=2`;
- an exact logistic normalization, periodic simplex foliation and elliptic
  period at `a+b=2`;
- the diagonal stable-manifold exception and full attracting oriented
  heteroclinic cycle above `a+b=2`.

The canonical evidence is
`results/c358_may_leonard_evidence.json`; the complete proof is
`THEOREM_PACKAGE.md`; the final paper is [paper/main.pdf](paper/main.pdf).

Run all release gates with:

```bash
python -B code/c358_release_manifest.py
```

The strict Route-A tuple is
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`.  The package is source-local,
uses scope `NO_BAD_EULER_OR_ROOT_NUMBER`, rejects Route A, and keeps Route B
locked.
