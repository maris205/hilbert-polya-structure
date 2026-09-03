# Claim-driven verification plan

## Claims

1. `H_n` is self-adjoint on `H^1(R;C^2)` and generates a unitary group.
2. Squaring gives the two stated shifted Pöschl--Teller operators.
3. The zero mode is unique and the nonzero point spectrum is exactly `+/-sqrt(j(2n-j))`, `1 <= j <= n-1`.
4. `+/-n` are resonances but not eigenvalues; the remaining spectrum is purely absolutely continuous.
5. Integer-height scattering is reflectionless.

## Analytic route

- Use bounded perturbation of the free Dirac operator for self-adjointness.
- Compute `A_n^*A_n` and `A_nA_n^*` exactly.
- Use `A_nA_n^*=A_{n-1}^*A_{n-1}+2n-1` inductively.
- Intertwine any hypothetical missing eigenstate down to the free operator to prove exhaustion.
- Raise the free plane wave and the free zero-momentum solution to obtain Jost and threshold states.
- Transfer positive scalar eigenspaces through `A_n` to the two Dirac energy signs.

## Independent computational lanes

- canonical producer over `0 <= n <= 24` and six rational momenta;
- producer-independent exact checker;
- symbolic factorization, ladder, threshold, and chiral-symmetry checks;
- two-directory byte replay;
- repaired-hash hostile mutation suite;
- deterministic three-round PDF rebuild, font, text, and raster checks.

Finite computation is explicitly a receipt, not the all-integer proof.
