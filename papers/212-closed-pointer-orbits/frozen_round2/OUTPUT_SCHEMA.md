# P212 complete output schema, version 1

Status: SOURCE_ONLY interface specification. No instance of this output has
been produced, parsed or accepted during source preparation. This document
specifies the complete prospective stdout of [verify.py](verify.py); it is
not a canonical output, execution receipt, independent review or PASS.
The exact input is [PARAMETERS.json](PARAMETERS.json). The execution sequence
and the separate root authorization gates are in [OUTPUT_PLAN.md](OUTPUT_PLAN.md).

## 1. Wire format and types

One successful completion emits exactly one ASCII JSON object followed by
one LF byte. Serialization uses `sort_keys=True`, `separators=(",", ":")`,
`ensure_ascii=True`, `allow_nan=False`; no progress text, timestamps, hashes,
filesystem paths, host identities or nondeterministic set iteration appear on stdout.
Object member names are sorted lexicographically on the wire. This document's
field lists define exact sets, not a second required insertion order.

All named objects below have exactly the listed fields, with no optional
members. Arrays are complete, including empty arrays and zero counts where
specified. Integers and Booleans are different types. `null`, floating-point
numbers, NaN and infinities do not occur in a completed output. No rational
number is rounded. The syntax aliases used below are:

| Alias | Exact representation |
|---|---|
| `Int` | JSON integer, never a Boolean |
| `Nat` | nonnegative `Int` |
| `Label` | integer in `1..n` for a carrier, or `1..s` for a canonical core catalogue |
| `Rat` | two-element `[numerator,denominator]`, signed integer numerator, positive integer denominator, coprime, zero as `[0,1]` |
| `Poly` | array of `[period,numerator,denominator]`, positive periods strictly increasing, nonzero reduced rational coefficients only |
| `Series` | array of `[core_size,period,numerator,denominator]`, nonzero reduced coefficients only, sorted by `(core_size,period)` |
| `Matrix(k)` | `k` rows of `k` nonnegative integers, symmetric; a diagonal entry counts loops once, its contribution to degree is twice its value |
| `State` | object with exactly `u:Label`, `v:Label`, `f:[Label]`; `f` has length `n` and position `a-1` is `f(a)` |
| `FlatState` | the length `n+2` array `[u,v,f(1),...,f(n)]`; used only inside predicate values |
| `CoreKey` | `[core_vertices,upper_triangle,frozen_targets]`; the first list is increasing, upper-triangle order is row-major pairs `a<=b` on those vertices, and frozen targets follow the increasing complementary source labels |

Matrices have no edge IDs. In particular a multiplicity of three between two
vertices is one integer, not three named objects. A path retains its vertex
sequence; equal direct paths are identical sequences. Vertex labels are not
quotiented. The carrier contains every function, including disconnected
functional graphs, and every ordered register pair, including `u=v`.

Parameters are read with duplicate-key rejection and explicit rejection of
floating-point and nonfinite tokens. The complete decoded object is compared
with the source's fixed object by canonical JSON, so changing a field, field
set, ordered list, integer to Boolean, cutoff or textual convention fails.
Only input JSON whitespace/member order are semantically irrelevant; the
future runtime binding must separately pin the actual raw parameter bytes.

## 2. Top-level object

The top-level object has exactly these 12 fields:

| Field | Value/type |
|---|---|
| `schema` | literal `"p212-full-output-v1"` |
| `parameters` | exact 14-field object in `PARAMETERS.json` |
| `role` | literal `"author_verifier_not_independent_review"` |
| `method` | literal `"literal_state_graph_vs_multiplicity_catalogue_observable_anchors_and_Fraction_series"` |
| `excluded_claims` | the four exact strings, in source `EXCLUDED_CLAIMS` order |
| `core_catalogues` | four `CoreCatalogue` objects, in `s=1,2,3,4` order |
| `carriers` | four `Carrier` objects, in `n=1,2,3,4` order |
| `series` | one `SeriesReport` |
| `coverage_limits` | three `CoverageLimit` objects in the order below |
| `predicates` | every `Predicate`, in actual append/evaluation order, with consecutive IDs from zero |
| `predicate_census` | one `PredicateCensus` for every declared predicate name, in source `PREDICATES` order, including any zero count |
| `summary` | one `Summary` |

The excluded-claim strings, in order, are:

1. `No finite computation proves the all-n theorem.`
2. `No finite observation of the three first-size 5/6/5 families is claimed.`
3. `No independent manuscript review, global novelty, priority, or publication acceptance is claimed.`
4. `Known kernel, inverse, zero preperiod, unit fibres, invariant, and standard counting are not new axes.`

`Summary` has exactly `carrier_sizes:[1,2,3,4]`, `state_count:Nat`,
`orbit_counts:[Nat]` of length four in carrier order, `predicate_count:Nat`,
`failure_ids:[Nat]` increasing, and `passed:Boolean`.
`predicate_count` equals the complete predicate array length. `failure_ids`
is exactly the IDs whose `passed` is false; summary `passed` means that list
is empty. It is only a finite author-verifier outcome.

## 3. Independent labelled-core catalogue

`CoreCatalogue` has exactly `s:Int` and `entries:[CoreEntry]`.
The enumeration is independent of the state graph: distribute exactly
`s+1` edges among the `s(s+1)/2` upper-triangle pairs; keep precisely the
connected matrices with every degree at least two. Entries follow increasing
lexicographic upper-triangle vectors; IDs are consecutive from zero within
each `s`. No graph-isomorphism quotient is taken.

`CoreEntry` has exactly `catalogue_id:Nat`, `s:Int`, `matrix:Matrix(s)`,
`upper:[Nat]` of length `s(s+1)/2`, and `description:Description`.

`Description` has exactly:

- `family`: one of `figure_eight`, `barbell`, `theta`;
- `row`: one of the seven row strings in the table below;
- `branches`: increasing branch labels, one for a figure-eight, two otherwise;
- `paths`: two paths for a figure-eight, three otherwise, each a complete
  vertex sequence including its endpoints;
- `lengths`: corresponding positive edge lengths, each `len(path)-1`;
- `predicted_period`: positive integer from the table;
- `predicted_orbit_count`: integer 1 or 2, from observable decoration classes.

Closed paths start/end at their branch and use the lexicographically smaller
of their two directions. Open paths are directed from the smaller-labelled
branch to the larger. Figure-eight cycles are sorted lexicographically.
Barbell paths are `[cycle_at_smaller_branch,cycle_at_larger_branch,bridge]`.
Theta paths are sorted lexicographically, retaining repeated direct paths.
No temporary incidence identity survives this representation.

| `row` | Condition | Period | Orbit classes | First core size |
|---|---|---:|---:|---:|
| `figure_eight_double_loop` | `a=b=1` | 1 | 1 | 1 |
| `figure_eight_short_nontrivial` | `a,b<=2`, not both 1 | `a+b` | 1 | 2 |
| `figure_eight_long` | `max(a,b)>=3` | `2(a+b)` | 2 iff both long, else 1 | 3 |
| `barbell_short` | `a,b<=2` | `a+b+2c` | 1 | 2 |
| `barbell_long` | `max(a,b)>=3` | `2(a+b+2c)` | 2 iff both long, else 1 | 4 |
| `theta_triple_direct` | all three lengths 1 | 2 | 1 | 2 |
| `theta_other` | any nondirect path | twice the sum of lengths | 1 iff at least two direct paths, else 2 | 3 |

These row labels are complete coarse degenerations. Observation of a row is
not observation of every all-parameter subclass within it.

## 4. Literal carriers, state arrows, invariants and orbits

`Carrier` has exactly 14 fields: `n`, `state_count`, `states`, `orbits`,
`groups`, `row_coverage`, `period_polynomial_observed`,
`period_polynomial_expected`, `extension_contributions`, `orbit_count`,
`period_set`, `maximum_period`, `fixed_state_ids`, and `fixed_iterates`.
`n` is 1, 2, 3 or 4; `state_count` is a `Nat`.
Both period polynomials are `Poly`; `orbit_count` is a `Nat`; `period_set` is
the increasing list of observed periods; `maximum_period` is its maximum.
`fixed_state_ids` is an increasing complete list of fixed states.

`states:[StateRecord]` contains every state once in lexicographic flat-state
order. The expected sizes are 1, 16, 243 and 4096, totaling 4356, but these
numbers are predictions until an authorized run actually returns them.
`StateRecord` has exactly 9 fields:

- `id:Nat`, the zero-based position in this carrier;
- `state:State`;
- `successor_id:Nat`, the ID of the simultaneous literal update;
- `inverse_id:Nat`, the ID of the separately computed inverse formula;
- `inverse_state:State`, the full inverse, not only its ID;
- `preimage_ids:[Nat]`, all actual graph predecessors in source-ID order;
- `orbit_id:Nat`, reference into this carrier's orbit array;
- `group_id:Nat`, reference into this carrier's fixed-core/frozen-map groups;
- `invariant:Invariant`.

`Invariant` has exactly `matrix:Matrix(n)`, `active_vertices:[Label]`,
`inactive_vertices:[Label]`, `pruning:[[Label,Label]]`,
`core_vertices:[Label]`, `core_matrix:Matrix(s)`, `core_degrees:[Int]`,
and `frozen_complement:[[Label,Label]]`. Vertex lists are increasing.
The core matrix rows/columns follow `core_vertices`, not all `1..n`.
The invariant matrix includes all stored edges and the extra register edge.
The active component is computed after adding that register edge.
Pruning removes the current smallest degree-one vertex at each step; each
pair records `[removed_vertex,its_unique_remaining_neighbour]` in that order.
The complement contains all non-core source labels, active pruned trees and
inactive components alike, in source-label order with their actual targets.

`orbits:[Orbit]` are ordered by smallest state ID; IDs are consecutive.
`Orbit` has exactly `id`, `representative_state_id`,
`state_ids_in_time_order`, `preperiod`, `period`, `group_id`, and `anchors`.
The first two and `group_id` are `Nat`; `preperiod` is integer zero;
`period` is a positive integer. `state_ids_in_time_order` starts with the
least state ID on that orbit and follows actual successor arrows until,
but excluding, the repeated initial state. This ordered sequence establishes
the observed minimal period directly: no state repeats before closure.
No period prediction controls the traversal stopping rule.

`anchors:[OrbitAnchor]` retain every phase satisfying the prescribed anchor
condition. `OrbitAnchor` has exactly `phase:Nat`, `state_id:Nat`,
`raw_decoration:RawDecoration`, and `class:DecorationClass`. Anchor records
follow increasing phase, and `state_id` equals the orbit's phase entry.

## 5. Fixed-core/frozen-map groups and observable decorations

Groups are independently generated in nested order: core size increasing,
core label subset lexicographic, canonical matrix catalogue ID increasing,
and full complementary target tuple lexicographic in `[n]^(n-s)`.
Every complement map is retained, not just a connected or forest-only case.
The empty complementary map occurs exactly once for `s=n`.

`Group` has exactly the following 13 fields: `id:Nat`, `s:Int`,
`catalogue_id:Nat`, `core_vertices:[Label]`, `core_matrix:Matrix(s)`,
`description:Description`, `frozen_complement:[[Label,Label]]`,
`state_ids:[Nat]`, `orbit_ids:[Nat]`, `expected_anchors:[ExpectedAnchor]`,
`observed_anchor_state_ids:[Nat]`, `expected_classes:[DecorationClass]`,
and `observed_classes:[ObservedClass]`. All ID lists are increasing.
`catalogue_id` refers to the catalogue for this `s`; `description` relabels
that canonical core by the increasing actual core label subset.

`ExpectedAnchor` has exactly `state:State`, `state_id:Nat`,
`raw_decoration:RawDecoration`, and `class:DecorationClass`.
Expected anchors are constructed from graph chains/orientations and the
frozen map without invoking the update map, deduplicated by the entire
literal state, and ordered by lexicographic flat state. They are not copied
from observed anchor states. Their IDs are resolved against the full carrier.

For a figure-eight the anchor is the shared branch with the extra arrow
starting its first prescribed cycle. For a barbell it is the smaller branch
with the extra arrow starting the bridge toward the larger branch. The two
cycle orientations are read from actual branch departure destinations. A
cycle of length 1 or 2 has bit zero only; a longer cycle has bit zero for
the canonical direction and one for its reversal.
`RawDecoration` is then exactly the length-two bit list `[b1,b2]`.
`DecorationClass` is the object `{"kind":"cycle_orientation_class",
"value":[b1,b2]}`, where `value` is the lexicographically least of the bits
and their simultaneous reversal (short-cycle bits stay zero).

For theta, the anchor is the smaller branch. Each path's token is its ordered
internal-vertex list from the smaller branch to the larger; direct paths
all have the identical empty token `[]`. `RawDecoration` is exactly
`[extra_token,stored_token,incoming_token]`. The first two are decoded from
the actual extra/stored destinations and removed from the token multiset;
the remaining token is incoming. The class is the object
`{"kind":"theta_cyclic_order","value":[token1,token2,token3]}`, with the
lexicographically least cyclic rotation of the raw triple. Reversal is
not taken in this quotient. Repeated direct tokens are indistinguishable,
so there is no hidden division by three factorial or fictitious edge label.

Expected class lists are sorted by the internal signature order (kind, then
value); all classes in one group have the same kind. `ObservedClass` has
exactly `class:DecorationClass` and `orbit_ids:[Nat]` increasing, with one
record per observed class in signature order. The central bijection check
compares the complete list of observed class-to-orbit sets with the complete
list of singleton actual orbit IDs. This rejects a class split between
orbits, distinct classes merged into one orbit, extra classes, missing
classes, and orbits that never meet a prescribed anchor. Exact expected and
observed anchor literal-state sets are compared separately.

`row_coverage:[RowCoverage]` has all seven rows in table order, including
zero-count rows. `RowCoverage` has exactly `row`, `group_ids`,
`first_core_size`, `observed_present`, `expected_present`, `group_count`,
`orbit_count`, and `state_count`. The row is a table string; IDs are increasing;
counts/first size are integers; presence flags are Booleans. Expected presence
means `n>=first_core_size`, not coverage of every subclass of the row.

## 6. Rational-series and complete census records

`extension_contributions:[ExtensionContribution]` has one record for every
`s=1..n`, in increasing order. Its exact fields are `s:Int`,
`falling_factorial:Int`, `complement_map_count:Int`, `multiplier:Int`,
`core_coefficients:Poly`, and `contribution:Poly`. The multiplier is
`(n)_s*n^(n-s)` and every contribution is the exact rational product with
the `t^s` core polynomial. No integer rounding is permitted.

`FixedIterate` has exactly `k:Int`, `fixed_state_ids:[Nat]`,
`observed_count:Nat`, and `expected_count:Rat`. Every `k` from 1 through
the predicted maximum period for that carrier is included, in increasing
order. Fixed-state IDs are found by literal repeated successor application,
not by assigning an orbit formula to a state; expected count is the
period-divisor sum. This remains a standard corollary, not a third axis.

`SeriesReport` has exactly `max_core_size:4`, `pieces:[SeriesPiece]`,
`total_terms:Series`, `coefficient_checks:[CoefficientCheck]`, and
`control_provenance:String`. The exact provenance string is
`Deductive rational expansions in the admitted MATHEMATICAL_AUDIT.md; not prior executed results.`
Pieces occur in family order `figure_eight,barbell,theta`; each `SeriesPiece`
has exactly `family` and `terms:Series`.

The expected side uses sparse exact `Fraction` arithmetic truncated only in
core degree `s<=4`. There is no independently chosen period truncation.
Writing `x=tq^2`, `Q=x/(1-x)`, and `D=(1-x)^(-2)-(1+x)^2`, the three
expressions evaluated are:

\[
\begin{aligned}
C_8&=tq+t^2q^3+\tfrac12t^3q^4+\tfrac14tq^4D,\\
C_B&=\frac{t^2q^4(1+tq)^2}{2(1-tq^2)}+
       \frac{t^2q^8D}{4(1-tq^4)},\\
C_\Theta&=\tfrac12t^2q^2+
\tfrac12t^2q^6(Q+Q^2+\tfrac13Q^3).
\end{aligned}
\]

The source constructs these by polynomial addition, multiplication,
geometric series and rational scaling. It does not generate them by fitting
observed orbit totals. Conversely observed core coefficients come from actual
orbits in the full `s` carrier whose core uses all `s` labels, divided by
`s!` solely for the EGF normalization. Before this stage in a future run,
orbit equivalence and class numbers will already have been compared through
the separately constructed complete anchor sets within the author program.

`CoefficientCheck` has exactly `s:Int`, `families:[FamilyCoefficient]`,
`observed_coefficients:Poly`, `expected_coefficients:Poly`,
`hand_control:Poly`, `univariate_coefficient:Rat`, `closed_coefficient:Rat`,
`period_weighted_coefficient:Rat`, and `labelled_orbit_counts:Poly`.
There are four checks in increasing `s`; the family list always has all
three families, including empty coefficient lists. `FamilyCoefficient` has
exactly `family`, `observed_coefficients:Poly`, `expected_coefficients:Poly`.
The univariate rational identity is checked through degree four against
`(t-t^2+t^4/2-t^5/12)/(1-t)^3`; the negative degree-five numerator term has
no coefficient effect within this cutoff. The closed coefficients are
`1,2,(5s^2+s+24)/24` in the stated cases. The period-weighted control is
`s^2(s+1)/2`. No degree-five state/core enumeration is performed.

The four `CORE_CONTROLS` and four `CARRIER_CONTROLS` in source are exact
deductive controls transcribed from the accepted mathematical audit. The
prospective carrier orbit totals 1, 8, 81, 1036 are not presented as actual
results of this new verifier before an authorized run.

## 7. Predicates, values and coverage limits

`Predicate` has exactly `id:Nat`, `name:String`, `scope:String`,
`observed:JSONValue`, `expected:JSONValue`, and `passed:Boolean`.
Values use only the integer/Boolean/string/array/object representations above,
with exact canonical JSON comparison. Each comparison is retained, not just
a total or digest. Tuple-valued internal keys/states become JSON arrays.
`PredicateCensus` has exactly `name:String`, `checks:Nat`, `failures:Nat`.
The names and value meanings below are exhaustive and ordered exactly as in
the source predicate declaration:

| Name | Observed / expected value |
|---|---|
| `carrier_size` | state count / `n^(n+2)` |
| `successor_in_carrier` | membership Boolean / true |
| `inverse_in_carrier` | membership Boolean / true |
| `inverse_after_forward` | inverse of actual forward `FlatState` / original `FlatState` |
| `forward_after_inverse` | forward of inverse `FlatState` / original `FlatState` |
| `unit_fibre` | complete predecessor ID list / singleton inverse ID list |
| `invariant_matrix` | successor's full matrix / original matrix |
| `active_component_bicyclic` | active edge count / active vertex count plus one |
| `registers_in_core` | two membership Booleans / `[true,true]` |
| `core_bicyclic` | core edge count / core vertex count plus one |
| `core_minimum_degree` | minimum-degree-at-least-two Boolean / true |
| `core_stored_arrows_internal` | per-core-vertex membership Booleans / all true |
| `frozen_complement` | successor's entire complement map / original complement map |
| `core_key_invariant` | successor's `CoreKey` / original `CoreKey` |
| `pruned_arrows_toward_core` | removed vertices with actual pointer targets / exact pruning pairs |
| `orbit_closure` | actual first revisited state ID / seed ID |
| `orbit_no_preperiod` | first revisited local position / zero |
| `orbit_partition` | sorted complete actual orbit state IDs / `0..state_count-1` |
| `orbit_exact_period` | actual distinct cycle length / structural predicted period |
| `orbit_group_constant` | sorted distinct complete keys on orbit / singleton expected key |
| `orbit_anchor_nonempty` | actual nonempty-anchor Boolean / true |
| `group_catalogue_complete` | sorted full observed keys / sorted independently constructed keys |
| `group_anchor_states` | sorted `[FlatState,raw_decoration,DecorationClass]` observed anchors / independently constructed anchors |
| `group_decoration_classes` | sorted observed class list / independently constructed class list |
| `group_orbit_decoration_bijection` | sorted class-to-orbit ID lists / sorted singleton actual orbit IDs |
| `group_orbit_count` | actual number of complete orbits / predicted 1 or 2 |
| `group_periods` | periods in actual orbit-ID order / predicted period repeated equally many times |
| `core_catalogue_graph_count` | number of actual full-core groups / number of independently enumerated matrices |
| `core_catalogue_orbit_census` | actual pure-core orbit count for that matrix / predicted 1 or 2 |
| `core_series_family` | actual core-orbit `Poly` divided by `s!` / exact rational family `Poly` |
| `core_series_total` | summed actual core `Poly` / summed rational `Poly` |
| `core_series_hand_control` | calculated rational `Poly` / audit's deductive core control |
| `univariate_rational_identity` | q=1 coefficient `Rat` / coefficient of explicit rational univariate function |
| `univariate_closed_coefficient` | q=1 coefficient `Rat` / closed coefficient `Rat` |
| `period_weighted_core_identity` | period-weighted coefficient `Rat` / `s^2(s+1)/2` as `Rat` |
| `carrier_period_polynomial` | complete actual orbit `Poly` / rational core-extension `Poly` |
| `carrier_hand_control` | complete actual orbit `Poly` / audit's deductive carrier control |
| `carrier_orbit_total` | number of actual orbits / sum of deductive control coefficients |
| `carrier_weighted_total` | sum of actual period times actual orbit count / full state count |
| `carrier_period_set` | increasing actual periods / `{1..2n}` plus stated even tail (or `[1]` for `n=1`) |
| `carrier_maximum_period` | actual largest period / 1 or `4n-4` |
| `carrier_fixed_states` | actual one-step fixed-state count / `n^n` |
| `fixed_iterate_count` | directly iterated count as `Rat` / divisor-sum count as `Rat` |
| `seven_row_coverage` | per-row presence Boolean / size-based expected presence; also sum of row state counts / full state count |
| `finite_coverage_limits` | matching `[n,group_id]` witnesses / empty array |
| `total_carrier_states` | sum of all four state counts / 4356 |

Scope strings are `n=N`; `n=N/state=ID`, `/orbit=ID`, `/group=ID`, `/k=K`,
or `/row=ROW`; `core_size=S`, optionally `/FAMILY` or `/catalogue=ID`;
one of the three coverage family strings; or `all_carriers`.
Predicate order is evaluation order, not alphabetical: all checks for each
carrier, followed by rational-series comparisons, the three coverage checks,
then the full state-total check. Consumers must retain this ordering.

`CoverageLimit` has exactly `family:String`, `first_core_size:Int`,
`observed_group_references:[[Int,Nat]]`, `finite_status:String`, and
`theorem_status:String`. The order and minimum sizes are:

1. `figure_eight_both_cycles_long`, size 5;
2. `barbell_both_cycles_long`, size 6;
3. `theta_all_paths_nondirect`, size 5.

The status literals are `not_exercised_in_n_1_2_3_4` and
`deductively_covered_by_all_parameter_anchor_argument` respectively. The
expected witness list is empty in all three cases. The theorem-status field
attributes coverage to the proof, not to execution or these strings.

## 8. Failure and reception boundary

If all construction completes, stdout has this exact schema whether ordinary
predicates pass or fail: exit 0 means no false predicates, exit 1 means one or
more false predicates, with every such ID explicitly listed. A fatal input,
construction, serialization or I/O error yields exit 2 and one diagnostic
line on stderr prefixed `P212 verifier failure: ` when caught inside `main`.
Interpreter startup, syntax or import errors before `main` are outside this
program-level status convention and are likewise nonadoptable failures.
Because output is serialized only after all checks, an earlier fatal error
does not emit a completed JSON
object. An I/O error can leave partial raw stdout; that raw stream must still
be preserved and must never be adopted as a canonical. Recorded checks in a
failed in-memory construction are not claimed to have been emitted.

No predicted byte count, predicate count, success flag or execution result is
prewritten here. Source reception must read the complete source and this
interface before a distinct runtime binding authorizes any scientific
invocation. A complete future stdout requires complete semantic reception;
neither matching headline totals nor a hash alone is that reception.
