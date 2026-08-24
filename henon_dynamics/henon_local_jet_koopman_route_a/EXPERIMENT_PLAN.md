# Experiment plan — C114

## Frozen objects

- map germ: \(F(u,v)=(u^2+3u/2-v/2,u)\);
- base point: \((0,0)\);
- quotient: \(A_4=\mathbb Q[u,v]/(u,v)^5\);
- basis: monomials of total degree at most four, degree first and descending
  exponent of \(u\) within each degree;
- matrix convention: column \(j\) is the coefficient vector of \(K(b_j)\);
- release scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Gates

1. Construct all 225 matrix cells by exact truncated polynomial arithmetic.
2. Extract the five total-degree diagonal blocks and verify their rational
   traces, determinants, and eigenvalue multisets.
3. Compute the full trace, determinant, eight trace powers, characteristic
   polynomial, and \(\det(I-zK)\).
4. Rebuild the linearized pullback and certify that the nonlinear correction
   is nonzero, strictly degree raising, and nilpotent.
5. Run an independent checker that imports no producer code.
6. Run a separate direct SymPy expansion.
7. Verify canonical JSON replay and reject at least eight hostile mutations.
8. Compile the paper twice in isolated fixed-date directories, compare bytes,
   inspect fonts and logs, and close a content-addressed manifest.

## Failure conditions

- any non-rational or untracked matrix entry;
- a basis-order or matrix-convention ambiguity;
- disagreement between producer, independent checker, or SymPy;
- a hostile mutation accepted by the checker;
- non-deterministic PDF bytes, unembedded fonts, unresolved references, or
  material TeX warnings;
- language that upgrades the finite local determinant to a global Fredholm
  determinant or introduces forbidden arithmetic/Route-B claims.
