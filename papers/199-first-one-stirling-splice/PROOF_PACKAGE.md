# P199 proof dependency and boundary certificate

The complete proof is in main.tex, not deferred to finite enumeration.

1. Pair-interval nesting constructs the contour tree. Vertex one is a
   root child. Its surgery proves closure and exact first-gap convention.
2. Each surviving ordered child list remains unchanged. Thus the internal
   labels transport by j to j−1, deleting one. The maximum equals the
   first star entrance, not only a Lyapunov upper bound.
3. The star slots stay fixed, so a return fixes an n-cycle label action.
   Every recurrent period is exactly n for n>=2.
4. Unique insertion of kk has 2k−1 gaps. Above threshold t, exactly
   k−t−1 protected internal gaps are forbidden. The resulting product
   simplifies to (n+t)!/(2^t t!).
5. Every source of a target is a single cut after root leaf n. The
   restored one adopts the cut's prefix. No source is omitted and
   different cuts have different child counts.
6. Maximum n means n−1 children follow n; hence exactly stars beginning
   with n. Root-degree derivative recurrence counts all image targets.

Boundary checks: empty fixed word with unique fibre/maximizer; singleton
11 fixed; at n=2 a star 2-cycle plus 1221 entering it, layers (2,1).
The maximum label is always a leaf, so adjacency alone is not the image
test. No all-time inverse claim, asymptotic theorem or external priority
claim is supported by this package.

Source subtraction and proof are logically separate. Equality T=c J_1
is a derivation from the cited definition, not a result attributed to
Brualdi–Dahl. Relabelling c alone is not a Stirling self-map.
