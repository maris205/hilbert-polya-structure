# Batch review: HCS-C204--HCS-C208

Date: 2026-08-27

Source commit: `d108ef46fea7a8f62490a69071a83fcbda7c113b`.

Evaluator authority: `flow_systems/skills/route-a-evaluator.md` version 0.2.0,
SHA-256 `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.

Common scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.

Recommendation: **retain all five independent theorem packages as substantial
dynamical progress; keep C204--C208 rejected by Route A and leave Route B
unauthorized.**  C204 and C205 own exact source primitive ledgers, while C206
has a candidate-local inviscid operator boundary.  None supplies the missing
rational-prime primitive owner, logarithmic clock, target divisor, or analytic
bridge.

## Completed paper outputs

### C204 -- rational-canonical dynamics of every finite linear map

For every matrix over every finite field, C204 proves the invariant-factor
formula for every iterate fixed count and separates the nilpotent primary part
from the invertible periodic subspace.  It closes the maximal transient height,
all exact periods and cycle counts, the complete finite Artin--Mazur zeta, and
the characteristic polynomial of composition on the full function space.  The
proof retains inseparable factors of `X^n-1`, nonsemisimple and singular maps,
and a genuine `GF(4)` control rather than using arithmetic modulo four.

### C205 -- algebraic zeta and primitive growth of the Dyck shift

C205 freezes the edge-type one-vertex `N`-loop Dyck convention and derives its
context-free circular-code equation and exact algebraic zeta.  It closes every
fixed and primitive count, topological entropy, the `N>1` dominant double pole
and primitive-cycle asymptotic, and both algebraic branch points.  The `N=1`
case is proved to collapse exactly to the full two-shift, where the pole order
and asymptotic coefficient change.  Finite words are not confused with cyclic
words whose bi-infinite repetition is admissible.

### C206 -- exact Couette mixing and enhanced dissipation

C206 derives the complete Fourier-sector propagator for Couette
advection--diffusion on `T x R`, including the transported frequency and the
exact integrated exponent.  Square completion gives the exact sector norm
with cubic term `a^2 k^2 t^3/12`, hence the enhanced `nu^(-1/3)` time scale.
The theorem also closes semigroup composition, inviscid mixing, every zero
parameter/mode/time boundary, the periodic-state classification, and the
noncompact-channel trace-class obstruction.  It does not import nonlinear
Couette stability conclusions.

### C207 -- full-exponent one-dimensional Barenblatt atlas

For every `m>0` and positive mass, C207 classifies centered nonnegative
first-kind zero-flux integrable similarity profiles: compact support for
`m>1`, the Gaussian at `m=1`, and algebraic tails for `0<m<1`.  It gives exact
Beta-function mass constants and every finite absolute moment, proves the
sharp fast-diffusion threshold `r<(1+m)/(1-m)` and the logarithmically divergent
second-moment boundary at `m=1/3`, and retains pressure/free-boundary geometry
and logarithmically rescaled stationarity.  The uniqueness statement is not
expanded to arbitrary Cauchy solutions.

### C208 -- complete linear birth--death branching process

C208 closes the probability-generating-function semigroup for every
nonnegative birth/death pair and every initial population.  The one-ancestor
law is zero-modified geometric, whereas the multi-ancestor transition law
retains the necessary survivor-binomial layer and conditional
negative-binomial convolution.  Exact moments and the subcritical
quasi-stationary geometric law, critical Yaglom exponential scaling, and
supercritical martingale-limit atom/gamma mixture are proved together with
critical, pure-birth, pure-death, zero-rate, zero-population and zero-time
boundaries.

## Strict Route-A record

| paper | A0 | A1 | A2 | A3 | A4 | overall |
|---|---|---|---|---|---|---|
| C204 | `A0_FAIL` | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C205 | `A0_FAIL` | `A1_WEAK` | `A2_FAIL` | `A3_FAIL` | `A4_FAIL` | `ROUTE_A_REJECTED` |
| C206 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FORMAL_HINT` | `ROUTE_A_REJECTED` |
| C207 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FAIL` | `ROUTE_A_REJECTED` |
| C208 | `A0_FAIL` | `A1_FAIL` | `A2_FAIL` | `A3_FAIL` | `A4_FAIL` | `ROUTE_A_REJECTED` |

Every `route_b_invocation_allowed` value is false.  Source finite-field
cycles, context-free bracket cycles and inviscid Fourier dynamics belong to
different phase spaces and clocks and are not combined into a synthetic pass.

## Uniform executable and release audit

| paper | checker exact cells/assertions | SymPy checks | hostile rejections | evidence bytes | payload closure | PDF pages |
|---|---:|---:|---:|---:|---:|---:|
| C204 | 144 | 204 | 18/18 | 29,867 | 27/27 | 2 |
| C205 | 177 | 78 | 19/19 | 19,124 | 27/27 | 3 |
| C206 | 9,646 | 2,713 | 18/18 | 393,278 | 27/27 | 3 |
| C207 | 3,462 | 56 | 34/34 | 75,262 | 27/27 | 3 |
| C208 | 2,194 | 1,009 | 23/23 | 76,842 | 27/27 | 4 |
| **total** | **15,623** | **4,060** | **112/112** | **594,373** | **135/135** | **15** |

The hostile total comprises repaired-hash semantic/schema attacks and one
stale-hash attack per package.  Every checker is producer-independent, every
symbolic program reconstructs headline identities separately, and every
canonical evidence file replays byte for byte.

For C204 the checker count records the 144 invariant-factor cells, with the
genuine-`GF(4)` and transient-tree controls reported separately; its SymPy
total is 198 polynomial-gcd cells plus six full-function Koopman
characteristic polynomials.  For C205 the checker total is 144 formal-series
cells plus 33 direct cyclic-word cells, and the SymPy total is 72 zeta-series
coefficients plus six entropy/dominant-radius identities.

Finite coverage remains a convention and regression oracle.  The universal
finite-field, all-`N`, all-real-parameter, all-`m>0`, and all-rate quantifiers
are discharged by written derivations or explicitly delimited source theorems,
not by the finite evidence ledgers.

Each package contains exactly 27 content-addressed payloads and one
self-excluded manifest, hence the round has 135 payloads, five manifests and
140 physical files.  The three revision PDFs in every package have pairwise
distinct hashes and `main.pdf == main_round2.pdf`.  Two fresh fixed-epoch
LuaLaTeX builds reproduce every final PDF byte for byte.  All fonts are
embedded and subsetted; logs contain no warning, bad box, undefined reference
or missing glyph; extracted text retains the tuple, scope literal and AI-use
disclosure.  Every final page was inspected visually.

## Content-addressed release ledger

| paper | semantic payload SHA-256 | evidence SHA-256 | PDF SHA-256 | manifest SHA-256 |
|---|---|---|---|---|
| C204 | `aa44c1ec0e97dfd2ddb2554e9550f65a536eaf455e5bd3a0998d91d8aa3c1a6f` | `b001387457de3bd332df5525739eeffdef9a254f39a2a3f99e26dc93bd074959` | `336d039d320202a36f7c3c64af1c6bc7a058431575b8ce4e78336d2e5016a38a` | `17b3354ae04a4f9230fc3e58463d2edf8510a987a1f5df0ab3af8e1faa42d954` |
| C205 | `a69388009e466b46ed68e6c034a4df089c916d8164b5e4b998518e80fd5795c3` | `dc14afafa3dbf22c820c81ff0fb4a851eb576c71098025153c2087f05241b10e` | `203531a0984884266508021d163ed6a5d03b651919698f34b140495b939c4986` | `20e960e1d63cfa55b553a0a01e22ae1ad0844774594ca83da3c70493a82e27d7` |
| C206 | `350708b57d73ceea8e9c979b3d8d259949bc46fdeb38b71e65d76827103eb362` | `cf21be47c3222110bb8176004a02b347add192b467cc2f91c9d0f093fe43da5e` | `724e467a74a3e9f789feaf91c419263a5fce3bcfbe5a67dae74c54e291e22d8b` | `2f9c8c59e45b5a52665fff69a71415e39b6e578f1006ef67fd8656fb16ce54bf` |
| C207 | `3e10d74bd66d2e978cdbf9f6b27530b3367ceed7302b79b43f093fac6e4d58c0` | `aeb3b26292ffb91a4294c298d33d5d66af3a8bc122fa733fec3568dde42b69ad` | `e8270094821947d0c99bc2f59e011e73acfffb5a1f3bd495f5317ac18da863ea` | `e520499a8c07dcf9aed7e0734c918f4ef6f5e3d56d9bd02de6f48dca18f2a4f5` |
| C208 | `2be1666222c3cb7dbc407d571f0bc9c3d695b19b54067b105f15a9c02c5b3cf5` | `d94b84c4d64799ea2dc9728fc96b8d8eb0f4976fd7d006af7441dd4b00565818` | `b69dddd4ca490c5df40f294705807486c21a47257695348a9dc4b3a7d1815325` | `b8eecd143478a5d4803e2cc4ca7237dfc7d6557b268f8978dfc0fb77c376fe3e` |

## Internal cross-review and repair ledger

These are artifact-bound theorem, scope and release audits.  They are not
external peer review, independent error processes, novelty certificates, or
acceptance scores.

- **C204:** the invariant-factor, nilpotent/invertible and full-function
  Koopman formulas were cross-read against the exact controls.  The Route
  record was normalized to the exact evaluator token and explicit false
  Route-B flag; a forced page break that orphaned the declarations was removed
  before the final two-page build.
- **C205:** the circular-code equation was restored as the explicit first step
  of the zeta derivation, the two-period sufficiency lemma was written out, and
  the entropy claim was tied to Krieger--Matsumoto Proposition 3.1.  The source
  title and official Muenster pagination 171--184 were corrected and the
  metadata conflict was recorded rather than silently merged.
- **C206:** the exact sector norm was separated from norm attainment.  For
  positive `nu t` the maximizing frequency is a null singleton, so no nonzero
  `L2` vector attains the norm; localized packets approach it.  The unitary
  `nu t=0` boundary, evidence and hostile tests were revised together.  A
  later precision audit separated 100 working decimal digits from the 82
  significant digits actually serialized in 1,350 fields and locked that
  distinction in both executable paths.
- **C207:** the profile class was made rigorous with `F^m` locally absolutely
  continuous, the integrated law almost everywhere, and uniqueness up to
  almost-everywhere equality; the positivity-component/zero-set argument was
  added.  The Gaussian moment, exact two-sided Darcy law and both branches of
  the free energy were made explicit, including the prohibition on an
  undefined infinity-minus-infinity cancellation and the `m<=1/3` stop.  The
  checker now freezes every theorem,
  grid, Beta constant, chemical-potential/null rule, nonclaim and Route field;
  33 repaired-hash attacks plus one stale-hash attack exercise that closure.
- **C208:** a malformed `\qquad` token was repaired, and the subcritical
  geometric quasi-stationary law gained its conditional-semigroup invariance
  identity and the `lambda=0` point-mass boundary.  Evidence, symbolic checks
  and hostile mutations were rerun after the repair.

Generated build and interpreter sidecars remain outside the released payloads
before manifest closure.  No release payload or user-authored source is
deleted.

## ARS integrity and post-manuscript audit

1. **Implementation bug passing self-review: PASS.**  Producer, independent
   checker, symbolic reconstruction, byte replay, hostile mutations and two
   fresh deterministic PDF builds agree after the last repair in every package.
2. **Hallucinated citation: PASS.**  Classical ownership and primary source
   locators are explicit; the C205 pagination conflict is disclosed, and no
   priority or global novelty certificate is asserted.
3. **Hallucinated result: PASS.**  Every infinite quantifier is supported by a
   written proof or a delimited classical theorem plus proved consequences;
   finite ledgers are described only as convention and regression evidence.
4. **Shortcut reliance: PASS.**  Small fields, finite word lengths, rational
   Fourier cells, selected exponents and selected rates are never promoted to
   proofs of the all-family statements.
5. **Bug reframed as insight: PASS.**  The layout, entropy-source,
   norm-attainment, precision-contract, profile-class, free-energy,
   moment/interface and quasi-stationary defects were repaired in the artifacts
   and every affected executable/release path was rerun.
6. **Methodology fabrication: PASS.**  Every named producer, checker, symbolic,
   replay, mutation, PDF and manifest path executed successfully and is frozen
   in the content-addressed release ledgers.
7. **Frame lock: PASS.**  The five clocks remain finite-map iteration, shift
   iteration, PDE time, diffusion time and branching time; no package borrows
   another package's operator or primitive ledger.

The final PDFs and evaluator records must be re-audited after every repair.  No
target zero or prime table, arithmetic local datum, Euler factor, root number,
automorphy object, target divisor/counting law/functional equation,
Hilbert--Pólya operator, or Route-B input may appear as an affirmative claim.

## Batch conclusion

This round takes five separate large steps: a complete all-finite-linear-map
dynamics theorem, an algebraic non-sofic primitive-orbit theorem, an exact
shear-mixing/dissipation theorem, a full-exponent nonlinear similarity atlas,
and a three-regime branching-process theorem.  It does not divide one theorem
among five manuscripts.

The roadmap conclusion remains negative and explicit.  None clears A0, and
the source-local A1/operator structures cannot be transferred or combined.
All five papers are retained as complete dynamical progress while all five
remain `ROUTE_A_REJECTED`, scope-locked, and Route B false.
