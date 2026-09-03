# Route-A idea report: C319--C323

## Round objective and frozen baseline

The user requested another group of exactly five finished papers, with a
theorem-scale advance in every paper and a deliberate change of dynamical
subtype whenever a proposed owner would merely repeat an earlier mechanism.
This round therefore changes both state space and proof engine in every slot:
an extrinsic geometric flow, a modular integrable polynomial flow, a growing
random network, a kinetic collision process, and a finite-dimensional quantum
search Hamiltonian.  None is a parameter slice or deferred section of another
paper.

The collision baseline is
`1ccbfe2d759fe007c6b53c9646e1ab031878b34a`, the fixed date is 2026-09-03,
and the build epoch is `1788393600`.  Every candidate is evaluated under
`flow_systems/skills/route-a-evaluator.md` v0.2.0, SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`,
with literal scope `NO_BAD_EULER_OR_ROOT_NUMBER`.

The collision scan covered the C1--C318 registry, all recent idea reports,
directory owners, and mechanism-level neighbors.  In particular, it removed
Chaplygin-sleigh scattering (already C199), Tsetlin/random-to-top (already an
instance of C192's braid-arrangement chamber walk), conjugate gradients (an
earlier C201 near-collision), and generic Grover/Szegedy spectral mapping.
`NEW` below means only that the frozen theorem has no owner elsewhere in this
workspace.  It is not a claim of literature priority.

## Frozen candidates

### C319 -- spherical Clifford-product mean-curvature flow

**Owner.**  For integers `p,q>=1`, `n=p+q`, evolve

`S^p(cos(theta)) x S^q(sin(theta))` in `S^(n+1)`

by the unnormalized spherical mean-curvature flow, with
`y=sin(theta)^2` and the negative-area-gradient convention.

**Large step.**  Prove invariance of this family and the exact equation

`y'=2(ny-q)`,

then close the complete maximal-time phase portrait.  The unique minimal
separator is `y=q/n`; each nonstationary branch is ancient, approaches that
separator exponentially backwards, and reaches one focal submanifold in an
explicit finite forward time.  Prove Type-I blow-up and identify the two
parabolic cylinder models, prove strict area dissipation, and independently
diagonalize the Jacobi operator `Delta+2n` on the minimal product to obtain
Morse index `n+3` and nullity `(p+1)(q+1)`.

**Nearest collision.**  C314 is a planar ancient curve-shortening solution,
whereas C281 is an intrinsic homogeneous product-sphere Ricci flow.  C319 is
an extrinsic hypersurface flow with focal collapse, cylindrical singularity
models, and the Clifford Jacobi spectrum.  The risk is low.

**Proof boundary.**  The theorem classifies the invariant Clifford-product
family, not arbitrary spherical mean-curvature flows.  The degenerate
`p=0` or `q=0` objects are not inserted into the hypersurface theorem, and a
source Jacobi operator is not a target spectral realization.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`; Route A rejected.

### C320 -- Darboux--Halphen modular dynamics

**Owner.**  Fix the sign convention

`x1'=x2*x3-x1*(x2+x3)`

and its cyclic companions.  This polynomial vector field, rather than a
borrowed theta convention, is the primary lock for every subsequent formula.

**Large step.**  Build a closed polynomial--theta--modular theorem: verify a
theta-constant solution coefficient by coefficient; record the noncollision
`PSL(2,C)` covariance; derive the Chazy projection for
`S=x1+x2+x3`,

`S'''=-4*S*S''+6*(S')^2`,

and the discriminant law

`[(x1-x2)(x2-x3)(x3-x1)]'=-2*S*(x1-x2)(x2-x3)(x3-x1)`.

Classify every double-collision face and the triple diagonal by rational
solutions, and close the theta cusp and Moebius-pole boundaries.  The native
`E2`/theta expansions and divisor sums are retained as a real but weak
arithmetic relation; they are not reinterpreted as prime orbits, a von
Mangoldt clock, or target Euler data.

**Nearest collision.**  C186 owns Euler-top elliptic action--angle dynamics
and C244 owns spherical-pendulum focus--focus monodromy.  Earlier modular
packages do not own the Darboux--Halphen polynomial flow, its Chazy projection,
collision stratification, or theta solution.  The risk is medium because the
literature contains opposite time signs and two nome conventions; exact ODE,
series, and modular-transformation locks are mandatory.

**Proof boundary.**  The theta chart describes the generic noncollision
complex solution and the discriminant-zero strata are proved separately.  A
complex modular chart is not silently called a global real flow.  Native
divisor sums provide neither primitive rational-prime ownership nor a
logarithmic prime roof.

**Strict tuple.**
`(A0_WEAK_ARITHMETIC_RELATION,A1_FAIL,A2_FAIL,`
`A3_PARTIAL_ANALYTIC_STRUCTURE,A4_FAIL)`; Route A rejected.

### C321 -- preferential-attachment degree martingales

**Owner.**  Start from one edge on vertices 1 and 2.  At size `n`, attach the
new vertex to one old vertex `v` with probability

`d_v(n)/(2(n-1))`.

There are no loops or multiple edges.  Fixed-vertex degrees `D_i(n)` and
global degree counts `N_k(n)` are separate observables.

**Large step.**  At the local scale, prove the all-order rising-factorial
identity

`E[D_i(n)^(overline r)]`
`=r! Gamma(n-1+r/2) Gamma(s_i-1)`
` /(Gamma(n-1) Gamma(s_i-1+r/2))`,

with `s_1=s_2=2` and `s_i=i` for `i>=3`.  Use its normalized martingales to
obtain almost-sure and moment convergence of `D_i(n)/sqrt(n)`, identify every
limit moment, and verify moment determinacy.  At the global scale, prove for
every fixed `k` the `L2` law

`N_k(n)/n -> 4/[k(k+1)(k+2)]`.

The single theorem thus connects old-vertex hub growth with the typical
degree's cubic tail instead of stopping at one master equation.

**Nearest collision.**  C263 is an exchangeable Polya urn, C276 is a static
uniform random mapping, and C307 is Erdos--Renyi connectivity under uniform
edge addition.  C321 is a nonexchangeable, degree-biased growing tree with
local and empirical-degree scales.  The risk is low to medium.

**Proof boundary.**  The initial-edge convention is never mixed with the
self-loop LCD convention.  The theorem does not claim the maximum-degree
law, joint hub ranking, or an `m>1` multiedge model.  Finite tree enumeration
checks conventions but does not prove the limiting laws.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`; Route A rejected.

### C322 -- Kac master-equation spectral gap

**Owner.**  On the energy sphere `S^(N-1)(sqrt(N))`, let `Q_N` average
uniformly over an unordered coordinate pair and a full rotation angle, and
fix the continuous-time generator

`L_N=N(I-Q_N)`.

The factor `N`, normalized surface measure, unordered-pair normalization, and
full `2*pi` angular average are part of the theorem.

**Large step.**  Prove that `Q_N` is a self-adjoint Markov contraction with
constants as its only fixed functions and reproduce the exact lower-bound
induction, not merely a finite polynomial calculation, to obtain

`gap(L_N)=(N+2)/(2(N-1))`.

Show equality on the centered fourth-moment mode

`sum_i v_i^4-3N^2/(N+2)`,

deduce sharp `L2` semigroup relaxation, and close `N=2`, arbitrary positive
energy by scaling, zero energy, and the large-`N` slow-mode limit.  This is a
complete kinetic spectral-gap paper rather than an observed eigenvalue.

**Nearest collision.**  C170 is the deterministic finite Kac ring, C183 is
a random walk on a finite permutation group, and C313 is deterministic
spherical geodesic flow.  None is the continuous-state random binary-collision
master equation.  The risk is medium to high because the lower gap requires
a genuine conditional-projection induction.

**Proof boundary.**  The result is an `L2` gap for the stated uniform-angle
finite-particle process.  It is not a complete spectrum, a nonlinear
Boltzmann entropy-decay theorem, or a result for an arbitrary angular kernel.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`; Route A rejected.

### C323 -- complete-graph continuous-time quantum search

**Owner.**  On `C^N`, with `M` marked vertices and `a=M/N`, use

`H_g=-g |s><s|-P_W`, `g>=0`,

where `|s>` is uniform and `P_W` projects onto the marked subspace.  The
complete-graph adjacency version is retained only after explicitly removing
its scalar global phase.

**Large step.**  Decompose the Hamiltonian into the marked and unmarked dark
spaces plus a two-dimensional bright block.  Close the full eigenvalue and
multiplicity ledger and prove the exact success law

`P_W(t)=a+4*g*a*(1-a)/Omega^2 * sin(Omega*t/2)^2`,

where `Omega^2=(g-1)^2+4ga`.  For `0<a<1`, prove perfect search occurs if and
only if `g=1`, with first hit `pi/(2*sqrt(a))`; derive the exact off-resonance
maximum and the critical `sqrt(a)` detuning window.  Retain `M=0`, `M=N`,
`N=1`, `g=0`, and disappearing-dark-space boundaries.

**Nearest collision.**  C143 is a discrete coined inhomogeneous walk, C183
is a classical random-transposition chain, and C318 is a local one-dimensional
chiral lattice.  C323 owns an oracle potential, permutation-symmetric
continuous Schrödinger evolution, a bright/dark splitting, and an exact
resonance window.  The risk is low.

**Proof boundary.**  The finite Hamiltonian is a natural source
quantization, not a Hilbert--Polya operator.  It neither matches target zeros
nor realizes rational primes, and it does not establish a computational
speedup outside the frozen oracle model.

**Strict tuple.**
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`; Route A
rejected.

## Historical ownership and rejected alternatives

The source locks are the isoparametric mean-curvature-flow literature for
C319; Halphen's system and modern theta/modular reconstructions for C320;
Barabasi--Albert and rigorous degree-sequence work for C321;
Carlen--Carvalho--Loss for C322; and Farhi--Gutmann for C323.  Each package
claims a proof-complete convention-locked synthesis and any explicitly
identified source-local extension, never priority over those ingredients.

The collision audit also rejected another Ricci ancient solution as too near
C281/C314, random-to-top as already contained in C192, conjugate gradients as
an old C201 near-collision, an M/M/1 continuation as too near C225, and a
generic quantum-walk spectral mapping as too near C143/C171/C183.  Hunter--
Saxton wave breaking and a two-site inclusion process remain model-changing
fallbacks only if the exact theta triple lock or Kac gap induction fails; a
weaker incomplete paper is not accepted.

No retained package introduces target arithmetic local data, target Euler
factors, bad-prime data, root numbers, automorphy, a target divisor/counting
law or functional equation, a target zero match, a Hilbert--Polya operator,
or Route-B authorization.
