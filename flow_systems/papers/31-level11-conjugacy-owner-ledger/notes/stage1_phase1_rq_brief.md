# P31 Stage-1 Phase-1 Research Question Brief

Date: **2026-09-01 UTC**  
Mode: **ARS Deep Research / FULL / Phase 1 only**  
Status: **REVISED PHASE-1 DESIGN — pending independent Checkpoint-1 replay**

## Topic area

Exact primitive-orbit ownership for the positive Level-11 newform time change
of the `Gamma_0(11)` geodesic flow, restricted to the frozen P26
Hecke-output population.

## Primary research question

How does a complete global oriented-owner partition of the frozen 138-instance Hecke-output population induce the frozen cell-local no-double-credit moment classification?

The question has one ordered object: first close global owner identity, then
apply the already frozen cell-local incidence operator. The global quotient and
the cell-local classification are different registered outputs; repeated
appearance of one owner across cells never creates another global owner. This
is a finite A1 ownership question, not a full primitive spectrum, Euler
product, A2 determinant, or Route-B question.

## FINER assessment

| Criterion | Score | Phase-1 justification |
|---|---:|---|
| Feasible | **4/5 — PROVISIONAL** | The population and pair universe are finite, but complete negative `Gamma_0(11)`-conjugacy certificates require a theorem-backed solver contract that is not yet bound; failure to bind it makes the endpoint `NOT_EVALUABLE`, not negative. |
| Interesting | 5/5 | P26's `2/2/134` split is instance-level; the smallest unresolved ownership issue is whether distinct output rows represent the same primitive owner. |
| Novel | **3/5 — PROVISIONAL** | No Phase-2 literature search has run. This placeholder records a testable project increment and is not a novelty or priority claim. |
| Ethical | 5/5 | The study uses theoretical mathematics and repository artifacts only; there are no human subjects, personal data, animals, or intervention. |
| Relevant | 5/5 | A complete owner quotient directly closes or fails the named Route-A A1 completeness gap while preventing finite Hecke multiplicity from being mistaken for zeta repetition. |
| **Average** | **4.4/5 — PROVISIONAL** | Feasibility and novelty remain provisional and must not be read as closure or novelty verdicts. |

## Frozen operational definitions

- **Owner:** an oriented primitive conjugacy class in
  `Gamma_0(11) <= PSL(2,Z)`, represented by a canonical positive-trace lift in
  `SL(2,Z)`.
- **Owner equivalence:** `M ~ N` only when an exact witness
  `C in Gamma_0(11)` proves `CMC^{-1}=N` in `PSL(2,Z)`. Equal trace, equal
  length, equal homology coordinate, or bounded-search failure is not proof.
- **Inversion:** `M^{-1}` is retained as the reverse-oriented owner and linked
  by an inverse-pair identifier; it is not silently collapsed with `M`.
- **Repetition:** if `M=P^r` with `r>1`, `P` owns the primitive class and `r`
  is a traversal exponent. Hecke branch-cycle degree is never identified with
  this exponent.
- **Global oriented-owner quotient `G`:** exactly one row per resolved oriented
  primitive owner ID across all 138 instances, independent of source word,
  prime, branch, cycle, or Hecke degree. Kernel class is a field of this global
  row. The inherited `2/2/134` split remains an instance-level control and is
  not a forecast of the counts in `G`.
- **Correspondence-incidence relation `I`:** one row per original instance,
  keyed by `(owner_id, source_word, prime, cycle_id, branch_set,
  hecke_degree, instance_id)`. It preserves all 138 rows and is never called a
  unique-owner quotient.
- **Cell-local quotient `C`:** for cell `c=(source_word,prime,hecke_degree)`,
  retain one row per `(c,owner_id)`. Duplicate incidences of the same owner in
  one cell have unit cell weight but remain visible in `I`.
- **Cross-cell rule:** one owner may occur in several cells or source/prime
  groups. It remains one row in `G`; it contributes one unit to each distinct
  cell in `C` because each frozen Hecke group is a separate recurrence
  estimand. These cell contributions are not pooled into a global-owner
  percentage.
- **Conflict matrix:** for group `h=(source_word,prime)` and owner `g`, record
  `D(g,h)={d: I contains (g,h,d)}`, raw counts `m(g,h,d)`, and cell indicators
  `u(g,h,d)=1[m(g,h,d)>0]`. `|D(g,h)|>1` gives
  `NOT_EVALUABLE_DEGREE_CONFLICT` for every scalar law in group `h`; no degree
  is selected and no cross-degree weight is invented.
- **Cell-local moment estimand:** with exact normalized period ratio
  `r(g,h)=k(g)/k(source_h)` and `k=2y+z`, define
  `M(h,d)=sum_g u(g,h,d) r(g,h)^2`. The normalization denominator is exactly
  `k(source_h)^2` through this ratio; there is no sample-size or owner-count
  denominator. For each frozen law `L_p in {a_p,a_p^2,a_p^2-p}`, the exact
  predicate is `M(h,1)=L_p` and `M(h,d)=0` for every represented `d>1`.
  Any inconsistent exact `r(g,h)` among duplicate incidences gives
  `NOT_EVALUABLE_OWNER_COORDINATE_CONFLICT`.
- **Two taxonomies:** the global kernel taxonomy counts rows of `G` as full
  complex-period kernel, nonzero real-projection-only kernel, or true
  real-projection nonkernel. The group-law taxonomy applies the preceding
  cell-local equations to each of the 55 groups. Neither denominator may be
  substituted for the other.

## Scope boundaries

### In scope

- The unchanged P26 time change `X_geo/rho_epsilon`, real Level-11 newform
  differential, positive-density interval, oriented owner convention, Hecke
  normalization, reciprocal log-zeta convention, and period coordinate
  `k(x,y,z)=2y+z`.
- Exactly the 138 registered correspondence-component rows and 55 frozen
  source-word/prime groups for `p in {2,3,5,7,13}`.
- Exact primitivity/root replay, full-subgroup conjugacy decisions, inversion
  pairing, the global owner quotient, the full correspondence-incidence
  relation, the frozen conflict matrix, and cell-local recomputation of the
  existing three finite scalar-law diagnostics.
- Comparison of the global-owner and cell-local results with the inherited
  instance-weighted
  `2/2/134` and `51/55`, `51/55`, `55/55` summaries.

### Out of scope

- Enlarging the word cutoff, primes, source groups, or the 138-row population.
- Enumerating all primitive `Gamma_0(11)` conjugacy classes.
- Changing the flow, density, owner orientation, Hecke normalization,
  newform coordinate, scalar laws, or matched controls.
- Constructing or validating a global dynamical determinant; A2--A4 and Route
  B remain closed.
- Literature synthesis, bibliography, novelty conclusions, manuscript
  drafting, or result generation in this Phase-1 brief.
- Prime tables, Riemann-zero tables, or target-zero fitting.

### Key assumptions to test rather than promote

- The frozen matrices and group labels replay from their source bytes.
- The existing per-instance root certificates survive independent exact
  verification.
- A complete subgroup-conjugacy decision procedure can be proved for every
  necessary trace/discriminant bucket. Its Phase-1 status is **PROVISIONAL —
  theorem contract unbound**; incomplete closure yields
  `NOT_EVALUABLE_CONJUGACY_INCOMPLETE`.
- Every duplicate incidence assigned one owner has the same exact global
  kernel fields and the same group-relative period ratio.
- Each owner has at most one Hecke degree inside a fixed source-word/prime
  group. This is tested, not assumed; conflict propagates to a predeclared
  not-evaluable group endpoint.

## Sub-questions

1. Can the all-pairs exact certificate ledger close a single global oriented primitive-owner partition with no unresolved root, conjugacy, or inverse decision?
2. How does that global partition map into the frozen incidence relation and conflict matrix without confusing cross-group recurrence incidences with additional owners?
3. What global kernel counts and cell-local verdicts follow from the frozen unit-cell moment equations, or which predeclared not-evaluable obstruction prevents them?

## Sub-question bindings (#547)

1. **Inherits:** population = frozen 138 rows; groups = frozen 55; artifact
   snapshot = P26 Round 4/6/8 bytes; domain = positive Level-11 time change;
   owner = oriented primitive `Gamma_0(11)` class; target data = forbidden.
   **Deviations:** none.
2. **Inherits:** all bindings of Sub-question 1; equivalence = exact subgroup
   conjugacy only; inverse = linked but not collapsed; degree = Hecke
   branch-cycle degree, never repetition. **Deviations:** none.
3. **Inherits:** all bindings of Sub-questions 1--2; global unit = one oriented
   owner ID across the population; cell unit = one owner per
   `(source_word,prime,degree)`; raw incidence = control only; denominator =
   exact `k(source)^2` inside the squared ratio and no count average; scalar
   laws = frozen `a_p`, `a_p^2`, and `a_p^2-p`. **Deviations:** none.

## Candidate questions considered

| # | Candidate | FINER average | Disposition |
|---:|---|---:|---|
| 1 | How does a complete global oriented-owner partition of the frozen 138-instance Hecke-output population induce the frozen cell-local no-double-credit moment classification? | **4.4/5, Feasible/Novel=PROVISIONAL** | **Selected:** closes the precise P26 A1 ownership gap while typing global identity and local Hecke incidence separately. |
| 2 | How many trace and homology collisions occur in the frozen population? | 4.2/5, Novel=PROVISIONAL | Not selected: descriptive invariants do not decide subgroup conjugacy or owner multiplicity. |
| 3 | Does the same taxonomy persist after enlarging the positive-word cutoff? | 3.6/5, Novel=PROVISIONAL | Deferred: it changes the frozen population before the current ownership gap is closed. |
| 4 | Does the Level-11 time change admit a global Hecke-compatible determinant? | 3.0/5, Novel=PROVISIONAL | Rejected for this phase: it jumps to A2 before A1 ownership is complete. |

## Phase boundary

This file is an RQ Brief only. Phase 2 bibliography, source verification,
synthesis, computation, claims, drafting, and Route evaluation are not
performed here.
