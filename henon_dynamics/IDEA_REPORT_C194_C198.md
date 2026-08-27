# Route-A idea report: C194--C198

Date: 2026-08-27

Source commit: `c3a5b9bbb3b6d0881f395abe4a01accd322f69cb`.

Evaluator: `flow_systems/skills/route-a-evaluator.md`, v0.2.0, SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.

Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Design objective

This round again implements the large-step rule literally: one complete
all-parameter dynamical theorem per paper, with a different mathematical owner
each time.  The five owners are positional-addition randomness, a nonlinear
parabolic PDE, a noncompact many-body Hamiltonian flow, an operator-splitting
algorithm, and a monotone compartmental ODE.  No theorem is cut into five
installments, and no finite regression grid is promoted to an all-family proof.

`NEW` below means only that C1--C193 does not already own the same frozen
dynamical theorem.  It is not a literature-priority or novelty claim.  Classical
sources retain ownership; the package contribution is the convention-locked
synthesis, new consequence ledger, executable certificate and strict Route-A
evaluation.

## Collision scan, kills and pivots

- **Holte carries retained.**  A generic second finite Markov spectrum would
  collide with C171, C183 and C192.  C194 survives only because the frozen owner
  is actual base-`b` column addition and the central theorem is the all-base
  semigroup `P_aP_b=P_ab`, Eulerian stationarity and complete simple spectrum.
  Riffle-shuffle language remains context, not the owner.
- **Rock breaking and Bernoulli--Laplace killed for this round.**  Both had
  credible full spectral theorems, but a second partition/orthogonal-polynomial
  Markov paper would weaken subtype diversity and sit too close to C190/C171.
  Kaprekar digit dynamics was also killed because its folded multiplier core
  was too near C172/C174.
- **Periodic viscous Burgers retained.**  C195 is not a finite-dimensional
  convergence example: the owner is the full periodic nonlinear PDE at every
  viscosity, circumference and mean, globally conjugated through the positive
  projective cone to the heat semigroup.  Its Galilean sign and first-active-mode
  theorem are mandatory.
- **Calogero--Moser retained with a title firewall.**  Generic “another Lax
  flow” language would collide with C185.  C196 survives by freezing the
  repulsive inverse-square many-body system and the free Hermitian pencil
  `Q_0+tL_0`, which gives all-`N` collision avoidance and noncompact scattering,
  not compact isospectral sorting.  Open Toda was not revived.
- **Kepler--Ligon--Schaaf and Chaplygin sleigh deferred.**  The former had a
  larger formula/regularization audit risk; the latter had a smaller theorem
  envelope.  Neither was weakened into a short paper.
- **Douglas--Rachford retained.**  C197 differs from C191's nonlinear
  positive-cone scaling: every pair of real subspaces and every real relaxation
  parameter are simultaneously classified by principal-angle blocks, including
  the orthogonal and unstable endpoints.
- **Closed SIR added as the fifth owner.**  Rather than select a second Markov
  chain, C198 closes a monotone nonlinear phase portrait with a branch-sensitive
  final-size theorem.  The zero-infection boundary, data-free mathematical
  scope and no-medical-advice firewall are mandatory.

No screened candidate supplied the simultaneous A0 requirements of rational
primes as primitive carriers, prime powers as repetitions and a logarithmic
clock.  Exact dynamics are retained; arithmetic semantics are not manufactured.

## Frozen independent theorem increments

### C194 — Holte carries at every base and width

For every `n>=1` and base `b>=2`, derive the exact carry transition matrix from
column addition, prove `P_aP_b=P_ab` and `P_b^r=P_(b^r)`, close the simple
spectrum `1,b^-1,...,b^{-(n-1)}`, Eulerian stationary law, eigenvectors, all
power traces, determinant and exact convergence.  Prime and composite bases
obey the same theorem; arithmetic relevance remains weak rather than a
prime-orbit law.

### C195 — periodic viscous Burgers through the positive heat cone

For every viscosity `nu>0`, circumference `L>0`, mean `m` and sufficiently
regular periodic initial datum, retain physical time and the Galilean shift
`x-mt`.  Prove global Cole--Hopf conjugacy on the positive projective cone,
unique constant equilibrium per mean leaf, absence of nonconstant recurrence,
the exact first-active-Fourier-mode asymptotic and the full equilibrium
linearization spectrum.

### C196 — repulsive rational Calogero--Moser free pencil

For every particle number `N>=2`, coupling `g>0` and ordered real initial
configuration, prove that particle positions are the ordered eigenvalues of
the Hermitian pencil `Q_0+tL_0`.  Close global collision avoidance and
completeness, the Lax integrals, asymptotic velocities and intercepts, ordering
reversal, complete scattering atlas and the no-bounded-nonconstant-periodic
boundary.  Finite `N` root tracking is regression, not the all-`N` proof.

### C197 — all-relaxation Douglas--Rachford dynamics

For every two linear subspaces in finite-dimensional real Hilbert space and
every real `lambda`, decompose the relaxed update into four intersection
spaces and all principal two-planes.  Derive the exact fixed space, convergence
window and operator-norm rate, unique uniform optimum, shadow limit,
trace/determinant factors, orthogonal rotation endpoint, finite-order criterion
and instability outside `[0,2]`.

### C198 — all-parameter closed SIR phase portrait

For every positive transmission/removal pair and nonnegative initial state,
reduce the mass-action system to `x'=-xy,y'=y(x-1)`.  One first integral must
close global positivity, peak, final-state convergence, lower/upper Lambert
branches, time quadrature, sensitivity, equilibrium-line stability and no
recurrence.  The `I0=0` upper-branch equilibrium is separate.  No clinical data
or medical prediction enter the package.

## Frozen strict expectations

| paper | A0 | A1 | A2 | A3 | A4 | overall |
|---|---|---|---|---|---|---|
| C194 | `A0_WEAK_ARITHMETIC_RELATION` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C195 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C196 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_NATURAL_QUANTIZATION` | `ROUTE_A_REJECTED` |
| C197 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C198 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FAIL` | `ROUTE_A_REJECTED` |

C194's positional-integer arithmetic is the only positive A0 signal, but it
does not label primitive cycles by rational primes or produce `log p`.  Every
Route-B flag remains false and no coordinate is transferred between papers.
