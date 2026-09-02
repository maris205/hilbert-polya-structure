# Route-A idea report: C314--C318

## Round objective and frozen baseline

The user requested exactly five independent papers and asked that each paper
make a theorem-scale advance rather than splitting one calculation into five
installments.  This round therefore changes the state space, clock, and proof
mechanism in every slot: an ancient geometric PDE, an integrable many-body
root flow, a full-memory stochastic walk, a nonlinear matrix algorithm, and a
chiral quantum lattice.

The collision baseline is
`1938bae19e5a92f9ce2411aafdc68323bd641bd0`, the fixed date is 2026-09-03,
and the build epoch is `1788393600`.  Every candidate is evaluated under
`flow_systems/skills/route-a-evaluator.md` v0.2.0, SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`,
with literal scope `NO_BAD_EULER_OR_ROOT_NUMBER`.

The collision scan covered the C1--C313 package registry, recent batch
reports, model owners, and mechanism-level neighbors.  `NEW` below means only
that the frozen theorem has no owner elsewhere in this workspace.  It is not
a claim of literature priority.

## Frozen candidates

### C314 -- Angenent oval under curve shortening

**Owner.**  For `t<0`, study the central connected component

`cos x = exp(t) cosh y`, `|x|<pi/2`.

The strip condition is part of the definition: without it the periodic
equation is the disjoint union of all `2*pi` horizontal translates and is
not one compact curve.

**Large step.**  Prove directly that it is a smooth embedded strictly convex
ancient curve-shortening solution.  Close its exact width, height, curvature
range, area, elliptic perimeter, strip arrival-time foliation, circular
extinction blow-up, and both translated Grim-Reaper ends.  The key identities
are

`|grad F|^2=1-exp(2t)`, `A(t)=-2*pi*t`, and

`L(t)=4*k*K(k)`, `k=sqrt(1-exp(2t))`,

where `K` uses the elliptic modulus convention.

**Nearest collision.**  C281 is a homogeneous Ricci scaling flow; C299 is a
radial self-similar Navier--Stokes vortex; C304 is linear Cahn--Hilliard.
None owns a compact ancient curve-shortening solution, its arrival-time strip
foliation, elliptic perimeter, or two translator ends.  The risk is low.

**Proof boundary.**  The theorem is a complete closure of this explicit
ancient solution, not a new classification of all convex ancient curves.
The endpoint `t=0` is an extinction point and `t=-infinity` is an asymptotic
end, not an additional smooth slice.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`; Route A rejected.

### C315 -- positive real Calogero goldfish flow

**Owner.**  Fix `x_1<...<x_N` and `v_i>0`, put

`P(z)=product_i(z-x_i)` and
`Q(z)=sum_i v_i product_{j!=i}(z-x_j)`,

and evolve the ordered roots of `P(z)-tQ(z)`.

**Large step.**  The Stieltjes quotient

`Q/P=sum_i v_i/(z-x_i)`

gives `N-1` fixed interlacing anchors.  Prove all-time simple real roots,
strictly positive particle velocities, the goldfish equation, the exact
polynomial-pencil group law, the center-of-mass law, and a two-sided
scattering atlas.  At each end, `N-1` particles freeze at the anchors while
one ballistic carrier of total speed `V=sum_i v_i` transfers from the
leftmost to the rightmost rank; its intercept is
`sum_i(v_i*x_i)/V` and the complete first `1/t` correction is retained.

**Nearest collision.**  C196 solves repulsive rational Calogero--Moser by a
Hermitian matrix pencil and has `N` asymptotically free velocities.  C315 has
a velocity-coupled goldfish equation, a scalar hyperbolic polynomial pencil,
and one-carrier scattering.  The surface similarity is real, but the owner,
force law, positivity cone, interlacing mechanism, and scattering theorem are
different; the risk is medium and controlled.

**Proof boundary.**  Strict positivity is essential.  A zero velocity can
create a finite-time collision, and mixed signs can produce a double root and
then a complex pair.  Equal initial positions are excluded.  The `N=1` free
particle and all-negative time reversal are boundary corollaries, not hidden
inside the positive theorem.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`; Route A rejected.

### C316 -- elephant random walk phase transition

**Owner.**  At each step, choose one previous increment uniformly and copy it
with probability `p` or reverse it with probability `1-p`; the first step has
bias `q`.  With `a=2p-1`, the position is a time-inhomogeneous Markov chain
even though the increment process has complete memory.

**Large step.**  Derive the exact conditional kernel and finite-product
formulae for the mean and second moment at every `p,q` and time.  Construct
the martingale normalization with a separate `p=0` chart, retain its
predictable quadratic variation, and close the three source limit regimes:

- `p<3/4`: diffusive Gaussian scale `sqrt(n)`;
- `p=3/4`: critical Gaussian scale `sqrt(n log n)`;
- `p>3/4`: almost-sure and `L^4` convergence on scale `n^(2p-1)`.

The first four moments of the superdiffusive limit and the deterministic
`p=1,q in {0,1}` faces are stated separately.

**Nearest collision.**  C263 is an exchangeable classical Polya urn, C273 is
an iid fluctuation theorem, and C302 is a recursive-algorithm contraction
limit.  None owns a full-memory increment process with the `p=3/4` scaling
transition and its exact finite-time laws.  The known urn representation is
background rather than the paper's owner.

**Proof boundary.**  The finite exact probability tables test conventions;
they do not prove the limit theorems.  The Gamma normalization is not used at
`p=0`, the second moment is not mislabeled as the variance, and blanket
non-Gaussian or nondegenerate language is not applied to deterministic
endpoints.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`; Route A rejected.

### C317 -- Newton--Schulz full basin and pseudoinverse flow

**Owner.**  For a rectangular complex matrix `A`, iterate

`X_(k+1)=X_k(2I-AX_k)`.

**Large step.**  For invertible square `A`, prove the exact residual law

`R_k=(I-AX_0)^(2^k)`

and the necessary-and-sufficient basin `rho(I-AX_0)<1`, not merely a norm
sufficient condition.  Derive the exact Jordan polynomial prefactor, the
nilpotent finite-termination time, and every unit-circle/exterior boundary.
For arbitrary rank, let `P=AA^dagger` and `Q=A^dagger A`; prove the complete
Moore--Penrose basin

`X_0=Q X_0 P` and
`rho((P-AX_0)|Ran(A))<1`,

with exact projected residual powers.  Finally close the canonical
`X_0=alpha A*` corridor, its optimal scale, rank-zero face, equality
truncation, and divergent exterior.

**Nearest collision.**  C257 conjugates a scalar quadratic Newton map to
squaring on the Riemann sphere; C201 studies heavy-ball Jury chambers; C309
is a continuous symmetric matrix Riccati flow.  Residual squaring alone would
be too close to C257.  The strengthened arbitrary-rank compatibility theorem,
Moore--Penrose iff basin, nonnormal Jordan rate, and complete scale boundary
give C317 a distinct matrix-algorithm owner.

**Proof boundary.**  Exact arithmetic convergence is separated from floating
point stability and implementation performance.  For singular `A`, the
identity residual cannot tend to zero on `ker A*`; projection compatibility
is indispensable.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`; Route A rejected.

### C318 -- finite SSH bulk--edge and quench atlas

**Owner.**  On `M>=2` two-sublattice cells, use real intracell/intercell
hoppings `v,w>=0` and the open chiral Hamiltonian

`H=[[0,T],[T*,0]]`, `T=vI+wS_-`.

**Large step.**  Derive the complete open-chain continuant and singular-value
pairing.  Prove that the unique strict hyperbolic edge doublet exists exactly
when

`w/v>(M+1)/M`,

with its exact `sinh` eigenvector, energy, exponential envelope, linear-taper
threshold, and large-`M` splitting.  Separate this finite threshold from the
bulk winding transition `w/v=1`.  Close the periodic spectrum and distinguish
the continuum gap from the finite sampled gap, including the odd-ring
correction `sqrt(v^2+w^2-2*v*w*cos(pi/M))`; retain the even/odd sampling of
the bulk critical momentum, all one-hopping/zero/uniform faces, and a
zero-safe block propagator.  A cross-phase Bloch quench retains
its exact critical momenta and times while explicitly distinguishing a
continuum mode zero from a finite-ring grid hit.

**Nearest collision.**  C308 is a one-sublattice non-Hermitian asymmetric
Hatano--Nelson chain whose theorem is nonnormal similarity, skin effect, and
OBC/PBC spectral sensitivity; it explicitly excludes topology.  C318 is a
Hermitian two-sublattice chiral system whose theorem is winding, finite edge
hybridization, and a finite/bulk threshold separation.  Repeating general
resolvent and conditioning calculations is excluded.  The risk is medium and
controlled.

**Proof boundary.**  A balanced finite chain with `v>0` has no exact zero
mode.  Bulk topology is not conflated with immediate finite-chain
hyperbolicity; at `v=w`, a finite periodic chain samples the zero only for
even `M`.  The model is single-particle, clean, and noninteracting.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`; Route A
rejected.

## Historical ownership and rejected alternatives

The source locks are Angenent's shrinking-curve construction and modern
convex-ancient classification papers; Calogero's 2001 goldfish paper; the
Schuetz--Trimper model and Bercu martingale analysis; the Schulz, Hotelling,
and Ben-Israel matrix iterations; and the original Su--Schrieffer--Heeger
papers plus standard chiral bulk--boundary references.  The packages claim a
proof-complete, convention-locked, executable synthesis, never priority for
the classical ingredients.

Ordinary rowmotion, consensus/voter variants, another scalar Newton map, and
another one-band nonnormal chain were rejected for direct workspace
collision.  A Rice--Mele pump was reserved as a more expensive successor to
C318; a Jackiw--Rebbi kink was rejected because its factorized front Hessian
would collide with C231 and C236.

No retained package introduces target arithmetic local data, target Euler
factors, bad-prime data, root numbers, automorphy, a target divisor/counting
law or functional equation, a target zero match, a Hilbert--Polya operator,
or Route-B authorization.
