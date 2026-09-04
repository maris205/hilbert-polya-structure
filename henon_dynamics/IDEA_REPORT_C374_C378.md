# Route-A idea report: C374--C378

## Round objective and frozen baseline

The user authorized exactly five independent complete papers and asked for a
large, theorem-scale advance in every slot, with a wholesale dynamical-model
change whenever a proposal would merely subdivide an existing result.  This
round therefore uses five different owners: an arboreal Kummer tower, an
arithmetic Cayley-graph tower, a compact magnetic Hamiltonian, a nonlocal
blow-up PDE, and an interacting eigenvalue diffusion.  Their state spaces,
clocks, proof mechanisms, and singular boundaries are different; no paper is
an installment of another.

The frozen collision baseline is
`f58422d8f03235329863f946654981ecb5d4dc97`, the evaluation date is
`2026-09-04`, and the deterministic build epoch is `1788480000`.  Every
candidate uses `flow_systems/skills/route-a-evaluator.md` v0.2.0 at SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`
and literal scope `NO_BAD_EULER_OR_ROOT_NUMBER`.  `NEW` below means only a
new workspace owner after collision review; it is not a literature-priority
claim.

## Frozen candidates

### C374 -- basepoint-two Kummer arboreal Frobenius dynamics

**Owner.**  The complete preimage tower of `2` under `z -> z^2`, with
splitting fields `Q(2^(1/2^n),zeta_(2^n))` and their faithful affine actions
on every level `n>=3`.

**Large step.**  Determine the radical--cyclotomic intersection exactly,
prove the all-level index-two affine Galois image and its four-kernel
restriction maps, identify the inverse-limit `2`-adic image, classify every
possible fixed-root multiplicity, and derive the exact Chebotarev density of
primes at which `x^(2^n)=2` has a root.  The finite enumeration audits the
closed formulas; it does not prove the all-level field theorem by sampling.

**Nearest collisions.**  C12A owns the universal finite-etale
Frobenius-permutation dictionary, while C369 owns the unrelated four-root
`S_4` scheme for one quartic.  Earlier Kummer packages concern collision
fields and determinant obstructions, not this compatible radical-preimage
tower.  C374 claims only the basepoint-two entanglement, image, fixed-root
spectrum, and density theorem.

**Strict tuple.**
`(A0_STRUCTURAL_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`;
the intrinsic prime-indexed Frobenius permutation is genuine, but the
finite-level root action does not furnish one all-level primitive/repetition,
orientation, phase, and monodromy atlas.  No target determinant, analytic
bridge, or target-zero operator is supplied; the canonical finite
permutation unitaries also lack a family-wide time-reversal and
phase/weight-preservation theorem, so they remain only a formal lift hint.

### C375 -- norm-five LPS towers and Hashimoto dynamics

**Owner.**  The six-regular LPS Cayley graph `X^(5,q)` for every prime
`q>5`, `q=1 mod 4`, together with the oriented-edge nonbacktracking operator
defined by the six norm-five Hamilton quaternions.

**Large step.**  Close the exact `PSL_2/PGL_2` Legendre chamber and
bipartiteness theorem, specialize the Bass--Hashimoto characteristic
identity, recover every primitive oriented cycle from all traces, prove the
complete nontrivial Hashimoto spectral-circle statement from the LPS
Ramanujan bound, and obtain the half--half conditional prime-chamber density.
Five complete finite groups test the implementation without replacing the
all-prime cited LPS input.

**Nearest collisions.**  C329 retains the universal Paley-graph
Bass--Ihara--Hashimoto mechanism, and C355 treats stochastic free-group walk
on an infinite tree.  Neither owns the norm-five quaternion congruence tower,
the Legendre-selected projective group, or the combined LPS spectral atlas.

**Strict tuple.**
`(A0_STRUCTURAL_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`;
prime-indexed arithmetic and a complete source-local primitive ledger are
genuine, but the graph cycles do not carry the modulus prime, prime-power
repetition, or a logarithmic-prime clock.  The graphs are not assembled into
one autonomous target owner and no target divisor is identified.

### C376 -- flat magnetic torus and Chern--Landau dynamics

**Owner.**  A unit-mass charged particle on a rectangular flat two-torus in
a constant magnetic field, together with the positive Bochner magnetic
Hamiltonian on every nonzero integral-flux line bundle.

**Large step.**  Derive the complete classical cyclotron return atlas,
quantize flux as the first Chern number, prove every Landau level and its
exact degeneracy, identify the finite magnetic-translation commutator in
both flux orientations, and evaluate the heat trace, spectral zeta,
zeta-regularized determinant, and exact unitary revival times.  The `B=0`
boundary retains the metric-dependent torus closing condition rather than a
coordinate-slope shorthand.

**Nearest collisions.**  C371 is a discrete rational-flux Harper Bloch
family and C356 is a two-band QWZ Chern pump.  Neither owns a continuum
Bochner Laplacian on a fixed line bundle, its Landau degeneracy, magnetic
translation representation, determinant, and double-revival atlas.

**Strict tuple.**
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`; Chern
integrality and a finite Heisenberg representation are exact source
topology, not a rational-prime carrier.  The source quantization is natural
but is not a Hilbert--Polya realization.

### C377 -- periodic Constantin--Lax--Majda exact blow-up atlas

**Owner.**  The inviscid nonadvective periodic equation
`omega_t=omega H omega`, in one explicit Fourier/Hilbert convention and for
arbitrary conserved mean.

**Large step.**  Prove the invariant Hilbert constraint and reduce the PDE
to a pointwise complex Riccati flow, derive both mean-zero and nonzero-mean
Mobius formulas, give necessary-and-sufficient first-pole clocks, close the
entire one-mode phase diagram, and derive local transverse profiles at every
simple first pole.  A global inverse-time norm rate is stated only when all
simultaneous first poles are simple; tangent and higher-order zeros remain in
the exact breakdown theorem but outside that rate claim.

**Nearest collisions.**  C309 owns a finite-dimensional symmetric-matrix
Riccati flow, while nearby Hunter--Saxton, Camassa--Holm, and Keller--Segel
packages have different transport/nonlocal mechanisms.  None owns the
fixed-sign periodic CLM Hilbert closure and arbitrary-mean pole atlas.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`; this is a complete source PDE
theorem without rational-prime orbit data, a target determinant, or a natural
self-adjoint quantization.

### C378 -- beta-two Dyson--Ornstein--Uhlenbeck eigenvalue diffusion

**Owner.**  Ordered eigenvalues of trace-metric Hermitian
Ornstein--Uhlenbeck diffusion, equivalently the Vandermonde Doob transform of
killed independent scalar OU particles in the type-A Weyl chamber.

**Large step.**  Carry one normalization from matrix entries to the exact
Dyson SDE, prove the Karlin--McGregor/Doob kernel and noncollision, identify
the reversible ordered GUE law, and derive the complete partition-indexed
`L^2` spectrum from Hermite Slater determinants.  Exact norms,
multiplicities, sharp gap `1/2`, heat trace, source Fredholm determinant, and
free-fermion oscillator conjugacy are closed for every finite matrix size.

**Nearest collisions.**  Earlier packages treat deterministic
Calogero--Moser scattering, scalar Jacobi diffusion, harmonic Kramers
dynamics, and finite killed walkers.  None owns this conservative continuous
eigenvalue diffusion and its complete partition spectrum.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`; exact random-matrix
solvability and a source oscillator transform do not provide arithmetic
origin or a target spectral bridge.

## Round decision

All five candidates are retained because each closes an independent
theorem-scale problem with explicit hypotheses and boundary faces.  C374 and
C375 are exploratory systems with structural arithmetic but only weak A1:
C374 has compatible finite-level Frobenius permutations without a complete
all-level primitive-orbit atlas, while C375's primitive graph cycles do not
inherit the modulus prime.  C376--C378 are deliberate cross-subtype controls
whose large advances are source-local and whose strict Route-A failures are
recorded rather than softened.  No paper introduces
target arithmetic local data, target Euler factors or bad-prime data, root
numbers, automorphy, a target divisor/counting law or functional equation, a
target-zero match, a Hilbert--Polya operator, or Route-B input.
