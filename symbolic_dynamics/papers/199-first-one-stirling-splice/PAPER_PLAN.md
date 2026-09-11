# FOSP anonymous short-paper plan

Date: 2026-09-05 UTC. **P199 / ROUND0_DRAFT / HOLD_EXTERNAL**.
The central FIVE_SEAT_FREEZE.md subsequently authorized P199. The outline
below is retained as the planning baseline; current deliverables and measured
build results are in README.md and BUILD.md.

## Configuration and one-sentence contribution

Working title: **A Cyclically Relabelled Stirling Join: Exact Depth Layers
and Root-Cut Fibres**.

One-sentence contribution: For the fixed-rank map obtained by joining the
two occurrences of label one and cyclically relabelling, prove the exact
nonleaf-label entrance clock, every depth layer, the ordered-star cycle
census, and the complete target root-cut inverse with its sharp extremum.

Type: proof-first finite combinatorial dynamics note. Target: project
internal anonymous short-note series, not a selected external venue.
Use the existing `amsart` A4/10pt, 25 mm margin, numeric `natbib`, anonymous
author, empty date, and stripped PDF metadata conventions exemplified by
`papers/192-first-collision-hurwitz/main.tex`. No project author identity,
institution, funding, or contribution statement may be invented.

Budget: approximately 2,200 body words plus 120–150 abstract words, with
equations and references giving a planning target of 4–5 pages. This is a
planning estimate, not a compiled page count. Five main sections; proofs
remain in the main text. No appendix is needed for the accepted theorem
surface. Skill defaults for ICLR, a nine-page budget, and a one-page related
work section are overridden by the requested short `amsart` format.

`criteria_binding_unavailable`: no external venue/track criteria were
supplied, and no venue-alignment or submission-readiness claim is made.

## Claims–evidence matrix

| ID | Exact planned claim | Deductive evidence | Finite counterexample pressure | Section |
|---|---|---|---|---|
| F1 | `T(A1B1C)=dec(A) nn dec(B)dec(C)` is closed; `T=c o J_1` exactly | author proof Lemma 1; accepted source supplement | author word rule versus reviewer tree representation | 1 |
| F2 | `tau(w)=max I(w)` with empty maximum zero; sharp tail `n-1` for n>=1 | author proof Lemma 2; independent proof audit | complete n=0..8 author / n=0..7 gate graphs | 2 |
| F3 | recurrent states are n! ordered stars; exact period n for n>=2 and `(n-1)!` cycles | author proof Lemma 4 | full recurrent graph components | 2 |
| F4 | depth CDF `(n+t)!/(2^t t!)`, 0<=t<=n-1; exact layers by differences | protected insertion-gap proof, Lemma 3 | all depth populations in frozen transcripts | 3 |
| F5 | one-step image iff n is a root leaf, image size `2^(n-1)(n-1)!` | author proof Lemma 5 and root-degree polynomial | complete target membership/count checks | 4 |
| F6 | every nonempty target fibre has `1 + root children after n` sources; maximum n at exactly the stars with n first | author proof Lemma 6; complete inverse-set gate | every source set compared, not only indegrees | 4 |

At n=0 all relevant sets and the sole fibre have size one and depth zero.
At n=1 the sole word is fixed. These boundaries are explicit in the main
statements, not silently inferred from expressions involving `(n-1)!`.

## Detailed structure and transitions

### Abstract plan — 120–150 words

Open with the literal fixed-rank join-and-relabel operation, not generic
claims about symbolic dynamics. State the exact clock and depth CDF, then
the star n-cycles and target-cut fibre maximum. One final sentence makes
clear that joins/contour encodings are classical and the package retains an
external owner hold. No “first,” “novel,” or verified-priority language.
The abstract is to be drafted only after the central freeze.

### 1. Convention, map, and owned local operation — about 470 words

Purpose: define precisely what is iterated and disclose its closest owner
before presenting results. Define Stirling words, the two small boundaries,
the contour tree, and the first-occurrence reinsertion slot. State
`T=c o J_1` with c(1)=n and c(j)=j-1 otherwise; show why c alone does not
preserve the Stirling carrier (`1221 -> 2112` at n=2).

Source role: Janson / Janson–Kuba–Panholzer support the classical dictionary;
Brualdi–Dahl is the direct local-join owner and constrains the contribution.
The owned n-1 join-reduction scale is not presented as an independent new
result. Subtract P179/GSE commuting-idempotent bookkeeping and P148 generic
ordered-tree cuts in the internal-boundary paragraph.

Transition: the tree operation preserves each surviving vertex's ordered
children, identifying the statistic used by the next section.

### 2. Nonleaf-label clock and recurrent action — about 420 words

Purpose: establish pointwise dynamics before any enumeration. Define
I(w), prove `I(Tw)={j-1:j in I(w), j>=2}`, and derive the exact first
entrance time rather than merely an upper bound. Give the gate-approved
deep witness, characterize stars, and prove exact n-periodicity from the
cyclic action on labels in fixed root slots.

Evidence: author Lemmas 2 and 4; independent proof audit. All proof steps
stay in the body. Transition: the condition `tau<=t` is equivalent to
protecting the leaf status of labels t+1 through n.

### 3. Protected insertion gaps and depth layers — about 360 words

Purpose: derive the finite-depth population without fitting a census.
Use the unique maximum-pair growth decomposition, count allowed gaps as
`k+t` for k>t, and simplify the product to the CDF. State the exact layer
as `F_n(t)-F_n(t-1)` with `F_n(-1)=0`; check both endpoints `n!` and
`(2n-1)!!`. Background carrier enumeration is zero credit.

Transition: population counts do not reconstruct predecessors, so turn to
the labelled target's root list for a separate inverse analysis.

### 4. Image and complete target cuts — about 650 words

Purpose: classify every labelled one-step source and all maximum fibres.
First prove the root-leaf image iff test. For a target root list
`(...,n,c_1,...,c_r)`, reconstruct each source by adopting the first k
subtrees for k=0..r and prove distinctness and completeness. Derive the
maximum and all maximizing stars, including their `(n-1)!` count.

Then give the short root-degree polynomial calculation
`R_(m+1)=z(z-1)R_m'+(2m+1)R_m` and
`R_m'(1)=2^m m!` to obtain the one-step image count. Do not replace this
deduction with a sequence match. All arguments belong in the main text.

Transition: summarize the separate finite checks and explicitly delimit
what this short note does not prove.

### 5. Exact control and claim boundary — about 300 words

Purpose: distinguish deductive results, finite falsification, and the
unresolved owner boundary. Report author exhaustive coverage through n=8
and Stage-1 independent coverage through n=7 separately; do not add their
assertion totals into a theorem count. Include the n=0,1,2 boundaries and
one terminal-box row if space permits. Preserve the direct-owner kill
switch and P51–P56 missing-manuscript caveat.

No all-time inverse closed form, every iterated-image formula, asymptotic
law, publication-priority claim, or later paper-review PASS is permitted.
Repository/code availability may cite the artifact package after central
freeze; external availability, funding, and human authorship facts remain
unasserted unless supplied.

## Figure/table plan

At most one small explanatory vector schematic: a target root list with
n marked and three following subtrees, with the four possible adoption
cuts shown beneath. The comparison is between possible predecessors of
one fixed target, not between invented competing algorithms. Caption plan:
“Every predecessor is obtained by choosing one cut in the ordered suffix
after the root leaf n; the prefix before the cut is adopted by the restored
vertex one.” This makes the inverse mechanism visible without duplicating
the proof. If it expands the note, use the displayed root-list formula
instead; no decorative hero image is required.

A compact theorem inventory or n=0,1,2,8 census table is optional. All
entries must come from the pinned contract/transcript, not new extrapolation.

## Citation scaffold and source roles

- Section 1: Richard A. Brualdi and Geir Dahl, *Multipermutations and
  Stirling Multipermutations*, Graphs and Combinatorics 40, article 22
  (2024), [publisher](https://link.springer.com/article/10.1007/s00373-024-02751-2).
  Required direct subtraction: left-join, Theorem 8 reduction and Section 5
  tree surgery. The exact FOSP factorization is our comparison, not a
  theorem attributed verbatim to that source.
- Sections 1 and 3: Svante Janson, *Plane recursive trees, Stirling
  permutations and an urn model*, [arXiv:0803.1129](https://arxiv.org/abs/0803.1129);
  and Janson, Markus Kuba, Alois Panholzer, *Generalized Stirling
  permutations, families of increasing trees and urn models*,
  [arXiv:0805.4084](https://arxiv.org/abs/0805.4084). Classical encodings,
  insertion, and enumeration only. Exact publisher-version bibliographic
  fields remain to be retrieved before generating BibTeX; no fields are
  filled from memory.
- Section 1, optional short neighbor comparison: Lukas Nabergall,
  *The combinatorics of a tree-like functional equation for connected
  chord diagrams*, [arXiv:2104.02296](https://arxiv.org/abs/2104.02296).
  Retain the Stage-1 distinction between rank-reducing deletion and this
  fixed-rank composite; it is not the closest local owner after the delta.

The primary metadata pages above were reopened during outline preparation;
the detailed theorem-reading scopes remain those in the accepted source
audit. Bibliography creation and complete citation/source verification
remain downstream obligations, not completed by this scaffold.

## Evidence pins and outline-review status

All paths below are under `docs/papers197_201_sequence/`:

- `scouting/replacement_stirling_lane/THEOREM_CONTRACT.md`:
  `5c08d64027703fa98ce11d277b4e8e7a4dbc7842ee3402a3c3269e975d2b7db9`.
- `scouting/replacement_stirling_lane/PROOF_CERTIFICATE.md`:
  `81648ebcca6d1b3405975833436aedfd7e10d8aab2a2140073c1711d1df249b2`.
- `scouting/replacement_stirling_lane/STAGE1_SOURCE_SUPPLEMENT.md`:
  `ac21c168c5b58e651e4a5a42af485e496e0732751d328b9ab3cafc59c399c42c`.
- Binding acceptance: `reviews/fosp_stage1_20260905/DELTA_ACCEPTANCE.md`;
  author replay: `scouting/replacement_stirling_lane/AUTHOR_REPLAY_RECEIPT_20260905.md`.

Skills used: paper-plan claim/evidence and section mapping, plus ARS
academic-paper outline-only structure architecture. The GPT-5.4-specific
outline-review endpoint was not available after tool discovery. This is a
same-agent structure self-check, **not** a fabricated external or independent
outline review. The parent may review the outline separately. User's
standing no-routine-confirmation instruction and explicit central-freeze
gate supersede template interview/confirmation prompts.

Current authorized transition: complete the allocated P199 Round 0, then
hand the frozen artifact to a process-separated paper reviewer. The author of this outline
also performed its Stage-1 gate; that gate must not later be counted as an
independent paper Review A or B of the manuscript drafted by this agent.
