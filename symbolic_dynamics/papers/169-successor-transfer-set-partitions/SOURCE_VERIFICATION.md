# P169 primary-source verification and subtraction log

**Metadata check:** 2026-09-03 UTC  
**Gate status:** `GREEN_OWNER_THIN`  
**External lifecycle:** `HOLD_EXTERNAL`

## Literal convention fixed before search

The searched map is the following self-map of canonically ordered set
partitions of `[n]`:

```text
every nonsingleton block removes its maximum and sends that label to the
cyclic successor block, simultaneously; singleton blocks do nothing.
```

Equivalently, in the restricted-growth word, the final occurrence of every
repeated letter `i` changes to `i+1 mod k` simultaneously.  A source about
another RGF action, an unlabeled pile update, or the load projection alone
does not determine this labelled self-map.

## Verified cited records

| Key | Primary record and verified metadata | Stable surface | Role and subtraction |
|---|---|---|---|
| `Wachs1994` | Michelle L. Wachs, “σ-Restricted Growth Functions and p,q-Stirling Numbers,” *JCTA* 68(2), 470--480 (1994) | DOI `10.1016/0097-3165(94)90117-1` | RGF/set-partition encoding; zero theorem credit |
| `JosephProppRoby2025` | Michael Joseph, James Propp, Tom Roby, “Whirling Injections, Surjections, and Other Functions Between Finite Sets,” *DMTCS* 27:3 (2025) | DOI `10.46298/dmtcs.14126`, arXiv `1711.02411` | sequential local whirling and RG-word dynamics; zero theorem credit |
| `JiLiWang2025` | David Ji, Michael Li, Daniel Wang, “Periods and Atomic Firing Sequences of Parallel Chip-Firing Games on Directed Graphs,” *Annals of Combinatorics* 29(4), 1155--1175 (2025) | DOI `10.1007/s00026-025-00760-3`; arXiv `2407.15889` | parallel directed-cycle chip firing and periods; the entire excess-load factor is zero-credit |
| `Brandt1982` | Jørgen Brandt, “Cycles of Partitions,” *Proc. AMS* 85(3), 483--486 (1982) | DOI `10.1090/S0002-9939-1982-0656129-5` | Bulgarian-solitaire integer-pile update and cycles; zero theorem credit |
| `Schutzenberger1972` | Marcel-Paul Schützenberger, “Promotion des morphismes d'ensembles ordonnés,” *Discrete Mathematics* 2(1), 73--94 (1972) | DOI `10.1016/0012-365X(72)90062-3` | jeu de taquin/promotion background; zero theorem credit |
| `StrikerWilliams2012` | Jessica Striker, Nathan Williams, “Promotion and Rowmotion,” *European Journal of Combinatorics* 33(8), 1919--1942 (2012) | DOI `10.1016/j.ejc.2012.05.003`, arXiv `1108.1172` | toggle/promotion/rowmotion conjugacy background; zero theorem credit |
| `TakahashiSatsuma1990` | Daisuke Takahashi, Junkichi Satsuma, “A Soliton Cellular Automaton,” *JPSJ* 59(10), 3514--3519 (1990) | DOI `10.1143/JPSJ.59.3514` | box-ball/soliton cellular automaton background; zero theorem credit |
| `ChoiEtAl2024` | Yunseo Choi, Katelyn Gan, Andrew Li, Tiffany Zhu, “On the Set Partitions That Require Maximum Sorts Through the aba-Avoiding Stack,” arXiv `2403.05113` (2024) | arXiv and DataCite DOI `10.48550/arXiv.2403.05113` | deterministic set-partition sorting and extremal passes; zero theorem credit |

The paper-local `references.bib` contains exactly these eight cited records.
DOI metadata were fetched from publisher/Crossref surfaces; arXiv titles,
authors, dates, and version status were checked on the arXiv abstracts.
Review A replaced the valid but preprint-only Ji--Li--Wang entry by its 2025
formal publication while retaining the arXiv identifier as an auxiliary
link.
Brandt's complete page range was cross-checked against the journal-indexed
institutional record because one machine DOI response truncates the final page.

## Literal subtraction

### Restricted-growth functions and whirling

Restricted-growth words already encode set partitions through ordered first
occurrences.  Whirling acts directly on this carrier and is assembled from
sequential coordinate maps.  Successor transfer is therefore not presented as
the introduction of dynamics on RG words.  Its literal step is simultaneous,
changes each repeated letter only at its last occurrence, is noninvertible,
and has nonuniform target fibres.  RGF syntax and all whirling mechanisms are
excluded from the residual package.

### Directed-cycle chip firing

For `z_i=|B_i|-1`, successor transfer projects exactly to

```text
z_i' = z_i - 1[z_i>0] + 1[z_(i-1)>0].
```

This is threshold-one parallel chip firing on a directed simple cycle.  Its
traffic/queue reading, smoothing mechanism, and generic period questions are
fully assigned to that owner lane.  The residual labelled statements are the
canonical prefix/suffix lift and the interlacing-sensitive inverse trace,
neither of which is encoded by `z`.

### Other nearby dynamics

Bulgarian solitaire removes one item from each integer pile and gathers the
removed items into a new pile, so it sorts unlabeled part sizes and can change
the number of piles.  Successor transfer instead preserves a fixed number of
labelled blocks and gives each donor a distinct prescribed successor.

Jeu de taquin, promotion, and rowmotion are bijective slide/toggle actions on
tableau, linear-extension, or poset carriers.  No such conjugacy is used here;
the phrase “window sorting” names only a proof step.  The box-ball system uses
a spatial carrier and soliton invariants, while successor transfer serves one
labelled maximum per active colour queue.  Deterministic set-partition stack
sorting is another direct-carrier map, but its update is a pattern-avoiding
stack pass rather than cyclic maximum transfer.  These mechanisms and their
generic clock language are excluded from the residual theorem package.

## Bounded owner-search result

The bounded exact-phrase, RGF, set-partition action, chip-firing, solitaire,
promotion, and carrier searches did not locate an inspected primary record
with the same simultaneous maximum-to-successor self-map together with both
the stratum clock/recurrent classification and the target-fibre trace.  A
search non-hit cannot support an external ownership statement.  Specialist
database and citation-chain checks remain prerequisites to any circulation.

## Internal collision boundary

The pre-paper gate checked P1--P166, including the high-collision systems P90,
P110, P126, P137, P138, P145, P147, and P148.  P90 consumes the traffic/load
projection; P110 changes block count by joining; the split/consolidation
systems change the carrier in ways absent here.  Generic clocks, periods,
fibres, Stirling counts, and trace algebra were not treated as separation.
This is an internal routing result only.

## Stable verification links

- <https://doi.org/10.1016/0097-3165(94)90117-1>
- <https://doi.org/10.46298/dmtcs.14126>
- <https://doi.org/10.1007/s00026-025-00760-3>
- <https://arxiv.org/abs/2407.15889>
- <https://doi.org/10.1090/S0002-9939-1982-0656129-5>
- <https://doi.org/10.1016/0012-365X(72)90062-3>
- <https://doi.org/10.1016/j.ejc.2012.05.003>
- <https://doi.org/10.1143/JPSJ.59.3514>
- <https://arxiv.org/abs/2403.05113>
