# Cartesian breadth-first map: complete mathematics, internal kill

**Handle:** `Q02_CBF`  
**Status:** `KILL_INTERNAL_CARTESIAN_TRAVERSAL / HOLD_EXTERNAL`.

This note records a correct theorem so that the calculation is reusable as a
negative control.  It is **not** a paper proposal.  The final section explains
why the theorem package fails the P1--P171 proof-transfer firewall.

## 1. Literal autonomous map

For a permutation `w` of `[n]`, let `C(w)` be its min-Cartesian tree: its
inorder traversal is `w`, its root is the least letter of `w`, and the two
subtrees are obtained recursively from the words to the left and right of
that least letter.  Define

```text
Phi_n(w) = labels of C(w) in breadth-first, left-before-right order.
```

This is a deterministic self-map of `S_n`.  It is not the preorder map used
in the earlier P142 scout; the distinction is literal, but ultimately not
enough for paper allocation.

Write `ell(w)` for the largest `k` such that `w_1...w_k=1...k`.

## 2. Sharp clock and recurrence theorem

### Theorem 2.1

For every `n>=1`:

1. `Phi_n(w) <=_lex w` for every `w`;
2. if `w` is not the identity, then
   `ell(Phi_n(w)) >= ell(w)+1`;
3. the identity is the unique periodic point;
4. every orbit reaches it in at most `n-1` steps, and this bound is sharp.

### Proof

The root of `C(w)` is 1, so if `w_1` is not 1 then the first output letter
already proves strict lexicographic decrease.  If `w_1=1`, the root has no
left child and its right subtree is `C(w_2...w_n)`.  Breadth-first reading
therefore gives

```text
Phi_n(w) = 1 Phi_(n-1)(w_2...w_n),
```

with the evident standardisation of the suffix.  Induction proves the first
claim.

Now suppose `ell(w)=k<n`.  The letters `1,2,...,k` occur consecutively at the
beginning.  Recursing at successive minima shows that they form a unary
right-child chain at the top of `C(w)`.  The remaining subtree is rooted at
`k+1`.  Since no other vertex occurs on any of the first `k` levels,
breadth-first reading starts with

```text
1,2,...,k,k+1.
```

Thus the identity prefix grows by at least one at each nonfixed step.  This
excludes every nontrivial cycle and gives the upper bound `n-1`.

For sharpness, set

```text
w_t = (1,2,...,t,n,t+1,t+2,...,n-1),    0<=t<=n-1.
```

The first `t` letters again make a unary right chain.  In the remaining
subtree, `t+1` is the root, `n` is its left child, and
`t+2,...,n-1` is its unary right chain.  Hence

```text
Phi_n(w_t)=w_(t+1).
```

The source `w_0=(n,1,2,...,n-1)` therefore has depth exactly `n-1`.  This
proves all four claims.  `square`

## 3. Every-target fibre theorem

Let `B_n` be the set of ordered binary-tree shapes with `n` vertices.  For a
target permutation `y`, label the vertices of a shape `T` by `y` in
breadth-first left-before-right order.  Call `T` *compatible with y* if every
parent label is smaller than each child label.

### Theorem 3.1

For every `y in S_n`,

```text
|Phi_n^(-1)(y)| = #{T in B_n : T is compatible with y}.       (3.1)
```

Consequently every fibre is at most the Catalan number

```text
Cat_n = binom(2n,n)/(n+1),
```

and equality holds at the identity target.

### Proof

Given a compatible shape, read its breadth-first labels from `y` and read
the same labelled tree inorder to obtain a unique source word `w`.  The
compatibility inequalities say precisely that the labelled tree is a
min-heap.  The uniqueness characterization of Cartesian trees now gives
`C(w)=T`, so `Phi_n(w)=y`.

Conversely, the Cartesian tree of every source in the fibre is one of these
compatible shapes, and its inorder word recovers the source.  The two
constructions are inverse.  There are `Cat_n` ordered binary shapes in total.
When `y=12...n`, parents precede children in breadth-first order and therefore
have smaller labels, so every shape is compatible.  `square`

### An evaluable target DP

Formula (3.1) is not merely existential.  A FIFO queue gives an exact dynamic
program.  A queue entry stores the label of the parent that created a pending
child slot.  Start with the sentinel queue `(0)`.  When reading target letter
`y_i`, pop the front label `p`; reject the state unless `p<y_i`; then append
zero, one, or two copies of `y_i`.  The multiplicities for these choices are

```text
0 children: 1,    1 child: 2 (left or right),    2 children: 1.
```

After all letters, retain only the empty queue.  Its accumulated weight is
exactly (3.1), because these choices are the BFS slot encoding of an ordered
binary shape.  This is the third, source-free construction checked by the
focused verifier.

## 4. Exact falsification pressure

`verify_cbf.py` uses three independent constructions:

1. a monotone-stack Cartesian-tree builder followed by a literal queue read;
2. recursive generation of every increasing labelled ordered binary tree,
   followed by independent inorder and breadth-first reads; and
3. the BFS-slot target DP above.

It exhausts all permutations through `S_9`.  The last three ranks are:

| `n` | states | image | sharp height | maximum fibre |
|---:|---:|---:|---:|---:|
| 7 | 5,040 | 164 | 6 | 429 |
| 8 | 40,320 | 718 | 7 | 1,430 |
| 9 | 362,880 | 3,805 | 8 | 4,862 |

The complete focused replay contains **4,730,679 assertions**.  Enumeration
checks the implementation and searches for counterexamples; the proofs above
carry the all-rank statements.

## 5. Decisive P1--P171 collision

The P142 combinatorial scout already records a permanent negative control on
the same carrier: send a permutation to the **preorder** of its min-Cartesian
tree.  That control proves:

- growth of the initial identity prefix;
- a sharp `n-1` convergence clock and the same witness family;
- unique identity recurrence;
- an every-target Cartesian-tree split recursion; and
- Catalan maximum fibres.

It is additionally reverse-complement conjugate to West's classical
stack-sorting map, which permanently kills the preorder literal.  That exact
conjugacy is not asserted for the breadth-first map here.  The present kill is
instead the stricter portfolio rule: changing one tree traversal leaves the
carrier, sufficient tree object, temporal potential, sharp clock, inverse
shape bijection, and Catalan extremum transferable from the P142 control.
The BFS queue DP is a neat alternate evaluator, not an independent second
theorem axis large enough to overcome that transfer.

Therefore the correct outcome is a **mathematically complete internal kill**,
not a provisional survivor and not a novelty non-hit.
