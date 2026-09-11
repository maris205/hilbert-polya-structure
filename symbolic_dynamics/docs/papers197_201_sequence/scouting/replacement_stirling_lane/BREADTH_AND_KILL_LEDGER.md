# Replacement breadth and kill ledger

Checkpoint: 2026-09-05 UTC.  The comparison unit is a fully literal finite
self-map, not a title or a parameter choice.  The current-batch systems LSPO,
LPC, RNT, BFSF, LTD, CMM, TCSD, GBE, SCT, SDD, LZK, and PZK are excluded and
are not counted below.  Exact-phrase scans of the local P1--P196 corpus found
no occurrence of the new literals below; the collision firewall separately
checks the nearest occupied silhouettes.

Only FOSP survives.  The other rows are retained as negative controls; a clean
definition is not enough when the dynamics is a generic action, sorting shell,
pruning shell, or standard local move.

| code | carrier | frozen literal map (including scheduler/hold) | quick signal | disposition |
|---|---|---|---|---|
| FOSP | order-`n` Stirling permutations | at the two `1`s, delete both, decrement survivors, and insert adjacent `nn` at the old first-`1` gap; `n=0,1` hold | exact depth `max` nonplateau label; CDF `(n+t)!/(2^t t!)`; image `2^(n-1)(n-1)!`; every-target fibre | **PROMOTE_SPIKE / OWNER_AMBER** |
| RBCR | Stirling permutations with their unique maximal depth-zero block factorization `W_1...W_d` | if `d>=2`, send `W_1...W_d` to `W_2...W_dW_1`; if `d<=1`, hold | period is exactly the root-block count modulo rotational symmetry; bijective | `KILL_GENERIC_COMPONENT_ROTATION` |
| O1CR | Stirling permutations written uniquely `A 1 B 1 C` | send `A 1 B 1 C` to `B 1 C 1 A`; no choices; `n=0` holds | a literal order-three compartment action | `KILL_FINITE_ACTION_NO_TAIL` |
| MMGI | Stirling permutations | delete the always-adjacent maximum pair `nn`; if its gap is `g` among `0,...,2n-2`, reinsert it at gap `2n-2-g`; `n=0` holds | explicit involution and fixed-gap census | `KILL_CANONICAL_INVOLUTION` |
| LICX | increasing plane trees on `0,...,n` | choose the least-labelled nonroot internal vertex; detach its rightmost child subtree and insert it immediately after that vertex in its parent's child list; hold if every nonroot vertex is a leaf | nonleaf mass is promoted toward the root; easy reverse child adoption | `KILL_ORDERED_TREE_PRUNING_SHELL` |
| RISA | increasing plane trees on `0,...,n` | scan consecutive root children left-to-right for the first labels `a<b`; detach the subtree rooted at `b` and make it the rightmost child of `a`; hold if no such pair exists | inversion/chain normal form, but the clock is a directed adjacent-order correction | `KILL_SORTING_CLOSURE_SHELL` |
| LIF | labelled Latin squares of fixed order `n` | lexicographically choose `(r_1,r_2,c_1,c_2)` whose `2x2` subarray is `a b / b a` with `a<b`, and interchange `a,b` in those four cells; hold if none exists | exact Latin-preserving intercalate trade; possible nontrivial trade graph | `KILL_STANDARD_TRADE / NO_CLOCK` |
| LCTP | nonnegative `r x c` contingency tables with fixed positive margins | lexicographically choose `i<j,k<l` with `x_(i,k),x_(j,l)>0`; subtract one there and add one at `(i,l),(j,k)`; hold if none exists | a deterministic transportation-circuit walk | `KILL_MARKOV_BASIS_MOVE / ORIENTATION_SHELL` |
| DORT | complete deterministic automata on ordered states `[m]` and alphabet `{0,1}` | choose the least state whose two outgoing targets differ and swap its `0`- and `1`-targets; hold if no row differs | selected row remains eligible, so every nonfixed orbit is a 2-cycle | `KILL_LOCAL_INVOLUTION` |
| OBBS | ordered independent `k`-tuples in `F_2^d`, `k>=2` | replace `(v_1,v_2,v_3,...)` by `(v_1,v_2+v_1,v_3,...)`; for `k<2` hold | fixed-point-free involution when `k>=2`; Gaussian carrier census | `KILL_BASIS_SHEAR_ACTION` |

## Literal closure notes

- RBCR and O1CR only move complete Stirling blocks, so no equal pair is cut.
- MMGI is closed because the current maximum pair is adjacent and may be
  inserted in every gap of the reduced Stirling permutation.
- LICX preserves increasing labels: a former child of `j` has label greater
  than `j`, while the new parent is the old parent of `j` and hence smaller
  than `j`.
- RISA adopts `b` only under `a<b`, which is exactly the inequality needed
  for an increasing tree.
- LIF is the standard four-cell Latin trade.  LCTP has zero row- and column-
  sum change.  DORT preserves one outgoing edge per letter, and OBBS performs
  an invertible elementary basis operation.

## Why the breadth controls do not rescue a slot

RBCR, O1CR, MMGI, DORT, and OBBS are transparent group actions or
involutions.  LICX is a monotone child-extraction/pruning rule; RISA is an
adjacent ordering/closure rule.  LIF and LCTP are interesting underused
carriers, but their literal updates are standard local trades and the scans
did not produce a sharp all-parameter clock plus an independent target atlas.
They are killed rather than embellished with a counter or renamed scheduler.

FOSP is retained because its countdown is not an attached state variable:
the exact clock is the largest *existing nonleaf label*, while recurrence is
nontrivial `n`-periodic label transport and the inverse theorem is a separate
target-side root-subtree cut.  The promotion/pruning resemblance still keeps
the external owner gate amber.

