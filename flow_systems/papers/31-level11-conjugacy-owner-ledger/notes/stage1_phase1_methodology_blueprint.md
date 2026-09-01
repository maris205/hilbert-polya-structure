# P31 Stage-1 Phase-1 Methodology Blueprint

Date: **2026-09-01 UTC**  
Mode: **ARS Deep Research / FULL / Phase 1 only**  
Status: **REVISED PHASE-1 DESIGN — pending independent Checkpoint-1 replay**  
Controlling RQ: see `stage1_phase1_rq_brief.md`

## Research paradigm

**Selected:** proof-first mathematical realism with exact computational
certification.  
**Justification:** the RQ asks for finite algebraic ownership facts. Every
machine classification must follow a proved decision rule and carry a witness
or a complete nonexistence certificate; numerical similarity cannot answer the
RQ.

## Method

**Type:** quantitative exact computational mathematics.  
**Specific method:** a source-locked, proof-first census of primitive roots,
oriented `Gamma_0(11)` conjugacy classes, inverse pairs, and owner-level
multiplicities, followed by exact recomputation of the frozen finite taxonomy.

The study has three ordered layers:

1. **Proof layer:** establish complete finite decision procedures and the
   owner/multiplicity theorem before viewing collision or taxonomy outcomes.
2. **Certificate layer:** execute those procedures on the frozen rows with
   integer/rational arithmetic, deterministic serialization, independent
   reimplementation, and adversarial fixtures.
3. **Estimand layer:** first emit the global owner quotient, then map it through
   the separately frozen correspondence-incidence and cell-local moment
   operators. Global identity is never inferred from, or weighted by, cells.

No statistical significance test, fitted threshold, prime target, or
Riemann-zero target is used.

## Design-freeze registry

| Axis | Frozen value |
|---|---|
| Dynamical object | P26's positive time change `X_geo/rho_epsilon` on `T^1Y_0(11)`; no change to `rho_epsilon`, clock, or positivity interval |
| Arithmetic input | Real Level-11 newform differential and inherited Hecke normalization |
| Population/panel | Exactly 138 frozen output instances in 55 source-word/prime groups; no row, word, or prime may be added or removed |
| PSL lift | Canonical determinant-one lift with positive trace |
| Primitive owner | Oriented primitive `Gamma_0(11)` conjugacy class |
| Equivalence | Exact `Gamma_0(11)` conjugacy in `PSL(2,Z)`; trace/length/homology are filters only |
| Inverse | Separate oriented owner linked by an exact inverse-pair relation |
| Power | Exact primitive root plus traversal exponent; never Hecke degree |
| Global identity table `G` | One row per oriented primitive owner across all instances; source, prime, branch, cycle, and degree do not multiply global owners |
| Incidence relation `I` | All original rows keyed by `(owner_id, source_word, prime, cycle_id, branch_set, hecke_degree, instance_id)` |
| Cell-local quotient `C` | One row per `(source_word,prime,hecke_degree,owner_id)`; duplicate rows in the same cell receive one unit, while `I` preserves raw multiplicity |
| Cross-group owner | May contribute once to each distinct frozen Hecke cell because groups are separate recurrence estimands, but remains exactly one global owner and is never pooled as repeated global credit |
| Conflict matrix | One row per `(owner_id,source_word,prime)` with degrees present, raw count by degree, cell-unit indicator by degree, within-group status, orthogonal cross-group flag, and scientific disposition |
| Degree conflict | More than one degree for one owner inside one source-word/prime group yields `NOT_EVALUABLE_DEGREE_CONFLICT` for that group's three law endpoints; no tie-break or negative-law verdict |
| Taxonomy laws | Frozen `a_p`, `a_p^2`, and negative control `a_p^2-p`; frozen coordinate `k=2y+z` |
| Determinant convention | None: no global product or determinant is defined in this study |
| Order of limits | None: one finite source-locked quotient; no cutoff, precision, or infinite-population limit |
| Forbidden inputs | Prime target tables, Riemann zeros, fitted owner rules, floating zero decisions, outcome-dependent panel changes |

## Data strategy

**Data type:** secondary, repository-local, exact artifacts.  
**Sampling:** complete census of the registered population, not a statistical
sample.  
**Time frame:** the source-locked P26 Round-4/6/8 snapshot; later rows are not
eligible without a new design.

Primary bindings:

| Artifact | SHA-256 | Role |
|---|---|---|
| `results/round4_hecke_cycle_ledger.csv` | `f906df349b8f1fa2864fed592792e0fff63ba246a069179b7bd8cfdf46520662` | Source matrices, branches, cycle degrees, and registered incidence |
| `results/round6_quadratic_degree_moment_ledger.csv` | `f95e1435c9293f8e008cebf80084ea2b522b76186dbd684b5e3997c5e588edea` | Frozen scalar-law estimands |
| `results/round8_exact_instance_taxonomy_ledger.csv` | `beb363e4080b794e33ec6bc729b1f3e4dd7ef322be63fc59755e18fdf6bc889f` | Exact per-instance homology and kernel classification |
| `results/round8_exact_group_moment_taxonomy_ledger.csv` | `532e799686dd8afefa3a7529717208305fedede3f3e74e14ccf761ab35d74f69` | Inherited group-law control result |
| `results/round8_summary.json` | `4ba5de801dfd06c8b03bfe5fc07297b8c4e074bcf26c70ec6566de401ae2384d` | Boundary and population invariants |

All paths above are relative to the P26 directory and are read-only inputs.

## Proof-first analytical framework

### P1 — exact group and lift convention

Prove that positive-trace determinant-one normalization gives one projective
matrix representative for each eligible hyperbolic input. Enforce
`c == 0 mod 11` for subgroup membership and retain exact integer matrices.

### P2 — primitive-root completeness

For each matrix `M`, derive a finite exponent list from the exact trace/Chebyshev
constraints for a possible equation `M=P^r`. Solve every remaining integral
matrix equation exactly and check `P in Gamma_0(11)`. The result is either an
exact primitive-root witness `(P,r)` or a finite completeness certificate.
Existing P26 root flags are comparison inputs, not accepted as the new proof.

### P3 — complete subgroup-conjugacy decision

The candidate universe is all `binom(138,2)=9,453` unordered pairs of frozen
instance rows after exact primitive-root replacement. Every pair receives
exactly one terminal status in an all-pairs ledger:

```text
INVARIANT_EXCLUDED
CONJUGATE_WITNESS
NONCONJUGATE_CERTIFIED
UNRESOLVED
```

The closure identity is

```text
n_invariant_excluded + n_conjugate_witness
+ n_nonconjugate_certified + n_unresolved = 9,453,
```

with `n_unresolved=0`. Each invariant exclusion names the exact invariant and
both values. Each positive certificate stores the two instance/root IDs,
canonical lifts, all four entries of `C`, `det(C)=1`, `C_21 mod 11=0`, the
exact equality `CM=NC`, and validator verdict.

Negative decisions use a fail-closed theorem contract, not an implementation
promise. Before any scientific execution, a contract identified by theorem
name, version, immutable proof/source locator, and implementation hash must
state and independently verify all of the following:

1. preconditions on the positive-trace hyperbolic inputs and their membership
   in `Gamma_0(11)`;
2. construction of the complete integral solution lattice of `CM=NC`;
3. reduction of `det(C)=1` with `C_21 mod 11=0` to the exact integral
   quadratic/congruence problem actually solved;
4. the centralizer quotient or fundamental-cycle construction, its finite
   reduction domain, and a decreasing or periodic termination invariant;
5. a proof that the serialized reduced residues/cycles exhaust every eligible
   conjugator, not merely every conjugator below a height bound.

A `NONCONJUGATE_CERTIFIED` row must contain the contract ID, pair/root IDs,
solution-lattice basis, determinant-form coefficients, congruence system,
centralizer generator and quotient convention, reduction-domain bounds,
ordered exhaustive residue/cycle payload, termination measure, payload hash,
and independent-validator verdict. Missing preconditions, an unbound theorem,
an incomplete cycle, or validator disagreement forces `UNRESOLVED`; bounded
search failure is never negative evidence.

At this Phase-1 revision the theorem/source binding remains **UNBOUND** and
solver feasibility is **PROVISIONAL**. If a complete contract and all pair
certificates cannot be supplied, the scientific endpoint is
`NOT_EVALUABLE_CONJUGACY_INCOMPLETE`: publish the unresolved-pair audit, but do
not emit a closed owner partition, global taxonomy, or cell-local law verdict.

### P4 — canonical IDs and inverse relations

Define the owner ID as the lexicographically least reduced representative in
the proved finite reduced cycle under the bound theorem contract. Canonicalize
`M` and `M^{-1}` independently, link their IDs, and keep both orientations.
Verify partition transitivity by composed exact witnesses, not only by
union-find state. No canonical ID is scientific output unless the all-pairs
closure identity in P3 holds.

### P5 — multiplicity theorem and recomputation

Create and validate three noninterchangeable objects:

1. `G(owner_id, canonical_root, inverse_owner_id, compact_class, k_owner,
   kernel_class)`, with exactly one row per global oriented owner;
2. `I(owner_id, source_word, prime, cycle_id, branch_set, hecke_degree,
   instance_id, raw_incidence_count, k_source, k_owner)`, preserving the 138
   original rows;
3. `C(source_word, prime, hecke_degree, owner_id, cell_unit_weight=1,
   raw_incidence_count)`, obtained only by deduplicating `I` within a cell.

The global kernel class is assigned once on `G` by the mutually exclusive
exact predicates inherited from P26:

```text
FULL_COMPLEX_PERIOD_KERNEL
    iff compact_homology_class(g)=0;
REAL_PROJECTION_ONLY_KERNEL
    iff compact_homology_class(g)!=0 and k(g)=0;
TRUE_REAL_PROJECTION_NONKERNEL
    iff k(g)!=0.
```

Unavailable or internally inconsistent exact homology data produces
`NOT_EVALUABLE_GLOBAL_KERNEL_FIELDS`, not a fourth empirical class.

For `h=(w,p)`, define

```text
m(g,h,d) = number of incidence rows in I with owner g and degree d,
u(g,h,d) = 1 if m(g,h,d)>0, otherwise 0,
D(g,h)   = {d : m(g,h,d)>0},
r(g,h)   = k(g)/k(source_h),
M(h,d)   = sum over global owner IDs g of u(g,h,d) * r(g,h)^2.
```

The square ratio has the exact normalization denominator `k(source_h)^2`;
`M(h,d)` is an unaveraged rational sum and has no owner-count, row-count, or
sample-size denominator. Duplicate incidences assigned one owner must agree on
`k(g)`, global kernel class, and `r(g,h)` exactly.

The conflict matrix has fixed columns

```text
owner_id, source_word, prime, degrees_present,
incidence_count_by_degree, cell_unit_weight_by_degree,
within_group_status, cross_group_flag, cross_group_count,
scientific_disposition
```

The within-group status is assigned by the priority order
`OWNER_COORDINATE_CONFLICT > MULTI_DEGREE_SAME_GROUP >
DUPLICATE_WITHIN_CELL > SINGLE_INCIDENCE`; the cross-group flag is orthogonal
and may coexist with any status:

| Status/flag | Exact condition | Scientific interpretation |
|---|---|---|
| `DUPLICATE_WITHIN_CELL` | Some `m(g,h,d)>1`, but `|D(g,h)|=1` | One global owner is repeatedly incident in one cell; unit cell credit, raw count retained |
| `SINGLE_INCIDENCE` | `|D(g,h)|=1` and `m(g,h,d)=1` | Ordinary cell-local incidence |
| `MULTI_DEGREE_SAME_GROUP` | `|D(g,h)|>1` | Hecke degree is not a function of owner in that group; all three group-law endpoints are `NOT_EVALUABLE_DEGREE_CONFLICT` |
| `OWNER_COORDINATE_CONFLICT` | Duplicate-owner rows disagree on a global kernel field or on `r(g,h)` | Invalid quotient or source binding; global and local endpoints are not evaluable |
| `cross_group_flag=true` | The same `g` occurs under at least two distinct `(w,p)` groups | One global ownership fact participates in several separate Hecke-group estimands; allowed unless a within-group obstruction also applies, and never counted as several owners |

For each law `L` with `lambda_L(p)` equal respectively to `a_p`, `a_p^2`, or
`a_p^2-p`, a conflict-free group passes exactly when

```text
M(h,1) = lambda_L(p)  and  M(h,d) = 0 for every represented d>1.
```

Its exact residual row stores `M(h,d)-lambda_L(p)` at `d=1` and `M(h,d)` at
`d>1`. The group denominator is 55 groups; the global kernel denominator is
`|G|`; the inherited denominator 138 is instance-only. A global owner appearing
in multiple groups contributes once to each separate group equation, not to a
pooled global moment. The global kernel taxonomy is computed once on `G`, while
the three recurrence taxonomies are computed on the 55 group equations.
A changed, unchanged, conflicted, or not-evaluable outcome is valid under its
predeclared label; none may be rewritten as a negative law verdict.

## Target-blind computational plan

1. Verify all five input hashes and population invariants before parsing
   scientific fields.
2. Rebuild each matrix from the locked branch data and reject any mismatch.
3. Refuse solver execution until the P3 theorem contract and the deterministic
   fixture manifest are bound and independently validated.
4. Run the proof-backed root and conjugacy solvers using exact integers only;
   account for all 9,453 pair rows and require zero unresolved rows before
   constructing owner IDs.
5. Emit separate witness-bearing global-owner `G`, correspondence-incidence
   `I`, cell-local `C`, pair-certificate, inverse-pair, conflict-matrix,
   global-kernel, and group-law ledgers in canonical order.
6. Re-run from a clean temporary tree and require byte-identical artifacts.
7. Run an independently implemented verifier that consumes, but does not
   create, the owner ledger and validates the separate theorem contract.
8. Keep all new outputs separate from canonical P26 results until their later
   pipeline stage authorizes promotion.

## Frozen controls

| Control | Predeclared expected behavior |
|---|---|
| Known-conjugate fixtures `CMC^{-1}` for fixed small `C in Gamma_0(11)` | Must retain the same owner ID and provide a witness |
| Inverse and proper-power fixtures | Must preserve orientation linkage and recover the primitive root/exponent |
| Same-trace but subgroup-split fixtures | Must not be merged without a subgroup witness |
| Simpler-parent `PSL(2,Z)` quotient | May merge at least as much as the subgroup quotient; its classes cannot be substituted for `Gamma_0(11)` classes |
| Row permutation and exact row duplication | Owner IDs must be order-invariant; duplicate input changes incidence counts but not unique-owner identities |
| Frozen incidence-weighted taxonomy | Serves as the matched baseline, not as truth for the unique-owner estimand |

The fixture-generation specification is frozen now, while its instantiated
manifest remains `NOT_PROVIDED`; that status blocks execution. For a matrix
`A=(a b; c d)`, define `height(A)=max(|a|,|b|,|c|,|d|)`. Order matrices by
`(height,a,b,c,d)` and frozen instance rows by
`(source_word,prime,cycle_id,instance_id)`.

- **Eight known-conjugate fixtures:** use the first eight eligible primitive
  source matrices `M_i` and the explicit
  `C_i=((1,i),(11,11*i+1))`, `i=1,...,8`; expected verdict is conjugate, and
  the stored witness is `C_i` (maximum conjugator height 89).
- **Eight inverse fixtures:** use the same eight `M_i`; expected output is a
  separate oriented ID linked to the ID of `M_i` (self-inverse conjugacy, if
  certified, must still be represented by the exact link rather than silent
  collapse).
- **Eight proper-power fixtures:** use `M_i^2` for `i=1,...,4` and `M_i^3`
  for `i=5,...,8`; expected primitive root is `M_i` with the displayed
  exponent.
- **Eight subgroup-split fixtures:** enumerate positive-trace hyperbolic
  matrices of height at most 24 in `Gamma_0(11)`, form same-trace pairs in the
  stated order, and retain the first eight pairs separated by the first
  available exact finite-quotient conjugacy obstruction in moduli
  `(11,121,2,3,5,7,13)`. Each row stores the finite quotient, its complete
  image enumeration, and the nonconjugate images. If eight do not exist, the
  fixture manifest is `NOT_EVALUABLE_INSUFFICIENT_SPLIT_FIXTURES`; the bound or
  selection rule may not be enlarged after scientific outcomes.
- **Sixteen small exhaustive verifier fixtures:** eight positive and eight
  negative pairs, in the same order, for which a separate elementary proof
  supplies a complete conjugator-height bound `B_fix`. The manifest stores
  `B_fix`, its proof-contract ID, and exhaustive enumeration hash; failure to
  supply a proved bound makes the verifier suite not closed.

Before any scientific row is classified, one immutable manifest must contain
all 48 fixture records, expected verdicts, generator version, contract IDs,
selection counts, bounds, serialized bytes, and SHA-256. No extra fixture may
be selected after collision classes or taxonomies are visible.

The independent verifier must check integer witness equations directly,
replay finite-quotient obstructions, validate every negative certificate
against the separately stated theorem contract and termination invariant, and
run the 16 bounded-exhaustive fixtures. Byte identity alone is only a
determinism check.

## Validity criteria

| Criterion | Required strategy |
|---|---|
| Construct validity | Keep conjugacy, inversion, power, Hecke degree, and multiplicity as separate typed fields |
| Internal validity | Every merge has an exact witness; every non-merge in a candidate bucket has a completeness certificate |
| Completeness | Account for 138/138 instances and exactly 9,453 unordered pair rows, with the four-status identity and zero unresolved rows |
| Estimand validity | Validate `G`, `I`, and `C` separately; freeze moment equations, denominator, cross-group rule, and conflict propagation before outcomes |
| Reliability | Two byte-identical builds plus a verifier that checks equations and completeness certificates against an independent theorem contract and bounded-exhaustive fixtures |
| Arithmetic exactness | Integer/rational decisions only; no floating zero or tolerance controls a classification |
| Target blindness | No prime target, zero target, fitted threshold, or output-driven fixture/panel selection |
| Boundary validity | Any successful census closes only the registered A1 ownership gap and does not create A2 credit |

## Kill gates

- Any source hash or 138/55 population invariant mismatch: **STOP — source
  lock failed**.
- Any root decision lacking a finite completeness proof: **STOP — primitive
  owner unresolved**.
- Any unbound conjugacy theorem/precondition/termination contract or incomplete
  48-record fixture manifest: **STOP — solver feasibility not established**.
- Any claimed conjugacy based only on trace, length, homology, or bounded
  search: **STOP — invalid equivalence evidence**.
- Any failure of the 9,453-pair accounting identity, any unresolved pair, or
  any negative certificate missing a required field: emit
  `NOT_EVALUABLE_CONJUGACY_INCOMPLETE`; **STOP — no closed owner ledger or
  taxonomy**.
- One owner carrying conflicting Hecke degrees within one source-word/prime
  group: label that group's three law endpoints
  `NOT_EVALUABLE_DEGREE_CONFLICT`; do not choose a degree, pool cells, or call
  the law false.
- Any owner-field or group-relative ratio disagreement among rows assigned the
  same owner: emit `NOT_EVALUABLE_OWNER_COORDINATE_CONFLICT`; **STOP the
  affected global/local endpoints**.
- Any need to change the panel, flow, owner orientation, laws, or multiplicity
  rule after seeing results: **STOP — new design and confirmation required**.
- Any attempt to infer a primitive Euler product or A2 from the finite ledger:
  **STOP_SCOPED**.

## Limitations by design

- The census can be complete for 138 rows while remaining silent about every
  unregistered primitive orbit.
- Unit owner weight is a declared primitive-product diagnostic, not a theorem
  that the Hecke correspondence has multiplicity one.
- A cell-local contribution is a Hecke-incidence estimand, not another global
  owner; the global kernel quotient and 55 group-law equations intentionally
  answer different questions.
- Complete subgroup nonconjugacy remains provisionally feasible until the P3
  theorem contract, its source/proof, and independent validator are bound.
- The exact owner quotient may refine A1 accounting but cannot supply an
  arithmetic prime-owner map, determinant, analytic continuation, or quantum
  lift.
- Novelty remains **PROVISIONAL** until Phase-2 literature verification.

## Ethical considerations and human-subjects status

This is theoretical and exact computational mathematics using public/project
artifacts. It involves no human participants, personal data, animals,
biological material, clinical activity, or field intervention. Human-subjects
administrative review is **not applicable**.

## Reporting standard

- **Recommended discipline standard:** theorem/proof plus computer-assisted
  certificate reporting; distinguish `PROVED`, `NUMERICALLY_CERTIFIED`, and
  `OPEN`; disclose source hashes, algorithms, completeness bounds, fixtures,
  failures, and deterministic replay.
- **EQUATOR guideline:** none applicable to this mathematical census; do not
  mislabel it as an observational or clinical study.
- Negative, null, conflict, and unchanged-taxonomy outcomes receive the same
  artifact and reporting treatment as positive collisions.

## Preregistration (#672 declaration only)

- Recommended: **Yes**, before scientific execution, because the owner rule,
  multiplicity rule, controls, and kill gates are confirmatory.
- Platform: **OSF Registries** if the scholar later supplies a completed record.
- Status: **not provided**.
- Completed artifact declaration: **not_provided**.
- Companion handle: **none**.
- Sidecar/advisory ownership: **dispatcher only**. This Phase-1 architect file
  does not create a hash, sidecar, or `preregistration-artifact/1.0`; the #672
  dispatcher operation has not been run.

## Phase boundary

This blueprint authorizes no computation by itself and contains no Phase-2
bibliography, Phase-3 synthesis, manuscript draft, review, result, claim
registration, Route promotion, or canonical refresh.
