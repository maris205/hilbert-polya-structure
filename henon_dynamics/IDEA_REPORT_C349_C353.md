# Route-A idea report: C349--C353

## Round objective and frozen baseline

The user requested five complete papers, each making a theorem-scale advance,
with broad subtype changes whenever a proposal would merely extend an existing
owner.  A workspace collision scan eliminated already owned Chaplygin-sleigh,
Lyness, Landau--Zener, Fisher--KPP, Brownian-resetting, Kingman, CIR, Kac,
finite-gap and related mechanisms.  The retained owners are an integrable
constrained Hamiltonian, a reaction--diffusion instability, an open queueing
network, a supersymmetric Dirac scatterer and an exchangeable partition-growth
process.  No retained paper is a chapter or parameter slice of another.

The frozen source baseline is
`327fc1172cebcdeb17adfd2d8ad12636fbb94f52`, the date is `2026-09-03`, and
the build epoch is `1788393600`.  Every candidate uses
`flow_systems/skills/route-a-evaluator.md` v0.2.0 at SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`
and literal scope `NO_BAD_EULER_OR_ROOT_NUMBER`.  Newness means only no
existing workspace owner; no literature-priority claim is made.

## Frozen candidates

### C349 -- Neumann oscillator and Uhlenbeck--Lax torus atlas

**Owner.**  The anisotropic Neumann Hamiltonian on `T*S^2` with distinct
positive axis coefficients.

**Large step.**  Prove global completeness; derive all three Uhlenbeck
integrals, their two affine relations and Dirac--Poisson involution; construct
the rational `2 x 2` Lax matrix and identify its determinant with the
Uhlenbeck resolvent; prove that every connected compact regular common level
is a Liouville two-torus and that physical closure is exactly the rational
frequency condition.  Close all axis equilibria, coordinate reductions,
double-spectrum `SO(2)` and isotropic great-circle boundaries, and retain only
the justified natural self-adjoint compact-resolvent quantization.

**Nearest collision.**  C186 owns the Euler top, C313 the round sphere, C331
the monopole sphere and C344 a complex resonant triad.  None owns constrained
Neumann separation, Uhlenbeck residues and the repeated-spectrum symmetry
atlas.

**Strict tuple.**
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`; Route A is
rejected and Route B locked.

### C350 -- Schnakenberg finite-domain Turing mode atlas

**Owner.**  The two-species Schnakenberg reaction--diffusion system with
positive diffusivities and Neumann boundary conditions on one interval.

**Large step.**  Determine the unique positive homogeneous equilibrium and
the exact kinetic stability chamber; diagonalize every Neumann mode; derive
the necessary-and-sufficient continuous Turing window; reduce it to the exact
strict integer selection on a finite interval; count unstable modes and give
every length entry/exit wall.  Close the homogeneous mode, both neutral
endpoints, the double wall, equal diffusion and excluded zero-diffusion faces.
The result is deliberately linear and does not manufacture a nonlinear
pattern branch.

**Nearest collision.**  C311 owns a finite-dimensional Brusselator Hopf
branch, C202 a scalar Fisher--KPP front and C304 a linear Cahn--Hilliard shell
atlas.  None owns a two-species activator--inhibitor finite-domain Turing
selection theorem.

**Strict tuple.** All five gates fail; Route A is rejected and Route B locked.

### C351 -- open Jackson network and quasi-reversible output atlas

**Owner.**  A finite open single-class network of exponential single-server
queues under a frozen row-routing convention.

**Large step.**  Solve the traffic equations and prove positive recurrence
exactly under componentwise subcritical load; derive the unique geometric
product form; reconstruct the full time-reversed visible marked-jump network;
and prove the independent Poisson external-output theorem with its correct
past/state orientation.  Close critical and overloaded non-positive-recurrent
faces, self-routing marks, isolated queues, tandems, zero direct-exit nodes and
the natural reversed class allowing zero exogenous rates.  Internal arc flows
are not falsely declared jointly independent.

**Nearest collision.**  Prior birth--death, exclusion, inclusion and closed
finite Markov owners do not contain an open interacting queueing network,
traffic equations, quasi-reversal and external output processes.

**Strict tuple.** All five gates fail; Route A is rejected and Route B locked.

### C352 -- integer-kink Jackiw--Rebbi Dirac atlas

**Owner.**  The whole-line Dirac Hamiltonian with
`A_n=d/dx+n*tanh(x)` at every positive integer height.

**Large step.**  Fix the self-adjoint domain and supersymmetric square;
exhaust the unique chiral zero mode and every nonzero simple bound pair;
construct a normalized Darboux unitary that proves the continuum purely
absolutely continuous with no embedded spectrum; derive both bounded non-`L2`
threshold spinors; and prove integer-height reflectionlessness with a frozen
Jost convention.  Close the free, kink-sign and dilation boundaries.

**Nearest collision.**  C224 is finite-dimensional Landau--Zener, C340 is a
periodic scalar finite-gap operator and C345 is a nonlinear Toda scatterer.
None owns a topological whole-line Dirac kink and adjacent Pöschl--Teller
hierarchy.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`; Route A is
rejected and Route B locked.

### C353 -- Ewens--Chinese-restaurant partition-growth atlas

**Owner.**  The exchangeable one-parameter insertion process on labelled set
partitions.

**Large step.**  Derive the Ewens EPPF and complete occupancy-vector law from
the local growth rule; prove that the total block count is a sum of independent
Bernoulli innovations; obtain its exact PGF, almost-sure logarithmic law and
variance-normalized CLT; and prove the joint independent-Poisson limit for
every fixed vector of block sizes from a complete mixed-factorial-moment
formula with uniform integrability.  Close the uniform-permutation,
zero-concentration and infinite-concentration fixed-size boundaries without
claiming a ranked Poisson--Dirichlet theorem.

**Nearest collision.**  C215 is a backward Kingman coalescent, C331 concerns
allele-frequency diffusions and C342 is a fixed-state birth--death WKB system.
None owns a growing exchangeable set partition and its two-scale block atlas.

**Strict tuple.** All five gates fail; Route A is rejected and Route B locked.

## Source and scope boundary

The source lineages are Neumann--Moser for C349, Schnakenberg--Turing for C350,
Jackson--Burke--Kelly for C351, Jackiw--Rebbi and exact 1+1 dimensional kink
spectral work for C352, and Ewens--Hoppe for C353.  Each paper rederives its
claims and treats citations as ownership context.

No package introduces target arithmetic local data, target Euler factors,
bad-prime data, root numbers, automorphy, a target divisor/counting law or
functional equation, a target-zero match, a Hilbert--Pólya operator, or Route-B
authorization.
