# Route-A idea report: C264--C268

## Round objective and baseline

This round follows the A1/A2-first roadmap while making five independent
theorem-scale advances rather than splitting one mechanism into installments.
The frozen source baseline is
`a24c701881d22a4e49eaa2a44b94395c3c540b3d`.  Every candidate uses
`flow_systems/skills/route-a-evaluator.md` v0.2.0 at SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`,
the build epoch `1788048000`, and scope
`NO_BAD_EULER_OR_ROOT_NUMBER`.

The collision audit tested finite functional graphs, graph quantum walks,
Boolean networks, self-exciting and reflected stochastic systems, biochemical
flows, free-boundary PDEs, hybrid impacts, molecular Hamiltonians, and
constant-field relativistic flows.  The retained five occupy different state
spaces, clocks, and proof technologies:

1. finite abelian endomorphism dynamics;
2. a self-exciting point process and affine PDMP intensity;
3. a local-time interface diffusion;
4. an infinite tight-binding quantum lattice;
5. a proper-time relativistic linear flow.

`NEW` below means only that no C1--C263 package owns the frozen theorem.  It
does not assert literature priority.

## Frozen candidates

### C264 — arbitrary finite abelian power maps

**Owner.**  For every finite abelian group `G` and every integer `d>=1`, one
source update is `P_d(g)=g^d`; `d=0` is a separate constant-map face.

**Large theorem step.**  Split `G=A_d x B_d`, where the order of `A_d` is
coprime to `d` and every prime of `B_d` divides `d`.  The first factor is the
complete periodic core and the second is the nilpotent transient factor.  The
paper closes every iterate fixed count, Möbius primitive/cycle count, finite
zeta, identical rooted in-tree, exact tail layers, all image ranks, the full
Koopman characteristic polynomial, and every zero-eigenvalue Jordan-block
multiplicity.  Thus the advance is not another finite-cycle census: it
recovers the entire nonpermutation Jordan sector.

**Nearest owners.**  C172 is one primitive finite-field multiplier, C204 is a
finite-vector-space linear map, C258 is an affine full-period congruential
map, and C260 is a projective permutation.  None owns arbitrary finite
abelian primary factors plus their full in-tree/zero-Jordan structure.

**Executable route.**  Enumerate finite abelian invariant-factor types,
directly construct every small functional graph and full-function composition
matrix, and independently compare cycles, tails, image ranks, nullity ladders,
and exact Jordan multiplicities.  Mutation targets include swapped primary
factors and the `d=0` boundary.

### C265 — exponential Hawkes process

**Owner.**  The predictable point-process intensity obeys

`d lambda_t=-b(lambda_t-nu)dt+a dN_t`,

with event hazard `lambda_(t-)`, `b>0`, and `a,nu>=0`.

**Large theorem step.**  The paper closes the joint count--intensity affine
transform, subcritical stationary Laplace law, every stationary moment,
intensity covariance, the continuous counting covariance density, the
complete covariance measure with its Dirac atom, a frozen no-`1/(2*pi)`
Bartlett spectrum, every window-count variance, the Borel cluster law, and
the Poisson/zero-immigration/critical/supercritical faces.  These three
covariance objects remain notationally and mathematically separate.

**Nearest owners.**  C208 has branching without a predictable intensity,
C214 has exogenous resetting, C233 has immigration--death, C246 has
state-dependent AIMD jumps, and C263 has exchangeable rather than
chronological reinforcement.  Hawkes self-excitation is a new owner.

**Executable route.**  Reconstruct moments from the generator, covariance
from the response convolution, spectrum by an independently frozen Fourier
transform, cluster probabilities by Lagrange inversion, and mutate the
left-limit intensity, Dirac atom, stability inequality, and `2*pi`
normalization.

### C266 — skew Brownian interface

**Owner.**  Freeze zero drift and symmetric semimartingale local time in

`X_t=x+B_t+(2p-1)L_t^0(X)`, `0<=p<=1`.

**Large theorem step.**  One theorem separates the discontinuous terminal
Lebesgue density from the speed-measure symmetric kernel, closes the Feller
generator interface, complete resolvent, every two-sided hitting probability,
both discounted exit sides, mean exit time, and generalized arcsine positive
occupation law.  Ordinary Brownian motion and both one-sided reflected limits
remain exact.

**Nearest owners.**  C200, C229, and C237 are diffusion owners without local
time transmission; C214 resets rather than transmits; C226 is a deterministic
moving interface.  The new content is the convention-complete stochastic
point interface.

**Executable route.**  Split all Gaussian and hyperbolic calculations at
zero, independently verify mass, Chapman--Kolmogorov, speed detailed balance,
resolvent Laplace transformation, interface BVPs, stable-ratio occupation
normalization, and hostile right-versus-symmetric-local-time changes.

### C267 — Wannier--Stark tight-binding flow

**Owner.**  On `ell^2(Z)`, freeze

`(H psi)_n=F n psi_n-J(psi_(n+1)+psi_(n-1))`, `F!=0`.

**Large theorem step.**  Fourier gauge conjugacy gives the simple pure-point
ladder `F Z` and a Bessel eigenbasis.  The paper closes every propagator
matrix element, the least full-space Bloch return, all delta-source shell
probabilities and second moments, unitarity, and the sharp operator-ideal
boundary: the propagator is noncompact/non-Schatten while the resolvent lies
in `S_p` exactly for `p>1`, not `S_1`.  The `J=0` and singular `F->0` free
lattice faces are distinguished.

**Nearest owners.**  C143 is a discrete-time coined edge walk, C171 is the
classical Ehrenfest chain, C178 is a harmonic metaplectic strobe, and C261 is
a cubic Fourier PDE.  None owns the uniform-field lattice ladder and its
full-line operator-ideal boundary.

**Executable route.**  Compare the closed Bessel kernel with independent
spectral sums and finite Schrödinger residuals, verify probability shells and
small-time signs, and mutate gauge orientation, Bessel order, return clock,
and the false trace-class claim.

### C268 — constant electromagnetic Lorentz flow

**Owner.**  In Minkowski space with `eta=diag(1,-1,-1,-1)`, a constant
electromagnetic generator `A` satisfies `A^T eta+eta A=0` and proper-time
dynamics `u'=Au`, `x'=u`.

**Large theorem step.**  The characteristic polynomial
`(z^2-a^2)(z^2+b^2)` produces exact hyperbolic and rotational spectral
projectors, the all-proper-time exponential, the integrated spacetime flow,
Lorentz-norm preservation, determinant one, and a complete periodic-velocity,
drift, and growth classification.  Electric-like, magnetic-like, zero-field,
and null-field faces are retained; on the nonzero null face `A^3=0`, so both
flow and position integral terminate polynomially.  Future timelike physical
worldlines are not misreported as closed merely because their velocity has a
rotational period.

**Nearest owners.**  C234 is a dissipative Landau--Lifshitz--Gilbert spin on a
sphere, C199/C230 are constrained mechanical flows, and C262 is a periodically
switched `SL(2,R)` oscillator.  C268 owns a constant Lorentz-algebra generator
in four-dimensional spacetime, invariant projectors, proper-time kinematics,
and the null-field nilpotent limit.

**Executable route.**  Generate exact rational electric/magnetic tensors in
all invariant chambers, reconstruct the matrix exponential and integral by a
producer-independent method, verify the Lorentz relation and minimal
polynomial symbolically, and mutate invariant signs, projectors, null
truncation, and coordinate-time/proper-time semantics.

## Rejected or reserved alternatives

| proposal | decision | reason |
|---|---|---|
| Ihara/Hashimoto nonbacktracking zeta | reject | Direct ownership collision with C15, C29, and C30. |
| Generic Szegedy/Grover spectral mapping | reject | Too close to C143/C171/C183 and mainly a generic restatement. |
| Hamming-graph continuous-time quantum walk | reserve | Mathematically complete, but the Wannier--Stark owner makes a larger infinite-dimensional quantum step with a sharper operator-ideal boundary. |
| Conjunctive Boolean network | reserve | Its eventual necklace rotation risks repeating C165/C190 unless a separate sharp saturation-exponent theorem is first closed. |
| Five stochastic queue/PDMP papers | reject as a batch | Hawkes, skew Brownian, reflected fluid queue, shot-noise OU, and M/G/1 are individually valid gaps, but using all five would violate the requested cross-subtype diversity. |
| PT dimer, Morse oscillator, delta interaction | reserve | Exact and viable, but C267 already fills the quantum slot and the retained constant-field Lorentz flow adds a different relativistic classical owner. |
| Stefan similarity, Goldbeter--Koshland, rimless wheel | reserve | Distinct backups; none was needed after all five frozen theorem contracts passed their pilot identities. |
| Free transport/Landau damping | reject for this round | Its shear mechanism is too close to the C206 Couette-mixing owner. |
| Finite-field Dickson/Chebyshev maps | reject with C264 | They are quotients of cyclic power maps and would split one theorem lineage across two papers. |

## Expected Route-A discipline

C264 may retain source-local A0/A1 coordinates because finite invariant
factors, exact primitive cycles, and a finite zeta are intrinsic.  They do not
identify rational primes with source primitive cycles or provide a logarithmic
prime clock.  C265--C268 remain Route-A rejected.  The speed-space operator of
C266, natural lattice Hamiltonian of C267, and Lorentz representation of C268
remain candidate-local; their coordinates cannot be combined.

All five use `NO_BAD_EULER_OR_ROOT_NUMBER`.  No package introduces target
arithmetic local data, Euler factors, root numbers, automorphy, a target
divisor/counting law or functional equation, a Hilbert--Pólya operator, a
target zero match, or Route-B authorization.
