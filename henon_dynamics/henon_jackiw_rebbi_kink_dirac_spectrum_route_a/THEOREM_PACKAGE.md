# Theorem package

## Main theorem

For each integer `n >= 1`, let `A_n=d/dx+n tanh x` and
`H_n=[[0,A_n^*],[A_n,0]]` on `H^1(R;C^2)`.  Then:

- `H_n` is self-adjoint;
- `H_n^2` has scalar channels
  `-d^2+n^2-n(n+1)sech^2 x` and
  `-d^2+n^2-n(n-1)sech^2 x`;
- its essential spectrum is `(-infinity,-n] union [n,infinity)` and its continuous part is purely absolutely continuous;
- the point spectrum consists of a simple upper-component zero mode proportional to `sech^n x` and the simple pairs
  `+/-sqrt(j(2n-j))`, `j=1,...,n-1`;
- both thresholds are resonant, neither is an `L^2` eigenvalue;
- the integer Pöschl--Teller channels, hence the Dirac problem, are reflectionless.

## Proof dependencies

1. Bounded-perturbation self-adjointness.
2. Direct first-order factorization.
3. Shape invariance with shift `2n-1`.
4. Inductive Darboux construction and descent-to-free exhaustion.
5. `ker A_n=span{sech^n}` and `ker A_n^*=0` in `L^2`.
6. Spectral pairing on every positive squared eigenspace.
7. Raised free zero-momentum and plane-wave solutions.
8. The normalized Darboux map `U_m=D_m product(B_0+r^2)^(-1/2)` is unitary from free `L^2` onto the continuous subspace; its orthogonal complement is exactly the `m`-state bound span.

## Proof status

All items are proved in `paper/main.pdf`.  The exact JSON and SymPy lanes check indexing and conventions but are not cited as proof of the infinite theorem.
