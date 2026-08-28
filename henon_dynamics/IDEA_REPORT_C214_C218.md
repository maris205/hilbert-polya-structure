# Route-A idea report: C214--C218

Date: 2026-08-28

Source commit: `077a098ac5811e465b69db71b5e6031a4827eb55`.

Evaluator: `flow_systems/skills/route-a-evaluator.md`, v0.2.0, SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.

Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Design objective

This round again interprets one paper as one complete theorem-scale advance.
The five owners are a renewal diffusion with Poisson resets, an exchangeable
genealogical pure-death process, a singular celestial Hamiltonian flow, a
conservative geophysical wave PDE, and a mixed hyperbolic--parabolic damping
PDE.  They have different phase spaces, clocks and source operators.  No
coordinate, determinant or Route score is transferred between them.

`NEW` below means only that the frozen owner is absent from the existing
workspace packages.  It is not a literature-priority claim.  Classical
results retain their source attribution; the retained increment is a
convention-locked all-parameter synthesis, complete singular/boundary atlas,
independently replayable evidence, finished paper and strict Route-A decision.

## Collision scan, kills and pivots

- Ordinary rowmotion was rejected again because its rectangle rotation and
  cyclic-sieving owner sits too close to the existing necklace, tableau and
  Kreweras packages.  Sandpiles on cycles or complete graphs are already
  strict slices of C176.
- Scalar Riccati and Kalman--Bucy proposals were rejected because their
  projective/Moebius reduction overlaps C189 and the positive-cone line around
  C191.  Random-to-top and top-to-random proposals remain inside the already
  dense finite Markov-spectrum lane.
- A McKendrick renewal semigroup was rejected because it would simultaneously
  overlap the existing renewal, delay and branching owners.  Integrate-and-
  fire was rejected as an affine reset/roof near-neighbor of C212.
- Brownian resetting survives because the owner is a continuous diffusion
  rebuilt at Poisson renewal times, with a source renewal transform,
  nonequilibrium stationary density, first-passage transform and an exact
  optimal-reset theorem.  Its Laplace-transform denominator is never called a
  dynamical zeta.
- Kingman's coalescent survives because the partition-valued genealogy and its
  all-sample projective consistency are not the birth--death branching process
  of C208.  Its block-count chain is only a lumped certificate of that owner.
- The Kepler problem was previously deferred because its regularization
  constants demanded a separate audit.  It is retained now only after freezing
  the planar convention, limiting the claim to the conic/action/scattering
  atlas and the explicitly derived Levi--Civita configuration regularization.
  No full Ligon--Schaaf symplectomorphism is re-proved or claimed.
- Rotating shallow water is constant-`f` dynamics on the two-torus.  It does
  not import beta-plane Rossby waves.  Kelvin--Voigt damping is retained for
  its slow spectral branch and essential accumulation; it is not the ordinary
  damped-wave/telegraph block of C213.

No retained system intrinsically labels primitive trajectories by rational
primes, realizes prime powers as their repetitions, or generates `log p` as a
source clock.  Exact transforms, characteristic polynomials and modal spectra
remain source-local.

## Frozen independent theorem increments

### C214 -- Brownian diffusion with Poisson resetting

For diffusivity `D>0`, reset rate `r>0`, reset/start point zero and absorbing
target `a>0`, close the free propagator renewal and its Laplace stationary
density.  Derive the survival and first-passage Laplace transforms, every
moment they determine, the exact mean first-passage time, and the unique
positive optimal dimensionless rate solving `z=2(1-exp(-z))`.  Zero reset,
zero target and zero diffusion are separate boundary branches.

### C215 -- Kingman genealogy, absorption and tree length

For every sample size, freeze the partition-valued Kingman coalescent in which
each block pair merges at rate one.  Prove the lumped block-count pure-death
chain with rates `binom(k,2)`, its all-time hypoexponential transition law and
independent holding-time representation.  Close the MRCA Laplace transform,
moments and infinite-sample absorption limit, together with the total tree-
length transform, moments and exact distribution.  Exchangeability,
restriction consistency and the one-sample boundary remain explicit.

### C216 -- planar Kepler conics and collision regularization

For `H=|p|^2/2-mu/|q|`, `mu>0`, derive the energy, angular-momentum and
Runge--Lenz identities and classify every nonradial orbit as an ellipse,
parabola or hyperbola.  Close the negative-energy period and radial action,
the positive-energy scattering angle, and every circular/radial/collision
boundary.  On one fixed energy surface, the Levi--Civita substitution
`q=u^2`, `dt=|u|^2 d tau` gives its exact oscillator/hyperbolic equation and
configuration-level collision continuation.  Kepler degeneracy makes
sampled-time fixed energy shells continua, stopping an ordinary isolated-
orbit zeta.

### C217 -- rotating shallow-water Fourier flow

For constant Coriolis parameter and gravity-wave speed on the two-torus,
diagonalize every energy-normalized three-by-three Fourier block into one
geostrophic and two inertia--gravity modes.  Give the exact projectors and
unitary group, potential-vorticity split, lattice-shell multiplicities,
finite-support periodicity criterion and all zero-parameter/zero-wave-number
boundaries.  The infinite stationary kernel and unitarity give the precise
noncompact/Schatten stopping theorem.

### C218 -- Kelvin--Voigt wave spectral atlas

For the Dirichlet equation `u_tt-u_xx-b u_txx=0`, classify every mode for all
`b>=0`.  Close the finite underdamped sector, every critical Jordan mode, the
infinite overdamped sector, exact energy dissipation, slow/fast asymptotics,
and the non-eigenvalue essential spectral accumulation at `-1/b`.  The exact
spectral-abscissa gap is `min(b omega_1^2/2,1/b)` for positive damping, with a
unique optimal damping `sqrt(2)/omega_1`; the undamped boundary is separate.

## Frozen strict expectations

| paper | A0 | A1 | A2 | A3 | A4 | overall |
|---|---|---|---|---|---|---|
| C214 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FAIL` | `ROUTE_A_REJECTED` |
| C215 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FAIL` | `ROUTE_A_REJECTED` |
| C216 | `A0_FAIL` | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_NATURAL_QUANTIZATION` | `ROUTE_A_REJECTED` |
| C217 | `A0_FAIL` | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C218 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |

These are pre-release expectations, not transferred verdicts.  The final
tuple of each paper is governed by its own content-addressed evaluator record.
Every `route_b_invocation_allowed` value remains false.
