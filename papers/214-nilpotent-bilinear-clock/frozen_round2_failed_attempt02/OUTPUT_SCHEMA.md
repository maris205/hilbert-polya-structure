# P214 complete author output schema — prospective

Status: `SOURCE_ONLY / NOT_EXECUTED / NO_CANONICAL`.
The future `CANONICAL.json` is a historical role filename containing JSONL,
NOT one JSON object. No file with that role is created or accepted here.
The stream is full evidence: never replace it with only the terminal summary,
a digest, or a selected subset of states or targets.

[OUTPUT_SCHEMA.json](OUTPUT_SCHEMA.json) is a Draft 2020-12 JSON Schema for
each individual line. It rejects unknown record fields and describes every
nested object; its `$schema` URI is a dialect identifier, not a requested
network fetch. This narrative supplies stream-level ordering, exact field
semantics, named checks and cross-record constraints that a per-line grammar
cannot fully express. No schema validation against scientific output has been
executed. Any document-only JSON syntax check is recorded in SOURCE_HANDOFF.md;
it neither runs this verifier nor validates a scientific transcript.

## Common data and ordering

Every record has `schema_version="p214-author-jsonl-v1"` and `kind`.
Case records additionally have q and m. Scientific records except run_start
have `checks`, mapping exact comparison names to true after success; repeated
comparisons under one name appear once per record and are fully counted in
run_complete.check_counts. Scalars representing codes, IDs, counts, depths
or valuations are integers. No floats occur. Lists are ordered, not sets
silently normalized by the serializer.

Ring code `sum(c_i*q^i)` uses ascending coefficient degree and the field-code
convention recorded by `field`. I codes are divisible by q. If nI=q^(m-1),
state `(x,y)` has ID `(x_code//q)*nI+y_code//q` in 0,...,nI^2-1.
All state-ID sets, predecessor lists, image lists, kernel code lists and
ring dictionaries are emitted in ascending order. Trajectory lists instead
follow time. Permutation/transition arrays are indexed by source state ID.
No cross-carrier ID is meaningful without q,m.

The exact successful stream order is: run_start; for each q=2,3,4, one field
then, for m=2,3,4, carrier, adapter, all states, all targets, depth rows,
fibre rows, carrier_complete; finally run_complete. State/target IDs increase
from zero without gaps; h increases 0,...,2m-2; fibre-row d increases
0,...,m-1. Thus prospective record multiplicities are 1,3,9,9,5271,5271,45,
27,9,1 respectively, totaling 10646. These are deductive protocol counts,
not observations. Successful serialization sorts keys, uses compact JSON,
ASCII escaping and a newline after every record. Exit zero and the final
complete record are both necessary, not sufficient, for later acceptance.

## Exact record fields

In the descriptions below, the common fields are not repeated. Every listed
field is required. Nullability is stated explicitly; there are no optional
scientific fields whose omission means zero.

`run_start`: `parameters` is the exact nine-pair ordered Cartesian list;
`q_values` and `m_values` are [2,3,4]. `program_role` is author_verifier,
`mathematical_scope` fixed_finite_box_only, and `configuration_policy`
embedded_constants_no_external_reads. These are assertions about intended
scope, not evidence that the interpreter dependency boundary was accepted.

`field`: q; `characteristic`; ordered `element_labels`; `modulus_binary`
(7 for q=4, otherwise null); complete q-by-q `addition_table` and
`multiplication_table`; `additive_inverses`; `multiplicative_inverses`
(zero entry null); checks. GF(4) labels are 0,1,alpha,1+alpha, modulus
alpha^2+alpha+1. The value alpha is not the ring variable t.

`carrier`: `ring_size=q^m`, `ideal_size=q^(m-1)`, `state_count=ideal_size^2`,
`t_code`, `negative_t_code`, all `ideal_codes`, and all `ring_elements`.
Each ring element object has `code`, length-m `coefficients`, and `valuation`
(m at zero); checks. The dictionary covers code 0 through q^m-1 exactly once.

`adapter`: complete arrays `P`, `P_inverse`, `Q`, `Q_inverse`,
`M_transitions`; `nonconjugacy_warning_witness` with `state_id=0`,
`Q_state_id`, `P_inverse_state_id`; checks. These implement P(x,y)=(x,y+t),
Q(u,w)=(u-t,w), M(a,b)=(b,ab). The warning only records Q != P^-1: it does
not itself prove the nonexistence of every dynamical conjugacy.

`state`: `state_id`; `x_code`, `y_code`; `x_valuation`, `y_valuation`;
`successor_state_id` for F, `linear_successor_state_id` for L;
`orbit`, `linear_orbit`; `actual_depth`, `expected_depth`;
`scalar_path_codes`; `P_state_id`, `M_P_state_id`, `Q_M_P_state_id`; checks.
Actual depth is discovered from the literal orbit, expected depth is the
theorem expression. A successful record has equal nonnegative depths.
The scalar path consists of the first coordinates of all nonrepeated orbit
states, then the second coordinate of the last such state: x0,...,x_(h+1).

Each `orbit` object has exactly `state_ids` (visited nonrepeated states plus
the first repeated state at the end), `cycle_start_index`, `cycle_state_ids`
(one copy of the detected cycle, no duplicate end), `period` (cycle length),
and `first_zero_index` (integer if zero was visited, otherwise null).
The walk's stopping rule uses only repeat detection in the transition array.
Under successful claim checks the cycle is [0], period 1 and first-zero index
equals depth. These conditions must not be used to manufacture observations.

`target`: `target_state_id`; `u_code`, `w_code`; `multiplier_code=t+u`,
`multiplier_valuation`; capped `d`; boolean `feasible`; complete literal
`predecessor_state_ids`; `actual_fibre_size`, `expected_fibre_size`;
`kernel_codes`; `unit_code`, `inverse_unit_code`; `shifted_w_code`;
`representative_x_code`; `coset_predecessor_state_ids`; `M_target_state_id`;
`M_predecessor_state_ids`; `transported_predecessor_state_ids`; checks.
Here d=min(multiplier_valuation,m-1), always >=1. Feasible means v(w)>=d+1.
The kernel is all t^(m-d)R codes even when the target is unreachable.
Unit/inverse fields are null exactly in the saturated case d=m-1;
otherwise they exist even for unreachable w. shifted_w is nonnull only for
reachable nonsaturated targets. representative_x is null for unreachable
targets, zero in the reachable saturated case, and the constructed
t*e^-1*w0 otherwise. Empty fibres have three empty F predecessor/coset/
transported lists, not omitted records. M_target is Q^-1(target);
its complete M predecessor list is transported using P^-1. Each successful
coset/predecessor list agrees including multiplicity, not merely as a set.

`depth_row`: h; `threshold_x=m-ceil(h/2)`, `threshold_y=m-floor(h/2)`;
`exact_state_ids`, `cumulative_state_ids`, `rectangle_state_ids`;
`linear_exact_state_ids`, `linear_cumulative_state_ids`;
`actual_exact_count`, `expected_exact_count`; `actual_cumulative_count`,
`expected_cumulative_count`; checks. The rectangle uses both valuation
thresholds. Expected exact count is 1 at h=0 and (q-1)q^(h-1) otherwise;
expected cumulative count is q^h. Every named list is complete.

`fibre_row`: d; `fibre_size`; `target_state_ids`,
`expected_target_state_ids`; `actual_count`, `expected_count`; checks.
Row d=0 denotes empty fibres, not target multiplier valuation zero. For
d>0, size=q^d. Expected count is q when d=m-1 and otherwise
(q-1)q^(2(m-d-1)); empty expected count is state_count minus image formula.

`carrier_complete`: `state_count`, `target_count`; `recurrent_state_ids`,
`fixed_state_ids`, `linear_recurrent_state_ids`; `maximum_depth`;
`maximum_depth_state_ids`, `expected_maximum_depth_state_ids`;
`maximum_fibre_size`, `maximum_fibre_target_state_ids`;
`saturated_target_state_ids`, `image_target_state_ids`; `actual_image_size`,
`expected_image_size`, `empty_fibre_count`; `unequal_positive_fibre_witness`,
`nonlinear_literal_witness`, `cancellation_witness`; checks.
The expected maximum-depth set has v(y)=1. Saturated targets are the q
distinct (-t+c*t^(m-1),0). At m>=3 the unequal witness has
`small_target_state_id`, `large_target_state_id`, full
`small_predecessor_state_ids`, `large_predecessor_state_ids`, and
`small_fibre_size`, `large_fibre_size`, using targets (0,0),(-t,0).
The nonlinear witness has `state_id` for (t,t), `F_state_id`, `L_state_id`.
Those two witnesses are null at m=2. Cancellation witness always has
`state_id` for (t,-t), the complete `orbit` object and `expected_state_ids`
from the explicit alternating -t powers, including final repeated zero.

`run_complete`: `status=FINITE_BOX_CHECKS_PASSED`; exact `parameters`;
`state_count=5271`, `target_count=5271`, `carrier_count=9`; `check_count`;
`check_counts` mapping names to numbers of comparisons;
`preceding_record_counts` excluding this final record; `checks`; `limitation`
with the literal finite-check/all-parameter/novelty caveat. The check count
includes the final coverage comparisons. This is prospective behavior, not
a PASS issued by a source document.

`verification_failure`: `status=FAIL`; `detail` with `scope`, `check`,
`actual`, `expected`; `attempted_check_count`; `preceding_record_counts`;
exit 1 and no run_complete. Scope identifies q,m,state/target/h/d as applicable
or the run configuration/completion. Counts include the failing comparison
when Audit.equal was entered; CLI rejection happens before any comparison.
`runtime_error`: `status=ERROR`, `error_type`, `message`,
`attempted_check_count`, `preceding_record_counts`; exit 2 and no run_complete.
Interpreter/import or broken-output failures outside the application handler
also remain failed runs, even if no well-formed error record can be emitted.

## Named comparison registry

Names below are exact source labels; repeated universal-loop comparisons
are represented by counts, while the full mathematical objects remain in
their associated records. Conditional labels appear only in their branch.

- Field: field_additive_identity, field_multiplicative_identity,
  field_additive_inverse, field_multiplicative_inverse,
  field_addition_closure, field_multiplication_closure,
  field_addition_commutative, field_multiplication_commutative,
  field_addition_associative, field_multiplication_associative,
  field_distributive; at q=4, gf4_alpha_square, gf4_characteristic_two.
- Carrier: carrier_ideal_size, carrier_state_count,
  ring_encoding_round_trip, ideal_power_cardinality.
- Adapter: adapter_P_permutation, adapter_P_inverse_permutation,
  adapter_Q_permutation, adapter_Q_inverse_permutation,
  adapter_P_inverse, adapter_Q_inverse, adapter_Q_is_not_P_inverse_at_zero.
- State: state_encoding_round_trip, closure, product_valuation,
  second_successor_in_t_squared, orbit_repeat_bound,
  unique_recurrent_sink_per_orbit, recurrent_period_one, exact_clock,
  maximum_depth_characterization, QMP_pointwise,
  linear_unique_recurrent_sink, linear_clock; at m=2, m2_linear_boundary,
  m2_literal_boundary. Scalar-loop branches: later_scalar_in_t_squared,
  later_multiplier_valuation_one, noncancellation_chain_valuation,
  cancellation_safe_odd_chain, cancellation_even_chain_lower_bound.
- Target: fibre_feasibility, fibre_kernel_size, fibre_size,
  fibre_coset_equality, fibre_QMP_transport,
  fibre_first_coordinate_constraint (the predecessor's second coordinate
  equals the target's first coordinate), fibre_kernel_equation;
  nonsaturated fibre_unit_inverse, fibre_shifted_unit;
  reachable fibre_representative_in_I, fibre_representative_equation;
  saturated_feasibility.
- Depth: cumulative_depth_rectangle, cumulative_depth_count,
  exact_depth_count, linear_exact_depth_census, linear_cumulative_depth_census.
- Fibre row: fibre_census_target_set, fibre_census_count.
- Carrier completion: zero_fixed, unique_recurrent_set, unique_fixed_set,
  linear_unique_recurrent_set, maximum_depth_value, maximum_depth_exact_set,
  maximum_fibre_value, maximum_fibre_exact_set, saturated_target_count,
  image_size, image_exact_set, predecessor_partition, fibre_mass,
  cancellation_witness_trajectory, cancellation_witness_clock;
  for m>=3, unequal_positive_fibre_small, unequal_positive_fibre_large,
  unequal_positive_fibres, m_ge_3_literal_nonlinear_difference.
- Run completion: complete_cartesian_state_total,
  complete_cartesian_target_total, complete_cartesian_carriers,
  complete_state_records, complete_record_census. Configuration failure:
  no_cli_arguments.

## Required later stream acceptance

A later authorized receiver must check exact field sets/schema, record order
and multiplicity, coordinate/ID bounds and code dictionary completeness,
the complete F/L/M transition and orbit correspondence, every target bucket
and coset (including empties), census partitions, witness references,
named check presence and branch applicability, count aggregation, final
status, runtime exit/capture and frozen source/runtime inputs. JSON Schema
alone checks grammar, not mathematical correctness or provenance. A later
determinism claim requires complete raw-byte stream comparison, not parsed
summary equality. None of those executions or comparisons is claimed here.
