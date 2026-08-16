# Results

## Exact analytic result

- Full complex poles:
  `alpha_(m,k)=2^(-1/(2m))*exp(pi*i*k/m)`, `0<=k<2m`.
- Principal coefficients:
  `b_(m,k)=c_m*(-1)^k/(sqrt(2)m)`.
- Raw pole family: not absolutely summable, already at `t=0`.
- Regularization: subtract Taylor degrees `0,...,m-1` from every level-`m`
  pole; the subtraction sums to zero within the level.
- Convergence: the regularized double series is absolutely normally
  convergent on compact punctured subsets and is independent of every pole
  enumeration.
- Exact tail: the regularized pole sum equals
  `L(t)=sum_(m>=2)c_m Phi(t^m)`.
- Exact counterterm, with `w=1+sqrt(2)t`:

      K_all=exp(3/2)w^(1/2)exp(-3/(4w))exp(L),
      K_all C_rel=1.

## Claim boundary

The result is an exact analytic renormalization obtained by copying the
complete channel ledger.  No transfer or self-adjoint operator, rational
prime meaning, von-Mangoldt amplitude, explicit formula, or Route-B result is
claimed.

## Reproducibility

The main certificate, independent reconstruction, double-mode test suite,
and sealed PDF are generated or checked by `bash code/run_c73.sh` and the
documented four-pass LaTeX build.
