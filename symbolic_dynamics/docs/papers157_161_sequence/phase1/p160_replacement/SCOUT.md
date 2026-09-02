# Replacement P160 breadth scout

**Date:** 2026-09-02 UTC  
**Portfolio boundary:** P1--P156 and retired BST  
**External state:** `HOLD_EXTERNAL`  
**Systems executed:** 12 literal dynamics, not parameter relabelings

## Outcome

`RCS`, rectangular-corner stripping of Ferrers diagrams, is the sole survivor.
For fixed positive integers `a,b`, one update deletes the first `a` rows and
first `b` columns.  Exact tests for four genuinely different parameter pairs,
five time ranks, every source of weight at most 30, and every nonempty target
of weight at most eight verify a two-axis silhouette:

1. the rank-`t` state is the southeast diagram beginning at row `at+1` and
   column `bt+1`, so the pointwise clock and the capped-family height are
   sharp rectangle conditions; and
2. for every time and every target, the source series factors into two
   independent bounded-partition series, with a separate complete formula for
   the empty target.

The first axis is not a generic finite-map statement.  The second resolves
every target, not only the image size or a maximum fibre.  The minimum-source
thresholds of the one-cell, two-cell row, and two-cell column targets recover
the ordered pair `(a,b)`.  This supplies a strong identifiability interface in
addition to the clock.

The owner pass found direct prior use of first-row/first-column deletion and
the Durfee decrement at `a=b=1`.  Those facts, Durfee-square enumeration, and
the elementary bounded-partition products receive zero credit.  No inspected
record stated the two-parameter dynamical system together with its all-time,
every-target fibre atlas or threshold-based recovery.  This is a bounded
search result only, not a novelty or priority claim.

## Twelve-system decision ledger

| handle | carrier and literal update | exact small signal | decision |
|---|---|---|---|
| `RCS` | integer partitions; delete the first `a` rows and first `b` columns | all iterates; sharp rectangle clock; every-time target fibres through weight 30 | **`SELECT_REPLACEMENT_P160`** |
| `PTF` | permutations; detach the maximum of every nontrivial cycle in parallel | maximum tails `0,1,...,6` through `S_7` | `KILL_CYCLE_PRUNING_P112_P155` |
| `ADE` | binary words; erase every `01` in parallel | maximum tails `floor(n/2)` through length 12; exactly `n+1` fixed words | `KILL_WORD_REWRITE_P90_P147` |
| `ESA` | set partitions; merge blocks having equal current size | maximum tails `0,0,1,1,2,1,2,2,3` through rank eight | `KILL_PARTITION_COALESCENCE_P116_P126` |
| `L2G` | maximum-degree-two graphs; apply the line-graph operator | `P_n` has tail `n`, every `C_n` is fixed | `KILL_DIRECT_LINE_GRAPH_OWNER` |
| `BCH` | binary linear codes; replace `C` by `C cap C^perp` | state/image counts `(374,31)` at length five; one-step idempotence | `KILL_CODE_HULL_IDEMPOTENT` |
| `CBA` | clutters; take the blocker of minimal transversals | `3,6,20,168` states through four vertices; exact involution | `KILL_EDMONDS_FULKERSON_OWNER` |
| `BMT` | plane binary trees; recursively sort the two child subtrees | Catalan-to-unordered image counts through eight nodes; idempotent | `KILL_TREE_CANONICALIZATION` |
| `NCR` | binary necklaces; reverse and complement | involution; fixed counts `0,1,0,2,...,32` through length 12 | `KILL_DIHEDRAL_GROUP_ACTION` |
| `HME` | finite hypergraphs; retain inclusion-maximal edges | image counts `3,6,20,168`; idempotent clutter reduction | `KILL_HYPERGRAPH_REDUCTION` |
| `TCR` | tournaments; reverse edges lying in an odd number of cyclic triangles | periods `2,2,4,4` and tails `0,1,1,2` at orders 3--6 | `KILL_UNSTABLE_BOOLEAN_TOURNAMENT` |
| `LPR` | balanced-plus-one binary words; rotate after the last prefix minimum | Catalan image and uniform fibre `2q+1` through length 13 | `KILL_CYCLE_LEMMA_CANONICALIZATION` |

## Why RCS is not an occupied pruning transfer

The update is a global coordinate truncation of a Ferrers ideal.  It does not
locally inspect degrees, leaves, runs, records, parity, or activity.  Its proof
does not reuse the vertex-survival, tree-expansion, composition-refinement, or
selected-subword scaffolds of P114, P126, P148, or P149--P156.  The inverse
splits a source diagram along a forced southeast target into an arbitrary
top excess partition and an arbitrary bounded bottom partition; the two
factors have orders `at` and `bt`.  That ordered two-boundary factorization is
also what makes `(a,b)` recoverable.  The nearest occupied carrier is P126's
ordered compositions, but its update splits parts and increases rank, whereas
RCS deletes a rectangular corner and decreases two Ferrers coordinates.

## Exact evidence and boundary

Run

```text
python -B docs/papers157_161_sequence/phase1/p160_replacement/verify_replacement_scout.py
```

and byte-compare stdout with `CANONICAL.txt`.  The frozen run contains 795,659
assertions.  Enumeration is regression pressure only; it proves neither the
all-parameter theorem nor owner absence.
