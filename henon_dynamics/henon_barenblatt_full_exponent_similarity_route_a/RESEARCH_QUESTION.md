# Research question

For every exponent `m>0` and mass `M>0`, can one give a single exact theorem
that classifies all centered, nonnegative, integrable first-kind similarity
profiles of the one-dimensional equation `u_t=(u^m)_{xx}` whose `F^m` is
locally absolutely continuous and whose zero-flux law holds almost everywhere,
and records every regime boundary without silently crossing the singular value
`m=1`?

The package answers yes in this deliberately narrow class.  It derives the
profile ODE from mass-preserving similarity scaling, fixes the unique mass
normalization, and proves:

- compact support and a moving free boundary for `m>1`;
- the Gaussian at `m=1`;
- algebraic tails for `0<m<1`;
- exact absolute-moment formulae and the threshold
  `r<(1+m)/(1-m)` in fast diffusion;
- logarithmic divergence at equality, including the second-moment boundary
  `m=1/3`;
- the stationary rescaled equation and its dissipation identity only where
  regularity, finite energy, and boundary decay justify it.

The energy is not left implicit: for `m!=1` it is
`integral(v^m/(m-1)+alpha*xi^2*v/2)`, while at `m=1` it is
`integral(v log(v)-v+xi^2*v/4)`.

It does **not** classify arbitrary Cauchy solutions, signed solutions,
translations, higher-dimensional profiles, or nonlinear long-time
asymptotics.  Centering removes the translation parameter, and zero flux is
part of the hypothesis rather than a conclusion about every weak solution.
