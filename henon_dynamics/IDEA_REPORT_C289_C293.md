# Route-A idea report: C289--C293

## Round objective and frozen baseline

The user requested five independent papers, each making one complete
theorem-scale advance rather than splitting one calculation into five
installments.  The collision baseline is
`7fbe9db30cc460a82883533d7cfb2edd988c5b65`, the fixed date is 2026-09-02,
and the build epoch is `1788307200`.  Every candidate is evaluated under
`flow_systems/skills/route-a-evaluator.md` v0.2.0, SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`,
with literal scope `NO_BAD_EULER_OR_ROOT_NUMBER`.

Three independent landscape scans covered all C1--C288 package titles, the
candidate and obstruction registries, recent idea reports and kill ledgers,
and neighboring symbolic/flow owners.  The retained systems change state
space, clock, and proof mechanism in every slot:

1. a smooth magnetic flow on a negatively curved surface;
2. a singular celestial Hamiltonian with two fixed primaries;
3. a stochastic irreversible adsorption process on finite graphs;
4. an event-driven inertial aggregation system and conservation law;
5. a degenerate magnetic quantum operator on a noncompact cylinder.

`NEW` below means only that no earlier workspace package owns the frozen
theorem.  It is never a claim of priority in the literature.

## Frozen candidates

### C289 -- constant magnetic flow on the hyperbolic plane

**Owner.**  On the simply connected surface of curvature `-kappa^2`, freeze
`D_t dot(gamma)=b J dot(gamma)` at speed `v`.

**Large step.**  Prove for every initial condition that the signed geodesic
curvature is `b/v` and close the sharp four-chamber classification.  Strong
field `|b|>kappa v` gives oriented hyperbolic circles with primitive period
`2 pi/sqrt(b^2-kappa^2 v^2)`; equality gives nonclosed horocycles; weak
nonzero field gives equidistant hypercycles; zero field gives geodesics.  A
Frenet proof and an independent `SO^+(2,1)` generator proof must agree,
including the `v=0`, flat-curvature, orientation, and threshold faces.

**Nearest collision.**  C268 is a flat-spacetime Lorentz flow, C270 is a
Heisenberg sub-Riemannian geodesic problem, and C138 is a finite magnetic
quantum graph.  None owns the negative-curvature circle/horocycle/hypercycle
transition.

**Proof status.**  `PROVABLE AS STATED`, provided the critical orbit is never
called periodic and the closed circles are treated as a clean continuum,
not as isolated UPOs.

**Strict tuple.**
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`; overall Route A
rejected.

The magnetic Laplacian is only a formal lift hint in this classical package:
no Hilbert-space domain, self-adjoint realization, orbit phases, or quantum
spectrum is constructed here.

### C290 -- planar CR3BP Lagrange-point stability atlas

**Owner.**  The normalized planar circular restricted three-body problem
with primary masses `1-mu,mu`, fixed at `(-mu,0)` and `(1-mu,0)`, for
`0<mu<=1/2`.

**Large step.**  Prove that there are exactly five equilibria.  The three
collinear points are unique on their three singularity-complement intervals,
have `S=(1-mu)/r_1^3+mu/r_2^3>1`, and are always saddle--center.  The two
triangular points have characteristic polynomial
`lambda^4+lambda^2+27 mu(1-mu)/4`.  At
`mu_R=(9-sqrt(69))/18`, the two imaginary pairs collide: below `mu_R` they
are distinct and elliptic, at equality each eigenvalue is algebraically
double but geometrically simple and produces linear growth, and above it
they form a Hamiltonian quartet.  The proof starts from the original
rotating vector field and closes `mu=1/2`, collision singularities, Jacobi
conservation, and the excluded `mu=0` circle of equilibria.

**Nearest collision.**  C216 is the single-center Kepler problem, C274 is a
linear Penning trap, and C284 is a point-vortex polygon.  None has two
singular primaries, five equilibrium branches, or the Routh--Gascheau
Hamiltonian-Hopf boundary.  C284's idea report explicitly reserved CR3BP as
viable.

**Proof status.**  `PROVABLE AS STATED`.  Any text calling the critical mass
ratio linearly stable, or replacing the all-`mu` proof by a finite scan,
would fail the gate.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`; overall Route A rejected.
The equilibrium theorem supplies no intrinsic primitive-periodic family;
nearby Lyapunov families are outside this paper and therefore do not raise A1.

### C291 -- finite path/cycle dimer random sequential adsorption

**Owner.**  Assign iid continuous priorities to graph edges and greedily
accept an edge exactly when both endpoints are still unmatched.  Freeze the
path `P_n` and simple cycle `C_n` laws.

**Large step.**  For the terminal matching size `M_n`, prove the exact path
PGF recurrence

`(n-1)F_n(z)=z sum_(a+b=n-2) F_a(z)F_b(z)`

and its Riccati bivariate OGF.  Close the triangular hierarchy for all
factorial moments, the exact mean generating function, linear mean and
variance asymptotics, and the complete support interval
`ceil((n-1)/3),...,floor(n/2)`.  For cycles prove
`G_n(z)=zF_(n-2)(z)`, the exact inherited variance/support, and the limiting
path--cycle mean correction `e^-2`.  The terminal object is maximal, not
necessarily maximum.

**Nearest collision.**  C175 Rule 184, C181 rotor routing, and C220 open
TASEP use graph locality or exclusion, but none has random greedy matching,
first-edge convolution, or finite path/cycle PGFs.

**Proof status.**  `PROVABLE AS STATED`; exhaustive edge orders are regression
evidence only, while the recurrence, singular expansion, and maximal-matching
constructions carry the all-`n` claims.

**Strict tuple.**  All five axes fail; overall Route A rejected.

### C292 -- arbitrary finite one-dimensional sticky particles

**Owner.**  Positive masses at ordered positions move ballistically and
undergo perfectly inelastic, permanently sticky collisions.

**Large step.**  Construct the unique all-time flow for every finite system,
including simultaneous multi-cluster events.  Identify its position vector
with the mass-weighted isotonic projection of `x+t v`, equivalently the
slopes of a lower convex hull in cumulative-mass coordinates.  Derive the
event partition, mass-weighted outgoing velocity, no-splitting property,
`N-1` merge bound, mass/momentum/center-of-mass conservation, and the exact
kinetic-energy loss at every event.  Finally verify the atomic mass and
momentum measures against the one-dimensional pressureless-Euler weak form
and energy entropy inequality.

**Nearest collision.**  C195 is viscous periodic Burgers, C228 is
spatially unstructured coagulation, and C279 is first-order path-TV
subgradient merging.  C292 is second-order ballistic, conserves momentum,
and satisfies the earlier kill ledger's explicit requirement that a Burgers
revival close arbitrary finite all-event interactions.

**Proof status.**  `PROVABLE AS STATED` after the frozen convention that
initially coincident particles are premerged.  Zero masses are excluded,
equal-velocity noncollisions and time-reversal nonuniqueness are explicit.

**Strict tuple.**  All five axes fail; overall Route A rejected.

### C293 -- magnetic Baouendi--Grushin cylinder

**Owner.**  The Friedrichs-form realization on `L^2(R x S^1)` of
`G_alpha=-partial_x^2+x^2(-i partial_theta+alpha)^2`.

**Large step.**  Fourier--Hermite reduction gives the complete channel
spectrum `(2n+1)|k+alpha|`.  For noninteger flux prove compact resolvent and
pure point spectrum; at integer flux split off exactly one free continuous
channel and retain the embedded nonresonant oscillator levels.  On the
zero-flux nonresonant sector prove multiplicity `2 d_odd(N)`, the exact heat
trace, the source-local spectral series
`2(1-2^-s) zeta(s)^2`, and its `Lambda log Lambda` counting law.  Close flux
periodicity, reflection, half-flux degeneracy, rational/irrational
multiplicity, and the singular approach to integer flux.

**Nearest collision.**  C270 supplies sub-Riemannian geometry but no
spectral operator, C184 supplies a different compact spectral recursion, and
C288 is a rank-one Schrödinger extension.  None has a degenerate cylinder or
a flux-driven compact-to-continuous spectral transition.

**Proof status.**  `PROVABLE AS STATED` for the Friedrichs realization.  An
unproved essential-self-adjointness claim is excluded.

**Strict tuple.**
`(A0_WEAK_ARITHMETIC_RELATION,A1_FAIL,A2_FAIL,A3_PARTIAL_ANALYTIC_STRUCTURE,A4_NATURAL_QUANTIZATION)`.
The arithmetic signal is only a source-mode factorization; overall Route A
remains rejected and Route B is disabled.

## Rejected or reserved alternatives

- Geometric-offspring Galton--Watson was killed because C208 already owns the
  linear-fractional branching trichotomy, extinction/Yaglom behavior, and
  supercritical martingale limit.  Discrete time alone is not a new theorem
  skeleton.
- GSR riffle shuffle was killed because C194 already owns its multiplicative
  carries/riffle semigroup and descent marginal.
- The ordinary Aharonov--Bohm ring was replaced by C293 because C133/C138
  already own finite magnetic quantum graphs, whereas the Grushin cylinder
  exhibits a genuine compact/continuous transition.
- Linear Cahn--Hilliard is provable only as a full-dimensional semigroup,
  lattice-shell, energy, and singular-boundary atlas; the present library is
  already dense in Fourier semigroup packages, so it remains reserved.
- One-dimensional Hegselmann--Krause, Quicksort, and finite dimer RSA all
  survived collision screening.  Dimer RSA was retained because its single
  paper closes paths and cycles, the whole PGF hierarchy, exact support, and
  boundary asymptotics with a smaller direct-owner overlap than the other
  two.

No retained package introduces target arithmetic local data, target Euler
factors, root numbers, automorphy, a target divisor/counting law or functional
equation, a target zero match, a Hilbert--Polya operator, or Route-B
authorization.  C293's displayed source-local series remains on the source
side of that firewall.
