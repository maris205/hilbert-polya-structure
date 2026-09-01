# P30 Phase-1 Methodology Blueprint — Revision 1

Date: **2026-09-01 UTC**  
Mode: **ARS Deep Research / FULL / Phase 1 only**  
Controlling RQ: `stage1_phase1_rq_brief.md`

## Phase and claim boundary

This is a Phase-1 design, not a source review, operator theorem, computation,
novelty claim, Route tuple, or manuscript result. It distinguishes a
roof-agnostic calibration identity from independent physical-roof fidelity and
cross-roof nontransfer. A0 remains failed/absent.

## Paradigm and method

**Paradigm:** positivist formal mathematics with reproducible numerical
certification.

**Method:** construct one source-verified pointwise return-map roof/operator;
calibrate coefficient identities for each typed roof; validate the physical
roof against independent geometry; and test cross-roof non-equivalence under a
frozen scale/coboundary relation. Any missing pointwise data, comparison map, or
certified error term yields `NOT_EVALUABLE`, not a favorable tolerance.

## Frozen physical object, owners, and clock

- Geometry: equal disks of radius `a`, equilateral separation `d=6a`, inherited
  no-eclipse condition, unit-speed trapped billiard flow.
- Owner: physically realized primitive **oriented** cyclic no-repeat itinerary;
  cyclic rotations identify one owner, time reversal remains distinct, and
  disk-label permutations are not silently quotiented.
- Repetition: the `r`-fold traversal has symbolic length `r n_p`, physical time
  `r T_p`, and logarithmic coefficient `1/r`.
- Clock: actual Euclidean flight length. Unit roof, constant clock, fitted
  owner scales, stability weights, and quantum weights remain separate objects.

## Pointwise roof/operator evaluability gate

Finite primitive totals do not define a transfer-operator roof. Before any
operator output, Phase 2 must verify and freeze:

1. a Poincare return section and symbolic state space `(Sigma,sigma)` for the
   trapped physical flow;
2. inverse branches and admissible sequences matching the inherited owner
   convention;
3. a deterministic geometric evaluator for the pointwise/cylinder roof
   `tau_phys(y)`, including collision points, branch domains, regularity, and
   interval or a priori error bounds;
4. a function space and operator
   `(L_rho,s f)(x)=sum_{sigma y=x} exp(-s rho(y)) f(y)` with stated determinant
   and trace hypotheses; and
5. an input path built from geometry/coding data rather than fitted finite
   periodic totals; inherited `T_p` values are used only for validation.

The evaluability artifact records exact source locators, formulas, code-input
schemas, and hashes. If the current ledger/collision data cannot instantiate a
pointwise roof on the operator domain, emit `OPERATOR_NOT_EVALUABLE`. An
orbit-sum interpolation fitted to the ledger is prohibited.

If Phase 2 identifies multiple operator/function-space pairs, it must freeze
one source-supported pair at a new author checkpoint before any construction
result is inspected; no best-performing pair may be selected.

## Typed roof registry

Every roof has its own owner weights, Euler product, trace exponential, and
operator determinant under the same conventions.

| Roof ID | Definition and expected role |
|---|---|
| `PHYSICAL_D6` | Pointwise geometric `tau_phys` at `d=6a`; internal identity expected to pass and periodic sums must independently reproduce physical data. |
| `UNIT` | `rho(y)=1`; internally expected to pass. Cross-roof nontransfer from `PHYSICAL_D6` is tested by the exact period-two/period-three ratio obstruction. |
| `SHUFFLED_POINTWISE` | A prospective, deterministic transformation of the **pointwise** roof on the coding domain, frozen before results; internally expected to pass and cross-roof nontransfer is tested. If only finite `T_p` labels can be shuffled, the determinant is `NOT_EVALUABLE` and that shuffle is a ledger unit test only. |
| `PHYSICAL_D29_5`, `PHYSICAL_D31_5` | Independently constructed neighboring-geometry pointwise roofs at `d/a=29/5,31/5`; each internally expected to pass, while cross-roof nontransfer from `PHYSICAL_D6` is tested on frozen owner witnesses. |

An internally passing control is the expected outcome. Internal control failure
indicates a construction/bookkeeping defect and provides no physical
specificity evidence.

## Algebraic calibration identity

For any admissible roof `rho`, define

```text
Z_rho(s) = product_p (1-exp(-s T_p(rho)))^-1,
D_rho(s) = det(I-L_rho,s) = 1/Z_rho(s)
```

only when the source-verified trace/determinant hypotheses hold. The Euler and
trace-exponential expressions are two algebraic organizations of the same
primitive/repetition weights. Their agreement is a calibration identity, not a
test that `rho` is physical. Unit, shuffled, and neighboring roofs may all pass.

## Physical fidelity and cross-roof nontransfer

### Independent pointwise-fidelity endpoint

The pointwise geometric evaluator is frozen without periodic totals. Its sums
around construction, validation, and prospective-holdout owners are then
compared with inherited physical `T_p` intervals. The exact period-two and
period-three formulas are mandatory regressions. Fidelity passes only when all
predeclared rows lie within the a priori geometric/numerical error bound; no
empirical tolerance is fitted.

### Frozen equivalence relation

For roofs on the same coding, declare

```text
rho_1 ~ rho_2 iff rho_1 = c rho_2 + h - h o sigma for one global c>0.
```

Under source-verified hypotheses this implies proportional periodic sums
`T_p(rho_1)=c T_p(rho_2)` for every owner. A pair of predeclared owners with
disjoint certified period-ratio intervals refutes equivalence/nontransfer. It
cannot prove equivalence from a finite panel.

- `PHYSICAL_D6` versus `UNIT`: use the exact period-two and period-three mean
  roofs; their unequal ratios are the frozen regression.
- `PHYSICAL_D6` versus each neighboring roof: use the same period-two and
  period-three owner types and certify that no one scale fits both geometries.
- `PHYSICAL_D6` versus `SHUFFLED_POINTWISE`: use two predeclared owner IDs whose
  association is altered by the frozen pointwise shuffle. If no admissible
  pointwise shuffled roof exists, report `NOT_EVALUABLE`; a shuffled totals
  table is not an operator determinant.

Cross-roof determinant coefficients may provide a secondary non-equivalence
certificate after the same global scale is fixed prospectively. Passing
nontransfer distinguishes typed models; it does not create arithmetic A0.

## Common coefficient comparison and cutoff mapping

### Orbit cutoff

Primary ledger: the 747 realized oriented owners at `d/a=6` through symbolic
length 12. At cutoff `N`, Euler and trace channels include exactly terms with
`r n_p<=N`.

- construction: `n_p<=8`;
- validation: `n_p=9,10` added;
- prospective complexity holdout: `n_p=11,12` added once after method freeze;
- diagnostic cutoff sequence: `N=6,8,10,12`.

The ledger is already readable and may have been seen historically. The final
partition is therefore not called sealed and carries only prospective
procedural holdout weight for this revised method.

### Legal finite-rank map

A rank-`R` determinant does not inherit an orbit cutoff merely by sharing label
`N`. The only primary three-channel comparison is coefficientwise:

```text
log D_rho(s) = -sum_{n>=1} trace(L_rho,s^n)/n.
```

For each `n<=N`, the complete orbit/repetition coefficient is compared with
the corresponding trace coefficient and with the rank-`R` projected trace
coefficient. The projection map and coefficient extractor must be justified by
the frozen source-supported operator scheme. The full rank-`R` determinant is
a separately typed approximation and is never described as containing exactly
the `r n_p<=N` orbit set.

Any full-function or zero comparison requires the prospective error identity

```text
E_total = E_orbit_tail(N) + E_rank(R) + E_quadrature + E_roundoff.
```

Every term must have a source/theorem-derived bound on the same complex domain.
Missing or incompatible terms produce `NOT_EVALUABLE`. Extra/missing zero
counts require a certified contour and argument-principle error bound; otherwise
zero fields are `NOT_EVALUABLE`.

## Phase-2-derived pre-validation freeze rule

Phase 2 may derive values only from verified theory, exact geometry, and a
priori bounds—not from P30 construction/validation/holdout determinant outputs.
Before any such output is evaluated, a new author-confirmed design-freeze
artifact must fix:

```yaml
return_section_and_coding:
pointwise_roof_algorithm_and_input_schema:
function_space_and_determinant_class:
projection_and_coefficient_map:
complex_domain_and_contours:
rank_sequence_and_stop_rule:
quadrature_rule:
precision_ladder:
coefficient_norm:
absolute_and_relative_error_bounds:
orbit_tail_bound:
rank_error_bound:
quadrature_error_bound:
roundoff_bound:
root_count_and_matching_rule:
resource_limit_and_failure_state:
typed_control_roofs_and_expected_directions:
artifact_hashes:
```

No empirical “construction convergence” may choose these values. If verified
theory cannot supply the complete contract, emit
`ERROR_CONTRACT_NOT_EVALUABLE` and do not call the result compatible.

## Data strategy

Read-only inherited validation data:

- `papers/25-three-disk-scattering-flow/results/three_disk_primitive_ledger_round2.csv`;
- `papers/25-three-disk-scattering-flow/results/round8_exact_roof_witnesses.csv`;
- `papers/25-three-disk-scattering-flow/results/round8_physical_roof_replay.csv`;
- `papers/25-three-disk-scattering-flow/results/round8_roof_nontransfer_summary.json`.

Pointwise operator inputs must come from the independently frozen geometry and
coding path. Prime tables, Riemann-zero tables, resonance targets used for
tuning, and holdout-driven refitting are forbidden.

## Analysis sequence

1. Phase 2 verifies a pointwise coding/roof/operator and the complete error
   contract; an author checkpoint freezes them before output inspection.
2. Build code-path-separated Euler/trace and finite-rank channels, documenting
   all shared inputs, conventions, assumptions, and correlated failure modes.
3. Validate `tau_phys` periodic sums against exact witnesses and the frozen
   construction/validation/prospective-holdout owner schedule.
4. For every evaluable roof, test its internal coefficient identity; controls
   are expected to pass internally.
5. Apply the frozen scale/coboundary nontransfer tests between physical and
   unit/shuffled/neighboring typed roofs.
6. Apply full-function/root tests only if all four error components and contour
   conditions are certified.
7. Emit per-roof calibration, per-pair nontransfer, typed physical determinant
   infrastructure endpoint, and fixed
   `A0_FAIL / A2_NOT_ELIGIBLE / NO_ROUTE_PROMOTION` status.

## Required outputs

```yaml
pointwise_roof_evaluability:
physical_periodic_sum_fidelity:
roof_internal_calibration_status:
coefficient_error_by_n_and_cutoff:
rank_projection_error:
orbit_tail_bound:
quadrature_error:
roundoff_error:
cross_roof_equivalence_status:
nontransfer_witnesses:
prospective_holdout_status:
zero_fields_status:
typed_physical_determinant_infrastructure:
full_candidate_a2_eligibility: A2_NOT_ELIGIBLE
overall_route_a_status: A0_FAIL_A2_NOT_ELIGIBLE_NO_ROUTE_PROMOTION
```

## Validity criteria

| Criterion | Required strategy |
|---|---|
| Construct validity | Pointwise geometric physical roof built independently of total-period validation data |
| Calibration validity | Treat internal Euler/trace/determinant agreement as roof-agnostic identity for every typed roof |
| Physical-model validity | Require independent periodic-sum fidelity plus cross-roof nontransfer; never infer it from a control's internal failure |
| Cutoff validity | Compare coefficients through `n<=N`; keep full finite-rank determinant and orbit-tail approximation separately typed |
| Numerical validity | Pre-validation freeze of all four error terms, domains, contours, rank, precision, and stopping rules |
| Holdout honesty | Call `n=11,12` a prospective complexity holdout, not unread or sealed data |
| Reliability | Report code-path separation and shared/correlated assumptions; separate code is not called independent evidence |
| Route validity | A typed physical determinant infrastructure result carries no A2 credit; the full candidate is `A2_NOT_ELIGIBLE` and overall Route A remains blocked at A0 |

## Kill gates

- No pointwise roof/coding/function-space data independent of totals:
  `OPERATOR_NOT_EVALUABLE`.
- No legal coefficient projection/common comparison object:
  `CALIBRATION_NOT_EVALUABLE`.
- Incomplete pre-validation error contract: `ERROR_CONTRACT_NOT_EVALUABLE`.
- Internal control passes: expected; never a specificity failure.
- Internal channel failure: implementation/operator mismatch; do not infer the
  roof is nonphysical.
- Physical periodic sums fail frozen geometric bounds:
  `PHYSICAL_ROOF_FIDELITY_FAIL`.
- Cross-roof pointwise control cannot be constructed: that pair is
  `NOT_EVALUABLE`; finite label shuffling cannot replace it.
- Different clocks, owners, cutoffs, or normalizations across one comparison:
  stop as invalid object mixing.
- Validation/holdout refitting or empirically chosen tolerances: new design
  required.
- Any positive overall Route-A A2 claim while A0 fails: `STOP_SCOPED`.

## Limitations

- The orbit ledger ends at word length 12 and does not prove an infinite-flow
  determinant.
- Pointwise operator data may be absent from current artifacts; `NOT_EVALUABLE`
  is an acceptable result.
- Internal identity can validate bookkeeping for artificial roofs and cannot
  establish physical correctness.
- Finite nontransfer refutes the frozen equivalence when certified but cannot
  prove all possible relations between models.
- Novelty remains provisional pending Phase 2.

## Ethics, reporting, and preregistration

- No human subjects, personal data, animals, or interventions are involved;
  human-subjects review is not applicable.
- Discipline standard: theorem/proof plus reproducible computational
  certificates; report typed roofs, shared assumptions, coefficient maps,
  error budgets, controls, failures, and `NOT_EVALUABLE` states.
- Preregistration recommended before execution; completed artifact declaration:
  `not_provided`; companion handle: `none`.
- #672 sidecar ownership: **dispatcher-only**; this file creates no digest or
  `preregistration-artifact/1.0` sidecar.

## Route and phase boundary

A passed result may be labeled only
`TYPED_PHYSICAL_DETERMINANT_INFRASTRUCTURE_PASS`. That label contains no A2
credit. The full candidate remains
`A0_FAIL / A2_NOT_ELIGIBLE / NO_ROUTE_PROMOTION`; no positive Route-A A2
verdict, A3/A4, or Route B follows. This blueprint authorizes no source search,
computation, drafting, claim, or canonical refresh by itself.
