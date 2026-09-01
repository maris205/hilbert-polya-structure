# Narrative report — P148

**Status: ROUND-2 INTERNAL REVIEW ACCEPTED / HOLD_EXTERNAL.**  
**Literal carrier:** `PT_{<=N}`, the finite disjoint union of plane rooted
trees with at most `N` vertices

## The map and the exact-layer distinction

At one step, retain the root and all even-depth vertices.  Delete every
odd-depth vertex and promote its ordered child block to its parent, preserving
the concatenated plane order.  Parity is then reset.  The output never has
more vertices, so the rule is a self-map of `PT_{<=N}`.  It is not a self-map
of an exact Catalan layer `PT_n`.

The exact layer matters for inverse questions.  “Image from size `n`” means
the restricted source set `PT_n` inside the finite carrier.  The formal fibre
series ranges coefficientwise over exact source sizes and is truncated at
size `N` inside any fixed carrier.

## Supporting temporal analysis — proved, but zero credit

After `k` steps, the surviving original vertices are those whose depths are
divisible by `2^k`; nearest surviving ancestors are joined and the original
contour order induces the plane order.  Thus

```text
h(E^k(T)) = floor(h(T)/2^k),
tau(T) = ceil(log2(h(T)+1)).
```

The deepest path makes the clock exact, an `n`-vertex path gives the maximum
`ceil(log2 n)`, and strict loss of depth-one vertices makes the singleton the
unique recurrent state.  These statements are correct and independently
verified.  They receive **zero contribution credit** at review closure:
once the directly owned unordered outward-contraction is iterated, the
unordered all-rank depth/clock formulas are cheap consequences.  Their
ordered restatement remains supporting analysis, not the residual paper
claim.

## Residual inverse axis

Fix a target vertex with `d` ordered children.  In a predecessor, those
children are grouped into consecutive nonempty blocks, one block for each
productive inserted odd child; arbitrary empty odd leaves occupy every gap.
If inserted odd vertices carry weight `y`, the reversible local factor is

```text
A_0(y)=1/(1-y),
A_d(y)=sum_{r=1}^d binom(d-1,r-1)y^r/(1-y)^(r+1)
      =y/(1-y)^(d+1)  (d>0).
```

For a target `U=(U_1,...,U_d)`, the repaired manuscript exposes the recursive
bijection

```text
F_U(y)=A_d(y) product_j F_{U_j}(y).
```

Multiplication over a target with `m` vertices and `I(U)` internal vertices
gives

```text
sum_{E(T)=U} y^(|T|-m)=y^I(U)/(1-y)^(2m-1).
```

Coefficient extraction yields the frozen binomial fibre formula and the
exact image condition `m+I(U)<=n` from source layer `PT_n`.

## Residual algebraic image axis

Weight a target by `z^(|U|+I(U))`.  A leaf contributes `z`; an internal root
contributes `z^2` and a nonempty ordered sequence of child trees.  Therefore

```text
H=z+z^2H/(1-H),
sum_{n>=1}|E(PT_n)|z^n=H/(1-z).
```

The first exact-layer image counts are
`1,1,2,3,5,9,17,34,71,153,338`.

## Ownership and review closure

Soo--Khoussainov--Linz, arXiv:2111.13238v4, Definition 6.6, directly owns the
unordered one-step rule.  Forgetting child order gives the exact natural
rooted-tree equivalence

```text
For(E(T)) ≅ OutContr(For(T), root(T)).
```

The unordered rule, partition-tree interpretation, generic promotion, bare
height compression, and cheap unordered all-rank consequences all receive
zero credit.  The only review-surviving conjunction is

```text
ordered every-target size-refined inverse
+ exact-layer image criterion
+ algebraic image series.
```

Hostile Review A recorded **1 Critical / 0 Major / 2 Minor**: the omitted
direct owner, compressed recursive-bijection exposition, and incorrect
Höner/year metadata.  Those defects were repaired and the owner gate was
reopened.  Independent Hostile Review B rederived the owner equivalence,
proofs, edge cases, metadata, verifier, isolated build, and all five pages,
returning **0 / 0 / 0, ACCEPT**.  The bounded owner-search non-hit is not a
novelty, priority, or freedom-to-release certificate.

## Frozen evidence

`verify_p148.py` enumerates all 23,714 plane trees through 11 vertices and
reports 216,905 exact assertions.  It checks labelled iterate skeletons,
clocks, every target/source-size fibre, local factors, exact image sets, and
the algebraic recurrence.  The canonical output passes and is byte-identical
to `verification_output.txt`; enumeration is not used as proof.

The accepted `main.pdf` is 5 A4 pages and 357,397 bytes, with SHA-256
`5c681793e5e97abb0ad718f876a2e0af11bd2d41585d860dc0c5b8c3992ed957`.
All 5/5 pages passed visual inspection, 5/5 references resolve, and a
source-only isolated build is byte-identical.  External status remains
`HOLD_EXTERNAL`.
