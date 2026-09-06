# FOSP theorem contract

Status: `PROMOTE_SPIKE / OWNER_AMBER / HOLD_EXTERNAL`.

This is an internal theorem candidate, not a novelty, priority, authorship,
venue, or release claim.  Stirling-permutation enumeration, adjacent insertion
of the maximum pair, the contour bijection with increasing plane trees, and
generic promotion language receive zero contribution credit.

## 1. Literal map and frozen boundaries

For `n>=0`, let `Q_n` be the set of words on the multiset

```text
{1,1,2,2,...,n,n}
```

such that every entry strictly between the two copies of `j` is greater than
`j`.  Thus `Q_0={()}` and `Q_1={(1,1)}`.

For `n>=2`, write the unique decomposition at the two copies of `1` as

```text
w = A 1 B 1 C.
```

Delete those two copies, decrement every surviving entry by one, and insert
the adjacent pair `n n` in the gap formerly immediately before the first
copy of `1`:

```text
T_n(w) = dec(A) n n dec(B) dec(C),                 (1.1)
dec(j)=j-1.
```

Equivalently, if the first copy of `1` is at zero-based position `p`, form
`u` by deleting both copies of `1` and decrementing the remaining letters,
then set `T_n(w)=u[:p]+(n,n)+u[p:]`.  This positional rule freezes the gap;
there is no choice, tie, scan continuation, or asynchronous update.  Set

```text
T_0(())=(),             T_1((1,1))=(1,1).          (1.2)
```

We call (1.1) **first-occurrence Stirling promotion (FOSP)** only as a local
handle.  The name supplies no originality claim and cannot evade a direct
owner of the literal map.

## 2. Tree dictionary and pointwise clock

Under the standard contour bijection, `Q_n` is the set of increasing plane
trees with root `0` and nonroot vertices `1,...,n`: record a vertex label on
the downward and upward traversal of its parent edge.  Formula (1.1) becomes:

1. vertex `1`, necessarily a root child, is deleted;
2. its ordered children are spliced into the root child list at its old slot;
3. every old label `j>=2` is changed to `j-1`;
4. a new root leaf labelled `n` is inserted at the same slot, immediately
   before the spliced children.

This is a proof model for the frozen word rule, not an alternative scheduler.

Let

```text
I(w)={j : the two copies of j in w are not adjacent},
tau(w)=max I(w), with max(empty)=0.                 (2.1)
```

Thus `I(w)` is the set of nonleaf labels in the tree.

### Theorem A: exact all-parameter temporal axis

For every `n>=0` and `w in Q_n`:

```text
I(T_n w)={j-1 : j in I(w), j>=2},                  (2.2)
tau(T_n w)=max(tau(w)-1,0).                         (2.3)
```

Consequently `tau(w)` is the exact entrance time into the recurrent set.
For `n>=1` the sharp maximum tail is `n-1`; for `n=0` it is zero.  A witness
for `n>=2` is

```text
11 22 ... (n-2)(n-2) (n-1) n n (n-1).             (2.4)
```

For `0<=t<=n-1`, define the depth CDF

```text
F_n(t)=#{w in Q_n : tau(w)<=t}=(n+t)!/(2^t t!).    (2.5)
```

The exact depth-`t` layer is instead

```text
E_n(t)=F_n(t)-F_n(t-1),   F_n(-1)=0.                (2.6)
```

Equations (2.5) and (2.6) must not be interchanged.  At `n=0`, separately,
`F_0(0)=E_0(0)=1`.

The recurrent states are exactly the ordered stars, equivalently the words

```text
pi_1 pi_1 pi_2 pi_2 ... pi_n pi_n,   pi in S_n.    (2.7)
```

There are `n!` of them.  At fixed child slots, `T_n` applies the label cycle
`1 -> n` and `j -> j-1` for `j>1`.  Hence:

- `n=0,1`: one fixed point and one cycle of length one;
- `n>=2`: every recurrent point has exact period `n`, there are `(n-1)!`
  cycles, and there are no fixed points.

The carrier count is the standard

```text
|Q_n|=(2n-1)!!, with (-1)!!=1.                     (2.8)
```

## 3. Exact one-step image

For a target `y`, factor its contour word into its maximal depth-zero blocks.
Their opening labels, in order, are the root children.  Then

```text
y in im(T_n)  iff  vertex n is a root leaf          (3.1)
```

for `n>=1`; the empty target is in the image at `n=0`.  In word language,
the adjacent block `n n` must itself be a maximal depth-zero block.

The image has the closed form

```text
|im(T_0)|=1,
|im(T_n)|=2^(n-1)(n-1)!        for n>=1.            (3.2)
```

This is a one-step image theorem.  No closed form for every iterated image is
claimed here.

## 4. Every-target one-step fibre and all maximizers

Suppose `n>=1`.  If `n` is not a root leaf of `y`, then

```text
|T_n^(-1)(y)|=0.                                    (4.1)
```

Otherwise let `r(y)` be the number of root children strictly after `n` in
the ordered root child list.  Then

```text
|T_n^(-1)(y)|=r(y)+1.                               (4.2)
```

The `r+1` predecessors are canonical: remove the root leaf `n`, increment all
remaining labels, create root child `1` at the vacated slot, and let it adopt
the first `k` subsequent root subtrees, for exactly one `k` in each of
`0,1,...,r`.

It follows that, for `n>=1`,

```text
max_y |T_n^(-1)(y)|=n.                              (4.3)
```

Moreover **all** targets attaining (4.3) are precisely the ordered stars in
which `n` is the first root child.  Their number is

```text
(n-1)!.                                             (4.4)
```

At `n=0`, the empty target is the unique maximizer and has fibre one.

## 5. Mandatory small ranks and terminal exact box

| `n` | states | image | recurrent | maximum tail | recurrent periods | cycles | max fibre | max targets |
|---:|---:|---:|---:|---:|---|---:|---:|---:|
| 0 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 1 |
| 2 | 3 | 2 | 2 | 1 | 2 | 1 | 2 | 1 |
| 8 | 2,027,025 | 645,120 | 40,320 | 7 | 8 | 5,040 | 8 | 5,040 |

The order-eight exact depth layers `t=0,...,7` are

```text
40,320; 141,120; 272,160; 378,000;
415,800; 374,220; 270,270; 135,135.                 (5.1)
```

These values are exhaustive checks, not the logical basis for Theorems A or
the inverse atlas.  `PROOF_CERTIFICATE.md` supplies the all-parameter proof,
and `verify_fosp.py` independently replays every labelled state through
`n=8`.

## 6. Claim boundary

- The theorem contract claims the literal map, exact pointwise clock, depth
  CDF and layers, recurrent cycle census, one-step image count, and complete
  labelled one-step fibre atlas.
- It does not claim external novelty, first discovery, a full iterated-image
  formula, or any asymptotic distribution theorem.
- A literal/direct owner for (1.1), on words or under the standard tree
  bijection, kills the candidate.  Renaming, reversing the word, shifting
  labels, or switching between the word and tree encodings is not separation.

