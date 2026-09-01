# Route-A idea report: C279--C283

## Round objective and baseline

This round was frozen from source commit
`51fb3d46f96b854314811c1ad62d3103cd5d54e5` under the user's instruction
to prefer Route A, take one theorem-scale step per paper, and change dynamical
subtype whenever a proposed owner would merely continue an earlier paper.
The five owners deliberately change state space, clock, randomness, and proof
technology:

1. a nonsmooth convex gradient flow on a finite path;
2. a projective orientation flow in a prescribed planar fluid gradient;
3. a nonlinear geometric metric flow on products of round spheres;
4. a killed compound-Poisson risk process;
5. a Fourier-multiplier Markov semigroup on a compact p-adic group.

The evaluator is `../flow_systems/skills/route-a-evaluator.md` v0.2.0 at
SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.
All proposals use fixed epoch `1788220800` and literal scope
`NO_BAD_EULER_OR_ROOT_NUMBER`.  They are source-local mathematical programs,
not claims of literature priority.

## Frozen candidates

### C279 -- path-graph total-variation flow

**Owner.**  The Euclidean subgradient flow of unweighted graph total
variation on the finite path `P_n`.

**Bold hypothesis.**  Path order should be strong enough to turn the abstract
maximal-monotone evolution into a complete finite coalescence algorithm and,
more surprisingly, make the continuous flow at every time equal the single
Rudin--Osher--Fatemi resolvent at that same time.

**Theorem-scale target.**  Prove global uniqueness, preservation of the
initial mean, finite-time consensus, explicit plateau flux and velocity,
no-splitting, joint treatment of simultaneous collisions, an `n-1` event
bound, and the all-time flow--ROF identity including collision and
post-consensus times.  Exact rational event enumeration must audit rather
than replace the arbitrary-real-data proof.

**Collision boundary.**  Earlier workspace packages do not own this
path-specific certificate, but Steidl--Weickert--Brox--Mrázek--Welk already
own the one-dimensional space-discrete TV-flow/regularization equivalence,
and Hoefling owns monotone fused-lasso fusion.  The honest residual is the
convention-complete event, boundary, proof, and executable closure.  No
literature originality is claimed, and the result is not extended to
branched, cyclic, weighted, or differently normalized graphs.

**Expected Route-A ceiling.**  Finite-time collapse leaves only constant
periodic points.  There is no rational-prime carrier, logarithmic prime clock,
primitive repetition law, source determinant, or same-clock unitary lift, so
the expected tuple is all fail.

### C280 -- Jeffery--Bretherton planar orientation flow

**Owner.**  The director of an axisymmetric spheroid in an arbitrary constant
incompressible planar linear flow, interpreted on projective orientation
space rather than on a chosen signed unit vector.

**Bold hypothesis.**  The nonlinear normalized director equation should be
the projectivization of one traceless `2 x 2` exponential.  A single signed
discriminant should therefore close elliptic, hyperbolic, nilpotent, identity,
least-period, stroboscopic, and aspect-ratio boundary behavior without
case-by-case quadrature.

**Theorem-scale target.**  Derive the exact projective lift, its
Cayley--Hamilton exponential, the complete discriminant atlas, fixed
directions and hyperbolic cells, the nilpotent shear limit, true projective
periods, stroboscopic fixed sets, and sphere-to-needle shape limits.  The
proof must keep director sign quotienting explicit and must not silently
replace prescribed orientation dynamics by coupled fluid--particle dynamics.

**Collision boundary.**  Classical Jeffery and Bretherton records establish
model lineage.  The retained advance is the source-local all-parameter
projective atlas and boundary closure, not a claim that the underlying
orientation equation is new.

**Expected Route-A ceiling.**  Elliptic periodic directions form clean
continua and hyperbolic chambers have only projective fixed directions.
Continuous fluid parameters provide at most a weak primitive analogy and no
intrinsic arithmetic clock, determinant bridge, or quantization.

### C281 -- homogeneous Ricci flow on products of round spheres

**Owner.**  The unnormalized Ricci flow of an arbitrary diagonal product
metric `g(0)=direct_sum_i a_i g_round` on
`M=product_i S^{d_i}`, including flat circle factors.

**Bold hypothesis.**  The product geometry should turn the nonlinear
geometric PDE into an exactly solvable affine scale flow while still
retaining a nontrivial singularity atlas: every tied collapse, curvature and
volume exponent, pointed Type-I model, and the distinction between finite
and infinite volume-normalized time should be classifiable in all
dimensions.

**Theorem-scale target.**  Prove the maximal ancient interval, exact scalar,
Ricci, Riemann, volume and diameter laws, the complete tied first-collapse
set, sharp Type-I residues, the product-shrinker times Euclidean pointed
blowup, and the constant-volume time conjugacy.  Prove that a partial
collapse reaches a finite normalized singularity while full collapse is
exactly the positive-Einstein co-shrinking face and becomes stationary for
all forward normalized time.  Separate all-flat tori, mixed flat/curved
products, one-factor, scaling, permutation and tie boundaries.

**Collision boundary.**  Ricci flow and product-curvature identities are
classical; the retained result is an all-dimension, convention-complete,
source-local synthesis with executable boundary reconstruction, not a
literature-priority claim.  The mechanism is absent from C1--C280 and is not
another heat semigroup, spectral-zeta paper, matrix sorting flow, or static
Riemannian geodesic theorem.

**Expected Route-A ceiling.**  Outside the flat face volume decreases
strictly to a singularity, while the flat face is stationary.  There is no
intrinsic isolated primitive-periodic ledger, rational-prime clock,
dynamical determinant, target analytic bridge, or same-clock quantum lift;
the expected tuple is all fail.

### C282 -- exponential-claim Cramér--Lundberg ruin process

**Owner.**  A compound-Poisson reserve with deterministic premium drift and
iid exponential claims, killed at the first passage below zero.

**Bold hypothesis.**  Memorylessness should close a genuinely joint transform
of ruin time and deficit from one positive characteristic root, and that
single formula should simultaneously expose loading chambers, overshoot
independence, the conditional first mean of ruin time, the critical
square-root cusp, an adjustment martingale, and the all-time supremum law.

**Theorem-scale target.**  Derive and verify the two-parameter transform
`E[e^{-q tau-sD}; tau<infinity]`, the favorable/critical/adverse loading
atlas, all no-claim and zero-reserve faces, the conditional mean ruin time and
its critical divergence, exponential overshoot independence, the adjustment
coefficient martingale, and the defective exponential supremum mixture.

**Collision boundary.**  Classical ruin theory supplies the model and the
Gerber--Shiu context.  The retained result is the package-local unified
transform and fully explicit boundary atlas; it is not a new risk model and
does not promote its workload duality into another dynamical owner.

**Expected Route-A ceiling.**  Absorption and compound-Poisson jump times
provide no nontrivial primitive periodic orbit, rational-prime labels,
logarithmic clock, orbit determinant, target zero bridge, or same-clock
quantization.  The expected tuple is all fail.

### C283 -- p-adic conductor-shell heat semigroup

**Owner.**  For one fixed rational prime `p`, a nonnegative Fourier multiplier
on `L^2(Z_p)` which is zero on constants and equals `p^(alpha n)` on the
characters of exact conductor `n`.

**Bold hypothesis.**  Declaring the conductor normalization directly should
make the residue filtration reconstruct positivity and simultaneously close
the full spectrum, exact heat trace, staircase oscillation, Schatten
threshold, meromorphic spectral zeta, pole lattice, primed determinant, and
all singular parameter faces.

**Theorem-scale target.**  Prove the spectrum and multiplicities, compact
resolvent, Markov and killed sub-Markov semigroups, exact heat trace,
eigenvalue counting limsup/liminf, log-periodic small-time profile, sharp
fractional-resolvent Schatten gate, complete mean-zero zeta pole lattice and
determinant, plus `alpha=0`, `mu=0`, `t=0`, `alpha=infinity`, and `p=2`
boundaries.  Finite quotient DFTs provide an independent normalization audit.

**Collision boundary.**  Chacón-Cortés--Zúñiga-Galindo Example 5.1 already
owns, after `d=1` and `beta=alpha` specialization, the same positive
conductor-shell spectrum, multiplicities, geometric spectral zeta, and
vertical pole lattice.  The honest residual is the added zero mode,
conditional-expectation/Markov reconstruction, staircase and log-periodic
closure, Schatten gate, determinant value, degenerate faces, and independent
finite-DFT audit.  No literature originality is claimed.

**Expected Route-A ceiling.**  A fixed local prime gives an honest weak
arithmetic relation but not the global family of rational primes.  Composite
branching controls reproduce the spectral algebra, so conductor shells do
not establish an arithmetic primitive-orbit dictionary.  A source spectral
zeta and determinant are not target Euler data or a Hilbert--Pólya operator.

## Rejected or reserved alternatives

Ideas that merely refined C274--C278, reused a previous state space without a
new theorem owner, or offered only numerical phase portraits were rejected.
The initially drafted dimer-RSA candidate was also retired after the hostile
scan found permanent internal kill records B11/G04/W01 and direct classical
owners; it is not part of this batch.
In particular, another linear Hamiltonian resonance atlas, another scalar
fractional Dirichlet multiplier, another finite random functional graph, and
another two-body integrable scattering reduction would have violated the
cross-subtype requirement.  General branched-graph TV flow, noisy Jeffery
dynamics, higher-dimensional RSA, nonexponential claims, and adelic/all-prime
couplings are reserved: each changes a central proof mechanism and cannot be
claimed from the present five source-local theorems.

## Expected Route-A discipline

The evaluator is applied literally.  A source-side zeta, probability PGF,
resolvent, heat trace, or natural linearization does not earn target-side
credit by terminology.  Finite computations are regression certificates,
not proofs of arbitrary-size, arbitrary-parameter, asymptotic, semigroup, or
operator statements.  No candidate may claim target arithmetic local data,
Euler factors, root numbers, automorphy, a target divisor/counting law or
functional equation, a target zero match, a Hilbert--Pólya operator, or
Route-B input.
