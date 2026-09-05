# Period-feedback: bounded source and collision audit

Date: 2026-09-05 UTC. Status: **OWNER_AMBER / HOLD_EXTERNAL**.
This is an author-side search and subtraction record, not independent
acceptance, a novelty certificate, or a paper allocation. AI-assisted search
and source comparison were used; no human-read attestation is inferred.

## Exact object and claim inventory

On all labelled functions $f:\{0,\ldots,n-1\}\to\{0,\ldots,n-1\}$, replace
the pointer at every vertex by its eventual cycle length minus one. Numerical
labels retain their roles at every epoch. This is not repeated composition
of one fixed $f$, the least common multiple of its cycle lengths, or a map
on functional-graph isomorphism classes.

| Claim | Mechanism | Credit boundary |
|---|---|---|
| Unique zero attractor | Distinct cycle lengths consume disjoint cyclic vertices | Finite-map eventual periodicity and cycle decomposition alone have zero credit |
| Sharp minimum rank for height $h$: $N_2=2$, $N_{h+1}=N_h(N_h+1)/2$ | Rank packing plus explicit optimal cycle-block lift and core-extension lemma | The numerical recurrence is already known; only this dynamical interpretation is a proposed residual |
| All critical-size extremizers and $D_h=D_{h-1}(N_h-N_{h-1})!$ | Equality in every rank-packing inequality forces recursive labelled cycle placement | A construction-only assertion would be weaker; complete necessity is essential |
| Every target fibre and image condition | Invariant target blocks and cycle-rooted forests | Static restricted-cycle enumeration is classical, not newly discovered |
| Unique largest fibre at zero | Strict connected-component comparison plus strict cross-block forest injection | Cayley count $(n+1)^{n-1}$ itself has zero credit |

## Primary and official source ledger

The study-design levels used for empirical research are not directly
applicable to proof literature. The grades below concern fitness for the
specific mathematical or bibliographic claim, not empirical evidence levels.
No COI or predatory-venue audit has been performed; this memo does not certify
either. No source is called peer-reviewed solely because it has an arXiv ID.

| Source and locator | Read / verification scope | What it supports; binding subtraction |
|---|---|---|
| Philippe Flajolet and Robert Sedgewick, *Analytic Combinatorics*, Cambridge University Press, 2009. [Author book page](https://sedgewick.io/books/analytic-combinatorics/), [official book PDF](https://ac.cs.princeton.edu/home/AC.pdf) | Author page and table of contents read; indexed official PDF passage for Example VII.3 read. Full PDF browser open failed on its 11 MB size. No full-book-read claim. | The labelled mapping decomposition is SET of CYC of rooted trees. Chapter II.5.2 and Example VII.3 are the background route; restricting the cycle size gives the stated EGF. Static SET/CYC formulas receive zero credit. Grade: direct official background, with bounded read scope. |
| Stephan Wagner, *Enumeration of highly balanced trees*, Ars Combinatoria 114 (2014), 15–32. [Author PDF](https://math.sun.ac.za/swagner/balanced.pdf), [author publication list](https://math.sun.ac.za/swagner/pub.html) | Section 4 content read through browser PDF extraction, including the displayed triangular recurrence and sequence; repeat browser opens timed out. The exact section was reproduced by a direct PDF-indexed search excerpt using `site.math.sun.ac.za/swagner/balanced.pdf "231" "26796"`. No saved complete PDF or full-paper-read claim is required. Author-list indexed text separately confirms title, year, volume and pages. The PDF's internal pagination is not asserted to equal journal pagination. | The sequence $2,3,6,21,231,26796,\ldots$ already enumerates a balanced-tree class and is identified there with A007501. Therefore neither this sequence nor its double-exponential recurrence is a contribution of the feedback note. Grade: direct author mathematical source excerpt for sequence ownership. |
| François Doré, Enrico Formenti, Antonio E. Porreca and Sara Riva, *Algorithmic reconstruction of discrete dynamics*, [arXiv:2208.08310v2](https://arxiv.org/html/2208.08310v2), 6 September 2022 | Abstract, introduction, and Section 2 read. The [current v4 landing page](https://arxiv.org/abs/2208.08310) was separately read; it has the different title *Decomposition and factorisation of transients in Functional Graphs*, revised 4 April 2024. Do not merge the v2 title with an unspecified latest version. | Section 2 calls a cyclic vertex's smallest return period its feedback. The actual investigated transformations are sum/direct-product equations $A\times X=B$ up to graph isomorphism, not period-statistic pointer writeback on fixed numeric labels. This is a close terminology and standard-decomposition owner, not a literal-map match in the read sections. Grade: direct author preprint, source-bounded neighbor. |
| Eric Schmutz, *Period Lengths for Iterated Functions*, [arXiv:0711.0312](https://arxiv.org/abs/0711.0312), 2007 | Official abstract / metadata read; no full-paper-read claim | Studies the period length under repeated composition of a random function, not iteration of an operator that replaces a function by its local cycle-period vector. Grade: abstract-level neighbor only. |
| Joachim von zur Gathen, *Iteration entropy*, [arXiv:1712.01407](https://arxiv.org/abs/1712.01407), 2017 | Official abstract / metadata read; no full-paper-read claim | A statistic of a fixed function and its iterates; the inspected abstract does not define the present labelled feedback self-map. Grade: abstract-level neighbor only. |

The rooted-forest count with a prescribed root set is used as a classical
input, explicitly isolated in the proof package. The exact restricted-cycle
formula is also derived there by selecting cyclic vertices, choosing their
cycle permutation, and attaching those rooted forests. We do not claim an
exact theorem-number citation for a book passage that was not read.

A root-side search hit, *Stabilized Identities in Finite Transformation
Semigroups*, at `https://www.mdpi.com/2073-8994/18/8/1247`, remained a
snippet-only, full-page-failed lead. It is **not included as verified source
evidence** and no detailed theorem subtraction is asserted for it.

## Search scope and reproducibility

The retained manuscript/kill-record surface was searched first. The local
`papers/` collection contains the project manuscripts rather than a distinct
functional-graph literature library; relevant available source TeX was used
for literal definitions. No Zotero or Obsidian connector was available. No
local `arxiv_fetch.py` was found in the available arXiv skill directory, so
official arXiv browsing was used. No external model received private drafts.

The following bounded queries were issued, with minor punctuation variants:

- `"functional graph" "period" "transform" iteration cycle length`
- `"endofunction" "cycle length" "iteration" map statistic`
- `"period map" "finite" functions cycle lengths`
- `"cycle length" "feedback" endofunction`
- `"iterated" "cycle-length" transformation maps`
- `"endofunction" "triangular" iteration`
- `"iterated cycle lengths" functions`
- `"cycle-length transform" function`
- `"2, 3, 6, 21, 231" "function"`
- `"period" "endofunctions" "triangular"`
- `"Enumeration of highly balanced trees" Wagner`
- `"eventual period" "map" "iteration" "cycle length"`
- `"endofunction" "period map"`
- `"cycle-length feedback"`

The searches exposed the known numerical sequence and close functional-graph
terminology. No literal owner for this exact self-map was located in these
bounded results. Search indexing, unavailable full texts, terminology
variation, and historical omissions remain live limitations. That non-hit
is not a novelty or priority claim. The source set is not a systematic review.

## Internal collision surface and its limitations

Available manuscript source was inspected for the following closest systems:

| Historical route | Occupied mechanism | Exact separation to be judged |
|---|---|---|
| P105 cycle-minimum pruning | Remove selected vertices from permutation cycles; longest-cycle clock and threshold matching | Current input includes all functions; the next pointer is the numeric period statistic, and cycles are rebuilt. The packing rank is not the old prune clock. |
| P167 least-preimage feedback | Pointer reversal/least predecessor, path structure, periods one or two, sharp linear transient bound | Current outputs are eventual cycle lengths, not selected predecessors; no reversed-path normal form appears. |
| P172 random self-image erosion | Fresh random maps acting on subsets, occupancy/Jordan analysis | Current system is deterministic on the full endofunction carrier. This is not the same literal map or stochastic quotient. |
| P186 rank-subtraction support erosion | Subset support gaps and a linear erosion clock | The current iteration depends on labelled cycle placement, not support gaps. |
| P188 self-sized prefix clipping | $A\mapsto A\cap[|A|]$, source-rank recursion and many fixed initial segments | The current sharp threshold is obtained by disjoint cycles of distinct lengths. Its unique zero attractor and critical-size factorial census are not prefix clipping formulas. |

P185 prefix-diversity feedback and P137 rank-feedback group splitting also
remain neighboring feedback labels in the project catalog; only the catalog
level was used here, not a claimed complete theorem audit of those papers.
The final independent gate must decide whether their proof mechanisms, or
any missed owner, subsume the proposed residual. P51–P56 manuscripts remain
absent from the recoverable collection, as recorded centrally; no complete
P1–P196 clearance is claimed.

## Canonical-statistic intake objection: preserved, not waved away

The existing file
`scouting/word_poset_lane/COLLISION_FIREWALL.md`, under the exact heading
**Permanent gates applied in this lane**, includes the exact bullet:

> canonical statistics written back as states;

The present literal map does write a canonical statistic back into pointer
states. Therefore it fails that word/poset lane's stated intake filter on
its literal wording. That file is preserved unchanged. The same-histogram
counterexample in the proof package shows only that a value-histogram factor
does not determine the next epoch; it does **not** defeat this broader bullet
and is not permission to re-enter that lane.

The central `PROBLEM_ANCHOR.md` is a separate recorded contract: it requires
a sharp all-parameter temporal theorem and a separate materially different
inverse/fibre/extremal/enumeration mechanism, and rejects generic bookkeeping,
classical-algorithm renaming, conjugacy, and collapsed axes. It does not
contain the same blanket bullet. This re-entry was explicitly commissioned
by the root outside the word/poset lane after the sharp rank theorem emerged.
That administrative scope fact is not a self-granted mathematical exemption.

The independent gate must evaluate the strongest rejection: perhaps the
package is still generic statistic writeback plus classical forest counting,
and the sharp triangular clock/equality analysis is insufficient residual.
The reply offered for testing is limited: unlike generic convergence, the
package proves minimal rank for every height, attains every threshold, and
classifies **all** critical-size extremizers; its targetwise inversion and
strict maximal-fibre comparison use a distinct mechanism. Correctness of
those statements does not force acceptance. If the reviewer rejects this
residual, preserve the proof and close the slot again.

## Handoff state

The companion exact verifier has 3,366,093 assertions, full carrier coverage
through $n=7$, complete target checks including absent targets through
$n=6$, and recursive critical witnesses through $n=26796$. Its frozen
`CANONICAL.txt` is a bounded check, not evidence of all-size correctness or
external novelty. The full all-size proof is
`THEOREM_CONTRACT_AND_PROOF.md`. Selection and external status remain
**independent-gate pending / OWNER_AMBER / HOLD_EXTERNAL** in this author memo.
