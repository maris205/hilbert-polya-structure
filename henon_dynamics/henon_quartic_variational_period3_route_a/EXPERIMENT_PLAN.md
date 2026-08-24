# Exact experiment plan — C120

## Objective

Produce a deterministic finite certificate for one primitive period-three
orbit of a quartic variational map, including both tangent and action data.

## Gates

1. Freeze the map, potential, generating convention, reversor, orbit word,
   chronological multiplication order, and scope firewall.
2. Derive determinant, inverse, reversibility, and generating relations over
   the polynomial ring.
3. Verify all three fixed points and every transition of the three-cycle.
4. Multiply `B(-1)B(1)B(0)` in chronological order and derive
   `det(I-zM)`.
5. Evaluate the cyclic action, gradient, Hessian, determinant,
   characteristic polynomial, exact algebraic eigenvalues, and Morse index.
6. Run three negative controls: nearby parameter, deleted cubic, and
   noncyclic word.
7. Apply the canonical Route-A evaluator and explicitly test the absence of a
   target prime correspondence, source-owned A2 object, and target divisor.
8. Recompute independently, cross-check symbolically, require canonical
   replay, and reject hostile mutations.
9. Compile the paper twice under a fixed date; require byte identity, embedded
   fonts, clean final log, and a hash-closed manifest.

## Acceptance criteria

- all arithmetic exact in `Q` or `Q(sqrt(3))`;
- cycle primitive and action critical point nondegenerate;
- all three controls fail with explicit nonzero residuals;
- checker imports no producer module;
- all 21 mutations rejected;
- canonical tuple `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)` checked in
  producer, independent checker, symbolic audit, and hostile mutations;
- no forbidden global, arithmetic, spectral, or Route-B claim.

## Failure interpretation

A failed structural identity invalidates the model receipt. A failed control
invalidates the intended attribution. A failed independent or replay test
blocks release. None of these failures may be reframed as a mathematical
discovery without a new frozen question and evidence package.
