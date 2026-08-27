# Route-A idea report: C199--C203

Date: 2026-08-27

Source commit: `d1e58971e570b855488009af384995702ddb887b`.

Evaluator: `flow_systems/skills/route-a-evaluator.md`, v0.2.0, SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.

Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Design objective

This round applies the large-step rule at theorem scale.  Each paper owns a
complete parameter family and a different kind of dynamics: nonholonomic
mechanical scattering, a degenerate reversible diffusion, an inertial
optimization recurrence, a reaction--diffusion traveling-wave reduction, and
a signed-network gradient semigroup.  None is one chapter of a common result.

`NEW` means only that C1--C198 contains no package with the same frozen
dynamical owner.  It is not a literature-priority claim.  Classical sources
retain ownership; the retained contribution is a convention-locked theorem
synthesis, explicit boundary and counterexample atlas, independent executable
certificate, complete paper, and strict Route-A decision.

## Collision scan, kills and pivots

- **Chaplygin sleigh revived only after enlarging the theorem owner.**  It was
  deferred in C194--C198 because a bare `tanh/sech` reduction was too small.
  C199 survives by closing the signed-offset parameter family, full `SE(2)`
  reconstruction, energy-independent angular scattering, asymptotic lines,
  transverse stability, singular invariant measure, reversibility, and the
  balanced-sleigh boundary in one theorem.  This is nonholonomic scattering,
  not a second compact Euler-top or Calogero--Moser paper.
- **Jacobi--Wright--Fisher retained with an explicit realization firewall.**
  C200 freezes the conservative zero-flux diffusion rather than only a formal
  differential expression.  Its continuous state space, degenerate endpoint
  classification, Beta reversibility, complete Jacobi spectrum and moment
  closure do not duplicate the finite Krawtchouk/Ehrenfest or other Markov
  packages.  The paper explicitly distinguishes recurrent sample paths from
  the absence of nonconstant periodic semigroup observables.
- **Polyak heavy-ball retained as a full real-parameter second-order atlas.**
  C201 is not another Douglas--Rachford contraction theorem.  Its owner is the
  inertial companion recurrence over every SPD spectral interval, including
  negative momentum, the exact Jury triangle, the unique minimax root factor,
  endpoint Jordan transients, and the symplectic boundary.
- **Fisher--KPP retained instead of a second finite-state model.**  C202 closes
  the entire wave-speed phase portrait, minimal-speed threshold, critical and
  supercritical tails, subcritical sign-change obstruction, zero-speed
  Hamiltonian boundary, and an exact nontrivial control wave.  Finite residual
  tests do not replace the shooting/trapping proof.
- **Signed weighted consensus retained only with its forest theorem.**  The
  elementary balanced/unbalanced limit alone would be too small.  C203 adds
  every disconnected positive-weight graph, exact orthogonal limit and rate,
  all rooted principal-minor signed-pseudoforest sums, and the complete
  characteristic-polynomial expansion.  Directed, switching and normalized
  models are excluded rather than silently generalized.
- **Gauss/Farey transfer systems not revived.**  Their modular/continued-
  fraction neighborhood collides too closely with the already extensive
  C17--C18 source and obstruction lane.  A second generic population ODE and a
  second spectral finite chain were also screened out to preserve subtype
  diversity and theorem size.

No retained system intrinsically labels primitive trajectories by rational
primes, realizes prime powers as their repetitions, or supplies a logarithmic
prime clock.  Exact spectral and determinant formulas stay source-local; no
arithmetic semantics are manufactured.

## Frozen independent theorem increments

### C199 -- signed-offset Chaplygin sleigh scattering

For every `m,J>0` and signed offset `a`, close the complete reduced and
reconstructed dynamics.  For `a!=0`, every nonstraight positive-energy branch
is one of two explicit heteroclinics, with exact energy-independent blade-angle
shift and two asymptotic contact-point lines.  The theorem also identifies the
correct attracting half-axis, half-plane Poisson form, singular invariant
density, obstruction to a smooth positive reduced or
configuration-Haar-factor density across the reduced equilibrium line,
reversor, and every straight/static boundary.  At `a=0`, constant velocities
yield the separate closed-circle or straight-line reconstruction.

### C200 -- canonical Jacobi diffusion spectral atlas

For every `alpha,beta>0`, freeze the conservative no-flux realization of the
Jacobi--Wright--Fisher SDE.  Classify both endpoints including equality at one,
prove Beta invariance and reversibility, diagonalize the generator in the
complete shifted-Jacobi basis, and close the sharp gap, heat kernel,
trace-class semigroup determinant, polynomial moment triangularization and
stationary moments.  Positive recurrence of paths is retained; only periodic
semigroup observables are ruled out.

### C201 -- all-real-parameter Polyak heavy-ball dynamics

For every SPD spectral interval `[m,L]`, classify constant-parameter heavy-ball
for all real step and momentum parameters.  The exact Jury triangle includes
negative momentum, endpoint modes determine the robust root radius, and the
unique all-real minimax parameters give Polyak's factor.  The theorem keeps the
defective endpoint blocks and their `k q^k` transients, the `m=L` nilpotent
boundary, complete characteristic data, conformal symplecticity, unit-circle
finite-order controls, and instability boundaries.

### C202 -- all-speed Fisher--KPP traveling-wave atlas

For every `D,r>0` and every real speed `c`, classify the traveling-wave phase
plane.  Positive monotone `1 -> 0` fronts exist exactly for
`c>=2 sqrt(D r)`, with reflected fronts for the negative-speed range.  The
subcritical focus forces sign-changing tails, the critical wave has its
polynomially corrected leading edge, the zero-speed Hamiltonian plane has
periodic ovals but no physical heteroclinic, and nonzero speed has strict
energy dissipation or antidissipation.  The Ablowitz--Zeppetella profile is an
exact nontrivial control inside the general theorem.

### C203 -- signed-Laplacian balance, consensus and forests

For every finite static undirected simple signed graph with positive edge
weights, including disconnected graphs and isolates, identify one kernel
direction per balanced component and none per unbalanced component.  Close the
orthogonal signed-consensus/zero limit and its exact operator-norm rate.  A
single Cauchy--Binet theorem then gives every principal minor as a rooted-tree
plus negative-unicycle pseudoforest sum and gives the full characteristic
polynomial, including the mandatory powers of four.

## Frozen strict expectations

| paper | A0 | A1 | A2 | A3 | A4 | overall |
|---|---|---|---|---|---|---|
| C199 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C200 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C201 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C202 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FAIL` | `ROUTE_A_REJECTED` |
| C203 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |

The formal A4 hints are candidate-local: a half-plane Poisson form, a
self-adjoint diffusion generator, a conformally symplectic recurrence, and a
self-adjoint signed Laplacian do not combine and do not preserve one common
physical clock.  Every Route-B flag remains false.
