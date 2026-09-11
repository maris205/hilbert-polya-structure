# Exact control results

## Canonical run

The standard-library verifier exhausts **18 distinct literal systems**.  Of
these, **16** satisfy the strict non-closure intake; two retractions are
retained only as negative controls.  The run finishes with:

```text
EDGE_DIGEST=ba346c933983b076b55a3560b603017a1f43cdc1f510aea12392eea624dd2098
ASSERTIONS=517353
RESULT=PASS
```

Two bytecode-disabled fresh runs were required to agree byte for byte before
`CANONICAL.txt` was frozen.

## M01 hostile boxes

| (n,q) | states | image | fixed | height | kernel/zero fibre |
|---:|---:|---:|---:|---:|---:|
| 2,2 | 16 | 4 | 1 | 2 | 10 |
| 2,3 | 81 | 9 | 1 | 2 | 33 |
| 3,2 | 512 | 37 | 1 | 2 | 152 |
| 3,3 | 19,683 | 729 | 1 | 2 | 2,355 |
| 4,2 | 65,536 | 829 | 1 | 2 | 8,800 |

For every target in every box, the program checks:

1. the literal indegree against the proper-colouring sum;
2. the refinement by the labelled diagonal occupation vector;
3. diagonal-zero and (q)-colourable support image membership;
4. image size by an independent sum over simple support graphs;
5. square-zero dynamics and exact depth layers; and
6. uniqueness of the maximal zero fibre.

## V02 hostile boxes

| (m) | states | image | fixed | 3-cycles | zero fibre | depth 2 |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 8 | 2 | 2 | 0 | 7 | 0 |
| 2 | 64 | 24 | 3 | 2 | 38 | 18 |
| 3 | 512 | 149 | 5 | 20 | 196 | 252 |
| 4 | 4,096 | 873 | 9 | 168 | 1,064 | 2,520 |
| 5 | 32,768 | 5,585 | 17 | 1,360 | 6,352 | 22,320 |

For every state, the program checks rotation on the all-dot-one core or
second-iterate collapse outside it.  For every target, it checks the exact
fibre formula by number of nonzero coordinates, pairwise dot products,
equality type, and the odd/even radical split.  The theorem passes; the
candidate is killed for internal proof-engine collision, not a failed formula.

## Breadth controls

The other sixteen maps are exhaustively scanned in the parameter boxes
listed in `CANONICAL.txt`.  Their purpose is early falsification and mechanism
diversity: vector cross-products, matrix Hadamard feedback, determinant
triggers, Gram defects, mixed matrix words, triangular commutators, companion
folds, permutation conjugation, directly owned Hurwitz and product-exchange
controls, and two finite-field polynomial maps.  None is promoted from a
small-box anomaly.
