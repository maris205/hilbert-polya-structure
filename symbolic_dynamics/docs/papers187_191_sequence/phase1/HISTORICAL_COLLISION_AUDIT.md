# Central historical-collision audit — P187–P191

Status: **live Stage-1 gate; no paper number follows from this document**.  
External status: `HOLD_EXTERNAL`.

This audit compares literal updates, sufficient statistics, schedulers, and
proof engines against P1–P186 and against earlier killed scouts.  A carrier
change, relabelling, parameter sweep, or decorated fibre does not reopen an
occupied mechanism.  Conversely, a shared word such as “gcd”, “partition”,
or “transpose” is not itself a collision: the equality must occur at the
update or theorem-engine level.

## Binding eliminations

| current candidate | central decision | binding evidence |
|---|---|---|
| `RC02/CGS`, cyclic neighbour gcd | `KILL_DIRECT_SCOUT_REPEAT` | The identical cyclic update, sliding-window iterate, longest-minimum-gap clock, sharp depth, and terminal fibres already occur as C2 in the P107–P111 combinatorial scout. |
| `RC04/SCE`, self-cardinality expansion | `KILL_CONJUGATE_WITHIN_BATCH` | Reverse-complement conjugates the update to `RC03/SCT`; it is one literal dynamical class, not a second system. |
| `RC05/LSS`, subset left stabilizer | `KILL_DIRECT_SCOUT_REPEAT` | A13 of the P172–P176 algebra scout has the identical map, idempotence, subgroup-lattice image, and Möbius inverse.  Moving to nonabelian examples does not change the engine. |
| `A02`, conjugacy-class-size power | `KILL_PERMANENT_POWER_FAMILY` | The P137–P141 ledger permanently withholds state-dependent group/permutation powers (`CCP/FCP/MCP`) absent a new literal update and proof engine.  Dihedral class sizes merely reduce the present map to exceptional doubling. |
| `A01`, nilpotent last-nonzero selector | `RESERVE_BELOW_VALUE_FLOOR` | Its Jordan fibre polynomial is correct, but the temporal/spectral axis is automatic because the update is defined to jump to the last nonzero iterate.  One substantial axis is not enough for this batch. |
| `C04/PME`, positional multiplicity echo | `KILL_OCCUPIED_COAGULATION` | Equality blocks of equal cardinality merge.  This is the permanent equal-cardinality/Glaisher-type coagulation quotient recorded throughout P122–P141. |
| `G02/ECSC`, equal-component-size completion | `KILL_OCCUPIED_COAGULATION` | Passing from blocks to connected graph components decorates, but does not alter, the same simultaneous equal-cardinality coagulation. |
| `C08/PBMP`, parallel block-minimum peeling | `KILL_FACTOR_OF_P105` | After forgetting cyclic order inside each P105 cycle, cycle-minimum pruning gives exactly the same synchronous least-element peeling clock.  Its inverse formula is a push-forward, not an independent system. |
| `C03/IPF`, simultaneous peak fall | `KILL_UNCLOSED_AND_OWNER_DENSE` | Exact monotonicity and small-box depth are real, but no all-parameter normal form or every-target inverse closed; parallel peak/pop-stack/Knuth rewriting is also owner dense. |

## Provisional separations still under proof/owner pressure

- `RC01/CDQ` is the positive cyclic valuation difference
  `(e_i-e_{i+1})_+`, not cyclic gcd smoothing, a one-coordinate valuation
  ladder, or a fixed power map.  Its height-layer freezing proof and cyclic
  target-constraint trace must both remain explicit.
- `RC03/SCT` uses the endogenous scalar rank `|A|` to truncate a labelled
  subset.  It is neither P185 prefix diversity nor P186 rank-subtraction of
  ordered support gaps.  Its temporal rank recursion and source-size fibre
  partition are different proof objects.
- `G01/TRC` remembers the full labelled row-sum vector as column heights and
  then alternates Ferrers conjugation.  P127 instead recomputes an odd
  outdegree parity relation.  Ferrers matrices, conjugate partitions, binary
  line sums, and their classical counts receive zero contribution credit.

The replacement candidates are added only after their lane files, exact
transcripts, and history-first audits are frozen.  No bounded source-search
non-hit can change a `KILL`, prove novelty, or lift `HOLD_EXTERNAL`.
