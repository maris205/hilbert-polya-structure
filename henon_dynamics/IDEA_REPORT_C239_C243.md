# Route-A idea report: C239--C243

Date: 2026-08-30

Source/code baseline: `489506cf92bfed721f94f22dd0444a60427f90a5`.

Evaluator: `flow_systems/skills/route-a-evaluator.md`, v0.2.0, SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.

Scope firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Design objective

This round takes one complete theorem-scale step in each paper while changing
the dynamical owner in every slot.  The five owners are a finite arithmetic
permutation, a discontinuous interval contraction, a countable-branch
expanding number map, a contact Hamiltonian flow, and a nonlinear mean-field
Hamiltonian flow on the Bloch sphere.  They are not five slices of one result.
`NEW` means absent from the frozen owner list in this workspace; it is not a
claim of global literature priority.

The A1 layer is deliberately prioritized: every retained system must have an
intrinsic and reproducible orbit, itinerary, or regular-level structure, with
primitive objects separated from repetitions and singular parameter faces.
That source-local success is never substituted for the mandatory A0
arithmetic gate or the target-matching requirements in A2--A3.

## Collision screening and pivot

- **C239 versus finite-field multipliers and necklace rotations.**  The owner
  is the all-parameter multiway perfect-shuffle permutation on `kn` positions,
  not multiplication by a primitive element on a finite field and not a fixed
  cyclic rotation.  Its orbit lengths vary over divisors of `kn+1`, and the
  theorem closes fixed counts, pointwise orders, cycle counts and the exact
  finite determinant uniformly in both parameters.
- **C240 versus circle rotations, interval exchanges and piecewise expanding
  maps.**  The owner is the contracted rotation
  `x -> {lambda*x+delta}` with `0<lambda<1`.  Carry words determine affine
  branch compositions and exact mode-locking intervals.  The discontinuity
  and half-open endpoint convention are part of the object; no conclusion is
  imported from an isometric rotation.
- **C241 versus finite-alphabet shifts and continued-fraction maps.**  The
  classical Lüroth map has a countably infinite full-branch alphabet and
  word-dependent slopes `n(n-1)`.  A digit cutoff is an explicitly typed
  finite receipt, while the theorem retains the full weighted series and its
  convergence boundary.  It is not a finite subshift relabelled as a
  countable system.
- **C242 versus Hamiltonian strobes and dissipative sphere flows.**  The owner
  is the Reeb flow on the boundary of a four-dimensional ellipsoid.  The
  irrational face has exactly two simple coordinate orbits with all iterates,
  actions, transverse rotations and Conley--Zehnder indices explicit; the
  rational face is a Morse--Bott degeneration and is kept separate.
- **C243 pivot versus the pre-existing Schottky control.**  A proposed
  pair-of-pants/Schottky geodesic package was killed before release because a
  rank-four Schottky cyclic ledger already exists elsewhere in the workspace.
  The replacement owner is the Bose--Josephson two-mode mean-field flow on the
  Bloch sphere.  It closes a pitchfork, regular energy components, separatrix,
  self-trapping barrier and elliptic period quadrature rather than repeating a
  free-group word atlas.  It is also distinct from the damped Hénon dimer of
  C118: the present object is a continuous conservative nonlinear spin flow,
  not a conformally symplectic discrete variational map.

Source-local finite zeta functions, weighted orbit series, Reeb indices,
elliptic periods and natural quantizations are not relabelled as arithmetic
local data, target divisors, Euler factors or Hilbert--Polya operators.  None
of the five systems intrinsically supplies rational-prime primitives together
with the target logarithmic clock.

## Frozen independent theorem increments

### C239 -- multiway perfect-shuffle cycle atlas

For `M=kn+1` and `rho(i)=ki mod M` on the nonzero residue representatives,
prove the all-parameter fixed-count identity
`Fix(r)=gcd(k^r-1,M)-1`.  Recover least periods and cycle counts by Moebius
inversion, prove the pointwise order formula
`ord_(M/gcd(i,M))(k)`, and close the exact finite source zeta, Koopman
characteristic polynomial and repetition ledger.  Direct modular iteration
and a literal multi-packet interleave implementation serve as independent
controls.

### C240 -- contracted-rotation mode-locking atlas

For `f(x)={lambda*x+delta}`, freeze the half-open branch convention and derive
the affine composition of every binary carry word.  Solve its unique fixed
point, intersect all stepwise branch inequalities to obtain the exact
admissible `delta` interval, separate primitive cyclic words from repeats,
and prove that every admissible itinerary has exactly one associated periodic
point.  The finite word cutoff gives an exact mode-locking census, but no
global one-cycle theorem or maximal-plateau claim is inferred from that
receipt.  Equality endpoints and inadmissible words are explicit negative
controls rather than rounded into plateau interiors.

### C241 -- Lüroth countable-branch periodic atlas

On `I_n=(1/n,1/(n-1)]`, `n>=2`, with
`L(x)=n(n-1)x-(n-1)`, prove that every finite digit word has a unique periodic
fixed point under the inverse-branch composition and multiplier
`prod n_j(n_j-1)`.  Separate primitive cyclic words and repetitions.  For
digits `2,...,M`, prove the exact weighted full-shift identity
`Z_M(z,s)=1/(1-z*A_M(s))`, where
`A_M(s)=sum_[n=2..M](n(n-1))^(-s)`, and pass to the full series on
`Re(s)>1/2`; retain the telescoping `A(1)=1` boundary.  The theorem explicitly
records that the unweighted full count is infinite in every positive period.

### C242 -- irrational-ellipsoid Reeb orbit atlas

For the standard contact form on
`partial E(a,b)`, write the exact flow
`(z_1,z_2)->(exp(2*pi*i*t/a)z_1,exp(2*pi*i*t/b)z_2)`.
When `a/b` is irrational, prove that the two coordinate circles are the only
simple closed orbits and close every iterate's period/action, transverse
multiplier and Conley--Zehnder index in the coordinate complex-line
trivialization used by Hutchings.  At rational `a/b=p/q`, record the common
mixed-orbit period and Morse--Bott continuum instead of continuing the
isolated-orbit statement through a singular boundary.

### C243 -- Bose--Josephson dimer phase portrait

For
`H(z,phi)=Lambda*z^2/2-sqrt(1-z^2)*cos(phi)` on the Bloch sphere, close the
full nonnegative-`Lambda` fixed-point and stability atlas.  Prove the
`Lambda=1` symmetry-breaking pitchfork, the exact quartic energy reduction

`zdot^2=-(Lambda^2/4)z^4+(Lambda*H-1)z^2+1-H^2`,

the turning-root and regular-level period quadratures, and their complete
elliptic-integral form where nonsingular.  For `Lambda>1`, identify the
`H=1` separatrix and its explicit homoclinic imbalance profile, and prove the
energy-component form of the macroscopic self-trapping criterion.  The pole
coordinate, `Lambda=0`, critical `Lambda=1`, and geometric `Lambda=2` faces
are audited separately.

## Frozen strict expectations

| paper | A0 | A1 | A2 | A3 | A4 | overall |
|---|---|---|---|---|---|---|
| C239 | `A0_FAIL` | `A1_PASS_ANALYTIC` | `A2_FAIL` | `A3_FAIL` | `A4_NATURAL_QUANTIZATION` | `ROUTE_A_REJECTED` |
| C240 | `A0_FAIL` | `A1_PASS_ANALYTIC` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C241 | `A0_FAIL` | `A1_PASS_ANALYTIC` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C242 | `A0_FAIL` | `A1_PASS_ANALYTIC` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C243 | `A0_FAIL` | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_NATURAL_QUANTIZATION` | `ROUTE_A_REJECTED` |

These are design expectations, not pre-awarded verdicts.  The release tuple
must be read from each content-addressed evidence/evaluator pair after
independent validation.  C241's source weighted series and domain theorem are
retained as source-local A1 structure only; they are not target A2--A3
functional-equation, divisor or counting-law evidence.
`route_b_invocation_allowed` remains false throughout.

## Release outcome

The five frozen owners all reached release: C239, C240, C241, C242, and C243
each have a complete theorem package, independent checker/SymPy/replay/
mutation evidence, three content-distinct manuscript revisions, and a closed
28-file manifest.  The uniform audit totals 30,925 checker assertions, 1,826
symbolic identities plus three independent elliptic quadratures, and 190
hostile rejections.  The strict tuples remain exactly those in the table
above; every overall verdict is `ROUTE_A_REJECTED` and Route B is false.  See
[`BATCH_REVIEW_C239_C243.md`](BATCH_REVIEW_C239_C243.md) for the immutable
hash receipt and final PDF links.
