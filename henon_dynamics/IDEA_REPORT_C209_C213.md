# Route-A idea report: C209--C213

Date: 2026-08-28

Source commit: `e8054522273dbd545f9d406978e5d4648c627918`.

Evaluator: `flow_systems/skills/route-a-evaluator.md`, v0.2.0, SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.

Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Design objective

This round again treats one paper as one theorem-scale advance.  Its five
owners are a Catalan combinatorial permutation, an infinite-dimensional delay
semigroup, a positive-quadrant Hamiltonian flow, a hybrid impact/reset flow,
and a persistent-velocity Markov process.  They have different state spaces,
clocks and source operators; no Route coordinate is transferred between them.

`NEW` below means only that the frozen owner is absent from the existing
workspace packages.  It is not a priority or literature-novelty claim.  The
papers retain classical ownership, state their convention locks, and add
complete boundary atlases plus independently replayable theorem evidence.

## Collision scan, kills and pivots

- A finite-alphabet continued-fraction transfer determinant was rejected even
  though it offered the strongest preliminary arithmetic signal.  The full
  workspace already contains a Gauss--Mayer package and a quadratic
  inverse-branch Ruelle package; a bounded-digit version would have been a
  smaller change of owner rather than the requested large step.
- A Jacobi--Perron/Brun replacement was also rejected.  A several-variable
  nuclearity and trace theorem could not be closed within the short-paper
  evidence contract without importing a major unresolved analytic obligation.
- Open Toda remains rejected because its Lax/scattering architecture is too
  close to C196.  Duffing and KdV remain too close to recent elliptic
  action/travelling-wave atlases.
- Ordinary Kreweras complementation is retained, rather than an
  `m`-divisible generalization, because its complete all-`n` fixed ledger can
  be locked by a Type-A cyclic-sieving theorem and checked by direct
  noncrossing-partition enumeration.  It shares a cyclic-sieving tool with
  C187, but its state set, generator, rank-duality law and orbit census are
  different; it is not a tableau parameter slice.
- The delay equation keeps the retarded phase space and method-of-steps clock.
  It is not the discrete third-order memory recurrence of C113.
- The telegraph process keeps a two-velocity piecewise-deterministic Markov
  owner.  It is neither the finite Kac-ring permutation nor the Couette PDE or
  branching process.

## Frozen independent theorem increments

### C209 -- complete Kreweras-complement cycle atlas

For every `n`, freeze ordinary noncrossing set partitions of the cyclically
ordered set `[n]` and the classical Kreweras complement `K`.  Prove
`K^2=rotation`, rank duality and the exact order boundary.  Close the fixed
count of every iterate: Catalan at the identity, central binomial counts for
nontrivial even powers, the unique odd-power half-turn family when `n` is
odd, and zero otherwise.  Möbius inversion then gives every least period and
cycle, the finite Artin--Mazur zeta, and the full finite Koopman
characteristic polynomial and root-of-unity spectrum, including all small-`n`
degeneracies.

### C210 -- scalar retarded-delay spectrum and stability atlas

For `x'(t)=-a x(t)-b x(t-tau)` with `a,b,tau>=0`, freeze the retarded phase
space and characteristic function.  Derive the exact method-of-steps
fundamental solution, the full Lambert-`W` spectral ledger for positive delay,
eventual compactness and spectral mapping, the complete repeated-root locus,
and the sharp stability/Hopf boundary.  The zero-delay, no-feedback,
equal-rate and zero-generator cases are separate theorem branches.

### C211 -- Hamiltonian Lotka--Volterra period atlas

For every positive predator--prey parameter quadruple, pass to logarithmic
coordinates and close the strictly convex Hamiltonian first integral.  Prove
that every non-equilibrium positive level is one periodic orbit, give exact
turning points and a convergent period/action quadrature, recover the small
oscillation period and exact cycle averages, and classify equilibria, axes
and escape boundaries.  No unproved global period-monotonicity or large-energy
asymptotic is promoted into the theorem.

### C212 -- affine-impact bouncing-ball atlas

For gravity `g>0`, restitution `0<=r<=1` and post-impact kick `J>=0`, reduce
the hybrid flight/reset flow to its exact affine impact map.  Close every
iterate, cumulative physical event time, finite-time Zeno collapse,
kick-supported periodic flight, stability multiplier and a separately labelled
formal event-map series (never a physical-flow zeta).
The elastic continuum, accelerated `r=1,J>0` branch, zero-kick boundary and
zero-duration impact fixed point remain distinct from positive-duration
physical periodic motion.

### C213 -- circle telegraph Fourier and hypocoercive atlas

For speed `c>=0` and flip rate `lambda>=0`, diagonalize the telegraph process
on the circle into exact `2 x 2` Fourier blocks.  Close the matrix semigroup,
complete spectrum, critical Jordan blocks, stationary states and sharp
spectral gap, together with ballistic, velocity-only and zero-generator
boundaries.  The high-frequency blocks determine the positive essential norm,
so every positive-time semigroup is noncompact and belongs to no finite
Schatten class in the nondegenerate process.

## Frozen strict expectations

| paper | A0 | A1 | A2 | A3 | A4 | overall |
|---|---|---|---|---|---|---|
| C209 | `A0_FAIL` | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_NATURAL_QUANTIZATION` | `ROUTE_A_REJECTED` |
| C210 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FAIL` | `ROUTE_A_REJECTED` |
| C211 | `A0_FAIL` | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C212 | `A0_FAIL` | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C213 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |

These are pre-release expectations, not verdict transfers.  Final tuples are
governed by each content-addressed evaluator record after theorem and scope
audit.  Every `route_b_invocation_allowed` value remains false.
