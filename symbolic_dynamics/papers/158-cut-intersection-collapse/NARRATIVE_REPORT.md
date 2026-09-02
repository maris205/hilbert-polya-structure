# Narrative report — P158 cut-intersection collapse

**Status:** `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.

## One-sentence result

Intersecting `K_n` with fresh independent fair vertex cuts has an exact
all-time absorption law and a complete labelled target atlas because an edge
survives precisely between vertices with complementary binary histories.

## Organizing invariant

After `t` epochs, every vertex carries a `t`-bit word.  The `2^t` words form
`R=2^(t-1)` distinguished complementary pairs.  A pair occupied on both sides
creates one connected complete bipartite component.  A pair occupied on only
one side contributes isolates.  This occupancy profile is the invariant used
on both theorem axes.

The empty target gives the absorption CDF through

```text
A_R(n)=n![x^n](2e^x-1)^R.
```

For a fixed labelled target with `r` nontrivial complete-bipartite components
and `z` isolates, reserving distinct oriented complementary pairs gives

```text
(R)_r 2^r A_(R-r)(z).
```

This formula exposes a necessary resource boundary: if `r=R`, any isolate
forces a zero fibre.  In particular, for `n=5,t=2`, two disjoint edges plus
one isolate are not attainable.

## Claim hierarchy

1. The every-labelled-target fibre, including all zero fibres, is the central
   result.
2. The absorption CDF, first-hit law, and exact mean series form the temporal
   axis.
3. The corrected image criterion and labelled image EGF are structural
   corollaries.
4. The union-bound tail is a supporting absorption certificate, not a
   contribution claim.

## Evidence state

The paper-local verifier compares literal successive intersections with the
complement-word graph for every history and enumerates every labelled simple
target in the frozen boxes.  It performs 77,530 exact assertions and preserves
the canonical transcript at SHA-256
`3e69dfb7d0653c140f2945a6fe4888afc569756a25acf20c1e7eaf2d9f432f0d`.
The computation is finite falsification pressure only.

## Ownership and limits

Graph cuts, complete-bipartite graph terminology, bicluster graphs, random
item-assignment graph language, labelled EGFs, and inclusion–exclusion are
owned inputs and receive zero credit.  The bounded source screen is neither a
novelty statement nor release clearance.  The paper is restricted to fair
independent cuts, a labelled complete initial graph, and finite labelled
fibres.  External status remains `HOLD_EXTERNAL`.
