# SD-C14 experiment plan

## Frozen tests

1. Prove and encode the positive circle-measure moment classification.
2. Audit cyclic approximants for every order 2--64 and repetitions 1--128.
3. Verify analytic and Fuglede--Kadison formulas at frozen complex points.
4. Locate the first Fourier leak of positive density perturbations.
5. Audit self-adjoint and recurrent balanced-word controls.
6. Repeat the analytic-determinant test on tensor-prime, composite-only, and
   seeded random-increasing inventories.

## Decision rules

- Exact nonzero moments with \(c>0\): `GO_INFINITE_HAAR_ESCAPE`.
- Analytic determinant independent of \(c\):
  `STOP_DETERMINANT_INVISIBILITY`.
- The same blindness for nonprime inventories: `PROVES_TOO_MUCH`.
- No target-zero or Route-B escalation is allowed.
