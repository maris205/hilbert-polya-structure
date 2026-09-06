# Combinatorial scouting: eight literal maps, zero promotions

Date: 2026-09-05 UTC. Author scout, not independent review. No formal paper
allocation, novelty finding or acceptance status is issued. `HOLD_EXTERNAL`.

The lane used the project research skill's cheap-pilot and two-axis gate.
It did not increase an ambient factorial cutoff to manufacture a survivor.
The only follow-up used a proved Catalan compression, tested the resulting
small complete core, and still rejected the candidate for an unclosed atlas.

## Literal ledger

All ranks are one-based, stable ties use the original position. Tree size is
vertex count; matching size is edge count. Each listed box is complete.
The last-box tuple is `(states,image,recurrent,max tail,max fibre)`.

| Handle | Finite carrier and literal autonomous update | Last complete box and result | Disposition |
|---|---|---|---|
| C01_DRF | Permutations: independently rotate each maximal strict decreasing run one place right, so its minimum moves to its front. | `n=8`: `(40320,8362,1,7,34)`; unique identity endpoint; exact admissible-run inverse and Fibonacci identity fibre. | `KILL_SORTING_SHELL`. An inversion-decreasing run operation, not a new temporal mechanism. The observed sharp `n−1` upper bound and global fibre extremum are not claimed as proved. |
| C02_APR | Permutations: compute `s_i=sum_(j<=i)(−1)^(j−1) w_j`, and replace each position by the stable rank of `s_i`. | `n=8`: `(40320,1241,2,4,798)`. Every state enters a Catalan-sized bi-increasing alternating carrier in two steps. | `KILL_UNCLOSED_CORE_ATLAS`. Exact core through size 20 has irregular maximum clocks and increasing numbers of two-cycles; there is no all-parameter recurrence classification or ambient every-target inverse theorem. |
| C03_BPC | Plane rooted trees: read outdegrees breadth-first, then decode that word as preorder outdegrees of the next plane tree. | 10 vertices: `(4862,4862,4862,0,1)`; 39 distinct periods, including 78. | `KILL_TRAVERSAL_BIJECTION_NO_ATLAS`. The inverse is just the opposite traversal decoder; singleton fibres contribute no independent theorem axis. |
| C04_BDC | Plane rooted trees: same breadth-first-to-preorder update, but process every sibling list by decreasing child outdegree, preserving old sibling order on ties. | 10 vertices: `(4862,918,297,12,40)`; periods `1,2,3,4,5,6,7,8`. | `KILL_NO_SPINE`. Sibling sorting creates loss, but neither a complete temporal theorem nor a target inverse classification closes. |
| C05_DPF | Trees on labels `0,...,n−1`, rooted at 0: compute depths `d_i`; make `(d_1,...,d_(n−2))` the next tree's ordinary smallest-leaf Prüfer code. For `n=2` use the empty code. | `n=7`: `(16807,2612,722,10,67)`; period 88 already occurs. | `KILL_CODE_FEEDBACK_NO_ATLAS`. The valid depth/code feedback is label-convention dependent and has no all-size spine. |
| C06_LHP | Perfect matchings: orient edges low/high; sort by `(length,low,high)`; concatenate all lows followed by all highs and pair consecutive entries. | Six edges: `(10395,3387,1934,8,52)`; five edges have a 20-cycle and tail 27. | `KILL_OLD_EVEN_SLICE`. Exactly historical `C03_LEW` at every even edge count; odd-edge change does not clear the old rewiring family or supply an atlas. |
| C07_SMT | Set partitions: order blocks by minimum; every nonsingleton simultaneously sends its lower median to the next block cyclically; singletons send nothing; reorder new blocks by minimum. One-block states hold. | `n=8`: `(4140,1485,322,7,12)`; periods `1,2,3,4,6`. | `KILL_TRANSFER_VARIANT_NO_ATLAS`. Unlike P169 maximum transfer, block minima can move and the canonical cyclic order changes. This defeats a naive P169 proof transfer but provides no replacement theorem. |
| C08_TIR | Permutations: form insertion tableau `P(w)`, transpose it, then read rows bottom-to-top, within rows left-to-right. | `n=8`: `(40320,764,764,1,90)`; `T³=T`, and every positive fibre is the standard-tableau number of the target shape. | `KILL_RSK_INVOLUTION_LIFT`. The previously killed row-word RSK retraction with tableau transposition added; complete mathematics but no residual temporal axis. |

## Evidence and proved content

`verify_breadth.py` enumerates 187,542 map/state pairs: three permutation maps
through `S_8`, two tree maps through ten vertices, Prüfer words through seven
vertices, perfect matchings through six edges, and set partitions through
eight labels. Carrier uniqueness, closure, full functional-graph decomposition,
fibre conservation and cycle-population conservation are checked. Edge tables
have deterministic SHA-256 digests. See `BREADTH_CANONICAL.json`.

`verify_apr_core.py` checks the proved two-step compression on all 46,233
permutations through `S_8`; then it enumerates all 23,713 Catalan core states
through even size 20. It separately verifies 2,055 odd-size lift identities.
This is **not** an enumeration of `S_20`. Core maximum tails for even sizes
2 through 20 are `0,1,2,3,5,3,5,5,6,5`; respective core cycle counts are
`1,1,1,1,1,2,2,3,4,6`, with period one only at sizes 2,4,6 and period two in
the remaining tested sizes. See `APR_CORE_CANONICAL.json`.

`verify_theory_and_collision.py` independently checks 5,913 DRF target inverse
counts, 46,233 tableau target fibres, 6,918 traversal inverses, and every
matching comparison through six edges. It imports the old matching literal
read-only and records its file hash. See `THEORY_COLLISION_CANONICAL.json`.
These are author verification, not an independent research review.

The short complete proofs and explicit unresolved claims are in
`PROOF_NOTES.md`; history/primary-source subtraction is in
`SOURCE_AND_COLLISION_NOTES.md`.

## Reproduction

From the repository root:

```sh
python docs/papers204_208_sequence/scouting/combinatorial/verify_breadth.py
python docs/papers204_208_sequence/scouting/combinatorial/verify_apr_core.py
python docs/papers204_208_sequence/scouting/combinatorial/verify_theory_and_collision.py
```

Canonical files contain the actual corresponding stdout. Standard-library
Python only; CPU, no GPU, no remote model or external manuscript transmission.
Tool discovery did not expose the older skill's prescribed external brainstorming
endpoint; current-process reasoning and local pilots were used without claiming
an external brainstorm or review. No central state file or Git path was edited.

Final denominator: **8 literal systems, 8 killed, 0 reserves, 0 promotions**.
The two traversal variants count as two literal maps, not as independent proof
engines; the matching even slice is explicitly debited rather than counted as
new theoretical content. Do not revive C02 merely by expanding its cutoff.
