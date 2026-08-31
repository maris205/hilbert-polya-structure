# Route-A idea report: C259--C263

## Round objective and baseline

This round freezes five independent dynamical owners rather than dividing one
theorem among five papers.  The source baseline is
`98782afe1e754c311ad0736f72ce09dcc7c85c77`.  Every candidate is evaluated by
`flow_systems/skills/route-a-evaluator.md` v0.2.0 at SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.
The fixed build epoch is `1788048000`.

The gap audit separated three crowded regions of the C1--C258 registry from
the remaining useful openings.  Hénon/Lozi/border-collision variants are
already dense in C104--C123; transfer, symbolic, quantum, finite-group, and
cellular owners are dense in C124--C194; and C195--C258 already cover many
standard ODE, PDE, diffusion, queueing, impact, Filippov, and traveling-wave
models.  The retained round therefore changes owner in every paper:

1. a nonlinear heterogeneous phase network on a tree;
2. a finite-field projective group action;
3. a linear dispersive PDE and rational-time revival group;
4. a periodically switched linear Hamiltonian oscillator;
5. an exchangeable reinforced stochastic process.

`NEW` below means only that no C1--C258 package owns the frozen theorem.  It is
not a literature-priority claim.

## Frozen candidates

### C259 — heterogeneous Kuramoto trees: complete locking and Morse atlas

**Owner.**  For a positively weighted tree with incidence matrix `B`, consider

`theta' = omega - B K sin(B^T theta)`

modulo diagonal rotation.  Subtract the mean frequency and orient every edge
away from a root.

**Theorem contract.**  The unique flow through edge `e` is the sum of the
centered frequencies on its child subtree.  Locking exists exactly when every
cut demand has magnitude at most its edge capacity.  Under strict inequalities
there are exactly `2^(N-1)` locked branches modulo rotation; each saturated
edge merges one inverse-sine pair.  A reduced-incidence congruence makes the
Morse index equal to the number of negative edge cosines and the quotient
nullity equal to the number of saturated edges.  Hence exactly one strict
branch is linearly asymptotically stable and all other strict branches are
unstable.  Violated cuts, identical frequencies, zero couplings, `N=1`, cyclic
graphs, and unlocked motion are explicit boundaries.

**Nearest local owners.**  C189 treats identical first-harmonic phases under a
common `PSU(1,1)` forcing reduction; C203 treats linear signed-Laplacian
consensus; C245 treats event-driven pulse synchronization.  C259 instead owns
heterogeneous frequencies, nonlinear sine balance, a tree cut-flow chamber,
all inverse-sine branches, and exact Hessian inertia.  A delayed-consensus
proposal was rejected because it would only splice C203's Laplacian modes with
C210's scalar Lambert-`W` delay theorem.

**Executable evidence.**  Enumerate labeled Prüfer trees, independently
reconstruct subtree flows and phase branches, compare reduced Hessian inertia,
exercise saturation/violation faces, and mutate edge orientation, cut signs,
inverse-sine choices, and zero-cosine policies.

### C260 — `PGL_2(F_q)` on the projective line: all types and all cycles

**Owner.**  One projective Möbius transformation in `PGL_2(F_q)` acts on the
`q+1` points of `P^1(F_q)` at each source-time step.

**Theorem contract.**  Classify identity, nontrivial unipotent, split
semisimple, and nonsplit semisimple elements.  For every type and every
iterate, give the complete cycle multiset, fixed counts, least periods,
primitive cycles, finite source zeta, and counting-measure Koopman determinant.
Include an exact projective reversor for every class, a characteristic-two
Artin--Schreier classifier, the split/nonsplit involution distinction, and the
exact order/type census whose total is `|PGL_2(F_q)|` for every prime power.

**Nearest local owners.**  C172 studies multiplication by a primitive element
on a finite field, C180 studies a Lattès three-channel Lefschetz ledger, C204
classifies linear endomorphisms of vector spaces by rational canonical form,
and C258 studies affine congruential maps on `Z/mZ`.  None owns the nonlinear
projective quotient action, its rational/nonrational eigenline dichotomy,
characteristic-two trace test, all-element type census, or projective
reversors.  The candidate retains only intrinsic finite-field arithmetic; it
does not identify rational primes with source primitive cycles.

**Executable evidence.**  Exhaust projective matrix classes over a frozen set
of prime fields and extension fields, quotient scalar representatives,
construct the literal permutation on `P^1`, and derive type/order solely from
that independent permutation.  Cross-check census, cycle/fixed/zeta/Koopman
ledgers, reversors, characteristic-two cases, replay, and hostile mutations.

### C261 — periodic Airy flow: cubic Talbot revival atlas

**Owner.**  The periodic linear Airy equation

`u_t + u_xxx = 0`

acts on the Fourier basis by `U(t)e_n=exp(i n^3 t)e_n`.

**Theorem contract.**  Prove the strongly continuous unitary group and its
least full-space return `2*pi`.  At every reduced rational time
`2*pi*p/q`, give the exact `q`-translate cubic-DFT formula and Parseval weight
identity, prove the strobe has exact order `q`, and classify its fixed subspace
by `q | n^3`, equivalently by a prime-valuation cube-root divisor.  Give the
least continuous return for every finite Fourier support and prove that an
irrational strobe fixes only constants.  Close noncompactness and non-Schatten
boundaries without assigning an ordinary Fredholm determinant.

**Nearest local owners.**  C217 is a three-branch rotating shallow-water
Fourier semigroup, C256 classifies nonlinear KdV cnoidal traveling waves, and
C178 studies harmonic-oscillator strobes.  C261 instead owns the cubic Fourier
phase, all rational Talbot translations, exact sampled fixed spaces, and the
integer cubic-divisibility law.  It does not claim nonlinear KdV dynamics or
arbitrary third-order boundary conditions.

**Executable evidence.**  Enumerate reduced rational strobes, independently
DFT the cubic phase, reconstruct translations on test Fourier data, check
prime valuations and strobe orders, and mutate cubic exponents, phase signs,
translation orientation, modulus reduction, and fixed-mode divisibility.

### C262 — square-wave Hill oscillator: complete Floquet and band-edge atlas

**Owner.**  A scalar Hamiltonian oscillator satisfies `x''+k(t)x=0`, where a
period contains two constant segments `(k_1,tau_1)` and `(k_2,tau_2)`.  Each
`k_j` may be positive, zero, or negative.

**Theorem contract.**  Use entire functions `C(k,tau)` and `S(k,tau)` to give
one formula for elliptic, shear, and hyperbolic segment matrices.  Multiply the
two exact `SL(2,R)` factors and prove

`Delta = 2 C_1 C_2 - (k_1+k_2) S_1 S_2`.

Classify all parameters by `|Delta|<2`, `|Delta|>2`, and `Delta=+/-2`, with
the last case separating `+/-I` from nontrivial Jordan growth.  Close all
iterate matrices by Chebyshev polynomials, Floquet multipliers/exponents,
periodic and antiperiodic band edges, segment-order effects, constant-coefficient
faces, zero duration, and zero stiffness.

**Nearest local owners.**  C110 is a finite-prefix nonautonomous Floquet Hénon
map, C178 is a constant harmonic strobe, C218 is a Kelvin--Voigt modal damping
atlas, and C252 is a state-triggered hysteretic relay.  C262 instead gives an
all-parameter exact periodic-coefficient `SL(2,R)` theorem; switching is fixed
in time and not state triggered.

**Executable evidence.**  Sample all sign combinations and band regions;
compare closed segment products with an independent ODE propagator; verify
determinants, discriminants, Cayley--Hamilton/Chebyshev iterates, Jordan edges,
and mutations of segment order, signs, trace coefficients, and equality policy.

### C263 — multicolor Pólya urn: finite laws through the Dirichlet limit

**Owner.**  A `K`-color classical Eggenberger--Pólya urn has nonnegative
initial masses `a_i`, positive total mass, and reinforcement `c>=0`.  One draw,
replacement, and reinforcement is one source-time update.

**Theorem contract.**  For `c>0`, delete zero-mass colors and normalize
`alpha_i=a_i/c`.  Close ordered-word exchangeability, the full
Dirichlet--multinomial count vector, beta--binomial marginals, exact means and
covariances, and every multi-index falling-factorial moment.  Prove the
normalized masses form a bounded martingale and converge almost surely and in
every finite `L^p` to a Dirichlet vector on the active face.  Prove both
directions of the de Finetti statement: Dirichlet mixing yields the finite
word law, and its posterior predictive rule recovers the urn.  Treat `c=0` as
iid without defining `alpha`; retain zero-mass dimensional reductions and the
deterministic one-color face.

**Nearest local owners.**  C171 is the Ehrenfest hypercube chain, C194 is the
Holte carry semigroup, C215 is a partition-valued coalescent, and C253 is a
fixed-population absorbing Moran chain.  C263 instead has increasing total
mass, exchangeable histories, a Dirichlet directing measure, and no fixation
boundary.

**Executable evidence.**  Enumerate ordered words and count compositions,
independently recurse the predictive law, compare all marginals and factorial
moments with exact rational formulas, verify every conditional martingale row
and Dirichlet monomial moment, then replay bytes and mutate chronology,
normalization, count/proportion roles, zero-reinforcement policy, and scope.

## Eliminated candidates and collision decisions

| proposal | decision | reason |
|---|---|---|
| Exponential-kernel Hawkes process | defer | It is a genuine point-process gap, but a release-quality stationary Laplace transform, intensity covariance, counting-measure covariance, and Bartlett-spectrum package needs a separate convention audit.  Retaining both Hawkes and Pólya would also use two stochastic slots while leaving the finite-group opening unused. |
| Rectangular-poset rowmotion | reject for this round | The binary-word conjugacy and Gaussian-binomial cyclic sieving are mathematically clean, but the paper shape is too close to C187 rectangular-tableau promotion and C209 Kreweras complementation: finite cyclic action, full fixed ledger, Möbius cycles, zeta, and CSP. |
| Inviscid Burgers Riemann problem | reject | A single shock/rarefaction atlas is too close to C195's globally conjugated periodic viscous Burgers owner and would be smaller than a full paper.  Revival would require an all-event theorem for arbitrary finite shock interactions. |
| Delayed network consensus | reject | Modal diagonalization reduces it to C203's Laplacian consensus plus repeated copies of C210's scalar delayed Lambert-`W` theorem; this is a splice, not a new owner. |
| Top-to-random shuffle / coupon collector | reject | The finite Markov/shuffle spectrum is crowded by C171, C183, and C239; the likely result would repeat the existing determinant/mixing narrative. |
| Skew Brownian interface diffusion | reserve | The local-time transmission kernel is distinct from C214 and C229, but its occupation-law convention requires careful normalization.  It is a backup if one frozen theorem fails, not a sixth paper. |
| Impulsive logistic harvesting | reserve | The Möbius return map is exact but the theorem step is smaller and sits near C198, C252, and C254. |
| Further relay, impact, dry-friction, rigid-body, KdV, Toda, kink, or standard one-dimensional-map variants | reject | These collide directly with C199, C212, C230, C231, C236, C238, C240, C249, C252, C255, C256, or with the registry's earlier logistic/tent/Gauss/Farey screening. |

## Expected Route-A discipline

C259, C261, C262, and C263 are expected to remain
`ROUTE_A_REJECTED`.  C260 may retain an exploratory A0 signal because the
finite-field and projective-line arithmetic are intrinsic, but that signal is
not a rational-prime primitive-orbit dictionary, logarithmic clock, target
divisor, target analytic continuation, or permission to invoke Route B.
Coordinates from different candidates must not be mixed.

All five use the literal scope `NO_BAD_EULER_OR_ROOT_NUMBER`.  No package may
introduce target arithmetic local data, Euler factors, root numbers,
automorphy, a target divisor/counting law or functional equation, a
Hilbert--Pólya operator, or a Route-B input.
