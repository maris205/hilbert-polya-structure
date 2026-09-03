# Route-A idea report: C334--C338

## Round objective and frozen baseline

The user requested another group of exactly five finished papers, with one
theorem-scale advance in each paper and a change of dynamical subtype whenever
a proposal would merely prolong an existing owner.  The collision scan covered
the C1--C333 registries, obstruction records, earlier idea reports, directory
owners and mechanism-level neighbors.  Ordinary rowmotion and the cat map were
discarded because the workspace already has direct owners; several safe but
smaller Markov-chain and reaction--diffusion proposals were displaced by five
results with stronger complete-theorem closures.

This round freezes five mechanisms: a Morse Hamiltonian and its natural
Schrodinger quantization, an exponential shot-noise decay process, a finite
Crow--Kimura mutation--selection flow, an integer-resonant Floquet rotor, and
Wilson's cycle-popping dynamics for weighted spanning trees.  None is a
deferred section or parameter slice of another retained paper.

The collision baseline is
`db2c816b7b6bd450f51f79b91842cb882b0bd773`, the fixed date is 2026-09-03,
and the build epoch is `1788393600`.  Every candidate is evaluated under
`flow_systems/skills/route-a-evaluator.md` v0.2.0, SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`,
with literal scope `NO_BAD_EULER_OR_ROOT_NUMBER`.  `NEW` below means only that
the frozen theorem has no owner elsewhere in this workspace; it is not a
claim of literature priority.

## Frozen candidates

### C334 -- Morse action and finite bound spectrum

**Owner.**  Freeze

`H=p^2/(2m)+D(exp(-2ax)-2exp(-ax))`, with `m,D,a>0`,

and its Friedrichs Schrodinger realization on the real line.

**Large step.**  Classify all classical energy chambers.  For `-D<E<0`,
derive both turning points and prove

`J(E)=sqrt(2mD)/a * (1-sqrt(-E/D))`,

`T(E)=2*pi/(a*sqrt(-2E/m))` and `dJ/dE=T/(2*pi)`.
With `lambda=sqrt(2mD)/(a*hbar)`, derive every and only bound energy

`E_n=-(a^2*hbar^2/(2m))*(lambda-n-1/2)^2`,

for integers `0<=n<lambda-1/2`, together with the Laguerre eigenfunctions,
node count, essential spectrum `[0,infinity)`, and the fact that equality at
zero energy is not an `L^2` bound state.

**Nearest collision.**  C250 owns Ermakov--Pinney/isotonic action, C232 the
Duffing oscillator, C295 the isochrone potential, and C216 the Kepler radial
problem.  None owns the Morse dissociation threshold and finite quantum bound
ladder.

**Proof boundary.**  The solvable molecular well supplies an analytic action
and a natural source quantization.  Neither supplies a rational-prime clock,
target determinant or Hilbert--Polya operator.

**Strict tuple.**
`(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`;
Route A rejected and Route B locked.

### C335 -- exponential shot-noise Ornstein--Uhlenbeck process

**Owner.**  Freeze `dX_t=-gamma X_t dt+dJ_t`, where `J` is compound Poisson
with intensity `kappa` and independent exponential marks of rate `beta`.

**Large step.**  Derive the pathwise mild solution and the complete transition
Laplace transform

`E_x exp(-sX_t)=exp(-s exp(-gamma t)x)`
` *((beta+s exp(-gamma t))/(beta+s))^(kappa/gamma)`.

Prove the unique stationary `Gamma(kappa/gamma,beta)` law, all cumulants
`kappa*(n-1)!/(gamma*beta^n)`, stationary covariance
`kappa exp(-gamma |t|)/(gamma beta^2)`, and the eigenvalue list
`0,-gamma,...,-m gamma` on every degree-at-most-`m` polynomial filtration.

**Nearest collision.**  C265 is self-exciting Hawkes, C233 is
`M/M/infinity`, C229 is CIR diffusion, and C328 is a two-velocity
run-and-tumble process.  C335 instead owns external compound-Poisson jumps
with deterministic exponential decay.

**Proof boundary.**  The polynomial filtration is finite dimensional.  It is
not promoted to a complete `L^2` spectral theorem, and the source stochastic
semigroup has no isolated arithmetic primitive ledger.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`; Route A rejected and Route B
locked.

### C336 -- Crow--Kimura single-peak quasispecies

**Owner.**  On binary strings of length `L`, freeze

`A_L=(U/L) sum_i(F_i-I)+s |0><0|`,

`p'=A_L p-(1^T A_L p)p`, with `U,s>0`.

**Large step.**  Prove the exact projectivization
`p(t)=exp(tA_L)p(0)/(1^T exp(tA_L)p(0))` and Perron convergence.  The mutation
operator has Hamming-layer eigenvalues `d_k=-2Uk/L`.  Rank-one selection
preserves `d_k` with multiplicity `binom(L,k)-1`; the remaining `L+1` simple
eigenvalues are precisely the roots of

`1=(s/2^L) sum_{k=0}^L binom(L,k)/(lambda+2Uk/L)`.

Prove one root above zero and one in every adjacent mutation gap, identify the
exact projective convergence gap, and close `s=0`, `U=0` and `L=1`.

**Nearest collision.**  C171 is the unselected Ehrenfest hypercube, C253 is
Moran fixation, C200 is Wright--Fisher and C271 is network SIS.  C336 owns the
rank-one single-peak selection perturbation and the full finite-genome
mutation--selection spectrum.

**Proof boundary.**  Finite `L` has an analytic, strictly interlacing
eigenvalue atlas.  The package does not claim a singular infinite-genome
error-threshold theorem.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`; Route A rejected and Route
B locked.

### C337 -- integer-resonant quantum kicked rotor

**Owner.**  Freeze the Floquet operator

`U_tau=exp(-i tau n_hat^2/2) exp(-i kappa cos(theta))`

on the momentum lattice, restricted to `tau=2*pi*ell` with integer `ell`.

**Large step.**  For even `ell`, prove that the free factor is the identity,
so every time kernel is

`<n|U^t|m>=(-i)^(n-m) J_(n-m)(kappa t)`.

Derive exact survival and momentum moments, including ballistic variance
`kappa^2 t^2/2`.  For odd `ell`, prove the free factor is the half-turn and
`U^2=I`, producing exact antiresonance.  Close arbitrary momentum-eigenstate,
zero-kick, operator-order and parity boundaries.

**Nearest collision.**  C178 is a harmonic metaplectic strobe, C143 is a
coined quantum walk, C148 is an open quantum baker, and C224 is Landau--Zener.
No retained owner has the infinite momentum lattice's primary resonance and
antiresonance sheet.

**Proof boundary.**  General rational resonances and detuning are left to
separate owners.  Natural unitarity is source quantization only.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`; Route A rejected
and Route B locked.

### C338 -- Wilson cycle-popping and weighted spanning trees

**Owner.**  On a finite connected undirected conductance graph with root
`r`, assign every nonroot vertex an independent infinite stack of outgoing
neighbors with probabilities proportional to conductance.  A legal move pops
a directed cycle in the current pointer graph.

**Large step.**  Prove almost-sure finite termination and the abelian fact that
the popped stack cells and terminal rooted tree do not depend on legal pop
order.  Identify the sequential version with Wilson loop-erased random walk,
prove

`P(T)=prod_(e in T)c_e / det(L_c^(r))`,

and, for distinct oriented edges, prove the transfer-current determinant for
all joint inclusion probabilities, with `P(e in T)=c_e R_eff(e)` as its
one-edge face.

**Nearest collision.**  C176 sandpile translation and C181 rotor-router
unicycles both touch spanning trees but are deterministic group/rotor owners.
C338 owns random infinite stacks, loop erasure, the weighted tree measure and
its determinantal edge law.

**Proof boundary.**  The matrix-tree and transfer-current determinants are
source graph identities.  They are not target Euler factors, target zeta
data, rational-prime local factors or a Hilbert--Polya construction.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`; Route A rejected and Route
B locked.

## Historical ownership and scope firewall

The source locks are Morse for the solvable molecular potential,
compound-Poisson shot-noise theory for exponential decay, Crow and Kimura for
the parallel mutation--selection model, the kicked-rotor resonance literature
for the Floquet parity sheet, Wilson for loop-erased random spanning-tree
sampling, and Burton--Pemantle for transfer currents.  Each package claims a
proof-complete, executable reconstruction inside its frozen convention, not
priority over those ingredients.

No retained package introduces target arithmetic local data, a target Euler
factor, bad-prime data, root numbers, automorphy, a target divisor or counting
law, a target functional equation, a target zero match, a Hilbert--Polya
operator, or Route-B authorization.
