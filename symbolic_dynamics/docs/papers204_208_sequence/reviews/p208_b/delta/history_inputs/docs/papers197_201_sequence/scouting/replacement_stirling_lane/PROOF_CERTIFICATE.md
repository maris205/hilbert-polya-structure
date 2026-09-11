# FOSP proof certificate

This file proves the theorem contract without using finite enumeration.
`verify_fosp.py` is an independent falsification certificate.

## Lemma 1: the literal update is a self-map

Use the standard contour encoding of an increasing plane tree rooted at `0`.
The two occurrences of a vertex label delimit exactly the contour traversal
of its subtree.  Since labels increase away from the root, the contour word
is a Stirling permutation, and every Stirling permutation has a unique such
tree.

Vertex `1` is necessarily a child of root `0`.  Delete it and splice its
ordered children into the root child list.  Decrementing all other positive
labels preserves every strict parent-child inequality.  The new largest
label `n` may be inserted as a leaf at any tree gap, in particular at the
vacated root slot.  The result is therefore another increasing plane tree.
Reading its contour gives exactly

```text
A 1 B 1 C  ->  dec(A) n n dec(B) dec(C).
```

This proves closure and also shows that the positional convention is literal:
the new leaf precedes precisely the children promoted out of vertex `1`.

## Lemma 2: transport of the internal-label set

A label is internal exactly when its two contour occurrences are nonadjacent.
Deleting vertex `1` removes its internal/leaf status.  Every old vertex
`j>=2` retains its entire ordered child list and receives label `j-1`; the new
vertex `n` is a leaf.  Hence

```text
I(Tw)={j-1:j in I(w),j>=2}.
```

Taking maxima with `max(empty)=0` gives

```text
tau(Tw)=max(tau(w)-1,0).                             (2.1)
```

After exactly `tau(w)` updates there are no internal nonroot vertices, so the
tree is a star.  If `tau(w)>0`, after only `tau(w)-1` updates the old vertex
`tau(w)` has become an internal vertex labelled `1`; the tree is not yet a
star.  Thus `tau` is the exact entrance time, not merely a Lyapunov bound.
The largest label `n` is always a leaf, so `tau<=n-1`.  The word in (2.4) of
the contract makes `n-1` internal and witnesses equality.

## Lemma 3: depth CDF by protected insertion gaps

Every order-`k` Stirling permutation is obtained uniquely by inserting the
adjacent pair `k k` into one of the `2k-1` gaps of an order-`k-1` word.
Fix `0<=t<=n-1`.  The condition `tau<=t` says that all labels
`t+1,...,n` remain leaves, or equivalently that none of their internal pair
gaps is used at a later insertion.

For `k<=t`, all `2k-1` gaps are allowed.  Just before inserting `k>t`, the
already protected adjacent pairs are `t+1,...,k-1`; their `k-t-1` internal
gaps are forbidden.  The number of allowed gaps is therefore

```text
(2k-1)-(k-t-1)=k+t.
```

Multiplication gives

```text
F_n(t)
 = product_(k=1)^t (2k-1) product_(k=t+1)^n (k+t)
 = (2t-1)!! (n+t)!/(2t)!
 = (n+t)!/(2^t t!).                                 (3.1)
```

An exact layer is obtained by set difference:

```text
#{tau=t}=F_n(t)-F_n(t-1),  F_n(-1)=0.               (3.2)
```

In particular `F_n(0)=n!`, the number of stars, while
`F_n(n-1)=(2n-1)!!`, the whole carrier.  This explicitly separates the CDF
from the exact-depth enumerator.

## Lemma 4: recurrent action and exact periods

On a star, the root child slots do not move.  The label at each slot changes
by the cycle

```text
c(1)=n,       c(j)=j-1 for j>=2.                    (4.1)
```

For `n>=2`, `c` is an `n`-cycle and every star uses every label.  Therefore
every recurrent orbit has exact period `n`, not a proper divisor.  The `n!`
stars form `(n-1)!` cycles.  For `n=0,1`, direct inspection gives one fixed
point.  Lemma 2 makes the stars globally attracting, so no point outside the
stars can be recurrent.

## Lemma 5: one-step image and its closed count

Every output has the newly inserted vertex `n` as a root leaf.  Conversely,
given any target with `n` a root leaf, remove that leaf, increment all labels,
and insert a new root child `1` at the vacated slot without adopting any
subsequent root subtree.  This is a predecessor.  Thus the image criterion is
exact.

It remains to count such targets.  For `m>=0`, let

```text
R_m(z)=sum_T z^(d_0(T)+1),                           (5.1)
```

where `T` ranges over increasing plane trees with root `0` and `m` nonroot
vertices and `d_0(T)` is the root outdegree.  A tree with exponent
`e=d_0+1` has `2m+1` leaf-insertion gaps: `e` root gaps increase the exponent
to `e+1`, and the other `2m+1-e` gaps leave it unchanged.  Hence

```text
R_0(z)=z,
R_(m+1)(z)=z(z-1)R_m'(z)+(2m+1)R_m(z).              (5.2)
```

Differentiate (5.2) and set `z=1`:

```text
R_(m+1)'(1)=(2m+2)R_m'(1),       R_0'(1)=1.         (5.3)
```

Therefore

```text
R_m'(1)=2^m m!.                                     (5.4)
```

Deleting root leaf `n` from an image target leaves an arbitrary order-`n-1`
tree; it records one of that tree's `d_0+1` root gaps.  Thus the number of
image targets is

```text
R_(n-1)'(1)=2^(n-1)(n-1)!.                          (5.5)
```

The verifier separately constructs the polynomials in (5.2) and checks both
their total `(2m-1)!!` and the derivative (5.4).

## Lemma 6: complete inverse atlas

Let the target root child list be

```text
(..., n, c_1,...,c_r),                              (6.1)
```

where `n` is a leaf.  In a predecessor, the deleted vertex `1` occupied the
slot now occupied by `n`.  Its former children appear, in their original
order, immediately after `n`; the old root children that originally followed
`1` then continue in the same list.  Thus a reverse step is specified by the
unique cut between those two groups.

There are exactly `r+1` cuts.  For cut `k`, remove `n`, increment every
surviving label, insert root child `1` at that slot, and make it adopt
`c_1,...,c_k`.  Each result is increasing, the results are distinct, and a
forward update recovers the target.  Conversely every predecessor determines
exactly this `k`.  This proves

```text
|T^(-1)(y)|=r+1.                                    (6.2)
```

If `n` is not a root leaf there is no predecessor by Lemma 5.  Formula (6.2)
therefore covers every labelled target, including empty fibres.

Since `r+1<=n`, the maximum fibre is `n`.  Equality forces `r=n-1`: all
vertices are root children and `n` is first.  Conversely each such ordered
star has fibre `n`.  Permuting the other labels gives exactly `(n-1)!`
maximizers.  This also proves the requested classification of all maximum-
fibre targets, not merely their number.

## Independence of the proof axes

The temporal proof uses transport of the nonleaf-label set and protected
growth gaps.  The inverse proof uses a target-side root-list cut.  The image
count uses a root-degree catalytic polynomial.  None is obtained by summing a
finite orbit table, and the target atlas is not inferred from the temporal
clock.  Classical carrier enumeration and the contour bijection remain
zero-credit background.

## Boundary audit

- `n=0`: the empty word is fixed; state, image, recurrent set, unique fibre,
  and unique maximizer all have size one; depth and maximum tail are zero.
- `n=1`: `11` is fixed; the image formula gives `1`, maximum fibre `1`, and
  the sole star has `1` first; depth is zero.
- `n=2`: the words are `1122,1221,2211`; the first and last form the star
  2-cycle, `1221` maps into it, the image has size two, depth layers are
  `(2,1)`, and the unique maximum-fibre target is the star beginning with
  `22`.

