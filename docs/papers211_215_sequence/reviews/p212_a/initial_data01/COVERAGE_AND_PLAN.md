# P212 A saved-DATA checker source gate

SOURCE ONLY: check.js has been manually inspected, not executed, imported,
syntax-parsed or used to produce a semantic PASS. It reads only the complete
saved `qa/p212_a_runs/initial02/stdout.raw` data file, using Node fs/crypto.
It never imports, runs, invokes or compiles either scientific producer. Its
bounded arithmetic validates saved records and their mathematical relations;
it does not launch a new scientific orbit experiment or change the cutoff.

Root must read the complete current source and issue a separate DATA execution
authorization before the following exact command is submitted, workspace cwd:

    node docs/papers211_215_sequence/reviews/p212_a/initial_data01/check.js

Zero script arguments. The only data path, expected full SHA256 and expected
3,004,047-byte size are fixed in the source. The SHA256 is
24d6054e4a29411948becfa256d2182301b3f73d3ef78df1cad9088ed8b9922b,
as recorded in root's complete initial02 receipt read at b749f5. Full raw
bytes and input dev/ino/mode/size/mtimeNs/ctimeNs must remain unchanged from
before to after the DATA audit. The command writes no file: root retains its
actual complete stdout/stderr/exit and source/input keys in a fresh receipt.

Navigation inspected initial01 at 7bf55d before the source-intake timing
defect was reported. That was JSON navigation only, not semantic acceptance.
Root's GUARD_SOURCE_CORRECTION.md and INITIAL_RECEPTION.md were then read
completely at b749f5. Initial01 is preserved but is ineligible as canonical
origin or strict replay. This checker is bound exclusively to clean initial02;
byte equality between runs does not cure initial01's timing defect.

## Coverage of every scientific output field

The checker first verifies whole-file hash, byte size and the exact canonical
ASCII JSON re-encoding plus final newline. Exact object-key sets reject added
or missing fields. All integer arithmetic is safe-integer checked during
complete canonical serialization. Values and nested arrays are checked by
complete equality, never a printed PASS or a digest substituted for semantic
comparison. An assertion failure stops acceptance and emits FAIL/exit 1.

| Output portion | Complete independent DATA validation |
| --- | --- |
| schema, role, method, parameters, limits | All exact literal strings, every parameter key/value, fixed carriers/core sizes, zero labels/imports/data inputs, 24 scale and unexercised 5/6/5 limits. |
| catalogues and each entry's id/edges | Independently enumerate sorted unordered edge multisets of s+1 edges on s fixed labels; retain exactly connected minimum-degree-two graphs. Match every saved entry and its order, not a stated catalogue count. |
| family/paths/lengths/row/period/decorations | Degree-derived branch set; exact path-edge cover, disjoint exhaustive internal labels, endpoints and loop/bridge/theta roles; canonical reversals and path ordering; complete seven-row formulas. |
| incidence_states | Every core state is selected from the already validated complete rank-indexed s-carrier by its exact augmented edge multiset. The multiplicity is independently product over edges of factorial(edge multiplicity): assignment of occurrence identities to the distinct register/stored slots. Compare all states and multiplicities. This avoids copying the producer's orientation backtracker. |
| visit_words | Check labels, full core coverage, primitive circular representative and ordering. Reconstruct every phase by last arrival; check direct old-state update, edges and incidence exhaustion, exact table period and decoration count. Later compare every necklace to register words from the independently validated saved full-core orbit routes. |
| coefficients_scaled24 | Independently expand the three displayed rational EGF pieces through t^4 (not the producer's ordered length-sum code). Match every family/period coefficient, total, weighted total and labelled core count. |
| carriers.n/states | Exactly n^(n+2) rows in fixed n=1,2,3,4; every full little-endian state equals its rank expansion. Direct algebraic old-state update and inverse determine the saved successor/predecessor IDs. Independently compute active connectivity, leaf-pruned core, all induced admissible subsets, frozen complement and group key; compare all eight row columns. |
| carriers.orbits | Every saved route is nonempty, duplicate-free, starts at the smallest still-unassigned rank and follows each checked literal arrow, closing precisely at its seed. The union equals the full rank carrier, no overlap or transient. No new orbit search/producer invocation is used. |
| carriers.groups | Independently form all core label subsets, each fully verified graph and every unrestricted frozen complementary function. Compare complete sorted group keys, IDs, catalogue links, member-derived actual orbit IDs and all last-arrival reconstructed normalized expected routes. |
| carriers.row_counts/period_counts | Recount all groups, orbits and states into all seven rows, and every exact-period orbit count from the complete saved partition. |
| extension_terms_scaled24 | Recompute every falling-factorial/frozen-map multiplier and complete rational-series core polynomial; compare all extension fields and the full carrier census. |
| unexercised_group_ids | Independently select both-long figure-eight/barbell and all-nondirect theta groups; compare all three saved lists and assert emptiness only for n<=4. |
| checks | Rebuild the complete ledger in exact producer-defined invocation order from independently checked records and arithmetic. Compare every name, scope, complete observed value, expected value and boolean. No saved ledger value supplies its own recomputed counterpart. |
| check_census/failure_ids/finite_passed | Derive all class names and frequencies from the rebuilt ledger, all failed row indices and the boolean definition; require all rebuilt predicates true. |

All 29 ledger classes are rebuilt: word_primitive_state_period,
word_swap_successors, word_exact_edges, word_incidence_exhaustion,
word_decoration_count, word_period_table, labelled_core_series_scaled24,
closed_core_coefficient_scaled24, weighted_core_coefficient_scaled24,
complete_core_complement_groups, first_repetition_is_seed, orbit_partition,
unit_predecessor, inverse_both_directions, full_augmented_edges,
frozen_core_key, register_membership, active_excess, core_excess_and_degrees,
complete_decorated_orbit_partition, exact_periods_for_group,
full_period_census_scaled24, attained_period_set, sharp_maximum, fixed_states,
weighted_full_mass, seven_row_presence, unexercised_first_size_families,
complete_fixed_carrier_total. Counts are recomputed, not hardcoded from the
navigation report's 34,683 rows.

## Output and boundary

On complete success one JSON line records schema, explicit saved-DATA PASS,
exact input key, actual assertion/ledger/class counts, per-carrier state/
orbit/group totals, and false producer-executed/canonical-adoption/all-size-
proof flags. On failure one JSON line records FAIL, completed assertion count
and error, with exit 1. Root must preserve the complete actual result before
reception; there is no prefilled result or canonical in this source package.

This checks scientific output semantics only. Root's independent raw command,
grant, runtime, exit, pre/post and capture receipts remain separate required
evidence. In particular, the final pinned guard compares runtime path/kind/
bytes/hash (or required-absence errno), records historical metadata drift,
and requires complete current pre/post equality. It does NOT reject historical
metadata drift by itself. Root's extra historical-equality preflight is a
separate stronger observation, not different guard semantics. The erroneous
earlier description and initial01 timing are preserved by root's correction.

Complete DATA acceptance can support only later root adoption of actual clean
initial02 stdout. Strict pairs, whole-byte comparisons, source build/view,
final manuscript Review A, later rounds and HOLD_EXTERNAL are unchanged.
