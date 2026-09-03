# Route-A idea report: C339--C343

## Round objective and frozen baseline

The user requested another batch of exactly five finished papers, with a
substantial theorem in every paper and a change of dynamical subtype whenever
a proposal would merely extend an existing owner.  The scan covered the
C1--C338 candidate registry, obstruction records, earlier idea reports,
directory owners and mechanism-level neighbors.  Direct collisions such as
Jaynes--Cummings, open TASEP, M/M/infinity, the finite M/M/1/K queue, the
Gauss/Selberg transfer-operator line and another ordinary quantum walk were
discarded.

This round freezes five independent mechanisms: a Katok--Zermelo Randers
geodesic flow, the one-gap Lame Hill operator, switch--walk--switch
lamplighter dynamics, directed edge reinforcement, and Erlang-distributed
memory.  No paper is a deferred section or a parameter slice of another.

The collision baseline is
`e2d94f886963cbe3d42b83f6ef542413a163d3a4`, the fixed date is 2026-09-03,
and the build epoch is `1788393600`.  Every candidate is evaluated under
`flow_systems/skills/route-a-evaluator.md` v0.2.0, SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`,
with literal scope `NO_BAD_EULER_OR_ROOT_NUMBER`.  `NEW` below means only
that the frozen theorem has no owner elsewhere in this workspace; it is not a
claim of literature priority.

## Frozen candidates

### C339 -- Katok--Zermelo two-geodesic Randers sphere

**Owner.**  Freeze the unit round sphere with Killing wind
`W=epsilon partial_phi`, `0<|epsilon|<1`, and the strongly convex
nonreversible Randers metric produced by Zermelo navigation.

**Large step.**  Prove that every unit Finsler geodesic is the wind flow
applied to a round great circle.  If `epsilon` is irrational, show that the
two orientations of the equator are the only oriented prime closed
geodesics, with

`T_+=2*pi/(1+epsilon)` and `T_-=2*pi/(1-epsilon)`.

Derive constant flag curvature one, the transverse Jacobi equation, the
Poincare multipliers and
`det(I-P_\pm)=4 sin^2(T_\pm/2)`.  Close zero wind, rational wind, sign reversal
and the loss of strong convexity at `|epsilon|=1` without forgetting that
orientation is physical for a nonreversible metric.

**Nearest collision.**  C305 is Euclidean constant-wind time optimization,
C313 is the reversible round Zoll clean family, C242 is an ellipsoid Reeb
flow, and C289/C331 are magnetic flows.  None owns the nonreversible
navigation metric and its complete irrational closed-geodesic atlas.

**Proof boundary.**  Finite rational-return tables are regression evidence;
orbit exhaustion comes from the great-circle plus wind-return argument.

**Strict tuple.**
`(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`; Route A is
rejected and Route B is locked.

### C340 -- complete one-gap Lame spectrum

**Owner.**  Freeze

`H_k=-d^2/dx^2+2*k^2*sn^2(x,k)` on `L2(R)`, `0<k<1`,

with real period `2 K(k)` and the standard self-adjoint realization.

**Large step.**  Prove

`sigma(H_k)=[k^2,1] union [1+k^2,infinity)`,

purely absolutely continuously.  Verify the exact periodic edge
`dn(x,k)` at `k^2` and antiperiodic edges `cn(x,k)` and `sn(x,k)` at `1`
and `1+k^2`; construct the Bloch/commuting-operator algebraic curve that
proves every higher gap is closed.  Retain the `k=0` free limit and the
`k up-arrow 1` Poschl--Teller soliton limit.

**Nearest collision.**  C262 treats a two-step piecewise-constant Hill
coefficient, C327 a singular delta comb with infinitely many gaps, and
C231/C221 nonperiodic soliton Hessians.  The smooth elliptic one-gap
completeness theorem is not owned by any of them.

**Proof boundary.**  Three explicit edge functions alone do not prove the
absence of higher open gaps; the finite-gap identity is mandatory.

**Strict tuple.**
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`; Route A is
rejected and Route B is locked.

### C341 -- finite-cycle lamplighter full spectrum

**Owner.**  On `Omega_n=Z_2^(C_n) x C_n`, first independently resample the
lamp at the current site fairly, take one step of the lazy cycle kernel
`Q(x,x)=1/2`, `Q(x,x+-1)=1/4`, and fairly resample the lamp at the arrival
site.

**Large step.**  Fourier-transform the lamp variables and prove the complete
orthogonal block decomposition

`P = direct-sum_(A subset C_n) D_A Q D_A`.

The nonempty blocks split into killed paths, whose length-`ell` eigenvalues
are `1/2+(1/2)cos(pi*j/(ell+1))`; the empty block is the intact lazy cycle.
From these data derive the complete characteristic polynomial and
multiplicities for the full `n*2^n` state chain, an explicit Walsh--sine
eigenbasis and, for `n>=3`, the sharp gap
`(1-cos(pi/n))/2` with top slow-mode multiplicity `n`.

**Nearest collision.**  C171 is independent hypercube bit flipping, C183 is
random transposition, C192 is a hyperplane chamber walk and C338 is Wilson
cycle popping.  None contains a moving lamp carrier and the full killed-path
Walsh decomposition.

**Proof boundary.**  Fair randomization is not deterministic toggling;
`n=1`, the merged-neighbor convention at `n=2`, the empty/full killed sets
and the absence of an infinite-volume claim are explicit.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`; Route A is rejected and
Route B is locked.

### C342 -- directed reinforcement as a Dirichlet environment

**Owner.**  Freeze a finite strongly connected directed multigraph with
labelled parallel arcs, at least one outgoing labelled arc at every vertex,
and positive initial weights `alpha_e`.  At vertex `v`, choose outgoing arc
`e` with probability
`(alpha_e+N_e)/(alpha_v+N_v)`.

**Large step.**  Derive the exact rising-factorial probability of every
legal path.  Independently integrate the same path probability against
row-wise independent
`Dirichlet((alpha_e)_(tail(e)=v))` transition vectors and prove equality of
the annealed laws.  Give the complete row-wise conjugate posterior and
predictive law.  Conditional irreducibility on the finite strongly connected
graph then yields almost-sure limits

`N_e(t)/N_tail(e)(t) -> omega_e`,
`N_v(t)/t -> pi_omega(v)`, and
`N_e(t)/t -> pi_omega(tail(e))*omega_e`,

together with exact Dirichlet means and covariances.

**Nearest collision.**  C263 is one global Polya urn, C338 uses fixed random
stacks, and C181 is deterministic rotor routing.  C342 owns a path-indexed
family of interacting vertex urns and the resulting random Markov
environment.  It does not invoke the unrelated undirected ERRW magic
formula.

**Proof boundary.**  Outdegree-one rows, labelled parallel arcs, positive
support and the non-strongly-connected final-class limitation are explicit;
quenched and annealed laws are never conflated.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`; Route A is rejected and Route B
is locked.

### C343 -- Erlang-2 distributed-memory stability atlas

**Owner.**  Freeze

`x'(t)=-a*x(t)-b*integral_0^infinity r^2*s*exp(-r*s)*x(t-s) ds`,

where `a,b>=0` and `r>0`, on compatible fading-memory histories.

**Large step.**  Prove exact equivalence with the three-dimensional chain

`x'=-a*x-b*z_2`, `z_1'=r*(x-z_1)`, `z_2'=r*(z_1-z_2)`.

For

`p(lambda)=(lambda+a)(lambda+r)^2+b*r^2`,

prove exponential stability exactly when
`b<2*(a+r)^2/r` for `b>0`.  At equality, factor
`p=(lambda+a+2r)(lambda^2+r*(r+2a))`, derive the crossing frequency and
transversality, and prove that above the wall exactly two roots lie in the
right half-plane.  Classify the discriminant/repeated-root locus and Jordan
sizes, including `b=0`, `a=r`, the constant mode and instantaneous-memory
limit.

**Nearest collision.**  C210 is a discrete-delay equation with an infinite
Lambert-W root array, C272 is an age-structured renewal transport equation,
and C218 is a Kelvin--Voigt wave PDE.  None owns a normalized distributed
delay with this complete finite-chain Routh/Hopf/Jordan atlas.

**Proof boundary.**  The theorem proves a linear imaginary-axis crossing,
not a nonlinear Hopf-bifurcation theorem or periodic-orbit existence.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`; Route A is rejected and Route B
is locked.

## Source and scope boundary

Primary source families are Ziller and Bao--Robles--Shen for Katok navigation;
Ince and standard Lame/Floquet references for the one-gap operator;
Lehner--Neuhauser--Woess for finite lamplighter harmonic analysis;
Enriquez--Sabot for the directed-reinforcement correspondence,
Diaconis--Freedman for partial-exchangeability lineage, and Sabot--Tournier
for an authoritative Dirichlet-environment overview; and Boese plus
Hurtado--Kirosingh for gamma-delay stability and the linear-chain trick.
Packages claim only self-contained
reconstruction and explicitly identified source-local consequences, never
priority over those results.

No retained package introduces target arithmetic local data, target Euler
factors, bad-prime data, root numbers, automorphy, a target divisor/counting
law or functional equation, a target zero match, a Hilbert--Polya operator,
or Route-B authorization.
