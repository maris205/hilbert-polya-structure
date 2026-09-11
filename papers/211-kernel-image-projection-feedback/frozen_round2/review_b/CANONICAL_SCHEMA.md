# P211 B complete-output schema and reception obligations

SOURCE_ONLY specification, 2026-09-08 UTC. No scientific output exists at
this preparation gate. The name of this document specifies a possible
future canonical; it does not designate one. Root alone may adopt actual
accepted stdout under the separate initial/adoption/replay gates.

## 1. Representation and strict serialization

The prospective producer is `verify.py`, invoked only after exact root
binding, with an isolated, no-site, no-bytecode, unoptimized interpreter:
`/absolute/python -I -S -B /absolute/verify.py --parameters /absolute/parameters.json`.
This is an interface specification, not an authorization or a claim that
the displayed command has run. The sole input file opened by the producer
is the supplied parameter document. It writes only stdout, not files.

Successful stdout is exactly one UTF-8 JSON object, sorted object keys,
ASCII-escaped strings, separators comma and colon without added spaces,
`allow_nan=False`, followed by exactly one LF. Duplicate keys, unexpected
keys, missing keys, wrong scalar types, nonfinite numbers, trailing data,
or serialization drift are rejection conditions for later reception.
All actual object key sets are specified below; there are no optional keys.
Object ordering is lexical after serialization; array order is semantic.

Conventions: `int` means a JSON integer, never a boolean. All integers are
nonnegative except the explicitly signed Laurent exponents. `bool` means
true or false, never 0 or 1. `ID` is an integer in `[0,M-1]` for the current
carrier. A `mask` is an integer in `[0,2^n-1]`, with site j represented by
bit `2^(j-1)`. All `histogram` arrays have length n, nonnegative integer
entries, and sum n. They encode the entire map by repeating label j its
entry number of times; no image quotient or coarse orbit code replaces a
state. Every site list is strictly increasing and contained in `[1,n]`.

The carrier consists of all nondecreasing maps `[n] -> [n]`, including
nonextensive and non-top-fixing inputs. Histograms are enumerated by choosing
n-1 bar positions among 2n-1 positions and are required to be in increasing
lexicographic order with no duplicates. IDs are their zero-based positions.
`path_word` is the exact histogram spelling `'*'*h1 + '|' + ... + '*'*hn`;
it contains n stars and n-1 bars, including empty runs when an entry is 0.

`K` means right endpoints of nonempty domain fibres, obtained from positive
histogram cumulative sums. `V` means occupied output labels. For a source,
the outer retraction support is K and the completed inner support is
`A=V union {n}`. Thus a target's K and V correspond respectively to the
paper's W and Z; the schema deliberately does not silently swap this
coordinate convention. Composition is right factor first.

## 2. Complete top-level object: 15 keys

| Key | Exact type and semantics |
| --- | --- |
| `schema` | String `p211-b-complete-path-certificate-v1`. |
| `role` | String `P211_REVIEW_B`. |
| `parameters` | The complete exact parameter object in section 3, not a hash or selected subset. |
| `carrier_count` | Integer 7, equal to the length of `carriers`. |
| `carriers` | Seven complete carrier objects, in n order 1,2,3,4,5,6,7. |
| `total_states` | Integer 2353, equal to the sum of carrier state counts. |
| `total_targets` | Integer 2353; every state is retained as a possible labelled target. |
| `total_edges` | Integer 2353; exactly one outgoing arrow for every state. |
| `check_counts` | Object with exactly the 12 category keys in section 3; each value is the sum of that category over all carriers. |
| `carrier_check_total` | Integer sum of the 12 global category counts. |
| `hand_attack_checks` | Integer 3, equal to the number of separately asserted hand attacks. |
| `hand_boundary_attacks` | Exact ordered heterogeneous list specified in section 10. |
| `check_total` | `carrier_check_total + hand_attack_checks`. |
| `status` | String `FINITE_COMPLETE_PATH_CHECKS_PASS`, emitted only after all producer assertions succeed; it is not manuscript or all-n acceptance. |
| `scope` | String `original n=1..7 counterexample pressure; not all-n proof or manuscript acceptance`. |

## 3. Complete parameters object: 13 keys

`parameters.json` and the literal `EXPECTED_PARAMETERS` are both binding.
The source checks exact recursive types, object key membership, list order,
and values. Object insertion order is not asserted; serialization sorts it.

| Key | Exact value |
| --- | --- |
| `schema` | `p211-b-parameters-v1` |
| `n_values` | `[1,2,3,4,5,6,7]` |
| `carrier_sizes` | `[1,3,10,35,126,462,1716]` |
| `expected_total_states` | Integer 2353 |
| `carrier` | `all_nondecreasing_maps_[n]_to_[n]_without_initial_restrictions` |
| `representation` | `weak_composition_histograms_and_stars_bars_paths` |
| `graph_method` | `whole_carrier_successive_composition_tables_full_carrier_guard` |
| `inverse_method` | `kernel_first_last_kernel_cut_then_global_fixed_size_image_subsets` |
| `output_schema` | `p211-b-complete-path-certificate-v1` |
| `ordering` | `n_ascending_histogram_lexicographic_ids_kernel_masks_ascending_sources_by_id` |
| `serialization` | `JSON_sort_keys_ensure_ascii_compact_allow_nan_false_plus_single_LF` |
| `predicate_categories` | Exact ordered 12-string list below. |
| `excluded_claims` | Exact ordered four-string list below. |

Predicate category order and meaning:

1. `B01_carrier_and_encoding`: stars-and-bars census/order; each path
   decoding and histogram support reconstruction.
2. `B02_literal_histogram_update`: literal block-push successor belongs to
   the complete carrier and its block widths sum to n.
3. `B03_support_identity_and_normalization`: successor support inclusions,
   exact anchor identity, precise image language, extensivity and top fixing.
4. `B04_composition_certificate`: full identity/edge/stable tables, every
   table composition, and every first fixed equality/terminal tail.
5. `B05_fixed_recurrent_terminal`: complete projection fixed set, no other
   recurrence via full stable power, pointwise terminal and fixed criterion.
6. `B06_pointwise_clock`: every source's full time, and every image
   source's boundary radius time.
7. `B07_boundary_lifetimes`: every image source's entire labelled surviving
   support prediction at epochs 0 through R+1, against global graph tables.
8. `B08_image_iff_and_witness`: image language iff nonempty actual fibre,
   and the transposed-support explicit predecessor for every image target.
9. `B09_kernel_first_decoder`: every decoded histogram/support/rank branch;
   uniqueness and complete source-ID fibre equality; off-image empty fibres.
10. `B10_rank_branch_binomial_counts`: separate 0/1 branch counts globally
    for each target and for every kernel option, including zero branches.
11. `B11_laurent_identity_and_total_mass`: independent parity-convolution
    coefficients equal each branch and actual fibre; all-target total mass.
12. `B12_sharp_parity_and_boundaries`: full height, parity witness, exact
    table depth and genuine initial normalization step for n greater than 1.

The excluded-claims list, in order, is
`global_fibre_maximum_or_maximizers`, `basin_cardinality_formulas`,
`all_time_inverse_formulas`, `global_priority_or_no_factor_no_lift_theorems`.

The category counters increment once per successful call to the local
`check` function, not per boolean conjunct, state comparison, low-level
precondition or `insist`. No current numerical check count is claimed.
Three explicit hand-attack assertions are counted separately. Parameter
validation, the final total-state assertion, and internal algorithm
preconditions are mandatory but not silently added to the category census.

## 4. Complete carrier object: 18 keys

| Key | Type, ordering and meaning |
| --- | --- |
| `n` | Current positive integer from the exact list. |
| `state_count` | M from the corresponding declared size, also `binom(2n-1,n-1)`. |
| `records` | M complete state/target objects, increasing ID, section 5. |
| `successor_table` | M IDs; entry s is the literal T successor. |
| `composition_tables` | List of complete M-entry ID arrays: G0 identity, G1 successor table, then `G(t+1)[s]=G1[G(t)[s]]`, through the first duplicated stable final table. Exactly height+2 tables. |
| `first_fixed_epochs` | M integers; entry s is the first t for which `G(t)[s]=G(t+1)[s]`. |
| `terminal_table` | M IDs; the stable value of each source column. |
| `fixed_ids` | Increasing list of every ID with a self-arrow, exactly `2^(n-1)` projection maps. |
| `recurrent_ids` | Same increasing list; stable full power excludes all nonfixed cycles. |
| `image_ids` | Increasing list of all targets with nonempty predecessor lists. |
| `zero_fibre_ids` | Increasing complementary list; no zero target is omitted. |
| `height` | Maximum first fixed epoch over all M sources. |
| `height_formula` | Integer 0 at n=1, otherwise `(n+1)//2`. |
| `sharp_witness_id` | ID of the complete parity histogram specified in section 9. |
| `inverse_mass` | Sum of all actual fibre counts, equal to M. |
| `kernel_first_mass` | Sum of all nonnull atlas counts, also M. |
| `check_counts` | Exact 12-category object of nonnegative integer call counts. |
| `check_total` | Sum of this carrier's category counts. |

The global composition construction uses an M-iteration guard, not the
proved height or a supplied clock bound. If any source has no adjacent
equality after M compositions it raises, with no passing JSON emitted.
These are powers of T on the full carrier, not powers of an individual
monotone function f on `[n]`. No per-orbit traversal or reverse-BFS result
is imported. The complete tables, not just times or cycle counts, survive.

## 5. Complete state/target record: 22 keys

| Key | Type and semantics |
| --- | --- |
| `id` | Current ID. |
| `histogram` | Complete histogram at this ID. |
| `path_word` | Exact stars-and-bars spelling. |
| `whole_values` | Complete length-n nondecreasing value list decoded from the histogram. |
| `kernel_mask` | K, the positive cumulative right endpoints. |
| `image_mask` | V, the occupied labels. |
| `completed_image_mask` | `V OR 2^(n-1)`. |
| `literal_block_cells` | Nonempty list of four-key block-push objects, section 6, increasing inner block end. |
| `successor_id` | Corresponding successor-table entry. |
| `predecessor_ids` | Increasing IDs of every source whose literal arrow reaches this target; may be empty. |
| `fixed` | Bool, successor equals ID. |
| `recurrent` | Bool, equal to `fixed` after the complete-graph stabilization certificate. |
| `first_fixed_epoch` | Exact corresponding full-table first equality epoch. |
| `terminal_id` | Corresponding stable table entry. |
| `predicted_terminal_id` | ID of projection with support `K intersection (V union {n})`. |
| `predicted_time` | 0 if `K=V`, otherwise `1 + radius(Tf)`. |
| `image_criterion` | Bool, whether the boundary parser accepts this whole target. |
| `boundary_lifetimes` | Null exactly off image; otherwise the three-key object in section 7. |
| `survival_certificate` | Null exactly off image; otherwise complete ordered list in section 7. |
| `kernel_first_atlas` | Null exactly off image; otherwise complete six-key object in section 8. |
| `laurent_certificate` | Null exactly off image; otherwise complete four-key object in section 8. |
| `fibre_count` | Length of the complete `predecessor_ids` list. |

All four conditional fields have the same null/non-null boundary. In
particular, an extensive top-fixing but nonimage target remains a full
record with empty predecessor list, count 0 and four null fields.

## 6. Every literal block cell: four keys

`inner_block_end` is a site a of completed support A. `block_width` is
a minus the previous A site, taking previous=0 initially.
`outer_suffix_mask` is the integer `K >> (a-1)`, strictly positive.
`assigned_output` is the first K site at or above a, equivalently
`a + bit_length(suffix & -suffix) - 1`. All are integers. The widths sum
to n; accumulating each width in its assigned output bin gives the
complete successor histogram. The cells retain the literal support
composition independently of the closed-time and inverse predictions.

## 7. Every boundary and survival object

An accepted target's `boundary_lifetimes` has exactly:

- `anchor_mask`: `K AND V`, including n.
- `intervals`: ordered list of two-key objects, one per increasing anchor.
  `anchor` is that site; `tokens` is its increasing list of strict sites
  between the previous anchor (or 0) and this anchor.
- `radius`: maximum token death epoch, or 0 when there are no tokens.

Each token has exactly `site` (positive integer), `initial_role` (string
`K` or `V`), and `death_epoch` (positive integer). Ignoring empty sites,
the target support word must be a concatenation of `(K V)* B`, where B
is a common anchor, the final B is n, and strict tokens alternate starting
with K and ending with V. If a strict interval has 2r tokens indexed
j=1,...,2r, token j dies at `min(j,2r+1-j)`. All anchors persist.

`survival_certificate` has radius+2 entries, in epochs 0,...,radius+1.
Each entry has exactly `epoch`, `kernel_mask`, `image_mask`, `state_id`.
A strict token survives iff epoch is less than its death epoch; its role
is swapped iff the epoch is odd. Common anchors enter both masks. The ID
is decoded from these entire masks and is checked against the entire
global composition table at that epoch, including a repeated stable epoch.

## 8. Every inverse and Laurent object

The target-only `kernel_first_atlas` has exactly six keys:

- `gaps`: increasing target-rank list of five-key gap objects below.
- `free_mask`: bit union of all gap masks.
- `kernel_options`: all subsets of `free_mask`, ordered by increasing
  integer mask, including the empty subset and options with zero counts.
  Each is the six-key option object below.
- `branch_counts`: length-two integer list `[N0,N1]`, separate balances.
- `count`: integer N0+N1.
- `descriptions`: all seven initial decoder fields plus attached source
  ID, hence eight keys per description below, sorted strictly by source ID.

For target endpoint/image pairs `(w_i,z_i)`, with `z_0=0`, each gap is
`D_i={z_(i-1)+1,...,w_i-1}` and has exactly:
`previous_output` = z_(i-1); `target_end` = w_i; `target_output` = z_i;
`sites` = the entire increasing D_i; `mask` = its exact bit mask. Empty
gaps are retained. These are target coordinates, not a scan over sources.

Every kernel option has exactly:

| Key | Meaning |
| --- | --- |
| `extra_kernel_mask` | A chosen subset L of the full free mask. |
| `rightmost_kernel_by_gap` | List q_i, where q_i is max of L in D_i, or z_(i-1) if empty. |
| `eligible_image_mask` | Union E of `{q_i+1,...,w_i-1}` over all gaps. |
| `kernel_extra_count` | Integer a, the cardinality of L. |
| `eligible_image_count` | Integer e, the cardinality of E. |
| `branch_binomial_counts` | `[binom(e,a),binom(e,a+1)]`; binomial is 0 for an out-of-range chosen size. |

For each option and balance delta=0,1, choose an `(a+delta)`-element
subset M of E. The algorithm generates these subsets lexicographically
as increasing site tuples, but the final retained descriptions are sorted
by source ID. Each description has exactly eight keys:
`source_histogram` (complete histogram), `source_kernel_mask` (`Z union L`),
`source_image_mask` (below), `completed_image_mask` (`W union M`),
`extra_kernel_mask` (L), `extra_image_mask` (M), `balance` (integer 0 or 1),
`source_id` (attached only after target-only reconstruction).
For balance 0 the source image is its completed image; for balance 1
remove n. Equal source support ranks and nonemptiness are required.
The decoder itself uses no actual arrow table, actual incoming lists,
source scan or author/A implementation. Outer checks attach IDs and
compare every generated source, no duplicates, against the full actual
predecessor list. Every kernel option retains both zero/nonzero branch
counts and is separately checked against its descriptions.

`laurent_certificate` has exactly four keys:

- `gap_factors`: one coefficient-pair list per retained gap, same order.
  For a gap of length d, this list contains every exponent e=-d,...,d
  in ascending order paired with
  `sum(binom(d,s) for s=abs(e),abs(e)+2,...,d)`.
- `product`: all ascending signed exponent/integer coefficient pairs of
  the convolution of all factors, including coefficient zero if produced.
  Each pair is exactly a length-two list; no object or coefficient map is
  substituted. For zero total gap length the product is `[[0,1]]`.
- `branch_counts`: product coefficients at exponents 0 and 1, missing
  exponents interpreted as 0, separately equal to atlas N0 and N1.
- `count`: sum of those two coefficients, equal to the whole actual fibre.

All factor exponents are present, even if a coefficient vanishes. This
parity-sum construction is separate from the kernel-first binomial sum
and from the source-ID actual incoming census. Neither coefficient
construction is credited as a new manuscript theorem by the B route.

## 9. Exact parity witness

At n=1 the histogram is `(1)`. For odd n greater than 1, put count 2 at
odd labels below n, count 1 at n, and 0 elsewhere. For even n, put count 2
at odd labels below n and 0 elsewhere, including n. The full histogram's
ID and graph time are retained, not only a claimed height. For n greater
than 1 its first map value is 1 and its literal successor's first value
is 2, so the initial normalization step is explicitly nontrivial.

## 10. Exact ordered hand attacks

The list contains exactly these three objects, with no additional keys:

1. `name` = `right_factor_first_and_initial_time`; `n` = 3;
   `source_histogram` = `[2,0,1]`; `forward_histogram` = `[0,1,2]`;
   `reversed_product_histogram` = `[0,0,3]`; `full_time` = 2.
2. `name` = `extensive_top_fixing_is_not_image_iff`; `n` = 4;
   `target_histogram` = `[0,1,1,2]`; `fibre_count` = 0.
3. `name` = `constant_three_rank_branches`; `n` = 3;
   `target_histogram` = `[0,0,3]`;
   `predecessor_histograms` = `[[0,0,3],[0,1,2],[0,3,0],[3,0,0]]`;
   `branch_counts` = `[2,2]`.

These constants are hand-derived attacks. They become finite execution
evidence only if an authorized successful producer actually emits them.

## 11. Reception is separate from production

Root's later receiver must bind this entire exact source, parameters,
schema and all transitive scientific helpers (there are none besides
standard-library imports), read the actual native initial receipt, verify
the full exact output schema and every saved field, preserve raw stdout
and stderr, and then decide whether to adopt the actual stdout bytes.
Schema-level counters or a hash match alone are not whole-output semantic
reception. Independent replay remains a separate role-specific binding
with exact bytes, status, source/input pins and complete equality checks.

Nothing in this source-only package claims a producer invocation, import,
compiled module, canonical, runtime acceptance, strict replay, build
acceptance, review PASS, completed Round2, or permission to enlarge the
original seven carriers.
