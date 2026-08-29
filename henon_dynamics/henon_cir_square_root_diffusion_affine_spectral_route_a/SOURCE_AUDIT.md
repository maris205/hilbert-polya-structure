# Source and claim audit — C229

## Frozen source

- SDE: `dX_t=kappa(theta-X_t)dt+sigma sqrt(X_t)dW_t` on `[0,infinity)`;
- generator: `kappa(theta-x) d/dx + (sigma^2/2)x d^2/dx^2`;
- clock: physical diffusion time;
- parameters: all nonnegative values, with interior formulas restricted to
  `kappa,theta,sigma>0`;
- source lock: `e1dc522e054c2d0ded74b017bc52c7b016a52c59`.

## Allowed evidence

Only the vector field, scale/speed boundary integrals, Riccati solution,
noncentral-χ² law, Gamma density, Laguerre identities, and finite rational
regression rows are used.  The producer does not read any target arithmetic or
external data file.

## Negative controls

The checker rejects altered Feller sides, boundary classes, transform values,
Gamma moments, eigenvalues, gap factors, atom masses, provenance and scope
flags even after a mutant recomputes the payload hash.  Route-A labels remain
strict: no primitive orbit owner, arithmetic clock, target determinant or
unitary lift is asserted.

## Citation boundary

The bibliography names the original CIR model and standard one-dimensional
diffusion references for context.  They are not used as hidden numerical data.
