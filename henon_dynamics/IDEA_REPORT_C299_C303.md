# Route-A idea report: C299--C303

## Round objective and frozen baseline

The user requested another batch of exactly five independent papers, with a
large theorem-scale advance in every paper, broad variation among dynamical
subtypes, and Route A examined first.  The collision baseline is
`83c058259c02707d004fca2d6b1a4ebaf5036094`, the fixed date is 2026-09-02,
and the build epoch is `1788307200`.  Every candidate is evaluated under
`flow_systems/skills/route-a-evaluator.md` v0.2.0, SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`,
with literal scope `NO_BAD_EULER_OR_ROOT_NUMBER`.

The collision scan covered all C1--C298 package titles, both registries, the
recent idea reports, and direct text searches for each proposed owner.  It
rejected Lattes dynamics, CIR diffusion, the Euler top, Lyness maps, the
Ehrenfest urn, rotor-router dynamics, sandpiles, the Kac ring, Toda flow and
other models already owned in the workspace.  The five retained systems use
different state spaces and different proof mechanisms:

1. a viscous vorticity PDE and its self-similar radial reduction;
2. a strictly hyperbolic two-field conservation law;
3. a finite absorbing Markov chain on the partition lattice;
4. a recursive distributional algorithmic process;
5. a completely positive quantum dynamical semigroup on the Bloch ball.

`NEW` below means only that the workspace contains no package owning the
frozen theorem.  It is never a claim of priority in the literature.

## Frozen candidates

### C299 -- Lamb--Oseen radial self-similar vortex

**Owner.**  The two-dimensional incompressible Navier--Stokes vorticity
equation at viscosity `nu>0`, restricted only for the classification theorem
to finite-circulation radial forward self-similar solutions with age
`tau=t+t_0>0`.

**Large step.**  Derive the similarity ODE and prove that finite circulation,
regularity at the origin and decay at infinity force the Gaussian

`omega(r,t)=Gamma exp(-r^2/(4 nu tau))/(4 pi nu tau)`.

Close its Biot--Savart velocity, semigroup age law, circulation and vorticity
moments, exact enstrophy/palinstrophy dissipation, fixed-radius Lagrangian
motion and the exponential-integral angular displacement.  Treat the core,
zero-circulation, singular-age and `nu -> 0+` measure limits separately.

**Nearest collision.**  C206 studies Couette enhanced dissipation and C207
studies nonlinear Barenblatt diffusion.  Neither owns a radial
Navier--Stokes vortex, the cancellation of nonlinear advection, or its exact
Biot--Savart/Lagrangian atlas.

**Proof status.**  `PROVABLE AS STATED` for the explicitly frozen radial
forward self-similar class.  No uniqueness claim is made for arbitrary
two-dimensional or three-dimensional vortex-filament solutions.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`; overall Route A rejected.

### C300 -- positive-density isothermal Euler Riemann solver

**Owner.**  The one-dimensional isothermal Euler system

`rho_t+(rho u)_x=0`,
`(rho u)_t+(rho u^2+a^2 rho)_x=0`, `a>0`,

with arbitrary constant left and right states of strictly positive density.

**Large step.**  Prove that the two wave curves reduce the entire Riemann
problem to one strictly increasing scalar equation with a unique positive
intermediate density.  Give the unique self-similar Lax solution, all four
shock/rarefaction combinations, exact fan profiles, Rankine--Hugoniot speeds,
strict mechanical-entropy production, vanishing-wave boundaries, and the
theorem that finite velocity jumps never create vacuum in this isothermal
chamber.  Isolate the singular pressureless limit `a -> 0+`, where strict
hyperbolicity and this solver cease to be uniform.

**Nearest collision.**  C195 owns a periodic viscous scalar Burgers flow.
C300 is a genuinely two-component strictly hyperbolic system, and its four
wave-pattern atlas cannot be recovered by renaming a scalar Burgers
shock/rarefaction slice.

**Proof status.**  `PROVABLE AS STATED` for `a>0` and positive left/right
densities.  The paper does not import the solver unchanged to vacuum data or
to pressureless Euler.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`; overall Route A rejected.

### C301 -- parallel binary partition fragmentation

**Owner.**  Begin with the one-block partition of `[n]`.  At every integer
round, independently label every element in each current block by a fair bit
and split the block into its nonempty bit classes.

**Large step.**  Determine the exact transition kernel on the full partition
lattice, the distribution at every time, the complete triangular spectrum
with Stirling multiplicities, the determinant, and the exact absorption-time
law.  The process is equivalently the collision partition of independent
uniform `t`-bit words, yielding

`P(T_n <= t)=(2^t)_n/2^(tn)`

and the sharp lattice birthday window: if `n^2/2^t -> lambda`, the absorption
probability tends to `exp(-lambda/2)`.  Simultaneous splits, unsplit blocks,
the singleton case `n=1`, time zero and the dyadic lattice effect are
retained.  The theorem is frozen for `n>=1`; the empty set is only an optional
degenerate extension and is not used in any formula.

**Nearest collision.**  C215 is a coalescing chain, C276 studies a single
birthday orbit statistic, and C194 studies a carries semigroup.  None owns
this monotone refinement chain together with its all-time partition law and
full partition-lattice spectrum.

**Proof status.**  `PROVABLE AS STATED`.  Finite Bell-lattice enumeration is
regression evidence; the kernel, spectrum and threshold are analytic.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`; overall Route A rejected.

### C302 -- randomized Quicksort comparison-cost dynamics

**Owner.**  Classical single-pivot Quicksort on a uniformly random
permutation of `n` distinct keys, recording the total number `X_n` of key
comparisons.

**Large step.**  Close the exact recursive distribution and probability
generating polynomial for every `n`, derive the exact mean and variance, and
pass from the centered recurrence to the contraction fixed point

`Y = U Y_1 + (1-U)Y_2 + 1+2U log U+2(1-U)log(1-U)`.

Prove the centered `L^2` convergence, uniqueness in the centered finite
second-moment class, and non-Gaussianity through the exact positive third
moment.  Include empty/singleton arrays, extreme pivots, independence,
centering and normalization boundaries.

**Nearest collision.**  Quicksort survived the C289 collision ledger.  C291
also uses a first-event convolution, but for irreversible dimer adsorption on
paths and cycles; it has neither recursive subproblem independence nor the
Quicksort contraction law.

**Proof status.**  `PROVABLE AS STATED` with the pivot convention and cost
model fixed.  Algorithmic running-time folklore is not substituted for the
distributional proof.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`; overall Route A rejected.

### C303 -- thermal qubit Lindblad entanglement-breaking atlas

**Owner.**  A qubit GKSL semigroup with downward rate `gamma_d`, upward rate
`gamma_u`, pure-dephasing rate `gamma_phi`, and Hamiltonian frequency
`omega`, using the frozen convention

`(gamma_phi/2)(sigma_z rho sigma_z-rho)`.

**Large step.**  Exponentiate the generator exactly on populations and
coherences; derive the affine Bloch map, fixed Gibbs state, complete
Liouvillian spectrum, semigroup law and exact trace-distance contraction
coefficient.  Compute the normalized Choi matrix and use the two-qubit PPT
criterion to prove the sharp condition

`p(1-p)(1-eta)^2 >= exp(-2 Gamma_2 t)`.

For two-sided thermal noise, prove existence and uniqueness of a finite
entanglement-breaking time and give its implicit root and the no-extra-
dephasing closed form.  Separately close one-sided damping, pure dephasing,
unitary and identity faces.

**Nearest collision.**  C223 and C224 are closed-system unitary two-level
models, C243 is a nonlinear Hamiltonian Bloch-sphere flow, and C297 is a
non-CPTP gain/loss ray flow.  C303 uniquely owns density matrices, complete
positivity, a dissipative semigroup and a Choi/PPT threshold.

**Proof status.**  `PROVABLE AS STATED` after fixing the factor-one-half
dephasing convention and distinguishing finite-time entanglement breaking
from its infinite-time boundary.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`; overall Route A
rejected.  The Liouvillian spectrum is not a Hilbert--Polya construction.

## Rejected and reserved alternatives

- The Morse oscillator and Lagrange top survived the local title scan, but
  the two fluid systems above give broader PDE-level classification theorems
  and a cleaner change of subtype from the immediately preceding round.
- A Tsetlin move-to-front chain and May--Leonard competition model remain
  viable independent owners.  The partition-fragmentation chain and
  Quicksort limit were selected because their all-time and limiting laws form
  stronger closed theorem packages.
- Lattes maps, CIR diffusion, the Euler top, Lyness dynamics, Ehrenfest,
  rotor-router, sandpile, Kac-ring and Toda proposals were rejected because
  existing workspace packages already own the relevant mechanism.
- A simplex projection flow and Galperin collision model were reserved due to
  immediate-round similarity to C298 and to C294/C296 respectively.

No retained package introduces target arithmetic local data, target Euler
factors, bad-prime data, root numbers, automorphy, a target divisor/counting
law or functional equation, a target zero match, a Hilbert--Polya operator,
or Route-B authorization.
