# Experiment Plan

## Claim-driven objective

Test the exact theorem and its sharp boundaries for the three signed H6
minimal polynomials inherited from HCS-P48.

## Protocol

1. Hash-lock HCS-P46, P47, and P48 dependencies.
2. Use the signed period-three polynomial $f_{-L_3}(X)=f_{L_3}(-X)$.
3. For each primitive period and every $1\le n\le12$, compute
   `Res(f, X^n-1)` and `Res(f, Phi_n)` over the integers.
4. Verify the exact divisor product over every divisor of `n`.
5. For all `n>2`, verify that the primitive norm is a square and record its
   canonical half norm.
6. Check the actual determinant full-field norm as the square of the cyclic
   resultant.
7. Reject the false one-scalar power law with `A_2 != A_1^2`.
8. Run sharp controls:
   - `n=2`, where the half exponent is unavailable;
   - positive-modulus substitution for the negative period-three eigenvalue;
   - the nonreciprocal polynomial `X^2-2X+2`, whose index-three primitive norm
     is 13;
   - reducible-polynomial mutation.
9. Generate the paper table only from the frozen JSON result.

## Evidence labels

- Symbolic identities and theorem: `PROVED`.
- Finite resultant ledger: `NUMERICALLY_CERTIFIED` using exact integers.
- Period-four eventual primitive divisors: `PROVED` from Flatters' theorem in
  its exact real-quadratic norm-one scope.
- Cross-orbit prime-ideal assembly: `OPEN`.

## Stop rules

The experiment must not:

- replace the signed period-three eigenvalue by its modulus;
- extend the square theorem to `n=2`;
- call the full $K$-norm the minimal natural norm;
- infer a quartic primitive-divisor theorem from a quadratic source;
- infer an all-prime Euler trace from the occurrence of fresh divisors.
