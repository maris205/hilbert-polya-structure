# Route-A idea report: C269--C273

## Round objective and baseline

This round continues the A1/A2-first roadmap with five independent,
theorem-scale dynamical owners.  It does not split one calculation into five
papers.  The frozen source baseline is
`9cb7483e97ef82fdc06d45ecb3043f183ce22391`.  Every candidate uses
`flow_systems/skills/route-a-evaluator.md` v0.2.0 at SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`,
the deterministic build epoch `1788134400` (2026-08-31 00:00:00 UTC), and
scope `NO_BAD_EULER_OR_ROOT_NUMBER`.

The collision audit ranged over finite-field polynomial maps,
sub-Riemannian control, cooperative epidemic networks, age-structured
transport, random-walk fluctuation theory, nonlinear dispersive PDEs, and
queues.  The retained owners have different state spaces, clocks, and proof
technologies:

1. a nonlinear map on each finite field;
2. a Hamiltonian control flow on the Heisenberg group;
3. a finite-dimensional cooperative nonlinear ODE;
4. an infinite-dimensional positive transport semigroup;
5. a discrete-time stochastic partial-sum process.

`NEW` below means only that no C1--C268 package owns the frozen theorem.  It
does not assert literature priority.

## Frozen candidates

### C269 — finite-field Chebyshev functional graphs

**Owner.**  On every finite field `F_q`, for every prime power `q` and every
integer `d>=1`, iterate the normalized Chebyshev/Dickson polynomial determined
by `T_d(u+u^{-1})=u^d+u^{-d}`.  The constant face `d=0` is separate.

**Large theorem step.**  Two cyclic covers of orders `q-1` and `q+1`, folded
by inversion and glued at their ramified intersection, recover the complete
labeled functional graph in every characteristic.  The theorem then closes
all fixed and primitive counts, cycles and finite source zeta, tail
filtration and height, every image rank, and the full Koopman characteristic
polynomial with exact zero-Jordan multiplicities.  Characteristic two and
nonprime fields remain inside the theorem rather than being extrapolated from
prime fields.

**Nearest owners.**  C260 classifies projective Möbius permutations and C264
classifies abstract finite-abelian power maps.  C269 is their nonlinear
quotient/gluing relative: two covers of different orders are folded and
ramified values must be identified, so the uniform-tree conclusion of C264
cannot simply be copied.

**Executable route.**  Construct exact finite fields, verify the chosen monic
irreducible modulus independently, enumerate all field vertices, compare the
direct polynomial graph with the two quotient covers, and reconstruct every
cycle, tail, image-rank and Koopman/Jordan invariant.  Hostile tests alter
ramification, characteristic-two identifications, field moduli, route locks,
and payload hashes.

### C270 — standard Heisenberg sub-Riemannian geodesics

**Owner.**  On real `H^1`, freeze
`X=partial_x-y partial_z/2`, `Y=partial_y+x partial_z/2`, the metric making
`X,Y` orthonormal, and unit-speed normal Hamiltonian time.

**Large theorem step.**  The paper integrates every normal geodesic, proves
there are no nontrivial abnormal minimizers, computes the exact exponential
Jacobian, and identifies the first conjugate, first rotational Maxwell, and
cut times as `2*pi/|lambda|` for `lambda!=0`; the `lambda=0` geodesics are
lines with no finite such time.  It proves that the nonzero vertical axis is
exactly the cut and first-conjugate locus, and closes the full distance
equation including `d(0,(0,0,z))=2*sqrt(pi*|z|)`.

**Nearest owners.**  C242 and C244 have contact/Hamiltonian structures, while
C216 treats Kepler regularization.  None owns a bracket-generating horizontal
metric, its exponential singularities, global Dido cut argument, or exact
Carnot--Caratheodory distance.

**Executable route.**  Reintegrate the Hamilton equations from the frozen
frame, differentiate the endpoint map symbolically, solve the Dido endpoint
problem, and compare hundreds of trajectories and distance roots against an
independent checker.  Mutations attack frame signs, unit-speed normalization,
Jacobian factors, the first phase, vertical distance, and Route-A locks.

### C271 — irreducible heterogeneous network SIS

**Owner.**  On `[0,1]^n`, freeze
`x'=beta*diag(1-x)A*x-D*x`, with `A>=0` irreducible, `D>0` diagonal, and
physical ODE time.

**Large theorem step.**  The spectral abscissa of `beta*A-D` gives the full
global extinction/endemic threshold.  Above threshold the theorem gives the
unique interior equilibrium attracting every nonzero state, a Hurwitz endemic
Jacobian, and strict componentwise transmission monotonicity.  At equality it
goes beyond stability and proves the sharp Perron-vector law
`t*x(t)->v/[beta*w^T*diag(v)A*v]` for every nonzero trajectory.

**Nearest owners.**  C227 is a dissipative Lorenz flow, C235 is a cyclic
replicator, and C254 is a scalar-resource chemostat.  None owns an arbitrary
irreducible contact matrix, strict subhomogeneity, and the normalized critical
Perron asymptotic.

**Executable route.**  Generate exact regular-network threshold, endemic and
critical rows; reconstruct spectra, equilibria, Jacobians and invariant
diagonal solutions independently; and use the proof's stable-complement
quotient to cover arbitrary networks.  Mutations target chamber labels,
Perron normalization, the `1/t` coefficient, Jacobian signs and route locks.

### C272 — Erlang age-transport semigroup

**Owner.**  On `L1(R_+)`, freeze mortality transport with the renewal boundary
whose fertility kernel is Erlang of order `k`.

**Large theorem step.**  The renewal denominator has `k` explicit algebraic
roots, but the paper proves the category firewall that a root is an `L1`
eigenvalue only when it lies right of the essential edge `Re(lambda)=-mu`.
It proves the semigroup is a compact newborn perturbation of the mortality
shift, obtains operator-norm rank-one asynchronous behavior for `beta>1`, and
separates that isolation transition from the population threshold
`beta=(1+mu/gamma)^k`.

**Nearest owners.**  C210 treats a scalar retarded delay equation and C218 a
damped wave with essential accumulation.  C272 instead owns a positive
boundary-renewal transport semigroup, a finite algebraic pole set, an `L1`
integrability gate, and a compact-versus-shift long-time decomposition.

**Executable route.**  Reconstruct every cleared denominator polynomial and
root, label it relative to the essential edge, verify the two thresholds and
all zero-birth faces, then cross-check the symbolic factorization, fresh byte
replay and repaired-hash attacks.  Finite roots remain regression evidence;
the characteristic and compactness arguments prove the semigroup theorem.

### C273 — Sparre--Andersen universal fluctuations

**Owner.**  Let `S_n` be partial sums of iid continuous increments symmetric
about zero, with the strict no-ties convention.  Time is the integer step.

**Large theorem step.**  The package proves the universal survival law
`q_n=binom(2n,n)/4^n`, its square-root generating function and first-descent
law.  It then proves that both the number of positive partial sums and the
unique maximum time have the exact discrete arcsine distribution
`q_k*q_(n-k)`, and both scale to `Beta(1/2,1/2)`.  A simple symmetric atomic
walk supplies an exact boundary showing why strict, nonnegative and tied
maximum conventions cannot be interchanged.

**Nearest owners.**  C266 has a continuous skew-Brownian occupation law,
C208 a branching law, and C263 an exchangeable urn.  None owns distribution-
free discrete survival, two finite arcsine laws, unique-maximum factorization,
and the atomic no-ties failure in one theorem.

**Executable route.**  Enumerate complete no-ties sign/permutation histories,
reconstruct central-binomial and convolution identities independently, check
scaling cells symbolically, and mutate strictness, maximum ties, first-descent
indexing, central coefficients and Route-A locks.

## Rejected or reserved alternatives

| proposal | decision | reason |
|---|---|---|
| focusing cubic NLS blow-up/scattering | reject | C221 already owns the substantive cubic-NLS dynamical mechanism. |
| ordinary M/G/1 queue | reject for this round | Pollaczek--Khinchine alone did not close a comparably large theorem, and the queue owner is too close to C225. |
| five finite/stochastic fluctuation papers | reject as a batch | Individually viable ideas would violate the requested cross-subtype diversity. |
| general Carnot-group cut locus | reserve | The standard `H^1` theorem closes exactly; a general Carnot claim would require new hypotheses and is not inferred. |
| another abstract finite power map | reject | C264 already owns the uniform abstract finite-abelian theorem; C269 was retained only after the ramified nonlinear quotient was proved separately. |

## Expected Route-A discipline

C269 retains source-local arithmetic and analytic primitive-cycle structure,
but finite-field parameters do not identify rational primes with source
primitive cycles or create a logarithmic prime clock; it remains exploratory.
C270--C273 are Route-A rejected.  A Maxwell time, Perron threshold, renewal
pole, survival transform, natural Hamiltonian, or finite Koopman operator is
candidate-local and cannot be combined across owners.

All five use `NO_BAD_EULER_OR_ROOT_NUMBER`.  No package introduces target
arithmetic local data, Euler factors, root numbers, automorphy, a target
divisor/counting law or functional equation, a target zero match, a
Hilbert--Polya operator, or Route-B authorization.
