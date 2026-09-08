# C419 — round-one nonauthor full-manuscript review

Date: 2026-09-08 UTC. Reviewer: current-team agent `/root/lyness_round5`.
Manuscript author: coordinator `/root`; original M1 proof author:
`scout_nonlinear_return`. The reviewer is neither author. This is a substantive
AI-assisted internal review, not human peer review, an external-model result,
a venue recommendation, or a worldwide-priority certificate.

**Verdict: PASS for the stated manuscript contract. Mandatory findings: 0.
Optional findings: 3.** No missing mathematical hypothesis, invalid implication,
uncovered equality case, lost letter phase, or unsupported target-arithmetic
promotion was found in the reviewed inputs. The manuscript actually contains
the complete proof; its proof is not replaced by a research-note pointer.

This is the full raw review, not a favorable summary of another report. The
second manuscript review, final fresh deterministic build pair, formal route
evaluation and final release verification remain separate coordinator gates.
No acceptance score is invented: venue calibration is not applicable here.

## 1. Actual reading and frozen input identity

Paper root relative to the current batch:
`papers/C419_positive_trace_words/`.
Reviewed [actual PDF](../../papers/C419_positive_trace_words/builds/author_polished/main.pdf):
11 pages, 345,991 bytes,
SHA-256 `ed7db89ae850acb7530c11c703359faaee15f8dd3d4fe7e4a4ae2c59cb3146a0`.

Read all 14 actual TeX/Bib files, 881 lines in total: `main.tex`,
`math_commands.tex`, `references.bib`, all nine section inputs and both
external table inputs. Also read the two inline tables in Section 5. Read the
entire extracted PDF text, pages 1–11, and visually inspected all eleven
existing `builds/author_polished/page-01.png` through `page-11.png` images.
They agree with the inspected PDF text at the mathematical and pagination
anchors below. No new renderer or compiler was run during this review.

Additional complete reads:

- The paper's `PAPER_PLAN.md`, supplement README, relocated check receipt,
  and both copied Python sources.
- [Original proof](../../../continuation_c414_c418_round2/mapping_class/PROOF_PACKAGE.md),
  all 526 lines, including all ten proof steps and limitations.
- [Original source audit](../../../continuation_c414_c418_round2/mapping_class/SOURCE_AUDIT.md),
  all 235 lines, and original `CHECK_RECEIPT.md`, all 52 lines.
- Original `classify_word.py`, all 126 lines, and `line_automaton.py`, all
  130 lines; static reading only.
- [Current proof/increment review](../../mapping_class_review/REVIEW_PROOF_AND_INCREMENT.md),
  all 131 lines, and [current source review](../../mapping_class_review/SOURCE_AUDIT.md),
  all 91 lines. Their favorable conclusions did not replace direct checking
  of the actual new manuscript and proof.
- C413's predecessor proof, lines 1–160 only, for its exact object, theorem,
  periodic levels and displayed cycle families. This was a targeted collision
  comparison, not a new complete C413 review.

The source input hashes below were read before substantive review and read
again before this report; they were unchanged. Paths in this block are
relative to the paper root.

```text
e034a05eb06d2643847b55c4068bf1635ed477c124e1fb4a44913e28be5ee7c5  main.tex
cda6d69f13969136256cefea61a9c69023c9c8e50b9b5565375fe1c71e378e40  math_commands.tex
d2df438c5200ecb51cd11b3571738395de6c7bc186baf0341c4b4ebcf2e89e65  references.bib
f35554fd5f9c05ab52c57c8483de1ec5761d9ed0f693152770e5fd2551bfbb20  sections/0_abstract.tex
7e6b6400379c69f5fb97d7a89ec61cc389641d76b7f1ac65b1b37eeb3959bc3f  sections/1_introduction.tex
051a29e706f17c0969200a6dfca242499c2b4724ca9c948c7ad41eda8409dfbc  sections/2_conventions.tex
6d3334dec931822dcdca9c2f33fc7a02c6c9078f406d714bf99e36ade5627de7  sections/3_escape_descent.tex
d55255b3a11e723c2583873ef87f8becabff5936abd8072c2cc2b71c602e225e  sections/4_locus.tex
54a860e24568759c860ba7c4360b34f4b09a7fd3f17fec9a657246e7ac09ed6a  sections/5_levels.tex
c5816cba44b783daeaa9b025c04ea58aad97db266261f6ce6ad57dd357751fd2  sections/6_classifier.tex
e41b725037c37856f394c7b56179789db0fcb32ac3a92296ac90c7287b3dc0f1  sections/7_two_sided.tex
986743b3b995c0649ff2799d878bfcaa4fa79a2f22ec4795b1cff44e93a2bd6b  sections/8_scope.tex
3c42ac44ce77355dba5407b9d2c91c9912d7877daa978446ad5e4ef9cf23be75  tables/realize.tex
6b0899d3a699a0012a96b461751effd969876b1b32e744cb8cf408911dad752f  tables/source_scope.tex
```

Supporting input hashes, using repository-relative paths:

```text
619172d8a1d9a99015917069df6fe9d648a689dd680b4bd8bf6e05962628409e  henon_dynamics/continuation_c414_c418_round2/mapping_class/PROOF_PACKAGE.md
8699961aac4b7d73138ff72263a8041418a8963f5482bd13fac75df50ec9854e  henon_dynamics/continuation_c414_c418_round2/mapping_class/SOURCE_AUDIT.md
0843ee15f81b610b39e637ecaa1d1e6f5fd6c698e460b821e55dd13bd8043625  henon_dynamics/continuation_c414_c418_round2/mapping_class/CHECK_RECEIPT.md
65f61434a4acb513f3d46d2546a68f6661fca8459f4685e821f567323debcbbc  henon_dynamics/continuation_c414_c418_round2/mapping_class/classify_word.py
3e260e709b07c7b71a5a7977d8377fc95407262751fd32037676b5a06beb4e0a  henon_dynamics/continuation_c414_c418_round2/mapping_class/line_automaton.py
86ad170b5b968037a320950530ffcbc7dcc3ce14133bdcb6cd3c5969a883c434  henon_dynamics/research_c419_c423/mapping_class_review/REVIEW_PROOF_AND_INCREMENT.md
cf4ad25b70487d60eaa4daf0d1c80c349d3be33c6e39ccb3476eb7e0f02fc6d3  henon_dynamics/research_c419_c423/mapping_class_review/SOURCE_AUDIT.md
db8143d09154c21fe70f4c84f59b14524d451753784b9faa6d4521c2c3bc2afd  henon_dynamics/continuation_c409_c413_round2/nonlinear_geometry/PROOF_PACKAGE.md
```

## 2. Contract and claim alignment

Theorem 1.1, PDF page 2, `sections/1_introduction.tex:42–65`, retains all
quantified integer points, all integer levels, and every finite positive word
containing both specified letters. One application of the chronological word
map is the ordinary clock. No restricted word census, finite height, trial
period, generic line parameter, or nonsingular-level assumption has replaced
those quantifiers.

Its four conclusions form one coherent classification: the exact universal
locus and its existential converse, the uniformly bounded levelwise
classifier, and proper forward/backward escape outside each word's periodic
set. The abstract, introductory theorem, proof sections and limitations agree.
The bound 40 is correctly identified as a candidate bound, not an established
optimal least period or an attained 40-cycle. The paper does not classify
ordinary rational nonintegral points, complex schemes, multiplicities,
finite-field dynamics, or finite whole-group orbits.

The source-system determinant is expressly not a target Euler factor or a
Hilbert–Pólya realization. This review assigns no formal route tuple and makes
no A2/A3 promotion; `NO_BAD_EULER_OR_ROOT_NUMBER` remains in force.

## 3. Independent mathematical audit

### 3.1 Coordinates, direction and explicit separators — PASS

Anchors: PDF pages 3–4; `sections/2_conventions.tex:3–84`.
Both polynomial inverses are correct and preserve the integer lattice.
The displayed invariant identity and the exact conjugacy by coordinate swap
prove invariance for both letters. On the four signed all-two points the
two sign-pair actions are permutations with square the identity; hence no
outside point can enter that exceptional set under a letter.

The exponent rows give `R_w = R_last ... R_first`: for example, applying
the pair substitution A then B sends `(X,Y)` to `(X^2Y,XY)`, with exponent
rows `(2,1)` and `(1,1)`, exactly `R_B R_A`. The point-indexed row-action
matrices in Section 6 have the opposite chronological multiplication order
for the stated reason. There is no transpose/order error. The trace-at-least-
three argument applies to every admissible product and claims only matrix
hyperbolicity, not uniform hyperbolicity of the real surface.

The fixed-line/escaping-word example is valid: each sixth power fixes the
applicable trace-one plane, while `(A composed with B)(1,1,m)` has the
displayed cone image for every `m >= 3`. The ordinary four-cycle under ABB
is correct for every nonzero integer m, including m = ±1; its four states
are distinct. Its level is `m^2+1`. The predecessor theorem has only the
other two level families, and the factor-pair calculation excludes overlap
when `|m| >= 2`. The trace-four/determinant argument also separates this
word from powers of the single Fibonacci map.

### 3.2 Common cone and every all-large branch — PASS

Anchors: PDF pages 4–5; `sections/3_escape_descent.tex:15–97`.
Inside the common cone, positivity makes the third modulus exactly
`ac-b`, with `ac-b >= c`. Equality requires `a=2` and `b=c`;
the next occurrence of B then produces `c^2-2 > c`. This treats the
non-strict boundary and proves a limit to infinity, not just an unbounded
subsequence. The coordinate-swap case is exact.

For all-large states outside the exceptional set, the proof covers negative
product, a third-coordinate maximum, tied first/second maxima, and either
strict remaining maximum. In the latter case, the four branches of
`d=bc-a` exhaust all integers. In particular the `d <= -2` branch is
correctly excluded by next-step cone entry, not falsely called immediate
descent. The exceptional all-two output cannot have an outside preimage.
Every surviving cone-free all-large step strictly decreases an integer
maximum, so entry into the small set is finite. The small-set exit inequality
is strict even at the smallest possible large coordinates, 2 and 2.

### 3.3 Every letter phase and exactly 39 lines — PASS

Anchors: PDF pages 5–6; `sections/3_escape_descent.tex:99–123` and
`sections/4_locus.tex:3–40`.
Expanding a word-periodic orbit gives a finite repeating letter trajectory
with the required two-letter recurrence. Once it reaches the small set it
cannot exit without escaping, so periodicity forces every phase to remain
small. A third coordinate that is the only small coordinate has both possible
predecessors all-large. This direction-sensitive exclusion is justified at
every phase, not only at word boundaries.

The fixed-small-coordinate rotations have orders dividing 4, 6 and 3 for
coordinate 0, 1 and -1. Their full lists of possible moduli include
`|y-z|` or `|y+z|`, with the signs correctly retained. If all of these are
large, the next opposite letter exits the small set. The necessary residual
condition is exactly `z=cy+b` with `c=±1`, `b` in `{-1,0,1}`; swapping
x and y gives the other six lines. Together with the 27 axis-parallel
lines this gives exactly the stated 39, not the historical diagnostic's 45.

### 3.4 Positive-word realization — PASS

Anchors: PDF pages 6–7, Proposition 4.2 and Table 2;
`sections/4_locus.tex:42–72`, `tables/realize.tex:5–11`.
The twelfth powers act identically on the specified small-coordinate planes.
Every table image follows from the actual one- or two-letter substitution;
in particular A squared sends `(c,t,ct+b)` to `(c,cb,-ct)`.
Thus `G^(12-r) composed with F composed with G^r` fixes the whole line,
uses positive letters only, and contains both letters even for r=0.
The four exceptional points are fixed by the stated A-squared/B-squared
word. This establishes the existential union of fixed sets, and therefore
the existential union of periodic sets. It does not imply that a candidate
is periodic for every word; the manuscript repeatedly preserves this boundary.

### 3.5 All integer levels and the uniform bound — PASS

Anchors: PDF pages 7–8; `sections/5_levels.tex:3–104`, Tables 3–4.
Distinct varying-coordinate directions and fixed intercepts justify the
line count. Restriction of K gives exactly the two displayed quadratic
expressions, with multiplicities 3, 16 and 20 after allowing parameter sign.
The signed factor pairs of 1, -7 and -3 give the three pairwise overlap
levels 1, 4 and 2. Negative parameter values are included.

Consequently only one quadratic family can contribute above level four,
giving bounds 6, 32 and 40. The low-level descriptions remove actual point
overlaps: sizes 1, 6, 16 and 26 at levels 0, 1, 2 and 4. For level four,
the patterns counted as `6+4+12+4` have distinct absolute-coordinate
patterns/product signs. The forms yield no negative level or level three.
The discriminant and parity tests recover all roots, including repeated
roots, and the exceptional set is added exactly at level four. There is no
hidden height cutoff or finite-level extrapolation.

### 3.6 Exact word cycles, least periods and determinant — PASS

Anchors: PDF pages 8–9; `sections/6_classifier.tex:3–95`.
Each letter restricts to a partial injection on the exact point set. The
matrix product and the explicit algorithm both reject an edge immediately
when any intermediate letter image leaves that set. The every-phase theorem
therefore preserves every genuine word cycle. Conversely every retained
cycle consists of actual coordinate transitions, and distinct vertices
preserve the ordinary least period.

A finite partial injection has only chains and cycles; an extra tail into a
cycle would violate injectivity. Thus the traversal and the trace formula
are complete. Nilpotent chain blocks contribute determinant one, each
d-cycle contributes `1-u^d`, and the empty-set convention is correct.
The finite determinant identity is explicitly deducted as a classical
consequence, not a separate arithmetic theorem.

### 3.7 Proper escape in both directions — PASS

Anchors: PDF pages 9–10; `sections/7_two_sided.tex:3–78`.
The forward proof does not assume periodicity when applying the later
small-coordinate rotation argument. A cone-free repeated-word orbit
eventually has every phase in the finite set at its invariant level.
Bijectivity turns eventual repeated word states into periodicity of the
original point. Consequently every nonperiodic point actually enters the
cone and tends to infinity at ordinary word times.

For backward time the polynomial involution satisfies both reverser
identities. Reversing the chronological word, not commuting its letters,
gives `W^(-1)=R U R`. Nonperiodicity passes to `R(P)` under U. The explicit
bound on Q from a bound on `R(Q)` proves properness of R, so a sequence
tending to infinity remains so after applying R. This establishes proper
backward escape, not merely backward unboundedness.

## 4. Static implementation and historical evidence

Both supplement code files compare byte-for-byte equal to the frozen
originals; `cmp` returned 0 for each. The hashes are those in Section 1.
No import, self-test, census, symbolic program, or classifier execution was
performed for this review.

`lines()[:39]` is exactly the 27 axis lines followed by the x-small and
y-small slanted families. The helper's last six definitions are not used
by the point classifier. Its coefficient recovery from parameters 0, 1,
-1 is exact because the manuscript has already proved the restrictions
quadratic, rather than because three numerical samples establish degree.
`isqrt`, square equality, parity, coordinate substitution and set
deduplication implement the proved construction. `classify` requires both
letters and tests membership after every letter. Its walk termination and
cycle accounting agree with the partial-injection proof. Assertions are
development checks, not a certification or hostile-input security claim.

The helper's generic-line `word_cycles` routine and observed generic-period
histogram are not equivalent to integer point periodicity; the manuscript
and supplement explicitly explain this. They do not assert an optimal
period list from the diagnostic.

The relocated supplement receipt differs from the original only in its two
Markdown targets, as verified with `diff -u`. Its historical reserve-stage
wording is preserved and explicitly contextualized by the supplement README.
Those old finite and symbolic PASS records are historical evidence, not
newly executed results or a substitute for the infinite proof.

Supplement receipt SHA-256:
`ec096d5f3d65e3b96f69f6c18e494f0a9d284d55af37f3e944e6332883c7e2b2`.
Supplement README SHA-256:
`062bb018bf7ea421eac2744f81f3ed70b6df48cc1fa45e0bf48119ba0613c855`.

## 5. Source ownership and bibliography

Both entire local audits were read. This review also made bounded fresh
primary-source accesses; it did not repeat a broad novelty search or claim
complete reading of every cited external paper.

- Sasaki–Yoshida's published PDF, Section 2.1, printed pages 26–27, explicitly
  gives the same two full-trace maps and lower/upper matrices. Lemma 2.1
  supplies their iterate formulas, and Section 2.2 describes conic dynamics.
  These are correctly credited rather than claimed as new.
  [Published source](https://www.jstage.jst.go.jp/article/tmj/60/1/60_1_23/_pdf).
- Roberts (1996), introduction, Section 4/Remark 4.1, Theorem 4.2 and
  Corollary 4.1, already treats broad infinite-order trace-map escape.
  Its strict half-trace threshold and region hypotheses do not by themselves
  supply the manuscript's exact integer boundary exhaustion. The manuscript
  correctly deducts the general escape mechanism.
  [Author-hosted published PDF](https://web.maths.unsw.edu.au/~jagr/R96.pdf).
- Humphries' introduction and Theorem 1 explicitly distinguish finite
  whole-group orbits from finite orbits under each group element and prove
  equality of those two sets. The half-trace convention is explicit. Neither
  quantifier equals an existential union over single positive words, as the
  manuscript's direct counterexample also shows. Its versioned record is
  dated 8 November 2016; no journal status was inferred from the HTML date.
  [Primary text](https://arxiv.org/html/1611.02743v1),
  [version record](https://arxiv.org/abs/1611.02743v1).
- Ghosh–Sarnak's version-three record confirms 30 May 2022 and the related
  Inventiones publication. Its abstract concerns the same cubic's integer
  points and finitely many Markoff-group orbits, not finiteness of each
  individual orbit. This visit checked record/abstract only; the more
  detailed theorem comparisons are those actually recorded in the two
  complete local audits. [Version record](https://arxiv.org/abs/1706.06712v3).
- Cantat–Loray's publisher record confirms the 2009 title, volume 59(7),
  pages 2927–2978 and DOI. Its stated object is mapping-class-group dynamics.
  The manuscript does not silently attach the older preprint's Theorem 5.3
  locator to that publication. This visit checked record/abstract only.
  [Publisher record](https://aif.centre-mersenne.org/item/AIF_2009__59_7_2927_0/).
- Roberts–Baake's author PDF and DOI resolver failed on this visit; the
  direct Springer record was accessible. Full-text ownership/normalization
  comparison for this item remains the explicitly recorded earlier primary
  accesses, not a claimed fresh PDF reading.
  [Publisher record](https://link.springer.com/article/10.1007/BF02188581).

C413 is honestly identified as an internal anonymous manuscript, not a
journal article. Its targeted theorem read confirms the deducted single-map
classification and two old level families. The residual here is the whole
positive-word integer exhaustion and exact word-dependent core, not the
generators, escape idea, conic rotations, fixed-curve mechanism or finite
determinant identity. This supports the admitted scope; it does not certify
worldwide priority. The previously inaccessible period-two-curve follow-up
remains an explicit source-coverage limitation, not an excluded theorem list.

## 6. PDF and presentation observations

All eleven pages were inspected, not just the title and conclusion. The
four-part main theorem is intact on page 2. The direction conventions,
four-way descent split, small-coordinate matrices, line-realization table,
low-level table, pointwise classifier and reverser equations are readable.
There is no visible clipped equation, missing glyph, blank proof page,
overlapping table column or broken mathematical reference. Equation 7.2 and
the final norm expression are correctly rendered even where plain-text
extraction is imperfect.

Read-only `pdfinfo` confirms 11 pages and 345,991 bytes. `pdffonts` lists
19 fonts, all embedded. The final log contains no matches for `Warning`,
`Overfull`, `Underfull` or `undefined`, and its output line agrees with the
actual PDF size/page count. Final-log SHA-256:
`3995b170edd8d41bd7eb62a08bdc57c3b25c38d815b7fc081724f87e84372483`.
These are observations of this author-polished build, not a fresh-build
reproducibility claim or a reclassification of the preserved first build.

### O1 — optional, minor, high confidence: keep the realization conclusion together

Anchor: PDF page 6 bottom/page 7 top;
`sections/4_locus.tex:61–68`, `sections/5_levels.tex:23–36`.
Equation 4.2 finishes page 6, but its predicate and final justification begin
page 7 after Table 3, a float from the next section. No text is missing and
the proof is correct; the page turn is unnecessarily interruptive. If
revising the layout, keep equation 4.2 with its following conclusion or
keep Table 3 within Section 5. This does not require a mathematical rerun.

### O2 — optional, minor, high confidence: make pairwise separation explicit

Anchor: PDF page 7, Lemma 5.1;
`sections/5_levels.tex:38–40`.
The proof establishes that the three level families are pairwise disjoint
above four. The wording “have no common values” could also be read as only
excluding a three-way intersection. Replace it with “are pairwise disjoint
above four” if desired. The following proof and bound already use the
correct stronger statement, so this is a clarity improvement, not a gap.

### O3 — optional, minor, moderate confidence: identify the inaccessible follow-up

Anchor: PDF page 10; `sections/8_scope.tex:29–32`.
The standalone article names an inaccessible period-two-curve follow-up
without identifying its authors or year. The original source audit identifies
Humphries–Manning (2015), *Curves of period two points for trace maps*.
Adding that short identification, or a bibliography entry using the already
verified metadata, would make the limitation traceable without opening local
notes. It must still say that the unseen theorem list was not excluded;
adding metadata does not justify claiming new full-text coverage.

## 7. Mandatory findings, requested response and gate boundary

Mandatory findings: **none**. No counterexample, missing phase condition,
incorrect all-level bound, converse error, matrix-order error, or properness
gap survived the above direct audit. No additional finite census or old test
rerun is requested. The supported judgment is that the manuscript faithfully
and self-containedly realizes the admitted source-classification contract.

The author may accept or decline O1–O3 with a short recorded reason. If
implemented, inspect the affected text/layout and retain the genuine revised
PDF; do not modify the frozen original proof or fabricate a mathematical
revalidation. The next manuscript round should inspect the actual revised
inputs under the coordinator's assignment.

The research-review and auto-paper-improvement-loop requirements were applied
as a full nonauthor manuscript/proof/source review with preserved raw findings.
The repository's current-team workflow governs the available-model fallback;
no legacy named external model, ML-conference score, or manuscript upload
was used. An attempted bounded helper delegation was unavailable because the
agent thread limit was reached; there is no helper result in this review.

Only this report was written. No author TeX/Bib/PDF, supplement, original
research file, mathematical output or Git state was changed by the reviewer.
