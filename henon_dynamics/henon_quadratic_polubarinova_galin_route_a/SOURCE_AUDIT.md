# Source audit

## Primary lineage

1. S. Richardson, *Hele Shaw flows with a free boundary produced by the
   injection of fluid into a narrow channel*, Journal of Fluid Mechanics 56
   (1972), 609--618. DOI:
   [10.1017/S0022112072002551](https://doi.org/10.1017/S0022112072002551).
   This is cited for classical injected Hele--Shaw moment-method lineage, not
   as a source for the package's exact degree-two endpoint theorem.

2. B. Gustafsson, *The string equation for polynomials*, Analysis and
   Mathematical Physics 8 (2018), 637--653. DOI:
   [10.1007/s13324-018-0239-3](https://doi.org/10.1007/s13324-018-0239-3).
   This is the direct source boundary for the polynomial
   Polubarinova--Galin/string-equation setting and normalization context.

3. B. Gustafsson and Y.-L. Lin, *On the dynamics of roots and poles for
   solutions of the Polubarinova-Galin equation*, Annales Academiae
   Scientiarum Fennicae Mathematica 38 (2013), 259--286. DOI:
   [10.5186/aasfm.2013.3802](https://doi.org/10.5186/aasfm.2013.3802).
   This supplies nearby polynomial-solution and root/pole dynamics context.

## What is derived locally

The Fourier coefficient equations, the coefficient ODE, conservation of
`a^2 b`, the scalar reduction `M0=F(u)`, the sharp first-cusp time, and the
rotated semicubical expansion are all derived directly in this package.  No
sentence attributes those formulas to a source unless the source is actually
being used as lineage.

## Workspace collision audit

The Route-A G0 scan covered the prior workspace candidates HCS-C1 through
HCS-C363.  The two closest retained geometric/free-boundary neighbors are
genuine separations, not omitted collisions:

- **C207** develops Barenblatt similarity profiles for scalar nonlinear
  diffusion, including pressure and support/free-boundary geometry.  It does
  not evolve a planar boundary through a time-dependent conformal map and
  does not use the Polubarinova--Galin boundary equation.
- **C360** develops the homogeneous Ricci flow of Berger metrics on
  `SU(2)`, including metric-cone, curvature, and extinction geometry.  It is
  an intrinsic metric flow, not a Polubarinova--Galin conformal-map boundary
  evolution.

Within the present C364--C368 batch, C364 is a finite Gauss-reduction
permutation, C366 a finite Krawtchouk XX spin chain, and C367 a reflected
Markov-fluid queue.  Those three entries are recorded only as same-batch
separation checks; C207 and C360 are the actual nearest neighbors supplied by
the prior-workspace scan.

## Evidence and novelty discipline

DOI metadata was checked against primary publisher/Crossref records.  No
priority or exhaustive-literature claim is made.  The package's contribution
is scoped as a self-contained complete atlas for the normalized quadratic
subfamily, not as a claim that degree-two Laplacian growth has never appeared
before.

No target arithmetic source, Euler factor, root number, automorphy result,
target divisor, target zero set, or Hilbert--Pólya construction was consulted
or claimed.
