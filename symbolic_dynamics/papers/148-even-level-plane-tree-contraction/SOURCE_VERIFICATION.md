# Source verification and claim subtraction — P148

**Checked:** 2026-09-01 UTC  
**Status:** bounded primary-source audit; `HOLD_EXTERNAL`

Only primary papers, arXiv records/full text, DOI metadata, and publisher
records were used for claim decisions.  Bibliographic indices were used only
to discover candidates.  A search non-hit is not a novelty or priority
certificate.

## Verified sources

| BibTeX key | Verified primary record | Role and subtraction |
|---|---|---|
| `ChenLiShapiro2007` | Chen, Li, and Shapiro, “The Butterfly Decomposition of Plane Trees,” *Discrete Applied Mathematics* 155(17), 2187--2201 (2007), DOI [`10.1016/j.dam.2007.04.020`](https://doi.org/10.1016/j.dam.2007.04.020); author preprint [`math/0511045`](https://arxiv.org/abs/math/0511045). | Plane-tree decomposition and parity-sensitive enumerative background.  Catalan/plane-tree encodings and parity statistics receive zero credit. |
| `SooKhoussainovLinz2022` | Khí-Uí Soo, Bakhadyr Khoussainov, and Simone Linz, “Quasi-Isometric Graph Simplifications,” [`arXiv:2111.13238v4`](https://arxiv.org/abs/2111.13238), especially Definition 6.6. | **Direct structural owner.**  Outward-contraction groups each even-level vertex with all downward odd neighbours and takes the partition-tree.  Forgetting plane order makes it exactly the one-step shadow of `E`.  The unordered rule, partition-tree interpretation, and bare height compression receive zero credit.  The inspected paper does not state the ordered iterate/fibre/image conjunction. |
| `BerkemerSiederdissenStadler2021` | Berkemer, Höner zu Siederdissen, and Stadler, “Compositional Properties of Alignments,” *Mathematics in Computer Science* 15(4), 609--630 (2021), DOI [`10.1007/s11786-020-00496-8`](https://doi.org/10.1007/s11786-020-00496-8), published online 28 December 2020. | Ordered-forest deletion/contraction with child promotion.  The primitive promotion operation receives zero credit.  The bibliography uses the version-of-record issue year 2021. |
| `NicholsEtAl2020` | Nichols, Pilz, Tóth, and Zehmakan, “Transition Operations over Plane Trees,” *Discrete Mathematics* 343(8), 111929 (2020), DOI [`10.1016/j.disc.2020.111929`](https://doi.org/10.1016/j.disc.2020.111929); preprint [`1810.02839`](https://arxiv.org/abs/1810.02839). | Simultaneous plane-tree transition operations and logarithmic transformation bounds.  Generic transition language and bare logarithmicity receive zero credit. |
| `KovchegovZaliapin2016` | Kovchegov and Zaliapin, “Horton Law in Self-Similar Trees,” *Fractals* 24(2), 1650017 (2016), DOI [`10.1142/S0218348X16500171`](https://doi.org/10.1142/S0218348X16500171); preprint [`1511.01558`](https://arxiv.org/abs/1511.01558). | Repeated leaf pruning and Horton--Strahler order.  Pruning clocks and self-similar-tree terminology receive zero credit. |

## Residual boundary

The manuscript does not score the unordered one-step rule, its partition-tree
interpretation, bare height compression, Catalan counts, generic ordered-tree
contraction, even/odd level statistics, simultaneous rotation, or Horton/leaf
pruning.  With `For` denoting the order-forgetting functor, the direct overlap
is recorded pointwise as

```text
For(E(T)) = outward-contraction(For(T), root(T))
```

up to the natural rooted-tree isomorphism.  Its bounded residual is only the
conjunction

```text
plane-order lift + all-rank divisible-depth iterate law
+ sharp pointwise binary clock
+ every-target size-refined ordered block-and-gap inverse
+ exact-layer image condition and algebraic image series.
```

## Reopened owner search after the direct hit

On 2026-09-01 UTC, the audit read Definition 6.6 and the complete reference
list of the Soo--Khoussainov--Linz primary manuscript.  Its references cover
graph contraction, graph simplification, centres/medians, and metric
approximation; none inspected there concerns iteration of outward-contraction
or inverse enumeration of rooted plane-tree predecessors.  Follow-up query
lanes were:

- exact `"outward-contraction"` and `"outward contraction"`;
- `iterated outward contraction tree`;
- `plane rooted tree odd level contraction promotion grandchildren`;
- `partition-tree inverse enumeration contraction`; and
- later works citing `arXiv:2111.13238`.

The search used arXiv primary records/full text, Crossref DOI/publisher
records, and the reference lists of candidate primary papers; OpenAlex was
used only as a citation-discovery index.  The exact arXiv phrase search found
no second primary record, and the citation-discovery record reported no later
citing work at the checkpoint.  These are bounded non-hits, not proof that no
owner exists.  No inspected primary source stated the surviving ordered
iterate/fibre/image conjunction.  The direct unordered owner remains fully
credited, and neither this repair nor a second review authorizes a novelty
claim, submission, posting, specialist contact, or external release.
