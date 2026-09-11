# Bounded primary-owner search

**Search date:** 2026-09-03 UTC  
**Scope:** only the strongest mathematical controls and the liveliest raw
literal map from the 22-system lane.  
**External state:** `HOLD_EXTERNAL`.

This is an early owner screen, not a systematic literature review, novelty
opinion, priority claim, or freedom-to-operate search.  A query non-hit has no
positive evidentiary value.

## Queries actually used

The web batches used the following strings, with automatic singular/plural
variants in some results:

1. `"breadth-first" "Cartesian tree" permutation level order`
2. `"level order" Cartesian tree permutations breadth first`
3. `permutations breadth first traversal min heap ordered binary tree level order enumeration`
4. `"heapable permutations" binary tree breadth first`
5. `site:oeis.org 1 1 2 4 12 39 164 718 3805 permutations binary tree breadth first`
6. `"level-order" "Cartesian tree" permutation iteration`
7. `"breadth-first traversal" "Cartesian tree" permutation`
8. `"level order" heap-ordered binary trees permutations enumeration`
9. `permutation to Cartesian tree then level order sequence`
10. `Cartesian tree level order sequence permutation heap ordered`
11. `binary word map mark matched parentheses positions iterate`
12. `parenthesis matching support binary word unmatched positions map`
13. `Dyck word canonical matching mark matched letters iteration`
14. `noncrossing parenthesis matching support operator binary strings`
15. `permutation transform rank adjacent cyclic sums iteration`
16. `"adjacent sums" permutation "rank" transformation`
17. `permutations ranked by adjacent sums cyclic dynamics`
18. `permutation adjacent sum ordering map`
19. `tournament arc reversal directed triangles operation`
20. `tournament "triangle reversal" arcs`

The repository-title and full-text sweep additionally used `Cartesian`,
`breadth`, `level-order`, `Dyck`, `parenthesis`, `matching support`, `LZ78`,
`move-to-front`, `true twin`, `codegree`, `antichain`, `blocker`, `Latin
normalization`, `tournament`, and `triangle reversal` across P1--P171.

## Primary-source subtraction

| control | primary source | what the source owns | consequence here |
|---|---|---|---|
| Cartesian trees | Vuillemin, *A unifying look at data structures*, [DOI 10.1145/358841.358852](https://doi.org/10.1145/358841.358852); Gabow, Bentley, and Tarjan, *Scaling and related techniques for geometry problems*, classical Cartesian-tree lineage; Buchsbaum and Westbrook, *Maintaining hierarchical graph views*, followed by linear construction literature such as [DOI 10.1016/0020-0190(94)00150-2](https://doi.org/10.1016/0020-0190(94)00150-2). | The unique heap-ordered tree with prescribed inorder word and linear construction. | The tree object and construction receive zero credit in `Q02_CBF`. |
| Cartesian preorder / stack sorting | Bousquet-Melou, *Sorted and/or sortable permutations*, [DOI 10.1016/S0012-365X(00)00146-1](https://doi.org/10.1016/S0012-365X(00)00146-1), together with the exact reverse-complement conjugacy proved in the P142 control. | West's stack-sorting map, iteration/sortability and preimage theory; internally, the same prefix clock and Catalan Cartesian fibre package. | This is the decisive proof-engine kill.  No claim is made that BFS itself is stack sorting; the P142 theorem silhouette already transfers. |
| Traversal permutations | Kretchmar, *Tree Traversals and Permutations*, [author-hosted manuscript](https://personal.denison.edu/~kretchmar/pubs/TreeTraversals.pdf). | Permutations arising from preorder/inorder/postorder pairs and transformations between the corresponding binary trees.  The inspected text has no `level`, `breadth`, `Cartesian`, or `heap` occurrence. | Useful neighbour, not a located owner of repeated Cartesian-inorder-to-BFS iteration.  The non-hit does not rescue the internal collision. |
| Heapable permutations | Byers et al., *Heapable sequences and subsequences* lineage; Balaji et al., *Fixed-Parameter Algorithms for Longest Heapable Subsequence and Maximum Binary Tree*, [arXiv:2110.00495](https://arxiv.org/abs/2110.00495); *Efficient methods of calculating the number of heapable permutations*, [DOI 10.1016/j.dam.2023.01.025](https://doi.org/10.1016/j.dam.2023.01.025). | Sequential placement of a sequence into some binary min-heap, recognition/counting, and maximum binary trees in permutation DAGs. | `Q02_CBF` instead fixes the Cartesian shape from inorder and asks whether a target is its BFS labelling.  Heapability is background only; no same-map owner was located. |
| Dyck/parenthesis normal forms | The ordinary Dyck-language stack grammar and matching decomposition; internally P74's exact exposed-stack/polycyclic normal forms. | Reduction to unmatched closes followed by unmatched opens, with matched Dyck blocks and Catalan counts. | The whole image/fibre theorem of `W01_BMS` is owner-subtracted even though the output support mask is a different literal object. |
| Box-ball carrier pairing | Takahashi and Satsuma, *A Soliton Cellular Automaton*, [DOI 10.1143/JPSJ.59.3514](https://doi.org/10.1143/JPSJ.59.3514); Kakei et al., *Linearization of the box-ball system*, [arXiv:1709.10195](https://arxiv.org/abs/1709.10195). | Pairing/moving balls to vacancies, carrier descriptions, soliton invariants and linearisation. | `W01_BMS` marks both matched endpoints and is not claimed conjugate to BBS, but particle-pairing language and generic carrier consequences receive zero credit. |
| Adjacent-sum cyclic arrangements | Mosahab, *A Classification of Cyclic Orderings with Distinct Adjacent Sums*, [DOI 10.2139/ssrn.7166164](https://doi.org/10.2139/ssrn.7166164). | Static existence/classification of cyclic residue orderings with pairwise-distinct adjacent sums modulo `n`. | Neighbouring static topic only.  It does not state stable reranking iteration or the `2n` orbit in `ASR_KILL_NOTE.md`.  The current kill is lack of an atlas/inverse, not direct ownership. |
| Tournament cycle reversals | Thomassen, *Arc reversals in tournaments*, [DOI 10.1016/0012-365X(88)90031-3](https://doi.org/10.1016/0012-365X(88)90031-3); Kolesnik--Mitchell--Przybylowski, *Coxeter interchange graphs*, [arXiv:2312.04532](https://arxiv.org/abs/2312.04532). | Equivalence under path/cycle reversals and interchange graphs generated by reversing directed triangles. | Reversal of triangle-related arcs is mature.  These sources do not state the simultaneous “each arc in exactly one triangle” map, but `T01_UTR` lacks a theorem package and has a direct P112 reserve neighbour. |
| Unique-triangle arcs | Morris, *Walecki tournaments with an arc that lies in a unique directed triangle*, [arXiv:2407.03807](https://arxiv.org/abs/2407.03807). | Structural consequences when a Walecki tournament has an arc lying in exactly one directed triangle. | The exact local predicate in `T01_UTR` already has a specialised owner context, though not the synchronous dynamic.  No novelty inference follows. |

## Exact-map outcomes

### `Q02_CBF`

No inspected source states the repeated map “construct the min-Cartesian tree
from the current inorder permutation, output its level order, and iterate.”
That negative result is irrelevant to the final decision: P142 already owns
the same carrier and transfers both headline proof engines after changing the
tree traversal.  Verdict: `KILL_INTERNAL_CARTESIAN_TRAVERSAL`.

### `W01_BMS`

No inspected source states iteration of the exact matched-position support
mask.  The support output is different from returning the reduced word and
from moving balls in a box-ball system.  However, formula (2.1) in
`BMS_DERIVATION.md` is entirely the classical residual/Dyck factorisation,
while the surviving temporal result is only a nonsharp quadratic ceiling.
Verdict: `KILL_CURRENT / OWNER_AMBER_CONTROL`.

### `Q01_ASR`

No same stable-rank update was located.  The explicit `2n` orbit is a genuine
mathematical handle, but complete enumeration at rank 9 exposes four recurrent
cycles and no target-local inverse statistic.  Verdict: `KILL_NO_ATLAS`.

### `T01_UTR`

No same synchronous unique-triangle-arc reversal was located in the bounded
search.  Classical triangle reversals, a primary paper specifically on arcs
in unique triangles, and P112's “at least one triangle” synchronous reserve
make the owner surface dense.  With no all-rank recurrent or fibre theorem,
the non-hit cannot carry weight.  Verdict: `KILL_CURRENT / RAW LEAD ONLY`.

## Search ceiling

The remaining 18 maps were killed by literal internal collision, a standard
named algorithm/normalisation, or failure of the two-axis theorem gate before
an exact-title search could affect their status.  A future re-entry would
require citation chasing in MathSciNet/Zentralblatt and specialist review;
this log deliberately makes no claim of completeness.
