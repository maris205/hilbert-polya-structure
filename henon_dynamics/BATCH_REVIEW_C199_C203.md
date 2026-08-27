# Batch review: HCS-C199--HCS-C203

Date: 2026-08-27

Source commit: `d1e58971e570b855488009af384995702ddb887b`.

Evaluator authority: `flow_systems/skills/route-a-evaluator.md` version 0.2.0,
SHA-256 `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.

Common scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.

Recommendation: **retain all five independent theorem packages as substantial
dynamical progress; keep C199--C203 rejected by Route A and leave Route B
unauthorized.**  Four packages expose only candidate-local formal
operator/Poisson hints, while C202 has no A4 signal.  None supplies the missing
rational-prime primitive owner, logarithmic clock, target divisor, or analytic
bridge.

## Completed paper outputs

### C199 -- signed-offset Chaplygin-sleigh scattering

For every nonzero signed center-of-mass offset and positive reduced energy,
C199 closes both heteroclinic branches of the Chaplygin sleigh, their stable
half-axis, the energy-independent blade-angle shift, and the complete `SE(2)`
reconstruction with asymptotic contact-point lines.  The theorem also gives
the reduced half-plane Poisson form, its off-equilibrium invariant measure,
the reversor, and the separate zero-offset periodic/straight boundary.  The
pointwise obstruction to a positive smooth invariant density is stated only
for reduced densities and full-flow densities with a configuration-Haar
factor; it does not exclude an arbitrary configuration-dependent full-flow
density.  Nonzero-offset nonstraight orbits scatter rather than form a
primitive periodic ledger.

### C200 -- canonical Jacobi--Wright--Fisher diffusion atlas

For every positive mutation pair in the frozen conservative/no-flux
realization, C200 classifies both endpoints, including the equality cases
`alpha=1` and `beta=1` on the entrance side.  It proves Beta reversibility,
the complete shifted-Jacobi eigenbasis, the exact gap, heat kernel and
source-local semigroup determinant, together with the triangular flow of all
polynomial moments and the stationary moment formula.  The canonical clock is
kept distinct from the common half-speed Wright--Fisher convention.  Positive
recurrence of sample paths is not confused with periodic observables:
`P_T f=f` has only constants in the declared `L2` space.

### C201 -- all-real Polyak heavy-ball stability and minimax theorem

For every SPD spectral interval and every real constant parameter pair, C201
closes the strict Jury triangle, including negative momentum, and proves that
the worst-case root radius is attained at the spectral endpoints.  The unique
real minimax parameters are the classical Polyak pair.  The optimum has
defective endpoint blocks and generic `O(k q^k)` transients, so the paper does
not claim a uniform `C q^k` bound.  The one-eigenvalue boundary is handled as a
nilpotent case, while conformal symplecticity, the genuinely symplectic
boundary, finite-order controls and instability boundaries are kept distinct.
The theorem is scoped to SPD quadratics rather than arbitrary nonlinear
strongly convex objectives.

### C202 -- every-speed Fisher--KPP traveling-wave phase atlas

C202 classifies the traveling-wave reduction at every real speed.  It proves
the minimal-speed threshold for a monotone physical front, the node/focus and
sign-changing regimes, critical and supercritical leading-edge tails, and the
strict integrated energy law for nonzero speed.  The zero-speed Hamiltonian
center and its periodic ovals are retained as a separate nonphysical boundary,
and the Ablowitz--Zeppetella profile supplies an exact normalization control.
The trapping argument includes the full boundary of its invariant triangle;
finite residual cases remain regression checks rather than a substitute for
the continuum proof.

### C203 -- signed-Laplacian balance, consensus and pseudoforests

For every finite disconnected static undirected signed graph with positive
edge weights, C203 proves the componentwise structural-balance kernel, the
exact signed-consensus/zero semigroup projection, and the sharp spectral rate.
It then closes every principal minor and the full characteristic polynomial by
pseudoforests whose components are either one-root trees or root-free negative
unicycles, with the exact factor `4^u`.  The theorem includes isolated
vertices, unbalanced components and the `L=0` rate boundary.  Directed or
switching networks are expressly excluded.  The characteristic polynomial is
a finite graph-combinatorial object, not a target dynamical zeta or divisor.

## Strict Route-A record

| paper | A0 | A1 | A2 | A3 | A4 | overall |
|---|---|---|---|---|---|---|
| C199 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C200 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C201 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C202 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FAIL` | `ROUTE_A_REJECTED` |
| C203 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |

Every `route_b_invocation_allowed` value is false.  The four A4 hints belong
to different source systems and clocks and are not combined into a synthetic
pass.

## Uniform executable and release audit

| paper | checker assertions | SymPy checks | hostile rejections | evidence bytes | payload closure | PDF pages |
|---|---:|---:|---:|---:|---:|---:|
| C199 | 737 | 61 | 13/13 | 48,339 | 27/27 | 3 |
| C200 | 1,819 | 171 | 16/16 | 32,604 | 27/27 | 3 |
| C201 | 478 | 156 | 19/19 | 20,276 | 27/27 | 3 |
| C202 | 2,579 | 1,511 | 102/102 | 110,686 | 27/27 | 3 |
| C203 | 46,766 | 1,530 | 13/13 | 2,054,275 | 27/27 | 3 |
| **total** | **52,379** | **3,429** | **163/163** | **2,266,180** | **135/135** | **15** |

The hostile total comprises 158 repaired-hash semantic/schema attacks and five
stale-hash attacks.  All five checkers are producer-independent, every
symbolic program reconstructs headline identities separately, and every
canonical evidence file replays byte for byte.

Finite coverage remains a convention and regression oracle.  C200 contains
nine rational parameter pairs and 1,206 exact scalar identities; C201 contains
14 parameter cases, 28 endpoint blocks and 238 certificate scalars; C203
exhausts 760 signed graph instances, 11,894 root sets and 760 complete
characteristic polynomials.  These finite ledgers are not used to discharge
the all-parameter theorems.

Each package contains exactly 27 content-addressed payloads and one
self-excluded manifest, hence the round has 135 payloads, five manifests and
140 physical files.  The three revision PDFs in every package have pairwise
distinct hashes and `main.pdf == main_round2.pdf`.  Two fresh fixed-epoch
LuaLaTeX builds reproduce every final PDF byte for byte.  All fonts are
embedded and subsetted; logs contain no warning, bad box, undefined reference
or missing glyph; extracted text retains the tuple, scope literal and AI-use
disclosure.  All 15 final pages were inspected visually.

## Content-addressed release ledger

| paper | semantic payload SHA-256 | evidence SHA-256 | PDF SHA-256 | manifest SHA-256 |
|---|---|---|---|---|
| C199 | `e70d22dc62564e940e3474b888d7914d3e65198e67a9a071d0708599bd168b5b` | `53cd651ca51c424bc58d1ae113bfb0ee8ba3029edf3c5544c08ecf368c9e5c6b` | `4c17171ef2e6b48aeb2dacac7cc37c422cb92bac07d645698e8d28c63198575b` | `d97f9641177ef3e32677401d484b63e0fd7c09b3c2e12a21e90064207eebc38b` |
| C200 | `c4dc107c6821a56768214ce14389efcfd585d55497631bab495e42e2961af7fb` | `0b4eba23909d81058e3257e31189fee3b101ba331c2e5dd44bff70d7ad1a4ab7` | `806a4b8f8031c4c0ad086f75f45d8b79036cf46e187720bcec4af3a15e5a340e` | `af81a85f6ff7da50644797a9e3d8df197d681b6d891293c0983c1bfde0cff608` |
| C201 | `ebdf541d38face76f3329be80ef61f66271cf004d91834a14dc3465b8455bccc` | `67624d94c9ecbf87ccb5fc1d2d9c427756bd382ccdd72c6ba35f65e9601c3cf9` | `25f512bc365cd52f75f486031bad85e45af7ee4c4fc947d01fcec9c613bc4b21` | `72caf0968651127f9e405944cd4228235e7138e8aa4cfc73c327d726ce6a1d87` |
| C202 | `f02781c209fe741b81985cde6999aa0b1af727793461b4ee0082693226218b5e` | `605176e6653d796b6f86b1df8493a64d07ef8bca0fa308b256bf970d27110243` | `674a6e9d137f4593caee9ad77cf8c7de407896eabf1c08adec396b6d64a1d711` | `162da0a6d61e3cca581798bddb728d4a881553f419d6115bbb61dbf0a04f7405` |
| C203 | `5bdb95ff9e7b1e1cb590cc53b362f36a8d7505a1e43a1e1444aa9558de23391b` | `fed6574189a1630fa2c5d9ec31dd10378afa1ad3b3f883fe3b3d598543cc6e47` | `395643b221b94c5af0345243e93ad18b30d69872acadd81d3830371be4ab9689` | `41900b39ff7241b2c8829a6d3217ae1b48039cb81e3f5ae5e3d58ae6d2700aea` |

## Internal cross-review and repair ledger

These are artifact-bound theorem, scope and release audits.  They are not
external peer review, independent error processes, or novelty certificates.

- **C199:** review corrected an overbroad invariant-density argument.  The
  equilibrium line is reduced, not a full-flow equilibrium set; the final
  theorem therefore scopes the pointwise obstruction to reduced and
  configuration-Haar-factor densities while retaining the correct off-line
  Haar lift.  The abstract was also narrowed explicitly to reduced
  heteroclinics.  A dedicated hostile mutation now attacks this distinction.
- **C200:** review separated positive recurrence of diffusion paths from the
  spectral assertion that periodic semigroup observables are constant, fixed
  the equality endpoint classification, and retained the factor-two clock
  convention.
- **C201:** review kept the exact Jury region for negative momentum, separated
  root radius from defective Jordan transients, and added the one-eigenvalue
  nilpotent boundary instead of dividing by a zero minimax factor.
- **C202:** review corrected the historical KPP translation locator and
  repaired the invariant-triangle boundary, energy wording, tail coefficients
  and critical second-derivative identity.  Evidence and all PDFs were rebuilt
  after the corrections.
- **C203:** independent matrix and combinatorial reconstruction retained
  root-free negative unicycles and their `4^u` weight, caught the necessity of
  the static-undirected frame, stated orientation change correctly as being at
  most a column sign, and added negative-triangle, zero-rate and
  directed-exclusion sentinels.

Generated build and interpreter sidecars were kept outside the released
payloads before manifest closure.  No release payload or user-authored source
was deleted.

## ARS integrity and post-manuscript audit

1. **Implementation bug passing self-review: CLEAR.**  Five independent
   checkers, five symbolic reconstructions, byte replay, hostile mutations and
   fresh deterministic builds agree after all recorded repairs.
2. **Hallucinated citation: CLEAR.**  Classical ownership and source locators
   are retained; no priority or novelty certificate is asserted.
3. **Hallucinated result: CLEAR AT PROOF LAYER.**  Every infinite quantifier is
   supported by a written proof or a delimited classical theorem plus proved
   consequences.  Finite ledgers remain regression evidence.
4. **Shortcut reliance: CLEAR.**  Sample parameters, wave speeds, companion
   blocks and small graphs are never promoted to proofs of complete families.
5. **Bug reframed as insight: CLEAR.**  Density scope, recurrence category,
   Jordan behavior, phase-plane boundaries and graph frame defects were
   repaired and re-audited rather than retained as discoveries.
6. **Methodology fabrication: CLEAR.**  Producer, checker, symbolic, replay,
   mutation, PDF and manifest paths are executable and content-addressed.
7. **Frame lock: CLEAR.**  The clocks remain nonholonomic physical time,
   diffusion time, optimizer iteration, traveling-wave coordinate and network
   semigroup time.  No coordinate borrows another candidate's A4 hint.

The final PDFs and evaluator records were re-audited after every repair.  No
target zero or prime table, arithmetic local datum, Euler factor, root number,
automorphy object, target divisor/counting law/functional equation,
Hilbert--Pólya operator, or Route-B input appears as an affirmative claim.

## Batch conclusion

This round takes five separate large steps: a complete nonholonomic scattering
atlas, a boundary-complete reversible diffusion spectrum, an all-real
optimization stability/minimax theorem, an all-speed reaction--diffusion wave
atlas, and a full signed-network principal-minor/characteristic-polynomial
formula.  It does not divide one theorem among five manuscripts.

The roadmap conclusion is still negative and explicit.  None of these owners
supplies A0--A3, and their formal A4 structures cannot be transferred or
combined.  All five papers are retained as complete dynamical progress while
all five remain `ROUTE_A_REJECTED`, scope-locked, and Route B false.
