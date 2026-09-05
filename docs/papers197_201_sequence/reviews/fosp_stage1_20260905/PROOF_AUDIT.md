# FOSP: independent all-parameter proof audit

Reviewer: `/root/batch197_fosp_gate`. Date: 2026-09-05 UTC.
This is a candidate gate, not manuscript Review A or Review B.

The input hashes are in `INPUT_PINS.sha256`. No author file was changed.

## Definition and closure

For `w = A 1 B 1 C`, the frozen output is `dec(A) nn dec(B) dec(C)`.
The first `1` is always encountered at contour depth zero: otherwise the
containing label would be smaller than 1. Thus the old first-1 gap is a root
gap, even when A is nonempty. Every old label greater than 1 occurs twice in
exactly one of A, B, C; a label cannot straddle a 1. Each surviving pair
therefore retains the Stirling inequality after removal and decrement, and
the new largest pair is adjacent at depth zero. This proves closure without
assuming the claimed tree description.

In the tree representation the output root list replaces child 1 by a leaf n
followed by the old children of 1, with old labels decremented. Old vertex
`j >= 2` keeps its own entire child list; only its parent can change. This
distinction verifies the proof's key premise. A left-join at an arbitrary
nonroot vertex is already a known local operation; see `SOURCE_AUDIT.md`.

## Point tail and recurrence

Let `I` be the nonempty-child labels, excluding root 0. Each old nonroot
child list above is preserved, the old vertex 1 disappears, and the newly
inserted vertex n is a leaf. Hence `I(Tw) = {j-1: j in I(w), j>1}`.
Iteration gives `I(T^t w) = {j-t: j in I(w), j>t}` while `t <= n-1`.
Therefore the first star epoch is exactly `max I`, with empty maximum zero.
No state outside the stars can be periodic, since its positive maximum
strictly decreases. On a star the child slots stay fixed and every label
undergoes the same n-cycle, proving exact period n for `n >= 2` and the
cycle count `(n-1)!`. There is no proper-divisor period because any fixed
slot would have to recover its original label under the label cycle.

The maximum label n must be a leaf, so the tail is at most n-1. A tree with
edge `(n-1,n)` and all other vertices as root children attains n-1. Thus
the bound is sharp, including n=1 with value zero.

## Depth CDF and exact layers

The unique maximum-insertion history has `2k-1` gaps at stage k. To have
`max I <= t`, every pair with label above t must remain adjacent. At stage
`k>t`, exactly `k-t-1` existing pair-interior gaps are protected; they are
distinct, even when protected pairs are adjacent to each other. There are
`k+t` choices. The product is

```
prod_{k=1}^t (2k-1) * prod_{k=t+1}^n (k+t)
  = (n+t)! / (2^t t!),             0 <= t <= n-1.
```

The product counts complete histories bijectively, rather than assuming
independent final adjacency events. Exact layer t is the difference of
successive CDFs; its zero baseline is `F_n(-1)=0`. At the endpoints the
CDF is `n!` and `(2n-1)!!`. All formulas and ranges in the input contract
are consistent. At n=0 the separate value one is necessary.

## Image and every labelled inverse set

Every output has n as a root leaf. Conversely, replacing such a leaf by 1
after increasing other labels gives a predecessor, so the image iff is
exact. If r root children follow n, a predecessor chooses precisely one cut
after k of these children, `0 <= k <= r`: the first k become children of
the recreated vertex 1. Any adoption skipping an intervening root child
would fail to reproduce the target order. Any adoption reaching a subtree
before n would move the first-1 gap. These exclusions prove exhaustiveness.
The r+1 choices are distinct because vertex 1 has a different child list.

Thus the fibre is zero off the image and r+1 on it. Its maximum n forces
r=n-1, which uses all vertices as root children and puts n first; conversely
every such star attains n. There are exactly `(n-1)!` such targets.

For the image count, deleting n from an image target leaves an arbitrary
order-(n-1) tree with one marked root insertion gap. If
`R_m(z) = sum z^(root_degree+1)`, maximum-leaf insertion gives
`R_{m+1}=z(z-1)R_m'+(2m+1)R_m`, `R_0=z`. Differentiation at 1 yields
`R_{m+1}'(1)=(2m+2)R_m'(1)`, hence image count
`R_{n-1}'(1)=2^(n-1)(n-1)!`. The old proof's derivative is correct; no
missing `R_m(1)` term survives differentiation. This is an independent
enumerative use of root gaps, while the point-tail argument uses nonleaf
labels and the inverse argument uses target root-list cuts.

## Boundaries and falsification design

At n=0 the empty tree has one state, one image, one fixed point, one
predecessor, zero tail. At n=1 the sole tree is a star and fixed; the general
image and maximum-fibre formulas give one. At n=2 the three words are
`1122`, `1221`, `2211`: the first and last form the 2-cycle, and the middle
has tail one and maps to `2211`, whose fibre is two.

`verify_independent.py` generates ordered child arrays, applies root surgery,
constructs the entire functional graph, and computes tails and cycle lengths
using indegree peeling. It never uses the claimed clock to decide recurrence
or tail. It compares the **entire** inverse set against cut reconstruction,
checks the word/tree dictionary, CDF, exact layers, image and mass, and all
maximizers. All 146,600 states across n=0,...,7 pass 1,496,779 assertions per
run. Joins' commutation/idempotence are additionally checked through n=5;
the local source factor `T=c J_1` is checked through n=7. This bounded
evidence supports falsification only; the deductions above establish the
all-parameter results.

Mathematical finding census: Critical 0, Major 0, Minor 0.
The independent source audit has a separate Major documentation finding.
