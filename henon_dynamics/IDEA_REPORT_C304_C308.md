# Route-A idea report: C304--C308

## Round objective and frozen baseline

The user requested another batch of exactly five independent papers, with a
large theorem-scale advance in every paper and a deliberate change of
dynamical subtype from one slot to the next.  The collision baseline is
`c0259978b1d7ebae63fe7b39fce1af2655b8529d`, the fixed date is 2026-09-03,
and the build epoch is `1788393600`.  Every candidate is evaluated under
`flow_systems/skills/route-a-evaluator.md` v0.2.0, SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`,
with literal scope `NO_BAD_EULER_OR_ROOT_NUMBER`.

The collision scan covered the C1--C303 package titles, both registries,
recent idea reports, and targeted owner/mechanism searches.  The five
retained systems change phase space, clock, and proof mechanism in every
slot:

1. a fourth-order analytic PDE semigroup on periodic Sobolev spaces;
2. a measurable-control navigation problem in Euclidean space;
3. a killed determinantal Markov process in a discrete Weyl chamber;
4. a monotone random graph growth process on the Boolean edge lattice;
5. a finite non-normal quantum lattice Hamiltonian with boundary-sensitive
   spectrum.

`NEW` below means only that no existing workspace package owns the frozen
theorem.  It is not a claim of priority in the literature.

## Frozen candidates

### C304 -- multidimensional linear Cahn--Hilliard spinodal semigroup

**Owner.**  On the `2*pi` periodic torus in dimension `d>=1`, take the
mean-zero realization

`A_(kappa,alpha)=-kappa Delta^2-alpha Delta`, `kappa>0`, `alpha in R`,

with domain `H^4(T^d) intersect L^2_0(T^d)`.

**Large step.**  Construct the self-adjoint analytic, positive-time
trace-class semigroup and its exact Fourier-shell expansion.  Close mass
conservation, instantaneous smoothing, the Cahn--Hilliard free-energy law,
the complete stable/neutral/spinodal atlas, Morse index and kernel
multiplicity from the representation numbers `r_d(n)`, every fastest-shell
cell and tie, and the initial-support-dependent long-time asymptotics.  The
same theorem proves that there is no nonstationary periodic solution and
classifies the singular `kappa -> 0` boundary into forward heat, identity,
and backward-heat non-generation.

**Nearest collision.**  C206 has second-order Couette enhanced dissipation,
C217 has conservative rotating shallow-water Fourier blocks, C218 has a
damped wave pencil, C261 has a dispersive periodic Airy--Talbot group, and
C277 has a Caputo fractional heat family.  None owns a fourth-order spinodal
generator together with lattice-shell Morse index, indefinite free energy,
fastest-shell ties, and the ill-posed zero-capillarity face.  The theorem is
not reduced to a one-dimensional Fourier table.

**Proof status.**  `PROVABLE AS STATED` for the frozen linearized periodic
model in every finite dimension.  No nonlinear cubic Cahn--Hilliard,
coarsening, or pattern-saturation theorem is asserted.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`; overall Route A
rejected.

### C305 -- constant-wind Zermelo navigation in every wind chamber

**Owner.**  In `R^d`, start at the origin and solve

`x_dot=W+u`, `|u|<=c`, `c>0`,

with measurable controls and a prescribed endpoint displacement.

**Large step.**  Prove that the exact time-`t` reachable set is the closed
ball with center `tW` and radius `ct`.  From its first contact with an
endpoint, derive the minimum-time value in the weak-wind, critical-wind, and
strong-wind chambers.  Close full-space reachability, the critical open
half-space, the strong-wind Mach cone and its double-root boundary, the
complete attainable-time intervals, and uniqueness almost everywhere of
the saturated constant optimal control.  Prove positive homogeneity and the
Hamilton--Jacobi equation in the reachable interior, and retain the loss of
regularity at the cone, zero wind, zero control speed, zero displacement,
rotational covariance, and scaling faces.

**Nearest collision.**  C222 is a second-order double-integrator
bang--bang problem, C270 is nonholonomic Heisenberg sub-Riemannian control,
and C268 is an uncontrolled Lorentz flow.  None has the translated reachable
balls, weak/critical/strong wind trichotomy, or strong-wind cone geometry.

**Proof status.**  `PROVABLE AS STATED` for constant wind in Euclidean
space.  Variable winds, obstacles, and global navigation on curved
manifolds remain outside scope.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`; overall Route A rejected.

### C306 -- killed noncolliding continuous-time walkers

**Owner.**  Let `1<=k<=L`.  Run `k` independent rate-two continuous-time
symmetric nearest-neighbor walks on `{1,...,L}` and kill the system at the
first boundary exit or coincidence, represented on the strictly ordered
discrete Weyl chamber.

**Large step.**  Diagonalize the one-particle Dirichlet generator by its
sine basis and prove the Karlin--McGregor determinant kernel.  Antisymmetric
tensor powers then give every Slater eigenfunction and all
`binomial(L,k)` eigenvalues.  From the positive ground state, derive the
exact survival and absorption law, leading decay and spectral gap, the
unique quasi-stationary distribution, and the Doob ground-state transform
with its exact invariant law proportional to the square of the ground
state.  The one-particle, completely filled, zero-time, long-time, and
small-volume faces are explicit.

**Nearest collision.**  C171 is the one-coordinate Ehrenfest chain, C183 a
random-transposition walk, C215 a coalescent genealogy, and C276 a uniform
random-mapping process.  None owns absorbing collision geometry,
Karlin--McGregor determinants, the full exterior-power spectrum, a
quasi-stationary law, and its conditioned noncolliding dynamics in one
theorem.  Killed collision is kept distinct from reflecting exclusion.

**Proof status.**  `PROVABLE AS STATED` for every finite `L,k`.  Finite
matrix evidence checks conventions; it is not used as the proof of the
all-size exterior-power theorem.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`; overall Route A
rejected.

### C307 -- Erdos--Renyi connectivity first passage

**Owner.**  Uniformly permute the `binomial(n,2)` edges of the complete
labelled graph and reveal one new edge at every integer time.  Let
`tau_conn` be the first time that the growing graph is connected.

**Large step.**  Decompose a disconnected graph by the component containing
vertex one to obtain an exact all-`n,m` recurrence for the number of
connected labelled graphs.  This gives the complete finite CDF, PMF, tail,
and moment formulas for `tau_conn`, with exhaustive small-graph controls.
The analytic theorem also closes the critical connectivity window:

`P(2 tau_conn/n-log n <= c) -> exp(-exp(-c))`.

Its proof separates Poisson convergence of isolated vertices from the
vanishing probability of disconnection without isolated vertices.  Integer
rounding, `n=1`, `n=2`, initial and terminal times, and monotone absorption
are retained.

**Nearest collision.**  C301 is a partition-refinement birthday process,
C291 is random sequential adsorption on paths and cycles, and C276 samples a
whole random mapping at once.  None owns the without-replacement graph-edge
growth clock, exact connected-graph recurrence, connectivity absorption
law, and its Gumbel window.

**Proof status.**  `PROVABLE AS STATED`.  The package does not promote the
finite recurrence to a new literature-priority claim, does not claim
unproved moment convergence from weak convergence, and does not identify
connectivity time with the last-isolated-vertex time outside a separately
proved asymptotic statement.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`; overall Route A rejected.

### C308 -- Hatano--Nelson boundary and skin-effect atlas

**Owner.**  Consider the nonreciprocal nearest-neighbor Hatano--Nelson chain
with right and left hopping amplitudes `t_R,t_L>=0`, under open boundary
conditions for `N>=2` and the standard oriented periodic ring for `N>=3`.
The coincident-neighbor `N=2` periodic convention is isolated separately.

**Large step.**  For positive hoppings, conjugate the open chain exactly to
a symmetric path adjacency matrix.  Close its Chebyshev characteristic
polynomial, real spectrum, normalized right/left sine eigenvectors,
biorthogonality, geometric skin envelope, eigenbasis conditioning, resolvent
and propagator.  In parallel, Fourier-diagonalize the periodic chain and
derive its spectral ellipse.  The theorem then resolves the Hermitian face,
orientation reversal, both one-sided faces--where the open chain is one
nilpotent Jordan block but the periodic chain is a diagonalizable cyclic
shift--the zero matrix, and the noncommuting open/periodic boundary limits.

**Nearest collision.**  C267 is an infinite Hermitian Wannier--Stark ladder,
C288 is a self-adjoint point interaction, C297 is a two-mode PT gain/loss
flow, and C303 is a CPTP qubit semigroup.  None owns a growing non-normal
nonreciprocal lattice, its exact diagonal similarity, boundary-sensitive
spectral collapse, and left/right skin geometry.

**Proof status.**  `PROVABLE AS STATED` for the clean finite chain.  Disorder
localization, interactions, bulk topology, and any target spectral match are
outside scope; right-amplitude localization is never confused with the
biorthogonal density.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`; overall Route A
rejected.

## Rejected and reserved alternatives

- Poisson Galton--Watson generation and total-progeny dynamics were rejected
  because C208 already owns the three-phase branching mechanism in
  continuous time.
- Bernoulli--Laplace diffusion was rejected because its finite orthogonal-
  polynomial Markov spectrum lies too close to C171 and C183 and had already
  failed several recent collision screens.
- Exponential shot-noise Ornstein--Uhlenbeck dynamics remains a valid future
  PDMP candidate, but using it here would make the batch less diverse than
  the retained discrete Weyl-chamber and random-graph systems.
- The grim-reaper curve-shortening translator and a one-jump Loewner chain
  were reserved: both have clean exact formulas, but their proposed theorem
  atlases were narrower or more convention-sensitive than C304--C305.
- A two-state gene-expression PDMP remains viable, but is closer to C213's
  two-state telegraph blocks than the retained Hatano--Nelson boundary atlas.

No retained package introduces target arithmetic local data, target Euler
factors, bad-prime data, root numbers, automorphy, a target divisor/counting
law or functional equation, a target zero match, a Hilbert--Polya operator,
or Route-B authorization.
