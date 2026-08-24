# Source audit — C114

## Source basis

This package is a self-contained exact calculation.  It uses only:

- the frozen polynomial formula printed in every artifact;
- rational polynomial arithmetic in the quotient by monomials of total
  degree at least five;
- elementary finite-dimensional linear algebra;
- independently reconstructed SymPy identities as a software cross-check.

No external dataset, scraped table, unpublished communication, or imported
orbit ledger is used.  No literature statement is needed for the finite
identities proved here, so the paper does not manufacture citations.

## Evidence ownership

The producer constructs the canonical JSON.  The checker independently
repeats the polynomial engine, basis order, matrix, graded blocks, traces,
determinants, and boundary verdict without importing the producer.  A separate
SymPy program reconstructs the same matrix directly from symbolic expansion.
The replay script verifies canonical bytes, and the hostile audit tests thirteen
independent corruptions against the checker.

## Boundary audit

The phrase “Koopman jet” means the induced pullback on the finite algebra
\(A_4\), not a global Koopman operator on a named analytic or Hilbert space.
The polynomial \(\det(I-zK)\) is an ordinary 15-dimensional determinant.  It
is not called a Fredholm determinant.  No arithmetic/local data, Euler factor,
root number, automorphy statement, Riemann-zero correspondence, or
Hilbert--Pólya operator enters the package.  Scope literal:
`NO_BAD_EULER_OR_ROOT_NUMBER`.
