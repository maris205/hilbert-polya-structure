# C197 hostile audit

## Attacks considered

1. **Wrong reflection order.**  Swapping `R_VR_U` reverses every generic
   rotation.  The off-diagonal projector checker detects this.
2. **Missing fixed component.**  `U-perp intersection V-perp` is fixed even
   though it is not feasible.  Composite models include two such dimensions.
3. **Endpoint laundering.**  `lambda=2` is orthogonal, not contracting.  It is
   isolated in theorem, evidence and Route grading.
4. **Rate overstatement.**  The rate includes mismatch directions as well as
   generic principal angles.  The theorem states the maximum and its boundary.
5. **Finite-grid overreach.**  Rational Pythagorean blocks do not prove the
   all-subspace theorem; the proof is decomposition-based.
6. **Determinant ownership.**  `det(I-zT_lambda)` is a finite algorithmic
   determinant, not an Artin--Mazur or target Fredholm determinant.
7. **Proves-too-much control.**  Prime and composite dimensions and arbitrary
   angles obey the same theorem, killing any arithmetic interpretation.
8. **Hash-only integrity.**  Mutations repair the payload hash before testing,
   so semantic checking is required.

## Outcome

No tested attack survives.  The source theorem ownership and strict Route-A
failure remain explicit.  This internal audit is not external peer review.
