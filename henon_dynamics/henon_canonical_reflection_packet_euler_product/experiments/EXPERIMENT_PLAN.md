# Experiment plan

All decisive checks are exact.

1. Compute odd primitive counts through period 41 by Möbius inversion.
2. Independently recover them by divisor subtraction from fixed counts.
3. Expand the unweighted Euler product through order 41.
4. Recover `z Z'/Z` from product coefficients and compare with the direct
   primitive/repetition divisor sum.
5. Record high-precision boundary diagnostics only as diagnostics.
6. Run eight unit tests in normal and optimized Python.
7. Reject 25 mutations, including fake meromorphic, Lind-zeta, arithmetic,
   and Route-B promotions.
