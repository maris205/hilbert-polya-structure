# Route-A idea report: C284--C288

## Round objective and baseline

This round follows the user's A-first instruction while requiring five
independent theorem-scale advances.  The source baseline is
`3878fa5282ca89f75700b3ef9d623f54dcb7bcf9`; the fixed date is 2026-09-02
and the build epoch is `1788307200`.  Every candidate uses
`flow_systems/skills/route-a-evaluator.md` v0.2.0, SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`,
and literal scope `NO_BAD_EULER_OR_ROOT_NUMBER`.

The collision scan covered every C1--C283 package title, the candidate and
obstruction registries, recent rejected/reserved ideas, and neighboring
`flow_systems`/`symbolic_dynamics` owners.  The retained state spaces and
proof mechanisms are intentionally different:

1. a singular first-order Hamiltonian vortex system;
2. a finite nonreversible closed queueing CTMC;
3. a state-dependent Weyl-reflection rewrite system;
4. a conservative hyperbolic PDE with boundary observation/control;
5. a singular self-adjoint quantum Hamiltonian.

`NEW` means only that no earlier workspace package owns the frozen theorem.
It is not a literature-priority claim.

## Frozen candidates

### C284 — Thomson polygon point-vortex stability

**Owner.**  Equal positive-strength planar Helmholtz--Kirchhoff vortices at
the vertices of a regular `N`-gon, `N>=3`, in the co-rotating frame.

**Large step.**  Derive the relative-equilibrium angular speed directly from
the pair Hamiltonian; reconstruct the complete Cartesian Hessian; use a
radial/tangential DFT to close every reduced Fourier block; and prove the
sharp linear classification: `N=3,...,6` elliptic after symmetry reduction,
`N=7` exactly degenerate in modes `3,4`, and every `N>=8` hyperbolic.  The
sign is governed by `2(N-1)-m(N-m)`.  Translation, rotation, scaling,
`Gamma=0`, `R=0`, and `N=2` are separated.  No nonlinear stability is
inferred at seven.

**Nearest collision.**  C217 is a linear shallow-water PDE, C243 a dimer,
C259 Kuramoto locking, and C274 a quadratic Penning trap.  None has the
noncanonical first-order point-vortex symplectic structure or the all-`N`
Thomson threshold.

**Strict tuple.**
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`; overall rejected.

### C285 — Gordon--Newell network and tied-bottleneck condensation

**Owner.**  An arbitrary finite irreducible closed single-server network
with `N` customers, possibly nonreversible routing, and exponential service.

**Large step.**  Prove the canonical product form
`pi_N(n)=Z_N^{-1} product_i w_i^{n_i}` with
`Z_N=h_N(w)`; close all occupation derivatives, station throughputs, directed
edge currents, time reversal, and the reversibility criterion; then prove the
complete unique/tied bottleneck limit.  Nonbottleneck occupancies converge to
independent geometric laws, a unique bottleneck absorbs `N-O(1)` customers,
and tied bottleneck fractions converge to the uniform Dirichlet law.

**Nearest collision.**  C225 is one finite-capacity birth--death queue, C233
an open infinite-server chain, and C220 open TASEP.  They have no arbitrary
nonreversible routing, canonical fixed-population ensemble, reversal flow, or
multi-bottleneck condensation.

**Strict tuple.**  All five axes fail; overall rejected.

### C286 — Coxeter numbers-game strong convergence

**Owner.**  Legal positive-coordinate firing by simple reflections for a
finite crystallographic Coxeter system, starting on any dominant face.

**Large step.**  Prove every legal firing order terminates at the same
antidominant point, every order has length
`|Phi^+|-|Phi_J^+|`, and its cumulative element is the unique shortest
parabolic-coset representative carrying the starting weight to the endpoint.
Close strictly dominant, wall, zero, rank-one, and disconnected faces; keep
affine/indefinite claims outside the finite theorem.

**Nearest collision.**  C192 studies a random face-semigroup walk and C185 a
continuous isospectral sorting flow.  The present invariant is deterministic
state-dependent Weyl reduction and exact parabolic face length.

**Strict tuple.**  All five axes fail; overall rejected.

### C287 — one-dimensional wave boundary-control minimal time

**Owner.**  The Dirichlet wave group on `(0,L)`, observed through the normal
derivative at one endpoint and controlled there by HUM duality.

**Large step.**  Prove the least common revival time and sharp one-sided
observability/control threshold are both `2L/c`, including equality.  At the
critical time derive the exact Parseval identity
`int_0^(2L/c)|u_x(t,L)|^2 dt=4E(0)/c^3`; for every shorter time construct a
compact traveling pulse with zero observation.  Freeze energy/transposition
spaces, the no-zero-mode fact, endpoint reversal, and all scaling faces.

**Nearest collision.**  C218 is a dissipative Kelvin--Voigt spectral problem,
C157 a two-dimensional half-wave trace, C261 an Airy revival, and C222 a
finite-dimensional bang--bang system.  None owns the exact infinite-
dimensional boundary control threshold.

**Strict tuple.**
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`; overall
rejected.

### C288 — one-dimensional delta point interaction

**Owner.**  The full-line self-adjoint extension
`H_alpha=-d^2/dx^2` with continuity and derivative jump
`psi'(0+)-psi'(0-)=alpha psi(0)`.

**Large step.**  Close the form/domain realization, negative-energy rank-one
resolvent, all sign-dependent spectrum, the unique attractive bound state,
left/right and even/odd scattering, the exact erfc heat kernel, and its
integrated relative diagonal trace.  Pole, free, zero/high-energy, and
small/large-time boundaries use one normalization.

**Nearest collision.**  C267 is an infinite lattice ladder, C231 a spatial
front Hessian, and C133/C138 finite metric quantum graphs.  None owns the
one-center full-line extension and its resolvent/scattering/heat closure.

**Strict tuple.**
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`; overall
rejected.

## Rejected or reserved alternatives

- CR3BP was viable but would have given this batch a second planar
  Hamiltonian stability atlas.
- Square-root Loewner dynamics was viable but has a direct published owner
  and a higher branch-convention risk than the retained five.
- Morse dynamics was reserved because its one-degree-of-freedom action
  mechanism sits near C250 and C232.
- Ordinary coupon collection, M/G/1, rowmotion, Burgers, sandpile, box--ball,
  and generic graph quantum walks remain rejected because earlier packages or
  explicit kill ledgers already own their main mechanism.

Every finite computation is a convention audit, not the proof of an
arbitrary-size or infinite-dimensional theorem.  No package introduces
target arithmetic local data, Euler factors, root numbers, automorphy, a
target divisor/counting law or functional equation, a target zero match, a
Hilbert--Pólya operator, or Route-B authorization.
