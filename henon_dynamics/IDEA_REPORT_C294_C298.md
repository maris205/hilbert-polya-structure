# Route-A idea report: C294--C298

## Round objective and frozen baseline

The user requested another batch of exactly five independent papers, with a
large theorem-scale advance in every paper and Route A given priority.  The
collision baseline is `f8d3ad9a8940b54e82854b2924be353575ed8fcb`, the
fixed date is 2026-09-02, and the build epoch is `1788307200`.  Every candidate
is evaluated under `flow_systems/skills/route-a-evaluator.md` v0.2.0,
SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`,
with literal scope `NO_BAD_EULER_OR_ROOT_NUMBER`.

Independent scans covered all prior C1--C293 titles, both registries, recent
idea reports, and the nearest geometric, Hamiltonian, hybrid, matrix, and
spectral owners.  The retained systems change state space and proof mechanism
in every slot:

1. an open hyperbolic dispersing billiard;
2. an integrable smooth central-force Hamiltonian;
3. an event-driven hard-core many-body shape flow;
4. a non-Hermitian projective two-mode flow;
5. a nonlinear gradient flow on a Grassmann manifold.

`NEW` below means only that the workspace contains no package owning the
frozen theorem.  It is never a claim of priority in the literature.

## Frozen candidates

### C294 -- equilateral three-disk open billiard

**Owner.**  Three equal circular obstacles of radius `r`, with centers at an
equilateral triangle of side `d>4r/sqrt(3)`, and the unit-speed exterior
specular billiard.

**Large step.**  Prove by all-period convex minimization that every cyclically
reduced three-symbol word determines a unique non-grazing, isolated,
hyperbolic periodic-ray iterate, with word powers recording traversal
multiplicity and primitive classes giving primitive rays.  Close time
reversal, the strict no-eclipse boundary, length bounds, positive
determinant-one optical
monodromy, the exact fixed ledger

`F_n=2^n+2(-1)^n`,

its Möbius primitive counts, and the source collision zeta

`1/((1-2z)(1+z)^2)`.

**Nearest collision.**  C247 and C275 own integrable interior circular and
elliptic billiards; C148 and neighboring Walsh packages are open symbolic
surrogates.  None owns a physical no-eclipse obstacle flow in which the full
reduced shift codes periodic-ray iterates, primitive classes give unique
isolated primitive rays, and word powers record traversal multiplicity.

**Proof status.**  `PROVABLE AS STATED` only in the strict no-eclipse chamber.
Finite word enumeration is evidence, not the geometric existence/uniqueness
proof.

**Strict tuple.**
`(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`;
overall Route A rejected.  This is the round's strongest A1 advance.

### C295 -- Hénon isochrone action--frequency atlas

**Owner.**  The smooth Hénon isochrone potential

`V(r)=-mu/(b+sqrt(b^2+r^2))`, with `mu,b>0`.

**Large step.**  Prove the exact circular energy boundary and the complete
bound action Hamiltonian

`J_r=mu/sqrt(-2E)-(ell+sqrt(ell^2+4mu b))/2`, `ell=|L|`.

Derive the energy-only radial period, the exact azimuthal/radial frequency
ratio, the if-and-only-if rational closure criterion and primitive return
time, and separately close circles, the smooth center-crossing face, escape,
signed angular momentum, and the noncommuting Kepler-collision corner.

**Nearest collision.**  C216 owns Kepler conics and collision regularization;
C250 owns an isotonic action law.  Neither has the Hénon potential's radial
isochrony together with generic apsidal precession and its full action-domain
boundary.

**Proof status.**  `PROVABLE AS STATED` after freezing `ell=|L|`, the precise
energy chamber, and the fact that the rational closure test is for
noncircular `ell>0` orbits only.

**Strict tuple.**
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`;
overall Route A rejected.

### C296 -- rotation-reduced equal hard rods on a circle

**Owner.**  Equal-mass rods of length `a` on a circle of circumference
`ell>Na`, with elastic velocity exchange, after quotienting the common
spatial rotation and labels.

**Large step.**  Construct the global rotation-reduced shape flow and prove
its conjugacy to free points on the available circle `L=ell-Na`, modulo
permutations and common translation.  Recover all collision events,
simultaneous collisions, conservation laws and no-Zeno behavior, then give
the exact reduced return condition

`y_i+T v_i = y_(sigma(i))+c (mod L),  v_i=v_(sigma(i))`

and the velocity-stabilizer/least-return ledger.

**Hostile repair.**  The initially proposed full physical-space free quotient
was false.  For `N=1`, it predicts period `(ell-a)/|v|` instead of
`ell/|v|`; common rigid rotation gives the same obstruction for every `N`.
Changing the cyclic cut shifts all compressed points by `a`, so the omitted
global rotation is a genuine cocycle.  C296 therefore owns only the explicitly
rotation-reduced shape flow and records the reconstruction obstruction rather
than hiding it.

**Nearest collision.**  C292 is irreversible sticky aggregation, C196 is a
smooth no-collision Calogero flow, and C212 is a one-body affine impact map.
None owns this elastic many-body shape quotient and its return stabilizer.

**Proof status.**  `PROVABLE AS CORRECTED`: the false full physical-space
version was replaced before release by the precisely rotation-reduced shape
theorem.  No positive full-physical-space conjugacy or reconstruction theorem
is shipped; the missing rotation is retained only as the explicit cocycle
obstruction that forced the correction.

**Strict tuple.**
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`;
overall Route A rejected, subject to the final evaluator audit.

### C297 -- PT-symmetric dimer

**Owner.**  The autonomous balanced-gain/loss matrix

`H=[[i gamma,kappa],[kappa,-i gamma]]`, `kappa>0`, acting on vectors in
`C^2` and rays in `CP^1`.

**Large step.**  Use `H^2=(kappa^2-gamma^2)I` to obtain the exact propagator
and the unbroken / exceptional / broken atlas.  Prove the generic vector and
projective least periods, the rank-one nilpotent exceptional growth, the
attracting/repelling broken rays, the global Riccati field, the conserved
indefinite form, and the explicit pseudo-Hermitian metric whose signature
changes sharply at the exceptional point.

**Nearest collision.**  C118 is a nonlinear conformally symplectic discrete
dimer, C223 is Hermitian Jaynes--Cummings, C224 is nonautonomous
Landau--Zener scattering, and C243 is a nonlinear Bose--Josephson dimer.
None owns the autonomous non-Hermitian three-phase projective-and-metric
theorem.

**Proof status.**  `PROVABLE AS STATED`.  The Riccati quadratic discriminant
is `-4 delta`, whereas the matrix characteristic discriminant is `+4 delta`;
the independent symbolic lane caught this sign distinction before release.

**Strict tuple.**
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`;
overall Route A rejected.  The positive metric is not transported through the
exceptional point and is not a Hilbert--Pólya construction.

### C298 -- Oja--Grassmann Schubert flow

**Owner.**  For a real symmetric matrix `A`, the rank-`k` orthogonal
projection flow

`dot P=[P,[P,A]]` on the real Grassmannian.

**Large step.**  Prove the global exact solution

`Ran P(t)=exp(tA) Ran P(0)`

and the resulting exponential law for every Plücker coordinate.  For simple
spectrum, close every Schubert cell rather than only generic initial data:
identify its limiting coordinate subspace, the actual nonzero-support rate,
all equilibria, and every exchange-mode stable/unstable dimension.  For
repeated spectrum, replace isolated equilibria by the full product-Grassmann
Morse--Bott family and prove convergence to the associated graded subspace.
A strict Lyapunov identity excludes nonconstant recurrence.

**Nearest collision.**  C185 evolves a full fixed-spectrum matrix by a
Brockett double bracket.  C298 evolves a rank-`k` subspace and its complete
Schubert/Plücker stratification; this is a different state manifold and
theorem owner.

**Proof status.**  `PROVABLE AS STATED` only if possible subset-sum ties are
handled through the flag/matroid support rather than an assumed globally
unique second Plücker weight.  The finite evidence must cover nongeneric
cells and repeated-eigenvalue faces.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`;
overall Route A rejected.

## Rejected or reserved alternatives

- Farey-map and continued-fraction candidates were rejected because
  C174/C179/C199/C209 already occupy the closest modular and induced
  symbolic owners; a renamed parabolic branch map would not be a clean new
  paper.
- A hexagonal flat-torus/Eisenstein dictionary was reserved because C152 and
  neighboring square-lattice billiard/spectral packages make the change of
  lattice too easy to misread as the main advance.
- Hegselmann--Krause dynamics survived collision screening but has no positive
  Route-A axis; C294's physical isolated-ray bridge and C298's full Schubert
  theorem were stronger choices for this batch.
- Kronig--Penney, a flat Klein bottle, relativistic Coulomb motion, and a
  harmonic run-and-tumble process remain viable independent future owners.
  They were not used to pad this five-paper round.

No retained package introduces target arithmetic local data, target Euler
factors, root numbers, automorphy, a target divisor/counting law or functional
equation, a target zero match, a Hilbert--Pólya operator, or Route-B
authorization.
