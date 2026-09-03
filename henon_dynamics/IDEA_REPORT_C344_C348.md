# Route-A idea report: C344--C348

## Round objective and frozen baseline

The user requested another round of exactly five finished papers, with a
theorem-scale advance in each paper and a change of dynamical subtype whenever
a proposal would merely continue an existing owner.  The mechanism-level scan
covered C1--C343 package titles and theorem summaries, both global registries,
recent idea reports, explicit collision ledgers and deferred candidates.

This round freezes five independent owners: a complex Hamiltonian resonant
triad, a side-coupled lattice impurity, a deterministic oblique Skorokhod map,
a nonlinear mean-field Fokker--Planck equation and an infinite random walk in
iid spatial disorder.  None is a chapter, parameter slice or postponed lemma
of another retained paper.

The collision baseline is
`1af63b945e19b5f94ac1cb76f93af5ac66d3d562`, the fixed date is 2026-09-03,
and the build epoch is `1788393600`.  Every candidate is evaluated under
`flow_systems/skills/route-a-evaluator.md` v0.2.0, SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`,
with literal scope `NO_BAD_EULER_OR_ROOT_NUMBER`.  `NEW` below means only no
existing workspace owner for the frozen mechanism; it is not a literature
priority claim.

## Frozen candidates

### C344 -- Hamiltonian resonant-triad elliptic dynamics

**Owner.**  Freeze the three-wave Hamiltonian

`H=z1*z2*conj(z3)+conj(z1)*conj(z2)*z3`

with `i zdot1=conj(z2)z3`, `i zdot2=conj(z1)z3`, and
`i zdot3=z1 z2`.

**Large step.**  Prove Liouville integrability using both Manley--Rowe
invariants and `H`; reduce `x=|z3|^2` to the complete cubic elliptic curve

`xdot^2=4*x*(N1-x)*(N2-x)-H^2`;

classify all accessible root chambers and give the Jacobi `sn^2` solution and
period.  Reconstruct the two independent phase increments by third-kind
elliptic quadratures and prove that full complex-orbit closure requires both
increments to be rational multiples of `2*pi`, not merely periodic intensity.
Close the phase-locked double-root wall, zero-Hamiltonian chart changes,
separatrix, coordinate axes, conjugation, time reversal and coupling scaling.

**Nearest collision.**  C211 has a real planar Lotka--Volterra period annulus,
C186 an Euler top, C230 open Toda, and C256 a KdV traveling profile.  None owns
a complex three-mode Hamiltonian, two Manley--Rowe levels and the distinction
between intensity and phase return.

**Proof boundary.**  Root tables and numerical elliptic quadratures are
receipts.  Analytic reduction and phase reconstruction prove the continuum
theorem.

**Strict tuple.**
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`; Route A is rejected and
Route B locked.

### C345 -- side-coupled Fano--Anderson spectral and scattering atlas

**Owner.**  Freeze the self-adjoint nearest-neighbor chain on
`ell^2(Z)` coupled at site zero to one discrete impurity of energy `epsilon`,
with hopping `J>0` and coupling `g`.

**Large step.**  Determine the complete spectrum: absolutely continuous band
`[-2J,2J]` of multiplicity two, no singular continuous spectrum and, for
`g!=0`, exactly two simple band-exterior eigenvalues.  Give the branch-locked
Schur resolvent, impurity density, bound-state residues and unit mass sum rule;
exclude embedded and threshold eigenvalues.  Derive exact reflection and
transmission and prove the in-band Fano zero at `E=epsilon`.  Close `g=0`,
`J=0`, edge-energy, coupling-sign gauge and the nonuniform weak-coupling limit.

**Nearest collision.**  C267 is a uniformly forced Wannier--Stark chain, C308
is non-self-adjoint Hatano--Nelson skin dynamics, C318 is a dimerized SSH chain,
and C288 is a continuum point interaction.  None combines a side discrete
state, two band-exterior poles and a Fano antiresonance.

**Proof boundary.**  Squaring the eigenvalue equation creates quartic
extraneous roots; branch and sign filters are part of the theorem.  Finite-box
spectra never prove the infinite absolutely continuous statement.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`; Route A is
rejected and Route B locked.

### C346 -- oblique Skorokhod map and sharp M-matrix wall

**Owner.**  For two-dimensional cadlag input `x`, freeze

`z=x+R*y>=0`, `R=[[1,-rho],[-sigma,1]]`, `rho,sigma>=0`,

with nondecreasing regulator and post-jump Stieltjes complementarity.

**Large step.**  Prove existence and uniqueness for every input exactly when
`rho*sigma<1`; identify the two running-supremum fixed-point equations; obtain
the exact weighted contraction factor `sqrt(rho*sigma)`, explicit regulator
and state Lipschitz constants and monotone Picard rate; and prove causality,
continuity preservation and continuous time-change covariance.  At the wall,
construct an infinite nonunique regulator cone, while one simultaneous
negative jump proves nonexistence everywhere at and above the wall.  Close
normal and both triangular faces.

**Nearest collision.**  C332 is scalar moving-interval play, C266 is
one-interface skew Brownian motion, C279 is total-variation flow, and C238 is
Filippov dry-friction capture.  None owns a two-axis oblique path map or its
sharp P/M-matrix threshold.

**Proof boundary.**  The contraction norm requires both weights positive;
triangular faces are solved explicitly.  Jump states are evaluated after the
regulator jump.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`; Route A is rejected and Route B
locked.

### C347 -- noisy mean-field Kuramoto stationary phase transition

**Owner.**  Freeze on the circle

`rho_t=D*rho_(theta theta)-K*d_theta[rho*r*sin(Psi-theta)]`,

where `D>0`, `K>=0` and `r exp(i Psi)=integral exp(i theta) rho(theta)dtheta`.

**Large step.**  Prove mass/positivity and the exact free-energy dissipation
identity.  Classify every stationary density as uniform or a von Mises
rotation, reduce self-consistency to a Bessel-ratio equation, and prove that
`K<=2D` has only the uniform state whereas `K>2D` has one nonzero concentration
and its full `S^1` orbit.  Diagonalize the uniform linearization, obtain the
sharp first-harmonic threshold `K_c=2D`, and derive the local order-parameter
expansion.  Close zero coupling, the critical neutral mode and the singular
zero-noise boundary without asserting all-data global convergence.

**Nearest collision.**  C259 is a finite deterministic tree-Kuramoto locking
problem; C213, C237 and C335 are linear or affine stochastic semigroups.  None
owns a nonlinear self-consistent circle PDE and its symmetry-breaking
stationary atlas.

**Proof boundary.**  A real zero eigenvalue is not a Hopf point.  The paper
does not claim a general nonlinear convergence theorem or include atomic
zero-noise equilibria in the positive-density result.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`; Route A is rejected and Route B
locked.

### C348 -- one-dimensional iid RWRE Solomon phase atlas

**Owner.**  Freeze the strictly elliptic nearest-neighbor walk in an iid
environment on `Z`, with `rho_x=(1-omega_x)/omega_x` and
`E|log rho_0|<infinity`; quenched and annealed laws remain distinct.

**Large step.**  Derive the exact finite-interval hitting formula from the
random potential.  Prove the complete recurrence/transience trichotomy from
`E log rho_0`, the deterministic annealed speed law from `E rho_0` and
`E rho_0^{-1}`, and the transient zero-speed chambers.  Specialize the full
atlas to `Beta(alpha,beta)` environments, including both unit-offset ballistic
walls and rational speeds, and recover the homogeneous walk as a boundary.

**Nearest collision.**  C342 is a finite directed reinforced walk represented
by row-Dirichlet transitions, C273 has iid increments, and C253 is a finite
absorbing Moran chain.  C348 instead owns quenched infinite spatial disorder,
a random potential and the separation of directional from ballistic
thresholds.

**Proof boundary.**  The zero-speed transient regions require an infinite-mean
crossing/regeneration argument; finite environment words cannot establish it.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`; Route A is rejected and Route B
locked.

## Sources and rejected alternatives

Primary owners are Manley--Rowe and the classical three-wave interaction
literature for C344; Friedrichs/Fano and discrete impurity scattering for
C345; Harrison--Reiman and Dupuis--Ishii for C346; Sakaguchi and rigorous
mean-field Kuramoto work for C347; and Solomon for C348.  The papers claim
proof-complete, convention-locked reconstructions and identified source-local
consequences, never priority over those ingredients.

Neumann's spherical oscillator was not selected because it would duplicate
the batch's integrable-Hamiltonian subtype.  Hasimoto filament dynamics and a
Schnakenberg Turing atlas survived local title scans but would create a second
PDE slot.  A star-transposition chain is exact but follows immediately after
C341's full finite Markov spectrum; noisy additive cellular automata lie too
close to C204/C171.  Somos/QRT dynamics, another Ricci ancient solution and
multi-allele Wright--Fisher were rejected or reserved because existing QRT,
Ricci and Jacobi/population owners make their mechanism boundaries less clean.

No retained package introduces target arithmetic local data, target Euler
factors, bad-prime data, root numbers, automorphy, a target divisor/counting law
or functional equation, a target zero match, a Hilbert--Pólya operator, or
Route-B authorization.
