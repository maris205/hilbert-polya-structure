# Hostile audit

## Mathematical attacks

- **Replacing the field line by one cover:** rejected.  Some quadratic lifts lie in `F_q^*`, others in the norm-one torus.  The theorem uses both.
- **Forgetting inversion:** rejected.  A field point has the inverse pair of lifts; Burnside corrections appear explicitly.
- **Double-counting ramification:** rejected.  The two covers meet at order `gcd(2,q-1)`; one or two branch values are subtracted in every quotient formula.
- **Treating characteristic two as odd:** rejected.  `+2=-2`, both cover orders are odd, and the branch correction collapses to one.
- **Claiming uniform quotient trees:** rejected.  Uniform power-map trees live upstairs; downstairs the labeled inversion quotient retains regular pairs and special folded branch components.
- **Inferring Jordan blocks from eigenvalue multiplicity:** rejected.  Exact zero blocks use the second differences of all image ranks.
- **Using finite samples as proof:** rejected.  The proof is the exact graph conjugacy plus cyclic subgroup formulas.

## Independence and integrity

The independent checker has its own polynomial irreducibility test, field-model consistency lock, finite-field arithmetic, Chebyshev recurrence, quotient formulas and direct orbit traversal.  It imports no producer.  Fresh replay is byte exact.  Forty-one repaired-hash mutations all fail, including replacement of the `q=4,d=0` irreducible modulus `[1,1,1]` by reducible `[1,0,1]`.  Both DOI records and their claim contexts were checked on publisher or author-primary pages.

## Route and claim boundary

Finite-field arithmetic is intrinsic but does not select rational primes as primitive cycles or produce a `log p` clock.  The source zeta is finite and rational.  The source Koopman matrix is canonical but generally nonnormal, so it supplies only `A4_FORMAL_HINT`; no self-adjoint realization is constructed.  No target datum, Euler factor, root number, automorphy statement, target divisor, functional equation, self-adjoint Hilbert–Pólya operator or Route-B input appears.  Audit verdict: **PASS within `NO_BAD_EULER_OR_ROOT_NUMBER`**.
