# Site-indexed circular parking displacement: closed spike and owner kill

Date: 2026-09-05 UTC. Status: **KILL_OWNER_TRANSFER / HOLD_EXTERNAL**.
These correct claims are archived as a negative result. They do not fill a
paper slot. CPD outputs car-indexed displacement; the distinct CSPD map below
outputs site-indexed displacement. They must not be conflated.

## Map and exact temporal theorem

Let `X_n={0,...,n-1}^n`. Cars `0,...,n-1` arrive in order at a circular
clockwise `n`-site park with preferences `a_i`. Every car parks at the first
free site. If car `i` parks at site `s` after passing `d` occupied sites,
set `S(a)_s=d`. Empty the park before the next epoch.

Let `I_n={d:0<=d_i<=i}` and let `PF_n` be the classical zero-based parking
functions, equivalently the words whose sorted entries satisfy `a_(i)<=i`.
Then

```
S(X_n) subset PF_n,
S^{-1}(I_n)=PF_n,
S|I_n=C,  C(d)_i=i-d_i,
S^2(X_n)=I_n,  S^4=S^2.
```

The recurrent set is `I_n`, with `n!/2` strict two-cycles for `n>=2`.
The exact tail is zero on `I_n`, one on `PF_n\I_n`, and two elsewhere.
The three depth populations are

```
n!, (n+1)^(n-1)-n!, n^n-(n+1)^(n-1).
```

At `n=1`, the sole point is fixed and both positive-depth counts vanish.

Proof. The displacement of car `i` is at most `i`, so the first output is
a permutation of an inversion sequence. Such a word is a classical parking
function. A circular parking preference is classical iff no car wraps past
site `n-1`. No wrap is equivalent, site by site, to displacement at site `s`
being at most `s`, proving the inverse-image characterization. On `I_n`,
car `i` parks at `i` by induction and gives coordinate complement. The
image, recurrence and exact depths follow. The classical parking count is
background, not a newly proved enumeration here.

## Every target fibre is a forest hook product

For `d in X_n`, form a directed constraint graph `Q_d` on the sites. For
each site `s`, put an arc `j -> s` for each cyclic site

```
j=s-d_s, s-d_s+1, ..., s-1  (mod n).
```

Then `d` is in `im S` iff `Q_d` is acyclic. If it is acyclic, its
reachability order is a rooted forest order, with descendants preceding
ancestors. Let `h_s` be the number of vertices in the principal lower ideal
of `s`, including `s`. Then

```
|S^{-1}(d)| = n! / product_s h_s.
```

For a cyclic `Q_d`, the fibre is zero.

Proof. A chronological order of occupied sites realizes `d` precisely when
every crossed site precedes its destination, namely when it is a linear
extension of `Q_d`. It then determines a unique preference sequence via
`preference=site-displacement (mod n)`. Distinct linear extensions give
distinct preference sequences: if preferences at two sites agree, the
farther destination's required interval contains the nearer one, fixing
their chronological order.

Take a sink `c` of an acyclic constraint graph and cut the circle immediately
after `c`. No interval can cross this cut, since such an interval would
contain `c` and give an outgoing arc from the sink. In the resulting linear
order every principal ideal is a contiguous interval ending at its vertex.
Induction proves this by closing its immediate predecessor interval under
the predecessor intervals of its members. Two such ideals are disjoint or
nested: if their intervals overlap, the later endpoint has the earlier
endpoint among its predecessors. Thus every vertex has at most one parent
in the Hasse diagram, giving a rooted forest. The usual rooted-forest
hook-length formula now counts its linear extensions.

The maximum nonzero fibre is `n!`, uniquely at `d=(0,...,0)`. Indeed the
constraint order has all `h_s=1` exactly when it has no arcs. The minimum
nonzero fibre is one, exactly when the order is a total chain. These targets
are obtained by choosing a cyclic cut, setting its first displacement to
zero, and choosing each subsequent displacement `d_j in {1,...,j}`. The
cut is unique because these targets have exactly one zero. There are `n!`
such targets.

## Image size and indecomposable permutations

The cut argument also proves

```
im S = union of all cyclic rotations of I_n.
```

Let `a_m` count indecomposable permutations of `m` letters, defined without
external sequence lookup by

```
a_1=1,
a_m=m!-sum_{j=1}^{m-1} a_j (m-j)!.
```

Then `|im S|=a_(n+1)`.

Proof. Each linear inversion sequence factors uniquely at the cuts crossed
by no predecessor interval. The indecomposable blocks correspond to direct-
sum indecomposable permutations through the value-indexed inversion table:
`d_i` is the number of smaller entries to the right of value `i`. A block
of length `m` therefore has `a_m` possibilities. The cyclic image vectors
factor uniquely into cyclic blocks. With `A(z)=sum_{m>=1}a_m z^m`, ordinary
cyclic-block counting on labelled circular positions gives

```
b_n := |im S| = n [z^n] sum_{k>=1} A(z)^k/k.
```

This formula is valid even for rotationally periodic vectors: a word with
`k` component boundaries has exactly `k` boundary markings, while the
positioned linear decomposition has `n` starting labels.

Put `F(z)=sum_{m>=0}m! z^m`. The ordinary sequence decomposition gives
`F=1/(1-A)`, so `sum b_n z^n=z F'/F`. The factorial coefficient identity
`z^2 F'+(z-1)F+1=0` yields `zF'/F=A/z-1`, proving `b_n=a_(n+1)`.

## The binding owner transfer

The independent gate identified an explicit earlier construction in the
primary 2022 Summer@ICERM slides by Lucas Chaves Meyles, Richter Jordaan,
Sam Sehayek and Ethan Spingarn, *Parking Functions of Fixed Displacement*:

https://app.icerm.brown.edu/assets/372/4323/4323_3429_ChavesMeyles-Spingarn-Jordaan_080320221400_Slides.pdf

Their “Partition-Preserving Order” places each car's preference at its final
occupied site. Their “Algorithm” gives the interval-precedence poset and
counts its linear extensions to enumerate each normalization class. Let
that normalization be `N`. On no-wrap inputs, literally

```
S(a)=C(N(a)).
```

Every admissible circular target rotates into `I_n`. Rotating all source
preferences yields the matching rotated site target and preserves fibre
cardinality. For a target in `I_n`, all its sources have no wrap. Therefore
**every circular fibre is a rotated instance of that already owned static
normalization fibre**. The forest hook refinement uses a standard theorem
on their interval poset. The image count above is formal cyclic assembly of
the corresponding inversion-sequence block decomposition.

Consequently this spike fails the independent residual-theorem threshold:
the extra temporal layer does not free the inverse theorem from the owner
transfer. This is a mechanism/owner kill, not a claim that the exact
iterated circular self-map has been located verbatim in an earlier paper.

The internal `D05_CPA` scout additionally owns prescribed-outcome parking
reconstruction and its displacement-marked product. That map outputs the
assignment permutation, so CSPD is not a literal repeat. This distinction
does not remove the binding external normalization transfer.
