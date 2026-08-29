# Experiment and evidence plan — C225

## Claim-led work units

1. **Finite generator:** encode endpoint diagonals exactly and verify row sums,
   detailed balance, and the `K=0` convention.
2. **Jacobi spectrum:** independently reconstruct the Robin sine modes, all
   eigenvalues, norms and residuals for four exact rate pairs and
   `K∈{1,2,4,8}`.
3. **Transient law:** reassemble every tested `P_t(i,j)` at three rational
   times and audit stochasticity, nonnegativity and reversibility.
4. **Mixing:** compute exact TV distances and compare to the reversible gap
   bound for every kernel row.
5. **Boundary atlas:** record zero-rate absorbing faces and capacity-limit rows
   for subcritical, critical, supercritical and asymmetric rates.

## Independent controls

The checker does not import producer functions.  SymPy verifies the generator,
Jacobi similarity, endpoint recurrence, orthogonality and a Chebyshev
characteristic factor.  A clean subprocess replay must be byte-identical.
Twenty-five repaired-hash mutations (including two unknown-key mutations) and a
stale-hash mutation must all fail.  The release manifest checks the exact
27-payload closure and deterministic three-revision PDF chain.

## Stop conditions

No target arithmetic, target divisor, Euler product, root number, automorphy,
or Route-B invocation is permitted.  If a proposed infinite-chain statement
requires a continuous-spectrum claim, it is removed rather than extrapolated.
