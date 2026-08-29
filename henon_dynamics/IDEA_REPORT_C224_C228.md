# Route-A idea report: C224--C228

Date: 2026-08-29

Source commit: `489672bd36abd3a4f6da92d1446a0af575917959`.

Evaluator: `flow_systems/skills/route-a-evaluator.md`, v0.2.0, SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.

Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Design objective

This round follows the A-route instruction to make a large, complete advance
in every paper while deliberately changing the dynamical subtype.  The five
owners are a nonautonomous scattering system, a finite Markov semigroup, a
parabolic free-boundary problem, a dissipative quadratic flow, and a nonlinear
kinetic equation with gelation.  Each package has its own phase space, clock,
normalization, theorem, executable receipt, two substantive manuscript
revisions, and strict stopping decision.  `NEW` means only that the frozen
owner is not already represented by an earlier workspace package; it is not a
priority or novelty claim.

## Collision decisions, kills, and pivots

- Ordinary open Toda was screened out: its Lax, sorting, and scattering
  language would collide with the established C182/C185/C196/C204/C209
  owner families.  The replacement is the genuinely nonautonomous
  Landau--Zener--Weber crossing (C224), whose finite-window ODE ledger is kept
  separate from its exact asymptotic connection law.
- The finite M/M/1/K queue (C225) is not C208's branching PGF or C220's
  boundary-driven exclusion chain.  Its theorem owner is the reversible finite
  birth--death generator, with a separate finite-capacity-to-infinite-capacity
  boundary atlas and no asserted continuous-spectrum theorem.
- The one-phase Stefan problem (C226) is a moving free boundary, not a fixed
  support diffusion.  The Neumann root, endpoint enclosures, flux partition,
  energy ledger, and zero-rate/rescaling faces are closed together.
- Lorenz-63 (C227) is retained for a global absorbing ellipsoid and a complete
  equilibrium/local-stability atlas.  Linear Hopf data are explicitly not
  promoted to a nonlinear chaos or Hopf-direction theorem.
- Product-kernel Smoluchowski coagulation (C228) is selected for an exact
  gelation boundary.  The Stockmayer/Smoluchowski and gel-reactive Flory
  postgel closures are kept as different equations, so no uniqueness claim is
  smuggled across the closure boundary.

None of the five owners supplies an intrinsic rational-prime carrier,
prime-power repetition law, or a logarithmic prime clock.  Source-local
  spectra, scattering phases, generating functions, and moments are therefore
  not converted into an arithmetic or Hilbert--Pólya object.

## Frozen theorem increments

### C224 -- Landau--Zener--Weber scattering

For the linear diabatic sweep
`i psi_dot=((v t/2) sigma_z+g sigma_x) psi`, close the scalar Weber reduction,
the exact asymptotic diabatic survival probability and Gamma/Stokes phase,
unitary scattering normalization, coupling-sign gauge, adiabatic/sudden
limits, and a controlled finite-window RK4 propagator ledger.  The finite
window rows are numerical controls with an explicitly reported Gram residual,
not an exact finite-time Weber formula.

### C225 -- finite M/M/1/K spectral--mixing atlas

For every declared finite capacity and nonnegative rate face, close the
stationary law, symmetric Jacobi conjugation, full finite spectrum and modes,
transient kernel, gap and TV/L2 mixing certificate, then separate the
`K -> infinity` positive-recurrent, null-recurrent, and mass-escape regimes.
Finite characteristic polynomials are not promoted to an infinite determinant.

### C226 -- one-phase Stefan--Neumann similarity

For the normalized heat/free-boundary model, prove existence and uniqueness of
the positive Neumann root, a five-term small-Stefan inverse series, a two-sided
large-Stefan Lambert-W enclosure, exact wall/interface flux partition, and the
sensible-plus-latent moving-domain energy identity.  Zero superheat,
zero diffusivity, and zero latent heat are singular rescalings, not finite
interface continuations.

### C227 -- Lorenz-63 dissipativity and stability atlas

For all positive `sigma,beta` and real `rho`, derive the shifted Lyapunov
identity and explicit absorbing ellipsoid, classify the origin and wing
equilibria, factor the Routh--Hurwitz margin and Hopf surface, and isolate
`rho=1`, zero-rate, and double-zero boundaries.  The package stops at local
linear stability and does not claim global chaos or a nonlinear Hopf direction.

### C228 -- product-kernel coagulation and postgel closure boundary

For monodisperse multiplicative-kernel concentrations, derive every pregel
coefficient, rooted/unrooted tree generating functions, moments, gel time and
critical tail, then verify the two inequivalent postgel loss closures and their
Lambert-W branch selection.  The branch distinction is part of the theorem;
finite coefficient rows remain regression controls for an all-size statement.

## Frozen strict expectations

| paper | A0 | A1 | A2 | A3 | A4 | overall |
|---|---|---|---|---|---|---|
| C224 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_UNITARY_OR_SCATTERING_CANDIDATE` | `ROUTE_A_REJECTED` |
| C225 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C226 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C227 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FAIL` | `ROUTE_A_REJECTED` |
| C228 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FAIL` | `ROUTE_A_REJECTED` |

These are frozen expectations only; each final tuple is read from its own
content-addressed evidence and evaluator record.  Every Route-B permission
remains false.
