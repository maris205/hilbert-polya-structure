# Route-A idea report: C354--C358

## Round objective and frozen baseline

The user requested exactly five finished papers, each taking a theorem-scale
step, with a change of dynamical subtype whenever a candidate would merely
extend an existing owner.  The collision scan covered the C1--C353 candidate
and obstruction registries, 391 first-level directories, earlier idea reports,
and mechanism-level neighbors.  Geometric-offspring Galton--Watson,
Bernoulli--Laplace, the ordinary Aharonov--Bohm ring, another reaction--diffusion
window, and synchronous complete-graph push were rejected as direct or near
collisions.  The retained owners are a heavy rigid body, an infinite-group
random walk, a topological Bloch pump, a nonsmooth isochronous oscillator, and
a cyclic competitive flow.  No retained paper is a parameter slice or a
deferred section of another.

The frozen collision baseline is
`140c8714b74de666d56f441ddfb712026955901a`, the date is `2026-09-03`, and
the build epoch is `1788393600`.  Every candidate uses
`flow_systems/skills/route-a-evaluator.md` v0.2.0 at SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`
and literal scope `NO_BAD_EULER_OR_ROOT_NUMBER`.  `NEW` means only that no
workspace package owns the frozen theorem; it is not a literature-priority
claim.

## Frozen candidates

### C354 -- Lagrange heavy top and two-phase closure

**Owner.**  The axisymmetric heavy top with a fixed point, positive transverse
and axial inertias, centre of mass on the body symmetry axis, and positive
gravity scale.

**Large step.**  Reduce the three conserved quantities to the complete cubic
equation for `u=cos(theta)`; classify every admissible root chamber; write the
regular nutation in Jacobi form; derive both reconstructed Euler-angle
increments as branch-locked third-kind elliptic integrals; and prove that a
regular physical `SO(3)` orbit closes exactly when both phase increments are
rational multiples of `2*pi`.  Close steady precession, double/triple roots,
separatrices, Euler-pole compatibility, sleeping tops, zero gravity, free
symmetric and spherical-top faces without using a coordinate pole as a
physical singularity.

**Nearest collision.**  C186 owns the torque-free Euler top, C244 the spherical
pendulum, C344 a resonant triad, and C349 the Neumann sphere.  None owns a
two-sided symmetric rigid body with gravity, spin momentum, and two-angle
reconstruction.

**Strict tuple.**
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`; Route A is
rejected and Route B locked.

### C355 -- Kesten spectrum and escape on a free group

**Owner.**  Uniform nearest-neighbour random walk on the free group `F_d`,
`d>=2`, with its self-adjoint convolution operator on `ell^2(F_d)`.

**Large step.**  Solve the tree cavity resolvent; prove the complete purely
absolutely continuous Kesten spectrum and root spectral density; derive the
radial birth--death chain, every even-time return probability by an exact
Dyck-excursion count, and the total first-return probability; then prove the
almost-sure escape speed and radial CLT.  Close the amenable `d=1` boundary,
where the spectral radius, recurrence, speed, and scaling law all change.

**Nearest collision.**  C341 is a finite lamplighter chain, C306 a killed
finite Weyl-chamber process, and C333 a finite gossip product.  None is an
infinite nonamenable Cayley-tree convolution operator with a Kesten measure
and ballistic escape theorem.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`; Route A is rejected and
Route B locked.

### C356 -- QWZ--Thouless Chern pump

**Owner.**  The periodic two-band Bloch family

`H_m(k,tau)=sin(k)sigma_x+sin(tau)sigma_y`
`           +(m+cos(k)+cos(tau))sigma_z`

on the momentum--pump torus.

**Large step.**  Determine the exact direct gap and prove that it closes
exactly at `m=-2,0,2`; construct the smooth occupied-band projector in every
gapped chamber; compute its first Chern number with a frozen orientation;
resolve all four Dirac points and their signed jumps; and identify the
adiabatic filled-band pumped charge with that Chern number under an explicit
uniform-gap and adiabatic-limit hypothesis.  Gapless walls and finite-speed
nonquantized corrections remain separate.

**Nearest collision.**  C318 owns a static finite SSH bulk--edge atlas, C331 a
Dirac-monopole sphere, and C337 an integer-resonant kicked rotor.  None owns a
two-parameter Bloch bundle with a full mass-chamber Chern/pump classification.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`; Route A is
rejected and Route B locked.  A Chern integer is source topology, not a
rational-prime carrier.

### C357 -- two-stiffness nonsmooth isochronous oscillator

**Owner.**  The continuous Hamiltonian

`H=p^2/2+(omega_+^2/2)(x_+)^2+(omega_-^2/2)(x_-)^2`

with independent nonnegative one-sided stiffnesses.

**Large step.**  Prove that every nonzero orbit is bounded and periodic
exactly when both stiffnesses are positive; derive its energy-independent
period and exact action; construct a seam-compatible piecewise-smooth
action--angle chart and full-return monodromy; and, for the Friedrichs
Schrodinger operator, prove a complete simple discrete spectrum characterized
by one parabolic-cylinder Wronskian equation.  Close equal stiffness, zero
energy, one flat half-line, and the free-particle face.

**Nearest collision.**  C212 has impact resets, C232 a smooth nonisochronous
Duffing potential, C238 dissipative Filippov friction, and C252 hysteretic
switching.  C357 is continuous, conservative, `C^1`-potential dynamics with a
stiffness seam and no reset.

**Strict tuple.**
`(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`; Route A
is rejected and Route B locked.

### C358 -- May--Leonard cyclic competition trichotomy

**Owner.**  The three-species cyclic Lotka--Volterra competition flow in the
strict intransitive chamber `(a-1)(b-1)<0`.

**Large step.**  Prove global positive flow and use
`R=xyz/(x+y+z)^3` to classify the full interior dynamics by `a+b`.  Below two,
every interior orbit converges to coexistence.  At two, normalize by total
population and an exact logistic time change to obtain a foliation by periodic
rock--paper--scissors leaves with an elliptic period quadrature and a unique
asymptotic phase.  Above two, the diagonal is the exact stable manifold of the
unstable coexistence point and every other interior orbit approaches the full
oriented boundary heteroclinic cycle with diverging residence times.  Close
coordinate faces, orientation reversal, the origin, axial equilibria and the
`a=b=1` degenerate simplex.

**Nearest collision.**  C211 is a two-species Hamiltonian Lotka--Volterra
period annulus, C254 a Monod chemostat threshold, C271 network SIS, and C347 a
noisy mean-field phase PDE.  None owns the three-dimensional cyclic
coexistence/periodic-leaf/heteroclinic transition.

**Strict tuple.**
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`; Route A is rejected and Route B
locked.

## Source and claim boundary

The source lineages are Lagrange and modern elliptic reconstruction for C354,
Kesten for C355, Qi--Wu--Zhang and Thouless for C356, asymmetric piecewise
quadratic oscillators and Sturm--Liouville theory for C357, and May--Leonard
for C358.  Each package supplies its own proof and treats sources as ownership
and convention context.

No package introduces target arithmetic local data, target Euler factors,
bad-prime data, root numbers, automorphy, a target divisor/counting law or
functional equation, a target-zero match, a Hilbert--Polya operator, or
Route-B authorization.
