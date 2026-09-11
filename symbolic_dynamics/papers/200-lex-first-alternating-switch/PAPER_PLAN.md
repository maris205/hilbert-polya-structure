# P200 allocated plan addendum

The central FIVE_SEAT_FREEZE.md now authorizes P200 Round 0. The following
prior outline is retained as the argument baseline; its pending-freeze
wording records the earlier milestone, not the current stage. Current
status and measured build evidence are in README.md and BUILD.md.

# LFAS anonymous short-paper plan

Date: 2026-09-05 UTC. **OUTLINE_ONLY / CENTRAL_FREEZE_PENDING / HOLD_EXTERNAL**.
No paper number, formal manuscript, `.bib`, or PDF is created by this plan.

## Configuration and one-sentence contribution

Working title: **Least Alternating-Rectangle Switching: A Width-Uniform
Tail Bound and Exact Predecessors**.

One-sentence contribution: For repeated lexicographically least binary
matrix interchange, identify the invariant pivot and two-visits-per-partner
structure, prove the row bound `2r-3` sharp for every `s>=r+1`, and give a
target-only inverse rule with maximum `(r-1)(s-1)` and all equality cases.

Type: proof-first combinatorial dynamics short note. Format: project
anonymous `amsart` A4/10pt, 25 mm margins, numeric `natbib`, empty date,
stripped metadata, as in the accepted P192–P196 notes. No external venue
has been chosen. Plan approximately 2,450 body words plus a 120–150-word
abstract, normally 4–5 pages including formulas and references; this is
not a verified compiled page count. Five main sections, all central proofs
in the body, no appendix required. Do not inflate the related-work section
to satisfy generic ML-paper template defaults.

`criteria_binding_unavailable`: no external target/track binding supplied;
no venue fit or submission-readiness assertion is made.

## Claims–evidence matrix

| ID | Exact planned claim | Deductive evidence | Finite counterexample pressure | Section |
|---|---|---|---|---|
| L1 | least incomparable row pair and first opposite column signs implement the literal rectangle order | author Theorem 1 setup; gate proof audit | naive four-entry selector versus row-support implementation | 1–2 |
| L2 | invariant first pivot, nonincreasing partner; exact recurrent iff test and only periods1,2 | author Theorem 1; intersection/union and selector arguments | complete functional graphs in author and gate controls | 2 |
| L3 | `tau<=2p-1<=2r-3`; equality for every r>=2,s>=r+1 | author Theorem 2; two-visits argument and explicit witness | 38 wide witnesses in each implementation; full small boxes | 3 |
| L4 | complete target-only predecessor sets from difference prefix and intervening-row comparability | author Theorem 3; independently rederived source necessity/sufficiency | every target SOURCE SET compared, including zero fibres | 4 |
| L5 | maximum `(r-1)(s-1)`, exactly two complementary maximizers except all16 at2x2 | author Theorem 4; equality in partner and column capacities | complete equality-target sets across all registered boxes | 4 |

Row/column margins, lonesum fixed points and their classical census,
generic descending-selector period arguments, and generic inverse
admissibility receive zero novelty credit. No new contribution is claimed
merely because the schedule is deterministic.

## Detailed structure and transitions

### Abstract plan — 120–150 words

Specify the four-index row-first lexicographic schedule immediately. Lead
with width-independent tail control sharp only in the stated wide regime,
then the target inverse formula and all maximum fibres. Briefly state the
invariant-pivot mechanism and distinguish the classical local interchange
from the admitted theorem package. End with the bounded evidence / external
hold boundary. Do not advertise a sharp formula for every rectangle size.

### 1. Literal interchange and subtraction — about 440 words

Purpose: prevent scheduler and carrier ambiguity. Fix `r,s>=2`, all labelled
binary matrices, rectangle order `(i,k,a,b)` with i<k,a<b, alternating
patterns, and hold branch. Define row supports and the least incomparable
pair equivalence. Cite Ryser for the local move and margins, Brewbaker for
lonesum background, and Baggett–Yan for nearby full interchange-graph
geometry. Explain that their line fibres are not this map's predecessor
fibres and that compression toward a prescribed basis is not this update.

Source roles: Ryser/Brewbaker support classical setup; Baggett–Yan is a
mandatory near-owner constraint. The internal TSW and P181/P192/P194
subtraction should be concise but explicit. Transition: containment of
earlier rows around the selected pair reveals the persistent pivot.

### 2. Pivot persistence and recurrent matrices — about 510 words

Purpose: characterize the periodic part without enumeration. Prove every
earlier row lies below the selected pair's intersection or above its union,
so the first pivot remains fixed and the partner cannot increase. State
the exact recurrent test: the first two differing columns have opposite
types and the switched pivot stays comparable to all intervening rows.

Give the selector-equality argument for strict two-cycles, the exclusion
of nonfixed sources into a fixed target, and the classical chain-of-row-
supports description of fixed matrices. No new lonesum census theorem is
necessary. Transition: track how often one partner can appear before that
local return test succeeds.

### 3. Two visits per partner and sharp wide tails — about 540 words

Purpose: replace generic rectangle-count reasoning with actual row geometry.
Use the signed difference word: after one switch the first two differing
positions are opposite. Counting selector states through first recurrence
allows at most two appearances per partner and proves `tau+1<=2p`.
Make the inclusion of the first recurrent state explicit to avoid an
off-by-one bound.

Give the full wide witness
`A_0={r}`, `A_k={0,k} union {k+2,...,r}` on r+1 columns and its two
selectors per decreasing partner. Prove the witness inductively, and show
trailing zero columns preserve it. State the 2x2 exception and keep the
square/narrow conjecture outside the theorem. Transition: the same signed
row differences yield an inverse condition on the target, but require an
independent necessity/sufficiency proof.

### 4. Target prefixes, image recognition, and extremal fibres — about 700 words

Purpose: replace testing a selector on each reversed source with explicit
conditions involving only the target. Define D_k,E_k,j_k, the next
same-type difference b_k, and the allowable opposite prefix. Require the
reversed pivot to be comparable with all intervening rows. State the exact
source set and image iff condition, including fixed targets' sole source.

Prove both directions, the exclusion of earlier pivots under reversal, and
distinctness of rectangle choices. Bound the partner contributions by
s-1 and classify every equality target. Spell out the two complementary
star-shaped row patterns; when r=s=2 all16 targets have fibre one.
Keep the full inverse and equality proofs in the main text.

Transition: finite graphs check the formulas and also record why tempting
extra claims were excluded.

### 5. Exact checks and unresolved boundaries — about 260 words

Purpose: state the tested scope without turning it into all-size evidence.
Author: 11 complete boxes, 38 wide witnesses, 1,076,738 assertions per run.
Independent Stage-1 control: 13 complete boxes, 273,040 states, 38 wide
witnesses, 3,595,488 assertions per run. Do not present the two runs of
one verifier as independent proofs or add their counts into a system count.

Use the measured `3x4` versus `4x3` image sizes, 3292 and 3290, as a direct
warning that transposition does not conjugate the row-first scheduler.
The expression `2min(r,s)-3-1{r=s}` remains conjectural; no all-depth or
basin enumeration is claimed. Preserve `OWNER_AMBER/HOLD_EXTERNAL`, the
P51–P56 gap, and the requirement for later paper Review A/B.

## Figure/table plan

No raster hero figure. A six-entry selector itinerary for the r=4,s=5
wide witness is the smallest useful visual:
`(0,3,0,4),(0,3,0,3),(0,2,0,3),(0,2,0,2),(0,1,0,2),(0,1,0,1)`.
Group entries into three partner pairs and mark the last as the first
recurrent selector. Caption plan: “Two selector states per partner are
attained along the wide witness; the final pair begins a strict two-cycle.”
This is an exact illustrative orbit, not a new empirical claim.

If a theory-comparison table helps, contrast the old generic rectangle-count
bound `binom(r,2)binom(s,2)-1` with the proved width-uniform row bound and
its sharpness regime. Do **not** call the new bound numerically tighter on
every tiny box: at2x2 the exact tail is0 while `2r-3=1`. A small census
table should prioritize boundaries and the asymmetric pair, not maximal
parameter boxes for visual impact.

## Citation scaffold and roles

- Section 1: H. J. Ryser, *Combinatorial Properties of Matrices of Zeros
  and Ones*, Canadian Journal of Mathematics9 (1957),371–377,
  [official DOI](https://doi.org/10.4153/CJM-1957-044-3).
  The local interchange and margins are fully owned background.
- Sections 1–2: Chad Brewbaker, *A Combinatorial Interpretation of the
  Poly-Bernoulli Numbers and Two Fermat Analogues*, Integers8 (2008),A02,
  [official article](https://math.colgate.edu/~integers/i2/i2.pdf).
  Lonesum characterization and counting receive no new credit.
- Section 1 and limitations: Jeffrey S. Baggett and Huiya Yan,
  *Interchange graphs of (0,1)-matrices are maximally Hamiltonian*,
  [arXiv:2607.13165v4](https://arxiv.org/html/2607.13165v4), revised
  17 August2026. Mandatory nearby full-graph/row-pattern geometry source;
  the gate inspected the line-fibre and compression scope directly.
- Optional brief Markov-basis context: Persi Diaconis and Bernd Sturmfels,
  *Algebraic Algorithms for Sampling from Conditional Distributions*,
  [DOI](https://doi.org/10.1214/aos/1030563990). Preserve the author's
  declared partial retrieval/read scope; do not claim a new complete
  full-text check in this outline.

Bibliographic records above are carried from the primary-source-checked
Stage-1 packages. Retrieve publication metadata and verify every eventual
BibTeX field before creating the manuscript bibliography. No source title
or result is invented to enlarge the related-work section.

## Evidence pins and review status

Under `docs/papers197_201_sequence/`:

- `scouting/lfas_reentry_20260905/THEOREM_CONTRACT_AND_PROOF.md`:
  `86005efbe22159d5f1ae33b0636de1432bec66c9e7ef7732123fc56712772730`.
- `scouting/lfas_reentry_20260905/SOURCE_AND_COLLISION.md`:
  `bd8efa8e4f64d9d136cc59fb3138f2fd05e6772383d5499f8d878cfcf1c3de0c`.
- Binding gate: `reviews/lfas_stage1_20260905/GATE_REPORT.md` and
  `DELTA_ACCEPTANCE.md`; author replay receipt is in the re-entry package.

Skills: paper-plan evidence matrix and section planning; ARS
academic-paper outline-only architecture, customized to the project.
The specified GPT-5.4 review endpoint is unavailable. No independent
outline-review claim is made: this is a same-agent structure check pending
parent inspection, not paper Review A/B.

Next authorized transition is the central five-seat freeze, after which
the root may assign the paper number and drafting directory. Anonymous
metadata, truthful code availability, and any required disclosure facts
must follow project conventions without invented authorship/funding.
Because this outline's author performed the Stage-1 LFAS gate, a later
manuscript drafted by this agent requires two different paper reviewers;
the Stage-1 gate cannot be relabelled as either paper review.
