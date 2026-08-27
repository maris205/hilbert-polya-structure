# Source audit

## Frozen owner, clock and normalization

The owner is the minimal nonexplosive continuous-time Markov branching chain
on `N_0` with per-particle birth rate `lambda`, per-particle death rate `mu`,
absorbing state zero, physical time `t`, and deterministic initial population
`z`. Its generator and branching normalization are part of the source lock.

The one-ancestor probability generating function is `F_t(s)=E_1[s^Z_t]`;
the `z`-ancestor PGF is `F_t(s)^z`. Off criticality the finite exact clock is
`delta=exp(-(lambda-mu)t)`. At `lambda=mu`, using that coordinate would create
a removable singularity, so the critical clock is `tau=lambda*t`. Neither
coordinate is observational data.

## Original source lock checked

- S. Karlin and J. McGregor, *Linear Growth, Birth and Death Processes*,
  Stanford University Technical Report **KAR ONR 3**, January 1958. The
  official Stanford record is
  [statistics.stanford.edu/technical-reports/linear-growth-birth-and-death-processes](https://statistics.stanford.edu/technical-reports/linear-growth-birth-and-death-processes),
  with persistent repository record
  [purl.stanford.edu/fx071vs8733](https://purl.stanford.edu/fx071vs8733).

The package gives a self-contained derivation and exact certificate. It does
not claim historical priority for the process, transition formula, branching
property, quasi-stationary law, Yaglom limit or martingale limit, and it does
not report external peer review.

## Collision and scope audit

Earlier finite birth--death operators in the repository, including the finite
Ehrenfest/Krawtchouk owner, have a finite state space, stationary spectral
normalization and a different theorem target. C208 owns the absorbing,
unbounded-state branching chain, its arbitrary-initial-population transition,
and all three survival/extinction scaling regimes. The C204--C207 objects use
finite-field iteration, a context-free shift, a shear PDE, and nonlinear
diffusion respectively; their clocks and phase spaces do not collide with
C208.

The scope literal is `NO_BAD_EULER_OR_ROOT_NUMBER`. No target zero or prime
table, arithmetic local datum, Euler factor, root number, automorphy object,
target divisor or functional equation, Hilbert--P\'olya operator, or Route-B
input is used. A probability generating function is explicitly not renamed a
dynamical zeta.
