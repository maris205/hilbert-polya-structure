# Route-A idea report: C274--C278

## Round objective and baseline

This round continues the A-first roadmap with five independent,
theorem-scale dynamical owners.  It deliberately changes state space, clock,
and proof technology from paper to paper rather than dividing one calculation
into five installments.  The frozen source baseline is
`418bcec5afb1f9e5905cc6e2ba7f9e099fef2e02`.  Every candidate uses
`flow_systems/skills/route-a-evaluator.md` v0.2.0 at SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`,
the deterministic build epoch `1788220800` (2026-09-01 00:00:00 UTC), and
scope `NO_BAD_EULER_OR_ROOT_NUMBER`.

The collision scan considered shuffle chains, coupon collection, rowmotion,
Bernoulli--Laplace diffusion, multivariate Ornstein--Uhlenbeck flow,
degenerate elliptic operators, billiards, charged-particle Hamiltonians,
random functional graphs, fractional evolution, and integrable wave PDEs.
Coupon/shuffle, rowmotion, Bernoulli--Laplace, and multivariate OU proposals
were rejected because nearby registered owners already contain their main
mechanism.  The five retained owners are mutually different:

1. a six-dimensional linear symplectic flow with a gyroscopic stability wall;
2. an integrable area-preserving billiard map on confocal caustics;
3. a random discrete self-map and its functional digraph;
4. a non-semigroup fractional-memory evolution on an infinite-dimensional
   Hilbert space;
5. a finite-dimensional invariant manifold inside a nonlinear integrable PDE.

`NEW` below means only that no C1--C273 package owns the frozen theorem.  It
does not assert literature priority.

## Frozen candidates

### C274 -- ideal Penning-trap symplectic atlas

**Owner.**  Freeze the classical ideal Penning trap with a uniform axial
magnetic field, a quadrupole electrostatic potential, physical time, and the
canonical six-dimensional Hamiltonian normalization used in the package.

**Large theorem step.**  Exponentiate the complete Hamiltonian matrix and
classify the stable, critical, and unstable radial chambers together with the
axial oscillator and every zero-frequency or sign boundary.  In the stable
chamber the modified-cyclotron and magnetron modes receive exact frequencies,
actions and Krein signs.  The theorem gives the complete boundedness and
closed-orbit resonance criterion, least periods, stroboscopic fixed spaces,
and the critical Jordan growth rather than reporting only the familiar
frequency formula.

**Nearest owners.**  C262 studies a time-periodic scalar Hill monodromy and
C268 studies covariant constant electromagnetic Lorentz motion.  C274 instead
has a static canonical magnetic Hamiltonian plus an electrostatic saddle; its
magnetron negative-energy mode, gyroscopic stabilization wall, and resonant
three-mode torus atlas are different invariants.

**Executable route.**  Reconstruct the canonical Hamiltonian matrix,
symplectic exponential, spectral projectors, mode energies, resonance gcds,
least periods and fixed-space dimensions independently over stable, critical,
unstable and singular rows.  Hostile mutations alter field signs, the
discriminant, mode ordering, Krein labels, resonance reduction, boundary
semantics and Route-A locks.

### C275 -- confocal elliptic-billiard Poncelet atlas

**Owner.**  Inside the normalized outer ellipse `E(f)`, freeze the invariant
sector tangent to a confocal inner elliptical caustic `E(e)`, with
`0<f<e<1`, oriented impact time, and the package's boundary coordinates.

**Large theorem step.**  Conjugate the billiard map on every such caustic to a
rigid rotation and prove the exact incomplete/complete elliptic-integral
formula

`rho = F(omega,e)/(2 K(e))`,

where

`omega = asin(sqrt((e^2-f^2)/(e^2(1-f^2))))`.

The paper closes strict parameter monotonicity and both endpoint limits.  For
every reduced rational `rho=p/q`, it proves that every point on the caustic
belongs to the same least-period-`q` Poncelet family and records the iterate
derivative along the invariant curve.  Irrational rotations and all boundary
faces remain explicit.  The theorem is intentionally confined to the
elliptic-caustic sector; no hyperbolic-caustic atlas is smuggled into it.

**Nearest owners.**  C247 treats the circular billiard, where the twist and
return shear are elementary.  C275 has nonconstant confocal geometry and a
genuine elliptic-integral rotation map; circular formulas cannot certify its
monotonicity, porism parameters, or eccentricity limits.

**Executable route.**  Independently evaluate the elliptic integrals, invert
selected rational rotations, verify monotonicity and endpoint cells, and
check direct reflection/tangency geometry for representative Poncelet
polygons.  Mutations attack modulus/amplitude conventions, the factor two,
orientation, gcd reduction, caustic ordering, endpoints, source hashes and
Route-A locks.

### C276 -- uniform random-mapping functional-digraph theorem

**Owner.**  Choose a self-map of `[n]` uniformly from all `n^n` maps, follow a
uniform marked vertex, and freeze integer iteration time and the standard
tail/cycle decomposition of its functional digraph.

**Large theorem step.**  Count maps with exactly `k` cyclic vertices and `j`
cycles by

`binom(n,k) * [k atop j] * k * n^(n-k-1)`,

derive the complete cyclic-point law

`P(C_n=k)=k (n)_k / n^(k+1)`,

and prove the marked tail/cycle joint law

`P(rho=r,lambda=l)=(n-1)_(r+l-1)/n^(r+l)`.

The same theorem obtains expected cycle counts, identifies `C_n` in law with
the marked first-collision length, and proves its Rayleigh scaling limit.
Thus the global graph count, a local orbit law, and the asymptotic collision
regime close in one paper rather than as unrelated finite enumerations.

**Nearest owners.**  C264 and C269 classify deterministic algebraic maps on
finite groups/fields, and C273 treats random-walk fluctuation laws.  C276 is a
uniform ensemble over every self-map: its Cayley-forest factor, Stirling cycle
factor and birthday-collision limit do not follow from those owners.

**Executable route.**  Enumerate every map through the declared finite cutoff,
reconstruct cyclic vertices, component cycles and marked tail/cycle pairs,
and compare all exact histograms with independently derived falling-factorial
laws.  Symbolic checks close normalization, moments and asymptotics; mutations
target Stirling kind/sign, forest factors, marked-root conventions, collision
indexing and Route-A locks.

### C277 -- Caputo fractional Dirichlet heat flow

**Owner.**  On `L2(0,pi)`, freeze the Dirichlet Laplacian `A`, the normalized
sine basis, physical Caputo time, and `0<beta<=1` in
`D_t^beta u + A u = 0`.

**Large theorem step.**  The exact multiplier
`E_beta(-n^2 t^beta)` yields inverse-stable subordination, positivity and
contraction.  For `0<beta<1` the family is proved not to be a semigroup and
has the sharp spatial endpoint
`A^theta S_beta(t)` bounded, within the declared `theta>=0` smoothing domain,
if and only if `theta<=1`: precisely two spectral Sobolev derivatives,
including the endpoint, and no more.  Negative powers are bounded because
`A>=I`, but lie outside that nonnegative smoothing domain.  The paper also
proves `S_beta(t)` belongs to `S_p` exactly for `p>1/2`, the operator-norm
limit
`t^beta S_beta(t) -> A^(-1)/Gamma(1-beta)`, and the singular `beta=1` heat
face with all-order smoothing and exponential decay.

**Nearest owners.**  C195 reaches a Markov heat flow through Cole--Hopf, C206
studies enhanced dissipation, and C272 studies an age-renewal transport
semigroup.  None has a Caputo memory clock, a non-semigroup solution family,
or the exact finite-smoothing/Schatten/resolvent trichotomy.

**Executable route.**  Evaluate Mittag--Leffler multipliers, the exact
`beta=1/2` error-function identity, smoothing maxima, Schatten partial sums,
composition failures and scaled long-time cells.  The independent checker and
symbolic audit reconstruct the conventions without importing the producer.

### C278 -- signed Camassa--Holm two-peakon atlas

**Owner.**  Freeze the ordered two-peakon manifold
`u=sum_j p_j exp(-|x-q_j|)` of the Camassa--Holm equation, physical time up to
collision, and only the explicitly declared post-collision `alpha` rule.

**Large theorem step.**  Momentum and energy reduce the four-dimensional
flow to

`y_dot^2=D^2 (y-1)(y-P^2/D^2)`, `y=exp(q_2-q_1)`.

For `p_1p_2!=0`, the root ordering gives exactly two strict chambers: an
explicit global same-sign cosh/tanh scattering branch and an explicit signed
sinh/coth branch with finite collision,
quadratic gap collapse, and reciprocal amplitude blow-up.  The paper closes
the centre/scattering data, profile limit, collision-energy concentration,
the degenerate `p_1p_2=0` single-peak/zero face, and the full declared `alpha`
energy ledger from conservative reflection to sticky coalescence.

**Nearest owners.**  C256 classifies KdV traveling-wave profiles, whereas
C278 evolves interacting singular Camassa--Holm measures and encounters
finite-dimensional blow-up.  The PDE's general weak-solution theory is not
claimed: the result remains on the ordered two-peakon manifold and its stated
extension.

**Executable route.**  Reconstruct conserved quantities, both explicit
branches, asymptotic series, centre motion, profile limit and extension energy
for generic and singular rows.  Mutations alter the gap sign, branch root,
collision coefficient, energy interpolation, PDE scope and Route-A locks.

## Rejected or reserved alternatives

| proposal | decision | reason |
|---|---|---|
| coupon collection / top-to-random shuffle | reject | nearby stochastic-permutation owners already contain the main stopping/mixing mechanism; the proposed theorem did not create enough owner distance |
| rowmotion and cyclic sieving | reject | the finite-poset/finite-action lane is already dense, and the candidate risked turning a known CSP package into another count table |
| Bernoulli--Laplace diffusion | reject | too close to registered finite Markov-chain spectral owners without a larger new representation theorem |
| multivariate Ornstein--Uhlenbeck flow | reject | existing Gaussian/linear-semigroup owners overlap its main Mehler and covariance calculations |
| full elliptic plus hyperbolic billiard caustic atlas | reserve | the elliptic sector closes exactly; the hyperbolic sector needs separate coordinate and singular-crossing proofs and is not inferred |
| arbitrary weak Camassa--Holm continuation | reject | the two-peakon reduction does not prove uniqueness or admissibility for arbitrary `H1` data |

## Expected Route-A discipline

C275 has analytic clean periodic families and a natural ambient Dirichlet
billiard.  Because the latter uses continuous physical flight time while the
frozen owner uses the one-reflection Poincare clock, and no same-clock
phase/weight correspondence is proved, it remains only an A4 formal hint;
the clean families independently make the ordinary isolated-orbit determinant
gate fail.
C274 has only weak closed resonances and a natural magnetic quantization.
C276--C278 have no rational-prime carrier or target determinant.  A source
Hamiltonian, Poncelet porism, finite source cycle count, Schatten class, Lax
context, or collision ledger remains candidate-local and cannot be combined
across owners into a target spectral claim.

All five use `NO_BAD_EULER_OR_ROOT_NUMBER`.  No package introduces target
arithmetic local data, Euler factors, root numbers, automorphy, a target
divisor/counting law or functional equation, a target zero match, a
Hilbert--Polya operator, or Route-B authorization.
