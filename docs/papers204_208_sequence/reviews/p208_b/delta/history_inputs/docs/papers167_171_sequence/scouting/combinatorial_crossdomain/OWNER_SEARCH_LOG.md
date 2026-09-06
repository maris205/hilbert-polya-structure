# STF bounded owner and novelty search

Search date: 2026-09-03.  Scope: identify a literal owner for “each
non-singleton canonically ordered set-partition block sends its maximum to the
next block simultaneously,” and subtract the obvious load/sorting neighbours.
This is a bounded primary-source search, not a novelty certificate.

## Queries actually used

The web/arXiv search batches used the following phrases (with minor singular
and plural variants):

1. `"set partitions" "move" "maximum" "next block" dynamics`
2. `set partition promotion maxima blocks cyclic`
3. `set partition whirling action blocks maximum`
4. `restricted growth word last occurrence promotion`
5. `"last occurrence" "restricted growth word" dynamics`
6. `"maximum element" "next block" "set partition"`
7. `site:arxiv.org whirling action set partitions blocks`
8. `site:arxiv.org restricted growth word cyclic action promotion set partition`
9. `Bulgarian solitaire set partitions deterministic dynamics blocks`
10. `box-ball system carrier set partitions promotion`
11. `jeu de taquin promotion set partitions cyclic sieving`
12. `deterministic parallel zero range process directed cycle threshold one chip`
13. `parallel chip-firing games on directed graphs cycle`
14. `set partition maximum stack sorting deterministic map`

No result in these batches states the literal STF rule.  The negative query
result has no standalone evidentiary weight; the useful outcome is the owner
subtraction below.

## Primary-source neighbour table

| Neighbour | Primary source | What is owned | Literal subtraction from STF |
|---|---|---|---|
| Restricted-growth-word whirling | Joseph, Propp, and Roby, *Whirling injections, surjections, and other functions between finite sets*, [arXiv:1711.02411](https://arxiv.org/abs/1711.02411), later [DMTCS DOI 10.46298/dmtcs.14126](https://doi.org/10.46298/dmtcs.14126). | Whirling is a composition of coordinate maps that repeatedly increment one value until the word remains in the chosen function family; the paper explicitly treats restricted-growth words/set partitions and homomesy. | This is the closest carrier owner.  Its map is sequential and invertible.  STF simultaneously increments the *last occurrence of every repeated value*, is noninvertible, has transients, and has target fibres of varying size.  Results cannot be presented as the first dynamics on RG words. |
| Static RGF structure | Wachs, *sigma-Restricted growth functions and p,q-Stirling numbers*, [DOI 10.1016/0097-3165(94)90117-1](https://doi.org/10.1016/0097-3165(94)90117-1); Bean, Bell, and Ollson, *Insertion Encoding of Restricted Growth Functions*, [arXiv:2510.17359](https://arxiv.org/abs/2510.17359). | First-occurrence normal forms and insertion/regular-language structure of restricted-growth functions. | These own the encoding/background, not the simultaneous last-occurrence transfer.  STF must cite RGF terminology rather than rebrand it. |
| Parallel chip firing on directed cycles | Ji, Li, and Wang, *Parallel chip-firing games on directed graphs*, [arXiv:2407.15889](https://arxiv.org/abs/2407.15889). | Parallel firing on directed graphs and possible periods on directed simple cycles. | STF's excess-load projection is literally the outdegree-one directed-cycle firing rule.  Therefore the load projection and traffic interpretation are **not** a novelty claim.  STF retains the ordered labels discarded by that projection; the canonical-window and five-state fibre results concern this labelled lift. |
| Bulgarian solitaire | Brandt, *Cycles of partitions*, [DOI 10.1090/S0002-9939-1982-0656129-5](https://doi.org/10.1090/S0002-9939-1982-0656129-5). | On integer partitions, remove one card from every pile and collect those cards into a new pile; cyclic states are classified. | Bulgarian solitaire sorts pile sizes and may change the number of piles.  STF preserves the number of set-partition blocks and sends distinct labelled maxima to distinct successor blocks.  The shared “one item from each nontrivial pile” language must be acknowledged, but the maps are not conjugate on their literal carriers. |
| Jeu de taquin / promotion | Schuetzenberger, *Promotion des morphismes d'ensembles ordonnes*, [DOI 10.1016/0012-365X(72)90062-3](https://doi.org/10.1016/0012-365X(72)90062-3); Striker and Williams, *Promotion and Rowmotion*, [arXiv:1108.1172](https://arxiv.org/abs/1108.1172). | Promotion, jeu-de-taquin sliding, and toggle/rowmotion conjugacies on tableaux, linear extensions, and order ideals. | These are bijective actions on constrained poset/tableau carriers.  STF is a noninvertible parallel maximum circulation on all set partitions.  Section 3 of the derivation may be described as a sorting lemma, but not as a new promotion action without an explicit conjugacy (none was found). |
| Box-ball systems | Takahashi and Satsuma, *A Soliton Cellular Automaton*, [DOI 10.1143/JPSJ.59.3514](https://doi.org/10.1143/JPSJ.59.3514); Kakei et al., *Linearization of the box-ball system*, [arXiv:1709.10195](https://arxiv.org/abs/1709.10195). | Carrier formulations, solitons, conserved scattering data, and linearization for box-ball evolution. | BBS moves balls to vacancies through a spatial carrier and preserves soliton data.  STF serves one labelled maximum from every nonempty excess-colour queue to the next colour.  Its load factor is queue-like, but no BBS soliton system or literal carrier equivalence was found. |
| Set-partition stack sorting | Choi, Gan, Li, and Zhu, *On the set partitions that require maximum sorts through the aba-avoiding stack*, [arXiv:2403.05113](https://arxiv.org/abs/2403.05113). | Deterministic stack-sorting maps directly on set partitions and extremal pass counts. | This is another direct-carrier owner.  Its update is a stack pass defined by pattern avoidance, not simultaneous cyclic block transfer.  STF's `n-2` clock must not be advertised generically as the first sharp sorting time for set partitions. |

## Internal P1--P166 collision subtraction

The immediate historical index, the P162--P166 kill ledger, and the high-risk
systems P90/P110/P137/P138/P145/P148 were checked before retention.

- **P90 Rule-184 traffic:** STF's load factor has a traffic/queue
  interpretation, so that factor is treated as owned machinery.  The literal
  set-partition lift and target fibres are not determined by it.
- **P110 shift-join partitions:** P110 joins blocks and changes block count;
  STF transfers maxima and preserves block count.
- **P137 rank-feedback split and the P126/P132 split family:** these refine
  blocks.  C04 and C05 were killed for this collision; STF never splits or
  merges a block.
- **P138 palindrome-XOR, P145 folded-cube vertex push, P148 tree contraction:**
  no carrier or literal-rule equality was found.  Their generic parity/folding
  arguments were not used.
- **P63/P115/P127 linear kernels:** C10 and C26 were killed because their whole
  signal reduces to these linear/coordinate engines.
- **Recent 308-candidate ledger:** centroid routing, balanced block splitting,
  graph-square/tree-center closure, and support-only random fragmentation were
  treated as occupied; the matching candidates here were killed immediately.

## Search verdict and claim boundary

The bounded search found **no literal STF owner**, but it found two strong
neighbours that materially constrain positioning: whirling already owns
restricted-growth-word dynamics, and directed-cycle chip firing owns the load
factor.  A defensible short-paper claim would therefore be narrow:

> a noninvertible labelled lift of directed-cycle queue firing on canonical set
> partitions, with a sharp preperiod theorem, complete periodic strata, and a
> full-target five-state fibre trace formula.

Before external circulation, this needs a conventional database search
(MathSciNet/Zentralblatt/Google Scholar citation chasing from the two nearest
owners) and an expert check of the transfer-matrix formula.  The present search
supports **provisional survival**, not a novelty assertion.
