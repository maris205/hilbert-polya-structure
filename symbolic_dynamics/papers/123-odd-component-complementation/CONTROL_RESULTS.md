# Control results

## Exact verifier

- Scope: every labelled simple graph on `0 <= n <= 6`.
- Assertion count: **203,244**.
- Checks: component-partition refinement; literal equality of orbit depth and the separately evaluated parity-pruned split clock; statewise recurrent and fixed iff criteria; eventual period ceiling; exact depth histograms; co-connected odd base counts; exhaustive aggregate literal fixed/recurrent censuses; and EGF assembly by cumulative depth.
- Canonical output: `code/verify_odd_component_complementation.out`.
- Fresh-output comparison: byte-for-byte equality required.

## Exact small-order census

| n | fixed | recurrent | genuine 2-cycles | maximum depth |
|---:|---:|---:|---:|---:|
| 0 | 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 0 | 0 |
| 2 | 2 | 2 | 0 | 0 |
| 3 | 4 | 4 | 0 | 1 |
| 4 | 48 | 48 | 0 | 1 |
| 5 | 216 | 648 | 216 | 2 |
| 6 | 27,920 | 30,512 | 1,296 | 2 |

## Owner and collision controls

- **Zero credit:** Gallai component/co-component decomposition; cograph and cotree theory; labelled species/exponential formula; classical connected labelled graph enumeration; the identity `q_n=2c_n-2^(n choose 2)` for odd `n>=3`.
- **Internal collision controls:** P75 concerns complement components without this parity-triggered self-map; P117 concerns parity-triggered runs; P118 has an unrelated all-depth mechanism. P122 uses parity-selected record blocks on permutations and lexicographic descent, but has neither graph complementation nor a component-refinement tree. Generic “parity-selected blocks plus a sharp transient” language receives no credit. No result is transferred from them.
- **Owner posture:** bounded non-hit only. No novelty or priority claim follows.
- **External posture:** HOLD.

## Interpretation control

The recursive object is called a parity-pruned component/co-component split tree. It is not represented as a new cotree or a new modular decomposition. Small-order computation is corroboration only.

The printed `connected` array uses `connected[0]=1` solely as an empty-state
sentinel in the exhaustive report.  Component assembly starts at size one and
`C_even` starts at size two, so this sentinel is never consumed as a
connected-graph species coefficient; the standard convention `c_0=0` remains
in force in the mathematics.
