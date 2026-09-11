# Exact output schema: finite-pointer-pilot-output-v1

Status: PREPARATION_ONLY / NOT_EXECUTED. This document specifies future output;
it is not a saved run or a result claim. The producer writes one JSON object
followed by one LF to stdout, ASCII JSON, sorted object keys, compact separators,
no NaN/Infinity, no comments and no timestamps. Arrays follow the order below.
It creates no output files. The separately approved executor must capture raw
stdout and stderr without normalization. No canonical exists for this pilot.

All integer fields below are JSON integers, not strings, floats or booleans.
Labels are 1-based; state/orbit/group/core IDs are 0-based within each box.
All cross-references refer to the same box. No state, edge or orbit is omitted.

## Common records

- `ratio = {numerator: integer, denominator: positive integer}` is the reduced
  Fraction representation, including denominator 1 for integral values.
- `integer_or_ratio` is an integer when its exact Fraction denominator is 1,
  otherwise a ratio record. Fractions in expected orbit counts are permitted
  only to preserve a failed prediction; their associated integrality check
  fails. A successful output has integer expected orbit counts throughout.
- `coefficient_row = {s: positive integer, p: positive integer, coefficient:
  ratio}`. Rows contain every nonzero coefficient within the stated t-degree
  bound, sorted by `(s,p)`; no q-degree bound is imposed.
- `period_count_row = {p: positive integer, count: integer_or_ratio}`. Only
  nonzero counts occur, sorted by p. Empirical counts are positive integers.
- `core_period_count_row = {s, p, count}` has the same convention, sorted
  by `(s,p)`.
- `check = {id: string, observed: JSON value, expected: JSON value, pass:
  boolean}`. `pass` is exact equality before JSON serialization; state tuples
  serialize to arrays on both sides. IDs are unique across the entire output.
  No failed comparison is suppressed. Complete named predicates are defined
  in CLAIM_PREDICATES.md.
- `edge_multiset`: sorted rows `[a,b,multiplicity]`, with `1<=a<=b<=n` and
  positive multiplicity. A loop is one edge; it contributes two to degree.

## Top-level object: exact keys

`schema_version`, `role`, `parameters`, `coefficient_arithmetic`, `core_series`,
`boxes`, `checks`, `summary`.

- `schema_version = "finite-pointer-pilot-output-v1"`.
- `role = "bounded-author-evidence-not-admission"`.
- `parameters`: exactly the parsed PARAMETERS.json object. The producer rejects
  extra/missing fields, reordered/changed boxes, noninteger numeric encodings,
  duplicate keys, nonfinite constants or any parameter change. Object-key
  order and whitespace in the input are semantically irrelevant; exact input
  bytes are separately pinned for the eventual execution binding.
- `coefficient_arithmetic = "fractions.Fraction; t-degree <= 4; q-degree uncapped"`.
- `core_series = {pieces, total}`. `pieces` has precisely `figure_eight`,
  `barbell`, `theta`, each a coefficient-row array; `total` is their exact sum.
- `boxes`: exactly four box objects, ordered n=1,2,3,4.
- `checks`: global/series check records in source traversal order; all per-box
  comparisons are retained within the boxes.
- `summary = {check_count, failed_count, failed_ids, status}`. Counts include
  every top-level and box check exactly once. `failed_ids` follows top-level
  then box-check order. `status` is `PASS` iff failed_count is zero, otherwise
  `FAIL`. Exit is 0 iff PASS and 1 on a completed report with failed predicates.
  Any process/program/parameter exception is a separate fatal failure, retained
  in raw stderr and exit status; it must not be relabelled as a complete report.

## Box object: exact keys and meanings

Scalar fields:

`n`, `declared_state_count`, `state_count`, `observed_maximum_period`,
`expected_maximum_period`, `observed_total_orbits`, `expected_total_orbits`.
The last expected value uses integer_or_ratio, all others are integers.

Array fields:

- `states`: complete state records in lexicographic order of
  `(u,v,f(1),...,f(n))`. The ID equals the array position.
- `edges`: exactly `[state_id, successor_id]` for every state, in state-ID order.
- `orbits`: every directly discovered cycle, starting at its least state ID,
  in increasing order of that least ID. No theorem period or inverse is used
  to discover these cycles.
- `groups`: every fixed labelled core/frozen-complement key, in lexical order
  of its canonical JSON key string. No orientation or edge-identity quotient
  is used to merge actual states.
- `core_catalog`: every distinct labelled core, in lexical order of its key.
- `observed_periods`, `expected_periods`: increasing lists of positive integers.
- `observed_period_orbit_counts`, `expected_period_orbit_counts`: period rows.
- `observed_core_period_orbit_counts`, `expected_core_period_orbit_counts`:
  core-period rows. The empirical core size is taken from a cycle member; the
  separate invariant/group checks detect any conflicting member assignment.
- `egf_extension_terms`: records `{s,p,core_coefficient:ratio,
  label_and_frozen_multiplier:integer,contribution:ratio}`, sorted by `(s,p)`.
  These retain every nonzero term of the period-refined extension formula.
- `total_orbit_formula_terms`: `{s,coefficient:ratio,multiplier:integer,
  contribution:ratio}`, one per s=1,...,n, in that order, using the separately
  written quadratic c_s formula rather than summing empirical core counts.
- `checks`: every state, orbit, group, extension-integrality and box check,
  in the order generated by the written source.

## State record: exact keys

`id`, `u`, `v`, `f`, `next`, `predecessors`, `inverse_formula_state_id`,
`orbit_id`, `orbit_position`, `preperiod`, `observed_period`, `core_id`,
`group_id`, `graph_multiset`, `active_component`, `attached_tree_vertices`,
`inactive_vertices`, `core`, `frozen_arrows`, `core_key`, `group_key`.

- `f` retains all n stored destinations. `next` is the direct successor ID.
  `predecessors` is the complete increasing list built from literal edges;
  it is not replaced by the inverse formula. `inverse_formula_state_id` is
  computed separately from equation (2) of the sealed proof.
- `orbit_id` identifies the discovered eventual cycle. `orbit_position` is
  its index in that cycle, or null for an unexpectedly transient state.
  `preperiod` is the directly discovered distance to the cycle. A successful
  report has preperiod zero everywhere. Tail states, if discovered, remain
  in `states`; the cycle-cover and preperiod predicates then fail.
- `observed_period` is the length of the discovered cycle, not a core formula.
- The active component is found from u in the whole undirected multigraph.
  The three vertex arrays are increasing; attached vertices are active
  component minus core, inactive vertices are its complement in [n].
- `frozen_arrows` contains every `[x,f(x)]` for x outside the core, sorted by x,
  including both attached trees and entirely inactive functional components.
- `core_key` is compact sorted-key JSON of `{vertices,edges}` for the core.
  `group_key` is compact sorted-key JSON of `{core:{vertices,edges},
  frozen_arrows}`. These are strings, not hashes, so the full key is recoverable.

## Core record: exact keys

`vertices`, `edges`, `edge_count`, `degrees`, `kind`, `parameters`, `branches`,
`chains`, `predicted_period`, `predicted_orbit_count`, `error`.

- `vertices`: increasing labels; `edges`: core edge_multiset;
  `degrees`: increasing `[vertex,degree]` rows; `edge_count` includes multiplicity.
- `kind`: `figure_eight`, `barbell`, `theta`, or `invalid` on a retained
  classification error. `error` is null for a valid classification, otherwise
  an explicit reason string; predicted fields are null for invalid cores.
- `parameters`: `{a,b}` for figure-eight, with a<=b; `{a,b,c}` for theta,
  with a<=b<=c; `{a,b,c}` for barbell, with a,b the cycle lengths at the lower/
  upper labelled branch and c the positive bridge length. It is empty if invalid.
- `branches`: increasing branch labels. `chains` contains records
  `{vertices:[labels],edge_ids:[integers],length:positive integer}`. The vertex
  walk includes both endpoints, repeated for a closed chain. Its orientation
  is the lexicographically smaller of forward and reverse vertex sequences;
  edge_ids reverse with it. Chains are sorted by `(vertices,edge_ids)`.
- Temporary edge IDs are 0-based occurrences in the full graph_multiset
  expanded in row order. They exist only for undirected chain extraction;
  they are not states, carrier edge labels, or extra orbit distinctions.
- Predicted period and predicted_orbit_count are the literal degenerate-case
  table values from the proof, not empirical counts. The latter is one or two.

## Remaining record types

- `orbit = {id,states:[state IDs],period,group_ids:[increasing group IDs],
  core_sizes:[increasing distinct sizes]}`. Both latter arrays normally have
  one member; a disagreement is retained and fails the group-invariance check.
- `group = {id,key,core_id,core,frozen_arrows,state_ids,orbit_ids,
  observed_periods,predicted_period,observed_orbit_count,predicted_orbit_count}`.
  State and orbit ID lists are complete and increasing. The observed orbit
  count is the number of distinct discovered cycles in this group, not its
  state count divided by a period. Exact coverage is checked separately.
- `core_catalog entry = {id,key,core,group_ids:[increasing group IDs]}`.

The schema and named equality records enable whole-output inspection; merely
matching its summary or hashes would not establish scientific agreement.
