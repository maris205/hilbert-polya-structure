# Bounded primary / authoritative owner check

**Run date:** 2026-09-04 UTC  
**Scope:** RX01 only, because all other denominator rows were killed before
the external-owner gate.  Search non-hits are not novelty evidence.

## Reproducible queries

The bounded web search used these exact query strings in three groups of four:

```text
"farthest vertex map" tree iteration graph
"antipodal map" tree graph farthest vertex
site:arxiv.org tree "farthest vertex" dynamics
site:doi.org tree graph "farthest-point map"

graph theory "farthest neighbor" map tree vertex
graph theory "farthest vertex" mapping tree diameter endpoints
"farthest point" map finite tree metric
"farthest-point map" graph vertices

site:atcoder.jp/contests/abc428/tasks abc428_e farthest vertex
site:atcoder.jp "Farthest Vertex" tree maximum label
site:arxiv.org "farthest node" "diameter endpoints" tree all vertices
site:dl.acm.org tree farthest vertex all vertices diameter endpoints
```

A final four-query context check used:

```text
tree eccentricities diameter endpoints theorem paper Harary graph eccentricity tree
"eccentricities of vertices in a tree" diameter endpoints paper
site:doi.org eccentricity tree diameter endpoints algorithm
site:arxiv.org tree eccentricity diameter endpoint all vertices
```

## Source ledger

| Source | What it owns | Effect on RX01 |
|---|---|---|
| [AtCoder Beginner Contest 428 E, *Farthest Vertex*](https://atcoder.jp/contests/abc428/tasks/abc428_e?lang=en) | On a labelled tree, for every vertex `v`, output the farthest vertex, breaking ties by the greatest label.  This is the complete pointwise map on the same carrier. | **Direct literal hit.** Reversing the label order conjugates greatest-label tie breaking to RX01's least-label rule. |
| [Official ABC428 E editorial](https://atcoder.jp/contests/abc428/editorial/14247) | A fixed diameter pair contains a farthest vertex for every root; an infinitesimal label perturbation makes the desired tie-broken farthest point unique; all answers follow in linear time. | **Direct proof-route hit.** It owns both the two-endpoint decoder and the tie-breaking perturbation used by the candidate spike. |
| [Farzan--Waller, *Antipodal Embeddings of Graphs*](https://doi.org/10.1112/jlms/s2-15.3.377) | Classical “antipodal graph” terminology under a unique diameter-distance antipode. | Adjacent terminology only; not the labelled-tree iteration.  It prevents broad antipodal-language ownership claims but is not the decisive kill. |
| [Wang, *Farthest Point Map on a Centrally Symmetric Convex Polyhedron*](https://arxiv.org/abs/1802.06934) | Iteration of a farthest-point map in a continuous polyhedral metric setting. | Different carrier and conclusions; recorded to delimit the query, not used as the kill. |

The searches also surfaced standard two-sweep tree-diameter notes, tree
eccentricity papers, and farthest-point maps on surfaces.  No journal/arXiv
hit in this bounded pass stated RX01's centre-cut fibre sizes or deterministic
transition spectrum verbatim.  That non-hit does **not** rescue the candidate:
once the official task/editorial's complete map and two-endpoint proof are
subtracted, those statements are immediate consequences of a rank-two
functional graph.

## Decision and lifecycle

`RX01 = KILL_DIRECT_OWNER`.

Therefore the replacement pass has no survivor.  Status is
**`EMPTY / HOLD_EXTERNAL`**: empty means no candidate advances internally;
`HOLD_EXTERNAL` records that this bounded search is not a global novelty
opinion.  No paper number, title, author slot, or external priority statement
is authorised.
