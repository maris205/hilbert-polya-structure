# FOSP: bounded source and internal-collision audit

Reviewer `/root/batch197_fosp_gate`, 2026-09-05 UTC. This source audit adds a
previously omitted close owner. It is not a novelty or priority certificate.

## Newly found local owner: mandatory subtraction

Brualdi and Dahl, *Multipermutations and Stirling Multipermutations*,
Graphs and Combinatorics 40, article 22 (2024), DOI
[10.1007/s00373-024-02751-2](https://link.springer.com/article/10.1007/s00373-024-02751-2),
define a **left-join** immediately before Theorem 8: move the second
occurrence of a label next to its first. Theorem 8 gives reduction to doubled
permutations using at most n-1 joins. Their Section 5 explicitly interprets
this as edge contraction followed by pendant-edge replacement. These local
operations, the star endpoint, and the bare convergence mechanism must
receive zero credit.

The following is this reviewer's exact comparison, not a claim quoted from
that source. Write `J_1(A1B1C)=A11BC` and set `c(1)=n`, `c(j)=j-1` for
`j>1`. Then **FOSP is exactly `T=c o J_1`**. The independent control checks
this identity on every state through n=7. Consequently the old firewall's
claim that Nabergall is the sharpest located near collision is superseded.

This identity is not a conjugacy of self-maps `Q_n -> Q_n`: cyclic relabeling
c alone is not a self-map (for example it sends `1221` to `2112` at n=2).
The known left-join is idempotent, whereas T has exact n-cycles. The inspected
Theorem 8 allows chosen nonadjacent labels to be joined; it does not state
the fixed-rank cyclic-relabeling map or its every-target root-cut atlas.
The full n-1 timescale by itself is now particularly weak evidence. The
remaining eligible conjunction is the prescribed relabeling schedule's exact
point clock and full depth CDF together with the complete target atlas,
image count and equality classification. This is an internal eligibility
judgment under the standing threshold, not a judgment of publishable novelty.

## Other inspected primary sources

| Source and inspected location | Credit removed / bounded comparison |
|---|---|
| [Janson, arXiv:0803.1129v1](https://arxiv.org/html/0803.1129v1), opening definition and contour discussion | Standard plane-recursive-tree/Stirling bijection, growth gaps, and leaf/plateau correspondence. These are proof inputs. |
| [Janson–Kuba–Panholzer, arXiv:0805.4084v1](https://arxiv.org/html/0805.4084v1), Example 3 and Section 3.1 | General increasing-tree growth and generalized Stirling encodings are standard; they do not themselves supply a new dynamical system. |
| [Nabergall, arXiv:2104.02296](https://arxiv.org/pdf/2104.02296), Section 8.1, Proposition 8.18, PDF pp. 40–41 | On the stated 1-terminal subclass, the associated Stirling word begins and ends with 1; its operation deletes the 1-pair and standardizes. That map reduces rank and omits the prescribed reinsertion. The section also supplies the standard contour bijection. |
| [Ma–Liu–Yeh–Yeh, arXiv:2506.16438v2](https://arxiv.org/pdf/2506.16438), Section 4.2 and pp. 17–18; [published author PDF](https://jeanyeh.github.io/publication/2026Eulerian-type%20polynomials%20over%20Stirling%20permutations%20and%20box%20sorting%20algorithm.pdf) | Recent box sorting concerns ordered weak set partitions and Young tableaux; its row/column rearrangement is not the fixed-rank pair turnover. It is a near-name/source control, not support for FOSP novelty. |

The older scout also lists Ma–Qi–Yeh–Yeh (2210.11372) and Prodinger
(1709.05966). This independent audit does not pretend to have re-read their
full text: the attempted 2210.11372 HTML endpoint failed. They remain
additional background entries from the author record, not independently
cleared sources in this gate.

## Internal historical comparison

The root state, current pipeline, and history caveats were read first. A
corpus keyword scan covered available `papers/` and `docs/` Markdown/TeX,
excluding the current batch and repeated cold-build archives. Search terms
included Stirling permutation, plane recursive tree, left-join,
shrink/pendant, least root child, and smallest-tree deletion. No earlier
literal FOSP or left-join scheduler was found in that bounded scan. This is
not an exhaustive semantic comparison of all old manuscripts.

The closest definition/proof records were then read directly and pinned:

| Prior evidence | What is shared and what distinguishes the present map |
|---|---|
| P114 `rooted-forest-leaf-peeling/main.tex` | Parallel deletion of all nonroot leaves; shrinking subsets and height clock. FOSP keeps rank, deletes label 1, and has recurrent n-cycles. |
| P148 `even-level-plane-tree-contraction/main.tex` | Ordered child promotion and inverse block/gap geometry are already occupied. P148 retains even generations and shrinks size; FOSP has one labelled root slot, fixed rank, and a maximum-label clock. Generic contraction and cut arguments receive no separation credit. |
| P169 `successor-transfer-set-partitions/main.tex` | Deterministic labelled promotion-like recurrent dynamics. Its simultaneous block-maximum transfer and interlacing trace fibre differ from the Stirling interval/root-cut map. |
| P179 `random-singleton-isolation/main.tex` and P182–P186 root coordinator kill ledger `GSE` | Commuting idempotents and history-support reduction are occupied proof machinery. The reviewer confirms that left-joins commute as well. Generic semigroup/support bookkeeping is zero credit; the present ordered-tree CDF and root cut are not supplied by P179's random partition kernel. |
| P192 `first-collision-hurwitz/main.tex` | Known local move plus a literal scheduler is already a research pattern. Hurwitz factorization and its endpoint inverse are different, and that shared pattern earns no credit. |
| P194 `least-raising-crystal-words/main.tex` | Known word operators plus least-colour choice, crystal signature clock and inverse lowering. No direct rule transfer to paired nested words. |
| P195 `odd-side-least-neighbor-trees/main.tex` | It changes only a distinguished vertex on a fixed labelled tree; FOSP changes ordered parent-child incidence. |
| P122–P126 combinatorial scout C01 | The parity root-rotation control is a full-binary-tree rule with periods 1/2, not the actual P122 manuscript. The control label must not be mistaken for the final P122 paper. |

P51–P56 manuscripts are absent. The recovered themes in
`docs/papers177_181_sequence/scouting/combinatorial_lane/TITLE_COLLISION_INVENTORY.md`
concern shadowing, forbidden-word SFTs, spoke codes, morphisms, probabilistic
automata, and SFT covers. This is only a topic warning; those missing papers
cannot be claimed as inspected. The existing historical snapshot is retained.

## Queries and stop boundary

Actual independent web query lanes included:

```
"Stirling permutations" "promotion"
"plane recursive trees" "delete" "smallest"
"Stirling permutation" "remove" "1" Nabergall
"Stirling" "left-join" dynamics
"Stirling permutations" "cyclic" "decrement"
"increasing plane trees" "cyclic" "delete"
"Stirling" "left-join" Brualdi Dahl cyclic
"Stirling permutation" "first" "decrement"
"Eulerian-type polynomials over Stirling permutations and box sorting algorithm"
```

Some searches returned irrelevant records, which supplied no evidence.
Only primary sources above support the comparisons. A source defining all of
`c o J_1` on `Q_n`, or a literally equivalent tree map, triggers a kill even
if it lacks the current formulas. No such owner was located in these bounded
lanes. Status remains `OWNER_AMBER / HOLD_EXTERNAL`, with a newly found
mandatory local-owner disclosure and no external clearance.
