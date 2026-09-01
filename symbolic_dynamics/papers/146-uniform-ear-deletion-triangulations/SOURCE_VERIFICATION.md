# Source verification and closest-owner gate — P146

Checked 2026-09-01 UTC.  This is owner subtraction, not novelty or release
clearance.

## Verified primary records

1. Günther Eder, Martin Held, and Peter Palfrader, “Parallelized Ear Clipping
   for the Triangulation and Constrained Delaunay Triangulation of Polygons,”
   Computational Geometry 73 (2018), 15–23,
   DOI 10.1016/j.comgeo.2018.01.004.  The
   [publisher record](https://doi.org/10.1016/j.comgeo.2018.01.004) verifies
   the full names, volume, pages, and algorithmic ear-clipping scope.
2. Alon Regev, “A Bijection Between Triangulations and 312-Avoiding
   Permutations,” arXiv:1311.1955.  The
   [primary manuscript](https://arxiv.org/abs/1311.1955) defines a
   smallest-labelled ear clip sequence and proves its triangulation
   bijection.
3. Anders Björner and Michelle L. Wachs, “q-Hook Length Formulas for
   Forests,” Journal of Combinatorial Theory, Series A 52(2) (1989), 165–187,
   DOI 10.1016/0097-3165(89)90028-9.  The
   [publisher record](https://doi.org/10.1016/0097-3165(89)90028-9)
   explicitly identifies the rooted-forest linear-extension hook formula as
   classical input.
4. Tomás M. Coronado, Joan Carles Pons, and Gabriel Riera, “Counting Cherry
   Reduction Sequences in Phylogenetic Tree-Child Networks is Counting Linear
   Extensions,” Bulletin of Mathematical Biology 86 (2024), article 146,
   DOI 10.1007/s11538-024-01374-1.  The
   [publisher-hosted text](https://doi.org/10.1007/s11538-024-01374-1)
   gives an explicit reduction-sequence/linear-extension bijection in a
   different carrier.

## Claim-by-claim overlap decisions

| source lane | directly owned input | not supplied by that source |
|---|---|---|
| Eder–Held–Palfrader | ear clipping as a polygon-triangulation algorithm | uniform-current-vertex endpoint distribution |
| Regev | deterministic labelled clip sequence and triangulation bijection | all deletion histories, final-face masses, or random endpoint law |
| Björner–Wachs | rooted-tree/forest hook count for linear extensions | the polygon-history to root-face poset identification or sum over final faces |
| Coronado–Pons–Riera | a reduction-history/linear-extension bijection in phylogenetic networks | polygon ears, weak-dual endpoint law, or the unrooted sharp minimum |

The manuscript therefore gives zero credit to ear clipping, weak duals,
generic reduction-to-linear-extension ideas, and the forest hook formula.
The remaining internal package is only the uniform-current-vertex root-face
law, its endpoint aggregation, and the elementary unrooted leaf-order minimum
with path equality.  The final induction is short and may be folklore; the
package is explicitly owner-thin.

Bounded searches included “random ear clipping triangulation distribution,”
“ear removal sequences dual tree,” “triangulation shelling orders hook
formula,” and “tree leaf removal order count.”  No inspected primary source
stated the complete residual conjunction.  This non-hit is not novelty,
priority, ownership, or freedom-to-operate evidence.  Status remains
HOLD_EXTERNAL.
