# Route-A idea report: C359--C363

## Round objective and frozen baseline

The user authorized exactly five independent papers and required a theorem-scale
advance in every paper, with a dynamical-system switch whenever a proposal would
only extend an existing owner.  The collision scan covered the C1--C358
candidate and obstruction registries, all 396 first-level project directories,
the most recent batch reports, and mechanism-level neighbors.  The retained
owners are a higher-derivative Hamiltonian oscillator, an anisotropic geometric
flow, a nonequilibrium finite-state jump process, a state-dependent alignment
system, and a nonlocal chemotaxis PDE.  Their clocks, phase spaces, proof engines,
and boundary phenomena are disjoint; no paper is a parameter slice or deferred
section of another.

The frozen collision baseline is
`05ca5f96b2c69a6ad6ba153d1084df750d7722c0`, the date is `2026-09-04`, and
the build epoch is `1788480000`.  Every candidate uses
`flow_systems/skills/route-a-evaluator.md` v0.2.0 at SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`
and literal scope `NO_BAD_EULER_OR_ROOT_NUMBER`.  `NEW` below is only a
workspace ownership statement, never a literature-priority claim.

## Ranked and frozen candidates

### C359 -- Pais--Uhlenbeck higher-derivative oscillator

**Owner.**  The real fourth-order variational system

`L=(qddot^2-(omega_1^2+omega_2^2)qdot^2+omega_1^2 omega_2^2 q^2)/2`

with the Ostrogradsky phase space and the physical time clock.

**Large step.**  Factor the Euler--Lagrange equation and construct an explicit
real canonical splitting for distinct positive frequencies into one positive-
energy and one negative-energy harmonic mode.  Classify boundedness, all
periodic and one-mode exceptional trajectories, irrational two-frequency torus
closures, sampled-flow monodromy, and the natural oscillator-difference
quantization.  Prove separately that the equal-frequency face is a genuine
Jordan degeneration with generic linear growth, that a zero frequency creates
an affine drift mode, and that a negative squared frequency creates exponential
directions.  The quantum spectrum is source-local and unbounded below; no
stability or Hilbert--Polya conclusion is permitted.

**Nearest collisions.**  C357 owns a second-order piecewise-quadratic
isochronous oscillator and C343 owns a dissipative third-order Jordan boundary.
Neither owns a fourth-order Ostrogradsky Hamiltonian, its signed canonical
splitting, or its resonant singular limit.

**Strict tuple.**
`(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`;
Route A is rejected because A0 fails and Route B remains locked.

**Verified source owners.**  Pais and Uhlenbeck, *Physical Review* 79 (1950),
DOI `10.1103/PhysRev.79.145`; Smilga, *Nuclear Physics B* 706 (2005), DOI
`10.1016/j.nuclphysb.2004.10.037`.

### C360 -- Berger-sphere Ricci-flow extinction atlas

**Owner.**  The volume-normalized and unnormalized Ricci flows on the
two-parameter Berger family

`g=A(sigma_1^2+sigma_2^2)+C sigma_3^2`

on `SU(2)`, with the Maurer--Cartan convention fixed before calculation.

**Large step.**  Derive the Ricci tensor and the exact unnormalized ODE

`A'=-8+4C/A`, `C'=-4C^2/A^2`.

For `r=C/A`, prove `r'=8r(1-r)/A` and the two-chamber first integral
`Ar/sqrt(abs(1-r))`.  Integrate the flow to elementary `atanh`/`atan`
lifespans; classify round extinction, Type-I asymptotics, every ancient and
finite-backward branch, and the sectional-curvature sign wall.  Then prove
that the volume-normalized flow is forward complete and converges
exponentially to the round metric.  Round data, lens-space quotients, and the
nonmetric `A=0` or `C=0` faces are kept separate.

**Nearest collisions.**  C281 owns affine factor collapse for products of
round spheres.  It does not own anisotropic `SU(2)` Ricci curvature, the Berger
ratio first integral, the ancient chambers, or the backward singularity.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`; Route A is rejected and
Route B remains locked.

**Verified source owners.**  Hamilton, *Journal of Differential Geometry* 17
(1982), DOI `10.4310/jdg/1214436922`; Isenberg and Jackson, *Journal of
Differential Geometry* 35 (1992), DOI `10.4310/jdg/1214448265`.

### C361 -- finite Markov-jump entropy production and fluctuation symmetry

**Owner.**  Every irreducible finite continuous-time Markov chain with
bidirected support, stationary law `pi`, and physical jump clock.

**Large step.**  Give the matrix-tree stationary law and the exact edge-current
decomposition.  Prove nonnegative steady entropy production, equality exactly
at detailed balance, and equivalence with vanishing cycle affinities.  Identify
total path entropy as the stationary forward/reversed path-density ratio and
derive the finite-time detailed fluctuation relation.  For the medium-entropy
tilt, prove the transpose identity `L_lambda^T=L_(1-lambda)`, equality of the
entire characteristic polynomials, Perron SCGF symmetry, and the associated
large-deviation antisymmetry under the stated differentiability hypothesis.
Close the equilibrium face, the automatically reversible two-state case, the
minimal three-state nonequilibrium cycle, reducible support, and one-way-edge
infinite-affinity boundaries without silently extending logarithms through
zero rates.

**Nearest collisions.**  C192 owns arrangement chamber walks, C183 a random
transposition spectrum, C194 the carries/riffle semigroup, and C351 Jackson
quasi-reversibility.  None owns entropy as a path-reversal Radon--Nikodym
functional or the Gallavotti--Cohen tilted-generator symmetry for arbitrary
finite bidirected jump networks.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`; all determinant and symmetry
statements are source thermodynamics, not a target determinant.

**Verified source owners.**  Schnakenberg, *Reviews of Modern Physics* 48
(1976), DOI `10.1103/RevModPhys.48.571`; Lebowitz and Spohn, *Journal of
Statistical Physics* 95 (1999), DOI `10.1023/A:1004589714161`.

### C362 -- Cucker--Smale conditional/unconditional flocking threshold

**Owner.**  The continuous-time all-to-all Cucker--Smale particle system with
communication kernel `psi(r)=(1+r^2)^(-beta)`, `beta>=0`, arbitrary particle
number and Euclidean dimension.

**Large step.**  Prove global classical flow, mean-velocity conservation,
monotone velocity variance, and the sharp diameter comparison system.  An
explicit Lyapunov barrier yields conditional flocking whenever the initial
velocity diameter lies below the communication tail integral and unconditional
flocking exactly throughout the divergent-tail chamber `beta<=1/2`, with an
explicit confinement radius and exponential alignment rate.  A two-agent
one-dimensional construction proves sharp failure for `beta>1/2`: above the
same tail threshold the pair separates with nonzero asymptotic relative speed,
while equality is the unbounded-separation threshold.  Zero coupling,
coincident particles, consensus data, and two-agent sharpness are explicit.

**Nearest collisions.**  C203 owns fixed-graph linear consensus and C333 owns
random complete-graph gossip.  Neither evolves positions jointly with velocities
through a state-dependent Laplacian or owns the communication-tail phase wall.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`; Route A is rejected and
Route B remains locked.

**Verified source owners.**  Cucker and Smale, *IEEE Transactions on Automatic
Control* 52 (2007), DOI `10.1109/TAC.2007.895842`; Ha and Liu,
*Communications in Mathematical Sciences* 7 (2009), DOI
`10.4310/CMS.2009.v7.n2.a2`.

### C363 -- planar Keller--Segel critical-mass virial atlas

**Owner.**  The parabolic--elliptic Keller--Segel equation on `R^2`,

`rho_t=Delta rho-div(rho grad c)`, `-Delta c=rho`,

for nonnegative classical solutions with the regularity and moment hypotheses
stated in the theorem.

**Large step.**  Derive mass and barycenter conservation, the free-energy
dissipation identity, the mass-preserving dilation law, and the exact second-
moment virial slope `4M(1-M/(8pi))`.  Prove that every supercritical classical
solution with finite second moment loses classical validity no later than the
explicit zero-moment time.  At the critical mass, classify the explicit radial
stationary family `8 lambda^2/(lambda^2+|x-a|^2)^2`, its potential and scaling,
and prove why its infinite second moment prevents a false contradiction with
the finite-moment virial theorem.  The radial cumulative-mass equation,
subcritical positive virial slope, zero solution, translations, and singular
Dirac limits are kept as distinct boundaries.  No full weak-solution or
subcritical convergence theorem is claimed without its separate analysis.

**Nearest collisions.**  C230 owns an Allen--Cahn front, C323 a Fisher--KPP
traveling-wave atlas, C330 a linear Cahn--Hilliard instability, and C350 a
Schnakenberg finite-domain Turing window.  None owns the nonlocal Newtonian
chemotactic drift, its `8pi` scaling threshold, or its virial blow-up clock.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`; Route A is rejected and
Route B remains locked.

**Verified source owners.**  Keller and Segel, *Journal of Theoretical Biology*
26 (1970), DOI `10.1016/0022-5193(70)90092-5`; Blanchet, Dolbeault and
Perthame, *Electronic Journal of Differential Equations* 2006(44), pp. 1--33.

## Eliminated or deferred candidates

- **Squared-Bessel/Bessel dimension atlas -- eliminated.**  C229 already owns
  the `kappa=0` CIR face as a squared-Bessel process, including its affine
  Laplace transform, dimension-zero absorption, and Feller boundary.  A general
  dimension package would enlarge that owner instead of changing systems.
- **Gilbert--Shannon--Reeds riffle shuffle -- eliminated.**  C194 already owns
  the multiplicative carries/riffle semigroup and descent marginal; C192 also
  owns the encompassing braid-arrangement chamber-walk spectrum.
- **MICZ--Kepler -- eliminated.**  Its monopole Kepler integrals would combine
  the already owned C216 Kepler and C331 monopole mechanisms rather than create
  an independent owner.
- **Veselova top -- eliminated.**  Its Hamiltonization lies simultaneously too
  close to C199 Chaplygin, C255 Suslov, and C349 Neumann owners, and its inertia
  convention presents avoidable theorem risk.
- **Darboux--Tannery, Higgs oscillator, and Brieskorn Reeb flow -- deferred as
  round-two clues.**  Each has a viable theorem, but retaining all three beside
  Berger and Pais--Uhlenbeck would over-concentrate this round in geometric and
  integrable mechanics.  They remain candidates for later collision scans.

## Source and claim boundary

Foundational and theorem-specific publisher records were checked before topic
freeze.  Sources establish model ownership and conventional formulas; every
retained package must supply its own derivation and executable finite audit.
Finite ledgers test identities, branches, conventions, and boundary handling;
they do not substitute for analytic proofs of continuum or asymptotic claims.

No package introduces rational-prime labels, prime-power repetitions, target
arithmetic local data, target Euler factors, bad-prime data, root numbers,
automorphy, a target divisor/counting law or functional equation, a target-zero
match, a Hilbert--Polya operator, or Route-B authorization.
