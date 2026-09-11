# P212 B complete output schema v1

This is the prospective interface of unexecuted source, not a result.
Exactly one ASCII, sorted-key, compact JSON object and LF is written on a
completed construction. No floats, nulls, paths, hashes or timestamps occur.
Integers, Booleans, strings, objects and arrays are distinct types.
Internal tuples become JSON arrays. Zero-based labels are 0..n-1.

`State` is `[u,v,f(0),...,f(n-1)]`. Its ID is the base-n little-endian
integer sum of coordinate i times n^i. The n=1 sole state has ID zero.
`Edge` is `[min(a,b),max(a,b)]`. An edge-multiset array is sorted and
retains equal entries as multiplicities, never as distinguishable identities.
`Poly24` is increasing `[period,24*coefficient]` pairs with zero coefficients
omitted. No rounding or division is used in the scaled comparison.
An ordinary `Poly` uses unscaled integer orbit counts in the same pair form.

## Top-level exact fields

| Field | Exact meaning |
| --- | --- |
| schema | `p212-review-b-v1` |
| role | `nonauthor_process_separated_B` |
| method | `inverse_digits_DSU_Pruefer_cotree_contraction_static_anchors_denominator_recurrence` |
| labels | `zero_based_little_endian` |
| carrier_sizes | `[1,2,3,4]` |
| catalogues | Four `Catalogue` objects, increasing s |
| carriers | Four `Carrier` objects, increasing n |
| series_pieces | Three `Piece` objects in figure_eight, barbell, theta order |
| core_series | Four `CoreSeries` objects, increasing s |
| coverage_limits | Three `Limit` objects, specified below |
| predicates | Every `Predicate` in evaluation order, no omissions |
| predicate_census | Every encountered name in alphabetical order with counts |
| summary | Exact `Summary` below |
| exclusions | Four literal strings below |

Exclusions in order: `finite evidence is not an all-n proof`;
`first-size 5/6/5 families are unexecuted`;
`no external review or global novelty certificate`;
`no build or lifecycle completion`.

## Catalogues and static anchors

`Catalogue` has exactly `s,entries`. `entries` follows increasing edge-multiset
lexicographic order. Each entry has exactly `edges,description,static_anchors`.
The complete catalogue is Prüfer-tree plus two edges, minimum degree two,
deduplicated by the complete edge multiset. It includes no graph-isomorphism
quotient and only s=1..4. Every connected core has at least one such tree.

`Description` has exactly `family,row,branches,paths,lengths,period,classes`.
Branches are increasing. Paths retain full ordered vertex sequences after
degree-two contraction, with each sequence replaced by the lesser of itself
and its reversal. Figure-eight and theta paths are lexicographically sorted;
barbell lists the sorted two closed paths first and the bridge last.
Lengths are numbers of edges. The period and classes are the manuscript's
seven-row table, reproduced by the source's branch-length cases.

`static_anchors` contains every `[State,[Raw,Class]]` in lexicographic State
order from a purely static destination enumeration whose multiset is exactly
the catalogue entry. `Raw` and `Class` are two bits for figure-eight/barbell;
Class is the smaller of the bit pair and its joint reversal, leaving short
cycles unchanged. For theta they are triples of internal-vertex token arrays,
with empty direct-path tokens indistinguishable; Class is the smallest cyclic
rotation, not reflection. The anchor is the smallest branch, additionally
requiring the first figure-eight cycle or the barbell bridge departure.

## Carriers, all arrows and invariant groups

`Carrier` has exactly `n,states,orbits,groups,row_counts,period_polynomial,
extension_contributions,fixed_iterates`.

`states` has every ID 0..n^(n+2)-1 once, in increasing order. A state record
has exactly `id,state,inverse,forward,orbit,invariant`. Inverse and forward
are complete target IDs. Orbit is the least ID in the DSU component.
`Invariant` has exactly `edges,active,pruning_layers,core,core_edges,complement`.
Active/core vertex lists increase. Pruning layers are successive simultaneous
degree-less-than-two deletion sets in increasing order. Complement contains
every non-core `[source,target]` in source order, including inactive components.

`orbits` has exactly `id,inverse_time,period` for each component in increasing
least ID order. The time list starts at that least ID and follows literal
inverse transitions until the first repeat, excluding the repeated state.
Its sorted contents must equal the DSU component and its repeat must be the
initial state. Period is that list's length, never a supplied stopping value.

Each group has exactly `id,key,description,states,orbits,actual_anchors,
expected_anchors,class_to_orbits`. Group order is lexicographic by full key;
IDs are consecutive from zero. `key` is `[core_vertices,core_edges,complement]`.
The expected key set enumerates every label subset, every catalogue and every
complement map. State/orbit ID arrays increase. Anchors are increasing triples
`[state_ID,Raw,Class]`, obtained respectively from observed members and static
core assignments lifted through the fixed complement. Class-to-orbit records
are `[Class,increasing_orbit_IDs]` in Class order. Comparing these sets to
the complete list of singleton group orbits verifies the decoration bijection,
not merely a count divided by a period.

`row_counts` has all seven manuscript row strings, each mapping to
`[number_of_groups,number_of_orbits,number_of_states]`, including zeros.
The exact row names and first core sizes are:

| Row | First size |
| --- | --- |
| figure_eight_double_loop | 1 |
| figure_eight_short_nontrivial | 2 |
| figure_eight_long | 3 |
| barbell_short | 2 |
| barbell_long | 4 |
| theta_triple_direct | 2 |
| theta_other | 3 |

Period polynomial is the complete unscaled actual `Poly`.
Each extension record has `s,multiplier,terms24` for s=1..n, where multiplier
is (n)_s n^(n-s) and terms24 is its product with the complete scaled core
period polynomial. Each fixed-iterate record has `k,ids,predicted24` for
every k from 1 to the stated maximum. IDs are computed by repeated inverse
application to all states; predicted24 is the period-divisor census sum.

## Series and limits

`Piece` has `family,terms24`, where terms24 is increasing `[s,period,c]` with
c the scaled EGF coefficient. Each `CoreSeries` has `s,terms24,closed24`.
No s>4 coefficient is emitted and there is no period truncation. The source
reconstructs the rational denominators using coefficient recurrences, checks
the univariate numerator over (1-t)^3 independently, and compares with the
closed coefficient formula and period-weighted identity.

`Limit` has `family,first_size,witnesses,status`. Ordered families are
figure_eight_both_long (5), barbell_both_long (6), theta_all_nondirect (5).
Witnesses are all matching `[n,group_ID]`, required empty. Status is always
`deductive_only`: an attribution to the separate proof, not an executed test
of those families.

## Complete predicates, census and summary

`Predicate` has `id,name,scope,observed,expected,passed`. ID is consecutive;
passed compares exact sorted JSON encodings, so Boolean/integer differences
are not collapsed. The observed/expected values are retained whole.
Scopes are n, n/state-ID, n/orbit-ID, n/gGROUP-ID, n/family, n/k,
n/row, core size, coverage family or all, as written in source.

| Name | Comparison |
| --- | --- |
| inverse_range | Inverse is within full carrier / true |
| unit_preimage | Forward slot previously unassigned / -1 |
| literal_forward | Inverse-table forward target / direct simultaneous update |
| backward_invariant | Inverse target's entire core/complement key / original key |
| full_edges_invariant | Inverse target's full edge multiset / original multiset |
| registers_core | Both register membership flags / both true |
| core_internal | Every core stored pointer remains in core / true |
| active_excess | Active edge count / active vertex count plus one |
| dsu_cycle | First repeat and sorted backward traversal / seed and full DSU members |
| complete_groups | Entire actual group-key list / complete static expected list |
| period_table | All actual group periods / full predicted period/class list |
| complete_anchor_states | Actual full anchor triples / static-lifted triples |
| decoration_bijection | Class-to-orbit sets / every singleton group orbit |
| decoration_cardinality | Actual class count / seven-row class count |
| full_census | Complete actual orbit Poly scaled by 24 / rational extension Poly24 |
| pure_family_series | Full-core family counts times 24 / s! times family EGF Poly24 |
| attained_period_set | Full observed set / full theorem set |
| maximum | Largest observed period / 1 or 4n-4 |
| fixed_states | Number of period-one orbits / n^n |
| state_mass | Actual period-weighted orbit total / full carrier size |
| fixed_iterate | Directly iterated fixed count times 24 / divisor-sum count |
| row_presence | Nonzero group count / n at least first size |
| univariate_rational_identity | Total core coefficient / rational recurrence coefficient |
| closed_core_coefficient | Total core coefficient / stated closed polynomial |
| weighted_core_coefficient | Weighted coefficient / 12s^2(s+1) |
| finite_coverage_boundary | Entire witness array / empty |
| total_states | Sum of actual carrier state lengths / 4356 |

Census records have exactly `name,checks,failures`, listing all 27 encountered
names alphabetically. Counts reflect every retained predicate; no actual
count or success is asserted before execution. Summary has exactly
`states,orbits,predicates,failure_ids,passed`. States is fixed 4356 and separately
checked against actual data, orbits is the four actual component counts,
predicates is the complete length, failure_ids is the increasing false-ID
list, and passed means that list is empty. A completed failing output retains
this same full schema. Caught fatal errors may emit no complete JSON; partial
streams are ineligible for adoption and remain preserved.
