# Papers 24--28 — Round-4 execution report

Date: **2026-08-27**

Batch: **one round / exactly five paper projects**

ARS state: **Stage 1 RESEARCH in progress for all five**

Proposal state: **Stage 1 Classical Flow Baseline / Route A A0--A1**

## Outcome

Round 4 gives every project a distinct paper-facing advance.  It closes one
geometric-control gap, one methods-integrity gap, two owner/obstruction
theorems, and the first explicit Bolza magnetic-orbit seed ledger.  The round
does **not** assign a formal Route-A tuple, evaluate A2--A4, invoke Route B, or
authorize an ARS Stage-2 manuscript.

| Paper | Round-4 result | Evidence and exact boundary | Paper-level consequence |
|---|---|---|---|
| P24 Bianchi holonomy | Replaced the infinite-volume Schottky surrogate by the genuine finite-volume, one-cusped, non-arithmetic control `S^3 \ 5_2=m015` | Control geometry and non-arithmeticity are source-proved; the 18 complex-length groups / 31 primitive classes by multiplicity are high-precision numerical observations, with an independent 9-class / 6-group prefix cross-check | The finite-volume/cusp control-class gap is closed, but the Bianchi word ball and control metric cutoff still use incompatible enumerations, so no cross-system score is lawful yet |
| P25 three-disk scattering | Audited the only Round-3 refinement-method switch over the full 2,241-row ledger | 2,202 rows use direct Newton and 39 use the frozen stationarity fallback; all 39 were historical open rows, all pass the same final contract, and the fallback path consumes no paraxial-comparison value | The negative-control methods section can now state that the fallback-requiring rows were neither dropped nor selected after reading the comparison result; the audit remains post-hoc and does not prove statistical unbiasedness |
| P26 level-11 time change | Proved the correctly normalized Hecke correspondence relation on a finite **sum of closed cycle owners**, `integral_(T_(p,*)C) alpha_f = a_p integral_C alpha_f` | The theorem is analytic; the batch separately checks 385 branch gluings, 320 eta-coefficient identities, 138 primitive-certified finite owners, and 55 numerical period sums | A one-prime/one-primitive-orbit recurrence is ruled out as the interpretation.  Because genus-one compact cohomology makes every legitimate closed-form control obey the same scalar relation, discriminative Hecke/Euler evidence is `STOP_SCOPED` |
| P27 congruence inverse limit | Proved quotient-order and whole-`g`-loop closing-time escape for every fixed infinite-order owner in any descending normal residual tower | If `o_n=ord(g Gamma_n)`, then `o_n` divides `o_(n+1)` and boundedness would force a nonzero power of `g` into the trivial intersection; hence `o_n -> infinity`.  The 24-row factorial-tower audit is illustration, not the proof | The earlier no-periodic-point result gains a broader same-owner mechanism: finite-level closing times cannot remain bounded while being reassigned to the inverse-limit flow; primitive minimal-period credit still requires a primitive owner |
| P28 Bolza magnetic flow | Instantiated four published opposite-side-pairing primitives as the first source-locked Bolza magnetic trace-branch ledger | Four inverse-paired axis owners, signed source repetitions `k=+/-1,+/-2,+/-3`, and two field signs give 48 rows with period, signed time, action, stability, Maslov, signed-branch partner, and field partner | The frozen signed-field even-`N` subtype now has explicit primitive-axis owners and source-bound signed branches rather than only an abstract theorem; this is a seed, not a complete Bolza spectrum, and gives no credit to zero/odd/all-`N` or fixed-operator regimes |

## Detailed results

### P24 — finite-volume cusped non-arithmetic control

The frozen control is the unit-speed geodesic flow on

```text
Y = S^3 \ 5_2 = m015,
clock = hyperbolic arclength.
```

The source chain separates theorem and executable layers:

1. HIKMOT's verified-census theorem supplies the complete finite-volume
   hyperbolic structure on `m015`.
2. SnapPy 3.3.2 returns a documented rigorous positive isometry result from
   the built-in `5_2` object to `m015`.
3. A one-component knot complement has one torus cusp.
4. Reid's arithmetic-knot-complement classification makes `5_2`
   non-arithmetic because it is not the figure-eight knot.

At real-length cutoff `3.05`, the primary implementation records 18 grouped
complex lengths with multiplicity 31.  An independent 106-bit implementation
agrees on the first 9 classes in 6 groups; its maximum complex-length residual
is `2.2944137070481165e-31`.  SageMath's interval backend was unavailable, so
the decimal spectrum remains
`HIGH_PRECISION_NUMERICAL_OBSERVATION_NOT_INTERVAL_VERIFIED`.

The control now matches hyperbolic dimension, orientability, torsion-free
manifold status, finite volume, cusp presence, geodesic-flow clock, and complex
length/holonomy owner type.  It intentionally does not match arithmetic owner,
covolume, exact cusp count of the Bianchi level-`(3)` quotient, generator
marking, or enumeration rule.

### P25 — conditioning and fallback-selection integrity

The audit freezes the Round-3 ledger SHA-256
`1b932a5ca3cf7123e9428b3eb2f26078d8e289eabb11dd828379ecf39eeb414e`.
The 39 fallback rows split as follows:

```text
topological length: 11 -> 1, 12 -> 38
d/a:                 5.8 -> 4, 6.0 -> 10, 6.2 -> 25
trace conditioning:  10^9--10^12 -> 1, above 10^12 -> 38
```

All 39 were `OPEN` in the historical binary64 artifact and all pass the same
post-refinement, multiscale, determinant, parity-corrected trace, and
half-density thresholds as the 2,202 direct-Newton rows.  The maximum fallback
half-density relative residual is `1.6711766389230827e-15`.

The static dependency audit verifies that the fallback call precedes the
paraxial trace conversion/comparison assignment inside `validate_row` and that
the ten checked map/refinement functions do not consume paraxial trace,
half-density, prime data, or zero data.  The trace string is copied earlier for
output provenance, so the claim is deliberately about computational
dependency, not first textual access.  Length/geometry counts are descriptive;
no causal conditioning law is inferred.

### P26 — sum-valued Hecke owner theorem and kill

For `p` prime to 11, freeze

```text
f(z) = eta(z)^2 eta(11z)^2,
omega_f = 2 pi i f(z) dz,
alpha_f = Re(omega_f),
T_p f(z) = p f(pz) + (1/p) sum_(b=0)^(p-1) f((z+b)/p).
```

Pairing `T_p omega_f=a_p omega_f` with an oriented cycle gives the proved
relation

```text
integral_(T_(p,*) C) alpha_f = a_p integral_C alpha_f.
```

For a hyperbolic owner `M`, right multiplication permutes the `p+1` double
coset branches.  Each permutation cycle `O` owns a closed class

```text
delta_O = beta_j M^|O| beta_j^(-1) in Gamma_0(11),
sum_O I(delta_O) = a_p I(M).
```

For the 11 frozen positive-word owners and `p={2,3,5,7,13}`, all 385 exact
branch identities, 320 exact coefficient identities, and 138 finite
primitive-root checks pass.  All 55 numerical period sums pass with maximum
primary complex residual `2.229752420147902e-14`.

The key falsification result is structural.  Since `X_0(11)` has genus one and
real Hecke eigenvalues, the same scalar relation holds for every smooth closed
real 1-form extending over the compact modular curve.  The registered
same-owner control therefore passes by theorem.  A nonmodular q-series fails
302/320 coefficient rows, but it has no `Gamma_0(11)` quotient owner.  Hence
the correspondence theorem is valid while its proposed discriminative
primitive-Euler interpretation is stopped.

### P27 — quotient-order and whole-loop closing-time escape theorem

Let `Gamma_1 >= Gamma_2 >= ...` be descending normal finite-index subgroups
with trivial intersection, and let `g` have infinite order.  If

```text
o_n = order of g Gamma_n in Gamma_1/Gamma_n,
```

then `o_n | o_(n+1)`.  A bounded divisibility sequence is eventually constant,
say at `r`, which would put `g^r` in every subgroup and contradict residuality.
Thus `o_n -> infinity`.  For a hyperbolic element the corresponding lift of the
chosen `g`-loop closes after the least number `o_n` of whole traversals, so its
closing time is `o_n ell(g) -> infinity`.  This time is not called the
underlying flow orbit's minimal period unless `g` is separately proved
conjugacy-primitive.  Normality makes the quotient order
conjugacy-independent.

The theorem specializes to the already proved `Gamma(3 n!)` residual tower.
The finite audit verifies all 21 transitions in the three sequences

```text
G3-A: 1, 3, 3, 6, 6, 36, 72, 288
G3-B: 1, 1, 3, 12, 60, 360, 360, 2880
G3-C: 1, 2, 6, 12, 12, 72, 72, 576.
```

The recorded words are primitive necklaces, while their full
`Gamma(3)`-conjugacy primitivity remains open.  Period escape only needs the
recorded elements to have infinite order and certifies their whole-loop closing
times, not unproved primitive minimal periods.  The result is positioned as an
elementary owner criterion and factorial-tower case study, not a general
aperiodicity priority claim.

### P28 — first explicit Bolza magnetic-owner seed

Four published opposite-side-pairing elements of the regular Bolza octagon
have translation length equal to the Bolza systole.  Therefore none can be a
proper power.  Their abelianization vectors `+/- e_j` prove that `f_j` and
`f_j^-1` are distinct oriented `Gamma`-conjugacy classes.  Equation (19) of the
source, however, uses a signed repetition `k` relative to one selected
primitive representative.  The ledger therefore takes one inverse-paired
primitive axis owner per `j` and uses the sign of `k` for the two trace
branches, avoiding double credit.  Inside the source-compatible signed-field
even subsequence, the grid is

```text
4 inverse-paired axes x 6 signed k values x 2 field signs = 48 rows.
```

Equivalently, the ledger has 8 field-axis owner pairs, 16 `|k|=1` signed
primitive-branch rows, and 32 signed repetition-branch rows.  Its oriented
owner credit is zero: branch orientation is carried by signed `k`, not by
minting a second primitive-axis owner.

Every row records the primitive-axis owner, signed source repetition, trace and
physical periods, signed trace time, total even-`N` action/phase, Fourier
argument, Poincare multipliers and stability denominator, Maslov index,
opposite-`k` partner, and `b <-> -b` partner.  The group transcription and
relator replay at 120 decimal digits; the relator residual is about
`1.534e-117`.

The source theorem, not that decimal replay, owns the group and magnetic-orbit
claims.  Connection holonomy is not separately reverse-engineered; only the
source-compatible total even-`N` action is retained.  Zero field, odd `N`,
arbitrary twists, all-`N`, fixed `Delta^L`, a complete Bolza spectrum, and a
matched non-arithmetic genus-two control remain open.

## Route-map correspondence

The two governing files remain `skills/route-a-evaluator.md` and
`skills/route-b-evaluator.md`.

| Paper | A0 correspondence | A1 correspondence | Why the project does not advance |
|---|---|---|---|
| P24 | Arithmetic substrate remains the Bianchi group; a genuinely non-arithmetic finite-volume control now exists | A numerical control-side complex-length prefix exists | No canonical orbit/prime-ideal owner map and no same-enumeration comparison |
| P25 | Arithmetic source is absent by construction, as required for the negative calibrator | The orbit/stability ledger and method audit are complete at the frozen cutoff | The half-density statistic proves too much and is stopped; this cannot manufacture A0 |
| P26 | The level-11 newform source and time change remain intrinsic | Oriented cycle ownership and the Hecke correspondence sum are proved | The relation is non-discriminative on genus-one cohomology and is not a primitive Euler factorization; A2 is unrun |
| P27 | Congruence provenance is intrinsic but no rational-prime link is proved | Total-space aperiodicity and finite-level owner-period escape are proved locally | This is an A1 obstruction/case study, not a formal evaluator tuple or a zeta owned by limit orbits |
| P28 | The arithmetic Bolza substrate and line-bundle source are intrinsic; a prime link is unproved | Four explicit inverse-paired primitive-axis owners and their signed source-`k` trace branches are instantiated in the frozen signed-field even subtype | The seed is incomplete and does not cover zero/odd/all-`N` or the fixed operator; Route B remains unavailable |

The exact batch receipt is:

```text
ARS_STAGE_1_PROJECTS_IN_PROGRESS=5/5
PROPOSAL_STAGE=1_CLASSICAL_FLOW_BASELINE
ROUTE_A_SCOPE=A0-A1
FORMAL_ROUTE_A_TUPLES_ASSIGNED=0/5
A2_A4_EVALUATIONS_RUN=0/5
ROUTE_B_EVALUATIONS_RUN=0/5
ROUTE_B_INVOCATIONS=0/5
ROUTE_B_INVOCATION_ALLOWED=false
GATES_A_E=NOT_REACHED
ARS_STAGE_2_MANUSCRIPTS_AUTHORIZED=0/5
FORBIDDEN_TARGET_TABLES_USED=0/5
```

Assignment states such as `UNASSIGNED`, `NOT_EVALUATED`, and `NOT_RUN` are
pipeline bookkeeping, not evidence tokens.  Local labels such as
`PROVED_A1_OBSTRUCTION` do not constitute a formal Route-A verdict.

## Reproducibility receipt

| Paper | Round-4 tests | Deterministic replay | Core artifact-tree SHA-256 |
|---|---:|---|---|
| P24 | 9/9 | two independent builds byte-identical | `54dc289c26ef8466405576c29d819d2ccc0464d57c78386e1a021464d78f6875` |
| P25 | 8/8 | two independent builds byte-identical | `85566062639b3e42efb4ae47816be5a967e8948233727fc1d0ef24bdeb432265` |
| P26 | 8/8 | two independent builds byte-identical | `4cd45da8e7fa82e4688bc6975dae44c4206837b40652979167432ffe7b07f20e` |
| P27 | 8/8 | two independent builds byte-identical | `2fcf33ed6c458339ac808d7b7007a240b7a588b0093249a90a35559f1ef2aa22` |
| P28 | 12/12 | two independent builds byte-identical | `b2387be3d4acc6485cd7f0e2d89eeaae9a36dace1ddf2d451d7f51ed3680bfd4` |
| **Total** | **45/45** | **5/5 reproducible** | — |

The root agent independently reran all five Round-4 test suites and all five
reproduction scripts.  Numerical tolerances are regression contracts, not
substitutes for the separately written source/proof layers.

## Source and integrity boundary

- P24 binds the control geometry to HIKMOT, the documented SnapPy isometry
  contract, and Reid's arithmeticity theorem.  It makes no novelty claim for
  selecting `5_2`.
- P26 binds modular-symbol/Hecke ownership to the primary Manin and Merel
  literature and locks the level-11 form to the authoritative LMFDB record.
- P28 binds the group generators/systole and magnetic trace formula to the
  published Bolza and Kordyukov--Taimanov sources.  An independent owner audit
  caught and closed an initial inverse-orientation double-credit ambiguity:
  `f_j` and `f_j^-1` remain nonconjugate group-theoretic facts, while the
  equation-(19) ledger now uses one inverse-paired axis-owner ID and signed
  `k` branches.
- P25 and P27 use frozen local artifacts for the new audit/theorem; P27 keeps
  the Round-3 closest-prior narrowing in force.
- No source proves the finite decimal ledgers merely by being cited.  Their
  numerical evidence levels are stated separately.

The academic-research workflow materially constrained the round: every result
has an explicit owner, evidence label, falsification boundary, source layer,
and smallest next artifact.  Nothing was promoted because it was convenient
for a paper narrative.

## Next smallest artifacts

1. **P24:** put candidate and control under one rigorously identical
   enumeration rule, then predeclare the holonomy comparison.
2. **P25:** either freeze a new source-derived discriminative observable or
   retain the current work as the methods/negative-control paper; do not extend
   the stopped half-density statistic by cutoff alone.
3. **P26:** derive how the sum-valued correspondence enters the first variation
   of the frozen dynamical zeta without merging primitive/repeated owners, or
   prove that the genus-one cohomological identity cannot imply a primitive
   Euler factorization.
4. **P27:** test the same owner criterion on a cocompact residual tower and
   finish the human positioning check for a short methodological case study.
5. **P28:** extend the four-axis seed to a bounded-length conjugacy census with
   a certified normal form, then instantiate the area/field/degree-matched
   non-arithmetic genus-two control.

These are the five prespecified targets for the next round.  They preserve the
initial continuous-time-flow restrictions while changing the subtype-specific
owner, clock, compactness, or control mechanism.
