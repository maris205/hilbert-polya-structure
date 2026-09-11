# Review A complete-graph output schema and parameter contract

Status: PREPARATION ONLY. This describes future output, not an executed
transcript. No `CANONICAL.json` has been created by this reviewer.

The capsule consists only of `verify.py` and `parameters.json`. The exact
interface is `verify.py --parameters ABS_PARAMETERS`; the parameter path
must be absolute. The approved infrastructure supplies the isolated Python
invocation and records its complete dependency/runtime key separately.
Ordinary imports are exactly `itertools`, `json`, `math`, `sys`. There are
no local helper imports, environment reads, subprocesses, network calls,
clocks, randomness, output files or dynamic code loading. The only explicit
file read in the scientific program is the one parameter file. Every
parameter field is required and the whole object must equal the literal
specification in the code; `n_values` and the expected total have explicit
integer-type checks. No command-line cutoff or alternate mode exists.

## Enumeration and independent representation

For each of the seven original carriers n=1,...,7, vertices are all length-n
nondecreasing value tuples over 1,...,n, in lexicographic order. Local vertex
IDs are zero-based indices. The total is 2,353 vertices, and those same
vertices are all potential targets, including every zero fibre. Edges are
computed once from whole-function run ends and two literal ceiling tables.
No temporal or inverse formula participates in computing these edges.

The full reverse adjacency is constructed by transposing those edges.
Indegree pruning discovers the recurrent remainder. Cycles are then traced
without assuming they are fixed, and a reverse breadth-first traversal
assigns every vertex's distance and cycle component. Each complete orbit
is also retained as an independent cross-check of those graph distances.
The image, peeling, terminal, sharp-time, and inverse predictions are only
compared after that complete graph exists. The inverse decoder enumerates
ordered ternary words in target gaps, not sources filtered by a forward
equation. A separate binomial/Laurent multiplication checks its counts.

## Exact JSON wire format

Successful stdout is exactly one ASCII JSON object followed by one LF,
serialized with `sort_keys=True`, `separators=(",", ":")`, and
`ensure_ascii=True`. There is no pretty-print whitespace, timestamp,
runtime path, platform field or nondeterministic set iteration in stdout.
All counts, labels, IDs and exponents are integers; truth values are JSON
booleans; the absent image-only evidence below is JSON null. Object key
order is lexicographic. All other array orders are specified below.
An assertion/parameter failure raises a real exception; it does not emit
the successful document. Infrastructure must preserve any partial/raw
streams and nonzero exit instead of installing a canonical from them.

The top-level object has exactly:

| Key | Meaning |
| --- | --- |
| `schema` | Literal `p211-a-complete-graph-v1` |
| `role` | Literal `P211_REVIEW_A` |
| `parameters` | Complete exact decoded parameter object |
| `carriers` | Seven carrier objects, increasing n |
| `total_vertices`, `total_targets`, `total_edges` | Each 2,353 on success |
| `check_total` | Sum of all carrier `check_total` values; not pre-invented |
| `verdict` | Literal `FINITE_GRAPH_CHECKS_PASS`, emitted only after actual checks |
| `scope` | Exact code literal restricting the result to finite pressure, not all-n proof or manuscript acceptance |

A carrier object has exactly:

| Key | Meaning/order |
| --- | --- |
| `n`, `vertex_count` | Chain size and binomial carrier size |
| `rows` | One row for every vertex/target, increasing ID |
| `cycles` | Cycles ordered by minimum vertex; each starts at its minimum and follows outgoing edges; on success each has length one |
| `indegree_pruning_order` | Initial zero-indegree IDs increasing, then newly exposed IDs appended in deterministic queue order |
| `reverse_breadth_first_order` | Cycle vertices first in `cycles` order, then previously unclassified incoming vertices in increasing incoming-ID order |
| `image_vertex_ids`, `zero_fibre_vertex_ids` | Increasing IDs determined from full reverse adjacency |
| `height`, `height_prediction` | Observed maximum graph distance and the stated parity formula |
| `height_attaining_vertex_ids` | Every graph vertex attaining that distance, increasing IDs; a finite census, not an added theorem |
| `specified_parity_witness_id` | The manuscript's explicit witness, with n=1 separated |
| `check_counts`, `check_total` | Name-to-success-count map and its sum |

Each row has exactly:

| Key | Meaning/order |
| --- | --- |
| `id`, `values` | Local ID and the complete length-n function tuple as an array |
| `kernel_ends`, `image_values` | Increasing run ends and corresponding increasing distinct values |
| `successor_id`, `predecessor_ids` | Literal outgoing edge and every incoming source ID, increasing |
| `cycle_index`, `graph_depth` | Index in `cycles`; reverse-BFS distance to that cycle |
| `orbit_with_repeated_terminal` | Start ID, every literal forward iterate up to first repeat, and that repeated terminal once; a fixed point has `[id,id]` |
| `terminal_id`, `terminal_support_prediction` | Graph-derived terminal ID; increasing predicted common support |
| `image_criterion`, `time_prediction` | Exact inequality predicate; full-carrier time prediction with fixed sources separated |
| `image_intervals`, `image_radius`, `peeled_successor_id` | Image-only labelled interval evidence, maximum strict-pair length and predicted next ID; null for off-image targets |
| `inverse_atlas` | Complete image-target object described next; null for off-image targets, whose `predecessor_ids` is exactly empty |

`image_intervals` is in increasing-anchor order and has one object per
anchor, exactly `anchor` (integer) and `strict_labels` (the increasing
alternating endpoint/value list before it). Empty strict lists remain
explicit, including an empty first interval or consecutive anchors.

An `inverse_atlas` object has exactly:

| Key | Meaning/order |
| --- | --- |
| `gaps` | Ordered D_i, each as its full increasing list of free integer sites; empty gaps are empty arrays |
| `gap_polynomials` | One Laurent coefficient table per gap |
| `product_polynomial` | Complete product coefficient table |
| `balance_counts` | Coefficients for exponents zero and one, in that order |
| `predicted_count` | Sum of those two coefficients |
| `descriptions` | One description for every decoded predecessor, increasing source ID |

A coefficient table is an array of `[exponent, coefficient]` rows in
strictly increasing exponent order; negative exponents are ordinary signed
integers. No zero coefficient is stored. Empty-gap polynomial is `[[0,1]]`.
A predecessor description has exactly `source_id`, `gap_words`, `X`, `A`,
`Y`, `balance`. The three supports are increasing integer arrays. Each
`gap_words[i]` has length `len(gaps[i])`; colours 0,1,2 mean neither, extra
X, extra A respectively. Deleting zero colours leaves all 1s before all 2s.
`balance` is zero or one and uniquely determines the recovered Y. The code
compares the entire decoded source-ID list with the graph's incoming list,
checks injection, total fibre count and both rank-branch counts separately.

## Predicate census and output acceptance

The `check_counts` keys are the exact names of `check(...)` calls in the
complete source, not a manually predicted run count. They cover carrier
membership/size/order, graph cycle and projection census, edge and inverse
mass, support reconstruction/containments/common anchors, exact image iff,
first-image normalization, terminals, full and image times, complete orbits,
labelled peeling, image witnesses, inverse injection/list equality/Laurent
counts/rank branches/zero fibres, height and parity witnesses. Preconditions
inside helpers and parameter checks also raise on failure but are not
included in that top-level named count. Accordingly `check_total` is not
claimed to count every comparison or every low-level invariant.

Root must read all fields and full code before any scientific invocation,
then issue an exact A-specific initial binding. Real initial stdout and
runtime evidence are received before root alone exclusively adopts absent
canonical bytes. A distinct exact binding then supplies the required strict
pair and three raw native comparisons. This schema is deliberately not the
author's schema, and A stdout is not expected to equal author canonical.
