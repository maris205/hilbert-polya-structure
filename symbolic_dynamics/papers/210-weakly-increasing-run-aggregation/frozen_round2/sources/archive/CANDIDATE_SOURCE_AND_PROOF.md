# Independent source, proof and residual-value examination

Assessor `/root/mna_candidate_gate`; 2026-09-07 UTC. This is a candidate
gate, not manuscript A/B or an external priority certificate. The original
author and root supplied the theorem deductions before this assignment.
I found no essential repair and supplied no new theorem extension. The
following records verification of their existing claims and exact deductions
of prior mechanisms. The complete original/copy/hash roles are in
[INPUT_ROLES.json](INPUT_ROLES.json); mutable central controls are not used
as scientific proof inputs.

## 1. Exact carrier and independent representation

For every N≥1 the carrier is all positive compositions of N, identified with
ordered partitions of N labelled unit cells into intervals. In the verifier,
each current block is a set of original cells. First form the graph on OLD
blocks, joining successive blocks precisely when their OLD cardinalities
satisfy left≤right. Then replace each connected component by the union of
its cell sets. This graph construction is the literal simultaneous map,
not sequential comparison with an accumulated sum. Neither clocks nor
external schedules occur in its state.

This reconstruction differs materially from the author's primary running-sum
implementation and its cut-endpoint companion: the independent dynamics is
component union on persistent labelled-cell sets, while graph depths are
also computed in increasing block-count order. Source enumeration is
recursive, not the author's cut-bitmask generator. Every orbit is retained,
not sampled. The independent inverse is an explicit set of sorted
refinements and a separately implemented left-to-right endpoint transfer;
it does not import the pilot or any old scientific implementation.

## 2. Deductive attack on the temporal axis

The all-size argument checked is exactly §§1–2 of frozen
[MNA_PROOF.md](inputs/author_lane40/MNA_PROOF.md). Positivity and strict block
count descent prove termination only; that generic fact receives zero credit.

I checked Lemma A at the persistent boundary between the final parent of the
left block and the first parent of the right block. If the right block had
not been born in the previous round, its first parent would be the whole
right block. The previously surviving strict descent would then still
prevent deletion, since the left block can only gain mass. Thus the RIGHT
block, not just some unspecified parent, was born one round earlier. Its
first internal boundary is an eligible previous-round cut. The induction
hypothesis applies to that cut's left block; the surviving inter-block
strict descent and integrality force the present left mass to be at least
the present round number. This uses original block containment correctly,
does not assume every parent is new, and does not make disjoint support
claims across unrelated mergers.

For Lemma B, the first two parents of a newly formed block are disjoint.
Lemma A supplies mass at least t for the first, and the just-checked
right-parent birth conclusion supplies the previous-round new-block bound
for the second. Hence the author's recursion M_t≥t+M_(t−1), M_1=2,
gives 1+t(t+1)/2. No extra-parent term can reduce that mass. A last nonfixed
round creates at least one such block, establishing the upper clock bound.

The equality construction is also complete: for every h≥1 and surplus
r≥0 the source (h,h−1,…,1,1+r) has exactly h nonfixed updates. At each
step the old prefix is strictly decreasing, so only its final block can
join the already increasing terminal pair; the potentially very large
surplus cannot make earlier OLD comparisons disappear prematurely. The
suffix mass given by the author is sufficient at every step. This also
checks values between successive triangular thresholds, not just equality
at those thresholds. N=1 separately has time zero. Therefore the claimed
global maximum H(N)=max{h:1+h(h+1)/2≤N} is proved by the existing argument.

These are checks of the author's two linked inductions, not a new independent
theorem. In the fixed-box falsifier the persistent-cell birth records pressure
17,215 disappearing cuts, 3,106 delayed right births and 9,956 new blocks.
The all-size conclusion does not depend on these finite counts.

## 3. Deductive attack on the inverse/image axis

Every output boundary is an original boundary at a specified cumulative
mass. Consequently an input mapping to target (s_1,…,s_m) has a UNIQUE
segmentation into m weakly increasing refinements of those masses. Each
inter-segment boundary must be a strict descent, and that condition is also
sufficient. This verifies both directions and prevents overcounting. The
endpoint coefficient formula correctly treats equal endpoints separately:
an all-a refinement exists precisely when a divides the total. For a<b,
reserving one a and one b and multiplying finite-degree geometric series
accounts for every multiplicity exactly once. This entire partition/transfer
apparatus is standard supporting machinery, with zero independent novelty.

The substantive simplification is the exact meaning of the suffix threshold:
it is the minimum attainable first part of a feasible suffix refinement,
not a guessed lower bound or a claim that every larger first part is feasible.
Finiteness ensures that the minimum is attained. An incoming refinement only
needs to end above that minimum; a suffix attaining the minimum is as good
as any other for all such incoming tests. If its total s≤r no last part can
work. For s=r+1, that last part occupies all the mass, forcing the singleton
and new minimum s. For s≥r+2, the two-part refinement (1,s−1) works and
achieves the absolute lower bound 1. This proves the author's three branches,
including failure necessity, with no assumption of convex feasible endpoint
sets. At the right edge, an all-one refinement gives r=1 for any positive
last target part. The result is O(m) integer comparisons, not a bit-complexity
claim independent of input integer sizes.

The post-pilot addendum's reset/ladder parsing is correct. In its forward
encoding, every reset consumes the unique current ladder and emits a
triangular part ≥3 followed by a number of ones. The inverse must reserve
the FINAL triangular atom before grouping strings of ones; the author does
so. This removes the potential ambiguity when the last atom is itself 1.
Initial ones, every reset atom and its following ones, and the reserved
final atom have unique roles. Reversing the read-list produces the target
orientation specified in the original. The mass calculation agrees on each
complete cycle and on the combined initial/final piece. Thus the existing
construction is genuinely bijective, not just equality of counts.

The formal series manipulation has positive weights and zero constant term
for the reset and triangular series, so every coefficient is finite. It needs
no convergence/asymptotic result. The image ↔ triangular-composition connection,
including the threshold proof, is ONE structural residual axis, not several
paper contributions. A recurrence, generating function and a bijection to
the same class cannot be counted as independent axes.

The temporal mass bound does not determine this target grammar: the two
already supplied targets (2,3,2) and (2,2,3) have the same total and multiset
but respectively nonempty and empty fibres. Conversely the one-step grammar
does not analyze births across repeated merger rounds. These are distinct
proof obligations rather than two presentations of one static count.

## 4. Exact internal collision deductions

The original comparison sources below are physically frozen in
`inputs/originals/`, with their complete source paths and hashes in INPUT_ROLES.
No P208/P209 science, review or build body was accessed.

| Prior mechanism | Actual deduction, rather than title comparison |
|---|---|
| CRG, old replacement-crossclass SCOUT §CRG | Same composition carrier and component SUM aggregation, but edge predicate gcd(left,right)>1. Deduct all generic coarsening, adaptive recomputation, and coupled segmentation ideas. Its archived result has only length−1 and no sharp all-weight clock or closed target theorem. MNA's (1,2) differs, but that witness alone is NOT the value argument: its linear-growth left-mass induction and exact endpoint-minimum collapse are the residual. |
| P147, complete main.tex | This is equality-run consolidation: a constant run a^k becomes ka. Its proof traces a previously born parent and doubles mass at each generation. The generic ancestry idea is deducted. MNA requires the stronger oriented conclusion that the right parent was just born and a second induction forcing the left contribution t; equality doubling is false here. At total 7, MNA's supplied (3,2,1,1) lasts three rounds, while P147's proved same-weight maximum is floor(log2 7)=2. Thus the old sharp clock cannot be transferred by a same-carrier clock-preserving conjugacy, and a general 'one parent is new' argument alone gives no triangular bound. The old divisor-path inverse is also deducted as generic boundary transfer; it does not establish MNA's minimum-first threshold. |
| P121, complete main.tex | Its actual system chooses ONE adjacent pair randomly and replaces x,y by xy+1, starting from all ones. The ordered random history and Yule/BST split law drive its distribution/moment analysis. Neither sum conservation nor an autonomous simultaneous weak-increasing-run rule is present. Deduct genealogy/coalescence language; no P121 split-law/moment theorem supplies MNA's deterministic time or image theorem. |
| FPT, C08 in the 182–186 combinatorial ledger | At the LEFTMOST descent, transfer one unit from its left part to its right part; part count stays fixed and the position-weighted potential rises by one. This is a sequential priority unit-transfer mechanism, not MNA's simultaneous cut removal. Its potential and endpoint/local inverse motifs receive no new credit. |
| C21_PDCF, original 187–191 CANDIDATES §C21 | Retain a cut at prefix sum s_i exactly when the immediately preceding old part a_i divides s_i. The rule depends on an absolute prefix, not the neighboring right mass. Its generic monotone cut clock and target-local path DP receive zero credit. For (1,2), its sole cut is retained because 1 divides 1, whereas MNA removes it. Prefix divisibility cannot be substituted for MNA's order inequality in either linked mass induction or the endpoint-minimum proof. |

The P147 comparison is the strongest internal objection. MNA remains a
variant of an occupied run-coarsening family; it must not be advertised as a
wholly unrelated carrier or a novel generic merger paradigm. After full
subtraction, however, the residual is not merely a renamed predicate plus
the same abstract length clock and generic transfer formula. The proved
sharp mass scale changes from exponential to triangular and requires the
additional order/integrality induction; the structural residual eliminates
partition enumeration entirely to identify the full image with a known
class. I find this sufficient for the project's narrow two-axis candidate
floor, not a claim about suitability for any particular journal.

## 5. Public primary sources and exact residuals

Actual web request/return serializations are `evidence/mna_web01.actual.json`
through `mna_web07.actual.json`. They are browser tool returns, not raw HTTP
packets, downloaded PDFs, or proof that omitted pages were read.

- [Wiseman A353847](https://oeis.org/A353847), full returned primary entry:
  the example and supplied Split implementation identify equality runs.
  Together with original P147 this consumes equality-run summation and
  run-sum vocabulary. It does not specify MNA's weak-order rule.
- [Wiseman A375123](https://oeis.org/A375123), full returned primary entry:
  its maximal weakly increasing runs agree with MNA, but it keeps each run's
  FIRST part. For (1,2), its output is (1), MNA's is (3), and equality-run
  summation's is (1,2). The leader map loses total mass and the fibre/clock
  claims here do not follow from that literal. Nonidentity alone earns zero
  credit. No source claim to novel run detection is allowed.
- [OEIS A023361](https://oeis.org/A023361), full returned primary entry:
  Wilson's 1998 triangular-composition sequence, its reciprocal series and
  recurrence are fully owned. Arndt's 2014 comment additionally owns the
  reset-to-one or increment-by-one composition representation. I explicitly
  deduct that ladder/renewal encoding too. The remaining statement is its
  exact connection to this MNA image, not a new triangular sequence, a new
  renewal argument or a new generic reset language.
- [Robbins 2014](https://ac.inf.elte.hu/Vol_043_2014/239_43.pdf): my live
  request failed. I independently read the author's frozen, successful
  199-line extracted primary body in `inputs/author_lane40/sources/09_robbins_polygonal_primary.json`,
  including Theorem 1 and proof and Theorem 4(a). This is an inspected
  archived primary extraction, NOT my own successful fetch. These deductions
  fully own allowed-part composition counting. I use no numerical table or
  asymptotic assertion. The extracted table's 93 at N=12 conflicts with its
  recurrence's 94; neither the failed author screenshot nor this gate's
  failed fetch certifies printed typography.
- [Gessel 2019, AJC 74(2), 364–370](https://ajc.maths.uq.edu.au/pdf/74/ajc_v74_p364.pdf):
  inspected definitions and run-theorem statement on printed pp.365–366,
  not a complete proof audit of the seven-page paper. The ribbon series
  enumerates positive-integer words by successive weak-increasing run
  LENGTHS. Replacing each letter variable X_j by z^j records total mass but
  loses the separate run masses; it does not become MNA's target vector.
  Retaining separators plus endpoint variables recovers precisely generic
  refinement/transfer bookkeeping, which is already assigned zero credit.
- [Zhuang, Counting permutations by runs](https://arxiv.org/pdf/1505.02308):
  independently inspected the positive-word/ribbon definitions, Theorem 1,
  the run-network definition, and Theorem 2 with its matrix proof on
  printed pp.1–7 (selected contexts, not all 26 pages). General matrix
  weighting owns finite-state run transfer. A fixed run-length composition
  L is not MNA's run-MASS vector: different letters with the same L have
  different sums. The theorem takes an already specified run network and
  does not prove the candidate's endpoint-minimum collapse. Encoding that
  already proved grammar as a weighted network is an application of known
  transfer machinery, not an extra contribution.
- [Gessel–Zhuang FPSAC2019 metadata](https://www.mat.univie.ac.at/~slc/wpapers/FPSAC2019/6.html):
  metadata/abstract and TeX-directory link were obtained, but its PDF fetch
  failed here. I do not turn the source child's earlier selected pp.1,3–4
  read into my own body read. The directly inspected Gessel/Zhuang sources
  above supply the precise generic ribbon/run-network subtraction; no
  unexplored theorem in this paper is claimed either to prove or to refute
  MNA's residual connection.
- [Chen–Ono–Mogielnicki, arXiv:2607.12873](https://arxiv.org/abs/2607.12873):
  a current-six-month primary abstract/definition screen, not a full body
  read. It studies record compositions of alternating permutations (factor
  lengths cut before left-to-right maxima), not autonomous mass coarsening.
  No proof claim from that paper is reused.

My four query groups contain 13 actual focused searches, including explicit
2024–2026 wording and a recent-six-month arXiv-domain query. They found no
verified exact owner of MNA's clock/image connection. Irrelevant photography,
construction and other search hits are retained but are not mathematical
sources. There was no direct Google Scholar/Semantic Scholar API session,
no comprehensive bibliography crawl, no cross-model reviewer service and no
specialist contact. The novelty-check skill's exhaustive database/service
recipe is consequently not claimed fulfilled; project-authorized bounded
primary-source review is the actual scope. Source limitations are genuine.

## 6. Final claim boundary

The all-size claims survive mathematical checking. The two residual axes
survive the named actual adapters after deducting all generic coarsening,
ancestry, partition transfer, ribbon/run networks, triangular enumeration
and ladder renewal. This supports `GO_NARROW_TWO_AXIS` at candidate level,
with OWNER_AMBER / HOLD_EXTERNAL and no global priority assertion.

Do not promise a maximum-fibre formula or even a one-part maximizing target:
the original box and independent graph both give 58 at (6,5) for N=11 and
88 at (6,6) for N=12. No all-time inverse, exact pointwise time formula,
classification of every deepest state, analytic asymptotics, enlarged pilot
or new scientific lane is part of this clearance.
