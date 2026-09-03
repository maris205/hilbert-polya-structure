# Route-A idea report: C324--C328

## Round objective and frozen baseline

The user requested another group of exactly five finished papers, with one
theorem-scale advance in every paper and an immediate change of dynamical
subtype whenever a proposed owner would merely repeat an earlier mechanism.
This round therefore uses five different state spaces and proof engines: a
nonlinear wave-breaking PDE, a randomized local-resampling algorithm, an
attractive finite-particle Markov chain, a periodic point-interaction quantum
Hamiltonian, and a confined active-particle PDMP.  None is a parameter slice
or deferred section of another paper.

The collision baseline is
`1aba1f6fd0cf81baa7c137a2ce7ce3d097ba63fc`, the fixed date is 2026-09-03,
and the build epoch is `1788393600`.  Every candidate is evaluated under
`flow_systems/skills/route-a-evaluator.md` v0.2.0, SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`,
with literal scope `NO_BAD_EULER_OR_ROOT_NUMBER`.

The collision scan covered the C1--C323 registry, all recent idea reports,
directory owners, obstruction records, and mechanism-level neighbors.  It
removed Wright--Fisher/Jacobi diffusion (C200), CIR diffusion (C229),
Landau--Zener scattering (C224), product-kernel coagulation (C228), rotor and
sandpile dynamics (C176/C181), rowmotion and ordinary voter models, another
finite quantum-search reduction, and another smooth curvature flow.  `NEW`
below means only that the frozen theorem has no owner elsewhere in this
workspace.  It is not a claim of literature priority.

## Frozen candidates

### C324 -- periodic Hunter--Saxton wave breaking

**Owner.**  On `T=R/Z`, fix the once-integrated classical formulation

`u_tx + u*u_xx + (u_x)^2/2 = -E/2`,

with a stated translation gauge and `C2` nonconstant initial data, where
`E=int_T u_x^2`.  The differentiated third-order Hunter--Saxton equation is
only a distributional consequence at this regularity.  Initially put
`E=int_T u0_x^2` and `m=min_T u0_x<0`.

**Large step.**  Solve the characteristic derivative problem for every such
initial datum, not merely for a special wave.  With `c=sqrt(E)/2`, prove

`eta_x=[cos(c*t)+(u0_x/sqrt(E))*sin(c*t)]^2`

and the exact pulled-back slope formula.  Deduce the maximal forward
classical lifespan

`T*=2/sqrt(E)*atan(sqrt(E)/(-m))`,

identify the breaking labels exactly as the minimizers of `u0_x`, and prove
the universal slope blow-up `u_x~-2/(T*-t)` there.  Retain Jacobian collapse,
energy conservation before breaking, simultaneous multiple minima, the
constant-data face, and the negative-time analogue through the maximum
slope.

**Nearest collision.**  C195 is parabolically smoothed viscous Burgers, C256
is a traveling-wave reduction of KdV, and C278 is a two-peakon Camassa--Holm
manifold.  C324 owns arbitrary periodic classical data, an exact
infinite-dimensional characteristic Jacobian, and its first wave-breaking
set.  The risk is low once the integrated constant and circle gauge are
locked.

**Proof boundary.**  The theorem stops at the first loss of a classical
diffeomorphism.  It neither selects nor claims uniqueness of a dissipative or
conservative weak continuation.  Twelve single-harmonic and six smooth
asymmetric two-harmonic checks audit conventions; they do not replace the
arbitrary-data proof.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`; Route A rejected.

### C325 -- Moser--Tardos witness-tree resampling dynamics

**Owner.**  Freeze the finite independent-variable Lovasz-local-lemma model.
Bad events depend only on declared variable sets; an infinite independent
resampling table supplies all randomness, and at each step any currently
violated event may be selected and its variables resampled.

**Large step.**  Under witnesses `x_A in (0,1)` satisfying

`P(A) <= x_A * product_(B in Gamma(A))(1-x_B)`,

prove from the execution log that every event's resampling count obeys

`E N_A <= x_A/(1-x_A)`.

Close the proper witness-tree probability lemma, the multitype branching
weight bound, finite total expectation, almost-sure termination, and the
fact that the terminal assignment avoids every bad event.  The theorem is
uniform in the legal event-selection rule; a lexicographic rule is frozen
only for finite exact audit chains.

**Nearest collision.**  C192 is a fixed finite hyperplane-chamber walk, C302
is a divide-and-conquer cost recursion, and C317 is deterministic matrix
residual squaring.  No registered owner has local constraint violations,
selective variable resampling, resampling tables, or witness-tree analysis.

**Proof boundary.**  Only the ordinary finite variable model is claimed.
Permutation, lopsided, parallel and distributed variants, and termination
outside the stated witness condition remain open.  The package reconstructs
small rational absorbing chains only as independent checks.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`; Route A rejected.

### C326 -- two-site symmetric inclusion process

**Owner.**  With total mass `N` and `alpha>0`, let `x in {0,...,N}` be the
occupation of site one and set

`L f(x)=(N-x)(alpha+x)[f(x+1)-f(x)]`
`       +x(alpha+N-x)[f(x-1)-f(x)]`.

**Large step.**  Prove the normalized beta-binomial law

`pi_N(x) proportional (alpha)_x (alpha)_(N-x)/(x!(N-x)!)`

is the unique reversible stationary law.  Diagonalize the entire generator:
the simple eigenvalues of `-L` are

`lambda_j=j(j-1+2*alpha)`, `0<=j<=N`,

with Hahn-polynomial eigenfunctions.  From orthogonality derive the complete
finite-time kernel, the sharp gap `2*alpha`, and sharp mean-zero `L2` decay.
Close `N=0`, `N=1`, and the singular `alpha downarrow 0` face, including the
absorbing endpoint law and the symmetric endpoint limit of stationarity.

**Nearest collision.**  C263 has a growing Polya urn whose marginal limit is
Dirichlet, C253 is an absorbing Moran chain, C285 is a closed queueing
network, and C322 is a continuous energy-sphere collision process.  Sharing
a beta-binomial weight does not share C326's inclusion rates, polynomial
filtration, Hahn spectrum, or zero-attraction boundary.

**Proof boundary.**  The theorem is for exactly two symmetric sites and fixed
total mass.  It does not infer a multi-site graph spectrum, open-boundary
nonequilibrium law, thermodynamic condensation scale, or infinite-particle
limit.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`; Route A rejected.

### C327 -- Kronig--Penney delta-comb band and gap atlas

**Owner.**  For period `a>0` and coupling `g in R`, define the self-adjoint
one-dimensional periodic point-interaction Hamiltonian

`H=-d^2/dx^2 + g*sum_(n in Z) delta(x-n*a)`

through its closed quadratic form and Floquet fibres.

**Large step.**  Derive the one-cell transfer matrix and the convention-safe
Floquet discriminant

`Delta(k^2)=cos(k*a)+g*sin(k*a)/(2*k)`,

with analytic zero-energy continuation and `k=i*kappa` on negative energy.
Prove that the spectrum is purely absolutely continuous and is exactly
`|Delta(E)|<=1`.  Close all repulsive, free and attractive chambers,
including the negative band, the zero-energy thresholds `g*a=0,-4`, every
open nonzero-coupling Bragg gap, fibre multiplicities and band-edge
degeneracies.  Add an indexed integrated-density/density-of-states formula
and the high-energy gap-width law `2*|g|/a+O(n^-2)` in energy units.

**Nearest collision.**  C288 is one point interaction on the line, C308 is a
finite non-Hermitian tight-binding chain, C318 is a finite chiral SSH lattice,
and C323 is a finite complete-graph oracle Hamiltonian.  None owns an infinite
periodic singular potential, its continuum Bloch discriminant, all-sign band
topology, or its negative-to-positive threshold atlas.

**Proof boundary.**  The theorem is one-dimensional, scalar, and exactly
periodic.  It does not assert disorder localization, nonlinear dynamics,
finite-crystal edge states, or target determinant/divisor matching.  The
Bloch operator is a natural source quantization only.

**Strict tuple.**
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,`
`A4_NATURAL_QUANTIZATION)`; Route A rejected.

### C328 -- harmonically confined run-and-tumble dynamics

**Owner.**  Let `sigma_t in {-1,+1}` flip at rate `lambda` and evolve

`dX_t/dt=v*sigma_t-mu*X_t`,

with `mu,v,lambda>0`.  The natural invariant interval is
`[-v/mu,v/mu]` and `alpha=lambda/mu`.

**Large step.**  Solve the stationary transport-switching equations to obtain
the normalized beta density

`rho(y)=Gamma(alpha+1/2)/(sqrt(pi)Gamma(alpha))`
`       *(1-y^2)^(alpha-1)`, `y=mu*x/v`,

together with the two velocity-resolved components.  Derive every joint
polynomial moment, including the vanishing even mixed moments and the explicit
odd mixed moments.  Obtain the complete stationary `2 x 2` correlation matrix:
the semigroup formula is for `t>=0`, negative lag is its transpose, and the
critical `mu=2*lambda` face has the correct Jordan limit.  On every finite
polynomial-observable space, prove the complete triangular generator spectrum

`{-n*mu, -(n*mu+2*lambda): 0<=n<=d}`

with multiplicities/generalized eigenvectors classified at resonances: positive
speed gives Jordan blocks exactly at odd integral `2*lambda/mu`, while even
integral resonance is semisimple.  Retain the zero-speed, zero-switching and
zero-confinement boundaries separately, including the semisimple `v=0,
lambda>0` face and the arbitrary-orientation `v=lambda=0` intersection.

**Nearest collision.**  C213 is an unconfined circular telegraph process with
Fourier blocks; C237 is Gaussian Kramers--Langevin diffusion; C265 is a
self-exciting point process.  C328 has deterministic harmonic flights,
compact trapping, a non-Gaussian beta stationary law, and a polynomial
observable hierarchy.

**Proof boundary.**  The polynomial-filtration theorem is not promoted to an
unproved complete `L2` spectrum.  Boundary atoms and nonunique invariant laws
at `lambda=0`, loss of confinement at `mu=0`, and collapse at `v=0` are not
hidden inside the positive-parameter density.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`; Route A rejected.

## Historical ownership and rejected alternatives

The source locks are Hunter and Saxton for the nonlinear director-field
equation; Moser and Tardos for algorithmic local-lemma resampling; the
symmetric inclusion-process literature and finite Hahn orthogonality; the
original Kronig--Penney model plus standard one-dimensional Floquet theory;
and the active-particle/run-and-tumble transport literature.  Each package
claims a proof-complete, convention-locked, executable synthesis and any
explicitly identified source-local extension, never priority over these
ingredients.

Wilson cycle-popping was mathematically strong but reserved to avoid two
large randomized algorithms in one batch.  Bernoulli--Laplace was rejected
as too near the existing finite Markov-spectrum lane.  Dyson--OU was reserved
because a variance normalization error would contaminate both the Coulomb
drift and the sharp gap.  STIRAP, monopole harmonics, Morse scattering,
Lieb--Liniger and kicked-rotor proposals were kept as future quantum owners
instead of using several adjacent quantum slots.  Kirchhoff vortices,
crystalline curvature, King--Rosenau Ricci flow and Hele--Shaw evolution were
also retained as model-changing fallbacks rather than filling this batch
with neighboring continuum PDEs.

No retained package introduces target arithmetic local data, target Euler
factors, bad-prime data, root numbers, automorphy, a target divisor/counting
law or functional equation, a target zero match, a Hilbert--Polya operator,
or Route-B authorization.
