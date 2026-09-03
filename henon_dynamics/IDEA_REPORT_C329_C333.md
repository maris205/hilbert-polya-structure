# Route-A idea report: C329--C333

## Round objective and frozen baseline

The user requested another group of exactly five finished papers, preserving
one theorem-scale advance per paper and changing dynamical subtype whenever a
proposal would merely continue an exhausted owner.  This round therefore
freezes five disjoint mechanisms: a finite-field non-backtracking graph flow,
a Diophantine continued-fraction map, a topologically charged magnetic
Hamiltonian and its natural quantization, a rate-independent sweeping process,
and a random continuous-state consensus product.  None is a deferred section
or parameter slice of another retained paper.

The collision baseline is
`5ca65027918c0fce7ef9af82f3faf2e46ed6530c`, the fixed date is 2026-09-03,
and the build epoch is `1788393600`.  Every candidate is evaluated under
`flow_systems/skills/route-a-evaluator.md` v0.2.0, SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`,
with literal scope `NO_BAD_EULER_OR_ROOT_NUMBER`.

The collision scan covered the C1--C328 registry, obstruction records, recent
idea reports, directory owners, and mechanism-level neighbors.  It rejected a
generic modular-surface/Selberg continuation because C16--C18 and C24--C30
already own the closest clocks and trace obstructions; Pell principal cycles
because the same collision is too strong; Morse scattering because two
quantum owners would reduce subtype diversity; Kida vortices because the full
Euler-to-reduced-system derivation carries more boundary risk than this round
can honestly close; and Gale--Shapley, Tsetlin, and Chinese-restaurant proposals
because stronger model-changing candidates survived.  `NEW` below means only
that the frozen theorem has no owner elsewhere in this workspace.  It is not a
claim of literature priority.

## Frozen candidates

### C329 -- Paley-graph non-backtracking dynamics

**Owner.**  For every odd prime power `q=1 mod 4`, take the Paley graph on
`F_q`, joining `x` and `y` when `x-y` is a nonzero square.  Its dynamical state
space is the set of directed edges and its time-one map is the Hashimoto
non-backtracking adjacency.  Primitive cycles are oriented, quotiented by
cyclic shift but not by reversal; powers remain repetitions of one primitive
cycle.

**Large step.**  Derive from finite-field character orthogonality the complete
strongly regular parameters and adjacency spectrum

`k=(q-1)/2`, `r=(-1+sqrt(q))/2`, `s=(-1-sqrt(q))/2`.

Prove the Bass determinant identity in the frozen convention and specialize it
to the explicit factorization

`det(I-uB)=(1-u^2)^[q(q-5)/4]`
` *(1-ku+(k-1)u^2)`
` *(1-ru+(k-1)u^2)^[(q-1)/2]`
` *(1-su+(k-1)u^2)^[(q-1)/2]`.

Recover the full non-backtracking spectrum, all traces, exact primitive-cycle
counts by Möbius inversion, and the source Ihara zeta.  Close the `q=5` cycle
boundary, extension-field representation, reversal convention, and the
Ramanujan inequality for the source graph.

**Nearest collision.**  C15 has a different Heisenberg congruence graph, C161
uses quadratic Gauss sums for a different operator, C260 classifies individual
projective Möbius maps, and C269 treats finite-field Chebyshev functional
graphs.  C329 owns the quadratic-residue Cayley graph together with its
non-backtracking primitive ledger and complete Paley--Bass factor.

**Proof boundary.**  The graph's finite-field origin and source Ihara product
are intrinsic, but neither is a rational-prime orbit law.  Ramanujan here is a
source-graph eigenvalue bound, not the Riemann hypothesis.  No target Euler
factor, divisor, zero set, root number, or automorphy statement is inferred.

**Strict tuple.**
`(A0_WEAK_ARITHMETIC_RELATION,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,`
`A4_FORMAL_HINT)`; Route A exploratory and Route B locked.

### C330 -- Romik--Berggren Pythagorean dynamics

**Owner.**  Freeze Romik's three-branch map on `(0,1)` with inverse branches

`F1(t)=t/(1+2t)`, `F2(t)=1/(2+t)`, `F3(t)=1/(2-t)`.

Rational points encoding primitive Pythagorean triples belong to the terminating
tree.  Periodic points are treated separately and are quadratic irrational.
Branch endpoints and the two parabolic endpoint words are not silently inserted
into the open phase space.

**Large step.**  Prove the Berggren inverse tree gives every primitive
Pythagorean triple exactly once and strictly descends under the forward height.
For every word of length `n` other than the pure `1` and pure `3` endpoint
words, prove that its cylinder has exactly one fixed quadratic irrational and
that distinct words give distinct fixed points.  Consequently

`#Fix(T^n)=3^n-2`,

with exact-period points and oriented primitive cycles obtained by Möbius
inversion, and

`zeta_T(z)=(1-z)^2/(1-3z)`.

Close the word monodromy matrices, determinant orientation, absolute
multipliers, repetitions, rational termination, boundary itineraries, and the
orientation-reversing word face.

**Nearest collision.**  C147/C152/C157 concern rational square-billiard
directions, C193 owns the Markoff Vieta tree, and C132/C137 own different
Möbius/Bergman transfer systems.  Generic Gauss/Farey proposals were previously
screened out; C330 instead freezes the three-branch Pythagorean tree and proves
the terminating-rational versus periodic-irrational split together with its
complete cycle census.

**Proof boundary.**  Romik owns the ternary Pythagorean dynamics.  This package
claims only a self-contained, convention-locked reconstruction and its exact
periodic atlas.  Pythagorean integrality is not promoted to a rational-prime
primitive dictionary, logarithmic clock, target determinant, or modular
geodesic theorem.

**Strict tuple.**
`(A0_WEAK_ARITHMETIC_RELATION,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,`
`A4_FORMAL_HINT)`; Route A exploratory and Route B locked.

### C331 -- Dirac-monopole magnetic flow and spectrum

**Owner.**  On the unit sphere, freeze the Hermitian line bundle of Chern
number `q in Z`, connection curvature `i(q/2)dA`, classical magnetic strength
`b=q/2`, and natural positive covariant Laplacian.  For classical energy `E`,
`|xdot|^2=2E`.

**Large step.**  Prove the Poincare vector

`J=x cross xdot+b*x`

is conserved, satisfies `J dot x=b` and `|J|^2=2E+b^2`, and rotates every
positive-energy trajectory on its oriented small circle with primitive period

`T=2*pi/sqrt(2E+q^2/4)`.

Then diagonalize the source covariant Laplacian through the `SU(2)` Casimir:

`lambda_(n,q)=n(n+|q|+1)+|q|/2`,
`mult(lambda_(n,q))=2n+|q|+1`, `n>=0`.

Deduce its exact heat-trace series and lowest-Landau-level degeneracy.  Close
the `q=0` round-sphere face, `E=0` stationary face, sign-reversal/conjugate-line-
bundle symmetry, lowest level, and the failure of global line-bundle
quantization for nonintegral charge.

**Nearest collision.**  C313 is only the uncharged round-sphere geodesic and
ordinary Laplacian, C289 is hyperbolic-plane magnetic flow without a compact
line-bundle spectrum, C293 is a singular magnetic Grushin cylinder, and C274
is an Euclidean Penning trap.  C331 owns the linked Chern-charge, small-circle,
and monopole-harmonic spectral theorem.

**Proof boundary.**  The Chern integer is intrinsic topology but not a rational
prime carrier.  Positive-energy trajectories form clean circle families, not
isolated hyperbolic orbits.  The covariant Laplacian is a natural source
quantization, not a Hilbert--Polya operator.

**Strict tuple.**
`(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,`
`A4_NATURAL_QUANTIZATION)`; Route A rejected and Route B locked.

### C332 -- scalar periodic Moreau play

**Owner.**  For `r>=0`, take a `T`-periodic, single-peak
`W^{1,1}_loc` input `u`, increasing from `m` to `M` and then decreasing to
`m`, with plateaux and corners allowed.  The moving interval is
`C(t)=[u(t)-r,u(t)+r]`, and the state solves

`-xdot in N_(C(t))(x)`.

**Large step.**  Prove each monotone segment is an exact Euclidean projection
update and hence that the one-period map is

`F(x)=min(max(x,M-r),m+r)`.

Writing `D=M-m`, classify all three chambers: for `D<2r`, `F` is the
projection onto a nontrivial fixed interval and `F^2=F`; at `D=2r`, that
interval collapses to one constant periodic state; for `D>2r`, `F` is constant
and every initial state is entrained in one period to the unique nontrivial
play loop.  Prove order preservation, sup-norm nonexpansion, time-
reparametrization invariance, exact sticking/sliding events, and

`Var_T(x)=2(D-2r)_+`,
`Diss_T=2r(D-2r)_+`.

**Nearest collision.**  C252 is a two-state relay coupled to a linear ODE,
C238 is an autonomous Coulomb/Filippov capture flow, and C279 is a path-TV
subgradient evolution.  C332 instead owns an externally driven moving convex
set, its one-period projection semigroup, memory interval, and exact hysteresis
area.

**Proof boundary.**  The theorem is scalar and single-peak.  Multipeak inputs,
higher-dimensional moving sets, and arbitrary hysteresis networks are separate
owners.  The `r=0`, `D=0`, threshold, plateau, and corner faces remain explicit.
The forcing period is not an arithmetic clock.

**Strict tuple.**
`(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`;
Route A rejected and Route B locked.

### C333 -- complete-graph randomized gossip covariance

**Owner.**  On `R^N`, choose one unordered edge `{i,j}` of the complete graph
uniformly at each discrete time and apply

`W_ij=I-eta*(e_i-e_j)(e_i-e_j)^T`, `0<=eta<=1`.

The conserved mean is removed by `P=I-J/N`, leaving a random product on
`1^perp`.

**Large step.**  Prove the exact first-moment law and diagonalize the full
second-moment operator

`T_eta(A)=average_(i<j) W_ij A W_ij`

on `Sym^2(1^perp)`.  Its scalar, standard, and `[N-2,2]` blocks have eigenvalues

`lambda0=1-4eta(1-eta)/(N-1)`,
`lambda1=1-(4eta-2eta^2)/(N-1)`,
`lambda2=1-4eta/(N-1)+4eta^2/[N(N-1)]`,

with multiplicities `1`, `N-1`, and `N(N-3)/2`, respectively, whenever the
blocks exist.  Give explicit projection formulas and the complete covariance
evolution.  Deduce the sharp identity

`E||y_t||^2=lambda0^t||y_0||^2`,

its exact probability tail bound, and almost-sure consensus for
`0<eta<1`.

**Nearest collision.**  C203 is a deterministic signed-Laplacian consensus
flow, C312 is state-dependent finite-time Hegselmann--Krause averaging, C183 is
the permutation-valued `eta=1` random-transposition boundary, and C322 is a
continuous energy-sphere Kac collision process.  C333 owns the dissipative iid
pair product and its complete covariance representation.

**Proof boundary.**  The result uses uniform edges of `K_N`; no arbitrary graph
or nonuniform-edge spectrum is inferred.  `N=1,2,3`, `eta=0`, the one-step
averaging face, and `eta=1` random swaps are separated.  A self-adjoint
second-moment transfer is only a formal source hint, not a unitary lift or
target determinant.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`; Route A rejected.

## Historical ownership and scope firewall

The source locks are Paley for the quadratic-residue graph, Hashimoto and Bass
for finite graph zeta, Romik for Pythagorean-triple dynamics, Dirac and
Wu--Yang for monopole charge and harmonics, Moreau for moving-convex-set
evolution, and Boyd--Ghosh--Prabhakar--Shah for randomized gossip.  Each package
claims a proof-complete, executable reconstruction inside its frozen
convention, not priority over those ingredients.

No retained package introduces target arithmetic local data, a target Euler
factor, bad-prime data, root numbers, automorphy, a target divisor/counting law
or functional equation, a target zero match, a Hilbert--Polya operator, or
Route-B authorization.  Paley/Romik source zetas and the monopole spectral
series remain source-side objects only.
