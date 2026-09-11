# Predeclared scientific predicates

Status: PREPARATION_ONLY / NOT_EXECUTED. Every comparison below is in the
written producer before any invocation. None is a reported successful test.
Only four boxes are permitted: n=1,2,3,4, containing 1,16,243,4096 states,
respectively, total 4356. No later finding may be disguised as an original
predicate; a revision must preserve this preparation and the first run.

## Independent algorithmic routes, not independent authorship

1. `literal_successor` reads old u,v,f(v), writes only f(v):=u, and advances
   the ordered pair. Exhaustive Cartesian states and only these literal
   successors feed `discover_cycles`. That function knows no graph/core
   formula, generating function, inverse formula, or expected period.
2. `graph_multiset`, `classify_state`, and `core_shape` independently construct
   the n+1 undirected edges, prune trees, and traverse maximal degree-two
   chains. They do not consume successors, cycle IDs, cycle lengths or EGF
   coefficients. Loop degrees and indistinguishable parallel occurrences
   are explicit. Shape and the written length table predict period and
   orbit-decoration count. Grouping retains the exact labelled core and all
   frozen destinations, not merely a graph isomorphism type.
3. `core_orbit_series` expands the three rational expressions of proof (4)
   with exact Fraction arithmetic. It sees neither states nor graphs nor
   empirical counts. Truncation is only t-degree<=4, with no q-degree cap.
   Label/frozen-complement extension multiplies by `(n)_s n^(n-s)`.
   `total_core_coefficient` separately implements proof (8)'s c_s values.

These separations pressure the author proofs; they are not nonauthor review.
Both the scout and root remain pointer proof contributors. The source-owned
list-reversal mechanism stays subtracted, and source priority remains bounded.

## Per state: ten predicates on every state in each box

The prefix is `nN.stateI.` for box N and the complete Cartesian state ID I.

| Suffix | Exact comparison and retained evidence |
|---|---|
| S01_successor_closed | The literal successor ID belongs to the full enumerated carrier. An impossible lookup is a fatal execution failure, not a silently skipped state. |
| S02_inverse_forward | R(R_inverse(state)) equals the entire original tuple. The inverse is not used to discover cycles or predecessors. |
| S03_inverse_backward | R_inverse(R(state)) equals the entire original tuple. |
| S04_indegree | The full predecessor-list length, built from all direct edges, equals one. |
| S05_preperiod | Directly discovered distance to the eventual cycle equals zero. |
| S06_multiset_invariant | The complete successor multiset of f-edges plus the extra location edge equals the original multiset. |
| S07_core_frozen_invariant | Successor and original full canonical core/frozen-arrow keys are identical. |
| S08_core_closed | Both locations and all stored destinations of core vertices lie in the core. |
| S09_core_valid | The undirected extraction yields figure-eight, barbell or theta, with all edges covered and valid bicyclic branch degrees. A classification error is retained as invalid and fails. |
| S10_period | The direct cycle length equals the exact shape/length-table prediction. |

## Per directly discovered cycle: three predicates

Prefix `nN.orbitJ.`.

- O01_edges: each direct successor of the saved cycle list equals the next
  saved cycle ID, including wraparound.
- O02_unique_members: the saved cycle contains no repeated state ID.
- O03_one_group: every cycle member has the same full fixed-core/frozen key.

## Per fixed labelled core and frozen complement: three predicates

Prefix `nN.groupJ.`.

- G01_orbit_count: the number of distinct directly discovered orbit IDs in
  this group equals the orientation/order census from the core table.
  Expected count is two for figure-eight/barbell exactly when both cycles
  have length at least three; for theta it is one with at least two direct
  chains and two otherwise. Both double-loop and triple-direct exceptions
  are handled explicitly by the period table.
- G02_periods: all discovered periods in the group form exactly the singleton
  consisting of the table's period.
- G03_exact_cover: the union of complete saved cycle lists is exactly the
  group's full state list, with no missing, extra or duplicate member.

G01 never computes `group_state_count / period`; it tests the independently
discovered number of cycles directly. This is the requested fixed-core and
frozen-complement orbit census, including the case that the extra edge joins
two previously separate f-components and arbitrary inactive components.

## Exact generating function and per-box predicates

For each nonzero (s,p) series coefficient with s<=N,
`nN.E01_integral_sS_pP` checks that `(N)_s N^(N-s) c_(s,p)` has denominator
one, and retains the coefficient, multiplier and exact contribution.

| Box suffix | Exact comparison |
|---|---|
| B01_carrier_count | Enumerated state count equals the parameter-file count. |
| B02_cardinality_formula | Enumerated count equals n^(n+2). |
| B03_edge_count | Complete saved edge count equals the declared state count. |
| B04_cycle_cover | Concatenated cycles, sorted, equal every carrier ID exactly once. |
| B05_period_set | Observed period set equals {1} for n=1, otherwise {1,...,2n} union even numbers from 2n+2 to 4n-4. Empty upper ranges stay empty. |
| B06_maximum_period | Observed maximum equals 1 for n=1 and 4n-4 otherwise. |
| B07_period_egf | The entire empirical period/orbit histogram equals the independently expanded period-refined EGF extension, including any unexpected observed period. |
| B08_core_period_egf | The entire empirical (core-size,period)/orbit histogram equals the same extension coefficient by coefficient. |
| B09_total_orbits | Directly discovered orbit count equals the separate sum using c_1=1, c_2=2, c_s=(5s^2+s+24)/24 for s>=3. |
| B10_fixed_states | Direct literal fixed-state count equals n^n. |
| B11_weighted_cycle_cover | Sum of period times empirical orbit count equals full carrier size; this is a consistency check, not the enumeration theorem. |

## Global/series predicates

- `series.C01_nonnegative_sS_pP`: every nonzero exact total coefficient is
  nonnegative. No coefficients are discarded for having an unexpected q degree.
- `series.C02_total_sS`: sum over p of coefficients equals c_s, for s=1,...,4.
- `series.C03_state_weight_sS`: sum over p of p times the coefficient equals
  s^2(s+1)/2, for s=1,...,4, the algebraic consistency identity in proof §7.
- `global.T01_four_boxes`: actual n list is exactly [1,2,3,4].
- `global.T02_total_states`: total retained state count equals 4356.
- `global.T03_unique_check_ids`: all scientific check IDs, including this
  check's own ID, are distinct.

No fixed-iterate sweep, n=5 check, subcarrier sampling, stochastic test,
cutoff search, extra box, higher-period truncation or pilot escalation is
included. A mismatch kills the claimed finite agreement until reviewed; it
does not authorize another run or a larger box. A successful finite output
would still not prove the all-parameter theorems or settle source ownership.
In particular the two-genuine-cycle figure-eight/barbell two-orbit rows need
at least five/six core vertices and are outside these four boxes. No PASS
may be interpreted as empirical coverage of those rows.
