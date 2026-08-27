# Source audit

## Frozen owner and clock

The owner is the canonical conservative/no-flux solution of the displayed
Jacobi SDE on `[0,1]`.  For `0<alpha<1` or `0<beta<1`, the interior differential
expression alone would allow other boundary extensions, so the realization is
part of the source lock.  The generator has no prefactor `1/2`; formulas from
the usual population-genetics clock are doubled.

## Primary and official sources checked

- C. L. Epstein and R. Mazzeo, *Wright--Fisher Diffusion in One Dimension*,
  SIAM J. Math. Anal. 42 (2010), DOI
  [10.1137/090766152](https://doi.org/10.1137/090766152): zero-flux
  realization, semigroups and endpoint asymptotics.
- Y. S. Song and M. Steinrücken, *A Simple Method for Finding Explicit
  Analytic Transition Densities...*, Genetics 190 (2012), DOI
  [10.1534/genetics.111.136929](https://doi.org/10.1534/genetics.111.136929):
  Beta speed density, complete Jacobi basis, boundary condition and the
  one-half-clock eigenvalues.
- R. C. Griffiths, *A Transition Density Expansion for a Multi-Allele
  Diffusion Model*, Adv. Appl. Probab. 11 (1979), DOI
  [10.2307/1426842](https://doi.org/10.2307/1426842): neutral transition
  density expansion.

The package claims a self-contained synthesis and exact certificate, not
historical priority or external peer review.

## Collision and scope audit

C171 is a finite Ehrenfest/Krawtchouk birth--death operator; C186 uses Jacobi
elliptic functions for the Euler top.  Neither owns this continuous-state
degenerate diffusion.  The scope literal is `NO_BAD_EULER_OR_ROOT_NUMBER`.
No prime table, target zero, arithmetic local datum, Euler factor, root number,
automorphy object, target functional equation, or Route-B object is used.
