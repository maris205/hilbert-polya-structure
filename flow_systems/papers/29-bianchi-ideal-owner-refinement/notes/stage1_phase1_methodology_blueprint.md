# P29 Phase-1 Methodology Blueprint — Revision 1

Date: **2026-09-01 UTC**  
Mode: **ARS Deep Research / FULL / Phase 1 only**  
Controlling RQ: `stage1_phase1_rq_brief.md`

## Phase and claim boundary

This blueprint defines a proof-first A0–A1 mechanism-or-obstruction study. It
contains no source findings, experiment, theorem, novelty claim, Route tuple,
or preregistration artifact. A2–A4 and Route B are excluded.

## Research paradigm and method

**Paradigm:** positivist formal mathematics with falsification-first exact
certification.

**Method:** a performance-independently registered ideal mechanism first faces
formal codomain/transformation tests; a complete primitive-owner quotient then
enables one exact finite-refinement estimand; finally, only controls proved
capable of challenging the mechanism contribute specificity evidence.

The RQ drives this order. Separation performance cannot select a mechanism,
repair a formal failure, close an unresolved quotient, or validate an
insensitive control.

## Frozen object, owner, and codomain

- Object: the inherited Paper-24 unit-speed geodesic flow on the torsion-free
  level-(3) Gaussian Bianchi manifold.
- Clock: hyperbolic arclength; no word-length or fitted clock is admissible.
- Primitive owner: a primitive loxodromic conjugacy class in the level-(3)
  group, modulo inversion for the primary unoriented owner.
- Repetition: `gamma^r`, `r>=2`, belongs to the primitive root and is not a new
  owner.
- Codomain: one literal nonzero prime ideal of `Z[i]`. Associates give the same
  ideal; conjugate split ideals remain distinct.
- First obstruction: the mechanism must prove that an unoriented,
  inversion-invariant class can select one split ideal. A norm, rational prime,
  unordered conjugate pair, residue, composite ideal, or orientation-dependent
  choice emits `SPLIT_IDEAL_CODOMAIN_OBSTRUCTION` or `FORMAL_MAP_REFUTED`.

## Phase-2 mechanism-registry interface

The exact admissibility grammar, three-candidate cap, canonical source/formula
ID, lexicographic order, and performance-independent primary-selection rule are
defined in the RQ Brief and are immutable.

The Phase-2 registry must contain, per row:

```yaml
candidate_id:
canonical_source_identifier:
exact_formula_locator:
normalized_formula_sha256:
direct_formula_bytes:
domain:
codomain:
parameters_and_source_fixed_values:
conjugacy_law:
inversion_law:
repetition_law:
split_ideal_compatibility_obligation:
excluded_inputs:
admissibility_status:
exclusion_reason:
control_sensitivity_contract:
```

Phase 2 may verify and fill these fields but may not apply a mechanism to P29
rows. The frozen registry and exclusions require a new author checkpoint before
formal or empirical execution. Multiple admissible mechanisms are all reported;
only the first in frozen order is primary, and no collision metric enters that
choice.

## Complete primitive-owner quotient prerequisite

### Frozen input boundary

- `papers/24-bianchi-holonomy-flow/results/round7_trace_discriminant_ledger.csv`;
- 11,481 matrix rows, including 10,976 loxodromic rows, under the inherited
  elementary-generated subgroup reduced-word-ball cutoff through length 5;
- historical `(D9,J3)` and control artifacts remain read-only.

This is a loxodromic **matrix-row population awaiting quotient**, not yet an
owner population.

### Required decision procedure

Before any owner split, a Phase-2-verified complete decision procedure must be
frozen for projective lifts, loxodromic status, primitive roots, level-(3)
conjugacy, inversion, and canonical unoriented IDs. Bounded search failure is
never a negative certificate.

The algorithm contract must record its theorem/algorithm identifier,
preconditions, exact arithmetic domain, termination/completeness argument,
candidate-pair filters, deterministic resource limit, and serialization. If no
complete procedure and prospective resource contract can be frozen without
outcome inspection, the quotient status is `QUOTIENT_NOT_EVALUABLE`.

### Certificate interface

The quotient emits three linked tables.

```yaml
row_certificate:
  row_id:
  exact_projective_lift:
  loxodromic_status:
  primitive_root_matrix:
  repetition_exponent:
  oriented_class_id:
  inverse_oriented_class_id:
  unoriented_owner_id:
  root_verdict:
  root_certificate_type:
  root_certificate_path:
  root_certificate_sha256:

pair_certificate:
  pair_id:
  invariant_bucket:
  conjugacy_verdict:
  positive_conjugator:
  negative_certificate_type:
  certificate_path:
  certificate_sha256:

owner_certificate:
  unoriented_owner_id:
  member_row_ids:
  oriented_ids:
  primitive_root_id:
  inverse_link:
  transitivity_witnesses:
  status:
```

### Fail-closed statuses

- `QUOTIENT_CERTIFIED`: every eligible row, root decision, and necessary pair
  decision is resolved with a complete certificate; partition transitivity and
  population accounting pass.
- `QUOTIENT_NOT_EVALUABLE`: no source-verified complete algorithm/resource
  contract exists or an input/precondition fails.
- `QUOTIENT_UNRESOLVED_STOP`: the prospectively frozen resource limit is reached
  with at least one unresolved root/pair; no negative decision is inferred.
- `QUOTIENT_CONTRADICTION`: certificates or inherited exact identifiers
  disagree.

Only `QUOTIENT_CERTIFIED` creates an owner population. All other states stop
performance analysis and preserve a quotient-obstruction result.

## Prospective partition and leakage contract

All conjugate representatives, inverse orientations, powers, shared primitive
roots, and source rows linked by the quotient belong to one partition unit. The
unit ID is hashed with public salt `P29-ROUND10-V1`: buckets 0–59 are
construction, 60–79 validation, and 80–99 prospective holdout. This is a new
procedural holdout, not a claim that historical bytes or `(D9,J3)` values were
unread.

No partition is emitted before `QUOTIENT_CERTIFIED`. Known algebraic relations
may not cross partitions. Any later equivalence merge invalidates the partition
and emits `QUOTIENT_CONTRADICTION`; it does not trigger repartition after
performance is seen.

## Primary estimand and disposition algorithm

For the frozen primary mechanism `M`, compute on the prospective holdout:

```text
B(u) = (D9(u), J3(u))
C_H = unordered distinct owner pairs with equal B
S_H(M) = pairs in C_H receiving distinct literal prime ideals under M
```

Gate order:

1. registry/candidate gate;
2. formal codomain, conjugacy, inversion, repetition, and split-ideal gate;
3. quotient gate;
4. `|C_H|>0` evaluability gate;
5. primary result `S_H=0` or `S_H>=1`;
6. separate specificity gate.

No rate threshold is fitted. `S_H/|C_H|`, construction/validation performance,
mapped fraction, bucket sizes, and type summaries are secondary. The complete
typed disposition table in the RQ Brief is normative.

## Controls and sensitivity audit

### Mechanism-challenging controls

Before performance, the candidate registry must name the exact statistic or
formal property each control can change and give a proof or constructive
witness of sensitivity.

1. **Simpler-parent transport:** apply the exact construction grammar to the
   inherited full Gaussian ambient/rational-parent panels; predeclare whether
   domain, codomain, or a specific structural law should fail.
2. **Neighboring-level transport:** apply the same frozen construction at
   Gaussian levels 2 and 4; no parameter or formula may be retuned.
3. **Cross-ring transport:** apply the source-authorized analogue, if one
   exists without invention, to the inherited Eisenstein level-(3) panel and
   predeclare the type-level consequence.

These controls do not automatically count as three canonical Route-A types.
The control-sensitivity artifact must state each type classification and the
Route-A evaluator must accept at least three distinct effective types before
`SPECIFICITY_PASS` is available. Otherwise the mandatory disposition is
`SPECIFICITY_NOT_ESTABLISHED`, even if `S_H>0`.

### Demoted tests

- A bijective randomized ideal-label permutation is expected to preserve the
  collision partition and `S_H`; it is retained only as a label-invariance unit
  test and contributes no specificity evidence.
- A one-to-one norm-matched composite substitution can also preserve the
  collision partition; it is retained only as a codomain/type-rejection unit
  test and contributes no specificity evidence.

Neither test may enter a control margin or the three-control count.

## Data and target firewall

Data are repository-local, exact Paper-24 artifacts plus definitions verified
in Phase 2. No prime table, Riemann-zero table, learned label, target-fitted
parameter, or outcome-selected formula is permitted. Candidate selection,
quotient rules, partitions, estimand, controls, and sensitivity expectations
freeze before owner performance.

## Analysis sequence

1. Freeze and author-confirm the Phase-2 mechanism registry without P29
   performance access.
2. Prove or refute each registered formal law; perform the split-ideal test
   first and select the primary mechanism only by frozen order/formal pass.
3. Build and verify the complete primitive-owner quotient; stop on any
   fail-closed state.
4. Emit the prospective partition and freeze implementation checks on the
   construction subset; no mechanism substitution is allowed.
5. Open validation for diagnostics, then the prospective holdout once for
   primary `S_H`.
6. Execute only sensitivity-qualified mechanism controls; run the two demoted
   invariance/type unit tests separately.
7. Emit one typed disposition without Route promotion.

## Validity criteria

| Criterion | Required strategy |
|---|---|
| Construct validity | Literal prime-ideal codomain plus proof of conjugacy, inversion, repetition, and split-ideal compatibility |
| Quotient validity | Complete positive/negative certificates and zero unresolved owner relations |
| Selection validity | Closed source-derived registry, maximum three rows, canonical order, formal-only primary selection |
| Endpoint validity | One exact primary integer `S_H` and a complete gate/disposition table |
| Control validity | Each specificity control must be proved capable of changing its declared property; insensitive relabelings are unit tests only |
| Leakage resistance | All conjugacy/inverse/power/root-linked rows remain in one prospective partition unit |
| Reliability | Exact arithmetic, deterministic serialization, hashes, and a read-only verifier of certificate contracts |
| Boundary validity | Finite word-ball conclusions remain finite A0–A1 evidence and cannot become A2 |

## Kill gates

- Registry absent, modified after performance, or target/performance selected:
  `NO_ADMISSIBLE_IDEAL_OWNER_MECHANISM` or new design required.
- Inversion-invariant selection of one split ideal cannot be proved:
  `SPLIT_IDEAL_CODOMAIN_OBSTRUCTION`.
- Any formal domain/codomain/conjugacy/repetition failure: `FORMAL_MAP_REFUTED`.
- Any non-certified quotient state: stop; no owner performance or repartition.
- No baseline-collision pair in holdout: `REFINEMENT_NOT_EVALUABLE`.
- Fewer than three accepted, sensitivity-qualified control types:
  `SPECIFICITY_NOT_ESTABLISHED`.
- Any target data, outcome-based rule change, or new mechanism after freeze:
  stop for a new author-approved run.
- Any Euler product, determinant, A2, or Route-B inference: `STOP_SCOPED`.

## Limitations

- The finite word-ball census is not the full group or full geodesic flow.
- Quotient certification may fail and is itself a legitimate scoped result.
- One separated holdout pair proves only finite refinement, not a global
  orbit-to-prime-ideal correspondence.
- Specificity can remain unestablished even when finite refinement is positive.
- Novelty remains provisional pending Phase 2.

## Ethics, reporting, and preregistration

- No human subjects, personal data, animals, or interventions are involved;
  human-subjects review is not applicable.
- Discipline standard: theorem/proof plus exact computational-certificate
  reporting, with `PROVED`, `REFUTED`, `NUMERICALLY_CERTIFIED`, `OPEN`, and
  `NOT_EVALUABLE` kept distinct.
- Preregistration recommended before execution; current completed artifact
  declaration: `not_provided`; companion handle: `none`.
- #672 sidecar ownership is **dispatcher-only**; this file creates no digest or
  `preregistration-artifact/1.0` sidecar.

## Phase boundary

Phase 2 may verify sources and fill the frozen registry, then must return to an
author design checkpoint. This blueprint authorizes no search, computation,
claim, draft, Route promotion, or canonical refresh by itself.
