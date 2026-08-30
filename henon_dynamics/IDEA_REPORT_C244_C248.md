# Route-A idea report: C244--C248

Date: 2026-08-30

Source/code baseline: `5f357e2d2b78604f6c286bfbd05da922e1d6791f`.

Evaluator: `flow_systems/skills/route-a-evaluator.md`, v0.2.0, SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.

Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Design objective

This round freezes five independent dynamical owners rather than splitting one
calculation into five manuscripts.  They are an integrable Hamiltonian system
with a focus--focus singularity, a deterministic hybrid event network, a
state-dependent stochastic jump process, an integrable billiard map, and an
aperiodic substitution system with an exact Fourier cocycle.  Each slot must
close one source-local theorem at all declared parameters and accompany it
with an independently replayable finite receipt.  `NEW` means absent from the
frozen owner list in this workspace; it is not a claim of global priority.

The A1 layer remains the first positive target whenever the owner has
intrinsic periodic objects.  C244, C245, and C247 must separate primitive
cycles or clean periodic families from repetitions and singular faces.  C246
is genuinely stochastic and C248 is shift-aperiodic, so their exact renewal
and diffraction structures are not relabelled as primitive-orbit evidence.
None of these source-local successes repairs the mandatory A0 arithmetic gate.

## Collision screening and retained owners

- **C244 versus one-degree-of-freedom elliptic atlases.**  The spherical
  pendulum is retained for its two-degree-of-freedom energy--momentum map and
  focus--focus monodromy.  This is not the Euler top, Duffing oscillator,
  ellipsoid Reeb flow, or Bose--Josephson dimer already represented in the
  workspace.
- **C245 versus circle maps and dry-friction events.**  The owner is a fully
  connected pulse-coupled integrate-and-fire network with simultaneous
  avalanche closure.  Its exact event map and monotone cluster absorption are
  distinct from contracted rotation plateaux, single-impact maps, and
  Filippov dry-friction dynamics.
- **C246 versus additive-noise and constant-rate telegraph models.**  The
  owner is the TCP/AIMD piecewise-deterministic Markov process with flow
  `Xdot=a`, state-dependent jump rate `rho*X`, and multiplicative loss
  `X -> beta*X`.  The embedded squared perpetuity and its continuous-time
  occupation law do not occur in the existing Brownian-reset, switching-
  moment, queue, or telegraph packages.
- **C247 versus square and rectangular billiards.**  The circular billiard is
  an exact rigid rotation in Birkhoff coordinates.  Its rational invariant
  circles are one-parameter clean families of regular star polygons with
  circular caustics, not lattice directions in a polygonal unfolding.
- **C248 versus Thue--Morse and finite cellular automata.**  The Rudin--Shapiro
  owner is a primitive length-two substitution and its balanced binary
  factor.  The retained result is the dyadic two-polynomial Fourier cocycle,
  exact energy identity, van Hove autocorrelation, and absolutely continuous
  diffraction.  It is not a periodic-skeleton or natural-boundary theorem.

Candidates based on beta/Parry shifts and ordinary rowmotion were rejected
during screening because those owners already occur elsewhere in the
workspace.  KdV was not retained because earlier idea reports had already
flagged its one-phase elliptic atlas as too close to recent soliton/action
packages.  These pivots are part of the design record.

## Frozen theorem increments

### C244 -- spherical-pendulum monodromy

For

`H=(p_theta^2+j^2/sin(theta)^2)/2+cos(theta)` and `u=cos(theta)`, prove the
reduced cubic identity

`udot^2=2(1-u^2)(h-u)-j^2`.

Close the critical-value curve, the bottom elliptic and top focus--focus
singularities, the declared regular root-chamber conditions with an
eight-row representative receipt, the period/azimuth/action quadratures, and
the oriented monodromy matrix `[[1,1],[0,1]]`.  Pole charts,
double roots and the `j=0` faces remain explicit rather than being inferred
from a singular coordinate formula.

### C245 -- pulse-coupled integrate-and-fire synchronization

For a strictly concave rise function

`U_a(phi)=(1-exp(-a*phi))/(1-exp(-a))`,

derive the exact event map, threshold convention and simultaneous avalanche
closure.  Prove that firing can merge but never split clusters, retain the
synchronous primitive event cycle, and separate the all-`N` almost-everywhere
synchronization theorem from a finite exact receipt for `N<=8`.  Tie
hypersurfaces, zero coupling and loss of strict concavity are separate faces;
the receipt is not advertised as an exhaustive continuum cell decomposition.

### C246 -- TCP/AIMD squared perpetuity and occupation law

For `Xdot=a`, jump intensity `rho*X`, and `X -> beta*X`, let `Y_n` be the
pre-jump level.  Prove the exact embedded recursion

`Y_(n+1)^2=beta^2*Y_n^2+2*a*E_(n+1)/rho`, `E_n ~ Exp(1)`,

and the unique stationary squared-perpetuity transform

`prod_(k>=0) (1+2*a*beta^(2k)*s/rho)^(-1)`.

Close its convergence and uniqueness, the continuous-time generator identity,
all moment recurrences, the stationary jump-cycle occupation formula, and the
`beta=0,1`, `a=0`, and `rho=0` boundaries.  The factor `a` is mandatory; a
scale-free recurrence is a failed certificate.

### C247 -- circular-billiard clean periodic families

Write the disk billiard map as a rigid rotation in boundary Birkhoff
coordinates.  Classify every primitive family by coprime integers `(m,n)`
with `1<=m<n/2`, prove the length

`L_(m,n)=2*n*R*sin(pi*m/n)`,

and record orientation, caustic, action and repetition.  Prove that each
rational invariant circle is a clean one-parameter fixed manifold with the
declared unipotent transverse return, so an isolated-orbit determinant is not
silently imported.  Diameters and grazing limits are separate boundaries.

### C248 -- Rudin--Shapiro Fourier cocycle and diffraction

For the primitive four-letter length-two substitution and its balanced
Rudin--Shapiro factor, prove the dyadic recursion

`P_(k+1)=P_k+z^(2^k)Q_k`,
`Q_(k+1)=P_k-z^(2^k)Q_k`,

the exact circle energy identity and square-root sup norm bound.  Derive the
paired correlation recursion in the declared van Hove convention and prove
that the binary comb has autocorrelation `delta_0` and Lebesgue diffraction.
Keep this two-point diffraction statement distinct from the full dynamical
spectrum and record the absence of nontrivial shift-periodic points.

## Frozen strict expectations

| paper | A0 | A1 | A2 | A3 | A4 | overall |
|---|---|---|---|---|---|---|
| C244 | `A0_FAIL` | `A1_PASS_ANALYTIC` | `A2_FAIL` | `A3_FAIL` | `A4_NATURAL_QUANTIZATION` | `ROUTE_A_REJECTED` |
| C245 | `A0_FAIL` | `A1_PASS_ANALYTIC` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C246 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C247 | `A0_FAIL` | `A1_PASS_ANALYTIC` | `A2_FAIL` | `A3_FAIL` | `A4_NATURAL_QUANTIZATION` | `ROUTE_A_REJECTED` |
| C248 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |

These are design expectations, not pre-awarded verdicts.  Every release tuple
must be read from the content-addressed evidence/evaluator pair after the
independent checker, symbolic reconstruction, replay and mutation suite pass.
`route_b_invocation_allowed` remains false throughout.

## Evidence and citation boundary

Publisher/DOI records are the authority for every retained reference.  The
source audit in each package must record the exact bibliographic match and the
limited claim it supports.  Classical source theorems may be reconstructed
and extended into a uniform executable atlas, but they are not presented as
new literature-priority results.  No target prime/zero table, arithmetic local
datum, Euler factor, root number, automorphy statement, target divisor or
counting law, target functional equation, Hilbert--Polya operator, or Route-B
input is permitted.

## Release outcome

All five frozen owners completed their declared theorem increment and the
independent artifact chain on 2026-08-30.  The release has 7,394 checker
assertions, 1,066 symbolic identities, 184 hostile mutations, 135 payload
files (140 physical files), and 12 final-paper pages.  The per-paper
three-round hashes and manifest ledgers are recorded in
[BATCH_REVIEW_C244_C248.md](BATCH_REVIEW_C244_C248.md).  The strict tuples are
read from the final evidence/evaluator pairs; every candidate is
ROUTE_A_REJECTED and Route B remains disabled.  The results are source-local
and do not supply target arithmetic, a target divisor, or a Hilbert--Pólya
operator.
