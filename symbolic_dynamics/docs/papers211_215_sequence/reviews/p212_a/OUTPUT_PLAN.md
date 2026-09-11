# Proposed independent producer output and adoption plan

SOURCE ONLY. No canonical path is populated, no execution receipt is supplied,
and no check total or byte count is forecast as an actual result.

After source acceptance, root must separately bind the exact interpreter,
ordinary runtime inputs, this source, documentary parameters, frozen input
pins, empty arguments, fixed environment/cwd/stdin, and fresh exact output
paths. Record actual request/result, exit, stdout/stderr and pre/post keys.
The first complete actual accepted stdout alone may become the independent
canonical. Do not fabricate a canonical or compare author-format bytes to
this different schema. Two separately bound strict/root replays must retain
complete raw output and demonstrate byte equality against the adopted
canonical and each other, with exact current keys. Required review/final
receipt and manifest stages occur after those real observations, not now.

The producer prints one deterministic ASCII JSON object and one newline.
It emits all ledger failures with observed/expected values before raising
if comparison failures occur. A structural `need` error can stop earlier;
such incomplete stdout is failed evidence and never a canonical. Stderr,
partial stdout and unsuccessful receipts must be preserved. Zero imports
does not claim an untrusted-host sandbox or authenticate execution by itself.

## Schema P212_A_FULL_OUTPUT_V1

Object keys are lexicographically encoded. Arrays retain the source-defined
order. Types are null-free: bool, integer, printable ASCII string, array,
or string-keyed object. Tuples serialize as arrays. No floating point occurs.
Every label is zero-based. A state is [u,v,f(0),...,f(n-1)], with little-endian
base-n rank. An edge is [min(a,b),max(a,b)]; repeated edges retain multiplicity.

Top-level exact keys: `schema`, `role`, `parameters`, `method`, `catalogues`,
`coefficients_scaled24`, `carriers`, `checks`, `check_census`, `failure_ids`,
`finite_passed`, `limits`. Literal values and ordering are fixed in source.

`catalogues` is [[s,entries],...] for s=1,2,3,4. Every entry has exact keys
`id, edges, family, paths, lengths, row, period, decorations, visit_words,
incidence_states`. IDs follow sorted edge-multiset order. Families 0/1/2
mean figure-eight/barbell/theta. Paths are canonical vertex lists;
lengths are their edge counts. Rows 0..6 are respectively double loop,
short figure-eight, long figure-eight, short barbell, long barbell,
triple-direct theta, other theta. Visit words are sorted primitive necklaces.
Incidence states are [state,positive multiplicity] in lexicographic state
order. Multiplicity counts marked/oriented edge-occurrence realizations;
only the state, not that multiplicity, defines a literal configuration.

`coefficients_scaled24` has [s,[figure8_polynomial,barbell_polynomial,
theta_polynomial],total24,period_weighted_total24]. A polynomial is sorted
[[period,integer_coefficient],...] omitting zero entries. These are scaled
EGF coefficients, not labelled integer orbit counts.

Each `carriers` object has exact keys `n,states,orbits,groups,row_counts,
period_counts,extension_terms_scaled24,unexercised_group_ids`.

* `states`: [id,state,successor_id,predecessor_id,group_id,orbit_id,
  active_vertex_bitmask,admissible_core_bitmasks], in increasing state ID.
  Admissible masks include the empty set; their union is the unique maximal
  induced minimum-degree-two subset of the active component.
* `orbits`: full directed ID routes, seeded by the smallest not-yet-assigned
  ID, with no duplicated closing state. Actual first repetition must be seed.
* A group key is [increasing_core_labels,sorted_core_edges,
  [[outside_label,frozen_target],...]]. `groups` rows are [id,key,core_size,
  catalogue_id,observed_orbit_ids,sorted_expected_orbit_routes]. Group IDs
  follow lexicographic key order; routes are rotated to smallest state ID.
* `row_counts`: seven [groups,orbits,states] rows in the row order above.
* `period_counts`: polynomial of actual full-carrier orbit counts.
* `extension_terms_scaled24`: [s,(n)_s*n^(n-s),core_polynomial24].
* `unexercised_group_ids`: three lists for both-long figure-eight,
  both-long barbell and all-nondirect theta, each expected empty in this box.

`checks` rows are [name,scope,observed,expected,passed], in actual invocation
order. Scope is a string, integer or [carrier_or_core_size,local_id]. Every
pass compares full deterministic wire values; no digest-only predicates.
`check_census` is sorted [name,row_count,failure_count]. `failure_ids` indexes
failed ledger rows; `finite_passed` means exactly that this list is empty,
not that an all-size theorem, manuscript or execution attestation passed.

The retained checks include full incidence exhaustion, reconstructed literal
successors and exact edges, primitive state periods, catalogue decoration
counts and table periods, complete core/complement groups, actual full orbit
partition, per-state inverse/invariant/core predicates, complete decorated
orbit partitions, integer-scaled core and carrier censuses, attained periods,
maximum, fixed states, weighted mass, all seven row-presence thresholds and
explicit unexercised-family lists. Exact predicate spellings are in source;
the generated census records every actual occurrence.
