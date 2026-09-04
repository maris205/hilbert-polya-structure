# Source audit

## Classical input

The package uses three standard results: Dedekind's good-prime
factorization/cycle correspondence, the discriminant criterion for the
alternating subgroup, and Chebotarev's density theorem.  Serre and Neukirch
are cited for the number-field framework; Lidl--Niederreiter is cited for
finite-field Frobenius and factorization.  No priority claim is made.

## Package-owned derivation

The following quartic-specific calculations are reproduced rather than
imported as opaque data:

- `disc(x^4-x-1)=-283`;
- irreducibility of `x^4+x+1` over `F_2`;
- the five displayed modular factorizations at 2, 7, 17, 71, and 83;
- the group-order proof that the Galois group is `S4`;
- the specialization of the fixed-point, primitive-orbit, determinant, and
  self-adjointness identities to each of the five `S4` cycle classes;
- the repeated-root factorization and derivative gcd at 283;
- exhaustive exact factor signatures for primes at most 10,000.

## Evidence boundary

The finite grid verifies the implementation and supplies witnesses.  It is
not used to infer irreducibility, a Galois group, or asymptotic densities.
Those conclusions follow from exact arguments and classical theorems.

## Collision audit

C12A already owns the universal zero-dimensional mechanism: on every reduced
finite fiber Frobenius is a finite permutation, its iterate counts are traces,
and its local zeta is the reciprocal finite permutation determinant.  C12A
also records that this cyclotomic, nilpotent-blind identity is nondiagnostic
by itself.  C369 does **not** reclaim that mechanism.  Its owner is restricted
to `x^4-x-1`: the `S4` Galois proof, the five-class all-good-prime
factor/fixed/primitive/density atlas, the non-étale boundary at `p=283`, and
the convention-locked executable ledger.

C19 concerns a period-seven Hénon curve and a two-axis time/Frobenius
problem.  C41 concerns a CM elliptic cohomological factor.  C172 concerns a
primitive finite-field multiplier on field elements, with a fixed point and
a large cycle, rather than an `S4` root fiber varying over rational primes.
C56 owns a degree-27 finite-etale Fano line scheme, its `W(E6)` normal-closure
action, and selected Frobenius cycle witnesses.  It does not give the
all-good-prime factor/fixed/primitive/density atlas for one quartic root
scheme that is owned here.
C364 concerns a finite Gauss reduction permutation with no rational-prime
fiber.  C369 is instead the complete zero-dimensional quartic root-scheme
permutation atlas.  That quartic-specific atlas, rather than the universal
finite-permutation determinant mechanism, is its distinct theorem owner.
