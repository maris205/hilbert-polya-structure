# Route-A idea report: C234--C238

Date: 2026-08-29

Source/code baseline: `0ebc633706bc34b8b915a44749423486fd4cd243`.

Evaluator: `flow_systems/skills/route-a-evaluator.md`, v0.2.0, SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.

Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Design objective

This round takes one complete theorem-scale step in each paper while changing
the dynamical owner in every slot.  The five state spaces and proof mechanisms
are a dissipative spin on the sphere, a cyclic population flow on a simplex,
an integrable hyperbolic field equation, a hypoelliptic phase-space diffusion,
and a nonsmooth differential inclusion.  None is an installment of another
paper.  `NEW` below means absent from the frozen owner list in this workspace;
it is not a claim of literature priority or novelty.

## Collision screening and pivots

- **C234 versus two-level quantum crossings and rigid-body flows.**  The owner
  is the classical constant-field Landau--Lifshitz--Gilbert equation on
  `S^2`, not the nonautonomous Landau--Zener scattering problem of C224 or the
  conservative Euler top.  Gilbert damping produces a globally explicit
  stereographic contraction and a pole-to-pole stability atlas.
- **C235 versus Hamiltonian Lotka--Volterra and epidemic flows.**  The owner is
  cyclic rock--paper--scissors replicator dynamics with one precisely frozen
  additive uniform-mutation law.  Its zero-mutation period foliation and its
  positive-mutation global Lyapunov contraction are proved in the same
  theorem.  No statement is extended to arbitrary mutation matrices.
- **C236 versus NLS and Allen--Cahn fronts.**  Sine--Gordon is a conservative
  hyperbolic field equation with topological kinks and time-periodic breathers.
  The theorem classifies the declared monotone traveling heteroclinics and
  audits the explicit breather family; it does not classify every finite-
  energy solution or every localized time-periodic solution.
- **C237 versus scalar diffusions and the circular telegraph process.**  The
  harmonic Kramers process is a two-coordinate hypoelliptic Ornstein--Uhlenbeck
  diffusion.  Its exact Gaussian Mehler kernel, damping-regime matrix flow and
  critical-damping optimum are distinct from a one-dimensional reversible
  diffusion or a two-velocity jump process.  No unproved full nonnormal
  `L^2` spectral theorem is inferred.
- **C238 versus impact maps and bounded control.**  The owner is a continuous-
  time Coulomb dry-friction oscillator with the multivalued sign graph fixed
  as a Filippov/maximal-monotone viability law.  This closes the sticking
  selection that blocked an earlier reserve.  It is not a reset impact map or
  an optimization policy.

Source-local spectra, periodic families, Gaussian kernels, event maps and
factorizations are not relabelled as arithmetic local data, target divisors,
Euler factors or Hilbert--Polya operators.  None of the five owners supplies a
rational-prime primitive carrier, a prime-power repetition law or a physical
`log p` clock.

## Frozen independent theorem increments

### C234 -- constant-field Landau--Lifshitz--Gilbert macrospin

For
`m_dot=-omega m cross e3-alpha omega m cross (m cross e3)` on the unit sphere,
close every nonnegative `alpha,omega` face.  In south-pole stereographic
coordinates prove the scalar complex flow
`z_dot=(-alpha*omega+i*omega)z`, reconstruct the full trajectory and the
hyperbolic-tangent law for `m_3`, prove exact energy dissipation and pole
stability, and separate the conservative latitude circles, identity face,
poles and resonant sampled-time fixed continua.

### C235 -- cyclic replicator with additive uniform mutation

For the cyclic simplex system
`x_dot=a*x*(y-z)+mu*(1/3-x)` and its rotations, prove simplex invariance and
close the full `a,mu>=0` atlas.  At `mu=0`, prove conservation of `xyz`, the
interior period foliation, boundary heteroclinic cycle and exact period
quadrature with its center limit.  At `mu>0`, use the exact logarithmic-product
identity and AM--GM to prove global convergence to the barycenter and exclude
nonconstant recurrence.  Include the linear contraction and identity faces.

### C236 -- sine--Gordon kink and breather atlas

For `u_tt-u_xx+sin(u)=0`, classify all finite-energy monotone traveling
heteroclinics as Lorentz-boosted kinks or antikinks, including their charge,
energy and momentum.  Verify the rest and boosted breather family, its period,
rest energy and limiting faces.  Factor the kink Hessian
`-d^2/dx^2+1-2 sech^2(x)` and identify its translation kernel, continuous
edge and absence of an internal discrete mode.  Claims remain restricted to
these declared coherent families.

### C237 -- harmonic Kramers--Langevin Mehler flow

For the phase-space diffusion
`dQ=P dt`, `dP=(-omega^2 Q-gamma P)dt+sqrt(2 gamma/beta)dW`, prove the exact
matrix exponential in underdamped, critical and overdamped regimes, the
Gaussian transition covariance and Gibbs invariant law, and the Kalman
hypoellipticity criterion.  Close stationary correlations, the sharp drift
spectral-abscissa rate and the critical-damping optimizer, with its polynomial
prefactor.  Keep the Hamiltonian zero-damping and unconfined zero-frequency
boundaries separate.

### C238 -- Coulomb dry-friction Filippov oscillator

For `x''+omega^2 x+c Sign(x')` containing zero with
`Sign(0)=[-1,1]`, fix the viability selection, prove the exact sticking band
and unique inward release, and integrate every sliding arc by a shifted
harmonic center.  Derive the first-stop phase, half-cycle turning map, exact
integer count to finite capture and the energy dissipation identity.  Close
the harmonic zero-friction boundary without importing an impact reset.

## Frozen strict expectations

| paper | A0 | A1 | A2 | A3 | A4 | overall |
|---|---|---|---|---|---|---|
| C234 | `A0_FAIL` | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C235 | `A0_FAIL` | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C236 | `A0_FAIL` | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_NATURAL_QUANTIZATION` | `ROUTE_A_REJECTED` |
| C237 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C238 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |

These are frozen design expectations.  The release verdict must be read from
each content-addressed evidence/evaluator pair after independent validation.
`route_b_invocation_allowed` remains false throughout.  Candidate-local
Hamiltonian or linearized operators do not authorize target arithmetic,
automorphy, a target functional equation, or Route-B input.
