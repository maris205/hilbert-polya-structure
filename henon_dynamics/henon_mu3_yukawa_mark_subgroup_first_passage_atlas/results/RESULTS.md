# C88 results

Canonical evidence SHA-256:
`4511d434f477784782f2af5106afff4c2cf3b48cd7eb7a62ed05b8f2f42afb1b`.

| `H` | order | first-passage range | minimal hits | exact expectation |
|---:|---:|---:|---:|---:|
| 0 | 1 | 0--0 | 1 | `0` |
| 1 | 2 | 1--16 | 1 | `17/2` |
| 2 | 3 | 1--10 | 24 | `3961/1320` |
| 3 | 3 | 1--9 | 13 | `2363/990` |
| 4 | 3 | 1--10 | 24 | `3961/1320` |
| 5 | 3 | 1--10 | 30 | `12631/3960` |
| 6 | 6 | 2--16 | 24 | `35207/3960` |
| 7 | 6 | 2--16 | 13 | `8687/990` |
| 8 | 6 | 2--16 | 24 | `35207/3960` |
| 9 | 6 | 2--16 | 30 | `357/40` |
| 10 | 9 | 2--10 | 38 | `13243/3960` |
| 11 | 9 | 1--13 | 18 | `289/72` |
| 12 | 9 | 1--13 | 18 | `289/72` |
| 13 | 9 | 1--13 | 13 | `34/9` |
| 14 | 18 | 3--16 | 38 | `2363/264` |
| 15 | 18 | 2--16 | 18 | `12121/1320` |
| 16 | 18 | 2--16 | 18 | `12121/1320` |
| 17 | 18 | 2--16 | 13 | `4522/495` |
| 18 | 27 | 2--13 | 25 | `1513/360` |
| 19 | 54 | 3--16 | 25 | `36499/3960` |

Every row sums to `16! = 20922789888000` ordered permutations.  All exact
CDF-difference counts agree with independently accumulated pivotal-edge
counts.  The evidence preserves all `20 x 17` count/probability/survival
rows, not only the summary above.

All `102` comparable subgroup pairs obey pointwise and stochastic order.  The
top row matches C83's subset-hit counts, pivotal totals and patterns,
permutation counts, reduced probabilities, survival counts, total mass, and
expectation entry by entry.  See
[C88_PREFREEZE_MANIFEST.json](../C88_PREFREEZE_MANIFEST.json) for the frozen
file ledger.
