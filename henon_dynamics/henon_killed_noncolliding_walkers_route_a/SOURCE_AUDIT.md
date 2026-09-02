# Source and claim audit

## Primary ownership

- Samuel Karlin and James McGregor, “Coincidence probabilities,” *Pacific
  Journal of Mathematics* 9 (1959), 1141–1164,
  DOI `10.2140/pjm.1959.9.1141`.  Ownership role: determinant probability for
  noncoincident birth–death paths.
- J. N. Darroch and E. Seneta, “On quasi-stationary distributions in absorbing
  continuous-time finite Markov chains,” *Journal of Applied Probability* 4
  (1967), 192–196, DOI `10.2307/3212311`.  Ownership role: finite
  continuous-time QSD context.

The manuscript does not claim priority for either theorem family.  The
workspace contribution is a self-contained specialization that closes the
full spectrum, absorption sums, boundary cases, and deterministic certificate
for the frozen model.

## Claim-to-evidence boundary

The complete theorem for arbitrary `L,k,t` is proved in `THEOREM_PACKAGE.md`
and `paper/main.tex`.  The JSON atlas stops at `L=8`; exact SymPy
characteristic polynomials stop at `L=5`.  Decimal strings are diagnostics,
not interval proofs.  No empirical result is used to extend a theorem.

## Negative-claim audit

The Karlin--McGregor determinant is a stochastic transition kernel, not a
target completed determinant.  Physical jump time is not an arithmetic prime
clock.  The symmetric finite generator motivates only `A4_FORMAL_HINT`; it is
not a same-clock target-zero lift.  No local arithmetic data, Euler factor,
root number, automorphy, target divisor/counting law, target functional
equation, target zero match, or Hilbert--Pólya operator is asserted.  Route B
is not invoked.
