# C425 — second actual nonauthor manuscript review

2026-09-09 UTC. Reviewer: assigned current-team arithmetic-lane agent,
not the C425 manuscript author or the coordinator who wrote the Fricke
proof. The reviewer also conducted the first actual manuscript pass
and earlier proof review. This is a fresh inspection of the actual
revised source and PDF, not either earlier report relabelled as round 2.
It is AI-assisted internal review, not external human peer review.

## Verdict

**P1 is closed. Mathematical must-fix: 0. Source/evidence must-fix: 0.
New minor or optional findings: 0. Further manuscript changes requested: 0.**

The sole coordinator-adopted abstract correction is implemented exactly
and now agrees with the theorem, the whole-line exhaustion proof and the
explicit possibility of travel between lines. The complete revised
manuscript regression found no new defect. Recommend closure of the two
scheduled manuscript-review passes, subject to coordinator adjudication.
Formal evaluation, the final fresh identical-input build pair and release
remain separate pending gates. This report assigns no numerical score,
worldwide-priority certification or publication acceptance.

## Actual revised object and full inspection

The reviewed `papers/C425_fricke_return/main.pdf` is 12 pages and
378223 bytes, SHA-256
`e7330f65920c40c566b01ee0d864d9f5a023c70010954e8af633c325f92c1dcb`.
Actual byte comparisons show equality with `main_round1.pdf` and
`build_round1_01/main.pdf`. The preserved initial PDF
`main_round0_original.pdf` is byte-identical to `baseline.pdf` and
`build_initial_04/main.pdf`, SHA-256
`aa6c4ee4bbc6f55bcf2934caccc927bf36aef872bf230466541c0f3de7b2f207`.

This pass freshly read all twelve active manuscript inputs in full:
`main.tex`, `math_commands.tex`, `references.bib` and all nine section
files, including all three tables. It separately read all of `build.sh`,
ROUND1_HANDOFF, the full 230-line first review, complete source diff,
input manifest, improvement log/state, SOURCE_AUDIT and historical
BUILD_REPORT. All 614 lines of the revised extracted PDF text were read,
and all twelve individual revised page images in
`build_round1_01/pdf_pages/` were actually viewed. A fresh streaming
`pdftotext -layout main.pdf -` was byte-compared with the saved text.
Thus the text read belongs to the current PDF, not the initial build.

The full first report is preserved unchanged as `ROUND1_REVIEW_RAW.md`;
an actual `cmp` against `manuscript_reviews/round1/C425_REVIEW.md`
succeeded. Its SHA-256 is
`e7e8a2cf840d37d52dc1dad9120342d60e711684a627e64dad6f8a61e5adb81e`.

## Exact change boundary and P1 resolution

All thirteen current reproducibility inputs passed `sha256sum -c
ROUND1_INPUT_MANIFEST.sha256`; the manifest SHA-256 is
`c9e8e11efeca9502f0b610847910736f613aa283f77f3f81a01d05c443b2b878`.
Each current input was also individually byte-compared with its actual
revised build's `source_snapshot/` member. All thirteen matched.
Each of the twelve inputs other than the abstract was independently
byte-compared unchanged with `baseline_source/`.

The generated, timestamp-free abstract diff was byte-compared with
`ROUND1_SOURCE_DIFF.patch`, SHA-256
`ac5b78c6543c875d8ee9869ad7ef6c82066fa90e39656b4364c394d2fca077ce`.
It contains exactly the two-line source substitution, with no other
active-input changes. The revised abstract SHA-256 is
`b07dad836fdd37ce8c7dc1a6f1335fb0caf4c18abe83681a1493d4b441211245`.
The complete initial-versus-revised extracted-PDF diff affects only
this sentence and the resulting six abstract-line wraps; all remaining
extracted text is unchanged.

At `sections/00_abstract.tex:14` and PDF page 1, the new statement is
that bijective affine parameter maps place every large periodic orbit
in a finite union of whole periodic lines. It no longer identifies a
finite orbit with an infinite line or asserts containment in a single
line. Theorem 1.1 item 2, Proposition 5.3 and the paragraph immediately
after Proposition 5.3 agree: the line union is invariant, its component
lines consist of periodic points, and a native orbit may move between
distinct lines before returning. Theorem 1.1 and its proof required no
change. The revised abstract's 27-line, 54-return and level-count
bounds are unchanged and retain the certified-return/least-period
distinction.

## Mathematical regression against the full revised manuscript

The following are fresh hand checks of the typeset argument, not
executed symbolic diagnostics or a new finite-core enumeration.

1. The native word remains `T=s_z o s_y o s_x`, rightmost first.
   The lifted inverse is correct and three steps from phase zero give
   exactly this word. Native triples partition the scalar coordinates,
   so the maximum in (2.6) includes intermediate factor updates.
   All ordered integer coefficients, zero coordinates and singular
   affine levels remain in scope.
2. At a genuine scalar maximum, the two recurrences in Lemma 2.1
   first bound both neighbors by two using integrality, then exclude
   either magnitude-two value by `2M-2-H>M`. The later propagation
   does not misuse this maximum lemma at a merely large coordinate.
3. Both edge identities in Table 2 and Lemma 3.1 have the correct
   phase, endpoint and parameter. Type I uses `v^2=1`; Type II uses
   `a_i=u`. Every intermediate line has a unit-slope coordinate and
   every edge parameter map is a bijection of the integers.
4. Lemma 4.1 exhausts omitted-edge cases: `|c|>=2` for Type I,
   then `|b|>=2`, `|b|=1` and `b=0` with `|a_(i+2)|>=2` for
   the zero case. Its estimates remain strict under `M>100B0`;
   both quadratic factors exceed `M/2`. Only 27 transitions are
   required for a repeated state among 28 visits, so there is no
   unjustified indefinitely iterated height estimate.
5. Phase return implies `3|ell_C`. Identity and reflection returns
   make entire parameter lines pointwise periodic, while nonzero
   translations cannot contain periodic parameters. Inclusion of
   every intermediate image in (5.3) and surjectivity of the affine
   integer maps prove equality with the forward image. Ambient
   bijectivity then supplies the inverse-image equality and removes
   every putative pre-cycle tail. This closes the entire orbit into
   the line union and is precisely the revised abstract's content.
6. Disjoint cycle-state sets give `sum ell_C/3 <= 27`, and dividing
   the lifted identity/reflection returns by three gives at most 54.
   These are line-count and return bounds, not assertions of every
   generic least period. Coincident lines can only reduce the count.
7. The partial map on `Q_R` has exactly the cycles wholly contained
   in the box. Injectivity makes any first repetition a return to
   the seed. The `N_R+1` bound proves finite termination. A box exit
   rejects only a wholly-box orbit; it does not falsely declare a
   line point nonperiodic. Line-union invariance removes entire core
   cycles and proves the exhaustive and disjoint output rules.
8. A unit-slope coordinate proves integer saturation and injectivity
   of every line. Linear equations decide coincidence and integral
   intersections. The divisor-indexed polynomial vectors in (6.1)
   distinguish identically zero vectors from finite gcd-root sets;
   zero and constant gcd cases are covered. The generic least period
   and every exceptional integer parameter are therefore determined.
9. Invariant transport in Section 7 is correct. Every originating
   state-line restriction is monic quadratic, preserved through the
   intermediate images and unit-slope reparametrizations. At most
   54 line points plus `N_R` core points lie on one integer level.
   Thus the ordinary primitive-cycle product is legitimate fibrewise;
   the manuscript correctly declines finite all-lattice fixed counts
   when a retained periodic line exists.

No sharpness, practical running-time guarantee or computed all-coefficient
census has been introduced. Procedure 6.3 is an exhaustive terminating
rule, and no mathematical execution is required to repair P1. The
earlier optional invariant-based observation about retained graph cycles
remains optional; its omission does not invalidate the affine-return test.

## Source, provenance and build regression

The bibliography and ownership discussion are byte-unchanged. They
continue to subtract Shin's independent-coefficient/group-orbit and
height/low-coordinate mechanisms, Cantat's fixed-fibre dynamics and
integral-finiteness consequence, and the complete C421 equal-forcing
slice. The surviving assertion is the specified-word, level-uniform
line/core exhaustion, not these earlier ingredients. The other three
public comparisons remain contextual rather than proof dependencies.
The six-entry bibliography, nine citation commands and six resolved
keys were checked in the actual revised `.aux` and PDF. All five public
DOIs remain visible; C421 remains local and unpublished.

Round 1's targeted primary-source retrievals and the manuscript's
source receipt were reread as their actual historical evidence. No new
web search or source retrieval is claimed in this text-only correction
pass, and no old full-source read is relabelled fresh. SOURCE_AUDIT and
BUILD_REPORT were rehashed to their unchanged recorded values. The
original proof, original audit and earlier proof-review hashes were
also checked unchanged; those historical documents were not edited or
used as substitutes for this fresh full-manuscript inspection.

The actual revision transcript records three pdfLaTeX passes and two
BibTeX passes ending with the 12-page 378223-byte PDF and latexmk's
completed-target message. Final engine and bibliography logs have no
Warning/Error/Overfull/Underfull/undefined match. No unresolved marker
was found in current source or extracted text. All 23 font resources
are embedded Type 1 with Unicode maps. The PDF is anonymous, undated
in creation/modification metadata, unencrypted and has no JavaScript.
The full twelve-page view found no clipping, collisions, missing glyphs,
unreadable table cells or broken proof continuations. Pages 1--11 contain
the article and page 12 its complete references.

The historical one-failed/three-successful initial builds remain
explicitly distinguished from this one successful author revision build.
The old BUILD_REPORT's baseline wording is identified as historical
by the current ROUND1_HANDOFF and improvement log. This reviewer did
not run LaTeX. An initial diagnostic guessed `build_round1_01/main.txt`;
`rg --files` resolved the actual `pdf_text.txt`, subsequently read in
full and compared with fresh PDF extraction. This harmless lookup is
not a compile or mathematical failure.

## Action boundary and next gate

Only this assigned round-2 report was written. Manuscript inputs,
PDFs, author receipts, old proofs/certificates, shared registries and
Git were not modified. Mathematical programs, symbolic diagnostics,
finite-core enumeration, old-certificate reruns, reviewer LaTeX builds,
external uploads and external-model calls during this review: zero.

The `research-review` skill supplied claim/evidence and full-record
discipline; the authorized batch replaces its external-model and
ML-venue defaults with assigned current-team nonauthor review. No
further author revision is requested. The coordinator may adjudicate
and close this manuscript-review sequence, then perform the separately
required formal evaluation and final fresh deterministic build/release
checks. The author `pending_round2` files were intentionally left
untouched by this reviewer.
