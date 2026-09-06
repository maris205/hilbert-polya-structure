# Combinatorial cross-domain scout: 22 systems, no allocation

**Date:** 2026-09-03  
**Route:** finite autonomous combinatorial dynamics  
**Decision:** `KILL_ALL_CURRENT`  
**External state:** `HOLD_EXTERNAL`.

## Outcome first

This lane implemented and exhaustively probed **22 genuinely different
literal maps** on posets, graphs, tournaments, 3-uniform hypergraphs, set
families, permutations, words, and Latin squares.  It then spent focused
proof and owner effort on the three most attractive false positives.  The
correct result is **zero survivors and zero reserves**.

That negative result contains three concrete advances:

1. The Cartesian breadth-first map has a proved sharp `n-1` clock and a
   complete every-target compatible-tree fibre DP, independently checked
   through `S_9`; reading the P142 archive shows that the entire proof
   silhouette is already occupied by its Cartesian-preorder negative control,
   so the BFS variant is decisively killed rather than cosmetically promoted.
2. Bracket-matching support has a proved Fibonacci image, exact target fibre
   `(z+1) product Cat_(r_i/2)`, and a strict first-run convergence potential;
   after P74/P90/P93 subtraction, the missing sharp maximum clock keeps it
   below the gate.
3. Cyclic adjacent-sum reranking has an explicit exact `2n` orbit for every
   `n>=3`, but full `S_9` enumeration finds three 18-cycles and one 9-cycle,
   refuting the simple recurrent-atlas conjecture and providing a clean early
   kill.

The most lively unanalysed literal map is simultaneous reversal of tournament
arcs lying in exactly one directed triangle.  At `n=6` it has tails through 4
and periods 1, 2, 4.  It is not retained: P112 has the adjacent “at least one
triangle” reserve, primary triangle-reversal ownership is dense, and this
lane has no all-rank clock or fibre theorem for the exact-one rule.

## Artifact map

- `IDEA_LEDGER.md`: all 22 carriers, literal updates, exact boxes, early
  signals, and individual kill decisions.
- `COLLISION_FIREWALL.md`: P1--P171 literal/system/proof-engine comparison.
- `OWNER_SEARCH_LOG.md`: bounded primary-source queries and owner subtraction;
  query non-hits explicitly receive no novelty value.
- `CBF_DERIVATION.md`: complete sharp clock and every-target fibre proof,
  ending in the decisive P142 internal kill.
- `BMS_DERIVATION.md`: image/fibre theorem, convergence proof, and the sharp
  boundary of what remains unresolved.
- `ASR_KILL_NOTE.md`: the all-rank `2n` orbit lemma and the rank-nine atlas
  counterexample.
- `breadth_pilots.py`, `verify_cbf.py`, `verify_bms.py`, and
  `verify_asr_kill.py`: standard-library exact programs.
- `BREADTH_CANONICAL.txt`, `CBF_CANONICAL.txt`, `BMS_CANONICAL.txt`, and
  `ASR_CANONICAL.txt`: byte-reproducible transcripts.
- `SHA256SUMS`: integrity manifest for this directory.

## Exact evidence

| program | complete exact scope | assertions |
|---|---|---:|
| `breadth_pilots.py` | all 22 maps; labelled posets through 5, graphs through 5, tournaments through 6, 3-graphs through 5, all set families through ground size 4, permutations through 7, binary words through 15/14, bounded q-ary words, Latin squares through order 4 | 1,344,326 |
| `verify_cbf.py` | every permutation through `S_9`; three-way literal/tree/queue-DP fibre agreement | 4,730,679 |
| `verify_bms.py` | every binary source and target through length 16; independent cancellation, image DP, fibre and potential | 848,808 |
| `verify_asr_kill.py` | complete functional graphs through `S_9`; principal orbit regression through rank 100 | 409,243 |
| **total** | | **7,333,056** |

All assertions are exact integer, set, state, orbit, fibre, or structural
equalities.  Enumeration is falsification pressure; the all-rank statements
retained in the notes have written proofs.

## Recommendation

Allocate **no paper slot** from this lane.  The strongest complete theorem is
an internal proof-engine collision; the strongest word theorem loses its
static axis to an occupied normal form; and the freshest permutation/tournament
maps lack complete recurrence and inverse axes.  Any re-entry must begin with
a materially different literal update and an independent labelled-fibre or
target-transfer theorem, not a traversal swap, pruning threshold, or larger
finite box.
