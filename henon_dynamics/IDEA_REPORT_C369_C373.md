# Route-A idea report: C369--C373

## Round objective and frozen baseline

The user authorized exactly five independent papers, asked that every paper
make a theorem-scale advance, and explicitly authorized changing dynamical
subtype whenever a proposed owner would only repeat an earlier result.  The
collision scan therefore rejected two tempting but insufficient drafts:
the basic focusing-cubic-NLS bright-soliton/Hessian package is already owned
by C221, while uniform stationarity, mean current, and fluctuation symmetry
for ring ASEP overlap C220 and C361.  Neither is recycled here.

The retained systems are a zero-dimensional arithmetic Frobenius groupoid, a
quasiregular contact flow, a magnetic Bloch family, a free-boundary Euler
flow, and a superintegrable classical--quantum Hamiltonian.  Their phase
spaces, clocks, proof engines, and boundary mechanisms are distinct; none is
a parameter slice or deferred section of another paper.

The frozen collision baseline is
`c6553f02d928c6aa05400ded57746869a85f0238`, the date is `2026-09-04`, and
the build epoch is `1788480000`.  Every candidate uses
`flow_systems/skills/route-a-evaluator.md` v0.2.0 at SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`
and literal scope `NO_BAD_EULER_OR_ROOT_NUMBER`.  `NEW` below denotes only a
workspace owner after collision review; it is never a literature-priority
claim.

## Frozen candidates

### C369 -- the quartic `S_4` Frobenius root scheme

**Owner.**  For `f(x)=x^4-x-1`, every good rational prime indexes the four
geometric roots of the reduced finite etale scheme, acted on by the explicitly
conventioned `p`-power Frobenius permutation.  Arithmetic and geometric
Frobenius are distinguished; inversion does not change the cycle atlas.

**Large step.**  Prove irreducibility, discriminant `-283`, and Galois group
`S_4`; identify factor degrees modulo every good prime with primitive
Frobenius-orbit lengths; and derive all fixed counts, Mobius-recovered cycles,
finite Koopman determinants, and the five conjugacy-class zeta forms.  The
Chebotarev densities are proved from the `S_4` class inventory rather than
fitted.  The ramified prime `283` is treated as a non-etale boundary with its
repeated factor retained.  No determinant is multiplied across primes and no
infinite direct sum is declared Fredholm.

**Nearest collisions.**  C12A already owns the universal statement that
Frobenius on a reduced zero-dimensional finite fibre is a finite permutation,
together with its finite zeta/determinant mechanism; C369 does not reclaim
that general owner.  C56 treats a degree-27 finite-etale Fano-line scheme and
selected `W(E6)` Frobenius witnesses, C41 a cubic-CM elliptic `H^1` bridge,
and C172 a chosen finite-field multiplier.  None owns the polynomial-specific
`x^4-x-1` Galois proof, five-class all-good-prime atlas, Chebotarev densities,
and ramified `p=283` boundary closed here.

**Strict tuple.**
`(A0_STRUCTURAL_ARITHMETIC_RELATION,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`;
the finite-fibre arithmetic source is genuine, but absence of one autonomous
global owner, a target divisor, and a target analytic bridge keeps Route B
locked.

**Lineage sources.**  The paper uses the standard Frobenius/factorization
dictionary and Chebotarev density theorem, with an explicit elementary
`S_4` proof for this polynomial.  Sources are recorded by theorem owner in
the package rather than being presented as novelty evidence.

### C370 -- quasiregular Reeb dynamics on `Sigma(2,p,q)`

**Owner.**  The Brieskorn link of `z_0^2+z_1^p+z_2^q`, for coprime odd
`3 <= p < q`, with its normalized weighted contact form and periodic Reeb
circle action.

**Large step.**  Prove the principal period `2pq`, the three exceptional
simple periods `2p`, `2q`, and `pq`, and the complete fixed-set/Morse--Bott
atlas for every return time.  In a frozen ambient-coordinate trivialization,
derive transverse rotations, return determinants, first degeneracy orders,
and nondegenerate Conley--Zehnder iterates.  Identify the Seifert quotient
`S^2(2,p,q)`, its orbifold Euler characteristic, and the principal
Robbin--Salamon index, including the exact sign wall.  The result stops before
contact homology and never convert integer weights into a prime clock.

**Nearest collisions.**  C242 owns an irrational ellipsoid Reeb flow with two
isolated coordinate orbits; C313 owns a round-sphere clean geodesic flow; and
C339 owns Katok--Zermelo closed geodesics.  None owns a weighted hypersurface
link with three exceptional isotropy strata and a principal Morse--Bott
family.

**Strict tuple.**
`(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`;
the exact integer-weight atlas is source-local and the non-isolated principal
family blocks an ordinary primitive-orbit promotion.

**Lineage source.**  Kwon and van Koert, *Brieskorn manifolds in contact
topology*, DOI `10.1112/blms/bdv088`.

### C371 -- rational-flux Harper--Chambers Bloch atlas

**Owner.**  The anisotropic Harper operator at every reduced flux `p/q`,
`q >= 3`, with two Bloch phases and positive coupling `lambda`, in one frozen
Landau-gauge and boundary-phase convention.

**Large step.**  Prove the phase-collapse identity

`det(EI-H)=P(E)-2 cos(q k_x)-2 lambda^q cos(q k_y)`,

then obtain the full two-dimensional spectrum as the inverse image of
`[-2(1+lambda^q),2(1+lambda^q)]`.  Classify band edges and closed gaps without
asserting that every gap is open; prove flux reversal, energy parity, and
Aubry duality; and compute the `q=1,2` repeated-edge boundaries separately.
Exact cyclotomic reconstruction and dense numerical fibres audit one theorem;
they do not prove the all-parameter identity by sampling.

**Nearest collisions.**  C15 contains the established Harper block only on
the sparse row `q=3^m`, flux `1/q`, for a different spectral-edge purpose.
C371 owns the all-reduced-flux, two-phase, anisotropic
Chambers--duality--band atlas.  It does not claim the Harper model or Chambers
formula as new.

**Strict tuple.**
`(A0_WEAK_ARITHMETIC_RELATION,A1_FAIL,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`;
the rational flux is not an arithmetic prime owner and the finite Bloch
determinant is not a dynamical or target determinant.

**Lineage sources.**  Chambers' formula and its rational-flux spectral use are
treated as established source mathematics.  Lamoureux--Mingo, Theorem 2.5
and Corollary 2.6, DOI `10.1090/S0002-9939-07-08830-2`, directly own the
cyclic-continuant cancellation and even-denominator constant term; the
package records their exact normalization map `lambda_LM=2 lambda`.  C371
claims only its convention-locked reconstruction, explicit endpoint-fibre
factorization, and executable atlas, never object or formula priority.

### C372 -- Kirchhoff ellipse and the complete Love mode wall

**Owner.**  A constant-vorticity elliptic patch for the planar incompressible
Euler equation, evolved by contour dynamics in the unbounded plane.

**Large step.**  Derive the exact rigid rotation
`Omega=omega*a*b/(a+b)^2`, patch invariants, and freeze the full Love mode
formula

`lambda_m^2=(omega^2/4){[2mab/(a+b)^2-1]^2-[(a-b)/(a+b)]^(2m)}`,

with the linearized dispersion explicitly attributed to Love rather than
claimed as a package-new contour derivation.

Separate translation (`m=1`) and elliptic-family (`m=2`) symmetry directions;
prove existence and uniqueness of every higher-mode critical aspect ratio;
and prove analytically that `m=3` is the first unstable mode, giving the
sharp all-mode wall `a/b=3`.  Zero vorticity, the circular limit, axis swap,
critical zero-frequency behaviour, and unstable growth rates are kept explicit.  The
paper claims spectral linear stability only, not unproved nonlinear or
post-filamentation dynamics.

**Nearest collisions.**  C284 owns point-vortex relative equilibria, C299 a
viscous Lamb--Oseen vortex, and C368 a Polubarinova--Galin Laplacian-growth
free boundary.  None owns an inviscid uniform vortex patch, its exact elliptic
rotation, or the all-mode Love wall.

**Strict tuple.**
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`; the rotating patch has a
genuine physical clock and modal operator but no arithmetic owner or target
analytic bridge.

**Lineage sources.**  Kirchhoff's ellipse and Love's stability calculation
are treated as classical.  Modern convention and formula checks use the
source record identified in the package; no historical priority claim is
made.

### C373 -- the hemispherical Higgs oscillator

**Owner.**  The spherical oscillator with potential
`omega^2 R^2 tan^2(theta)/2` on one open hemisphere, together with the
Friedrichs quantum Hamiltonian selected by the equatorial barrier.

**Large step.**  Derive the exact radial action

`I_r=(sqrt(2R^2E+omega^2R^4)-|L|-omega R^2)/2`,

the action Hamiltonian, the exact `2:1` frequency locking, turning-point and
period atlas, and all classical boundary faces.  Solve the quantum problem in
Jacobi polynomials, including the full energy and multiplicity ledger, flat
limit, and zero-coupling Dirichlet-hemisphere limit.  Finally prove an
independent exact rationality criterion internal to the source spectrum: a full identity revival
exists exactly when `2 nu` is rational, with its least revival multiplier
given explicitly.  This rationality is not promoted to target arithmetic.

**Nearest collisions.**  C349 owns the Neumann oscillator on the full sphere,
C244 the spherical pendulum and focus--focus monodromy, and C313 the free
round-sphere geodesic flow.  None owns the equatorial `tan^2` barrier,
hemisphere Friedrichs spectrum, or exact revival criterion.

**Strict tuple.**
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`; the source
quantization is canonical, but it is not a target spectral realization.

**Lineage source.**  Higgs, *Dynamical symmetries in a spherical geometry I*,
DOI `10.1088/0305-4470/12/3/006`, with later separation-of-variables sources
audited inside the package.

## Round decision

All five candidates are retained because each closes a mathematically
independent all-parameter theorem with explicit singular faces and hostile
evidence.  C369 is the only structural arithmetic candidate.  C370 retains a
weak integer-weight relation; C371--C373 are deliberate cross-subtype controls
whose value is their source theorem rather than Route-A success.  No paper
introduces target arithmetic local data, target Euler factors or target
bad-prime data, root numbers, automorphy, a target divisor/counting law or functional equation,
a target-zero match, a Hilbert--Polya operator, or any Route-B input.
