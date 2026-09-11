# Candidate theorem contract — Boolean Gram dynamics (`BGM`)

**Status:** `AMBER_REENTRY / NEEDS_INDEPENDENT_HOSTILE_GATE`  
**External status:** `HOLD_EXTERNAL`

## Literal system

For `n>=1`, let `X_n` be the `n x n` Boolean matrices.  Multiplication is
over the Boolean semiring and

```text
Gamma_n(A)=A A^T.
```

The rows of `A` are subsets of `[n]`; `Gamma_n(A)` is their labelled
intersection relation.  Loops are retained, so a vertex is looped exactly
when its row is nonempty.

## Forward theorem

Put `G=Gamma_n(A)`.  For every `t>=1`,

```text
Gamma_n^t(A)=G^(2^(t-1)),
```

where the right side is a Boolean relation power.  Every connected component
of `G` is reflexive on its vertices, hence repeated squaring is monotone and
eventually completes each component.  The recurrent states are therefore
exactly the partial equivalence relations: disjoint unions of fully looped
cliques, together with unlooped isolated vertices.  They are all fixed.

If `D(G)` is the largest component diameter, then

```text
depth(A)=0                                  if A is already fixed,
depth(A)=1+ceil(log_2 D(G))                 otherwise,
```

with the logarithmic contribution declared zero for `D(G)<=1`.  Thus the
sharp carrier height is zero for `n=1` and

```text
1+ceil(log_2(n-1))
```

for `n>=2`; the row--edge incidence matrix of the labelled path is sharp.
The fixed-state count is

```text
sum_(k=0)^n binom(n,k) Bell(k) = Bell(n+1).
```

Consequently the zeta function is `(1-z)^(-Bell(n+1))`.

## Independent one-step inverse theorem

A target `H` is feasible only if it is a symmetric relation and every edge
has both endpoint loops.  For such `H`, let `C(H)` consist of the empty set
and every fully looped clique of `H`, and let `E*(H)` contain each looped
singleton and each unordered edge.  For `S subseteq E*(H)`, set

```text
c_H(S)=#{C in C(H): no e in S is contained in C}.
```

Then the complete ordered-column fibre is

```text
|Gamma_n^(-1)(H)|
 = sum_(S subseteq E*(H)) (-1)^|S| c_H(S)^n.
```

The target is in the image exactly when its loop/edge requirements admit a
cover by at most `n` fully looped cliques.  This is an edge-and-loop version
of the classical intersection-number criterion.  Empty columns are allowed,
and repeated ordered columns are distinct matrix choices.

## Mandatory subtraction and boundary gates

1. Boolean matrix multiplication, row-intersection graphs, graph powers,
   diameter doubling, partial equivalence relations, Bell counts, edge clique
   covers, and inclusion--exclusion are all zero-credit ingredients.
2. P127 (binary transpose/outer-product dynamics), P143 (Boolean row
   inclusion residual), and P163 (Boolean-relation/shadow powers) are the
   closest internal papers; a manuscript must compare literal maps and proof
   engines rather than rely on different titles.
3. `n=1`, the zero matrix, targets with unlooped incident edges, isolated
   looped vertices, empty columns, and the `D<=1` convention must be tested
   explicitly.
4. The old P142--P146 reserve dossier is prior internal evidence, not a fresh
   novelty check.  Promotion requires a new independent gate and verifier
   replay against the present P1--P166 portfolio.
5. A direct owner for iteration of `A -> A A^T` over the Boolean semiring, or
   a proof transfer that consumes both the forward clock and ordered-cover
   fibres, kills the candidate.

No paper number is allocated by this contract.
