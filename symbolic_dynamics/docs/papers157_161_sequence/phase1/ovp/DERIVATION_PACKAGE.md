# Derivation package — parallel odd-vertex pruning

## 1. Why the temporal bound is linear and sharp

The handshaking lemma makes the current odd-degree set `D(G)` even.  If the
state is not fixed then `|D(G)|>=2`, so every active epoch loses at least two
vertices.  This gives `tau(G)<=floor(|V(G)|/2)<=floor(n/2)`.

For the path `P_n`, the only odd vertices are its two endpoints.  Deleting
them leaves `P_(n-2)` (or the singleton/empty boundary), so exactly two
vertices disappear in every active round.  Its clock is `floor(n/2)`.

There can be no nontrivial cycle because an active step strictly decreases
the vertex set.  A state is fixed exactly when all degrees are even.

## 2. One strict inverse as a parity system

Fix a target `H` on a labelled set `S`, `|S|=s`, and a prospective deleted
set `D`, `|D|=d>0`, disjoint from `S`.  A predecessor has the edges of `H`
inside `S`; its free edge variables are precisely

```text
E_D = {uv : at least one of u,v lies in D}.
```

For every `u in S`, impose

```text
sum_{v in D} x_uv = deg_H(u)  (mod 2),
```

so `u` has even predecessor degree.  For every `v in D`, impose

```text
sum_{w != v} x_vw = 1         (mod 2),
```

so `v` is deleted.  The sum of all right sides is `d` modulo two, since the
degree sum of `H` is even.  Hence consistency forces `d` even.

When `d` is even, the right side has total parity zero.  The variable graph
`(S union D,E_D)` is connected, and its binary incidence matrix has rank
`s+d-1`.  It has `sd+binom(d,2)` variables.  Thus a fixed `D` supports

```text
2^[sd+binom(d,2)-(s+d-1)]
 = 2^[s(d-1)+binom(d-1,2)]
```

predecessors.  Choosing `D` among the `n-s` unused labels gives `B_n(s,s+d)`.
No property of the target edge set survives except the automatically even
sum of its degree parities.  This is the source of target-uniformity.

## 3. Why powers of the transfer are literal orbit counts

Every strict predecessor has every vertex of its deleted set odd, hence is
not an even graph.  It therefore cannot wait under the map.  Consequently a
chain of `k` strict inverse steps is the unique reversal of a forward orbit
segment with `k` active epochs.  The intermediate edge patterns do not alter
the next strict-predecessor count, only their ranks do.  Matrix multiplication
of `B_n` therefore counts literal inverse chains without quotienting or
overcounting.

If `H` is non-even, a `t`-step predecessor must make exactly `t` strict
moves, giving `B_n^t`.  If `H` is even, it may enter `H` after any
`0<=k<=t` strict moves and then wait, giving `I+B_n+...+B_n^t`.

## 4. Images, fixed counts, and temporal layers

Every strict step adds a positive even number of labels in reverse.  Hence a
non-even rank-`s` target has a `t`-step predecessor iff at least `2t` ambient
labels are unused.  Sufficiency follows because every positive even transfer
entry is nonzero; take increments two at a time.  An even target is always in
every image through its fixed self-predecessor.

On a fixed `s`-set, the binary incidence map from edge indicators to degree
parities has rank `s-1` for `s>=1`; therefore its kernel contains
`e_s=2^[binom(s,2)-s+1]=2^binom(s-1,2)` even graphs.  The empty boundary has
`e_0=1`.  Multiplying the target-resolved inverse formula by
`binom(n,s)e_s` and summing over `s` yields the temporal CDF.  Successive
differences give every exact shell.
