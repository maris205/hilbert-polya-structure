# Route-A idea report: C309--C313

## Round objective and frozen baseline

The user requested exactly five independent papers, each making one
theorem-scale advance rather than splitting one result into installments.
This round deliberately changes state space, clock, and proof mechanism in
every slot.  The collision baseline is
`b3e2f3f7207b85d7be942ff72b1f49e754615c76`, the fixed date is 2026-09-03,
and the build epoch is `1788393600`.  Every candidate is evaluated under
`flow_systems/skills/route-a-evaluator.md` v0.2.0, SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`,
with literal scope `NO_BAD_EULER_OR_ROOT_NUMBER`.

The collision scan covered the C1--C308 package registry, recent batch
reports, model owners, and mechanism-level neighbors.  The retained systems
are:

1. an all-dimensional nonlinear matrix differential equation;
2. a planar bounded-curvature time-optimal control problem;
3. a nonlinear chemical reaction oscillator at Hopf bifurcation;
4. a finite-agent discontinuous confidence-network map; and
5. a maximally periodic Hamiltonian flow coupled to its native elliptic
   operator.

`NEW` below means only that the frozen theorem has no owner elsewhere in this
workspace.  It is not a literature-priority claim.

## Frozen candidates

### C309 -- symmetric matrix Riccati Mobius flow

**Owner.**  On the real vector space of symmetric `n` by `n` matrices,
`n>=1`, solve

`Xdot=I-X^2`, `X(0)=X0`.

**Large step.**  Lift the equation to `Udot=V`, `Vdot=U` and derive the
matrix Mobius solution

`X(t)=(sinh(t) I+cosh(t) X0)(cosh(t) I+sinh(t) X0)^(-1)`.

Use the spectral theorem to close the complete signed-time pole and maximal
interval atlas, including simultaneous poles.  Prove that forward
globality is equivalent to `lambda_min(X0)>=-1`, identify the exact limit
`I-2P_{lambda=-1}` and its support-dependent exponential rate, and derive
the trace-gradient identity for `Phi(X)=tr(X^3/3-X)`, excluding every
nonconstant recurrent trajectory.  Classify all symmetric-involution
equilibria as Grassmann components and compute stable, unstable, and center
dimensions `p(p+1)/2`, `q(q+1)/2`, and `pq`.  Finally, prove the full
Loewner divided-difference formula for the Frechet derivative of every
regular time map.

**Nearest collision.**  C185 is an isospectral double-bracket flow, C297
has one scalar projective Riccati coordinate in a two-mode PT system, and
C298 evolves fixed-rank projections on a Grassmannian.  None owns an
all-dimensional moving-spectrum matrix Riccati flow together with the full
pole atlas, involution Morse--Bott geometry, and Loewner derivative.

**Proof status.**  `PROVABLE AS STATED` for every finite dimension.  The
finite block lift is source geometry only and is not promoted to a target
operator.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`; Route A rejected.

### C310 -- boundary-safe Dubins optimal synthesis

**Owner.**  Normalize a forward planar car to unit speed and unit curvature
bound, start at `(0,0,0)`, and prescribe terminal pose `(x,y,phi)`.  Radius
scaling restores every positive speed/curvature scale.

**Large step.**  Freeze one coordinate convention and derive all six global
candidate families `LSL`, `RSR`, `LSR`, `RSL`, `RLR`, and `LRL`, with four
square-root feasibility discriminants and two three-circle cosine tests.
Replay every feasible word by exact segment integration before minimizing.
Close zero-length pieces, coincident poses, tangent discriminants, the
`atan2(0,0)=0` convention, the `2*pi mod 2*pi=0` face, complete ties,
reflection, and scale covariance.  The result is a deterministic set-valued
global minimizer, not merely six generic formulas.

**Nearest collision.**  C222 is a second-order double-integrator bang--bang
problem, C270 is Heisenberg sub-Riemannian control, and C305 is
constant-wind Euclidean navigation.  None has the nonholonomic Dubins car,
its six-word reduction, or the full analytic feasibility/degeneracy atlas.

**Proof status.**  `PROVABLE AS STATED` using the classical Dubins reduction
plus exhaustive analytic evaluation of the six families.  Obstacles,
reverse gear, and spatially variable curvature bounds are outside scope.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`; Route A rejected.

### C311 -- Brusselator Hopf normal form

**Owner.**  For `A>0`, `B>=0`, consider the dimensionless Brusselator

`xdot=A-(B+1)x+x^2 y`, `ydot=Bx-x^2 y`.

**Large step.**  Prove positive-quadrant invariance and global forward
existence from `(x+y)dot=A-x`.  Identify the unique equilibrium `(A,B/A)`
and close its complete node, defective-node, focus, and Hopf chamber atlas,
whose boundaries are `(A-1)^2`, `1+A^2`, and `(A+1)^2`.  At
`B=1+A^2`, fix normalized right/left eigenvectors, derive the complete
quadratic/cubic multilinear tensors and obtain

`G21=-(1+2/A^2)-i(4A^4-7A^2+4)/(3A^3)`.

In the stated Kuznetsov convention,
`l1=-(A^2+2)/(2A^3)<0`; hence the Hopf branch is supercritical and locally
stable.  Derive its leading physical amplitude
`r^2=A^2(B-1-A^2)/(A^2+2)+O((B-1-A^2)^2)`, first harmonic, and frequency
correction, while explicitly declining any global uniqueness claim for
cycles.

**Nearest collision.**  Earlier packages contain linear oscillators,
Hamiltonian centers, and relaxation semigroups, but none derives a complete
parameter-plane linear atlas and an exact convention-audited Lyapunov
coefficient for this nonlinear chemical oscillator.

**Proof status.**  `PROVABLE AS STATED` locally at Hopf and globally only
for positivity/existence.  The scope does not contain a global limit-cycle
attractor theorem.

**Strict tuple.**
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`; Route A rejected.

### C312 -- one-dimensional Hegselmann--Krause finite termination

**Owner.**  For ordered agents on the line, update synchronously by the
average of all agents at closed distance at most `epsilon>0`.

**Large step.**  Prove order preservation, coincident-block persistence,
convex-hull contraction, and permanent decomposition across every gap
larger than `epsilon`.  Reproduce the decisive two-step progress lemma and
turn it into the explicit safe stopping bound `4n^3+2n+2`.  Characterize
all fixed points exactly as equal-position clusters separated by more than
`epsilon`, and identify every strict neighbor cell with a rational
row-stochastic linear map.  Isolate a commonly missed invariant failure:
the arithmetic mean is not conserved, with the exact trajectory
`(0,1/2,7/5) -> (1/4,19/30,19/20)` changing its mean from `19/30` to
`11/18`.

**Nearest collision.**  C171 and C183 are time-homogeneous finite Markov
chains, C301 is a random absorbing partition refinement, and C307 is
monotone random-graph growth.  None owns a deterministic discontinuous
state-dependent confidence graph with an all-size finite-termination proof,
fixed-cluster atlas, and exact cell matrices.

**Proof status.**  `PROVABLE AS STATED` in one dimension for homogeneous
closed confidence balls and synchronous updates.  Heterogeneous,
asynchronous, noisy, and higher-dimensional variants are separate models.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`; Route A rejected.

### C313 -- round-sphere geodesic and Laplace atlas

**Owner.**  On the round sphere `S_R^d`, `d>=2`, take the unit tangent
geodesic flow and the Laplace--Beltrami operator of the same fixed metric.

**Large step.**  Solve the flow in embedding coordinates and prove that
every orbit has least period `2*pi*R`.  Classify every time-map fixed set:
the whole unit tangent bundle at integer periods and the empty set
otherwise.  Prove the return differential is the identity, so the family is
maximally clean, identify the oriented-Grassmann orbit quotient, and close
the reversor and Liouville invariance.  On the operator side, derive the
spherical-harmonic eigenvalues `ell(ell+d-1)/R^2`, their exact
multiplicities, and the heat trace.  Completing the square gives

`Q=sqrt(-Delta+(d-1)^2/(4R^2))`,

whose one-period propagator is `(-1)^(d-1) I` and whose two-period
propagator is exactly the identity.

**Nearest collision.**  C242 has isolated Reeb orbits on an irrational
ellipsoid and C295 has action variables for the Henon isochrone.  Neither
owns a maximally clean common-period geodesic fibration, its oriented
Grassmann quotient, and an exact source-Laplacian revival in one theorem.

**Proof status.**  `PROVABLE AS STATED` for the fixed round metric.  The
maximal degeneracy is retained rather than misreported as isolated orbit
evidence.

**Strict tuple.**
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`; Route A
rejected.

## Rejected and reserved alternatives

- An Ermakov--Pinney/isotonic action package was rejected from this batch
  because its integrable central-force mechanism is too close to C295 and
  did not enlarge the subtype spread.
- A hysteretic relay oscillator was reserved because convention-dependent
  switching surfaces would require a longer independent well-posedness
  audit than the present theorem increment.
- Further first-passage refinements of the earlier finite Yukawa-mark chain
  were excluded: they would split one existing model into several small
  papers, contrary to the user contract for this round.
- A generic compact Zoll-manifold claim was rejected in favor of the round
  sphere, where orbit geometry, clean return, multiplicities, and quantum
  revival can all be proved exactly without hidden genericity assumptions.

No retained package introduces target arithmetic local data, target Euler
factors, bad-prime data, root numbers, automorphy, a target divisor/counting
law or functional equation, a target zero match, a Hilbert--Polya operator,
or Route-B authorization.
