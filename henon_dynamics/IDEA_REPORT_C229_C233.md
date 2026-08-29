# Route-A idea report: C229--C233

Date: 2026-08-29

Source/code baseline: `e1dc522e054c2d0ded74b017bc52c7b016a52c59`.

Evaluator: `flow_systems/skills/route-a-evaluator.md`, v0.2.0, SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.

Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Design objective

This round follows the Route-A instruction to take a large, complete step in
each paper while changing the dynamical subtype.  The five owners are a
degenerate positive diffusion, a finite integrable lattice, a dissipative
reaction--diffusion front, a conservative nonlinear oscillator, and a
countable-state Markov semigroup.  They have different state spaces, clocks,
invariants and proof tools; none is a five-part decomposition of one result.
The word `NEW` below means absent from the earlier owner list in this
workspace, not a literature-priority or novelty claim.

## Collision screening and pivots

- **C229 versus Jacobi/Wright--Fisher and other diffusions.**  Earlier
  diffusion packages use compact beta-type state spaces or a different
  degeneracy.  The CIR square-root coefficient has a distinct Feller boundary
  classification, affine Laplace transform, Gamma law and Laguerre spectrum.
  The zero-drift, zero-volatility and boundary atoms are kept as CIR faces,
  not folded into a generic diffusion template.
- **C230 versus earlier sorting and action--angle flows.**  The owner is the
  finite *open* Toda lattice with positive Jacobi edges and scattering data.
  Lax isospectrality, Moser sorting, norming weights and the explicit `N=2`
  sech trajectory are proved together.  No periodic-orbit ledger is inferred
  from the scattering coordinates.
- **C231 versus Fisher--KPP and other fronts.**  Allen--Cahn is a balanced
  gradient front with a selected zero speed and a Pöschl--Teller spatial
  Hessian.  This is not the Fisher--KPP traveling-wave threshold or a claim
  about nonlinear spectral stability; the translation kernel and essential
  edge are source-local and explicitly audited.
- **C232 versus positive Hamiltonian period annuli.**  The Duffing owner is a
  quartic one-degree-of-freedom oscillator with a double-well separatrix.
  Its turning-root quadratic, endpoint-cancelled period/action integrals and
  homoclinic sech profile close the barrier boundary.  The continuum of
  energy ovals is retained as an obstruction to a discrete primitive owner.
- **C233 versus M/M/1/K and branching processes.**  M/M/infinity is the
  countable immigration--death chain, not the reflected finite queue and not
  the two-rate branching PGF.  Its exact binomial-survivor plus
  Poisson-immigration kernel, all Charlier modes, positive-time trace and
  rate-boundary atlas are proved in one package.

None of the five source owners has an intrinsic rational-prime carrier,
prime-power repetition law, or physical `log p` clock.  A source-local
  spectrum, scattering invariant, Fredholm product, action, or generating
  function is therefore not relabeled as a target divisor or a
  Hilbert--Pólya operator.

## Frozen independent theorem increments

### C229 -- CIR square-root diffusion

For `dX=kappa(theta-X)dt+sigma*sqrt(X)dW` on the nonnegative half-line, close
the all-parameter Feller boundary atlas (including the atom at zero), the
affine Laplace transform and noncentral-chi-square transition law, and the
Gamma invariant measure on the nondegenerate face.  Diagonalize the generator
with normalized Laguerre modes, prove the sharp gap and mixing estimate, and
keep deterministic, zero-volatility and zero-mean boundary faces separate.

### C230 -- open Toda Lax/scattering flow

For every finite open Toda chain with positive Flaschka edges, prove the global
Hamiltonian and Jacobi Lax equations, simple isospectral invariants, Moser
sorting and norming weights, and the exact `N=2` sech scattering trajectory.
Close the action--angle boundary rows and distinguish asymptotic scattering
from recurrent periodic dynamics.  The finite ledger is an audit of the
source theorem, not an arithmetic orbit product.

### C231 -- Allen--Cahn front and Pöschl--Teller spectrum

For the balanced Allen--Cahn gradient equation, derive the unique translated
heteroclinic `tanh` front and the selected speed `c=0`, prove the energy
dissipation identity, factor the spatial linearization, and identify its
translation kernel and essential spectral edge.  Zero diffusivity,
unbalanced forcing and orientation faces remain explicit; no nonlinear Hopf
or target operator claim is made.

### C232 -- Duffing energy topology and separatrix

For `x_dot=v`, `v_dot=-delta*x-beta*x^3` with `beta>0`, classify every regular
energy component in the single- and double-well regimes, solve the turning
points as a quadratic in `x^2`, and evaluate endpoint-cancelled period and
action quadratures with `I'(E)=T(E)/(2*pi)`.  Close the quartic, center and
saddle limits, the explicit homoclinic `sech` orbit, and the `beta=0` faces.
The continuum-energy boundary is a declared Route-A obstruction.

### C233 -- M/M/infinity Poisson--Charlier semigroup

For the immigration--death generator on `N_0`, prove the unique positive-rate
Poisson invariant law, the exact binomial-survivor/Poisson-immigration kernel
and PGF, the complete Charlier eigenbasis and gap, the positive-time trace and
source Fredholm product, and coupling total-variation bounds.  Pure-death,
pure-birth, identity, small-intensity, small-service and long-time faces are
separate theorem statements; a finite PMF window is only a regression oracle.

## Frozen strict expectations

| paper | A0 | A1 | A2 | A3 | A4 | overall |
|---|---|---|---|---|---|---|
| C229 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C230 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C231 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C232 | `A0_FAIL` | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C233 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |

These are frozen design expectations only; the release verdict is read from
each content-addressed evidence/evaluator pair.  `route_b_invocation_allowed`
remains false for every candidate.  A formal source-local spectrum or action
coordinate does not authorize a target quantization, arithmetic local datum,
Euler factor, root number, automorphy claim, target functional equation, or
Route-B input.
