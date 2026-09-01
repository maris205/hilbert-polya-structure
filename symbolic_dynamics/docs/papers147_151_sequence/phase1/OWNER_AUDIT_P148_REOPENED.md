# Reopened owner audit — P148 outward-contraction hit

**Checkpoint:** 2026-09-01 UTC  
**Trigger:** independent Hostile Review A  
**External status:** `HOLD_EXTERNAL`

## Direct primary owner

Khí-Uí Soo, Bakhadyr Khoussainov, and Simone Linz, *Quasi-Isometric Graph
Simplifications*, [`arXiv:2111.13238v4`](https://arxiv.org/abs/2111.13238),
Definition 6.6, defines outward-contraction on a rooted finite tree.  Each
even-level vertex is grouped with all downward odd-level neighbours and the
output is the corresponding partition-tree.

Let `For` forget the order of children in a plane rooted tree and retain the
root.  Direct inspection of Definition 6.6 gives

```text
For(E(T)) is naturally isomorphic to
outward-contraction(For(T), root(T)).
```

The quotient supervertices are indexed by original even-depth vertices.  An
edge between supervertices crosses from an odd child to one of its original
even-depth children, so it joins an even vertex to an original grandchild.
This is exactly the unordered shadow of one P148 update.

## Mandatory subtraction

The following are now direct-owned and receive zero contribution credit:

1. the unordered rooted one-step rule;
2. its partition-tree interpretation;
3. grouping an even vertex with its odd children; and
4. bare one-step height compression; and
5. the cheap unordered all-rank depth/clock consequences obtained by
   iterating the owner.

The owner paper studies quasi-isometric simplification and preservation of
tree centres/medians.  Its inspected text does not state a plane-order lift,
an iterated `2^k` depth-divisibility theorem, a target-resolved inverse, an
exact-size image criterion, or the algebraic image series.

## Reference and later-citation screen

The complete reference list of the v4 primary manuscript was screened.  It
contains graph contraction, graph summarization, partitioning, metric
embedding, spanners, centrality, and tree-optimization sources; no cited item
was an iterated outward-contraction or plane-tree inverse enumeration.

Follow-up query lanes were recorded exactly:

```text
"outward-contraction"
"outward contraction"
iterated outward contraction tree
plane rooted tree odd level contraction promotion grandchildren
partition-tree inverse enumeration contraction
works citing arXiv:2111.13238
```

The audit used arXiv primary records/full text, Crossref DOI/publisher
metadata, candidate primary reference lists, and OpenAlex only as a discovery
index for later citations.  The exact arXiv phrase lane returned no second
primary paper; the citation-discovery entry reported zero later citing works
at this checkpoint.  These are bounded non-hits and carry no novelty,
priority, ownership, or release force.

The broader same-primitive source remains Berkemer, Höner zu Siederdissen,
and Stadler, *Mathematics in Computer Science* 15(4), 609--630 (2021),
[DOI 10.1007/s11786-020-00496-8](https://doi.org/10.1007/s11786-020-00496-8),
published online in 2020.  It owns generic ordered child promotion, not the
parity-specific iterate/fibre package.

## Repaired residual

Only the following conjunction remains eligible for internal scoring:

```text
complete plane-ordered size-refined every-target fibre
+ exact-layer image criterion and algebraic image series.
```

The manuscript now states the forgetful equivalence explicitly, exposes the
recursive inverse bijection `F_U=A_d product_j F_Uj`, corrects the
Berkemer--Höner zu Siederdissen--Stadler version-of-record metadata, and
preserves the Critical review record.  A distinct independent hostile Review
B subsequently reconstructed the forgetful equivalence, applied the stronger
unordered-iterate subtraction above, and accepted the narrowed package with
0 Critical / 0 Major / 0 Minor.  P148 is therefore `GO_INTERNAL AFTER OWNER
REPAIR`; external release remains prohibited.
